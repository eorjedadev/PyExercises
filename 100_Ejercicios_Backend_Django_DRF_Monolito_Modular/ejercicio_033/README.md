# Ejercicio 033 — Interfaces Públicas entre Módulos y Creación de Pedidos

[← Ejercicio 032](../ejercicio_032/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 034 →](../ejercicio_034/README.md)

---

### Contexto de negocio

Para crear un pedido, el módulo `apps/orders` necesita obtener información de productos activos del catálogo. En lugar de permitir que `orders` haga consultas arbitrarias o manipule modelos de `catalog` directamente, `apps/catalog` debe exponer una interfaz pública clara (`selectors.get_active_products_by_ids`) y `apps/orders` debe exponer su servicio principal `orders.services.create_order`.

### Estado actual del sistema

Modelos `Order` y `OrderItem` listos en `apps/orders`; selectores listos en `apps/catalog`.

### Nueva necesidad

Implementar el endpoint `POST /api/v1/orders/` y el servicio `create_order(...)` que coordine la recepción de la lista de ítems solicitados, consulte el catálogo mediante la interfaz pública y genere la orden con sus líneas.

### Objetivo

Aprender a diseñar e invocar interfaces públicas entre módulos en una arquitectura monolítica modular, evitando acoplamiento espagueti y garantizando que los precios provengan siempre de la fuente de verdad del catálogo.

### Actor

Cliente Autenticado autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`create_order` (servicio en `apps/orders/services.py`), `OrderCreateInputSerializer`, `get_active_products_by_ids` (selector en `apps/catalog/selectors.py`).

### Reglas de negocio

1. El cliente envía únicamente la lista de ítems con `product_id` y `quantity`, además de la dirección de entrega elegida.
2. Todos los productos solicitados deben existir y estar en estado activo (`is_active=True`, `status=PUBLISHED`). Si alguno no está disponible, la operación se rechaza por completo.
3. El backend calcula automáticamente `unit_price`, `subtotal`, `tax` (ej. 18% o tasa aplicable) y `total_amount`.
4. La orden creada se devuelve con status `201 Created`.

### Contrato esperado

Crear Pedido:
- `POST /api/v1/orders/`
  Header: `Authorization: Bearer <token>`
  Request Body:
  ```json
  {
    "shipping_address_id": "uuid-direccion",
    "items": [
      { "product_id": "uuid-prod-1", "quantity": 2 },
      { "product_id": "uuid-prod-2", "quantity": 1 }
    ]
  }
  ```
  Response: `201 Created` con el detalle completo de la orden calculada.

### Persistencia

Inserción de 1 fila en `orders_order` y N filas en `orders_orderitem`.

### Relaciones

`Order`, `OrderItem`, `CustomerProfile`, `Product`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar que la lista `items` no esté vacía, cantidades positivas y que la dirección pertenezca al usuario autenticado.

### Transacciones

Garantizar que la cabecera y todas las líneas se inserten juntas.

### Casos límite

El cliente envía dos veces el mismo `product_id` en la lista de ítems (debe consolidarse la cantidad o rechazarse por duplicado).

### Casos de error

`400 Bad Request` si algún producto no existe o está inactivo; `404 Not Found` si la dirección no pertenece al cliente.

### Consideraciones de seguridad

Cálculo de precios realizado exclusivamente en el servidor; el cliente no puede alterar importes.

### Consideraciones de rendimiento

Consultar todos los productos necesarios en una sola consulta SQL usando `filter(id__in=product_ids)` en lugar de N consultas individuales.

### Fundamentos de Python relacionados

Mapeo de listas a diccionarios para búsquedas en memoria O(1) (`{p.id: p for p in products}`).

### Conceptos Django relacionados

Separación limpia de llamadas entre paquetes de aplicaciones (`apps.catalog.selectors`).

### Conceptos DRF relacionados

Serializadores con listas de objetos anidados (`ListSerializer`, `many=True`).

### PostgreSQL

`INSERT INTO orders_order ...; INSERT INTO orders_orderitem ...;`.

### Arquitectura

Contratos explícitos entre módulos: `apps/orders` consume la API interna de `apps/catalog`.

### Dependencias entre módulos

`apps/orders.services` importa funciones públicas de `apps.catalog.selectors` y `apps.customers.selectors`.

### Antes de programar

1. ¿Por qué es inaceptable hacer un bucle `for item in items: Product.objects.get(id=item.product_id)` dentro del servicio?
2. ¿Cómo evita la interfaz pública que cambios internos en el modelo `Product` rompan el servicio de `create_order`?

### Pruebas mínimas

1. Crear 2 productos activos, enviar petición de creación de orden con 2 líneas -> Verificar que la orden se cree con status `201` y los totales calculados correctamente.
2. Verificar que las líneas de pedido tengan los snapshots de nombre y SKU correctos.

### Pruebas negativas

1. Enviar una petición con un `product_id` inexistente -> Verificar que responda `400 Bad Request` con mensaje de producto no disponible.
2. Enviar una lista de `items` vacía `[]` -> Verificar rechazo `400`.

### Documentación

Documentar el flujo de creación de pedidos y las dependencias inter-módulos en `MAPA_ARQUITECTURA.md`.

### Explicación posterior

Explica cómo el uso de un diccionario `{p.id: p for p in products}` reduce la complejidad algorítmica de matching de O(N*M) a O(N+M) en la construcción de las líneas de orden.

### Aplicación profesional

Core de procesamiento de órdenes en cualquier arquitectura de comercio electrónico empresarial.

### Reto adicional

Implementar validación para consolidar automáticamente líneas con productos repetidos en el payload sumando sus cantidades.
