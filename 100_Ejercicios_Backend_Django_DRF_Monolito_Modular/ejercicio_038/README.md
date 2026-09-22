# Ejercicio 038 — Endpoints de Acción de Negocio Específicos (POST /orders/{id}/cancel/)

[← Ejercicio 037](../ejercicio_037/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 039 →](../ejercicio_039/README.md)

---

### Contexto de negocio

En APIs REST profesionales, las operaciones de negocio que cambian el estado y desencadenan efectos secundarios no deben ocultarse detrás de un `PATCH` ambiguo. Se deben diseñar endpoints de acción explícitos como `POST /api/v1/orders/{id}/cancel/` y `POST /api/v1/orders/{id}/mark-as-shipped/` con semántica clara.

### Estado actual del sistema

Máquina de estados de pedidos implementada en `apps/orders`.

### Nueva necesidad

Crear el endpoint de acción `POST /api/v1/orders/{id}/cancel/`, que valide que el pedido esté en estado cancelable, libere el stock reservado en `apps/inventory` y registre el motivo de la cancelación.

### Objetivo

Diseñar e implementar endpoints de acción en DRF (`@action` en ViewSets o vistas dedicadas con `APIView`), comprendiendo cuándo apartarse del CRUD tradicional para modelar operaciones ricas del dominio.

### Actor

Cliente (cancelación por arrepentimiento) o Administrador (cancelación operativa)

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`OrderCancelAPIView` (o `@action(detail=True, methods=['post'])`), servicio `cancel_order`, `apps.inventory.services.release_reserved_stock`.

### Reglas de negocio

1. Un cliente solo puede cancelar su propio pedido si el estado es `PENDING`.
2. Un Administrador u Operador puede cancelar pedidos en estado `PENDING` o `PAID` indicando una justificación obligatoria (`cancellation_reason`).
3. Al cancelar, el servicio de órdenes debe invocar a `apps/inventory` para liberar el stock reservado de todos los ítems.
4. La orden pasa al estado `CANCELLED` y se responde `200 OK` con el resumen de la orden cancelada.

### Contrato esperado

Cancelar Pedido:
- `POST /api/v1/orders/{id}/cancel/`
  Header: `Authorization: Bearer <token>`
  Body: `{"reason": "El cliente solicitó cambio de modelo"}`
  Response: `200 OK`
  ```json
  {
    "id": "uuid-orden",
    "order_number": "ORD-2026-00001",
    "status": "CANCELLED",
    "cancellation_reason": "El cliente solicitó cambio de modelo",
    "updated_at": "2026-09-22T14:00:00Z"
  }
  ```

### Persistencia

Actualización de `orders_order` y decremento de `quantity_reserved` en `inventory_stockitem` con movimiento `RESERVATION_RELEASE`.

### Relaciones

`Order`, `OrderItem`, `StockItem`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Propietario del pedido (si está `PENDING`) o roles `ADMIN`/`ORDERS_OPERATOR`.

### Validaciones

Validar presencia de `reason` si es una cancelación administrativa.

### Transacciones

Transacción atómica que actualiza la orden y libera el inventario.

### Casos límite

Intentar cancelar una orden que ya fue enviada (`SHIPPED`) -> Rechazo.

### Casos de error

`409 Conflict` si el estado no permite cancelación; `403 Forbidden` si un cliente intenta cancelar una orden ajena o ya pagada.

### Consideraciones de seguridad

Verificación de permisos y propiedad antes de ejecutar la acción.

### Consideraciones de rendimiento

Operación rápida sobre claves primarias indexadas.

### Fundamentos de Python relacionados

Métodos de servicio con parámetros opcionales y control de flujo.

### Conceptos Django relacionados

Vistas de acción, integración con servicios transaccionales.

### Conceptos DRF relacionados

Uso de métodos POST para acciones de negocio en REST.

### PostgreSQL

`UPDATE orders_order SET status = 'CANCELLED' ...; UPDATE inventory_stockitem SET quantity_reserved = quantity_reserved - X ...;`.

### Arquitectura

El endpoint actúa como controlador HTTP delegando toda la lógica al servicio `orders.services.cancel_order`.

### Dependencias entre módulos

`apps/orders` invoca `apps.inventory.services.release_reserved_stock`.

### Antes de programar

1. ¿Por qué `POST /orders/{id}/cancel/` es más expresivo y seguro que un `PATCH /orders/{id}/` con `{"status": "CANCELLED"}`?
2. ¿Qué efectos secundarios deben revertirse al cancelar un pedido no pagado?

### Pruebas mínimas

1. Crear un pedido con 2 ítems (stock queda reservado), invocar `POST /orders/{id}/cancel/` -> Verificar que el pedido quede `CANCELLED` y que el stock reservado vuelva a 0 en inventario.
2. Verificar que la respuesta retorne status `200 OK`.

### Pruebas negativas

1. Intentar cancelar una orden que ya está en estado `DELIVERED` -> Verificar respuesta `409 Conflict` o `400 Bad Request`.
2. Usuario B intentando cancelar la orden del Usuario A -> Verificar `404/403`.

### Documentación

Documentar los endpoints de acción en la especificación OpenAPI de órdenes.

### Explicación posterior

Explica la diferencia entre CRUD anémico y modelos ricos en operaciones de dominio (Command Pattern en APIs REST).

### Aplicación profesional

Implementación de flujos de negocio complejos en logística, cancelaciones, devoluciones y pagos.

### Reto adicional

Implementar un segundo endpoint de acción `POST /api/v1/orders/{id}/mark-as-paid/` accesible solo por el sistema de pagos o administradores.
