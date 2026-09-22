# Ejercicio 001 — Fundación del Monolito Modular y Configuración de Módulos

[← Volver al Índice Principal](../README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 002 →](../ejercicio_002/README.md)

---

### Contexto de negocio

Una empresa de retail tecnológico está iniciando la construcción de su plataforma central de backend. Para evitar el desorden de un monolito espagueti y el sobrecosto de microservicios prematuros, la dirección técnica ha decidido adoptar una arquitectura monolítica modular donde cada capacidad de negocio resida en un paquete interno aislado dentro de `apps/`.

### Estado actual del sistema

Inicio del proyecto desde cero. No existen modelos ni endpoints previos.

### Nueva necesidad

Diseñar la estructura base del repositorio, configurar el entorno con soporte para PostgreSQL, crear el módulo inicial `apps/core` (o `apps/common`) estrictamente para utilidades transversales agnósticas y el módulo `apps/catalog` para gestionar el catálogo comercial.

### Objetivo

Establecer la estructura de directorios del monolito modular, configurar la integración con variables de entorno, registrar las apps dentro de `config/settings.py` permitiendo imports limpios (`apps.catalog`), y verificar el arranque limpio del servidor sin dependencias circulares.

### Actor

Arquitecto de Software / Desarrollador Backend Inicial

### Módulo responsable

`config` y estructura base de `apps/`

### Entidades involucradas

Estructura de settings, paquetes modulares (`apps/catalog`, `apps/core`), variables de entorno.

### Reglas de negocio

1. Todas las aplicaciones del negocio deben residir dentro del directorio `apps/`.
2. El paquete `config` solo orquesta configuración global, URLs de entrada y middlewares centrales.
3. Ningún módulo puede usar paths absolutos hardcodeados ni credenciales en texto plano.
4. Las utilidades compartidas en `core` no deben depender de modelos ni lógica de módulos de negocio.

### Contrato esperado

Endpoint de comprobación inicial:
- `GET /api/v1/health/` -> Status: `200 OK`
  Response: `{"status": "healthy", "environment": "development", "versión": "1.0.0"}`

### Persistencia

Configuración de conexión a PostgreSQL mediante `DATABASE_URL` o parámetros en `.env`.

### Relaciones

No aplica entidades de base de datos en este paso fundacional.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar la presencia de variables de entorno requeridas al iniciar el proceso Django.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Variables de entorno faltantes o corruptas al iniciar el servidor (debe fallar tempranamente con un mensaje claro).

### Casos de error

`500 Internal Server Error` si la base de datos PostgreSQL configurada no es accesible al consultar salud.

### Consideraciones de seguridad

Garantizar que `.env` esté ignorado en `.gitignore` y que `SECRET_KEY` no se exponga en logs ni repositorios.

### Consideraciones de rendimiento

Carga perezosa de configuraciones y verificación eficiente de conexión.

### Fundamentos de Python relacionados

Estructura de paquetes Python (`__init__.py`), `sys.path`, manipulación de rutas con `pathlib.Path`, manejo de excepciones de entorno.

### Conceptos Django relacionados

`django-admin startproject`, modularización de settings, `INSTALLED_APPS` con `apps.catalog.apps.CatalogConfig`, `manage.py`.

### Conceptos DRF relacionados

`rest_framework` en `INSTALLED_APPS`, configuración básica de `REST_FRAMEWORK` en settings (`DEFAULT_RENDERER_CLASSES`, `DEFAULT_PARSER_CLASSES`).

### PostgreSQL

Creación de base de datos dedicada, usuario con privilegios mínimos y extensiones estándar si aplican.

### Arquitectura

Monolito Modular: `config/` (orquestación), `apps/` (dominios de negocio), `common/` o `apps/core/` (utilidades puras).

### Dependencias entre módulos

`config` depende de `apps.catalog` y `apps.core`. Ningún módulo de `apps/` debe depender de `config`.

### Antes de programar

1. ¿Por qué colocar las apps dentro de `apps/` en lugar de la raíz y cómo afecta esto a `sys.path` y `AppConfig`?
2. ¿Qué riesgos conlleva que una app dentro de `apps/` intente importar configuraciones directas de `config.settings`?

### Pruebas mínimas

1. Verificar que `python manage.py check` ejecute sin advertencias de configuración.
2. Probar que `GET /api/v1/health/` retorne status `200 OK` con el JSON de versión esperado.

### Pruebas negativas

1. Iniciar la aplicación sin la variable de entorno `DATABASE_URL` y verificar que el arranque falle con `ImproperlyConfigured` explícito.

### Documentación

Documentar en el README del proyecto la estructura de directorios adoptada, comandos de arranque en Windows (PowerShell) y variables de entorno necesarias.

### Explicación posterior

Explica cómo configuraste el `apps.py` de cada módulo para que Django reconozca el namespace `apps.catalog` y por qué es una mala práctica usar `common` como depósito de código sin cohesión.

### Aplicación profesional

Configuración de proyectos empresariales escalables con múltiples desarrolladores, evitando conflictos de nombres e imports espagueti.

### Reto adicional

Configurar un middleware ligero que inyecte un identificador único de petición (`X-Request-ID`) en todas las respuestas HTTP.
