# Ejercicio 029 — Desactivación de Cuentas y Soft Delete vs Eliminación Física

[← Ejercicio 028](../ejercicio_028/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 030 →](../ejercicio_030/README.md)

---

### Contexto de negocio

Cuando un usuario decide cerrar su cuenta o cuando un administrador desactiva a un cliente fraudulento, eliminar físicamente la fila con `DELETE FROM users_user` provocaría la destrucción en cascada de pedidos históricos, facturas y registros de auditoría. Se requiere una estrategia de desactivación lógica (Soft Delete) controlada.

### Estado actual del sistema

Módulos `apps/users` y `apps/customers` activos.

### Nueva necesidad

Implementar el flujo de desactivación de cuenta (`POST /api/v1/users/me/deactivate/`), invalidando tokens activos, marcando `is_active = False` y excluyendo usuarios inactivos de listados regulares sin romper referencias históricas.

### Objetivo

Comprender cuándo aplicar Soft Delete vs eliminación física, las consecuencias de `on_delete` en cascada y cómo gestionar el ciclo de vida de identidades inactivas.

### Actor

Usuario Propietario / Administrador con permisos administrativos y credenciales de acceso seguras.

### Módulo responsable

`apps/users` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`User`, servicio `deactivate_user_account`.

### Reglas de negocio

1. Un usuario autenticado puede solicitar la desactivación de su propia cuenta confirmando su contraseña actual.
2. Al desactivarse, `is_active` pasa a `False` y se revoca inmediatamente cualquier sesión o refresh token activo.
3. Un usuario inactivo no puede iniciar sesión ni generar nuevos tokens.
4. Todos los registros históricos de auditoría y compras deben conservar la referencia al ID del usuario.

### Contrato esperado

Desactivar Mi Cuenta:
- `POST /api/v1/users/me/deactivate/`
  Header: `Authorization: Bearer <token>`
  Body: `{"current_password": "ClaveSuperSegura2026!", "reason": "Ya no uso el servicio"}`
  Response: `200 OK` `{"message": "Su cuenta ha sido desactivada correctamente."}`

### Persistencia

Actualización de `is_active = false` en `users_user` y registro de auditoría.

### Relaciones

`User`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar que `current_password` coincida con el hash actual del usuario mediante `check_password()`.

### Transacciones

Transacción atómica: marcar inactivo + revocar tokens + auditar evento.

### Casos límite

Usuario que intenta desactivar una cuenta ya desactivada.

### Casos de error

`400 Bad Request` si la contraseña actual es incorrecta.

### Consideraciones de seguridad

Exigir re-autenticación con contraseña para operaciones destructivas como desactivación de cuenta para prevenir que una sesión descuidada sea saboteada.

### Consideraciones de rendimiento

Los índices en PostgreSQL que filtran por `is_active = true` aceleran las consultas de usuarios operativos.

### Fundamentos de Python relacionados

Método `user.check_password(raw_password)`. Tipado estricto con `typing` (`Optional`, `Dict`, `List`), decoradores, dataclasses, manejo estructurado de excepciones y programación modular.

### Conceptos Django relacionados

`user.is_active`, custom managers para filtrar activos por defecto vs método explícito.

### Conceptos DRF relacionados

Endpoint de acción personalizado con validación de contraseña previa.

### PostgreSQL

`UPDATE users_user SET is_active = false, updated_at = NOW() WHERE id = ...`.

### Arquitectura

El servicio `apps/users/services.py:deactivate_user_account(...)` encapsula la orquestación de la desactivación.

### Dependencias entre módulos

`apps/users` invoca `apps.audit.services.record_audit_event`.

### Antes de programar

1. ¿Por qué ejecutar `user.delete()` físico en una base de datos de producción con órdenes y facturas asociadas es un desastre operativo?
2. ¿Por qué es crucial verificar la contraseña actual del usuario antes de desactivar la cuenta?

### Pruebas mínimas

1. Crear un usuario, autenticarse, enviar desactivación con contraseña correcta -> Verificar que `is_active` sea `False`.
2. Intentar autenticarse nuevamente con las mismas credenciales -> Verificar `401 Unauthorized`.

### Pruebas negativas

1. Enviar desactivación con contraseña incorrecta -> Verificar `400 Bad Request` y que la cuenta permanezca activa.

### Documentación

Documentar la política de desactivación de cuentas en el módulo de usuarios.

### Explicación posterior

Explica los pros y contras del Soft Delete generalizado vs Soft Delete explícito por estado del negocio (`is_active`, `status = CANCELLED`).

### Aplicación profesional

Gestión de ciclo de vida de usuarios, cumplimiento del derecho de supresión/cancelación en GDPR y retención de datos contables.

### Reto adicional

Implementar un mecanismo para que un Administrador pueda reactivar una cuenta (`POST /api/v1/users/{id}/reactivate/`) registrando la justificación en auditoría.
