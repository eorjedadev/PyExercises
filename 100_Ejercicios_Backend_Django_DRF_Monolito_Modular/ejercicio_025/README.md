# Ejercicio 025 — Gestión Segura de Configuración y Variables de Entorno

[← Ejercicio 024](../ejercicio_024/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 026 →](../ejercicio_026/README.md)

---

### Contexto de negocio

El equipo de seguridad ha auditado el repositorio y exige eliminar cualquier valor de configuración sensible que pudiera estar hardcodeado. La aplicación debe configurarse al 100% mediante variables de entorno con tipado estricto, valores por defecto seguros y soporte para archivos `.env` en desarrollo local.

### Estado actual del sistema

Proyecto con múltiples módulos activos. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Integrar `django-environ` (o `python-decouple`) en `config/settings.py`, configurando `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, `DATABASE_URL`, tiempos de vida de JWT y parámetros de seguridad mediante variables de entorno.

### Objetivo

Profesionalizar la gestión de configuración en Django siguiendo los principios de 12-Factor App (Config en el entorno), garantizando que el código sea agnóstico al entorno de ejecución.

### Actor

Ingeniero de Backend / DevOps en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`config` (Capa de Orquestación global, settings modulares y enrutamiento).

### Entidades involucradas

`config/settings.py`, `.env.example`, `.gitignore`.

### Reglas de negocio

1. `DEBUG` debe ser `False` por defecto a menos que la variable de entorno `DJANGO_DEBUG` sea explícitamente `'True'` o `'1'`.
2. `SECRET_KEY` es obligatoria; si no está definida en el entorno, el servidor debe abortar el arranque con un error descriptivo.
3. La base de datos debe configurarse parseando `DATABASE_URL` (ej. `postgres://user:pass@localhost:5432/dbname`).
4. Debe existir un archivo `.env.example` versionado en Git con nombres de variables y valores ficticios de ejemplo.

### Contrato esperado

Arranque exitoso con `python manage.py check` leyendo variables desde archivo `.env` local.

### Persistencia

Configuración de conexión a PostgreSQL mediante `env.db('DATABASE_URL')`.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de tipos de datos en variables de entorno (booleanos, listas, URLs, enteros).

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Espacios residuales o comillas accidentales en el archivo `.env`.

### Casos de error

`django.core.exceptions.ImproperlyConfigured` si falta una variable requerida sin valor por defecto.

### Consideraciones de seguridad

Asegurar estrictamente que `.env` esté en `.gitignore`. Nunca hacer commit de claves privadas ni credenciales de PostgreSQL.

### Consideraciones de rendimiento

Las variables de entorno se leen una sola vez durante el arranque del proceso Django.

### Fundamentos de Python relacionados

Módulo `os`, `pathlib.Path`, tipado y conversión de datos.

### Conceptos Django relacionados

`django-environ`, configuración de `DATABASES`, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`.

### Conceptos DRF relacionados

Parámetros de DRF (`ACCESS_TOKEN_LIFETIME`, `REFRESH_TOKEN_LIFETIME`) leídos dinámicamente desde el entorno.

### PostgreSQL

Cadena de conexión estándar de PostgreSQL con SSL opcional.

### Arquitectura

La capa de configuración en `config/` aísla el código del entorno de infraestructura.

### Dependencias entre módulos

`config/settings.py` es el único lugar donde se inicializa `environ.Env`.

### Antes de programar

1. ¿Por qué dejar `DEBUG = True` en producción es una vulnerabilidad catastrófica?
2. ¿Por qué es obligatorio mantener un `.env.example` actualizado para el equipo de desarrollo?

### Pruebas mínimas

1. Ejecutar `python manage.py check` con variables válidas en `.env` -> 0 errores.
2. Verificar que `settings.DEBUG` sea booleano `False` cuando `DJANGO_DEBUG=0`.

### Pruebas negativas

1. Eliminar la variable `SECRET_KEY` del entorno y verificar que Django rechace iniciar con `ImproperlyConfigured`.

### Documentación

Documentar en el `README.md` principal todas las variables de entorno soportadas y sus formatos.

### Explicación posterior

Explica el principio III de The Twelve-Factor App ('Store config in the environment') y cómo `django-environ` simplifica el despliegue en entornos Docker, Kubernetes o Cloud.

### Aplicación profesional

Estándar obligatorio en cualquier empresa de software profesional y pipelines de CI/CD.

### Reto adicional

Configurar soporte para leer variables booleanas seguras para `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE` y `CSRF_COOKIE_SECURE`.
