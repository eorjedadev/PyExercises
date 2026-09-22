# Ejercicio 060 — Documentación Automática OpenAPI / Swagger con drf-spectacular

[← Ejercicio 059](../ejercicio_059/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 061 →](../ejercicio_061/README.md)

---

### Contexto de negocio

Mantener documentación de API manualmente en archivos estáticos siempre queda desactualizado y genera fricción con los equipos de frontend, aplicaciones móviles y clientes de integración. El backend debe generar automáticamente una especificación OpenAPI 3.0 viva, tipada y exhaustiva, con interfaces interactivas Swagger UI y Redoc, documentando parámetros, esquemas de entrada/salida, cabeceras de autenticación JWT y códigos de error estándar.

### Estado actual del sistema

Todos los módulos principales del monolito implementados.

### Nueva necesidad

Integrar `drf-spectacular`, configurar `REST_FRAMEWORK['DEFAULT_SCHEMA_CLASS'] = 'drf_spectacular.openapi.AutoSchema'`, personalizar metadatos globales del proyecto y documentar vistas complejas usando el decorador `@extend_schema`.

### Objetivo

Dominar la generación profesional de documentación OpenAPI 3.0 en Django REST Framework con `drf-spectacular`, describiendo contratos exactos, esquemas de seguridad Bearer JWT y ejemplos de peticiones y respuestas.

### Actor

Desarrolladores Frontend, Integradores de API, Evaluadores de Seguridad

### Módulo responsable

`config/` y aplicado transversalmente en todas las `apps/`

### Entidades involucradas

`SPECTACULAR_SETTINGS` en `settings.py`, `SpectacularAPIView`, `SpectacularSwaggerView`, `SpectacularRedocView`, decorador `@extend_schema`.

### Reglas de negocio

1. El esquema OpenAPI 3.0 en formato YAML/JSON debe estar disponible en `GET /api/schema/`.
2. La interfaz interactiva Swagger UI debe servirse en `GET /api/docs/` y Redoc en `GET /api/redoc/`.
3. La documentación debe incluir el esquema de seguridad global `BearerAuth` para autorizar peticiones interactivamente con JWT.
4. Endpoints con acciones especiales (ej. `/cancel/`, `/webhooks/`, `/reports/`) deben estar decorados con `@extend_schema` explicando parámetros, descripciones y respuestas de error `4xx`/`5xx`.

### Contrato esperado

Endpoints de Documentación:
- `GET /api/schema/` -> Esquema OpenAPI 3.0 (YAML/JSON)
- `GET /api/docs/` -> Swagger UI interactivo
- `GET /api/redoc/` -> Redoc visualizador

### Persistencia

No aplica. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Público o restringido a staff según configuración de entorno.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validación estática del esquema con `python manage.py spectacular --validate`.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Serializadores dinámicos polimórficos o vistas sin serializer explícito (deben ser documentadas con `@extend_schema(request=..., responses=...)`).

### Casos de error

Advertencias de generación de esquema si faltan tipos en vistas no estándar.

### Consideraciones de seguridad

Posibilidad de deshabilitar Swagger en producción pública si la política de la empresa lo exige.

### Consideraciones de rendimiento

El esquema OpenAPI puede generarse estáticamente en tiempo de build (`python manage.py spectacular --file schema.yml`) para no penalizar peticiones en runtime.

### Fundamentos de Python relacionados

Decoradores avanzados con argumentos complejos, introspección de tipos y docstrings.

### Conceptos Django relacionados

Configuración de URLs de documentación en `config/urls.py`.

### Conceptos DRF relacionados

`drf-spectacular`, `@extend_schema`, `@extend_schema_view`, `OpenApiParameter`, `OpenApiExample`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

La especificación OpenAPI representa el contrato formal de todo el monolito modular hacia el mundo exterior.

### Dependencias entre módulos

`drf-spectacular` inspecciona automáticamente todas las `apps/` registradas en `INSTALLED_APPS`.

### Antes de programar

1. ¿Por qué `drf-spectacular` (OpenAPI 3.0) es el estándar moderno superior frente a las herramientas obsoletas basadas en Swagger 2.0 (como `drf-yasg` o `coreapi`)?
2. ¿Cómo permite un archivo `schema.yml` generar automáticamente SDKs de cliente para TypeScript, Kotlin o Swift?

### Pruebas mínimas

1. Ejecutar `python manage.py spectacular --validate` y verificar que el esquema se genere con 0 advertencias y 0 errores.
2. Consultar `GET /api/docs/` en el navegador y verificar que la interfaz Swagger UI cargue todos los endpoints con sus métodos y modelos.

### Pruebas negativas

1. Probar que ningún endpoint privado exponga campos excluidos o de solo lectura como si fueran de entrada.

### Documentación

Publicar el esquema OpenAPI generado en la raíz de documentación del proyecto.

### Explicación posterior

Explica el concepto de API-First / Contract-Driven Development y cómo OpenAPI 3.0 actúa como fuente única de verdad para frontend, backend, testing automatizado y contratos de integración.

### Aplicación profesional

Estándar universal en la industria de software para documentación, gobernanza de APIs y generación de clientes SDK.

### Reto adicional

Configurar un comando de exportación en CI/CD que valide el esquema OpenAPI y rechace el merge si algún endpoint carece de tipado o descripción.
