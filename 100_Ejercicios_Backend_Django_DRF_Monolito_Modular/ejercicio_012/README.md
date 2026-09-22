# Ejercicio 012 — Filtrado Declarativo, Búsqueda Textual y Ordenamiento Seguro

[← Ejercicio 011](../ejercicio_011/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 013 →](../ejercicio_013/README.md)

---

### Contexto de negocio

Los clientes necesitan buscar productos por texto (en nombre y descripción), filtrar por rango de precios, filtrar por categoría y ordenar los resultados por precio ascendente/descendente o por fecha de creación.

### Estado actual del sistema

Listado paginado de productos en `apps/catalog`.

### Nueva necesidad

Integrar `django-filter` y los filtros nativos de DRF (`SearchFilter`, `OrderingFilter`), configurando filtros declarativos con validación de campos permitidos.

### Objetivo

Diseñar una capa de filtrado profesional evitando `if 'param' in request.GET` manuales y previniendo inyecciones de ordenamiento sobre campos no indexados o privados.

### Actor

Cliente de Catálogo autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `ProductFilterSet` (`django_filters.FilterSet`).

### Reglas de negocio

1. Búsqueda textual en campos `name` y `description` mediante `?search=termino`.
2. Filtrado por rango de precios mediante `?min_price=X` y `?max_price=Y`.
3. Filtrado exacto por `?category_id=UUID`.
4. Ordenamiento permitido únicamente por `price_amount` y `created_at` (`?ordering=price_amount` o `?ordering=-created_at`). Cualquier otro campo debe ser ignorado.

### Contrato esperado

Búsqueda y Filtro Combinado:
- `GET /api/v1/catalog/products/?search=mouse&min_price=20&max_price=100&ordering=-price_amount`
  Response: `200 OK` con productos que coincidan con la búsqueda, dentro del rango y ordenados de mayor a menor precio.

### Persistencia

Generación de cláusulas `WHERE name ILIKE ... AND price_amount BETWEEN ... ORDER BY price_amount DESC` en PostgreSQL.

### Relaciones

`Product` y `Category`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validar que `min_price` y `max_price` sean números válidos.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Enviar `?ordering=secret_internal_field` (debe ser ignorado por el filtro seguro sin lanzar error ni exponer datos).

### Casos de error

`400 Bad Request` si los valores de los filtros numéricos no son válidos (ej. `min_price=abc`).

### Consideraciones de seguridad

Configurar `ordering_fields` de manera explícita para evitar que clientes maliciosos fuercen ordenamientos costosos por campos sin índice.

### Consideraciones de rendimiento

Asegurar índices en PostgreSQL para los campos filtrables (`price_amount`, `category_id`, `created_at`).

### Fundamentos de Python relacionados

Diccionarios de filtros, operadores de comparación.

### Conceptos Django relacionados

`django_filters.FilterSet`, `django_filters.NumberFilter(lookup_expr='gte')`.

### Conceptos DRF relacionados

`filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]`, `filterset_class`, `search_fields`, `ordering_fields`.

### PostgreSQL

Consultas optimizadas con operadores `ILIKE`, `>=`, `<=` y cláusulas `ORDER BY`.

### Arquitectura

El `ProductFilterSet` reside en `apps/catalog/filters.py`, manteniendo las vistas limpias y declarativas.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué construir filtros manualmente con múltiples `if request.GET.get(...)` genera código difícil de mantener y probar?
2. ¿Cuál es el peligro de no restringir `ordering_fields` en DRF?

### Pruebas mínimas

1. Crear 3 productos con diferentes precios y nombres, filtrar por `min_price=50` y verificar que solo aparezcan los productos correspondientes.
2. Buscar `?search=Gaming` y comprobar que coincidan productos con esa palabra en nombre o descripción.

### Pruebas negativas

1. Enviar `?min_price=invalido` y verificar respuesta `400 Bad Request`.
2. Enviar `?ordering=campo_inexistente` y comprobar que el orden vuelva al default seguro sin fallar.

### Documentación

Documentar la lista completa de parámetros de filtrado y ordenamiento en el contrato de la API.

### Explicación posterior

Explica cómo `django-filter` inspecciona los campos del modelo y genera dinámicamente las cláusulas del QuerySet.

### Aplicación profesional

Implementación de motores de búsqueda y filtrado para e-commerce, catálogos de productos y paneles de administración.

### Reto adicional

Agregar un filtro personalizado `in_stock=true` que filtre productos cuyo stock (que modelaremos más adelante) sea mayor a cero.
