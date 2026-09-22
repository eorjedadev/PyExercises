# Ejercicio 018 — Autenticación con JWT (JSON Web Tokens) y Emisión de Tokens

[← Ejercicio 017](../ejercicio_017/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 019 →](../ejercicio_019/README.md)

---

### Contexto de negocio

Para soportar clientes desacoplados (Single Page Applications y apps móviles iOS/Android), la plataforma debe implementar autenticación sin estado (stateless) mediante JSON Web Tokens (JWT). El backend debe emitir un `access_token` de vida corta para autorizar peticiones y un `refresh_token` de vida más larga para renovar credenciales.

### Estado actual del sistema

Modelo `User` y endpoint de registro operativos en `apps/users`.

### Nueva necesidad

Integrar `djangorestframework-simplejwt`, configurar la emisión de tokens en `apps/users/urls.py` (`POST /api/v1/users/token/`) y personalizar los claims del payload JWT para incluir `user_id` y `email`.

### Objetivo

Comprender la anatomía de un JWT (Header, Payload, Signature), configurar SimpleJWT en Django, emitir tokens tras validar credenciales y comprender la autenticación stateless en DRF.

### Actor

Usuario Registrado en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/users` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`User`, `TokenObtainPairView`, `CustomTokenObtainPairSerializer`.

### Reglas de negocio

1. El usuario debe enviar sus credenciales (`email` y `password`).
2. Si las credenciales son correctas y el usuario está activo (`is_active=True`), se devuelven `access` y `refresh` tokens.
3. Si el usuario está inactivo o las credenciales son incorrectas, debe responder `401 Unauthorized` con un mensaje genérico para evitar enumeración de usuarios.
4. El `access_token` debe tener un tiempo de expiración corto (ej. 15 a 30 minutos).

### Contrato esperado

Login / Obtener Token:
- `POST /api/v1/users/token/`
  Request Body: `{"email": "dev.junior@empresa.com", "password": "ClaveSuperSegura2026!"}`
  Response: `200 OK`
  ```json
  {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
  ```

### Persistencia

SimpleJWT valida la contraseña contra el hash en `users_user`.

### Relaciones

`User`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

`AllowAny` para el endpoint de obtención de token.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación de credenciales criptográficas mediante `authenticate()`.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Usuario con `is_active=False` intentando autenticarse (debe rechazarse con `401 Unauthorized`).

### Casos de error

`401 Unauthorized` con código `INVALID_CREDENTIALS` cuando email o password no coinciden.

### Consideraciones de seguridad

Firmar los tokens con una clave secreta robusta (`SIGNING_KEY`), nunca incluir contraseñas ni datos altamente sensibles en el payload público del JWT.

### Consideraciones de rendimiento

La autenticación JWT no requiere consultar la base de datos en cada petición subsecuente si la firma criptográfica es válida.

### Fundamentos de Python relacionados

Criptografía simétrica (HMAC-SHA256), codificación Base64Url, marcas de tiempo UNIX (`exp`, `iat`).

### Conceptos Django relacionados

`django.contrib.auth.authenticate`, configuración de middlewares de autenticación.

### Conceptos DRF relacionados

`DEFAULT_AUTHENTICATION_CLASSES = ['rest_framework_simplejwt.authentication.JWTAuthentication']` en settings.

### PostgreSQL

`SELECT * FROM users_user WHERE email = ...`.

### Arquitectura

Módulo de autenticación en `apps/users`, proveyendo tokens para todo el sistema.

### Dependencias entre módulos

`config/settings.py` configura `SIMPLE_JWT`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Cuáles son las 3 partes de un JWT y por qué la firma impide que un cliente altere el payload?
2. ¿Por qué es un error crítico de seguridad almacenar contraseñas o números de tarjeta de crédito en el payload de un JWT?

### Pruebas mínimas

1. Enviar credenciales válidas y comprobar que la respuesta retorne status `200` y contenga las claves `access` y `refresh`.
2. Decodificar el token `access` y verificar que contenga el `user_id` y `email` en sus claims.

### Pruebas negativas

1. Enviar password incorrecto y verificar respuesta `401 Unauthorized`.
2. Enviar email de un usuario inactivo (`is_active=False`) y comprobar rechazo `401`.

### Documentación

Documentar la estructura del token y los tiempos de expiración en la documentación de seguridad.

### Explicación posterior

Explica qué diferencia existe entre autenticación por sesiones (stateful) y autenticación por JWT (stateless), y qué ventajas ofrece JWT para APIs REST.

### Aplicación profesional

Estándar de la industria para autenticación en arquitecturas SPA (React, Vue, Angular), móviles y servicios desacoplados.

### Reto adicional

Personalizar el serializer del token para incluir el nombre completo del usuario (`full_name`) y su rol directamente en el payload del JWT.
