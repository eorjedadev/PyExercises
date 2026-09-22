# Ejercicio 036 — Coordinación Transaccional entre Orders e Inventory

[← Ejercicio 035](../ejercicio_035/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 037 →](../ejercicio_037/README.md)

---

### Contexto de negocio

Al crear un pedido en `apps/orders`, el sistema debe coordinar inmediatamente con `apps/inventory` para reservar o descontar el stock de cada producto. Si algún producto no tiene stock suficiente, la orden completa debe cancelarse y ningún stock debe modificarse. Ambos módulos deben coordinarse mediante una operación atómica limpia.

### Estado actual del sistema

Módulos `apps/orders` y `apps/inventory` implementados independientemente.

### Nueva necesidad

Integrar la llamada al servicio `inventory.services.reserve_stock_for_order(items=...)` dentro del flujo de `orders.services.create_order`, garantizando que si el inventario rechaza la reserva, la orden no se cree.

### Objetivo

Aprender la coordinación transaccional entre módulos dentro de un monolito modular, invocando servicios internos dentro de una transacción compartida y manejando excepciones de dominio limpiamente.

### Actor

Cliente Autenticado autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/orders` orquestando llamada a `apps/inventory`

### Entidades involucradas

`create_order` (`apps/orders/services.py`), `reserve_stock` (`apps/inventory/services.py`), `Order`, `StockItem`.

### Reglas de negocio

1. Antes de confirmar la orden, se debe reservar el stock solicitado en `apps/inventory`.
2. Si todos los ítems tienen existencias disponibles, el stock pasa a `quantity_reserved += quantity` y la orden se crea en estado `PENDING`.
3. Si un solo ítem no tiene stock suficiente, se lanza `InsufficientStockError`, la transacción se revierte por completo (`ROLLBACK`) y no se crea la orden ni se reserva nada.
4. La API debe responder `400 Bad Request` con el SKU y nombre del producto agotado.

### Contrato esperado

Respuesta ante falta de Stock:
- `POST /api/v1/orders/` (solicitando 5 unidades de un producto con solo 2 disponibles)
  Response: `400 Bad Request`
  ```json
  {
    "error": {
      "code": "OUT_OF_STOCK",
      "message": "Stock insuficiente para el producto 'Wireless Gaming Mouse'. Solicitado: 5, Disponible: 2.",
      "details": { "product_id": "uuid-prod-1", "available_stock": 2 }
    }
  }
  ```

### Persistencia

Transacción única en PostgreSQL que afecta a `orders_order`, `orders_orderitem`, `inventory_stockitem` y `inventory_stockmovement`.

### Relaciones

Interacción entre entidades de órdenes e inventario mediada por servicios.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación de stock disponible antes de la reserva.

### Transacciones

Transacción atómica global en `create_order` que engloba la operación de inventario.

### Casos límite

Compra con 10 productos donde el 10mo ítem falla por stock (los 9 anteriores deben liberarse automáticamente por el rollback).

### Casos de error

Excepción `InsufficientStockError` mapeada a código HTTP `400`.

### Consideraciones de seguridad

Garantizar que no se sobrevenda inventario (overselling).

### Consideraciones de rendimiento

Las operaciones dentro de la transacción deben ser rápidas para no retener bloqueos en base de datos.

### Fundamentos de Python relacionados

Propagación de excepciones personalizadas entre capas.

### Conceptos Django relacionados

`transaction.atomic`, manejo de excepciones de dominio en la capa HTTP.

### Conceptos DRF relacionados

Mapeo de excepciones en el custom exception handler.

### PostgreSQL

`BEGIN; INSERT INTO orders_order ...; UPDATE inventory_stockitem SET quantity_reserved = ...; COMMIT;`.

### Arquitectura

Llamada directa entre servicios de módulos internos: `orders.services` invoca la función pública `inventory.services.reserve_stock`.

### Dependencias entre módulos

`apps.orders.services` depende de `apps.inventory.services`. `apps.inventory` NO conoce a `apps.orders`.

### Antes de programar

1. ¿Por qué la dependencia unidireccional `orders -> inventory` es correcta y tener `inventory -> orders` crearía una dependencia circular destructiva?
2. ¿Qué ventaja ofrece que ambos módulos compartan el mismo motor de PostgreSQL en un monolito frente a una arquitectura de microservicios con dos bases de datos separadas?

### Pruebas mínimas

1. Crear stock de 10 unidades, crear orden de 3 unidades -> Verificar que la orden se cree y que `quantity_reserved` sea 3 y disponible sea 7.
2. Intentar crear orden de 8 unidades (supera los 7 disponibles) -> Verificar error `400` y comprobar que la orden no exista y el stock siga en reservado=3.

### Pruebas negativas

1. Solicitar compra de un producto con stock 0 y comprobar rechazo inmediato sin filas huérfanas en ninguna tabla.

### Documentación

Documentar el diagrama de secuencia de creación de orden con reserva de stock en la carpeta `diagramas/`.

### Explicación posterior

Explica cómo el Monolito Modular simplifica la consistencia transaccional (ACID local) en comparación con el patrón Saga o transacciones distribuidas requeridas en microservicios.

### Aplicación profesional

Flujo troncal de plataformas de e-commerce de alto rendimiento.

### Reto adicional

Implementar la liberación automática de stock reservado si la orden es cancelada posteriormente.
