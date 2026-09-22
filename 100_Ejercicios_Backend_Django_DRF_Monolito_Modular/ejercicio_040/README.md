# Ejercicio 040 — Control de Concurrencia con Bloqueo Pesimista (select_for_update)

[← Ejercicio 039](../ejercicio_039/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 041 →](../ejercicio_041/README.md)

---

### Contexto de negocio

Durante un evento de alta demanda (ej. 'Black Friday' o lanzamiento de entradas limitadas), 100 usuarios intentan comprar simultáneamente el último producto disponible en inventario (`stock = 1`). Una implementación ingenua leerá `stock = 1` para todos los hilos al mismo tiempo (Race Condition / Condición de Carrera) y aprobará múltiples compras, generando sobreventa y pérdidas económicas. Se requiere implementar bloqueo pesimista en PostgreSQL mediante `select_for_update()`.

### Estado actual del sistema

Reserva de stock implementada con transacciones atómicas simples.

### Nueva necesidad

Modificar la consulta de reserva de stock en `apps/inventory/services.py` para utilizar `StockItem.objects.select_for_update().get(...)` dentro del bloque `transaction.atomic()`.

### Objetivo

Dominar el control de concurrencia pesimista en bases de datos relacionales con Django y PostgreSQL (`SELECT ... FOR UPDATE`), comprendiendo los bloqueos de fila (Row-Level Locking), contención y prevención de Race Conditions.

### Actor

Múltiples Clientes concurrentes autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/inventory` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`StockItem`, `select_for_update`, `transaction.atomic`.

### Reglas de negocio

1. Al consultar el `StockItem` para verificar y descontar stock, la fila en PostgreSQL debe ser bloqueada exclusivamente para la transacción actual (`SELECT ... FOR UPDATE`).
2. Las transacciones concurrentes sobre el mismo producto deben esperar su turno en la cola de la base de datos hasta que la primera confirme (`COMMIT`) o cancele (`ROLLBACK`).
3. La segunda transacción leerá el stock actualizado (0) y rechazará la compra limpiamente con `InsufficientStockError` sin permitir sobreventa.
4. El bloqueo debe liberarse inmediatamente al finalizar la transacción.

### Contrato esperado

Garantía de consistencia absoluta: si hay 1 unidad en stock y 5 peticiones simultáneas, exactamente 1 petición recibe `201 Created` y las otras 4 reciben `400 Bad Request`.

### Persistencia

Cláusula `SELECT ... FROM inventory_stockitem WHERE product_id = ... FOR UPDATE` en PostgreSQL.

### Relaciones

`StockItem`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

`transaction.atomic()` es OBLIGATORIO para que `select_for_update()` tenga efecto en PostgreSQL.

### Casos límite

Bloqueos mutuos (Deadlocks) si múltiples transacciones bloquean múltiples recursos en diferente orden (debe asegurarse un orden de bloqueo determinista por `product_id`).

### Casos de error

`400 Bad Request` por falta de stock para las peticiones que llegaron milisegundos después.

### Consideraciones de seguridad

Protección de la integridad financiera contra fraudes por concurrencia.

### Consideraciones de rendimiento

`select_for_update` introduce contención deliberada en filas calientes; mantener las transacciones ultracortas.

### Fundamentos de Python relacionados

Programación multihilo / concurrente para pruebas de estrés (`concurrent.futures.ThreadPoolExecutor`).

### Conceptos Django relacionados

`QuerySet.select_for_update(nowait=False, skip_locked=False, of=())`, requerimiento de `transaction.atomic`.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`SELECT * FROM inventory_stockitem WHERE id = ... FOR UPDATE;` (Row Exclusive Lock).

### Arquitectura

El control de concurrencia reside en el servicio de inventario en `apps/inventory/services.py`.

### Dependencias entre módulos

Interno a `apps/inventory`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué `select_for_update()` no tiene ningún efecto si se ejecuta fuera de un bloque `transaction.atomic()`?
2. ¿Qué es un Deadlock (interbloqueo) en PostgreSQL y cómo se previene ordenando los IDs de productos antes de bloquearlos (`product_ids.sort()`)?

### Pruebas mínimas

1. Escribir una prueba de concurrencia usando `ThreadPoolExecutor` con 10 hilos simultáneos intentando comprar 1 solo producto disponible en base de datos PostgreSQL real.
2. Verificar que exactamente 1 hilo tenga éxito y 9 hilos reciban `InsufficientStockError`, y que el stock final sea exactamente 0 (cero sobreventas).

### Pruebas negativas

1. Verificar que no queden bloqueos colgados en la base de datos si un hilo lanza una excepción inesperada.

### Documentación

Documentar la estrategia de bloqueo de concurrencia y prevención de deadlocks en el README de inventario.

### Explicación posterior

Explica la diferencia entre Concurrencia Pesimista (`select_for_update`) y Concurrencia Optimista (control por versión / timestamp), y cuándo elegir cada una.

### Aplicación profesional

Sistemas de venta de entradas de conciertos (Ticketing), subastas, transferencias bancarias y reservas de vuelos.

### Reto adicional

Investigar y probar el parámetro `nowait=True` o `skip_locked=True` para colas de procesamiento de trabajos.
