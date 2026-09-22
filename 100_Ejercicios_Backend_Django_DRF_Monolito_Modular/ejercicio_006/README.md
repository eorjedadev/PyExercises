# Ejercicio 006 — Categorías y Relaciones Jerárquicas con ForeignKey Auto-referencial

[← Ejercicio 005](../ejercicio_005/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 007 →](../ejercicio_007/README.md)

---

### Contexto de negocio

Los productos del catálogo deben organizarse en categorías estructuradas como un árbol jerárquico (ej. 'Electrónica' -> 'Computación' -> 'Laptops'). Cada producto debe pertenecer a una categoría hoja, y una categoría puede tener subcategorías hijas.

### Estado actual del sistema

Modelo `Product` y endpoints de catálogo funcionando en `apps/catalog`.

### Nueva necesidad

Crear el modelo `Category` con soporte auto-referencial (`parent`), relacionar `Product` con `Category` y manejar integridad referencial en eliminaciones.

### Objetivo

Modelar relaciones 1 a N y árboles de categorías en PostgreSQL, configurar `ForeignKey`, `related_name`, políticas `on_delete=models.PROTECT` y exponer endpoints de categorías.

### Actor

Administrador de Catálogo / Cliente autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Category` (atributos: `id` UUID, `name`, `slug`, `parent` FK nullable), `Product` (FK `category`).

### Reglas de negocio

1. Una categoría puede no tener padre (categoría raíz) o tener una categoría padre existente.
2. Una categoría no puede ser su propio padre (prohibir ciclos directos).
3. No se puede eliminar una categoría si tiene productos asociados (`on_delete=models.PROTECT`).
4. Cada producto debe pertenecer obligatoriamente a una categoría activa.

### Contrato esperado

Crear Categoría:
- `POST /api/v1/catalog/categories/`
  Request: `{"name": "Laptops", "parent_id": "uuid-de-computacion"}`
  Response: `201 Created`

Listar Árbol de Categorías:
- `GET /api/v1/catalog/categories/`
  Response: `200 OK` con categorías y subcategorías anidadas o referenciadas.

### Persistencia

Tablas `catalog_categories` y `catalog_products` con clave foránea `category_id` e índice en PostgreSQL.

### Relaciones

`Category.parent` -> `ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')`; `Product.category` -> `ForeignKey(Category, on_delete=models.PROTECT, related_name='products')`.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validar que `parent_id` exista y no sea igual al ID de la propia categoría.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Eliminar una categoría con 50 productos asociados (debe ser rechazada limpiamente por la regla `PROTECT`).

### Casos de error

`400 Bad Request` si se intenta asociar una categoría inexistente o crear una referencia circular.

### Consideraciones de seguridad

Prevenir recursión infinita en serializadores anidados al recorrer árboles de profundidad indeterminada.

### Consideraciones de rendimiento

Crear índices sobre claves foráneas (`db_index=True`) para optimizar joins y filtros por categoría.

### Fundamentos de Python relacionados

Estructuras de datos en árbol, recursividad para serialización de jerarquías.

### Conceptos Django relacionados

`models.ForeignKey`, `on_delete=models.PROTECT`, `related_name`, migraciones con claves foráneas.

### Conceptos DRF relacionados

`PrimaryKeyRelatedField`, `SlugRelatedField`, serializadores anidados de lectura.

### PostgreSQL

`FOREIGN KEY (category_id) REFERENCES catalog_categories(id) ON DELETE RESTRICT`.

### Arquitectura

El módulo `apps/catalog` encapsula completamente la relación entre productos y categorías.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué `on_delete=models.PROTECT` es más seguro para categorías comerciales que `models.CASCADE`?
2. ¿Qué ocurre si un serializador intenta serializar `children` recursivamente sin límite de profundidad?

### Pruebas mínimas

1. Crear una categoría raíz y luego una subcategoría con `parent` asociado.
2. Crear un producto asignándole la subcategoría y verificar que `product.category.name` retorne el nombre correcto.

### Pruebas negativas

1. Intentar eliminar una categoría que tiene un producto asociado y verificar que Django/PostgreSQL lance excepción de protección.
2. Intentar asignar como `parent` un UUID inexistente y comprobar error `400`.

### Documentación

Documentar el diagrama relacional ER entre `Category` y `Product` en la carpeta `diagramas/` del módulo.

### Explicación posterior

Explica la diferencia entre `related_name='products'` y el default `product_set`, y por qué los nombres explícitos son obligatorios en proyectos profesionales.

### Aplicación profesional

Organización taxonómica de catálogos en plataformas de e-commerce, bibliotecas digitales y sistemas de inventario.

### Reto adicional

Implementar un endpoint `GET /api/v1/catalog/categories/{id}/products/` que devuelva todos los productos de esa categoría y de todas sus subcategorías descendientes.
