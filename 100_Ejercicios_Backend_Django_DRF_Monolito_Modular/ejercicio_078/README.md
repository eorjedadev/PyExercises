# Ejercicio 078 — Coordinación Multi-Módulo: Devoluciones -> Inventario + Pagos + Notificaciones

[← Ejercicio 077](../ejercicio_077/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 079 →](../ejercicio_079/README.md)

---

### Contexto de negocio

Cuando un Operador de Calidad aprueba e inspecciona una devolución (`POST /api/v1/returns/{id}/approve/`), el sistema debe desencadenar una coreografía multi-módulo coordinada: 1) En `apps/inventory`, reingresar los productos aptos al stock disponible (`INFLOW`). 2) En `apps/payments`, procesar el reembolso del dinero (`refund`) a la tarjeta del cliente mediante la pasarela. 3) En `apps/notifications`, enviar un correo y aviso in-app al cliente informando la acreditación de su reembolso.

### Estado actual del sistema

Módulo de devoluciones creado y conectado con órdenes.

### Nueva necesidad

Implementar el servicio `returns.services.approve_and_process_return(return_request_id, ...)` que orqueste de forma atómica y segura las llamadas a los servicios de inventario, pagos y notificaciones.

### Objetivo

Dominar la coordinación de flujos de negocio complejos que abarcan múltiples módulos en un monolito modular, manteniendo la consistencia de datos y el desacoplamiento mediante servicios públicos.

### Actor

Operador de Calidad / Auditor de Devoluciones

### Módulo responsable

`apps/returns` orquestando `inventory`, `payments`, `notifications`

### Entidades involucradas

`ReturnRequest`, `approve_and_process_return` (servicio), `inventory.services.adjust_stock`, `payments.services.refund_transaction`, `notifications.services.send_notification`.

### Reglas de negocio

1. Solo solicitudes en estado `REQUESTED` pueden ser aprobadas.
2. Si el producto devuelto está en buen estado, se suma al stock disponible en `apps/inventory` con motivo `'Reingreso por devolución aprobada'`.
3. Se invoca el reembolso en `apps/payments` por el monto correspondiente a los artículos devueltos.
4. La solicitud pasa a estado `COMPLETED` y se emite la notificación al cliente.
5. Si el reembolso en la pasarela falla por fondos o error de red, la transacción de base de datos debe manejar el error limpiamente.

### Contrato esperado

Aprobar Devolución (Operador):
- `POST /api/v1/returns/{id}/approve/`
  Header: `Authorization: Bearer <token_operador>`
  Body: `{"restock_items": true, "notes": "Producto recibido en caja original e impecable."}`
  Response: `200 OK`
  ```json
  {
    "id": "uuid-devolucion",
    "status": "COMPLETED",
    "refund_amount": "49.90",
    "refund_transaction_id": "uuid-tx-reembolso",
    "completed_at": "2026-09-22T20:00:00Z"
  }
  ```

### Persistencia

Actualización de `returns_returnrequest`, inserción en `inventory_stockmovement`, inserción en `payments_paymenttransaction` (tipo `REFUND`), inserción en `notifications_notification`.

### Relaciones

Interacción entre 4 módulos mediada exclusivamente por servicios.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar que la solicitud no haya sido procesada previamente.

### Transacciones

Transacción atómica para actualización de estados y reingreso de stock; llamada a pasarela manejada con resiliencia.

### Casos límite

El cliente devolvió un producto roto que no es apto para reventa (`restock_items = False`: se reembolsa el dinero pero NO se reingresa al inventario).

### Casos de error

`409 Conflict` si la devolución ya estaba completada o rechazada.

### Consideraciones de seguridad

Verificación estricta de permisos de operador para aprobar reembolsos financieros.

### Consideraciones de rendimiento

Liberación de hilos y notificación asíncrona tras el commit.

### Fundamentos de Python relacionados

Orquestación de servicios mediante composición de funciones.

### Conceptos Django relacionados

`transaction.atomic`, `transaction.on_commit` para el envío del correo de reembolso.

### Conceptos DRF relacionados

Endpoints de acción con autorización por rol.

### PostgreSQL

Actualizaciones atómicas en múltiples tablas del monolito.

### Arquitectura

El servicio orquestador reside en `apps/returns/services.py`, actuando como cliente de las interfaces públicas de los otros 3 módulos.

### Dependencias entre módulos

`apps.returns` depende de las interfaces públicas de `apps.inventory`, `apps.payments` y `apps.notifications`.

### Antes de programar

1. ¿Cómo garantiza el Monolito Modular que el reingreso de stock y el registro de la devolución ocurran en la misma base de datos sin necesidad de complejas transacciones distribuidas (2PC)?
2. ¿Por qué la llamada a la pasarela de pagos debe aislarse mediante el adaptador para que un fallo en red pueda reintentarse sin duplicar el reingreso de inventario?

### Pruebas mínimas

1. Aprobar una devolución con reingreso de stock -> Verificar que la solicitud pase a `COMPLETED`, el stock aumente en inventario, se registre el reembolso en pagos y se genere la notificación al usuario.
2. Verificar que la orden original mantenga su integridad histórica.

### Pruebas negativas

1. Intentar aprobar por segunda vez una devolución ya completada -> Verificar rechazo `409 Conflict`.

### Documentación

Documentar el diagrama de secuencia de aprobación de devoluciones en la carpeta `diagramas/`.

### Explicación posterior

Explica cómo el diseño modular permite orquestar flujos de negocio complejos manteniendo a cada módulo concentrado en sus propias invariantes.

### Aplicación profesional

Procesamiento integral de garantías, reembolsos bancarios y logística inversa en retail y comercio electrónico.

### Reto adicional

Agregar soporte para devoluciones parciales donde solo se reembolsa un subconjunto del pedido original recalculando impuestos proporcionalmente.
