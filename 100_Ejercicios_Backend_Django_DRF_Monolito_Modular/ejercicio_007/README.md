# Ejercicio 007 — Relaciones Many-to-Many con Metadata mediante Tabla Intermedia Explícita

[← Ejercicio 006](../ejercicio_006/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 008 →](../ejercicio_008/README.md)

---

### Contexto de negocio

Los productos pueden etiquetarse con múltiples Tags comerciales (ej. 'Oferta', 'Nuevo', 'Eco-Friendly', 'Gamer'). El equipo de marketing requiere registrar metadata en la asociación, como la fecha de asignación del tag y la prioridad de visualización de cada etiqueta en la ficha del producto.

### Estado actual del sistema

Modelos `Category` y `Product` funcionando en `apps/catalog`.

### Nueva necesidad

Crear el modelo `Tag` y la relación muchos a muchos con `Product` utilizando una tabla intermedia explícita (`through='ProductTagAssignment'`) con metadata adicional.

### Objetivo

Dominar relaciones N a M en Django y PostgreSQL usando modelos intermedios explícitos con `through`, evitando tablas intermedias automáticas e invisibles.

### Actor

Operador de Marketing / Catálogo en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Tag` (`id`, `name`, `slug`, `color_hex`), `ProductTagAssignment` (`id`, `product`, `tag`, `priority_order`, `assigned_at`), `Product`.

### Reglas de negocio

1. Un producto no puede tener el mismo Tag duplicado.
2. La prioridad de visualización es un entero positivo (1 = máxima prioridad).
3. El color hexadecimal del Tag debe cumplir formato `#RRGGBB`.
4. Si se elimina un Tag, se eliminan las asignaciones asociadas (`CASCADE`), pero el producto permanece intacto.

### Contrato esperado

Asignar Tags a Producto:
- `POST /api/v1/catalog/products/{id}/tags/`
  Request: `{"tag_id": "uuid-tag", "priority_order": 1}`
  Response: `201 Created`

Detalle de Producto con Tags:
- `GET /api/v1/catalog/products/{id}/`
  Response incluye: `"tags": [ { "id": "...", "name": "Oferta", "color_hex": "#FF0000", "priority_order": 1 } ]`

### Persistencia

Tablas `catalog_tags` y `catalog_product_tag_assignments` con índice compuesto único `(product_id, tag_id)` en PostgreSQL.

### Relaciones

`Product.tags = models.ManyToManyField(Tag, through='ProductTagAssignment', related_name='products')`.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validar unicidad del par `(product, tag)` y formato de `color_hex` con regex `^#[0-9A-Fa-f]{6}$`.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Intentar asignar dos veces el mismo Tag al mismo producto.

### Casos de error

`400 Bad Request` si el tag ya está asignado al producto (`UniqueConstraint`).

### Consideraciones de seguridad

Validar existencia del producto y del tag antes de intentar insertar la relación.

### Consideraciones de rendimiento

Utilizar `prefetch_related` al serializar productos con sus tags para evitar problemas N+1.

### Fundamentos de Python relacionados

Expresiones regulares (`re`), ordenamiento de listas por atributos (`key=lambda x: x.priority_order`).

### Conceptos Django relacionados

`models.ManyToManyField`, argumento `through`, `models.UniqueConstraint` en `Meta.constraints`.

### Conceptos DRF relacionados

Serializadores de modelos intermedios, serializadores anidados para lectura.

### PostgreSQL

`CREATE UNIQUE INDEX unique_product_tag ON catalog_product_tag_assignments (product_id, tag_id)`.

### Arquitectura

La tabla intermedia modela explícitamente el concepto de negocio 'Asignación de Tag con Prioridad' dentro de `apps/catalog`.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué es una mejor práctica usar siempre una tabla intermedia explícita con `through` en lugar del `ManyToManyField` automático de Django?
2. ¿Qué ventaja ofrece `UniqueConstraint` sobre el obsoleto `unique_together` en Django moderno?

### Pruebas mínimas

1. Crear un producto, un tag y asignarlos mediante `ProductTagAssignment.objects.create()`.
2. Consultar `product.tags.all()` y verificar que el tag aparezca en la colección.

### Pruebas negativas

1. Intentar registrar un segundo `ProductTagAssignment` con el mismo producto y tag -> Verificar `IntegrityError`.
2. Intentar crear un Tag con color inválido 'rojo-brillante' -> Fallo de validación `400`.

### Documentación

Documentar en el README del módulo la estructura de la tabla intermedia y sus campos de metadata.

### Explicación posterior

Explica cómo se consultan los campos de la tabla intermedia al recorrer la relación desde `Product`.

### Aplicación profesional

Sistemas de etiquetado, roles de usuario con fechas de expiración, matrículas de estudiantes en cursos con calificaciones.

### Reto adicional

Implementar un endpoint para actualizar en lote (`batch`) la prioridad de todas las etiquetas de un producto en una sola petición.
