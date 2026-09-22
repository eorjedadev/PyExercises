# Ejercicio 031 — Módulo de Pedidos (apps/orders) y Definición de Límites de Dominio

[← Ejercicio 030](../ejercicio_030/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 032 →](../ejercicio_032/README.md)

---

### Contexto de negocio

La plataforma va a iniciar el procesamiento de compras comerciales. El módulo de pedidos (`apps/orders`) debe nacer como una capacidad de negocio autónoma y altamente cohesiva. Debe colaborar con `apps/customers` (quién compra) y `apps/catalog` (qué se compra), pero sin acoplar sus estructuras ni permitir que otros módulos modifiquen el estado interno de las órdenes de manera indiscriminada.

### Estado actual del sistema

Módulos `apps/users`, `apps/catalog`, `apps/customers` y `apps/audit` operativos.

### Nueva necesidad

Crear el módulo `apps/orders`, modelar la entidad raíz de agregación `Order` y definir las interfaces públicas que expondrá este módulo hacia el resto del monolito.

### Objetivo

Diseñar los límites de dominio (Bounded Context) para el módulo de pedidos, identificando las responsabilidades que le pertenecen (cálculo de totales, estados de la orden, líneas de pedido) y las que pertenecen a otros módulos.

### Actor

Cliente Autenticado / Gestor de Pedidos autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Order` (`id` UUID, `order_number` VARCHAR único, `customer` FK, `status`, `currency`, `subtotal_amount`, `tax_amount`, `shipping_amount`, `total_amount`, `shipping_address_snapshot` JSONField, `created_at`, `updated_at`).

### Reglas de negocio

1. El `order_number` debe ser un código correlativo de negocio legible (ej. `ORD-2026-00001`).
2. El estado inicial de toda orden recién creada es `PENDING`.
3. La orden debe almacenar una 'foto inmutable' (snapshot) de la dirección de entrega en formato JSON para que si el cliente edita su dirección en `apps/customers` en el futuro, el pedido histórico no se altere.
4. Todos los importes monetarios deben ser de precisión fija `DecimalField(12, 2)`.

### Contrato esperado

Estructura del Recurso Order:
- `GET /api/v1/orders/{id}/`
  Response: `200 OK`
  ```json
  {
    "id": "uuid-orden",
    "order_number": "ORD-2026-00001",
    "status": "PENDING",
    "total_amount": "149.80",
    "currency": "USD",
    "created_at": "2026-09-22T12:00:00Z"
  }
  ```

### Persistencia

Tabla `orders_order` en PostgreSQL con restricciones `UNIQUE` sobre `order_number`.

### Relaciones

`Order.customer` -> `ForeignKey('customers.CustomerProfile', on_delete=models.PROTECT)`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Un cliente solo puede consultar sus propios pedidos; un operador con rol `ORDERS_OPERATOR` o `ADMIN` puede consultar cualquier pedido.

### Validaciones

Validar que el subtotal, impuestos y total sean coherentes (`total = subtotal + tax + shipping`).

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Generación concurrente de números de orden (debe evitarse colisión con secuencia o transacciones aisladas).

### Casos de error

`404 Not Found` al consultar una orden inexistente o que pertenece a otro cliente.

### Consideraciones de seguridad

Protección de Ownership en consultas de pedidos.

### Consideraciones de rendimiento

Índices en PostgreSQL sobre `(customer_id, status)` y `order_number`.

### Fundamentos de Python relacionados

Generación de correlativos formateados (`f'ORD-{year}-{seq:05d}'`), manipulación de decimales.

### Conceptos Django relacionados

`models.TextChoices` para estados, `models.PROTECT` en claves foráneas para evitar eliminación accidental de clientes con pedidos históricos.

### Conceptos DRF relacionados

Serializadores de salida de pedidos, control de permisos basados en rol y propietario.

### PostgreSQL

`CREATE TABLE orders_order (id UUID PRIMARY KEY, order_number VARCHAR(30) UNIQUE NOT NULL, ...)`.

### Arquitectura

Monolito Modular: `apps/orders` encapsula la lógica de compras sin invadir `apps/catalog` ni `apps/customers`.

### Dependencias entre módulos

`apps/orders` depende de `apps.customers` para vincular el perfil del comprador.

### Antes de programar

1. ¿Por qué la dirección de entrega debe guardarse como un snapshot JSON en el pedido en lugar de solo guardar la clave foránea a la dirección del cliente?
2. ¿Por qué `on_delete=models.PROTECT` es la única política aceptable para la relación entre un pedido y el cliente?

### Pruebas mínimas

1. Crear una orden mediante el ORM y verificar que persista con su número de orden único y estado `PENDING`.
2. Verificar que `order.customer` apunte al perfil del cliente.

### Pruebas negativas

1. Intentar eliminar el `CustomerProfile` asociado a una orden existente y comprobar que Django lance `ProtectedError`.
2. Intentar duplicar un `order_number` y verificar que PostgreSQL lance `IntegrityError`.

### Documentación

Documentar en el README del módulo `apps/orders` los estados de la orden y la política de snapshots inmutables.

### Explicación posterior

Explica el concepto de Bounded Context de Domain-Driven Design (DDD) aplicado a un monolito modular con Django.

### Aplicación profesional

Módulo central de comercio electrónico, facturación, órdenes de servicio y procesamiento de transacciones.

### Reto adicional

Implementar un generador de número de orden seguro basado en secuencias de base de datos de PostgreSQL.
