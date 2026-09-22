# Ejercicio 022 — Verificación de Ownership y Permiso Personalizado IsOwner

[← Ejercicio 021](../ejercicio_021/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 023 →](../ejercicio_023/README.md)

---

### Contexto de negocio

Los clientes pueden registrar múltiples direcciones de entrega (domicilio, oficina, casa de playa) en el módulo `apps/customers`. Una vulnerabilidad crítica común (IDOR / BOLA - Broken Object Level Authorization) ocurre cuando un usuario cambia el ID en la URL y accede o modifica la dirección de otro usuario. El backend debe garantizar la estricta verificación de propiedad (Ownership).

### Estado actual del sistema

Módulo `apps/customers` con perfil básico creado.

### Nueva necesidad

Crear el modelo `CustomerAddress`, exponer endpoints CRUD de direcciones (`/api/v1/customers/addresses/`) e implementar la clase de permiso `IsAddressOwner` que verifique que `address.customer.user == request.user`.

### Objetivo

Dominar la prevención de vulnerabilidades IDOR/BOLA en DRF mediante `has_object_permission`, filtrado automático de QuerySets por propietario en `get_queryset()` y permisos personalizados.

### Actor

Cliente Autenticado autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/customers` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`CustomerAddress` (`id` UUID, `customer` FK, `title`, `street`, `number`, `city`, `postal_code`, `is_default`), `IsAddressOwner`.

### Reglas de negocio

1. Un cliente puede tener múltiples direcciones.
2. Un usuario solo puede listar, ver, editar y eliminar sus propias direcciones.
3. Si un usuario intenta acceder a la dirección de otro usuario por ID, la API debe responder `404 Not Found` (o `403 Forbidden`, recomendando 404 para evitar enumeración de existencia).
4. Solo puede existir una dirección marcada como `is_default=True` por cliente.

### Contrato esperado

Listar Mis Direcciones:
- `GET /api/v1/customers/addresses/`
  Header: `Authorization: Bearer <token_usuario_A>`
  Response: `200 OK` (Solo retorna las direcciones del usuario A)

Intentar Ver Dirección de Otro Usuario:
- `GET /api/v1/customers/addresses/{id_direccion_usuario_B}/`
  Header: `Authorization: Bearer <token_usuario_A>`
  Response: `404 Not Found`

### Persistencia

Tabla `customers_customeraddress` con FK a `customers_customerprofile`.

### Relaciones

`CustomerAddress.customer` -> `ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='addresses')`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

`IsAddressOwner` y restricción de QuerySet en la vista.

### Validaciones

Garantizar que al crear una dirección, el `customer` se asigne automáticamente desde `request.user.customer_profile`.

### Transacciones

Transacción atómica si se actualiza `is_default=True` para desmarcar la anterior dirección por defecto.

### Casos límite

El usuario A intenta enviar un payload `POST` con `{"customer_id": "id_del_usuario_B"}` (el backend debe ignorarlo y forzar el usuario de la sesión).

### Casos de error

`404 Not Found` al intentar acceder a un objeto ajeno.

### Consideraciones de seguridad

Mitigación directa de OWASP API Security Top 10 #1: Broken Object Level Authorization (BOLA).

### Consideraciones de rendimiento

Filtrar siempre por `customer__user=request.user` en el nivel de base de datos (`WHERE customer_id = ...`).

### Fundamentos de Python relacionados

Comparación de objetos y verificación de identidad.

### Conceptos Django relacionados

Filtrado de QuerySets por relaciones cruzadas (`CustomerAddress.objects.filter(customer__user=request.user)`).

### Conceptos DRF relacionados

`permissions.BasePermission`, `has_object_permission(self, request, view, obj)`, sobreescritura de `perform_create(self, serializer)`.

### PostgreSQL

`SELECT ... FROM customers_customeraddress WHERE customer_id = ... AND id = ...`.

### Arquitectura

Seguridad por defecto en la capa de datos y vistas de `apps/customers`.

### Dependencias entre módulos

Interno a `apps/customers`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué filtrar el QuerySet en `get_queryset()` es la primera línea de defensa antes de evaluar `has_object_permission`?
2. ¿Por qué responder 404 en lugar de 403 al solicitar un recurso ajeno previene la enumeración de IDs en APIs públicas?

### Pruebas mínimas

1. Crear 2 usuarios (Usuario 1 y Usuario 2) con una dirección cada uno. Autenticarse como Usuario 1 y listar direcciones -> Comprobar que solo aparece la dirección 1.
2. Autenticarse como Usuario 1 y consultar el detalle de su propia dirección -> Status `200 OK`.

### Pruebas negativas

1. Autenticarse como Usuario 1 e intentar consultar `GET /api/v1/customers/addresses/{id_direccion_usuario_2}/` -> Verificar status `404 Not Found`.
2. Autenticarse como Usuario 1 e intentar enviar `DELETE` sobre la dirección del Usuario 2 -> Verificar status `404 Not Found`.

### Documentación

Documentar la política de autorización por propietario en el README del módulo.

### Explicación posterior

Explica por qué confiar en un `customer_id` enviado en el cuerpo de una petición JSON es una falla crítica de seguridad y cómo `perform_create` lo previene asignando `serializer.save(customer=request.user.customer_profile)`.

### Aplicación profesional

Regla dorada en sistemas multi-tenant, banca, perfiles de usuario y gestión de recursos privados.

### Reto adicional

Implementar una restricción única condicional en PostgreSQL (`UniqueConstraint` con `condition=Q(is_default=True)`) para garantizar a nivel de base de datos que solo haya una dirección por defecto por cliente.
