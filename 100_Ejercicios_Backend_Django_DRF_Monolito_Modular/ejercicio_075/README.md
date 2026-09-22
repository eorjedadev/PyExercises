# Ejercicio 075 — Configuración Multientorno (Development, Testing, Production) y Settings Modulares

[← Ejercicio 074](../ejercicio_074/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 076 →](../ejercicio_076/README.md)

---

### Contexto de negocio

Tener un único archivo `settings.py` gigantesco con condicionales `if DEBUG:` dispersos por todo el archivo es frágil y peligroso. La configuración debe estructurarse como un paquete modular `config/settings/` dividido en: `base.py` (común a todos), `development.py` (desarrollo local ágil), `testing.py` (optimizado para velocidad en CI) y `production.py` (máxima seguridad, SSL forzado, cookies seguras, CORS estricto y almacenamiento seguro).

### Estado actual del sistema

`config/settings.py` como archivo único. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Reestructurar `config/settings/` como paquete Python modular, creando `base.py`, `development.py`, `testing.py`, `production.py` y configurando la variable `DJANGO_SETTINGS_MODULE` dinámicamente según el entorno.

### Objetivo

Dominar la organización modular de settings en proyectos Django profesionales de gran envergadura, garantizando el aislamiento de configuraciones y aplicando políticas de seguridad estrictas en producción.

### Actor

Ingeniero de Backend / DevOps / CI Pipeline

### Módulo responsable

`config` (Capa de Orquestación global, settings modulares y enrutamiento).

### Entidades involucradas

`config/settings/base.py`, `development.py`, `testing.py`, `production.py`, `manage.py`, `wsgi.py`, `asgi.py`.

### Reglas de negocio

1. `base.py` contiene todas las configuraciones universales: `INSTALLED_APPS`, `MIDDLEWARE`, `REST_FRAMEWORK`, `TEMPLATES`, `AUTH_PASSWORD_VALIDATORS`.
2. `development.py`: `DEBUG = True`, logging detallado en consola, toolbar activada, CORS permisivo para frontend local.
3. `testing.py`: `PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']` (para acelerar tests 500%), `EMAIL_BACKEND = 'locmem'`, base de datos de test rápida.
4. `production.py`: `DEBUG = False`, `SECURE_SSL_REDIRECT = True`, `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True`, `SECURE_HSTS_SECONDS = 31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`, `SECURE_HSTS_PRELOAD = True`.

### Contrato esperado

Arranque exitoso en cada entorno especificando `--settings=config.settings.development` o mediante `DJANGO_SETTINGS_MODULE` en `.env`.

### Persistencia

Configuración de base de datos PostgreSQL según entorno.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de configuraciones obligatorias de seguridad en producción.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Olvidar definir una variable requerida en producción (el arranque debe fallar inmediatamente con `ImproperlyConfigured`).

### Casos de error

`django.core.exceptions.ImproperlyConfigured` ante configuraciones inseguras en producción.

### Consideraciones de seguridad

Cumplimiento del checklist de seguridad de Django (`python manage.py check --deploy`).

### Consideraciones de rendimiento

Aceleración masiva de la suite de tests en `testing.py` utilizando un hasher de contraseñas ultrarrápido exclusivo para pruebas.

### Fundamentos de Python relacionados

Herencia de configuraciones mediante imports de módulos (`from .base import *`).

### Conceptos Django relacionados

`python manage.py check --deploy`, `DJANGO_SETTINGS_MODULE`, configuración de cabeceras HSTS y SSL.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

Configuración de conexiones SSL (`sslmode=require`) para PostgreSQL en producción.

### Arquitectura

Modularización limpia de la capa de configuración en `config/settings/`.

### Dependencias entre módulos

`config/settings/` orquesta la configuración global.

### Antes de programar

1. ¿Por qué usar `MD5PasswordHasher` exclusivamente en `testing.py` puede reducir el tiempo de ejecución de la suite de pruebas de 2 minutos a 10 segundos?
2. ¿Qué verificaciones realiza el comando `python manage.py check --deploy` antes de autorizar un pase a producción?

### Pruebas mínimas

1. Ejecutar `python manage.py check --settings=config.settings.development` -> 0 errores.
2. Ejecutar `pytest --ds=config.settings.testing` -> Ejecución ultrarrápida de todos los tests.
3. Ejecutar `python manage.py check --deploy --settings=config.settings.production` y verificar que pase todas las auditorías de seguridad.

### Pruebas negativas

1. Intentar iniciar en producción con `SECRET_KEY` insegura o `DEBUG=True` y comprobar que `check --deploy` emita advertencias críticas de seguridad.

### Documentación

Documentar la estructura de settings modulares y las instrucciones de despliegue en el README principal.

### Explicación posterior

Explica cómo gestionar entornos en CI/CD (GitHub Actions, Docker, Kubernetes) mediante la variable de entorno `DJANGO_SETTINGS_MODULE=config.settings.production`.

### Aplicación profesional

Estándar indiscutible en empresas de desarrollo de software para mantener proyectos ordenados, seguros y listos para producción.

### Reto adicional

Configurar soporte para lectura de configuraciones de almacenamiento en AWS S3 (`django-storages`) exclusivamente dentro de `production.py`.
