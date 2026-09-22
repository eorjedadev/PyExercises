# Ejercicio 032 — Modelado de Líneas de Pedido e Inmutabilidad de Precios Históricos

[← Ejercicio 031](../ejercicio_031/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 033 →](../ejercicio_033/README.md)

---

### Contexto de negocio

Un pedido se compone de una o más líneas de detalle (`OrderItem`). Si un producto del catálogo cambia de precio mañana (ej. de $50 a $80), los pedidos realizados hoy deben seguir reflejando estrictamente el precio unitario al que fueron comprados ($50). Los precios y nombres en las líneas de pedido deben ser inmutables.

### Estado actual del sistema

Modelo `Order` creado en `apps/orders`. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Crear el modelo `OrderItem`, relacionarlo con `Order` y `Product`, copiando el nombre del producto, SKU y precio unitario en el momento exacto de la compra.

### Objetivo

Garantizar la inmutabilidad histórica de transacciones comerciales, modelando entidades de detalle (`OrderItem`) y evitando que cambios futuros en el catálogo alteren registros contables pasados.

### Actor

Sistema de Pedidos ejecutando procesos internos de dominio o tareas programadas de fondo.

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`OrderItem` (`id` UUID, `order` FK, `product` FK nullable/protect, `product_name_snapshot`, `product_sku_snapshot`, `unit_price`, `quantity`, `line_total`), `Order`.

### Reglas de negocio

1. La cantidad debe ser un entero estrictamente mayor a cero (`quantity >= 1`).
2. `unit_price` debe capturar el precio del producto al momento de crear el ítem.
3. `line_total` se calcula como `unit_price * quantity`.
4. Si un producto es desactivado o eliminado del catálogo en el futuro, el `OrderItem` debe conservar el snapshot del nombre, SKU y precio (`on_delete=models.SET_NULL` o `PROTECT`).

### Contrato esperado

Detalle de Orden con Ítems:
- `GET /api/v1/orders/{id}/`
  Response incluye:
  ```json
  "items": [
    {
      "id": "uuid-item-1",
      "sku": "TECH-MOU-001",
      "product_name": "Wireless Gaming Mouse",
      "unit_price": "49.90",
      "quantity": 2,
      "line_total": "99.80"
    }
  ]
  ```

### Persistencia

Tabla `orders_orderitem` en PostgreSQL con restricción `CHECK (quantity > 0)` y `CHECK (unit_price >= 0)`.

### Relaciones

`OrderItem.order` -> `ForeignKey(Order, on_delete=models.CASCADE, related_name='items')`; `OrderItem.product` -> `ForeignKey('catalog.Product', on_delete=models.PROTECT)`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Acceso controlado por el propietario de la orden o personal autorizado.

### Validaciones

Validar que `quantity` sea positivo y que el cálculo `line_total == unit_price * quantity` sea exacto.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

El producto del catálogo cambia de precio 5 segundos después de que el usuario creó la orden (el precio en la orden debe mantenerse intacto).

### Casos de error

`400 Bad Request` si la cantidad es menor a 1.

### Consideraciones de seguridad

No permitir que el cliente envíe el `unit_price` en el request de compra; el precio debe ser consultado por el backend desde el catálogo oficial.

### Consideraciones de rendimiento

Uso de `prefetch_related('items')` al consultar órdenes para evitar N+1 queries al serializar las líneas de detalle.

### Fundamentos de Python relacionados

Multiplicación de `Decimal` por `int`, propiedades computadas (`@property`).

### Conceptos Django relacionados

`related_name='items'`, `models.CheckConstraint`, serializadores anidados para lectura de relaciones 1 a N.

### Conceptos DRF relacionados

`OrderItemOutputSerializer` anidado dentro de `OrderDetailOutputSerializer`.

### PostgreSQL

`CREATE TABLE orders_orderitem (id UUID PRIMARY KEY, order_id UUID NOT NULL REFERENCES orders_order(id) ON DELETE CASCADE, ...)`.

### Arquitectura

`apps/orders` posee el modelo `OrderItem`. Copia datos esenciales de `apps/catalog` para lograr desacoplamiento temporal.

### Dependencias entre módulos

`apps/orders` referencia `Product` en la clave foránea pero no depende de la lógica interna de `apps/catalog`.

### Antes de programar

1. ¿Por qué es una vulnerabilidad crítica permitir que el cliente HTTP envíe el `unit_price` en el payload de creación del pedido?
2. ¿Qué ocurriría con los reportes contables anuales si las líneas de pedido leyeran el precio directamente mediante `item.product.price_amount` en lugar de guardar su propio `unit_price` histórico?

### Pruebas mínimas

1. Crear un producto con precio $50.00, crear una orden con 2 unidades de ese producto -> Verificar que `item.unit_price` sea $50.00 y `item.line_total` sea $100.00.
2. Modificar el precio del producto a $75.00 en el catálogo y volver a consultar la orden -> Verificar que `item.unit_price` siga siendo $50.00.

### Pruebas negativas

1. Intentar crear un `OrderItem` con cantidad 0 o negativa y verificar que PostgreSQL lance `IntegrityError` por el CheckConstraint.

### Documentación

Documentar la regla de inmutabilidad de precios en el diccionario de datos de `apps/orders`.

### Explicación posterior

Explica cómo el principio de 'Inmutabilidad de Hechos Pasados' (Past Facts) aplica al diseño de bases de datos relacionales para comercio y contabilidad.

### Aplicación profesional

Diseño de sistemas de facturación, carritos de compra, cotizaciones y órdenes de compra corporativas.

### Reto adicional

Agregar un método en el modelo `Order` que recalcule y valide la suma de todas sus líneas contra `subtotal_amount`.
