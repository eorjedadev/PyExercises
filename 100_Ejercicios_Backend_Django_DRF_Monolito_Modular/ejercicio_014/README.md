# Ejercicio 014 — Introducción a la Capa de Selectores y Consultas Reutilizables

[← Ejercicio 013](../ejercicio_013/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 015 →](../ejercicio_015/README.md)

---

### Contexto de negocio

Varias vistas y servicios necesitan consultar productos bajo diferentes criterios de negocio: productos destacados, productos activos por categoría, productos con bajo stock y búsqueda avanzada. Escribir consultas `.filter(...)` complejas y repetitivas directamente en las vistas genera duplicación y errores.

### Estado actual del sistema

Capa de servicios implementada en `apps/catalog/services.py`.

### Nueva necesidad

Crear la capa de selectores (`apps/catalog/selectors.py`) para centralizar todas las consultas de lectura de productos y categorías, manteniendo las vistas delgadas.

### Objetivo

Aprender el patrón Selectors en Django/DRF, entendiendo la separación entre operaciones de escritura (Servicios) y operaciones de lectura (Selectores).

### Actor

Cualquier vista, servicio o consumidor de datos de catálogo

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `Category`, funciones en `apps/catalog/selectors.py` (`get_product_by_id`, `list_active_products`, `get_products_by_category`).

### Reglas de negocio

1. Todas las funciones de lectura deben devolver QuerySets tipados u objetos de modelo, permitiendo encadenar operaciones si es necesario.
2. Las funciones de selector deben incluir optimizaciones de consulta por defecto (`select_related` / `prefetch_related`).
3. La función `get_product_by_id(*, product_id: UUID) -> Optional[Product]` debe retornar `None` o la instancia sin lanzar `DoesNotExist` no controlado.

### Contrato esperado

Uso en vistas:
```python
# En views.py:
def get_queryset(self):
    return list_active_products(category_id=self.request.query_params.get('category_id'))
```

### Persistencia

Consultas `SELECT` optimizadas en PostgreSQL.

### Relaciones

`Product` y `Category`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validación de parámetros de entrada en selectores.

### Transacciones

No requerida para operaciones de solo lectura.

### Casos límite

Consultar con un `category_id` inexistente (debe devolver un QuerySet vacío `Product.objects.none()`).

### Casos de error

Retorno consistente de `None` o QuerySets vacíos sin excepciones inesperadas.

### Consideraciones de seguridad

Evitar concatenación de strings en queries; uso exclusivo de parámetros en el ORM.

### Consideraciones de rendimiento

Centralizar `select_related('category')` y `prefetch_related('tags')` dentro del selector para que ninguna vista olvide optimizar.

### Fundamentos de Python relacionados

Type hinting con `QuerySet[Product]`, `Optional[Product]`, funciones puras de lectura.

### Conceptos Django relacionados

`QuerySet.none()`, encadenamiento de filtros (`.filter()`), reutilización de consultas.

### Conceptos DRF relacionados

Integración de selectores en `get_queryset()` de vistas genéricas o en métodos de `APIView`.

### PostgreSQL

`SELECT ... FROM catalog_products INNER JOIN catalog_categories ...`.

### Arquitectura

Separación explícita de Lecturas (`selectors.py`) y Escrituras (`services.py`) dentro del módulo `apps/catalog`.

### Dependencias entre módulos

Interno a `apps/catalog`. Otros módulos podrán consultar `catalog.selectors`.

### Antes de programar

1. ¿Por qué separar consultas complejas en `selectors.py` es más limpio que sobrecargar el `Manager` del modelo con decenas de métodos?
2. ¿Cómo ayuda esta separación a evitar consultas duplicadas entre diferentes vistas?

### Pruebas mínimas

1. Probar `list_active_products()` y verificar que no incluya productos con `is_active=False`.
2. Probar `get_product_by_id(product_id=...)` con un ID válido y uno inexistente.

### Pruebas negativas

1. Consultar `get_product_by_id` con un UUID inexistente y comprobar que retorne `None` sin lanzar excepciones no controladas.

### Documentación

Documentar cada selector en `apps/catalog/selectors.py` indicando qué filtros y optimizaciones aplica.

### Explicación posterior

Explica la diferencia de propósito entre `services.py` (cambios de estado, transacciones, efectos secundarios) y `selectors.py` (solo lectura, sin efectos secundarios).

### Aplicación profesional

Bases de código Django profesionales con alta carga de lectura donde las consultas deben estar estandarizadas y optimizadas en un solo lugar.

### Reto adicional

Crear un selector `get_featured_products_with_tags(*, limit: int = 10) -> QuerySet[Product]` que utilice `prefetch_related` y devuelva los productos más recientes con sus etiquetas.
