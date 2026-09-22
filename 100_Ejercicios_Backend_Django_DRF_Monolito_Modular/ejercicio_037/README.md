# Ejercicio 037 — Máquina de Estados del Pedido y Transiciones Válidas

[← Ejercicio 036](../ejercicio_036/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 038 →](../ejercicio_038/README.md)

---

### Contexto de negocio

Una orden de compra tiene un ciclo de vida estricto: `PENDING` -> `PAID` -> `PROCESSING` -> `SHIPPED` -> `DELIVERED`. Alternativamente, puede pasar a `CANCELLED` bajo condiciones específicas. Permitir que un cliente o un endpoint genérico `PATCH` cambie el estado de una orden arbitrariamente (ej. pasar de `DELIVERED` de vuelta a `PENDING`, o de `CANCELLED` a `PAID`) destruiría la coherencia del negocio.

### Estado actual del sistema

Creación de órdenes y reserva de stock operativas.

### Nueva necesidad

Implementar una Máquina de Estados Finita (FSM) para `Order.status`, centralizando las reglas de transición válidas y prohibiendo mutaciones de estado no autorizadas.

### Objetivo

Modelar el ciclo de vida de entidades con máquinas de estados en Django/Python, validando transiciones permitidas y bloqueando transiciones ilegales con excepciones de dominio.

### Actor

Cliente, Operador Logístico, Sistema de Pagos

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Order`, Enum de estados `OrderStatus`, excepciones `InvalidStateTransitionError`, servicio `transition_order_status`.

### Reglas de negocio

1. Transiciones válidas:
   - `PENDING` -> `PAID` o `CANCELLED`
   - `PAID` -> `PROCESSING` o `CANCELLED` (con reembolso)
   - `PROCESSING` -> `SHIPPED`
   - `SHIPPED` -> `DELIVERED`
   - `DELIVERED` -> (Estado final inmutable)
   - `CANCELLED` -> (Estado final inmutable)
2. Cualquier intento de transición no permitida debe lanzar `InvalidStateTransitionError`.
3. El campo `status` no debe ser editable directamente mediante un `PATCH` genérico de DRF.

### Contrato esperado

Intento de Transición Inválida:
- Intento de pasar orden de `DELIVERED` a `PENDING`
  Response: `409 Conflict` (o `400 Bad Request`)
  ```json
  {
    "error": {
      "code": "INVALID_STATE_TRANSITION",
      "message": "No se puede transicionar el pedido del estado 'DELIVERED' al estado 'PENDING'."
    }
  }
  ```

### Persistencia

Actualización de columna `status` en `orders_order`.

### Relaciones

`Order`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Verificación de permisos según la transición solicitada.

### Validaciones

Validación contra el grafo de transiciones permitidas del modelo.

### Transacciones

Transacción atómica durante cada cambio de estado.

### Casos límite

Intentar transicionar una orden al mismo estado en que ya se encuentra (idempotencia o no-op).

### Casos de error

`409 Conflict` ante transiciones de estado incompatibles.

### Consideraciones de seguridad

No exponer el campo `status` como editable en los serializers de actualización de la orden.

### Consideraciones de rendimiento

Actualizaciones simples de columna en base de datos.

### Fundamentos de Python relacionados

Diccionarios o grafos de transición en Python (`ALLOWED_TRANSITIONS = { OrderStatus.PENDING: {OrderStatus.PAID, OrderStatus.CANCELLED}, ... }`).

### Conceptos Django relacionados

`models.TextChoices`, encapsulamiento de lógica en servicios de dominio.

### Conceptos DRF relacionados

Deshabilitar actualización directa de campos de estado en serializers.

### PostgreSQL

`UPDATE orders_order SET status = 'PAID', updated_at = NOW() WHERE id = ...`.

### Arquitectura

La máquina de estados reside en `apps/orders/models.py` o `apps/orders/services.py`, gobernando el ciclo de vida del pedido.

### Dependencias entre módulos

Interno a `apps/orders`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué exponer `status` en un `ModelSerializer` con `fields = '__all__'` permite que cualquier atacante marque su pedido como `PAID` sin haber pagado?
2. ¿Qué ventajas ofrece centralizar el grafo de transiciones en un solo lugar del código?

### Pruebas mínimas

1. Probar la secuencia válida `PENDING` -> `PAID` -> `PROCESSING` -> `SHIPPED` -> `DELIVERED` y verificar que cada paso actualice el estado correctamente.
2. Probar la cancelación desde `PENDING` -> `CANCELLED`.

### Pruebas negativas

1. Intentar transicionar una orden `CANCELLED` a `PAID` y verificar que lance `InvalidStateTransitionError`.
2. Intentar transicionar una orden `DELIVERED` a `CANCELLED` y comprobar rechazo.

### Documentación

Documentar el diagrama de estados del pedido en el README de `apps/orders`.

### Explicación posterior

Explica el patrón State Machine en arquitectura de software y por qué los cambios de estado deben representarse mediante verbos y endpoints de acción en lugar de CRUD genérico.

### Aplicación profesional

Sistemas de seguimiento de paquetería, procesamiento de reclamos de seguros, reservas hoteleras y flujos de aprobación.

### Reto adicional

Crear un método helper `order.can_transition_to(target_status: OrderStatus) -> bool` para consultar la viabilidad de una transición antes de ejecutarla.
