# Ejercicio 055 — Módulo de Envíos y Logística (apps/shipping) y Asignación de Transportista

[← Ejercicio 054](../ejercicio_054/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 056 →](../ejercicio_056/README.md)

---

### Contexto de negocio

Una vez que una orden es pagada (`PAID`), entra al flujo de preparación y despacho logístico (`apps/shipping`). El equipo de almacén debe asignar una empresa de transporte (ej. DHL, FedEx, Courier Local), generar un código de seguimiento (Tracking Number) y registrar las etapas del envío (`LABEL_CREATED`, `PICKED_UP`, `IN_TRANSIT`, `OUT_FOR_DELIVERY`, `DELIVERED`).

### Estado actual del sistema

Módulos de órdenes, pagos y facturación operativos.

### Nueva necesidad

Crear el módulo `apps/shipping`, modelar `Shipment` y `Carrier`, exponer endpoints para que operadores asignen guías de envío y para que clientes consulten el rastreo de sus paquetes.

### Objetivo

Diseñar el dominio logístico en el monolito modular, modelando el ciclo de vida del despacho físico y su sincronización con el estado global de la orden.

### Actor

Operador Logístico / Cliente que rastrea su paquete

### Módulo responsable

`apps/shipping` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Carrier` (`id` UUID, `name`, `code`, `tracking_url_template`, `is_active`), `Shipment` (`id` UUID, `order_id` UUID, `carrier` FK, `tracking_number`, `status`, `shipped_at`, `delivered_at`, `notes`), servicio `create_shipment`.

### Reglas de negocio

1. Solo se pueden generar envíos para órdenes en estado `PAID` o `PROCESSING`.
2. El `tracking_number` debe ser único por transportista.
3. Al crear el envío en estado `IN_TRANSIT`, el servicio de logística debe invocar a `apps/orders` para transicionar la orden a `SHIPPED` y a `apps/notifications` para alertar al cliente con el enlace de rastreo.
4. Al marcarse como `DELIVERED`, la orden pasa a `DELIVERED`.

### Contrato esperado

1. Asignar Envío (Operador):
- `POST /api/v1/shipping/shipments/`
  Header: `Authorization: Bearer <token_operador>`
  Body: `{"order_id": "uuid-orden", "carrier_id": "uuid-carrier", "tracking_number": "TRK-987654321"}`
  Response: `201 Created`

2. Consultar Rastreo (Cliente):
- `GET /api/v1/shipping/track/{tracking_number}/`
  Response: `200 OK` `{ "carrier": "DHL Express", "status": "IN_TRANSIT", "tracking_url": "https://tracking.dhl.com/TRK-987654321" }`

### Persistencia

Tablas `shipping_carrier` y `shipping_shipment` en PostgreSQL.

### Relaciones

`Shipment.carrier` -> `ForeignKey(Carrier)`; `Shipment` referencia `order_id` como UUID.

### Autenticación

`IsAuthenticated` para crear envíos; el rastreo por tracking number puede ser público o de propietario.

### Autorización

Solo roles `ORDERS_OPERATOR` o `ADMIN` pueden crear/modificar envíos.

### Validaciones

Validar que la orden esté pagada y que el transportista esté activo.

### Transacciones

Transacción atómica: crear envío + actualizar orden a `SHIPPED` + encolar notificación.

### Casos límite

Intentar despachar una orden que aún no ha sido pagada (debe ser bloqueado por regla de negocio).

### Casos de error

`409 Conflict` si la orden no está en estado apto para envío; `400 Bad Request` si el tracking ya existe.

### Consideraciones de seguridad

Verificación de permisos de operador para la creación de envíos.

### Consideraciones de rendimiento

Índice único sobre `(carrier_id, tracking_number)` e índice sobre `order_id` en `Shipment`.

### Fundamentos de Python relacionados

Formateo de URLs dinámicas (`carrier.tracking_url_template.format(tracking_number=...)`).

### Conceptos Django relacionados

Relaciones entre módulos mediante servicios y eventos.

### Conceptos DRF relacionados

Serializadores de despacho y endpoints de rastreo público.

### PostgreSQL

`CREATE TABLE shipping_shipment (id UUID PRIMARY KEY, order_id UUID NOT NULL, tracking_number VARCHAR(100) NOT NULL, ...)`.

### Arquitectura

`apps/shipping` aísla toda la lógica de transportistas, guías y rastreo.

### Dependencias entre módulos

`apps.shipping.services` invoca `apps.orders.services.transition_order_status` y `apps.notifications.services.send_notification`.

### Antes de programar

1. ¿Por qué la gestión de transportistas y números de guía debe ser un módulo separado de `apps/orders`?
2. ¿Cómo se sincroniza el estado del envío con el estado general de la orden sin crear dependencias circulares?

### Pruebas mínimas

1. Crear una orden pagada, crear un envío asignándole transportista -> Verificar `201 Created` y que la orden cambie a estado `SHIPPED`.
2. Consultar el endpoint de rastreo con el tracking generado -> Verificar `200 OK` y URL de seguimiento construida.

### Pruebas negativas

1. Intentar crear un envío para una orden en estado `PENDING` (no pagada) -> Verificar rechazo `409 Conflict`.

### Documentación

Documentar el flujo de logística y las plantillas de URL de transportistas en el README de `apps/shipping`.

### Explicación posterior

Explica cómo la coordinación de estados entre dominios (Logística -> Órdenes) mantiene la cohesión interna y permite integrar múltiples couriers externos en el futuro.

### Aplicación profesional

Sistemas de fulfillment, integración con APIs de FedEx/DHL, plataformas de última milla y despachos de almacén.

### Reto adicional

Implementar soporte para múltiples bultos/paquetes asociados a una sola orden de compra.
