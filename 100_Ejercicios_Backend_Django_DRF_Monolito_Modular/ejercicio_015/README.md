# Ejercicio 015 — Formato de Respuestas de Error Estandarizado y Custom Exception Handler

[← Ejercicio 014](../ejercicio_014/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 016 →](../ejercicio_016/README.md)

---

### Contexto de negocio

Los diferentes módulos del backend y las validaciones de DRF producen formatos de error heterogéneos (a veces listas, a veces diccionarios, a veces errores HTML en 500). El equipo de frontend y los clientes móviles exigen un contrato de error estándar, predecible y parseable para toda la API del monolito.

### Estado actual del sistema

Módulo `apps/catalog` funcionando con excepciones estándar de DRF.

### Nueva necesidad

Crear un Custom Exception Handler en `apps/core/exceptions.py` y registrarlo en `settings.py` para normalizar todas las respuestas de error (`4xx` y `5xx`) bajo un formato único.

### Objetivo

Implementar el manejo centralizado de excepciones en DRF, mapear excepciones de dominio personalizadas a status codes HTTP apropiados y garantizar que ningún error no controlado exponga datos sensibles.

### Actor

Cualquier cliente que reciba un error HTTP

### Módulo responsable

`apps/core` (utilidad transversal) (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`custom_exception_handler`, excepciones personalizadas (`ApplicationError`, `EntityNotFoundError`, `DomainValidationError`).

### Reglas de negocio

1. Todas las respuestas de error deben seguir estrictamente la estructura:
   ```json
   {
     "error": {
       "code": "ERROR_CODE_STRING",
       "message": "Descripción legible para humanos",
       "details": { "campo": ["error específico"] },
       "timestamp": "2026-09-22T12:00:00Z"
     }
   }
   ```
2. Errores de validación de DRF (`400`) deben mapearse al código `VALIDATION_ERROR`.
3. Recursos no encontrados (`404`) deben mapearse al código `RESOURCE_NOT_FOUND`.
4. Errores inesperados (`500`) deben registrarse en el log con stacktrace completo pero devolver al cliente un código `INTERNAL_SERVER_ERROR` genérico sin exponer detalles técnicos.

### Contrato esperado

Ejemplo de Respuesta 400 Estandarizada:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados contienen errores de validación.",
    "details": {
      "sku": ["El SKU es obligatorio."]
    },
    "timestamp": "2026-09-22T10:00:00Z"
  }
}
```

### Persistencia

No aplica. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Excepción no manejada de Python puro (ej. `ZeroDivisionError` o `OperationalError` de base de datos).

### Casos de error

Transformación de cualquier fallo en la respuesta JSON estructurada correspondiente.

### Consideraciones de seguridad

Ocultar información de depuración, rutas de archivos y versiones de base de datos en respuestas de producción.

### Consideraciones de rendimiento

El handler de excepciones debe ser ultrarrápido y no realizar llamadas bloqueantes de I/O.

### Fundamentos de Python relacionados

Manejo avanzado de excepciones (`try...except`, herencia de `Exception`), introspección y timestamps.

### Conceptos Django relacionados

`django.core.exceptions.PermissionDenied`, `Http404`.

### Conceptos DRF relacionados

`REST_FRAMEWORK['EXCEPTION_HANDLER']`, `rest_framework.views.exception_handler`, `exceptions.APIException`.

### PostgreSQL

No exponer errores de sintaxis SQL directamente al cliente.

### Arquitectura

`apps/core/exceptions.py` define el contrato global de errores para todos los módulos del monolito.

### Dependencias entre módulos

`config/settings.py` referencia `apps.core.exceptions.custom_exception_handler`. Los módulos de negocio lanzan excepciones heredadas de `ApplicationError`.

### Antes de programar

1. ¿Por qué exponer stacktraces o mensajes de error crudos de PostgreSQL es una vulnerabilidad de seguridad crítica?
2. ¿Cómo simplifica un contrato de error uniforme el desarrollo de clientes frontend y móviles?

### Pruebas mínimas

1. Provocar un error de validación en `POST /api/v1/catalog/products/` y verificar que la respuesta contenga las claves `error.code`, `error.message` y `error.details`.
2. Provocar un `404` y verificar que `error.code` sea `'RESOURCE_NOT_FOUND'`.

### Pruebas negativas

1. Simular una excepción inesperada en una vista de prueba y verificar que retorne status `500` con el JSON de error estándar sin filtrar el traceback.

### Documentación

Documentar la estructura canónica de errores y la tabla de códigos de error en la guía general del proyecto.

### Explicación posterior

Explica cómo el custom exception handler envuelve al `exception_handler` por defecto de DRF y en qué casos retorna `None` requiriendo manejo adicional para errores 500.

### Aplicación profesional

Estandarización de APIs empresariales consumidas por múltiples equipos, SDKs y clientes de terceros.

### Reto adicional

Agregar un campo opcional `correlation_id` (tomado del `X-Request-ID` del middleware) dentro del objeto `error` para facilitar el rastreo en logs.
