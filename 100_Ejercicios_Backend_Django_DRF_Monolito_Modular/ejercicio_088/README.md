# Ejercicio 088 — Gestión Segura de Secretos en Docker para Entornos Windows y CI/CD

[← Ejercicio 087](../ejercicio_087/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 089 →](../ejercicio_089/README.md)

---

### Contexto de negocio

Hardcodear contraseñas de base de datos o claves secretas en `docker-compose.yml` o en el `Dockerfile` provoca que cualquier persona con acceso al repositorio o al registro de imágenes Docker pueda leer credenciales de producción. Se requiere implementar gestión segura de secretos mediante Docker Secrets, archivos de entorno no versionados y variables de inyección en tiempo de ejecución.

### Estado actual del sistema

Docker y Docker Compose configurados. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Configurar la inyección segura de secretos en `docker-compose.yml` mediante `env_file: [.env]`, crear validaciones en `settings.py` para leer secretos desde archivos montados (`/run/secrets/`) y documentar el flujo seguro de variables en Windows y CI/CD.

### Objetivo

Dominar las mejores prácticas de seguridad en la gestión de secretos con Docker y Django, evitando fugas de credenciales en imágenes de contenedores y repositorios Git.

### Actor

Ingeniero de Seguridad / DevOps en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`config/` y archivos de configuración Docker

### Entidades involucradas

`docker-compose.yml`, `.env`, `.env.example`, `.gitignore`, `config/settings/base.py`.

### Reglas de negocio

1. Ninguna imagen de Docker compilada (`docker build`) debe contener secretos dentro de sus capas de filesystem.
2. En desarrollo local con Docker en Windows, las variables se inyectan dinámicamente desde el archivo local `.env` (ignorado en Git).
3. En producción, los secretos deben inyectarse mediante variables de entorno del orquestador o Docker Secrets montados en memoria.
4. El backend debe abortar el arranque inmediatamente si detecta que se están usando claves secretas de ejemplo inseguras en producción.

### Contrato esperado

Contenedores ejecutándose de forma segura sin exponer credenciales en `docker history` ni en el código fuente.

### Persistencia

Configuración segura de PostgreSQL. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de fortaleza de secretos al iniciar Django.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Auditar la imagen generada con `docker history --no-trunc <image_name>` para comprobar que ningún `ARG` o `ENV` exponga contraseñas en las capas de build.

### Casos de error

`ImproperlyConfigured` si falta algún secreto requerido.

### Consideraciones de seguridad

Cumplimiento de normativas de seguridad y auditorías de código (prevención de credenciales expuestas en Git).

### Consideraciones de rendimiento

Garantizar presupuesto de consultas O(1) evitando el problema N+1 mediante `select_related` y `prefetch_related`. Uso de índices B-Tree específicos y selección acotada de columnas mediante `only()` o `defer()`.

### Fundamentos de Python relacionados

Lectura de secretos desde archivos montados en el sistema de archivos de Linux (`pathlib.Path('/run/secrets/...').read_text()`).

### Conceptos Django relacionados

`django-environ` con soporte para `_FILE` suffixes (Docker Secrets).

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

Contenedor de PostgreSQL recibiendo contraseñas seguras desde variables de entorno inyectadas.

### Arquitectura

Seguridad de infraestructura en la capa de despliegue del monolito.

### Dependencias entre módulos

Transversal a la configuración del proyecto. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué pasar secretos mediante la instrucción `ENV` en un Dockerfile hace que la contraseña quede grabada permanentemente en el historial de la imagen Docker para siempre?
2. ¿Cómo funciona la técnica de Docker Secrets para montar claves directamente en memoria RAM (`/run/secrets/`) sin escribirlas en disco?

### Pruebas mínimas

1. Construir la imagen Docker, inspeccionar sus capas con `docker history` y verificar que no aparezca ninguna contraseña en texto plano.
2. Iniciar el stack con `docker compose --env-file .env up` y comprobar que Django se conecte exitosamente a PostgreSQL usando las credenciales inyectadas.

### Pruebas negativas

1. Verificar que el archivo `.env` esté listado en `.gitignore` y que `git status` no lo detecte para commit.

### Documentación

Documentar la guía de gestión de secretos y rotación de claves en `docs/SECURITY.md`.

### Explicación posterior

Explica cómo los pipelines de CI/CD modernos (GitHub Secrets, Vault de HashiCorp, AWS Secrets Manager) inyectan credenciales en tiempo de ejecución sin exponerlas en el código fuente.

### Aplicación profesional

Seguridad en infraestructura Cloud, cumplimiento de auditorías SOC2 / ISO 27001 y protección de secretos corporativos.

### Reto adicional

Configurar un hook de Git (`pre-commit`) con herramientas como `detect-secrets` o `gitleaks` para bloquear commits accidentales de claves privadas.
