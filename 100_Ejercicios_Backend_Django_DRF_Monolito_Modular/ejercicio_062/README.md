# Ejercicio 062 — Optimización con select_related y Prefetch Personalizado

[← Ejercicio 061](../ejercicio_061/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 063 →](../ejercicio_063/README.md)

---

### Contexto de negocio

Una vez diagnosticado el problema N+1 en el listado de órdenes del ejercicio anterior, se requiere aplicar la optimización definitiva mediante el ORM de Django. La consulta debe reducirse de 151 queries a exactamente 2 o 3 queries SQL constantes, sin importar si se listan 10, 50 o 100 órdenes a la vez.

### Estado actual del sistema

Diagnóstico de N+1 completado en `apps/orders`.

### Nueva necesidad

Refactorizar la consulta en `apps/orders/selectors.py` aplicando `select_related('customer__user')` para relaciones 1 a 1 / ForeignKey directas, y `prefetch_related(Prefetch('items', queryset=...))` para la colección 1 a N de ítems con ordenamiento y filtros.

### Objetivo

Dominar el uso quirúrgico de `select_related` (SQL `INNER/LEFT JOIN`) y `prefetch_related` con objetos `Prefetch` avanzados en Django/DRF, reduciendo el número de consultas a O(1).

### Actor

Desarrollador Backend / Optimizador de Base de Datos

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Order`, `CustomerProfile`, `User`, `OrderItem`, `Prefetch`, selector `list_orders_optimized`.

### Reglas de negocio

1. Para traer la orden con el perfil del cliente y el usuario en una sola consulta SQL, se DEBE usar `select_related('customer__user')`.
2. Para traer las líneas de pedido (`items`), se DEBE usar `prefetch_related(Prefetch('items', queryset=OrderItem.objects.select_related('product')))`.
3. El número total de consultas SQL ejecutadas para listar N pedidos debe ser exactamente 2 o 3, independientemente de la cantidad de pedidos paginados.
4. Los datos devueltos por la API deben ser 100% idénticos a los del contrato original.

### Contrato esperado

Misma respuesta JSON original, pero con tiempo de respuesta reducido en más de un 90% (de 4,000 ms a < 80 ms).

### Persistencia

PostgreSQL ejecuta exactamente 1 `SELECT ... INNER JOIN customers_customerprofile ... INNER JOIN users_user ...` y 1 `SELECT ... FROM orders_orderitem WHERE order_id IN (...)`.

### Relaciones

`Order`, `CustomerProfile`, `User`, `OrderItem`, `Product`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Órdenes sin ítems o pedidos con relaciones nulas (los LEFT JOIN de `select_related` deben manejarlos limpiamente sin omitir registros).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

Optimización que protege contra caídas del servidor por sobrecarga de base de datos.

### Consideraciones de rendimiento

Reducción drástica del uso de CPU en PostgreSQL y eliminación del tiempo de espera de red.

### Fundamentos de Python relacionados

Construcción de queries compuestas en Python.

### Conceptos Django relacionados

`QuerySet.select_related()`, `QuerySet.prefetch_related()`, clase `django.db.models.Prefetch` con `to_attr` y `queryset` personalizado.

### Conceptos DRF relacionados

Integración de QuerySets pre-optimizados en vistas y ViewSets.

### PostgreSQL

`SELECT orders_order.id, ... FROM orders_order INNER JOIN customers_customerprofile ON ... INNER JOIN users_user ON ...; SELECT * FROM orders_orderitem WHERE order_id IN ('id1', 'id2', ...);`.

### Arquitectura

Toda la optimización relacional se encapsula dentro del selector en `apps/orders/selectors.py`.

### Dependencias entre módulos

Interno a `apps/orders` con joins hacia `customers` y `users`.

### Antes de programar

1. ¿Cuándo se debe usar `select_related` y por qué NO se puede usar para relaciones de tipo ManyToMany o ForeignKey inversa (1 a N)?
2. ¿Cómo funciona internamente `prefetch_related` de Django al ejecutar una segunda consulta con la cláusula `WHERE in (...)` y hacer el ensamblado en memoria de Python?

### Pruebas mínimas

1. Crear 50 órdenes con múltiples ítems en la base de datos de pruebas.
2. Ejecutar la vista optimizada dentro de `CaptureQueriesContext(connection) as ctx` y verificar mediante aserción estricta `assert len(ctx.captured_queries) <= 3`.
3. Verificar que la serialización de todos los campos sea completa y correcta.

### Pruebas negativas

1. Comprobar que al aumentar los registros de 10 a 100, el número de consultas capturadas se mantenga constante en <= 3 (complejidad O(1) verificada).

### Documentación

Documentar la optimización realizada y la comparación de benchmarks antes/después en el `README.md` de `apps/orders`.

### Explicación posterior

Explica cómo el objeto `Prefetch` permite filtrar y ordenar los registros relacionados antes del prefetch (ej. `Prefetch('items', queryset=OrderItem.objects.order_by('created_at'))`).

### Aplicación profesional

Regla fundamental de oro para todo desarrollador senior en Django: ninguna API de listado debe pasar a producción sin `select_related` y `prefetch_related` auditados.

### Reto adicional

Utilizar el argumento `to_attr='active_items'` en `Prefetch` para almacenar un subconjunto filtrado de elementos relacionados sin alterar la caché estándar de Django.
