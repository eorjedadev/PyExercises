# Ejercicio 077 — Módulo de Devoluciones y Reembolsos (apps/returns)

[← Ejercicio 076](../ejercicio_076/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 078 →](../ejercicio_078/README.md)

---

### Contexto de negocio

Los clientes que hayan recibido un pedido (`DELIVERED`) tienen derecho a solicitar la devolución parcial o total de artículos dentro de los 30 días posteriores a la entrega. El nuevo requerimiento exige crear el módulo de devoluciones (`apps/returns`), modelar el ciclo de vida de una solicitud de devolución (`ReturnRequest`) y gestionar las etapas de inspección, aprobación y rechazo.

### Estado actual del sistema

Módulos de catálogo, clientes, órdenes, inventario, pagos y envíos operativos.

### Nueva necesidad

Crear el módulo `apps/returns`, modelar `ReturnRequest` y `ReturnItem`, y exponer el endpoint `POST /api/v1/returns/` para que los clientes soliciten la devolución de ítems específicos de una orden entregada con motivo y evidencia.

### Objetivo

Diseñar un nuevo módulo de negocio sobre un monolito modular existente, respetando los límites de los módulos previos e implementando el ciclo de vida de devoluciones.

### Actor

Cliente Autenticado (Solicitante) / Operador de Calidad (Aprobador)

### Módulo responsable

`apps/returns` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`ReturnRequest` (`id` UUID, `order_id` UUID, `customer_id` UUID, `status`, `reason`, `refund_amount`, `requested_at`, `inspected_at`), `ReturnItem` (`id` UUID, `return_request` FK, `order_item_id` UUID, `quantity`, `condition_notes`).

### Reglas de negocio

1. Solo se pueden solicitar devoluciones para órdenes en estado `DELIVERED` cuya fecha de entrega no supere los 30 días de antigüedad.
2. La cantidad a devolver de cada ítem no puede superar la cantidad comprada originalmente en el pedido.
3. Los estados de una solicitud de devolución son: `REQUESTED`, `APPROVED`, `REJECTED`, `COMPLETED`.
4. El cliente debe especificar el motivo (`DEFECTIVE_PRODUCT`, `WRONG_ITEM`, `BUYER_REMORSE`) y una descripción.

### Contrato esperado

Solicitar Devolución:
- `POST /api/v1/returns/`
  Header: `Authorization: Bearer <token>`
  Body:
  ```json
  {
    "order_id": "uuid-orden-entregada",
    "reason": "DEFECTIVE_PRODUCT",
    "notes": "El mouse no enciende el sensor óptico.",
    "items": [
      { "order_item_id": "uuid-order-item", "quantity": 1 }
    ]
  }
  ```
  Response: `201 Created` `{ "id": "uuid-devolucion", "status": "REQUESTED", ... }`

### Persistencia

Tablas `returns_returnrequest` y `returns_returnitem` en PostgreSQL.

### Relaciones

`ReturnRequest` referencia `order_id` y `customer_id` como UUIDs; `ReturnItem` vinculado a `ReturnRequest`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Solo el cliente propietario del pedido original puede solicitar la devolución.

### Validaciones

Validar que la orden esté en `DELIVERED`, dentro de los 30 días, y que las cantidades no excedan lo comprado.

### Transacciones

Transacción atómica al crear la solicitud y sus ítems.

### Casos límite

Cliente intentando solicitar dos devoluciones simultáneas para el mismo ítem superando la cantidad comprada.

### Casos de error

`400 Bad Request` si la orden no está entregada, superó los 30 días o los ítems no coinciden.

### Consideraciones de seguridad

Verificación de propiedad y reglas temporales.

### Consideraciones de rendimiento

Índices en PostgreSQL sobre `order_id` y `customer_id` en `returns_returnrequest`.

### Fundamentos de Python relacionados

Cálculo de diferencias de fechas (`timezone.now() - order.delivered_at <= timedelta(days=30)`).

### Conceptos Django relacionados

Modelado de relaciones maestro-detalle con `ForeignKey`.

### Conceptos DRF relacionados

Serializadores de solicitud de devolución con validación cruzada entre módulos.

### PostgreSQL

`CREATE TABLE returns_returnrequest (id UUID PRIMARY KEY, order_id UUID NOT NULL, status VARCHAR(30) NOT NULL, ...)`.

### Arquitectura

`apps/returns` nace como un módulo autónomo que colabora con `apps/orders` mediante interfaces públicas.

### Dependencias entre módulos

`apps.returns.services` consulta `apps.orders.selectors` para validar la elegibilidad de la orden.

### Antes de programar

1. ¿Por qué la lógica de devoluciones debe ser un módulo separado (`apps/returns`) en lugar de añadir 15 campos nuevos al modelo `Order`?
2. ¿Cómo se valida la regla de los 30 días de garantía sin acoplar la base de datos de órdenes a la de devoluciones?

### Pruebas mínimas

1. Crear una orden entregada hace 5 días, solicitar devolución de 1 ítem -> Verificar `201 Created` y estado `REQUESTED`.
2. Intentar solicitar devolución de una orden entregada hace 40 días -> Verificar rechazo `400 Bad Request` por plazo vencido.

### Pruebas negativas

1. Intentar devolver 5 unidades de un producto cuando el cliente solo compró 2 unidades -> Verificar rechazo de validación `400`.

### Documentación

Documentar las políticas de devolución y los endpoints en el README de `apps/returns`.

### Explicación posterior

Explica el principio de Responsabilidad Única a nivel de módulos: `apps/orders` se encarga de procesar ventas, `apps/returns` se encarga de revertir ventas.

### Aplicación profesional

Módulo esencial en plataformas de comercio electrónico, retail y distribución física (Reverse Logistics).

### Reto adicional

Agregar soporte para adjuntar fotografías de evidencia del producto defectuoso utilizando el módulo de archivos de `apps/billing`.
