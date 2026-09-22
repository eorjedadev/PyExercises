# Ejercicio 028 — Módulo de Auditoría y Trazabilidad de Eventos de Negocio

[← Ejercicio 027](../ejercicio_027/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 029 →](../ejercicio_029/README.md)

---

### Contexto de negocio

Para cumplimiento normativo y seguridad, el sistema debe registrar una bitácora inmutable de eventos críticos del negocio (ej. 'Usuario inició sesión', 'Cambio de contraseña', 'Producto creado', 'Modificación de precios'). Este registro de auditoría de negocio no debe confundirse con los logs técnicos de depuración.

### Estado actual del sistema

Módulos `apps/users`, `apps/catalog`, `apps/customers` operativos.

### Nueva necesidad

Crear el módulo `apps/audit`, modelar la entidad `AuditEvent` y crear una función de servicio pública `record_audit_event(...)` que otros módulos puedan invocar para registrar acciones con actor, IP, recurso y cambios.

### Objetivo

Diseñar un subsistema de auditoría inmutable en el monolito modular, comprendiendo la diferencia entre logging técnico y auditoría de negocio.

### Actor

Sistema interno (invocado por servicios de otros módulos)

### Módulo responsable

`apps/audit` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`AuditEvent` (`id` UUID, `actor` FK User nullable, `event_type`, `resource_type`, `resource_id`, `ip_address`, `user_agent`, `payload` JSONField, `created_at`), servicio `record_audit_event`.

### Reglas de negocio

1. Los registros de auditoría son de solo inserción (Append-Only); no se permite actualizar (`UPDATE`) ni eliminar (`DELETE`) filas de auditoría.
2. Cada evento debe registrar el tipo de evento (ej. `USER_LOGIN_SUCCESS`, `PRODUCT_PRICE_CHANGED`), el actor responsable y la fecha exacta en UTC.
3. La información sensible (contraseñas, tokens completos) debe ser sanitizada antes de guardarse en el `payload` JSON.
4. Solo usuarios con rol `ADMIN` pueden consultar el endpoint de auditoría `GET /api/v1/audit/events/`.

### Contrato esperado

Consultar Auditoría (Solo Admin):
- `GET /api/v1/audit/events/?event_type=PRODUCT_PRICE_CHANGED`
  Header: `Authorization: Bearer <token_admin>`
  Response: `200 OK`
  ```json
  {
    "count": 1,
    "results": [
      {
        "id": "uuid-evento",
        "actor_email": "admin@empresa.com",
        "event_type": "PRODUCT_PRICE_CHANGED",
        "resource_type": "Product",
        "resource_id": "uuid-producto",
        "ip_address": "192.168.1.1",
        "payload": { "old_price": "50.00", "new_price": "65.00" },
        "created_at": "2026-09-22T11:30:00Z"
      }
    ]
  }
  ```

### Persistencia

Tabla `audit_auditevent` en PostgreSQL con particionamiento opcional o índices sobre `event_type` y `created_at`.

### Relaciones

`AuditEvent.actor` -> `ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar no presencia de claves prohibidas en el payload (`password`, `token`, `secret`).

### Transacciones

No debe abortar la operación principal si la auditoría falla (manejo resiliente).

### Casos límite

Acción realizada por un usuario anónimo o proceso del sistema (actor `None`).

### Casos de error

`403 Forbidden` si un usuario no administrador intenta acceder al endpoint de auditoría.

### Consideraciones de seguridad

Sanitización estricta de payloads para cumplir con normativas de privacidad (GDPR, PCI-DSS).

### Consideraciones de rendimiento

Inserciones rápidas; índice compuesto sobre `(resource_type, resource_id)` para consultas de historial de un objeto específico.

### Fundamentos de Python relacionados

Serialización JSON segura de objetos Python, sanitización de diccionarios con claves prohibidas.

### Conceptos Django relacionados

`models.JSONField` de PostgreSQL, modelos inmutables (bloquear `save()` si no es creación o usar permisos de DB).

### Conceptos DRF relacionados

Vistas de solo lectura (`generics.ListAPIView`, `ReadOnlyModelViewSet`).

### PostgreSQL

`CREATE TABLE audit_auditevent (id UUID PRIMARY KEY, event_type VARCHAR(100) NOT NULL, payload JSONB, created_at TIMESTAMPTZ NOT NULL, ...)`.

### Arquitectura

`apps/audit` expone una interfaz de servicio pública `apps.audit.services.record_audit_event(...)` que es consumida por otros módulos.

### Dependencias entre módulos

Otros módulos (`apps/users`, `apps/catalog`) llaman a `apps.audit.services.record_audit_event`. `apps/audit` solo conoce `settings.AUTH_USER_MODEL`.

### Antes de programar

1. ¿Por qué la auditoría de negocio no debe implementarse mediante simples `logger.info()` en archivos de texto planos de logs?
2. ¿Por qué la clave foránea a `User` debe tener `on_delete=models.SET_NULL` en lugar de `CASCADE`?

### Pruebas mínimas

1. Ejecutar una acción auditada (ej. login o cambio de precio) y verificar que se cree una fila en `audit_auditevent` con el actor y payload correctos.
2. Autenticarse como Administrador y listar eventos de auditoría -> `200 OK`.

### Pruebas negativas

1. Autenticarse como cliente estándar e intentar consultar `GET /api/v1/audit/events/` -> Verificar `403 Forbidden`.

### Documentación

Documentar la lista estándar de `event_type`s y la firma de `record_audit_event` en el README de `apps/audit`.

### Explicación posterior

Explica el principio de inmutabilidad en pistas de auditoría (Audit Trail) y cómo proteger la tabla contra modificaciones directas mediante permisos de PostgreSQL (`REVOKE UPDATE, DELETE ON audit_auditevent FROM app_user`).

### Aplicación profesional

Requisito mandatorio en aplicaciones financieras, de salud, comercio electrónico y certificaciones SOC2 / ISO 27001.

### Reto adicional

Implementar un extractor de IP y User-Agent que obtenga la información directamente del objeto `request` de Django.
