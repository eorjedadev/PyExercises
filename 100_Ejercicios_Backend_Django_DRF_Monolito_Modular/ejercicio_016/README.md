# Ejercicio 016 — Modelo de Usuario Personalizado y Migración Inicial en apps/users

[← Ejercicio 015](../ejercicio_015/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 017 →](../ejercicio_017/README.md)

---

### Contexto de negocio

La plataforma necesita autenticar usuarios mediante correo electrónico único en lugar de nombre de usuario (username). Modificar el modelo de usuario de Django a mitad de un proyecto en producción es una de las operaciones más traumáticas y propensas a errores. Por ello, la arquitectura exige definir un `User` personalizado dentro del módulo `apps/users` desde el inicio.

### Estado actual del sistema

Módulos `apps/core` y `apps/catalog` funcionando.

### Nueva necesidad

Crear el módulo `apps/users` y definir un modelo `User` heredando de `AbstractBaseUser` y `PermissionsMixin`, configurando `EMAIL_FIELD = 'email'` y `USERNAME_FIELD = 'email'`.

### Objetivo

Implementar un Custom User Model profesional en Django, crear su `UserManager` personalizado con `create_user` y `create_superuser`, y configurar `AUTH_USER_MODEL = 'users.User'`.

### Actor

Desarrollador Backend / Sistema de Identidad

### Módulo responsable

`apps/users` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`User` (`id` UUID, `email`, `first_name`, `last_name`, `is_active`, `is_staff`, `is_superuser`, `date_joined`), `UserManager`.

### Reglas de negocio

1. El email es el identificador único para el inicio de sesión y debe normalizarse automáticamente a minúsculas (`normalize_email`).
2. No debe existir el campo `username` en la base de datos.
3. La clave primaria debe ser UUID v4 para evitar enumeración secuencial de usuarios.
4. `is_active` debe ser `True` por defecto para usuarios registrados.

### Contrato esperado

Creación mediante `python manage.py createsuperuser` y persistencia en tabla `users_user` de PostgreSQL.

### Persistencia

Tabla `users_user` en PostgreSQL con restricciones `UNIQUE` e índice sobre `email`.

### Relaciones

Raíz del módulo de identidad; servirá como clave foránea para perfiles y auditorías posteriores.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

Soporte para flags de Django (`is_staff`, `is_superuser`) y grupos de permisos.

### Validaciones

Validación de formato de email (`EmailValidator`) y obligatoriedad.

### Transacciones

Operación atómica obligatoria mediante `transaction.atomic()`. Garantiza que todas las mutaciones en la base de datos se confirmen de forma íntegra o se reviertan totalmente (Rollback) ante fallos.

### Casos límite

Email con mayúsculas mezcladas (`User@Example.COM` -> debe guardarse como `user@example.com`).

### Casos de error

`ValueError` si se intenta crear un usuario sin email mediante el manager.

### Consideraciones de seguridad

Nunca almacenar contraseñas en texto plano; delegar el hashing a `set_password()` de Django.

### Consideraciones de rendimiento

Índice `db_index=True` sobre `email` en PostgreSQL para consultas de login instantáneas.

### Fundamentos de Python relacionados

Herencia múltiple de clases (`AbstractBaseUser`, `PermissionsMixin`), métodos de clase, tipado estricto.

### Conceptos Django relacionados

`AUTH_USER_MODEL = 'users.User'`, `BaseUserManager`, `normalize_email`, `AbstractBaseUser`.

### Conceptos DRF relacionados

Compatibilidad de DRF con el modelo de usuario personalizado de Django.

### PostgreSQL

`CREATE TABLE users_user (id UUID PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(128) NOT NULL, ...)`.

### Arquitectura

`apps/users` es el módulo central de autenticación e identidad del monolito.

### Dependencias entre módulos

`settings.py` declara `AUTH_USER_MODEL = 'users.User'`. Ningún módulo debe importar `User` directamente, sino usar `get_user_model()` o `settings.AUTH_USER_MODEL` en FKs.

### Antes de programar

1. ¿Por qué cambiar `AUTH_USER_MODEL` después de aplicar la primera migración en Django es tan peligroso?
2. ¿Por qué es una mejor práctica usar `settings.AUTH_USER_MODEL` en relaciones foráneas en lugar de importar la clase `User` directamente?

### Pruebas mínimas

1. Crear un usuario estándar mediante `User.objects.create_user(email='test@example.com', password='pass')` y verificar que el password esté hasheado (comience con `pbkdf2_sha256$` o `argon2`).
2. Crear un superusuario mediante `create_superuser` y verificar que `is_staff` y `is_superuser` sean `True`.

### Pruebas negativas

1. Intentar crear un usuario con email vacío y verificar que lance `ValueError('El email es obligatorio')`.
2. Intentar registrar un email duplicado y verificar `IntegrityError` en PostgreSQL.

### Documentación

Documentar la configuración de `AUTH_USER_MODEL` y los comandos de creación de usuarios iniciales en la guía del repositorio.

### Explicación posterior

Explica cómo funciona `normalize_email` al procesar la parte del dominio del correo y por qué las contraseñas nunca deben guardarse antes de pasar por `make_password` / `set_password`.

### Aplicación profesional

Arquitectura base de cualquier aplicación web moderna basada en correo electrónico.

### Reto adicional

Configurar el algoritmo de hashing de contraseñas para usar `Argon2` o `BCrypt` en lugar de `PBKDF2` si la biblioteca está disponible.
