# Ejercicio 039 — Jerarquía de Excepciones de Dominio y Mapeo Limpio a HTTP

[← Ejercicio 038](../ejercicio_038/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 040 →](../ejercicio_040/README.md)

---

### Contexto de negocio

A medida que la lógica del negocio se complejiza (órdenes, inventario, clientes), los servicios lanzan diversas excepciones de negocio: `InsufficientStockError`, `OrderNotFoundError`, `InvalidStateTransitionError`, `CouponExpiredError`. Los servicios NO deben importar ni conocer códigos HTTP (`status.HTTP_400_BAD_REQUEST`). Se requiere una jerarquía limpia de excepciones de dominio en Python puro y un mapeo centralizado a HTTP.

### Estado actual del sistema

Múltiples servicios lanzando excepciones dispersas.

### Nueva necesidad

Crear la jerarquía de excepciones base `DomainError` en `apps/core/exceptions.py`, hacer que cada módulo defina sus propias excepciones heredadas y actualizar el exception handler para traducir automáticamente cada excepción de dominio a su código HTTP y formato estándar.

### Objetivo

Desacoplar completamente la capa de dominio de la capa HTTP de DRF, estructurando excepciones de Python limpias con mensajes y metadatos de contexto.

### Actor

Cualquier consumidor del backend en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/core` y todos los módulos de negocio

### Entidades involucradas

`DomainError`, `EntityNotFoundError`, `BusinessRuleViolationError`, `ConflictError`, `custom_exception_handler`.

### Reglas de negocio

1. Ninguna función en `services.py` o `selectors.py` puede importar `rest_framework.exceptions` ni `rest_framework.status`.
2. Toda excepción de negocio debe heredar de `DomainError` e incluir un `message` legible y un `code` alfanumérico en mayúsculas.
3. El exception handler debe mapear: `EntityNotFoundError` -> `404`, `ConflictError` / `InvalidStateTransitionError` -> `409`, `BusinessRuleViolationError` -> `400`.
4. Las respuestas deben mantener la estructura `{ "error": { "code": ..., "message": ..., "details": ... } }`.

### Contrato esperado

Respuesta automática ante `InsufficientStockError`:
```json
{
  "error": {
    "code": "INSUFFICIENT_STOCK",
    "message": "Stock insuficiente para el producto 'Monitor 4K'.",
    "details": { "requested": 3, "available": 1 },
    "timestamp": "2026-09-22T15:00:00Z"
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

Validación de consistencia en el manejo de errores.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Excepción de dominio lanzada con `details` nulo o con tipos no serializables a JSON.

### Casos de error

Mapeo determinista de cada excepción a su status code exacto.

### Consideraciones de seguridad

Garantizar que las excepciones de dominio no filtren credenciales ni datos de conexión a bases de datos.

### Consideraciones de rendimiento

Garantizar presupuesto de consultas O(1) evitando el problema N+1 mediante `select_related` y `prefetch_related`. Uso de índices B-Tree específicos y selección acotada de columnas mediante `only()` o `defer()`.

### Fundamentos de Python relacionados

Herencia de clases de excepción (`class InsufficientStockError(BusinessRuleViolationError):`), inicializadores con atributos personalizados (`self.code`, `self.details`).

### Conceptos Django relacionados

Separación arquitectónica de concerns: Dominio agnóstico al framework web.

### Conceptos DRF relacionados

`custom_exception_handler(exc, context)` reconociendo `isinstance(exc, DomainError)`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

Principio de Arquitectura Limpia: El núcleo del negocio (servicios) no depende de la capa de entrega (DRF/HTTP).

### Dependencias entre módulos

Todos los módulos heredan sus excepciones de `apps.core.exceptions.DomainError`.

### Antes de programar

1. ¿Por qué lanzar `raise rest_framework.exceptions.ValidationError` dentro de un archivo `services.py` viola el principio de desacoplamiento arquitectónico?
2. ¿Cómo permite esta separación reutilizar los mismos servicios en un script de consola CLI o en tareas Celery sin cambios?

### Pruebas mínimas

1. Invocar un servicio que lance `InsufficientStockError` desde un test unitario sin levantar cliente HTTP -> Verificar que la excepción de Python se capture normalmente con sus atributos.
2. Invocar el endpoint HTTP que dispara esa regla y verificar que la respuesta sea `400 Bad Request` con el JSON formateado.

### Pruebas negativas

1. Probar que una excepción no mapeada (`ZeroDivisionError`) sea capturada como `INTERNAL_SERVER_ERROR` `500` sin caerse el proceso.

### Documentación

Documentar la taxonomía de excepciones de dominio en la guía de desarrollo del proyecto.

### Explicación posterior

Explica cómo la inversión de dependencias y el desacoplamiento de la capa HTTP facilita la migración o adición de nuevos canales de entrega (GraphQL, gRPC, CLI) sobre los mismos servicios de negocio.

### Aplicación profesional

Arquitectura de software empresarial, Domain-Driven Design (DDD) y Clean Architecture en Python.

### Reto adicional

Agregar metadatos de contexto automático a las excepciones de dominio (como el ID de la entidad involucrada) para enriquecer la respuesta al cliente.
