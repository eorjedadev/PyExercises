# Ejercicio 064 — Diseño Profesional de Índices en PostgreSQL (Compuestos y Parciales)

[← Ejercicio 063](../ejercicio_063/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 065 →](../ejercicio_065/README.md)

---

### Contexto de negocio

A medida que la tabla `catalog_products` alcanza cientos de miles de registros, las consultas frecuentes como filtrar por categoría y estado activo (`WHERE category_id = X AND is_active = true`), o buscar por SKU, comienzan a realizar escaneos secuenciales de tabla completa (Sequential Scans), degradando el tiempo de respuesta de la tienda. Se requiere diseñar e implementar una estrategia de índices profesional.

### Estado actual del sistema

Modelos sin optimización explícita de índices adicionales.

### Nueva necesidad

Definir índices compuestos (`models.Index(fields=['category', 'is_active'])`) e índices parciales en PostgreSQL (`models.Index(fields=['created_at'], condition=Q(is_active=True))`) en `apps/catalog` y `apps/orders`, analizando su impacto con `EXPLAIN ANALYZE`.

### Objetivo

Comprender cuándo y cómo crear índices en PostgreSQL con Django, evaluando el costo de escritura vs beneficio de lectura, y dominando los índices compuestos y condicionales (Partial Indexes).

### Actor

Ingeniero de Base de Datos / Backend Senior

### Módulo responsable

`apps/catalog` y `apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `Order`, `models.Index`, `models.Q` en `Meta.indexes`.

### Reglas de negocio

1. Las consultas que filtran por múltiples columnas frecuentemente deben contar con un índice compuesto respetando el orden de cardinalidad (ej. `category_id, is_active`).
2. Para tablas donde la gran mayoría de consultas solo buscan registros activos (`is_active = true`), se DEBE crear un Índice Parcial en PostgreSQL (`condition=Q(is_active=True)`), ahorrando espacio en disco y acelerando las búsquedas.
3. No crear índices indiscriminadamente en columnas que rara vez se filtran o que tienen alta tasa de escritura/modificación.

### Contrato esperado

Migración de Django que cree los índices en PostgreSQL y verificación de `Index Scan` mediante `EXPLAIN`.

### Persistencia

Comandos DDL en PostgreSQL: `CREATE INDEX idx_products_cat_active ON catalog_products (category_id, is_active); CREATE INDEX idx_products_active_created ON catalog_products (created_at) WHERE is_active = true;`.

### Relaciones

`Product`, `Category`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación atómica obligatoria mediante `transaction.atomic()`. Garantiza que todas las mutaciones en la base de datos se confirmen de forma íntegra o se reviertan totalmente (Rollback) ante fallos.

### Casos límite

Orden de las columnas en un índice compuesto (el operador de prefijo más selectivo debe ir primero).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

Protección contra ataques de DoS por consultas no indexadas de alta CPU.

### Consideraciones de rendimiento

Reducción del costo de consulta de escaneo secuencial (O(N)) a búsqueda en árbol B-Tree (O(log N)).

### Fundamentos de Python relacionados

Uso de objetos `Q` para condiciones de índices parciales.

### Conceptos Django relacionados

`Meta.indexes = [models.Index(name='...', fields=[...], condition=Q(...))]`, inspección con `sqlmigrate`.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`EXPLAIN ANALYZE SELECT * FROM catalog_products WHERE category_id = '...' AND is_active = true;`.

### Arquitectura

La definición de índices reside en los modelos de cada módulo (`models.py`).

### Dependencias entre módulos

Interno a `apps/catalog` y `apps/orders`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué agregar 20 índices a una tabla acelera las lecturas pero ralentiza drásticamente las inserciones (`INSERT`) y actualizaciones (`UPDATE`)?
2. ¿Qué ventaja ofrece un Índice Parcial (con cláusula `WHERE`) en PostgreSQL en comparación con un índice regular que indexe toda la tabla?

### Pruebas mínimas

1. Generar la migración de índices y verificar mediante `python manage.py sqlmigrate catalog <migración>` que se generen las sentencias `CREATE INDEX ... WHERE ...` exactas.
2. Aplicar la migración y comprobar en PostgreSQL con `\d catalog_products` que los índices estén activos.

### Pruebas negativas

1. Verificar que una consulta sobre un producto inactivo no utilice el índice parcial exclusivo de productos activos.

### Documentación

Documentar la justificación de cada índice creado en el diccionario de datos de la base de datos.

### Explicación posterior

Explica cómo PostgreSQL utiliza los árboles B-Tree para buscar rangos de valores en tiempo logarítmico y por qué el principio del 'prefijo más a la izquierda' determina si un índice compuesto puede ser utilizado o no por una consulta.

### Aplicación profesional

Optimización y afinamiento (Tuning) de bases de datos relacionales en sistemas con millones de filas y alta concurrencia.

### Reto adicional

Investigar y crear un índice de tipo GIN o GiST en PostgreSQL para búsquedas avanzadas.
