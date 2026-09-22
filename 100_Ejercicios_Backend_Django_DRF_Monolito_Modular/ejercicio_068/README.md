# Ejercicio 068 — Logging Estructurado Profesional en Formato JSON para Producción

[← Ejercicio 067](../ejercicio_067/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 069 →](../ejercicio_069/README.md)

---

### Contexto de negocio

Usar `print()` o logs en texto plano desordenado en producción hace imposible buscar, filtrar y analizar eventos en herramientas centralizadas de observabilidad (Datadog, AWS CloudWatch, ElasticSearch/Kibana, Grafana Loki). Se requiere configurar el sistema de logging de Django para emitir logs estructurados en formato JSON con nivel, timestamp ISO, logger, mensaje, contexto de negocio y correlación de peticiones (`request_id`).

### Estado actual del sistema

Configuración básica de logging de Django por defecto.

### Nueva necesidad

Configurar `LOGGING` en `config/settings.py` con un formateador JSON (`python-json-logger` o formateador personalizado en `apps/core/logging.py`), asegurando que ningún dato sensible (contraseñas, tokens completos) aparezca en los logs.

### Objetivo

Dominar el logging estructurado profesional en Django, entendiendo la configuración de `dictConfig`, loggers por módulo (`apps.orders`, `apps.payments`), handlers y formateadores JSON.

### Actor

Desarrollador / Sistema de Observabilidad / DevOps

### Módulo responsable

`config/` y `apps/core` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`config/settings.py` (`LOGGING`), `StructuredJsonFormatter`, `logging.getLogger(__name__)`.

### Reglas de negocio

1. Todos los logs de nivel `INFO`, `WARNING`, `ERROR` y `CRITICAL` deben emitirse como líneas JSON válidas de una sola línea (NDJSON).
2. Cada línea de log debe incluir: `timestamp` (UTC ISO-8601), `level`, `logger_name`, `message`, `module`, `function`, `line_number`.
3. Si la petición cuenta con un `X-Request-ID` (inyectado por el middleware), debe incluirse automáticamente en el campo `request_id` del JSON.
4. Los logs de excepciones (`logger.exception`) deben incluir el campo `exception` estructurado sin romper el formato JSON de una sola línea.

### Contrato esperado

Ejemplo de Salida de Log Estructurado en Terminal / Stdout:
```json
{"timestamp": "2026-09-22T19:00:00.123Z", "level": "INFO", "logger": "apps.orders.services", "message": "Orden creada exitosamente", "order_id": "uuid-123", "total": "149.80", "request_id": "req-abc-999"}
```

### Persistencia

Salida estándar (`stdout` / `stderr`) para que sea capturada por Docker o agentes de observabilidad.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validar no presencia de claves sensibles en los extras de log.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Registrar un mensaje que contenga saltos de línea o caracteres Unicode (el formateador JSON debe escaparlos correctamente en una sola línea).

### Casos de error

Captura de excepciones en `logger.error` con `exc_info=True`.

### Consideraciones de seguridad

Filtro automático para sanitizar o enmascarar campos como `password`, `token`, `secret`, `cvv`, `credit_card`.

### Consideraciones de rendimiento

El logging a `stdout` no debe realizar I/O bloqueante a disco sincrónico.

### Fundamentos de Python relacionados

Módulo `logging` estándar de Python, creación de clases `logging.Formatter` y `logging.Filter`.

### Conceptos Django relacionados

Configuración `LOGGING` en `settings.py` usando `logging.config.dictConfig`.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

`apps/core/logging.py` centraliza los formateadores y filtros transversales del monolito.

### Dependencias entre módulos

Todos los módulos obtienen su logger con `logger = logging.getLogger(__name__)`.

### Antes de programar

1. ¿Por qué `print()` es inaceptable en código backend profesional de producción (no tiene niveles, no tiene timestamps, no es redirigible y satura buffers)?
2. ¿Por qué el formato JSON en logs de una sola línea es el estándar para agregadores de logs como Datadog o ElasticSearch?

### Pruebas mínimas

1. Emitir un log con `logger.info('Mensaje de prueba', extra={'custom_key': 'valor'})` y comprobar que la salida sea un string JSON válido parseable con `json.loads()`.
2. Verificar que los campos estándar (`timestamp`, `level`, `message`) estén presentes.

### Pruebas negativas

1. Intentar registrar un diccionario que contenga `{'password': 'secreto123'}` en el `extra` y verificar que el filtro de seguridad lo enmascare como `{'password': '***'}`.

### Documentación

Documentar las convenciones de logging y la configuración de `LOGGING` en la guía de operaciones.

### Explicación posterior

Explica los 5 niveles estándar de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL) y cuándo utilizar cada uno en el ciclo de vida de un backend.

### Aplicación profesional

Observabilidad en entornos Cloud, depuración de incidentes en producción (Root Cause Analysis) y auditoría técnica.

### Reto adicional

Crear un `SensitiveDataFilter` que inspeccione automáticamente el diccionario `extra` del log y reemplace cualquier valor cuya clave coincida con patrones sensibles por `[REDACTED]`.
