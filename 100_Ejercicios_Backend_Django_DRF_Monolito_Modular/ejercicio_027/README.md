# Ejercicio 027 — Flujo de Recuperación de Contraseña con Tokens Criptográficos

[← Ejercicio 026](../ejercicio_026/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 028 →](../ejercicio_028/README.md)

---

### Contexto de negocio

Si un usuario olvida su contraseña, debe existir un mecanismo seguro de recuperación. El sistema nunca debe revelar si un correo electrónico existe o no al solicitar el restablecimiento (prevención de enumeración de usuarios). El token generado debe ser temporal, criptográficamente seguro y de un solo uso.

### Estado actual del sistema

Módulo `apps/users` con autenticación operativa.

### Nueva necesidad

Implementar dos endpoints en `apps/users`: `POST /api/v1/users/password-reset/` (solicitud de token) y `POST /api/v1/users/password-reset-confirm/` (confirmación y cambio de clave con token y uidb64).

### Objetivo

Diseñar un flujo completo de recuperación de contraseña en backend, utilizando `PasswordResetTokenGenerator` de Django y codificación segura `urlsafe_base64_encode`.

### Actor

Usuario Anónimo que olvidó su clave en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/users` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`User`, `PasswordResetTokenGenerator`, servicio `request_password_reset`, servicio `confirm_password_reset`.

### Reglas de negocio

1. Al solicitar recuperación, si el email existe, se genera un token criptográfico vinculado al estado actual de la contraseña del usuario.
2. La respuesta HTTP a la solicitud de recuperación debe ser SIEMPRE `200 OK` con un mensaje genérico ('Si el correo existe en nuestro sistema, recibirá instrucciones'), exista o no el correo en la base de datos.
3. El token debe expirar automáticamente (por defecto tras `PASSWORD_RESET_TIMEOUT` segundos).
4. Una vez cambiada la contraseña, el token debe quedar automáticamente invalidado para evitar reusos.

### Contrato esperado

1. Solicitar Reseteo:
- `POST /api/v1/users/password-reset/`
  Body: `{"email": "usuario@empresa.com"}`
  Response: `200 OK` `{"message": "Si el correo está registrado, se han enviado las instrucciones."}`

2. Confirmar Nuevo Password:
- `POST /api/v1/users/password-reset-confirm/`
  Body: `{"uidb64": "MQ", "token": "c12345-6789abcdef...", "new_password": "NuevaClaveSegura2026!"}`
  Response: `200 OK` `{"message": "La contraseña ha sido actualizada exitosamente."}`

### Persistencia

Actualización de `password` hasheado y `last_login` en `users_user`.

### Relaciones

`User`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

`AllowAny` validada por la posesión del token criptográfico.

### Validaciones

Validación de fortaleza de la nueva contraseña con validadores de Django.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Usuario que solicita reseteo, cambia su clave con el token, e intenta usar el mismo token por segunda vez (debe ser rechazado como inválido).

### Casos de error

`400 Bad Request` si el token es inválido, expiró o el `uidb64` está corrupto.

### Consideraciones de seguridad

No revelar existencia de usuarios en respuestas de error (Timing attacks y Enumeration attacks).

### Consideraciones de rendimiento

`PasswordResetTokenGenerator` genera y valida tokens sin necesidad de almacenar filas en base de datos gracias al HMAC del hash de contraseña actual.

### Fundamentos de Python relacionados

Codificación Base64 segura para URLs (`urlsafe_base64_encode`, `urlsafe_base64_decode`), firmas HMAC.

### Conceptos Django relacionados

`django.contrib.auth.tokens.default_token_generator`, `django.utils.http.urlsafe_base64_encode`, `PASSWORD_RESET_TIMEOUT`.

### Conceptos DRF relacionados

Serializadores de validación de tokens y nuevas contraseñas.

### PostgreSQL

`UPDATE users_user SET password = ... WHERE id = ...`.

### Arquitectura

Los servicios en `apps/users/services.py` encapsulan la lógica de emisión y verificación de tokens.

### Dependencias entre módulos

Interno a `apps/users`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué responder 'El usuario no existe' en un formulario de recuperación de clave es un fallo de privacidad y seguridad?
2. ¿Cómo logra Django que el token de recuperación quede invalidado automáticamente en cuanto el usuario cambia su contraseña sin guardar el token en la base de datos?

### Pruebas mínimas

1. Solicitar reseteo para un usuario existente, obtener el `uidb64` y `token`, y enviar la confirmación con una contraseña nueva -> Verificar cambio exitoso.
2. Comprobar que el usuario ahora pueda autenticarse con la nueva contraseña y no con la anterior.

### Pruebas negativas

1. Intentar reusar el mismo token tras haber cambiado la clave -> Verificar rechazo `400 Bad Request`.
2. Enviar un email no registrado a `/password-reset/` -> Verificar que responda `200 OK` idéntico sin lanzar error.

### Documentación

Documentar el flujo de dos pasos de recuperación de contraseña en la guía de API.

### Explicación posterior

Explica el funcionamiento interno de `PasswordResetTokenGenerator`: cómo utiliza un HMAC SHA-256 compuesto por el ID del usuario, su contraseña hasheada actual y la fecha de último login para validar el token sin estado.

### Aplicación profesional

Flujo de autoservicio de recuperación de cuentas en cualquier producto digital moderno.

### Reto adicional

Registrar un evento de seguridad en el módulo de auditoría cada vez que se complete un cambio de contraseña exitoso.
