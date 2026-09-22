# Ejercicio 024 — Permisos Dinámicos basados en Rol y Estado del Recurso

[← Ejercicio 023](../ejercicio_023/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 025 →](../ejercicio_025/README.md)

---

### Contexto de negocio

En el catálogo existen productos en diferentes estados: `DRAFT` (borrador), `PUBLISHED` (publicado) y `ARCHIVED` (archivado). Las reglas de acceso son dinámicas: los clientes solo pueden ver productos `PUBLISHED`; los gestores pueden ver borradores; pero nadie (ni siquiera un gestor) puede modificar un producto `ARCHIVED` a menos que sea un Administrador del sistema.

### Estado actual del sistema

Catálogo con productos y sistema RBAC en `apps/users`.

### Nueva necesidad

Agregar el campo `status` (`DRAFT`, `PUBLISHED`, `ARCHIVED`) a `Product` e implementar una clase de permiso compleja a nivel de objeto (`ProductStatePermission`) que combine el rol del usuario y el estado actual de la entidad.

### Objetivo

Dominar permisos contextuales y dinámicos a nivel de objeto en DRF, integrando el estado del recurso y los privilegios del actor.

### Actor

Cliente, Gestor de Catálogo, Administrador

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product` (con `status`), `ProductStatePermission` (`BasePermission`).

### Reglas de negocio

1. `GET /products/{id}/`: Permitido a clientes si `status == PUBLISHED`. Permitido a `CATALOG_MANAGER` y `ADMIN` en cualquier estado.
2. `PATCH /products/{id}/`: Permitido a `CATALOG_MANAGER` solo si `status != ARCHIVED`. Si está `ARCHIVED`, solo `ADMIN` puede modificarlo.
3. Intentar modificar un producto archivado sin ser admin debe responder `403 Forbidden` con mensaje explicativo: 'Los productos archivados están bloqueados'.

### Contrato esperado

Gestor intentando editar producto archivado:
- `PATCH /api/v1/catalog/products/{id_archivado}/` (Token Gestor)
  Response: `403 Forbidden` `{ "error": { "code": "ARCHIVED_RESOURCE_LOCKED", "message": "..." } }`

Admin editando producto archivado:
- `PATCH /api/v1/catalog/products/{id_archivado}/` (Token Admin)
  Response: `200 OK`

### Persistencia

Campo `status` en tabla `catalog_products`. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

`ProductStatePermission` implementando `has_object_permission`.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Cliente intentando adivinar el ID de un producto en estado `DRAFT` (debe responder `404 Not Found` en el QuerySet).

### Casos de error

`403 Forbidden` ante operaciones sobre estados bloqueados.

### Consideraciones de seguridad

Garantizar que el queryset base filtre según el rol antes de llegar a la vista (`Product.objects.filter(status='PUBLISHED')` para clientes).

### Consideraciones de rendimiento

Índice compuesto sobre `(status, is_active)` en PostgreSQL.

### Fundamentos de Python relacionados

Lógica booleana compuesta, evaluación de estados mediante Enums.

### Conceptos Django relacionados

`models.TextChoices` para estados del producto.

### Conceptos DRF relacionados

`has_object_permission(self, request, view, obj)`, `check_object_permissions(request, obj)`.

### PostgreSQL

`CREATE INDEX idx_products_status ON catalog_products (status, is_active)`.

### Arquitectura

La lógica de permiso contextual reside en `apps/catalog/permissions.py`.

### Dependencias entre módulos

`apps/catalog` utiliza la información de rol de `request.user`.

### Antes de programar

1. ¿Por qué `has_object_permission` no se ejecuta en métodos `POST` de creación y solo en `GET`, `PUT`, `PATCH`, `DELETE` sobre instancias individuales?
2. ¿Por qué es vital filtrar el QuerySet en `get_queryset()` además de tener `has_object_permission`?

### Pruebas mínimas

1. Autenticarse como Gestor y modificar un producto `DRAFT` -> Verificar `200 OK`.
2. Autenticarse como Admin y modificar un producto `ARCHIVED` -> Verificar `200 OK`.

### Pruebas negativas

1. Autenticarse como Gestor e intentar modificar un producto `ARCHIVED` -> Verificar `403 Forbidden`.
2. Consultar como anónimo un producto `DRAFT` -> Verificar `404 Not Found`.

### Documentación

Documentar la matriz de permisos por estado y rol en el README de catálogo.

### Explicación posterior

Explica la secuencia exacta en que DRF ejecuta: autenticación -> `has_permission()` -> obtención de objeto -> `has_object_permission()` -> serialización/ejecución.

### Aplicación profesional

Sistemas editoriales, flujos de aprobación de compras, ciclos de vida de contratos y documentos legales.

### Reto adicional

Implementar una acción personalizada `POST /api/v1/catalog/products/{id}/archive/` que cambie el estado a `ARCHIVED` y solo pueda ser invocada por Administradores.
