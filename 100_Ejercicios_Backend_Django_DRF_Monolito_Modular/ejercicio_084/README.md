# Ejercicio 084 — Permisos Granulares de Soporte, Asignación de Agentes y Escalado

[← Ejercicio 083](../ejercicio_083/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 085 →](../ejercicio_085/README.md)

---

### Contexto de negocio

En el equipo de atención al cliente existen diferentes niveles: `SUPPORT_AGENT_L1` (atención básica), `SUPPORT_AGENT_L2` (casos técnicos avanzados) y `SUPPORT_SUPERVISOR`. Se requiere un sistema de asignación de tickets, reasignación inteligente y escalado automático con registro de auditoría cuando un ticket de alta prioridad no ha sido atendido en menos de 2 horas (violación de SLA - Service Level Agreement).

### Estado actual del sistema

Módulo de soporte básico operativo. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Implementar endpoints de gestión de soporte: `POST /api/v1/support/tickets/{id}/assign/`, `POST /api/v1/support/tickets/{id}/escalate/`, e implementar un comando de verificación de SLAs `check_support_slas`.

### Objetivo

Dominar el control de acceso basado en roles jerárquicos (Hierarchical RBAC), flujos de asignación de trabajo y cumplimiento de acuerdos de nivel de servicio (SLAs) en backend.

### Actor

Agente de Soporte L1/L2 / Supervisor de Soporte

### Módulo responsable

`apps/support` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`SupportTicket`, `TicketAssignmentHistory`, servicio `assign_ticket`, servicio `escalate_ticket`, comando `check_support_slas`.

### Reglas de negocio

1. Un agente L1 puede autoasignarse tickets o asignarlos a otros agentes L1.
2. Solo un agente L1, L2 o Supervisor puede escalar un ticket de nivel 1 a nivel 2 (`escalate`), justificando el motivo técnico.
3. Cada asignación y escalado debe registrar una fila inmutable en `TicketAssignmentHistory` con fecha, actor y motivo.
4. Si un ticket `URGENT` permanece sin respuesta por más de 2 horas, el comando de SLA debe marcarlo como `SLA_BREACHED` y alertar al Supervisor.

### Contrato esperado

Escalar Ticket a Nivel 2:
- `POST /api/v1/support/tickets/{id}/escalate/`
  Header: `Authorization: Bearer <token_agente_l1>`
  Body: `{"target_level": "L2", "reason": "Requiere investigación en pasarela de pagos."}`
  Response: `200 OK` `{ "status": "OPEN", "support_level": "L2", ... }`

### Persistencia

Tablas `support_supportticket` y `support_ticketassignmenthistory` en PostgreSQL.

### Relaciones

`TicketAssignmentHistory.ticket` -> `ForeignKey(SupportTicket)`; `assigned_to` -> `ForeignKey(User)`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Roles `SUPPORT_AGENT_L1`, `SUPPORT_AGENT_L2`, `SUPPORT_SUPERVISOR`.

### Validaciones

Validar que el agente asignado esté activo y pertenezca al nivel de soporte adecuado.

### Transacciones

Transacción atómica al actualizar ticket y registrar historial.

### Casos límite

Un cliente intentando llamar al endpoint de asignación o escalado (debe ser bloqueado con `403 Forbidden`).

### Casos de error

`403 Forbidden` a usuarios sin privilegios de soporte.

### Consideraciones de seguridad

Control estricto de privilegios para evitar que agentes no autorizados cierren incidencias sin resolver.

### Consideraciones de rendimiento

Índices en PostgreSQL sobre `(status, priority, created_at)` para el comando de auditoría de SLAs.

### Fundamentos de Python relacionados

Manipulación de tiempos y deltas con `timezone.now()`.

### Conceptos Django relacionados

Comandos de gestión para verificación periódica de SLAs.

### Conceptos DRF relacionados

Clases de permisos especializadas `IsSupportStaff`, `IsSupportSupervisor`.

### PostgreSQL

`CREATE TABLE support_ticketassignmenthistory (id UUID PRIMARY KEY, ticket_id UUID NOT NULL, assigned_by_id UUID, assigned_to_id UUID, ...)`.

### Arquitectura

Gestión de roles y flujos de trabajo internos dentro de `apps/support`.

### Dependencias entre módulos

`apps.support` utiliza la autenticación de `apps.users`.

### Antes de programar

1. ¿Qué es un Service Level Agreement (SLA) en soporte técnico y cómo se monitorea en el backend mediante marcas de tiempo?
2. ¿Por qué todo cambio de agente o escalado debe quedar registrado en una tabla histórica de auditoría?

### Pruebas mínimas

1. Un agente L1 escala un ticket a L2 -> Verificar que el ticket pase a nivel L2 y se inserte el registro en `TicketAssignmentHistory`.
2. Ejecutar `call_command('check_support_slas')` sobre un ticket urgente creado hace 3 horas sin respuesta -> Verificar que se marque como `is_sla_breached = True`.

### Pruebas negativas

1. Cliente estándar intentando invocar el endpoint de escalado -> Verificar `403 Forbidden`.

### Documentación

Documentar la matriz de escalado y los tiempos de SLA en la guía de operaciones de soporte.

### Explicación posterior

Explica cómo se estructuran los sistemas de enrutamiento y asignación de carga de trabajo (Workload Routing) en centros de soporte de gran escala.

### Aplicación profesional

Sistemas de Helpdesk empresarial, gestión de incidentes críticos (ITIL / SRE) y centros de atención telefónica/digital.

### Reto adicional

Implementar un algoritmo de asignación automática de tipo Round-Robin entre los agentes L1 activos disponibles.
