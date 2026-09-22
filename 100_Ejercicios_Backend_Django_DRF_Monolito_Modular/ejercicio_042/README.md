# Ejercicio 042 — Idempotencia en APIs y Prevención de Doble Cobro con Idempotency-Key

[← Ejercicio 041](../ejercicio_041/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 043 →](../ejercicio_043/README.md)

---

### Contexto de negocio

En redes móviles o conexiones inestables, un cliente puede enviar `POST /api/v1/orders/`, el servidor procesa la orden con éxito, pero la conexión se corta antes de que el cliente reciba el `201 Created`. El cliente reintenta la petición automáticamente. Si el backend no es idempotente, se crearán dos órdenes idénticas y se descontará el stock dos veces. Se requiere implementar soporte para cabecera `Idempotency-Key`.

### Estado actual del sistema

Creación de órdenes operativa. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Crear el módulo `apps/core/idempotency` con un modelo `IdempotencyRecord` y un middleware o decorador que capture la cabecera HTTP `Idempotency-Key`, almacenando el payload de respuesta para retornar el mismo resultado ante reintentos sin duplicar efectos secundarios.

### Objetivo

Dominar el concepto de Idempotencia en APIs REST para métodos no seguros (`POST`), almacenando huellas de peticiones y respuestas en base de datos para garantizar que peticiones duplicadas devuelvan el resultado original sin re-ejecutar la lógica de negocio.

### Actor

Cliente de API / App Móvil autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/core` aplicado en `apps/orders`

### Entidades involucradas

`IdempotencyRecord` (`id` UUID, `idempotency_key` VARCHAR unique, `user` FK, `request_path`, `request_hash`, `response_status_code`, `response_body` JSONField, `created_at`, `locked_at`), decorador/middleware `@idempotent_operation`.

### Reglas de negocio

1. El cliente envía una cabecera opcional u obligatoria `Idempotency-Key: <uuid-único>` en `POST /orders/`.
2. Si es la primera vez que se recibe la clave para ese usuario, se procesa la orden, se guarda la respuesta en `IdempotencyRecord` y se responde `201 Created`.
3. Si se recibe la misma `Idempotency-Key` por segunda vez con el mismo payload, el backend NO ejecuta el servicio de creación; recupera la respuesta guardada y devuelve el mismo JSON y status code original (`201 Created`).
4. Si se envía la misma `Idempotency-Key` pero con un payload diferente (tampering), debe responder `422 Unprocessable Entity` o `400 Bad Request` indicando conflicto de clave.
5. Si una petición con la misma clave está actualmente en proceso (concurrente), responder `409 Conflict` (operación en curso).

### Contrato esperado

1. Primera Petición:
- `POST /api/v1/orders/` (Header `Idempotency-Key: 123e4567-e89b-12d3-a456-426614174000`)
  Response: `201 Created` `{ "id": "orden-uuid-1", ... }`

2. Reintento con misma clave y body:
- `POST /api/v1/orders/` (Misma cabecera y mismo body)
  Response: `201 Created` `{ "id": "orden-uuid-1", ... }` (Retornado desde el registro, 0 órdenes nuevas creadas)

### Persistencia

Tabla `core_idempotencyrecord` en PostgreSQL con índice único sobre `(user_id, idempotency_key)`.

### Relaciones

`IdempotencyRecord.user` -> `ForeignKey(settings.AUTH_USER_MODEL)`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

La clave de idempotencia está asociada al usuario autenticado.

### Validaciones

Validación de formato UUID de la cabecera `Idempotency-Key` y hash SHA-256 del cuerpo de la petición.

### Transacciones

Bloqueo o inserción atómica del registro de idempotencia.

### Casos límite

Peticiones concurrentes idénticas que llegan en el mismo milisegundo (el primer hilo adquiere el lock en la tabla de idempotencia, el segundo espera o recibe 409).

### Casos de error

`400 Bad Request` si la clave de idempotencia no es válida o si el payload cambia con la misma clave.

### Consideraciones de seguridad

Aislar las claves de idempotencia por usuario: el Usuario B no puede espiar la respuesta del Usuario A usando su misma clave.

### Consideraciones de rendimiento

Purgar registros de idempotencia antiguos después de 24 o 48 horas mediante un comando de mantenimiento.

### Fundamentos de Python relacionados

Generación de hashes criptográficos con `hashlib.sha256(request.body).hexdigest()`.

### Conceptos Django relacionados

Middlewares de Django, decoradores de vista, almacenamiento de respuestas HTTP serializadas.

### Conceptos DRF relacionados

Interceptación de peticiones antes de `dispatch()` en vistas de DRF.

### PostgreSQL

`CREATE UNIQUE INDEX unique_user_idempotency ON core_idempotencyrecord (user_id, idempotency_key);`.

### Arquitectura

Mecanismo transversal reutilizable en `apps/core/idempotency.py` aplicable a cualquier endpoint sensible del monolito.

### Dependencias entre módulos

`apps/orders` aplica el decorador provisto por `apps/core`.

### Antes de programar

1. ¿Por qué los métodos `GET`, `PUT` y `DELETE` son naturalmente idempotentes según la especificación HTTP, mientras que `POST` no lo es?
2. ¿Por qué Stripe y las pasarelas de pago de clase mundial exigen `Idempotency-Key` para toda operación de cobro o creación de recursos?

### Pruebas mínimas

1. Enviar una petición `POST /orders/` con cabecera `Idempotency-Key: clave-1` -> Verificar `201 Created` y orden creada.
2. Enviar inmediatamente una segunda petición con la misma cabecera y mismo payload -> Verificar `201 Created` con el MISMO ID de orden y comprobar que en base de datos solo exista 1 sola orden.

### Pruebas negativas

1. Enviar la misma clave con un cuerpo diferente (cambiando los ítems) -> Verificar que responda `400 Bad Request` por discrepancia de payload.

### Documentación

Documentar el uso de la cabecera `Idempotency-Key` en la guía de integración de la API.

### Explicación posterior

Explica el estándar IETF Draft para cabeceras `Idempotency-Key` en HTTP y cómo protege a las aplicaciones contra la duplicación involuntaria de transacciones financieras.

### Aplicación profesional

Estándar fundamental en sistemas bancarios, pasarelas de pago (Stripe, Adyen), carritos de compra y microtransacciones.

### Reto adicional

Configurar un tiempo de expiración (TTL) de 24 horas para los registros de idempotencia.
