# Ejercicio 020 — Protección de Endpoints y Clases de Permisos en DRF

[← Ejercicio 019](../ejercicio_019/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 021 →](../ejercicio_021/README.md)

---

### Contexto de negocio

Actualmente los endpoints del catálogo están abiertos a cualquier usuario anónimo. El negocio requiere que las operaciones de consulta (`GET`) sigan siendo públicas, pero cualquier operación de creación (`POST`), modificación (`PATCH`) o eliminación (`DELETE`) requiera obligatoriamente que el usuario esté autenticado en el sistema.

### Estado actual del sistema

Catálogo público y sistema de autenticación JWT funcionando.

### Nueva necesidad

Configurar permisos granulares en `apps/catalog/views.py` usando `permissions.IsAuthenticatedOrReadOnly` o clases de permisos personalizadas.

### Objetivo

Dominar el sistema de permisos de DRF (`permission_classes`), la diferencia entre permisos a nivel de vista y permisos a nivel de objeto, y el manejo de cabeceras `Authorization: Bearer <token>`.

### Actor

Usuario Anónimo vs Usuario Autenticado en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`ProductListCreateAPIView`, `ProductRetrieveUpdateDestroyAPIView`, `permissions.IsAuthenticatedOrReadOnly`.

### Reglas de negocio

1. Cualquier visitante puede ejecutar `GET /api/v1/catalog/products/` y `GET /api/v1/catalog/products/{id}/`.
2. Solo usuarios autenticados con un JWT válido pueden ejecutar `POST`, `PUT`, `PATCH` y `DELETE`.
3. Peticiones de modificación sin token deben responder `401 Unauthorized`.
4. Peticiones con tokens malformados o expirados deben responder `401 Unauthorized`.

### Contrato esperado

Creación con Token:
- `POST /api/v1/catalog/products/`
  Header: `Authorization: Bearer eyJhbGciOi...`
  Body: `{ "sku": "PROD-AUTH-01", "name": "Teclado Mecanico", ... }`
  Response: `201 Created`

Creación sin Token:
- `POST /api/v1/catalog/products/` (Sin cabecera Authorization)
  Response: `401 Unauthorized`

### Persistencia

No aplica cambios adicionales de esquema. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

`IsAuthenticatedOrReadOnly` aplicada en las vistas del catálogo.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Cabecera `Authorization` enviada sin el prefijo `Bearer ` o con espacios extra.

### Casos de error

`401 Unauthorized` con código `AUTHENTICATION_FAILED`.

### Consideraciones de seguridad

Nunca confiar en datos de identidad enviados en el body (ej. `user_id`); obtener siempre al usuario desde `request.user` autenticado.

### Consideraciones de rendimiento

Verificación rápida en memoria de la firma del JWT.

### Fundamentos de Python relacionados

Inspección de atributos de objeto (`request.user.is_authenticated`).

### Conceptos Django relacionados

`HttpRequest.user`, integración con `AnonymousUser`.

### Conceptos DRF relacionados

`permission_classes`, `permissions.BasePermission`, `permissions.IsAuthenticated`, `permissions.IsAuthenticatedOrReadOnly`.

### PostgreSQL

No requiere queries si el token es válido y no toca tablas adicionales.

### Arquitectura

El módulo `apps/catalog` utiliza la infraestructura de autenticación de `apps/users` mediante la interfaz estándar de DRF.

### Dependencias entre módulos

`apps/catalog` depende conceptualmente de la autenticación de `apps/users` mediada por DRF.

### Antes de programar

1. ¿Qué diferencia conceptual existe entre el código HTTP 401 (Unauthorized) y el código 403 (Forbidden)?
2. ¿Cómo determina DRF si una petición es de lectura o de escritura en `IsAuthenticatedOrReadOnly`?

### Pruebas mínimas

1. Consultar `GET /api/v1/catalog/products/` sin cabecera de autenticación -> Verificar `200 OK`.
2. Enviar `POST` con token JWT válido -> Verificar `201 Created`.

### Pruebas negativas

1. Enviar `POST` sin cabecera de autorización -> Verificar `401 Unauthorized`.
2. Enviar `POST` con un token expirado -> Verificar `401 Unauthorized`.

### Documentación

Documentar los requisitos de autenticación por método HTTP en el esquema OpenAPI.

### Explicación posterior

Explica los métodos `has_permission(self, request, view)` y `has_object_permission(self, request, view, obj)` en `BasePermission` y en qué momento del ciclo de vida se evalúa cada uno.

### Aplicación profesional

Protección de APIs públicas con áreas administrativas o de escritura controlada.

### Reto adicional

Crear una clase de permiso personalizada `IsStaffOrReadOnly` que exija que el usuario autenticado tenga además `request.user.is_staff == True` para modificar el catálogo.
