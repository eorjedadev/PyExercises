# Ejercicio 035 — Módulo de Inventario (apps/inventory) y Movimientos de Almacén

[← Ejercicio 034](../ejercicio_034/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 036 →](../ejercicio_036/README.md)

---

### Contexto de negocio

El catálogo define los productos comerciales, pero las existencias físicas pertenecen a otra capacidad: la gestión de inventario (`apps/inventory`). El negocio necesita controlar el stock disponible, stock reservado y un historial inmutable de movimientos de almacén (entradas por compra a proveedores, salidas por venta, ajustes por merma o inventario físico).

### Estado actual del sistema

Módulos de catálogo, clientes y órdenes operativos.

### Nueva necesidad

Crear el módulo `apps/inventory`, modelar la entidad `StockItem` (inventario actual por producto) y `StockMovement` (bitácora inmutable de entradas y salidas), y exponer el servicio de ajuste de inventario.

### Objetivo

Diseñar el dominio de inventario en una arquitectura modular, manteniendo la separación entre catálogo (datos del producto) e inventario (existencias físicas y movimientos).

### Actor

Operador de Almacén / Gestor de Inventario

### Módulo responsable

`apps/inventory` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`StockItem` (`id` UUID, `product_id` UUID unique, `quantity_on_hand`, `quantity_reserved`, `updated_at`), `StockMovement` (`id` UUID, `stock_item` FK, `movement_type`, `quantity_delta`, `reason`, `reference_id`, `created_at`).

### Reglas de negocio

1. Cada producto tiene exactamente un `StockItem`.
2. El stock disponible calculable es `quantity_on_hand - quantity_reserved`.
3. El campo `quantity_on_hand` nunca puede ser negativo (`CheckConstraint(quantity_on_hand >= 0)`).
4. Cada cambio en el stock físico DEBE registrar obligatoriamente una fila en `StockMovement` con la cantidad modificada (`quantity_delta`), el tipo (`INFLOW`, `OUTFLOW`, `RESERVATION`, `ADJUSTMENT`) y el motivo.

### Contrato esperado

Ajustar Inventario Manualmente:
- `POST /api/v1/inventory/adjust/`
  Body:
  ```json
  {
    "product_id": "uuid-producto",
    "quantity_delta": 50,
    "movement_type": "INFLOW",
    "reason": "Llegada de lote de proveedor PO-2026-99"
  }
  ```
  Response: `200 OK` `{ "product_id": "...", "quantity_on_hand": 50, "available": 50 }`

### Persistencia

Tablas `inventory_stockitem` y `inventory_stockmovement` en PostgreSQL.

### Relaciones

`StockItem` referencia `product_id` como UUID sin clave foránea dura directa si se prefiere bajo acoplamiento, o FK protegida; `StockMovement` tiene FK a `StockItem`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar que un ajuste no resulte en stock negativo.

### Transacciones

Transacción atómica obligatoria: actualizar `StockItem` + insertar `StockMovement`.

### Casos límite

Ajuste negativo mayor a las existencias disponibles (debe ser rechazado con error de dominio `InsufficientStockError`).

### Casos de error

`400 Bad Request` si la operación viola el balance de existencias.

### Consideraciones de seguridad

Trazabilidad total: no permitir modificaciones directas del campo `quantity_on_hand` sin pasar por el servicio que genera el `StockMovement`.

### Consideraciones de rendimiento

Índice único sobre `product_id` en `StockItem` e índice sobre `(stock_item_id, created_at)` en `StockMovement`.

### Fundamentos de Python relacionados

Operaciones aritméticas con signos, tipos de movimiento con `TextChoices`.

### Conceptos Django relacionados

`models.CheckConstraint(check=Q(quantity_on_hand__gte=0))`, servicios de dominio con transacciones.

### Conceptos DRF relacionados

Serializadores de ajuste de inventario y vistas de administración.

### PostgreSQL

`UPDATE inventory_stockitem SET quantity_on_hand = quantity_on_hand + 50 WHERE product_id = ...; INSERT INTO inventory_stockmovement ...;`.

### Arquitectura

`apps/inventory` es el único módulo autorizado para modificar el stock de los productos.

### Dependencias entre módulos

`apps/inventory` solo conoce el identificador `product_id`.

### Antes de programar

1. ¿Por qué es una mala práctica agregar simplemente un campo `stock` en el modelo `Product` de catálogo en lugar de tener un módulo de inventario dedicado?
2. ¿Por qué toda modificación de stock debe dejar una fila en la tabla de movimientos (Ledger de inventario)?

### Pruebas mínimas

1. Crear un `StockItem` con 10 unidades, registrar una entrada de 15 unidades mediante el servicio -> Verificar que `quantity_on_hand` sea 25 y exista un movimiento `INFLOW` de +15.
2. Registrar una salida de 5 unidades -> Verificar que `quantity_on_hand` sea 20 y exista un movimiento `OUTFLOW` de -5.

### Pruebas negativas

1. Intentar restar 30 unidades a un stock de 20 -> Verificar que lance `InsufficientStockError` y que el stock permanezca en 20.

### Documentación

Documentar el modelo de ledger de inventario en el README de `apps/inventory`.

### Explicación posterior

Explica el patrón Ledger (Libro Mayor) aplicado al control de existencias y por qué el estado actual (`quantity_on_hand`) debe ser siempre igual a la suma histórica de todos sus movimientos.

### Aplicación profesional

Sistemas ERP, centros de distribución logística (WMS), tiendas físicas y bodegas de e-commerce.

### Reto adicional

Crear un comando de verificación `python manage.py audit_inventory_discrepancies` que compruebe que el `quantity_on_hand` de cada ítem coincida con la suma matemática de sus movimientos.
