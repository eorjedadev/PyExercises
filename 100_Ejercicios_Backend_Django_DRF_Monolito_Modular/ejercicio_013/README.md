# Ejercicio 013 — Introducción a la Capa de Servicios y Desacoplamiento de Lógica

[← Ejercicio 012](../ejercicio_012/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 014 →](../ejercicio_014/README.md)

---

### Contexto de negocio

El proceso de alta de un producto se ha vuelto complejo: además de guardar el modelo, se debe normalizar el SKU, generar un slug único resolviendo colisiones, calcular impuestos preliminares y emitir un registro de trazabilidad. Colocar toda esta lógica en el método `create()` del serializer o en la vista violaría el principio de responsabilidad única.

### Estado actual del sistema

CRUD básico de productos con serializers y vistas genéricas en `apps/catalog`.

### Nueva necesidad

Crear la capa de servicios (`apps/catalog/services.py`) con la función pura de negocio `create_product(...)` para orquestar la creación de productos fuera de las vistas y serializers.

### Objetivo

Implementar el patrón Service Layer en Django/DRF, entendiendo por qué la lógica de negocio debe residir en funciones de servicio independientes del protocolo HTTP.

### Actor

Operador de Catálogo / Proceso Batch en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `create_product` (servicio en `apps/catalog/services.py`), `ProductCreateInputSerializer`.

### Reglas de negocio

1. Si el slug generado colisiona con uno existente, el servicio debe agregar un sufijo incremental (ej. `laptop-pro-1`, `laptop-pro-2`).
2. El SKU debe ser normalizado a mayúsculas y sin espacios residuales antes de guardarse.
3. La creación del producto debe devolver la instancia del modelo creada o lanzar una excepción de dominio si una regla falla.
4. La vista solo debe validar el input mediante el serializer, llamar al servicio y serializar el resultado.

### Contrato esperado

Creación mediante Servicio:
- `POST /api/v1/catalog/products/`
  Request: `{"sku": "  lap-001 ", "name": "Laptop Pro", "price_amount": "1200.00", "category_id": "uuid"}`
  Response: `201 Created` con `sku: "LAP-001"` y `slug: "laptop-pro"`

### Persistencia

Persistencia gestionada dentro del servicio `create_product` mediante el ORM.

### Relaciones

`Product` y `Category`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validación sintáctica en Serializer; validación de reglas de negocio y unicidad de slug en el Servicio.

### Transacciones

Garantizar que si falla un paso posterior dentro del servicio, no queden datos corruptos.

### Casos límite

Crear 3 productos con el mismo nombre 'Mouse Gamer' (los slugs deben ser `mouse-gamer`, `mouse-gamer-1`, `mouse-gamer-2`).

### Casos de error

Excepción de dominio personalizada `CatalogDomainError` traducida a `400` en la capa HTTP.

### Consideraciones de seguridad

Aislar la lógica del framework HTTP permite reutilizar el servicio desde comandos CLI, tareas en background o tests unitarios sin simular peticiones HTTP.

### Consideraciones de rendimiento

Optimizar la consulta de verificación de slugs existentes con `Product.objects.filter(slug__startswith=...).values_list('slug', flat=True)`.

### Fundamentos de Python relacionados

Funciones con type hinting (`def create_product(*, sku: str, name: str, ...) -> Product:`), keyword-only arguments, excepciones personalizadas.

### Conceptos Django relacionados

Separación de capas: View (HTTP) -> Serializer (Contrato) -> Service (Dominio) -> Model (Persistencia).

### Conceptos DRF relacionados

Delegación en vistas: `product = create_product(**serializer.validated_data)`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

El patrón Service Layer desacopla el framework web (DRF/Django) de la lógica pura del negocio dentro del monolito modular.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Qué problemas ocurren cuando toda la lógica de negocio se escribe dentro de `serializer.create()` o `view.post()`?
2. ¿Cómo facilita la capa de servicios escribir pruebas unitarias rápidas sin levantar el cliente de API?

### Pruebas mínimas

1. Probar directamente la función `create_product(...)` en un test unitario pasando argumentos tipados y verificar que el producto retornado esté guardado en base de datos.
2. Probar la creación de dos productos con el mismo nombre y verificar la desambiguación de slugs.

### Pruebas negativas

1. Llamar a `create_product` con una categoría inactiva y verificar que lance `CatalogDomainError` explícito.

### Documentación

Documentar las firmas de los servicios públicos en el archivo `apps/catalog/services.py` con docstrings completos.

### Explicación posterior

Explica por qué usar keyword-only arguments (`*`) en funciones de servicio previene errores accidentales al pasar parámetros por posición.

### Aplicación profesional

Arquitectura limpia en Django aplicada a aplicaciones empresariales donde los servicios son invocados por APIs REST, GraphQL, tareas Celery y scripts CLI.

### Reto adicional

Implementar un servicio `update_product_price(*, product_id: UUID, new_price: Decimal, reason: str) -> Product` que registre en un log el cambio de precio.
