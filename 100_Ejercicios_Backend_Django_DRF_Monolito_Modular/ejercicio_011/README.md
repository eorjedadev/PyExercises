# Ejercicio 011 — Paginación de Recursos y Control de Carga en Memoria

[← Ejercicio 010](../ejercicio_010/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 012 →](../ejercicio_012/README.md)

---

### Contexto de negocio

A medida que el catálogo crece a miles de productos, devolver todos los registros en una sola respuesta provoca saturación de memoria en el servidor, sobrecarga en la transferencia de red y bloqueos en el navegador. Se requiere implementar paginación configurable y eficiente.

### Estado actual del sistema

Listado de productos sin paginación en `apps/catalog`.

### Nueva necesidad

Configurar paginación global y específica para el endpoint de productos, soportando `PageNumberPagination` con metadatos de total de páginas, página siguiente y previa.

### Objetivo

Comprender el funcionamiento de la paginación en DRF y PostgreSQL (`LIMIT` y `OFFSET`), configurando límites máximos de página para evitar abusos (`max_page_size`).

### Actor

Cliente Web / App Móvil autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/catalog` y configuración en `config/settings.py`

### Entidades involucradas

`Product`, `StandardResultsSetPagination`.

### Reglas de negocio

1. El tamaño de página por defecto es de 20 productos.
2. El cliente puede solicitar un tamaño personalizado mediante `?page_size=N`, con un máximo estricto de 100 productos por página.
3. La respuesta debe incluir metadata: `count` (total de elementos), `next` (URL siguiente), `previous` (URL previa) y `results` (lista de productos).
4. Si se solicita una página fuera de rango (ej. página 9999), debe responder `404 Not Found` con mensaje claro.

### Contrato esperado

Listado Paginado:
- `GET /api/v1/catalog/products/?page=2&page_size=10`
  Response: `200 OK`
  ```json
  {
    "count": 150,
    "next": "http://localhost:8000/api/v1/catalog/products/?page=3&page_size=10",
    "previous": "http://localhost:8000/api/v1/catalog/products/?page=1&page_size=10",
    "results": [
      { "id": "...", "name": "...", "price_amount": "..." }
    ]
  }
  ```

### Persistencia

PostgreSQL ejecuta `SELECT ... LIMIT 10 OFFSET 10` y `SELECT COUNT(*) FROM catalog_products`.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validar que `page` y `page_size` sean enteros positivos.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Enviar `?page_size=500` (el backend debe acotarlo automáticamente al `max_page_size=100`).

### Casos de error

`404 Not Found` cuando `page` supera el total de páginas disponibles.

### Consideraciones de seguridad

Prevenir ataques de denegación de servicio (DoS) limitando estrictamente el tamaño máximo de página que un cliente puede solicitar.

### Consideraciones de rendimiento

Comprender el costo de `COUNT(*)` en tablas de PostgreSQL con millones de registros y ordenar siempre por un campo indexado (`created_at` o `id`).

### Fundamentos de Python relacionados

División entera, cálculo de límites y offsets.

### Conceptos Django relacionados

`core.paginator.Paginator`, slicing en QuerySets de Django (`queryset[offset:offset+limit]`).

### Conceptos DRF relacionados

`pagination.PageNumberPagination`, `pagination_class`, atributos `page_size`, `page_size_query_param`, `max_page_size`.

### PostgreSQL

`SELECT * FROM catalog_products ORDER BY created_at DESC LIMIT 20 OFFSET 40`.

### Arquitectura

Clases de paginación reutilizables en `apps/core/pagination.py` aplicadas en `apps/catalog`.

### Dependencias entre módulos

`apps/catalog` importa la paginación genérica de `apps/core/pagination.py`.

### Antes de programar

1. ¿Por qué es un error grave permitir que el cliente solicite `?page_size=100000`?
2. ¿Por qué todo QuerySet paginado debe tener un ordenamiento explícito (`ordering = ['-created_at']`)?

### Pruebas mínimas

1. Crear 25 productos, solicitar `GET /api/v1/catalog/products/?page_size=10` y comprobar que `results` contenga 10 elementos y `count` sea 25.
2. Comprobar que `next` apunte a la página 2 y `previous` sea `null`.

### Pruebas negativas

1. Solicitar `GET /api/v1/catalog/products/?page=999` y verificar respuesta `404 Not Found`.

### Documentación

Documentar los parámetros query de paginación y la estructura de la respuesta en la guía de la API.

### Explicación posterior

Explica cómo evalúa Django los QuerySets perezosamente (`lazy evaluation`) para que el slicing se traduzca directamente en `LIMIT` y `OFFSET` en SQL sin traer toda la tabla a memoria.

### Aplicación profesional

Optimización de APIs de alto tráfico y prevención de saturación de memoria en servidores de producción.

### Reto adicional

Investigar e implementar una clase alternativa basada en `CursorPagination` para feeds de datos en tiempo real donde los registros cambian frecuentemente.
