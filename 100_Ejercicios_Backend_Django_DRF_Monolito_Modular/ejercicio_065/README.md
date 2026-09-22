# Ejercicio 065 — Búsqueda Avanzada de Texto Completo en PostgreSQL (Full-Text Search)

[← Ejercicio 064](../ejercicio_064/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 066 →](../ejercicio_066/README.md)

---

### Contexto de negocio

La búsqueda básica mediante `icontains` o `ILIKE` en PostgreSQL es lenta en grandes catálogos porque no puede usar índices B-Tree estándar y no comprende el lenguaje natural: no soporta raíces de palabras (lematización: 'correr' coincide con 'corriendo'), ranking de relevancia ni ponderación (el título tiene más peso que la descripción). Se requiere implementar Full-Text Search nativo de PostgreSQL.

### Estado actual del sistema

Búsqueda simple de productos en `apps/catalog`.

### Nueva necesidad

Integrar las capacidades nativas de búsqueda de texto completo de PostgreSQL en Django (`django.contrib.postgres.search`), implementando `SearchVector`, `SearchQuery`, `SearchRank` y resaltado de coincidencias (`SearchHeadline`) en el módulo de catálogo.

### Objetivo

Dominar Full-Text Search (FTS) nativo de PostgreSQL con Django, ponderando campos con pesos (`Weight('A')` para nombre, `Weight('B')` para descripción) y ordenando los resultados por relevancia.

### Actor

Cliente de Catálogo / Motor de Búsqueda autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `SearchVector`, `SearchQuery`, `SearchRank`, `SearchHeadline`, selector `search_products_fulltext`.

### Reglas de negocio

1. La búsqueda debe usar el diccionario de idioma configurado (ej. `'spanish'` o `'english'`).
2. El campo `name` tiene peso 'A' (máxima relevancia); el campo `description` tiene peso 'B'.
3. Los resultados deben ordenarse automáticamente por su puntuación de relevancia (`SearchRank`) de mayor a menor.
4. La respuesta debe incluir un snippet resaltado (`SearchHeadline`) que muestre el fragmento de la descripción donde apareció la palabra buscada.

### Contrato esperado

Búsqueda Full-Text con Relevancia:
- `GET /api/v1/catalog/products/search/?q=inalambrico`
  Response: `200 OK`
  ```json
  [
    {
      "id": "uuid-prod-1",
      "name": "Mouse Inalámbrico Pro",
      "rank": 0.6079,
      "headline": "Sensor óptico con tecnología <b>inalámbrico</b> de 2.4GHz..."
    }
  ]
  ```

### Persistencia

Tipos nativos `tsvector` y `tsquery` en PostgreSQL con soporte para índice GIN (`GinIndex`).

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validar que la cadena de búsqueda `q` no esté vacía.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Búsqueda con errores ortográficos menores o palabras con acentos/tildes (PostgreSQL normaliza raíces lingüísticas automáticamente con el diccionario de idioma).

### Casos de error

`400 Bad Request` si el parámetro de búsqueda contiene caracteres especiales de sintaxis FTS corruptos.

### Consideraciones de seguridad

Protección contra inyecciones de sintaxis de búsqueda mediante el uso de `SearchQuery(q, search_type='websearch')`.

### Consideraciones de rendimiento

Crear un índice `GinIndex` en PostgreSQL sobre el vector de búsqueda para que la consulta no ejecute cálculos al vuelo.

### Fundamentos de Python relacionados

Manipulación de parámetros de búsqueda y strings.

### Conceptos Django relacionados

`django.contrib.postgres.search.SearchVector`, `SearchQuery`, `SearchRank`, `SearchHeadline`, `django.contrib.postgres.indexes.GinIndex`.

### Conceptos DRF relacionados

Endpoint de búsqueda especializado con paginación.

### PostgreSQL

`SELECT name, ts_rank(to_tsvector('spanish', name), to_tsquery('spanish', 'inalambrico')) AS rank FROM catalog_products WHERE to_tsvector('spanish', name) @@ to_tsquery('spanish', 'inalambrico') ORDER BY rank DESC;`.

### Arquitectura

El motor de búsqueda reside en `apps/catalog/search.py` o `selectors.py`.

### Dependencias entre módulos

Interno a `apps/catalog` aprovechando la integración de Django con PostgreSQL.

### Antes de programar

1. ¿Por qué `ILIKE '%termino%'` no puede utilizar índices estándar y fuerza un escaneo secuencial completo de la tabla?
2. ¿Cómo funciona la lematización (Stemming) en PostgreSQL para encontrar 'zapatos' cuando el usuario busca 'zapato'?

### Pruebas mínimas

1. Crear 2 productos (uno con la palabra en el título y otro con la palabra en la descripción), buscar el término -> Verificar que ambos aparezcan y que el del título tenga un `rank` mayor.
2. Verificar que `headline` contenga la etiqueta resaltada `<b>...</b>`.

### Pruebas negativas

1. Buscar una palabra que no existe en el catálogo y comprobar que devuelva una lista vacía `[]` con status `200 OK`.

### Documentación

Documentar la sintaxis de búsqueda admitida (búsqueda tipo web, operadores OR/AND) en la guía de la API.

### Explicación posterior

Explica cómo PostgreSQL compite favorablemente con motores externos como Elasticsearch para catálogos de tamaño medio gracias a `tsvector`, `tsquery` e índices GIN sin necesidad de mantener infraestructura adicional.

### Aplicación profesional

Buscadores de productos en e-commerce, motores de búsqueda documental y búsqueda de artículos en blogs y wikis.

### Reto adicional

Configurar un campo almacenado `search_vector = SearchVectorField()` en el modelo `Product` actualizado automáticamente por triggers o señales para máxima velocidad de consulta.
