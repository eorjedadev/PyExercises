# Ejercicio 019 — Rotación de Refresh Tokens, Expiración y Revocación

[← Ejercicio 018](../ejercicio_018/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 020 →](../ejercicio_020/README.md)

---

### Contexto de negocio

Si un `access_token` es interceptado, su impacto debe estar acotado por una expiración corta. Para mantener la sesión abierta sin pedirle la contraseña al usuario constantemente, el cliente debe usar el `refresh_token`. Para máxima seguridad, cada vez que se usa un refresh token, debe invalidarse y emitirse uno nuevo (Token Rotation y Blacklisting).

### Estado actual del sistema

Emisión básica de JWT en `apps/users`. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Configurar `TokenRefreshView` con `ROTATE_REFRESH_TOKENS = True` y `BLACKLIST_AFTER_ROTATION = True`, e implementar un endpoint de Logout (`POST /api/v1/users/logout/`) que envíe el refresh token a la lista negra.

### Objetivo

Dominar el ciclo de vida de tokens de refresco, rotación automática y revocación explícita mediante lista negra (`simplejwt.token_blacklist`) en PostgreSQL.

### Actor

Usuario Autenticado en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/users` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`TokenRefreshView`, `TokenBlacklistView`, tabla `token_blacklist_outstandingtoken` en PostgreSQL.

### Reglas de negocio

1. El endpoint `POST /api/v1/users/token/refresh/` recibe un `refresh_token` válido y devuelve un nuevo `access_token` y un nuevo `refresh_token`.
2. El `refresh_token` utilizado queda inmediatamente invalidado en la lista negra.
3. Si un cliente intenta reusar un refresh token ya utilizado, la petición debe ser rechazada con `401 Unauthorized`.
4. El endpoint `POST /api/v1/users/logout/` recibe el refresh token actual y lo revoca permanentemente.

### Contrato esperado

Refresco con Rotación:
- `POST /api/v1/users/token/refresh/`
  Request: `{"refresh": "token_actual..."}`
  Response: `200 OK` `{ "access": "nuevo_access...", "refresh": "nuevo_refresh..." }`

Cierre de Sesión (Logout):
- `POST /api/v1/users/logout/`
  Request: `{"refresh": "token_actual..."}`
  Response: `204 No Content`

### Persistencia

Persistencia de tokens emitidos y revocados en las tablas de `rest_framework_simplejwt.token_blacklist` en PostgreSQL.

### Relaciones

Tokens vinculados a `User`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

El logout requiere `IsAuthenticated`; el refresh requiere token de refresco válido.

### Autorización

Verificación de validez criptográfica y no presencia en lista negra.

### Validaciones

Validar firma y expiración del refresh token.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Reutilización de un refresh token robado o caducado.

### Casos de error

`401 Unauthorized` con detalle `Token is blacklisted or invalid`.

### Consideraciones de seguridad

La rotación con lista negra previene ataques de repetición y permite revocar accesos inmediatamente sin esperar la expiración del refresh token.

### Consideraciones de rendimiento

Índice en base de datos sobre el campo `jti` (JWT ID) en la tabla de lista negra para consultas instantáneas.

### Fundamentos de Python relacionados

Manipulación de tiempos con `datetime.timedelta`, excepciones de JWT (`TokenError`, `InvalidToken`).

### Conceptos Django relacionados

`INSTALLED_APPS += ['rest_framework_simplejwt.token_blacklist']`, migraciones de blacklist.

### Conceptos DRF relacionados

`TokenRefreshView`, `TokenBlacklistView`, configuración de `SIMPLE_JWT` en settings.

### PostgreSQL

`INSERT INTO token_blacklist_blacklistedtoken ...`.

### Arquitectura

Gestión de ciclo de vida de credenciales dentro de `apps/users`.

### Dependencias entre módulos

Interno a `apps/users` con soporte de `simplejwt`.

### Antes de programar

1. ¿Por qué un access token no se puede revocar de forma puramente stateless y por qué su tiempo de vida debe ser corto?
2. ¿Cómo detecta SimpleJWT el intento de reuso de un refresh token ya rotado?

### Pruebas mínimas

1. Obtener un par de tokens, enviar el refresh token a `/token/refresh/` y comprobar que se reciba un nuevo par.
2. Enviar el refresh token anterior nuevamente y comprobar que sea rechazado con status `401`.
3. Probar el endpoint `/logout/` y verificar que el token quede invalidado.

### Pruebas negativas

1. Enviar un string corrupto como refresh token y verificar respuesta `401`.

### Documentación

Documentar la política de rotación y los endpoints de refresco y logout en la guía de seguridad.

### Explicación posterior

Explica el compromiso entre escalabilidad stateless (access tokens puros) y control de seguridad stateful (blacklist de refresh tokens en base de datos).

### Aplicación profesional

Autenticación segura de nivel bancario y corporativo cumpliendo con estándares OWASP.

### Reto adicional

Crear un comando de mantenimiento `python manage.py flushexpiredtokens` para purgar periódicamente tokens expirados de la base de datos de PostgreSQL.
