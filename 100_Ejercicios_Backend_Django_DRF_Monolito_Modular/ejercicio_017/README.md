# Ejercicio 017 — Registro de Usuarios y Validación Criptográfica de Contraseñas

[← Ejercicio 016](../ejercicio_016/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 018 →](../ejercicio_018/README.md)

---

### Contexto de negocio

Los nuevos usuarios deben poder registrarse en la plataforma enviando sus datos personales básicos y su contraseña. El backend debe aplicar políticas estrictas de seguridad de contraseñas (longitud mínima, complejidad, no similitud con datos personales, no contraseñas comunes) antes de crear la cuenta.

### Estado actual del sistema

Modelo `User` personalizado activo en `apps/users`.

### Nueva necesidad

Crear el endpoint `POST /api/v1/users/register/` con un serializer dedicado que integre `django.contrib.auth.password_validation.validate_password` y cree el usuario usando la capa de servicios.

### Objetivo

Construir un flujo de registro seguro en DRF, aplicando validadores de contraseñas estándar de Django y retornando respuestas limpias sin exponer datos sensibles.

### Actor

Usuario Anónimo (Visitante) en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/users` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`User`, `UserRegisterInputSerializer`, `UserPublicOutputSerializer`, servicio `register_user`.

### Reglas de negocio

1. El email no debe existir previamente en el sistema.
2. La contraseña debe pasar todos los validadores configurados en `AUTH_PASSWORD_VALIDATORS` de `settings.py`.
3. La contraseña debe enviarse como campo de solo escritura (`write_only=True`) y nunca debe devolverse en la respuesta JSON.
4. Tras el registro exitoso, el usuario queda en estado activo y se responde `201 Created`.

### Contrato esperado

Registro de Usuario:
- `POST /api/v1/users/register/`
  Request Body:
  ```json
  {
    "email": "dev.junior@empresa.com",
    "password": "ClaveSuperSegura2026!",
    "first_name": "Carlos",
    "last_name": "Mendoza"
  }
  ```
  Response: `201 Created`
  ```json
  {
    "id": "c1a2b3d4-0000-4000-8000-123456789abc",
    "email": "dev.junior@empresa.com",
    "first_name": "Carlos",
    "last_name": "Mendoza",
    "date_joined": "2026-09-22T10:00:00Z"
  }
  ```

### Persistencia

Inserción de nueva fila en tabla `users_user` con password hasheado.

### Relaciones

`User`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

`validate_password(password, user=User(...))` dentro del serializer para aplicar las reglas de seguridad de Django.

### Transacciones

No requerida para registro simple de usuario.

### Casos límite

Contraseña idéntica al correo electrónico o excesivamente común ('password123', '12345678').

### Casos de error

`400 Bad Request` con lista de motivos por los cuales la contraseña fue rechazada.

### Consideraciones de seguridad

Garantizar que el campo `password` tenga `write_only=True` en el serializer para evitar fugas accidentales en serializaciones posteriores.

### Consideraciones de rendimiento

El costo de hashing de contraseñas es deliberadamente alto en CPU para proteger contra ataques de fuerza bruta; mantener factores de trabajo adecuados.

### Fundamentos de Python relacionados

Excepciones de validación, paso de argumentos a funciones de seguridad.

### Conceptos Django relacionados

`django.contrib.auth.password_validation.validate_password`, `AUTH_PASSWORD_VALIDATORS`.

### Conceptos DRF relacionados

`serializers.CharField(write_only=True, style={'input_type': 'password'})`, `permissions.AllowAny`.

### PostgreSQL

`INSERT INTO users_user (id, email, password, ...) VALUES (...)`.

### Arquitectura

El servicio `apps/users/services.py:register_user(...)` encapsula la lógica pura de registro.

### Dependencias entre módulos

Interno a `apps/users`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué es fundamental que la validación de contraseñas ocurra antes de llamar a `set_password`?
2. ¿Por qué `password` debe ser `write_only=True` en el serializer?

### Pruebas mínimas

1. Enviar una petición válida con email único y contraseña robusta -> Verificar status `201` y que el password retornado NO esté en el JSON.
2. Verificar en base de datos que el password guardado sea un hash seguro.

### Pruebas negativas

1. Enviar una contraseña débil ('123') y verificar respuesta `400` con los errores de validación de Django.
2. Intentar registrar un email ya existente y verificar respuesta `400` con mensaje de duplicidad.

### Documentación

Documentar el endpoint de registro en la especificación OpenAPI de `apps/users`.

### Explicación posterior

Explica qué validadores de contraseñas vienen por defecto en Django (`UserAttributeSimilarityValidator`, `MinimumLengthValidator`, `CommonPasswordValidator`, `NumericPasswordValidator`) y cómo operan.

### Aplicación profesional

Módulo de onboarding de usuarios en cualquier producto digital SaaS o e-commerce.

### Reto adicional

Agregar un validador personalizado que exija al menos un carácter especial y un número en la contraseña.
