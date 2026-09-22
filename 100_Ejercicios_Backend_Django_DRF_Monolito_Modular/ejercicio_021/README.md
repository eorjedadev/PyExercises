# Ejercicio 021 — Módulo de Clientes (apps/customers) y Perfil Desacoplado 1 a 1

[← Ejercicio 020](../ejercicio_020/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 022 →](../ejercicio_022/README.md)

---

### Contexto de negocio

El modelo `User` en `apps/users` solo debe encargarse de credenciales e identidad (email, password, flags de acceso). La información comercial del cliente (dirección de facturación, teléfono, tipo de documento fiscal, fecha de nacimiento, preferencias de compra) pertenece a una capacidad de negocio diferente: la gestión de clientes.

### Estado actual del sistema

Módulo de usuarios y autenticación operativos.

### Nueva necesidad

Crear el módulo `apps/customers`, modelar la entidad `CustomerProfile` relacionada 1 a 1 con `User`, y exponer endpoints para consultar y actualizar el perfil del cliente.

### Objetivo

Diseñar límites limpios entre módulos: separar la identidad técnica (`User` en `apps/users`) del perfil comercial (`CustomerProfile` en `apps/customers`) sin acoplarlos en un único modelo gigantesco.

### Actor

Cliente Autenticado autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/customers` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`CustomerProfile` (`id` UUID, `user` OneToOne, `phone_number`, `tax_id`, `tax_id_type`, `birth_date`, `address_line1`, `city`, `postal_code`, `country`), `User`.

### Reglas de negocio

1. Cada usuario tiene exactamente un `CustomerProfile`.
2. El perfil puede crearse perezosamente en el primer acceso o mediante un servicio de registro comercial.
3. El número de teléfono debe validarse en formato internacional E.164 (`+1234567890`).
4. `apps/users` no debe contener referencias directas a campos de facturación o direcciones.

### Contrato esperado

Consultar Mi Perfil:
- `GET /api/v1/customers/me/`
  Header: `Authorization: Bearer <token>`
  Response: `200 OK`
  ```json
  {
    "id": "uuid-perfil",
    "email": "dev.junior@empresa.com",
    "first_name": "Carlos",
    "last_name": "Mendoza",
    "phone_number": "+51987654321",
    "tax_id": "10456789012",
    "city": "Lima",
    "country": "PE"
  }
  ```

### Persistencia

Tabla `customers_customerprofile` en PostgreSQL con clave foránea única `user_id`.

### Relaciones

`models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_profile')`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Solo el usuario propietario puede ver y editar su propio perfil.

### Validaciones

Validación de formato E.164 de teléfono y código de país ISO 3166-1 alpha-2.

### Transacciones

No requerida para consulta/actualización simple.

### Casos límite

Usuario recién registrado que consulta `/customers/me/` antes de haber guardado datos de perfil (debe retornar el perfil inicial o crearlo al vuelo de forma transparente).

### Casos de error

`401 Unauthorized` si no hay token; `400 Bad Request` si el formato de teléfono es inválido.

### Consideraciones de seguridad

No permitir que un usuario modifique el `user_id` de su perfil para usurpar el perfil de otro usuario.

### Consideraciones de rendimiento

Usar `select_related('user')` en el selector para traer datos de usuario y perfil en una sola consulta SQL.

### Fundamentos de Python relacionados

Expresiones regulares para validación de teléfonos, manipulación de fechas.

### Conceptos Django relacionados

`models.OneToOneField`, `settings.AUTH_USER_MODEL`, propiedades calculadas.

### Conceptos DRF relacionados

Serializadores con campos combinados de dos modelos relacionados, vistas basadas en `request.user`.

### PostgreSQL

`CREATE TABLE customers_customerprofile (id UUID PRIMARY KEY, user_id UUID UNIQUE NOT NULL REFERENCES users_user(id) ON DELETE CASCADE, ...)`.

### Arquitectura

Monolito Modular: `apps/users` maneja credenciales; `apps/customers` maneja datos del cliente. Bajo acoplamiento.

### Dependencias entre módulos

`apps/customers` depende de `apps/users` (a través de `settings.AUTH_USER_MODEL`). `apps/users` NO debe importar nada de `apps/customers`.

### Antes de programar

1. ¿Por qué agregar 30 campos de perfil, direcciones y facturación directamente al modelo `User` es un error de arquitectura?
2. ¿Qué ventaja tiene que `apps/users` no conozca la existencia de `apps/customers`?

### Pruebas mínimas

1. Crear un usuario, autenticarse, llamar a `GET /api/v1/customers/me/` y verificar que devuelva los datos del perfil y del usuario.
2. Enviar `PATCH /api/v1/customers/me/` con un número de teléfono válido y verificar persistencia en PostgreSQL.

### Pruebas negativas

1. Enviar un teléfono con formato inválido ('123-abc') y verificar error `400`.

### Documentación

Documentar el modelo de perfil de cliente y sus endpoints en el README de `apps/customers`.

### Explicación posterior

Explica cómo la relación OneToOne garantiza integridad 1 a 1 en PostgreSQL mediante una restricción `UNIQUE` en la columna foránea `user_id`.

### Aplicación profesional

Separación de dominios de IAM (Identity and Access Management) y CRM/Customer Domain en plataformas empresariales.

### Reto adicional

Implementar un servicio `get_or_create_customer_profile(user: User) -> CustomerProfile` en `apps/customers/services.py` que garantice la existencia del perfil.
