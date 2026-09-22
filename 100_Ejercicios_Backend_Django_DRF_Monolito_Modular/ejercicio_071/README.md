# Ejercicio 071 — Transiciones Suaves de Contratos y Deprecación de Campos con Sunset Headers

[← Ejercicio 070](../ejercicio_070/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 072 →](../ejercicio_072/README.md)

---

### Contexto de negocio

Antes de eliminar por completo un campo obsoleto de la API en una versión futura (ej. el campo `old_price_str`), el backend debe advertir a los desarrolladores y clientes mediante cabeceras estándar HTTP de deprecación (`Deprecation: true`, `Sunset: Wed, 11 Nov 2026 00:00:00 GMT`). Esto permite a los consumidores migrar con meses de anticipación sin sorpresas ni roturas inesperadas.

### Estado actual del sistema

Sistema de versionado implementado. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Crear un decorador o middleware `deprecated_endpoint(sunset_date=...)` en `apps/core` que inyecte las cabeceras estándar de deprecación `Deprecation` y `Sunset` según las normas RFC 8594 / draft-ietf-httpapi-deprecation-header.

### Objetivo

Dominar la gestión profesional de deprecación y obsolescencia de APIs REST, comunicando fechas de apagado mediante cabeceras HTTP estándar y logs de advertencia.

### Actor

Desarrollador Integrador / Cliente de API

### Módulo responsable

`apps/core` aplicado en endpoints en proceso de retiro

### Entidades involucradas

`deprecated_endpoint` (decorador / middleware), cabeceras HTTP `Deprecation`, `Sunset`, `Link`.

### Reglas de negocio

1. Todo endpoint o versión marcada como obsoleta debe responder con las cabeceras HTTP:
   - `Deprecation: @1762819200` (timestamp UNIX de cuando fue marcado obsoleto o booleano `true`)
   - `Sunset: Wed, 11 Nov 2026 00:00:00 GMT` (fecha exacta de apagado definitivo)
   - `Link: <https://api.empresa.com/docs/migration-v2>; rel="deprecation"; type="text/html"`
2. El endpoint debe seguir funcionando con normalidad (status `200 OK`) hasta que se cumpla la fecha `Sunset`.
3. Se debe emitir una advertencia en los logs del servidor indicando el `User-Agent` del cliente que continúa usando el endpoint obsoleto.

### Contrato esperado

Respuesta de Endpoint Obsoleto:
- `GET /api/v1/catalog/old-products/`
  Response: `200 OK`
  Headers:
    `Deprecation: true`
    `Sunset: Wed, 11 Nov 2026 00:00:00 GMT`
    `Link: <https://api.empresa.com/docs/migration>; rel="deprecation"`

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

Cliente que consulta el endpoint después de la fecha Sunset cumplida (el backend puede retornar `410 Gone` indicando que el recurso fue retirado definitivamente).

### Casos de error

`410 Gone` para endpoints cuya fecha de sunset ya pasó.

### Consideraciones de seguridad

Alertar a clientes sobre versiones antiguas que puedan contener algoritmos criptográficos débiles.

### Consideraciones de rendimiento

Garantizar presupuesto de consultas O(1) evitando el problema N+1 mediante `select_related` y `prefetch_related`. Uso de índices B-Tree específicos y selección acotada de columnas mediante `only()` o `defer()`.

### Fundamentos de Python relacionados

Decoradores de función en Python (`functools.wraps`), formateo de fechas HTTP según RFC 7231 (IMF-fixdate: `formatdate(usegmt=True)`).

### Conceptos Django relacionados

Manipulación de cabeceras en `HttpResponse`, `email.utils.formatdate`.

### Conceptos DRF relacionados

Decoradores sobre métodos de `APIView` y ViewSets.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

Utilidad transversal de gobernanza de APIs en `apps/core/deprecation.py`.

### Dependencias entre módulos

Cualquier módulo puede aplicar `@deprecated_endpoint` a sus vistas.

### Antes de programar

1. ¿Por qué apagar una API antigua sin previo aviso (Breaking Change sin Sunset) destruye la confianza de los clientes y socios de integración?
2. ¿Cómo permite la cabecera `Sunset` a los clientes automatizados alertar a sus propios equipos de que un servicio dejará de funcionar?

### Pruebas mínimas

1. Solicitar un endpoint decorado con `@deprecated_endpoint` -> Verificar que la respuesta retorne `200 OK` y contenga las cabeceras `Deprecation`, `Sunset` y `Link`.
2. Verificar que la fecha en `Sunset` cumpla con el formato estándar GMT de HTTP.

### Pruebas negativas

1. Simular una fecha de Sunset en el pasado y verificar que el endpoint responda `410 Gone` con mensaje de recurso retirado.

### Documentación

Documentar la política de ciclo de vida y deprecación de APIs en el portal de desarrolladores.

### Explicación posterior

Explica los estándares RFC 8594 (The Sunset HTTP Header Field) y RFC 9651 (Deprecation HTTP Header) y cómo las grandes empresas de tecnología gestionan la evolución de sus contratos públicos.

### Aplicación profesional

Gobernanza de APIs empresariales, migración ordenada de aplicaciones móviles y acuerdos de nivel de servicio (SLAs).

### Reto adicional

Registrar una métrica en los logs con el conteo diario de peticiones a endpoints obsoletos para monitorear el avance de la migración de clientes hacia la nueva versión.
