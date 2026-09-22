# Ejercicio 059 — Endpoints de Comprobación de Salud del Sistema (Health Checks)

[← Ejercicio 058](../ejercicio_058/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 060 →](../ejercicio_060/README.md)

---

### Contexto de negocio

En entornos de producción modernos gestionados por balanceadores de carga, Docker, Kubernetes o servicios Cloud, la infraestructura necesita verificar periódicamente si la aplicación backend está viva (Liveness Probe) y lista para recibir tráfico real (Readiness Probe). Si la conexión a PostgreSQL o la caché falla, el balanceador debe dejar de enviar tráfico inmediatamente a esa instancia y alertar al equipo de operaciones.

### Estado actual del sistema

Sistema completo con PostgreSQL, caché y múltiples módulos.

### Nueva necesidad

Crear el endpoint profesional de comprobación de salud `GET /api/v1/health/` en `apps/core/views/health.py`, verificando activamente la conectividad a PostgreSQL (`connection.cursor().execute('SELECT 1')`), estado de la caché y tiempo de respuesta.

### Objetivo

Construir Health Check Endpoints profesionales en Django/DRF, distinguiendo comprobaciones de vida (`liveness`) y disponibilidad (`readiness`), sin exponer información técnica interna sensible.

### Actor

Balanceador de Carga / Kubernetes / Monitor de Uptime

### Módulo responsable

`apps/core` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`HealthCheckAPIView`, `django.db.connection`, `django.core.cache.cache`.

### Reglas de negocio

1. `GET /api/v1/health/live/` (Liveness): Comprueba que el proceso de Django esté respondiendo (status `200 OK` inmediato).
2. `GET /api/v1/health/ready/` (Readiness): Ejecuta comprobaciones activas: ejecuta `SELECT 1` en PostgreSQL y escribe/lee una clave temporal en caché.
3. Si todas las dependencias críticas responden, responde `200 OK` con `{"status": "healthy", "checks": {"database": "healthy", "cache": "healthy"}}`.
4. Si alguna dependencia crítica falla, debe responder `503 Service Unavailable` con el detalle del servicio degradado.
5. El endpoint NO debe exponer contraseñas, IPs internas, versiones exactas ni trazas de error al público.

### Contrato esperado

1. Sistema Saludable:
- `GET /api/v1/health/ready/`
  Response: `200 OK`
  ```json
  {
    "status": "healthy",
    "timestamp": "2026-09-22T18:00:00Z",
    "checks": {
      "database": "healthy",
      "cache": "healthy"
    }
  }
  ```

2. Base de Datos Caída:
- `GET /api/v1/health/ready/`
  Response: `503 Service Unavailable`
  ```json
  {
    "status": "unhealthy",
    "checks": {
      "database": "unreachable",
      "cache": "healthy"
    }
  }
  ```

### Persistencia

Ejecución de consulta liviana `SELECT 1;` en PostgreSQL.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validación de tiempos de respuesta de dependencias.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Base de datos saturada con conexiones agotadas (debe responder 503 por timeout de conexión).

### Casos de error

`503 Service Unavailable` ante fallos de infraestructura.

### Consideraciones de seguridad

No exponer stack traces ni datos de configuración interna en respuestas públicas de health check.

### Consideraciones de rendimiento

La comprobación debe ser ultraliviana (no ejecutar queries pesadas) para que pueda consultarse cada 5 segundos sin impactar el rendimiento.

### Fundamentos de Python relacionados

Manejo de excepciones de conexión (`OperationalError`), medición de tiempos con `time.monotonic()`.

### Conceptos Django relacionados

`django.db.connection`, `django.core.cache`, `django.views.View` o `APIView` sin autenticación.

### Conceptos DRF relacionados

Endpoint con `permission_classes = [AllowAny]` y `authentication_classes = []`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

`apps/core` provee los endpoints de observabilidad e infraestructura.

### Dependencias entre módulos

Independiente de los módulos de negocio; solo interactúa con la infraestructura de Django.

### Antes de programar

1. ¿Por qué es vital que un Health Check de Readiness ejecute un `SELECT 1` real en lugar de simplemente responder `200 OK` en memoria?
2. ¿Por qué la distinción entre Liveness (¿el proceso está vivo?) y Readiness (¿el proceso puede atender peticiones?) es crucial en arquitecturas con contenedores?

### Pruebas mínimas

1. Consultar `GET /api/v1/health/ready/` con la base de datos operativa -> Verificar status `200 OK` y estado `healthy`.
2. Consultar `GET /api/v1/health/live/` -> Verificar status `200 OK`.

### Pruebas negativas

1. Simular un fallo de conexión a base de datos mediante un mock en `connection.cursor` y verificar que responda `503 Service Unavailable`.

### Documentación

Documentar los endpoints de health check en la guía de operaciones y monitoreo.

### Explicación posterior

Explica cómo los balanceadores de carga (Nginx, AWS ALB) y orquestadores (Kubernetes) utilizan las señales HTTP 200 vs 503 para enrutar tráfico o reiniciar contenedores automáticamente (Self-Healing).

### Aplicación profesional

Monitoreo de alta disponibilidad, integración con Datadog, Prometheus, AWS Route53 y Kubernetes Probes.

### Reto adicional

Agregar medición de latencia en milisegundos para cada servicio verificado (`database_latency_ms`).
