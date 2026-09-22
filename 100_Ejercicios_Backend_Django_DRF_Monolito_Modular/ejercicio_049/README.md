# Ejercicio 049 — Módulo de Notificaciones (apps/notifications) y Desacoplamiento de Eventos

[← Ejercicio 048](../ejercicio_048/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 050 →](../ejercicio_050/README.md)

---

### Contexto de negocio

Cuando ocurren eventos importantes en el negocio (ej. 'Cuenta registrada', 'Pedido confirmado', 'Pago recibido', 'Stock bajo'), el sistema debe emitir notificaciones a los usuarios (notificaciones internas in-app, emails, SMS). El módulo de pedidos o pagos no debe encargarse de formatear plantillas de correo ni conectarse a servidores SMTP; esa responsabilidad pertenece al módulo `apps/notifications`.

### Estado actual del sistema

Módulos de usuarios, órdenes y pagos operativos.

### Nueva necesidad

Crear el módulo `apps/notifications`, modelar la entidad `Notification` (notificaciones in-app para usuarios) y exponer el servicio `notifications.services.send_notification(...)`.

### Objetivo

Diseñar un sistema de notificaciones desacoplado en el monolito modular, modelando notificaciones in-app leídas/no leídas y endpoints para que los clientes consulten su bandeja de entrada.

### Actor

Cliente Autenticado / Sistema de Notificaciones

### Módulo responsable

`apps/notifications` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Notification` (`id` UUID, `user` FK, `title`, `message`, `notification_type`, `link_url`, `is_read`, `created_at`), servicio `send_notification`.

### Reglas de negocio

1. Una notificación pertenece a un único usuario (`User`).
2. Los tipos de notificación son: `ORDER_STATUS_CHANGED`, `PAYMENT_CONFIRMED`, `PROMOTION_ALERT`, `SECURITY_ALERT`.
3. El cliente puede consultar sus notificaciones ordenadas de más reciente a más antigua y marcar una notificación como leída (`PATCH /api/v1/notifications/{id}/read/`).
4. Debe existir un endpoint para obtener el conteo de notificaciones no leídas (`GET /api/v1/notifications/unread-count/`).

### Contrato esperado

1. Listar Mis Notificaciones:
- `GET /api/v1/notifications/`
  Response: `200 OK`
  ```json
  [
    {
      "id": "uuid-notif-1",
      "title": "Pago Aprobado",
      "message": "Tu pago para la orden ORD-2026-00001 fue procesado con éxito.",
      "notification_type": "PAYMENT_CONFIRMED",
      "is_read": false,
      "created_at": "2026-09-22T16:00:00Z"
    }
  ]
  ```

2. Marcar como Leída:
- `POST /api/v1/notifications/{id}/read/` -> `200 OK` `{ "is_read": true }`

### Persistencia

Tabla `notifications_notification` en PostgreSQL con índices sobre `(user_id, is_read)`.

### Relaciones

`Notification.user` -> `ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Un usuario solo puede ver y modificar sus propias notificaciones.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

No requerida para lectura/actualización simple.

### Casos límite

Marcar como leída una notificación que ya estaba leída (idempotente, responder 200 sin cambios).

### Casos de error

`404 Not Found` al intentar acceder a una notificación ajena o inexistente.

### Consideraciones de seguridad

Protección estricta de ownership en todas las vistas de notificaciones.

### Consideraciones de rendimiento

Índice compuesto en PostgreSQL sobre `(user_id, is_read, -created_at)` para que la consulta del badge de no leídas sea casi instantánea.

### Fundamentos de Python relacionados

Manipulación de listas, booleanos y tipos enumerados.

### Conceptos Django relacionados

`select_related('user')`, métodos de queryset personalizados (`.unread()`, `.mark_all_as_read()`).

### Conceptos DRF relacionados

Endpoints de acción para marcar como leída, serializadores de notificaciones.

### PostgreSQL

`SELECT COUNT(*) FROM notifications_notification WHERE user_id = ... AND is_read = false;`.

### Arquitectura

`apps/notifications` actúa como sumidero de eventos de comunicación, permitiendo que otros módulos envíen avisos sin acoplarse.

### Dependencias entre módulos

Otros módulos (`apps/orders`, `apps/payments`) llaman a `apps.notifications.services.send_notification`.

### Antes de programar

1. ¿Por qué centralizar las notificaciones en un módulo dedicado evita tener plantillas de texto y lógica de mensajes dispersas por todo el backend?
2. ¿Cómo optimizar en PostgreSQL una consulta que se ejecuta en cada carga de página: contar notificaciones no leídas?

### Pruebas mínimas

1. Enviar una notificación a un usuario mediante `send_notification(...)` y verificar que aparezca en `GET /api/v1/notifications/` con `is_read = False`.
2. Invocar el endpoint de marcar como leída y comprobar que `unread-count` disminuya en 1.

### Pruebas negativas

1. Usuario A intentando marcar como leída una notificación del Usuario B -> Verificar `404 Not Found`.

### Documentación

Documentar la interfaz pública de envío de notificaciones en el README de `apps/notifications`.

### Explicación posterior

Explica el patrón Publisher-Subscriber conceptual dentro de un monolito y cómo un módulo de notificaciones desacopla la causa (orden pagada) del efecto (aviso al cliente).

### Aplicación profesional

Centros de notificaciones in-app (campanita), sistemas de alertas, notificaciones push móviles y avisos transaccionales.

### Reto adicional

Implementar un endpoint `POST /api/v1/notifications/mark-all-read/` que actualice en lote todas las notificaciones pendientes del usuario en una sola consulta SQL (`update(is_read=True)`).
