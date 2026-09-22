# Ejercicio 079 — Sistema de Suscripciones Periódicas (apps/subscriptions) y Ciclos de Facturación

[← Ejercicio 078](../ejercicio_078/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 080 →](../ejercicio_080/README.md)

---

### Contexto de negocio

El negocio amplía su modelo hacia productos digitales y servicios SaaS recurrentes (ej. membresía premium mensual o anual). Se requiere diseñar el módulo de suscripciones (`apps/subscriptions`), modelar planes (`SubscriptionPlan`), suscripciones activas (`Subscription`), periodos de facturación (Billing Cycles) y ciclo de vida (`TRIAL`, `ACTIVE`, `PAST_DUE`, `CANCELED`).

### Estado actual del sistema

Módulos de catálogo, clientes, órdenes, pagos y facturación operativos.

### Nueva necesidad

Crear el módulo `apps/subscriptions`, modelar `SubscriptionPlan` y `Subscription`, y exponer endpoints para que los clientes elijan un plan y se suscriban mediante cobro recurrente.

### Objetivo

Diseñar el dominio de suscripciones recurrentes en Django/DRF, modelando ciclos de renovación automática, periodos de gracia y control de estados de membresía.

### Actor

Cliente Autenticado (Suscriptor) autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/subscriptions` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`SubscriptionPlan` (`id` UUID, `name`, `code`, `price_amount`, `billing_interval`, `interval_count`, `trial_days`, `is_active`), `Subscription` (`id` UUID, `customer_id` UUID, `plan` FK, `status`, `current_period_start`, `current_period_end`, `cancel_at_period_end`, `created_at`).

### Reglas de negocio

1. Un plan define su intervalo: `MONTHLY` (mensual) o `YEARLY` (anual).
2. Si el plan incluye días de prueba (`trial_days > 0`), la suscripción inicia en estado `TRIAL` y no cobra hasta que finalice el periodo de prueba.
3. Al suscribirse, se fija la fecha de inicio (`current_period_start`) y fecha de fin (`current_period_end`).
4. El cliente puede cancelar la suscripción con la opción de mantener el acceso hasta el final del periodo pagado (`cancel_at_period_end = True`).

### Contrato esperado

Suscribirse a un Plan:
- `POST /api/v1/subscriptions/`
  Header: `Authorization: Bearer <token>`
  Body: `{"plan_id": "uuid-plan-pro", "payment_method_token": "pm_sim_123"}`
  Response: `201 Created`
  ```json
  {
    "id": "uuid-suscripcion",
    "plan_name": "Plan Pro Mensual",
    "status": "ACTIVE",
    "current_period_start": "2026-09-22T00:00:00Z",
    "current_period_end": "2026-10-22T00:00:00Z",
    "cancel_at_period_end": false
  }
  ```

### Persistencia

Tablas `subscriptions_subscriptionplan` y `subscriptions_subscription` en PostgreSQL.

### Relaciones

`Subscription.plan` -> `ForeignKey(SubscriptionPlan)`; `customer_id` como UUID.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar que el plan esté activo y que el cliente no tenga ya una suscripción activa idéntica.

### Transacciones

Transacción atómica: crear suscripción + procesar primer cobro en `apps/payments`.

### Casos límite

El cliente cancela su suscripción el día 5 de un plan mensual pagado (debe seguir teniendo acceso hasta el día 30; `cancel_at_period_end = True`).

### Casos de error

`400 Bad Request` si la tarjeta es rechazada en el primer cobro de la suscripción.

### Consideraciones de seguridad

Protección de acceso a características premium validando el estado `ACTIVE` o `TRIAL` en tiempo real.

### Consideraciones de rendimiento

Índice en PostgreSQL sobre `(customer_id, status)` para consultar el estado de membresía en cada petición sin sobrecarga.

### Fundamentos de Python relacionados

Cálculo de fechas con `dateutil.relativedelta` o `datetime.timedelta`.

### Conceptos Django relacionados

`models.TextChoices` para estados e intervalos de facturación.

### Conceptos DRF relacionados

Serializadores de planes y suscripciones, endpoints de cancelación.

### PostgreSQL

`CREATE TABLE subscriptions_subscription (id UUID PRIMARY KEY, plan_id UUID NOT NULL, status VARCHAR(30) NOT NULL, current_period_end TIMESTAMPTZ NOT NULL, ...)`.

### Arquitectura

`apps/subscriptions` encapsula la lógica SaaS y membresías.

### Dependencias entre módulos

`apps.subscriptions` invoca `apps.payments` para los cobros y consulta `apps.customers`.

### Antes de programar

1. ¿Por qué una suscripción cancelada no debe pasar inmediatamente a inactiva si el cliente ya pagó el mes por adelantado?
2. ¿Cómo se calculan fechas mensuales exactas considerando meses de 28, 30 y 31 días?

### Pruebas mínimas

1. Crear un plan mensual de $29.00, crear una suscripción -> Verificar que el periodo finalice exactamente 1 mes después y el estado sea `ACTIVE`.
2. Invocar el endpoint de cancelación y comprobar que `cancel_at_period_end` cambie a `True` manteniendo el estado `ACTIVE`.

### Pruebas negativas

1. Intentar suscribirse a un plan inactivo (`is_active = False`) -> Verificar rechazo `400 Bad Request`.

### Documentación

Documentar el ciclo de vida de suscripciones en el README de `apps/subscriptions`.

### Explicación posterior

Explica los modelos de negocio recurrentes (SaaS, Membership) y por qué separar los Planes de las Instancias de Suscripción permite cambiar precios de planes futuros sin afectar los contratos de clientes existentes.

### Aplicación profesional

Plataformas de streaming, software SaaS B2B, clubes de suscripción de productos y membresías premium.

### Reto adicional

Crear una clase de permiso reutilizable `HasActiveSubscription` en `apps/subscriptions/permissions.py` para proteger endpoints exclusivos de usuarios premium.
