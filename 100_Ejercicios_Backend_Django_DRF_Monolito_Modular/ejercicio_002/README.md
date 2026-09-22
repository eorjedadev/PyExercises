# Ejercicio 002 — Modelado de Dominio de Catálogo y Tipos de Datos en PostgreSQL

[← Ejercicio 001](../ejercicio_001/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 003 →](../ejercicio_003/README.md)

---

### Contexto de negocio

El negocio necesita comercializar productos físicos y digitales. Cada producto debe contar con SKU único, nombre comercial, descripción detallada, precio monetario exacto en céntimos o decimales precisos, estado de publicación y peso físico para cálculo logístico posterior.

### Estado actual del sistema

Estructura base del monolito configurada con el módulo `apps/catalog` registrado.

### Nueva necesidad

Crear el modelo de dominio `Product` en `apps/catalog` con los tipos de datos nativos adecuados de PostgreSQL y restricciones de integridad.

### Objetivo

Diseñar el modelo `Product`, definir tipos de datos precisos para dinero y cantidades, aplicar migraciones sobre PostgreSQL y evitar tipos flotantes imprecisos.

### Actor

Desarrollador Backend / Modelador de Datos

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product` (atributos: `id` UUID, `sku`, `name`, `slug`, `description`, `price_amount`, `currency`, `weight_grams`, `is_active`, `created_at`, `updated_at`).

### Reglas de negocio

1. El SKU debe ser alfanumérico en mayúsculas y único en todo el catálogo.
2. El precio monetario no puede ser negativo y debe utilizar precisión fija (`DecimalField`), nunca punto flotante binario (`float`).
3. La moneda por defecto es 'USD' (código ISO 4217 de 3 caracteres).
4. El slug se genera a partir del nombre y debe ser único.

### Contrato esperado

Interacción interna a nivel de ORM y comandos de migración. Verificación en base de datos PostgreSQL.

### Persistencia

Tabla `catalog_products` en PostgreSQL con tipos `UUID`, `VARCHAR`, `DECIMAL(12, 2)`, `INTEGER`, `BOOLEAN`, `TIMESTAMP WITH TIME ZONE`.

### Relaciones

Entidad raíz de agregación sin relaciones foráneas en esta etapa.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación de formato de SKU (regex alfanumérico sin espacios), precio mayor o igual a 0.00.

### Transacciones

Operaciones DDL gestionadas atómicamente por el motor de migraciones de Django.

### Casos límite

Intentar registrar dos productos con el mismo SKU en diferente capitalización ('abc-123' vs 'ABC-123').

### Casos de error

`IntegrityError` en PostgreSQL cuando se viola la restricción de unicidad del SKU.

### Consideraciones de seguridad

Protección contra inyecciones SQL asegurada por el uso exclusivo del ORM de Django con consultas parametrizadas.

### Consideraciones de rendimiento

Definir índice único sobre `sku` e índice sobre `slug` e `is_active` para búsquedas frecuentes.

### Fundamentos de Python relacionados

Uso de `decimal.Decimal`, decoradores, métodos mágicos `__str__` y `__repr__`, typing con `UUID`.

### Conceptos Django relacionados

`models.Model`, `models.UUIDField`, `models.DecimalField`, `models.SlugField`, `models.Index`, `models.UniqueConstraint`.

### Conceptos DRF relacionados

No aplica directamente en este ejercicio enfocado en persistencia.

### PostgreSQL

Mapeo a tipos nativos: `uuid_generate_v4()`, `NUMERIC(12,2)`, `TIMESTAMPTZ`, constraints `UNIQUE`.

### Arquitectura

El modelo `Product` es privado al módulo `apps/catalog`. Otros módulos no deben modificarlo directamente.

### Dependencias entre módulos

Aislado. Solo depende de utilidades base de Django y tipos de Python.

### Antes de programar

1. ¿Por qué `float` es peligroso para representar dinero y por qué `DecimalField` o enteros en centavos son la opción profesional en backend?
2. ¿Por qué es recomendable usar UUID como clave primaria pública en lugar de IDs secuenciales auto-incrementales?

### Pruebas mínimas

1. Crear un producto válido mediante el ORM y verificar que persista en PostgreSQL con todos sus atributos.
2. Validar que `__str__` devuelva una representación clara (`[SKU] Nombre`).

### Pruebas negativas

1. Intentar crear un producto con precio negativo y verificar que falle la validación.
2. Intentar duplicar un SKU existente y verificar que PostgreSQL lance `IntegrityError`.

### Documentación

Documentar en el diccionario de datos del módulo `apps/catalog` cada campo, su tipo en PostgreSQL y su regla de negocio.

### Explicación posterior

Justifica la elección de tipos de datos para dinero y fechas con zona horaria (`DateTimeField(auto_now_add=True)` vs `timezone.now`).

### Aplicación profesional

Modelado de catálogos comerciales, sistemas de facturación y ERPs donde la exactitud numérica y unicidad son críticas.

### Reto adicional

Agregar un campo `metadata` de tipo `JSONField` en PostgreSQL con default `dict` para atributos variables del producto.
