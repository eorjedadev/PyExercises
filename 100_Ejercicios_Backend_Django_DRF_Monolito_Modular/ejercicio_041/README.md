# Ejercicio 041 — Módulo de Promociones (apps/promotions) y Validación de Cupones

[← Ejercicio 040](../ejercicio_040/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 042 →](../ejercicio_042/README.md)

---

### Contexto de negocio

El equipo de marketing necesita aplicar códigos promocionales y cupones de descuento a las compras. Un cupón puede ofrecer un porcentaje de descuento (ej. 15%) o un monto fijo (ej. $20.00), con reglas de fecha de validez (desde/hasta), monto mínimo de compra, límite de usos totales y límite de un uso por cliente.

### Estado actual del sistema

Módulos de catálogo, clientes, órdenes e inventario operativos.

### Nueva necesidad

Crear el módulo `apps/promotions`, modelar `Coupon` y `CouponUsage`, e implementar la interfaz de validación y aplicación de cupones durante la creación del pedido en `apps/orders`.

### Objetivo

Diseñar un módulo de promociones desacoplado, modelando reglas complejas de negocio con fechas, límites de uso por usuario y cálculo exacto de descuentos.

### Actor

Cliente que aplica un cupón en su compra

### Módulo responsable

`apps/promotions` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Coupon` (`id` UUID, `code` VARCHAR unique, `discount_type`, `discount_value`, `min_order_amount`, `max_uses`, `current_uses`, `valid_from`, `valid_until`, `is_active`), `CouponUsage` (`id` UUID, `coupon` FK, `customer` FK, `order_id` UUID, `used_at`), servicio `validate_and_apply_coupon`.

### Reglas de negocio

1. El código de cupón no distingue mayúsculas/minúsculas (ej. `VERANO2026` es igual a `verano2026`).
2. El cupón debe estar activo y la fecha actual debe estar dentro del rango `[valid_from, valid_until]`.
3. El subtotal del pedido debe ser mayor o igual a `min_order_amount`.
4. `current_uses` no puede superar `max_uses`.
5. El cliente no debe haber utilizado el mismo cupón en una compra previa (`CouponUsage`).
6. El descuento no puede exceder el subtotal del pedido (el total nunca puede ser negativo).

### Contrato esperado

Crear Pedido con Cupón:
- `POST /api/v1/orders/`
  Body:
  ```json
  {
    "shipping_address_id": "uuid-dir",
    "coupon_code": "DESCUENTO15",
    "items": [ ... ]
  }
  ```
  Response: `201 Created` con desglose: `"subtotal": "100.00", "discount_amount": "15.00", "total_amount": "85.00"`

### Persistencia

Tablas `promotions_coupon` y `promotions_couponusage` en PostgreSQL.

### Relaciones

`CouponUsage.coupon` -> `ForeignKey(Coupon)`; `CouponUsage.customer` -> `ForeignKey('customers.CustomerProfile')`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación de vigencia temporal, montos mínimos y unicidad de uso por usuario.

### Transacciones

Transacción atómica: crear orden + incrementar `current_uses` en cupón + registrar `CouponUsage`.

### Casos límite

Cupón que vence en el segundo exacto en que se procesa la compra; dos compras simultáneas usando el último cupón disponible (`select_for_update` en `Coupon`).

### Casos de error

`400 Bad Request` si el cupón está vencido, no alcanza el monto mínimo o ya fue usado por el cliente.

### Consideraciones de seguridad

Protección de concurrencia en cupones con límite estricto de usos.

### Consideraciones de rendimiento

Índice único sobre `code` en mayúsculas en `Coupon` e índice compuesto sobre `(coupon_id, customer_id)` en `CouponUsage`.

### Fundamentos de Python relacionados

Cálculo de porcentajes con `Decimal`, comparación de fechas con `django.utils.timezone.now()`.

### Conceptos Django relacionados

`models.CheckConstraint`, `timezone.now`, claves foráneas inter-módulo.

### Conceptos DRF relacionados

Serializadores de órdenes con campo opcional `coupon_code`.

### PostgreSQL

`CREATE UNIQUE INDEX unique_coupon_code ON promotions_coupon (UPPER(code));`.

### Arquitectura

`apps/promotions` encapsula el cálculo de descuentos. `apps/orders` invoca `promotions.services.apply_coupon`.

### Dependencias entre módulos

`apps.orders.services` depende de `apps.promotions.services`.

### Antes de programar

1. ¿Por qué es vital almacenar el `discount_amount` exacto en la orden en lugar de solo recalcularlo en el futuro a partir del cupón?
2. ¿Por qué se debe usar `timezone.now()` de Django en lugar de `datetime.now()` de Python estándar?

### Pruebas mínimas

1. Crear un cupón de 20% de descuento con mínimo $50, aplicar a una orden de $100 -> Verificar descuento de $20.00 y total de $80.00.
2. Verificar que se cree el registro en `CouponUsage` y que `current_uses` se incremente en 1.

### Pruebas negativas

1. Intentar usar un cupón expirado -> Verificar rechazo `400 Bad Request`.
2. Intentar usar el mismo cupón por segunda vez con el mismo usuario -> Verificar rechazo por cupón ya utilizado.

### Documentación

Documentar el ciclo de vida y validaciones de cupones en el README de `apps/promotions`.

### Explicación posterior

Explica cómo el uso de una tabla de auditoría de usos (`CouponUsage`) garantiza que las restricciones por usuario se apliquen con consistencia relacional en PostgreSQL.

### Aplicación profesional

Sistemas de fidelización, campañas de marketing digital, cupones de bienvenida y descuentos por volumen.

### Reto adicional

Agregar soporte para cupones aplicables únicamente a una categoría específica de productos del catálogo.
