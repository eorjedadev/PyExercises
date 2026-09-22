# Ejercicio 023 — Control de Acceso Basado en Roles (RBAC) sin Dispersar if user.role

[← Ejercicio 022](../ejercicio_022/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 024 →](../ejercicio_024/README.md)

---

### Contexto de negocio

El sistema requiere soportar múltiples roles de negocio: `CUSTOMER` (cliente estándar), `CATALOG_MANAGER` (gestor de productos), `ORDERS_OPERATOR` (operador logístico) y `ADMIN` (administrador del sistema). Llenar las vistas de condicionales espagueti tipo `if request.user.role == 'ADMIN' or ...` hace que el sistema sea frágil y difícil de auditar.

### Estado actual del sistema

Autenticación y módulos de catálogo y clientes operativos.

### Nueva necesidad

Diseñar un sistema de roles y permisos explícitos en `apps/users`, modelar roles mediante Enums o Grupos, e implementar clases de permisos reutilizables (`IsCatalogManager`, `IsAdminRole`).

### Objetivo

Implementar Role-Based Access Control (RBAC) limpio y extensible en Django/DRF, centralizando la lógica de autorización en clases de permiso declarativas.

### Actor

Usuarios con diferentes roles de negocio

### Módulo responsable

`apps/users` y aplicado transversalmente

### Entidades involucradas

`User` (con campo `role` tipado con `TextChoices` o integración con `django.contrib.auth.models.Group`), clases de permiso (`HasRole`, `IsCatalogManager`).

### Reglas de negocio

1. Los roles válidos son `ADMIN`, `CATALOG_MANAGER`, `ORDERS_OPERATOR`, `CUSTOMER`.
2. Solo usuarios con rol `CATALOG_MANAGER` o `ADMIN` pueden crear, editar o eliminar productos en el catálogo.
3. Los usuarios con rol `CUSTOMER` solo tienen acceso de lectura al catálogo.
4. Si un usuario autenticado intenta realizar una acción fuera de su rol, debe responder `403 Forbidden` con mensaje descriptivo.

### Contrato esperado

Gestor de Catálogo creando producto:
- `POST /api/v1/catalog/products/` (Token de usuario con rol `CATALOG_MANAGER`)
  Response: `201 Created`

Cliente intentando crear producto:
- `POST /api/v1/catalog/products/` (Token de usuario con rol `CUSTOMER`)
  Response: `403 Forbidden`
  ```json
  {
    "error": {
      "code": "PERMISSION_DENIED",
      "message": "No tienes los permisos requeridos para gestionar el catálogo."
    }
  }
  ```

### Persistencia

Campo `role` en tabla `users_user` con tipo `VARCHAR(30)` o tabla intermedia de roles.

### Relaciones

`User`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Clase de permiso `IsCatalogManager` evaluando `request.user.role in [Role.CATALOG_MANAGER, Role.ADMIN]`.

### Validaciones

Validar que el rol asignado pertenezca al conjunto permitido de `TextChoices`.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Usuario autenticado cuyo rol fue revocado durante una sesión activa (la siguiente petición debe rechazarlo inmediatamente al evaluar `request.user.role`).

### Casos de error

`403 Forbidden` cuando el usuario está autenticado pero no tiene privilegios suficientes.

### Consideraciones de seguridad

Principio de mínimo privilegio: por defecto los nuevos usuarios reciben rol `CUSTOMER`.

### Consideraciones de rendimiento

El rol se carga junto con el usuario en la sesión/token, evitando consultas repetitivas.

### Fundamentos de Python relacionados

Uso de `enum.StrEnum` o `django.db.models.TextChoices` para tipado estricto de roles.

### Conceptos Django relacionados

`models.TextChoices`, propiedades de ayuda en el modelo (`user.is_catalog_manager`).

### Conceptos DRF relacionados

`permissions.BasePermission`, método `has_permission`, personalización de `message` en la clase de permiso.

### PostgreSQL

`ALTER TABLE users_user ADD COLUMN role VARCHAR(30) NOT NULL DEFAULT 'CUSTOMER'`.

### Arquitectura

`apps/users/permissions.py` centraliza las definiciones de permisos de roles; los demás módulos importan las clases de permiso de forma declarativa.

### Dependencias entre módulos

`apps/catalog` importa clases de permisos de `apps/users/permissions.py`.

### Antes de programar

1. ¿Por qué es perjudicial colocar chequeos de rol manuales (`if user.role == ...`) dentro del cuerpo de las funciones de vista en lugar de usar `permission_classes`?
2. ¿Cuál es la diferencia entre autenticación (¿quién eres?) y autorización (¿qué puedes hacer?)?

### Pruebas mínimas

1. Crear un usuario con rol `CATALOG_MANAGER`, autenticarse y crear un producto -> Verificar `201 Created`.
2. Crear un usuario con rol `CUSTOMER`, autenticarse e intentar crear un producto -> Verificar `403 Forbidden`.

### Pruebas negativas

1. Enviar petición de creación sin token -> Verificar `401 Unauthorized` (falla autenticación antes de evaluar permisos).

### Documentación

Documentar la matriz de roles y permisos en la sección de arquitectura de seguridad.

### Explicación posterior

Explica cómo se compone una lista de permisos en DRF (`permission_classes = [IsAuthenticated, IsCatalogManager]`) y cómo DRF evalúa cada permiso en orden cortocircuitando ante el primer fallo.

### Aplicación profesional

Sistemas empresariales B2B, ERPs, plataformas educativas y paneles de administración con control de acceso granular.

### Reto adicional

Implementar una factoría de permisos `HasAnyRole(*roles)` que permita declarar dinámicamente en cualquier vista: `permission_classes = [HasAnyRole('ADMIN', 'CATALOG_MANAGER')]`.
