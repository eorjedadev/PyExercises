# Ejercicio 083 — Sistema de Soporte y Tickets de Atención al Cliente (apps/support)

[← Ejercicio 082](../ejercicio_082/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 084 →](../ejercicio_084/README.md)

---

### Contexto de negocio

Cuando un cliente experimenta un problema con un pedido o producto, debe poder abrir un Ticket de Soporte vinculado a su orden de compra. El módulo de atención al cliente (`apps/support`) debe permitir registrar tickets, mantener un hilo de mensajes bidireccional (conversación entre el cliente y los agentes de soporte) y gestionar prioridades (`LOW`, `MEDIUM`, `HIGH`, `URGENT`) y estados (`OPEN`, `WAITING_CUSTOMER`, `RESOLVED`, `CLOSED`).

### Estado actual del sistema

Módulos de usuarios, clientes, órdenes, catálogo y pagos operativos.

### Nueva necesidad

Crear el módulo `apps/support`, modelar `SupportTicket` y `TicketMessage`, y exponer endpoints para que clientes abran tickets y respondan mensajes, y para que agentes de soporte gestionen las incidencias.

### Objetivo

Diseñar el dominio de Helpdesk y atención al cliente en el monolito modular, modelando conversaciones anidadas en hilos y vinculando tickets a entidades de otros módulos (`Order`).

### Actor

Cliente Autenticado / Agente de Soporte autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/support` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`SupportTicket` (`id` UUID, `ticket_number`, `customer_id` UUID, `order_id` UUID nullable, `subject`, `priority`, `status`, `assigned_agent_id` UUID nullable, `created_at`, `updated_at`), `TicketMessage` (`id` UUID, `ticket` FK, `sender` FK User, `message_body`, `is_internal_note`, `created_at`).

### Reglas de negocio

1. El `ticket_number` debe ser correlativo (ej. `TCK-2026-00001`).
2. Un cliente puede vincular opcionalmente el ticket a una orden suya existente.
3. Los clientes solo pueden ver mensajes donde `is_internal_note = False`. Las notas internas solo son visibles para agentes de soporte y administradores.
4. Cuando un agente responde un mensaje, el ticket pasa a `WAITING_CUSTOMER`; cuando el cliente responde, pasa a `OPEN`.

### Contrato esperado

1. Abrir Ticket (Cliente):
- `POST /api/v1/support/tickets/`
  Body: `{"subject": "Demora en entrega", "priority": "HIGH", "order_id": "uuid-orden", "message": "El paquete no ha llegado..."}`
  Response: `201 Created` `{ "ticket_number": "TCK-2026-00001", ... }`

2. Agregar Mensaje al Hilo:
- `POST /api/v1/support/tickets/{id}/messages/`
  Body: `{"message_body": "Aquí adjunto más detalles..."}`
  Response: `201 Created`

### Persistencia

Tablas `support_supportticket` y `support_ticketmessage` en PostgreSQL.

### Relaciones

`TicketMessage.ticket` -> `ForeignKey(SupportTicket, on_delete=models.CASCADE, related_name='messages')`; `TicketMessage.sender` -> `ForeignKey(settings.AUTH_USER_MODEL)`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Clientes solo ven sus propios tickets; agentes de soporte ven todos los tickets asignados o generales.

### Validaciones

Validar que el `order_id` pertenezca al cliente si se envía.

### Transacciones

Transacción atómica: crear ticket + crear primer mensaje inicial.

### Casos límite

El cliente intenta responder a un ticket que ya está en estado `CLOSED` (debe ser rechazado o reabrir el ticket según la política de negocio configurada).

### Casos de error

`403 Forbidden` si un cliente intenta leer notas internas (`is_internal_note=True`) o acceder a un ticket ajeno.

### Consideraciones de seguridad

Protección de visibilidad de notas internas entre agentes.

### Consideraciones de rendimiento

Uso de `prefetch_related(Prefetch('messages', queryset=...))` para serializar el hilo de mensajes en una sola consulta.

### Fundamentos de Python relacionados

Modelado de hilos conversacionales y filtrado condicional de colecciones.

### Conceptos Django relacionados

`related_name='messages'`, métodos de queryset para excluir notas internas para clientes.

### Conceptos DRF relacionados

Serializadores con visibilidad dinámica de campos según el rol del usuario autenticado.

### PostgreSQL

`CREATE TABLE support_supportticket (id UUID PRIMARY KEY, ticket_number VARCHAR(30) UNIQUE NOT NULL, ...)`.

### Arquitectura

`apps/support` encapsula todo el sistema de Helpdesk sin invadir `apps/orders`.

### Dependencias entre módulos

`apps.support` consulta `apps.orders` para validar el pedido asociado.

### Antes de programar

1. ¿Por qué las 'notas internas' de agentes de soporte deben filtrarse a nivel de QuerySet en el backend en lugar de solo ocultarlas con CSS en el frontend?
2. ¿Cómo se diseña la relación entre un ticket y una orden para que sea opcional (permitiendo consultas generales sin orden)?

### Pruebas mínimas

1. Crear un ticket con mensaje inicial como cliente -> Verificar creación exitosa con status `OPEN` y 1 mensaje asociado.
2. Un agente agrega una nota interna (`is_internal_note=True`). El cliente consulta el ticket -> Verificar que el cliente NO vea la nota interna en el JSON.

### Pruebas negativas

1. Cliente A intentando ver el ticket del Cliente B -> Verificar `404 Not Found`.

### Documentación

Documentar el modelo de tickets y los permisos de notas internas en el README de `apps/support`.

### Explicación posterior

Explica el patrón Helpdesk / Ticketing y cómo gestionar la privacidad de datos en conversaciones compartidas entre clientes y personal interno.

### Aplicación profesional

Sistemas de atención al cliente (Zendesk, Freshdesk, Jira Service Management) integrados nativamente en plataformas empresariales.

### Reto adicional

Notificar automáticamente al cliente por email en segundo plano cada vez que un agente responda su ticket.
