# Ejercicio 067 — Optimización de Memoria en Consultas Masivas con only(), defer() y values_list()

[← Ejercicio 066](../ejercicio_066/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 068 →](../ejercicio_068/README.md)

---

### Contexto de negocio

Existen endpoints de autocompletado y sincronización masiva que solo necesitan el `id` y `name` de 10,000 productos. El modelo `Product` contiene columnas pesadas (`description` de miles de caracteres, `metadata` JSONB grande). Traer todas las columnas del modelo para miles de registros satura la memoria RAM del contenedor y sobrecarga el ancho de banda entre PostgreSQL y Django. Se requiere optimizar el payload SQL a nivel de columnas.

### Estado actual del sistema

Consultas masivas cargando todas las columnas del modelo en memoria.

### Nueva necesidad

Crear el endpoint optimizado de autocompletado `GET /api/v1/catalog/products/autocomplete/` utilizando `Product.objects.filter(is_active=True).only('id', 'sku', 'name')` o `values('id', 'sku', 'name')` para generar payloads ultraligeros.

### Objetivo

Dominar la optimización de memoria y transporte en Django mediante `only()`, `defer()`, `values()` y `values_list()`, comprendiendo el costo de instanciar miles de objetos de modelo completos en memoria RAM.

### Actor

Buscador Frontend / Sistema de Sincronización

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `only()`, `defer()`, `values()`, selector `list_products_lightweight`.

### Reglas de negocio

1. El endpoint de autocompletado solo debe devolver los campos esenciales: `id`, `sku`, `name`.
2. La consulta SQL generada debe ser estrictamente `SELECT id, sku, name FROM catalog_products ...`, sin traer columnas pesadas (`description`, `metadata`, `attributes`).
3. La respuesta debe responder en menos de 50 milisegundos para miles de registros.

### Contrato esperado

Autocompletado Ultraligero:
- `GET /api/v1/catalog/products/autocomplete/?q=mous`
  Response: `200 OK`
  ```json
  [
    { "id": "uuid-1", "sku": "TECH-MOU-001", "name": "Wireless Gaming Mouse" }
  ]
  ```

### Persistencia

PostgreSQL ejecuta `SELECT id, sku, name FROM catalog_products WHERE ...`.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Acceder accidentalmente a un campo diferido (ej. `product.description`) en código posterior (Django ejecutará una consulta SQL adicional por cada campo diferido accedido; se debe evitar este antipatrón).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

No exponer campos internos no solicitados. Prevención de vulnerabilidades OWASP API Top 10: validación estricta contra Mass Assignment, control de Ownership para evitar BOLA/IDOR y parametrización de consultas contra SQLi.

### Consideraciones de rendimiento

Reducción del consumo de memoria en un 80% y disminución del tiempo de serialización.

### Fundamentos de Python relacionados

Medición de uso de memoria con `sys.getsizeof()` y listas de diccionarios planos.

### Conceptos Django relacionados

`QuerySet.only()`, `QuerySet.defer()`, `QuerySet.values()`, `QuerySet.values_list(flat=True)`.

### Conceptos DRF relacionados

Serializadores ligeros o retorno directo de diccionarios con `Response(data)` sin pasar por serializadores pesados.

### PostgreSQL

`SELECT id, sku, name FROM catalog_products WHERE is_active = true AND name ILIKE '%mous%';`.

### Arquitectura

Los selectores ligeros residen en `apps/catalog/selectors.py`.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué instanciar 10,000 objetos `Product` de Django en memoria consume mucho más RAM que obtener una lista de 10,000 diccionarios planos con `values()`?
2. ¿Qué peligro tiene usar `.defer('description')` si luego un serializador intenta leer `product.description`?

### Pruebas mínimas

1. Crear 100 productos en la base de datos de pruebas, invocar el endpoint de autocompletado dentro de `CaptureQueriesContext` -> Verificar que el SQL ejecutado contenga solo `SELECT ...id, sku, name` y NO incluya `description` ni `attributes`.
2. Verificar que el JSON retornado contenga exactamente los 3 campos esperados.

### Pruebas negativas

1. Comprobar que no se disparen consultas diferidas (deferred queries) adicionales durante la serialización.

### Documentación

Documentar la lista de endpoints de alto rendimiento en la guía de APIs.

### Explicación posterior

Explica el compromiso entre conveniencia (instancias ricas de Model con métodos y validaciones) y rendimiento extremo (diccionarios planos con `values()` o tuplas con `values_list()`) en consultas de gran escala.

### Aplicación profesional

Endpoints de autocompletado en tiempo real, exportaciones masivas a Data Lakes, sincronizaciones con CRMs y feeds de catálogo para Google Shopping / Facebook Catalog.

### Reto adicional

Crear un selector `get_product_ids_by_category(category_id) -> list[UUID]` que use `values_list('id', flat=True)` para obtener una lista pura de UUIDs en 1 milisegundo.
