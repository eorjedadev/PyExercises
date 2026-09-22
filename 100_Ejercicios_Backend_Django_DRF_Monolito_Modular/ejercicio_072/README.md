# Ejercicio 072 — Estrategias de Caché en Lecturas Frecuentes e Invalidación Granular

[← Ejercicio 071](../ejercicio_071/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 073 →](../ejercicio_073/README.md)

---

### Contexto de negocio

La página de inicio y el catálogo de productos destacados reciben 10,000 visitas por minuto. Ejecutar consultas a PostgreSQL para cada visitante satura la base de datos innecesariamente con datos que cambian pocas veces al día. Sin embargo, si un gestor de catálogo cambia el precio de un producto, el cambio debe reflejarse inmediatamente (el problema clásico de la invalidación de caché).

### Estado actual del sistema

Consultas de catálogo directas a PostgreSQL. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Implementar almacenamiento en caché de alto rendimiento para el selector de productos destacados en `apps/catalog/selectors.py`, e implementar la invalidación granular de caché en `apps/catalog/services.py` cada vez que un producto se crea, actualiza o desactiva.

### Objetivo

Dominar el patrón Cache-Aside (Lazy Loading) en Django, comprendiendo la serialización de datos en caché, generación de claves deterministas (`cache_key`) e invalidación quirúrgica basada en eventos de cambio de estado.

### Actor

Visitante Anónimo / Gestor de Catálogo con permisos administrativos y credenciales de acceso seguras.

### Módulo responsable

`apps/catalog` y `apps/core/cache` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`django.core.cache.cache`, selector `get_cached_featured_products`, servicio `invalidate_product_cache(product_id)`.

### Reglas de negocio

1. El selector de productos destacados debe intentar obtener los datos desde la caché (`cache.get(key)`); si no existen (Cache Miss), consultar PostgreSQL, guardar en caché por 1 hora (`cache.set(key, data, 3600)`) y retornar.
2. Los datos cacheados deben ser estructuras de datos nativas (listas de diccionarios JSON serializables), NO QuerySets perezosos de Django.
3. Cada vez que se actualice un producto mediante `update_product` o `update_product_price`, el servicio DEBE invalidar inmediatamente la clave de ese producto y la clave de la lista de destacados (`cache.delete(key)`).
4. La API debe responder con cabecera `X-Cache: HIT` o `X-Cache: MISS` para facilitar el diagnóstico.

### Contrato esperado

1. Primera Petición (Cache Miss):
- `GET /api/v1/catalog/featured/` -> `200 OK` (Header `X-Cache: MISS`, tiempo 85 ms)

2. Segunda Petición (Cache Hit):
- `GET /api/v1/catalog/featured/` -> `200 OK` (Header `X-Cache: HIT`, tiempo 2 ms)

### Persistencia

PostgreSQL solo se consulta en Cache Miss o en invalidaciones; lecturas servidas desde la memoria de caché de Django.

### Relaciones

`Product`, `Category`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Caída temporal del servidor de caché (el selector debe capturar la excepción y consultar PostgreSQL de forma transparente sin que la API falle (Fallback resiliente)).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

Nunca almacenar datos privados de otros usuarios en claves de caché públicas.

### Consideraciones de rendimiento

Reducción del tiempo de respuesta a < 5 ms y reducción de la carga en PostgreSQL en más del 95%.

### Fundamentos de Python relacionados

Manejo de estructuras serializables (`pickle` o `json`), generación de claves de caché con hashing (`hashlib.md5`).

### Conceptos Django relacionados

`django.core.cache.cache`, métodos `cache.get`, `cache.set`, `cache.delete`, `cache.get_or_set`.

### Conceptos DRF relacionados

Decoradores de vista o lógica dentro del selector.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

La lógica de lectura con caché reside en `selectors.py`; la invalidación reside en `services.py`.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué guardar un objeto `QuerySet` crudo directamente en caché es un error grave y por qué se deben guardar diccionarios o listas ya serializadas?
2. ¿Cuáles son los dos problemas más difíciles en ciencias de la computación según Phil Karlton? ('Naming things and cache invalidation').

### Pruebas mínimas

1. Consultar productos destacados (Cache Miss), verificar que se guarde en caché. Consultar por segunda vez y comprobar que no se ejecuten queries a PostgreSQL (Cache Hit verificado).
2. Modificar el precio de un producto mediante el servicio y verificar que la clave de caché se elimine y la siguiente consulta devuelva el precio nuevo.

### Pruebas negativas

1. Simular un fallo en el backend de caché y verificar que la API consulte la base de datos normalmente sin lanzar error 500.

### Documentación

Documentar la taxonomía de claves de caché y las políticas de TTL en la guía de rendimiento.

### Explicación posterior

Explica el patrón Cache-Aside frente a Write-Through y Write-Behind, y por qué la invalidación explícita en servicios es superior a depender pasivamente del tiempo de expiración (TTL).

### Aplicación profesional

Sistemas de alto tráfico, portales de noticias, catálogos de comercio electrónico y APIs públicas consumidas por millones de usuarios.

### Reto adicional

Implementar versionado de claves de caché mediante un prefijo global (ej. `v1:featured_products`) que permita invalidar toda la caché del catálogo en 1 milisegundo incrementando el número de versión.
