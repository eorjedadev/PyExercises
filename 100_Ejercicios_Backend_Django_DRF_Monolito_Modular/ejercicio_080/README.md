# Ejercicio 080 — Facturación Recurrente Automática y Gestión de Períodos de Gracia

[← Ejercicio 079](../ejercicio_079/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 081 →](../ejercicio_081/README.md)

---

### Contexto de negocio

Para que las suscripciones se renueven automáticamente, el backend debe contar con un proceso de facturación recurrente programado (Scheduled Billing Engine). Diariamente, el sistema debe buscar suscripciones que vencen hoy, intentar el cobro automático mediante la pasarela de pagos, extender el periodo si el cobro es exitoso, o gestionar reintentos y periodos de gracia (Dunning Management) si la tarjeta falla.

### Estado actual del sistema

Módulo de suscripciones y pasarela de pagos operativos.

### Nueva necesidad

Crear el comando de gestión `python manage.py process_recurring_billing` en `apps/subscriptions/management/commands/process_recurring_billing.py` y el servicio de renovación automática.

### Objetivo

Dominar la automatización de cobros recurrentes y la gestión de morosidad (Dunning / Grace Period) en Django, procesando renovaciones en lotes y manejando reintentos sin interrumpir el servicio inmediatamente ante el primer fallo.

### Actor

Motor de Facturación Automática (Cron / Worker)

### Módulo responsable

`apps/subscriptions` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`process_recurring_billing` (Command), servicio `renew_subscription`, `SubscriptionBillingAttempt`.

### Reglas de negocio

1. El comando busca suscripciones en estado `ACTIVE` cuya fecha `current_period_end <= now()`.
2. Si la suscripción tiene `cancel_at_period_end = True`, pasa automáticamente a estado `CANCELED` y no se cobra.
3. Si debe renovarse, se intenta el cobro mediante `payments.services.charge_saved_payment_method`.
4. Si el cobro es exitoso, `current_period_start` y `current_period_end` se extienden al siguiente ciclo y se genera la factura.
5. Si el cobro falla, la suscripción pasa a `PAST_DUE` (período de gracia de 3 días) y se encola un correo de aviso de pago fallido al cliente.

### Contrato esperado

Ejecución del Motor de Renovaciones:
```powershell
python manage.py process_recurring_billing
[BILLING] Procesando 5 suscripciones que vencen hoy...
- Sub 001: Cobro exitoso $29.00 USD. Renovada hasta 2026-11-22.
- Sub 002: Cancelada al final del periodo segun solicitud del cliente.
- Sub 003: Fallo de tarjeta (Fondos insuficientes). Estado: PAST_DUE (Dia 1 de 3).
[OK] Proceso finalizado: 3 renovadas, 1 cancelada, 1 en periodo de gracia.
```

### Persistencia

Actualización de fechas y estados en `subscriptions_subscription` e inserción de cobro en `payments`.

### Relaciones

`Subscription, SubscriptionPlan, PaymentTransaction`.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Cada renovación individual se ejecuta en su propia transacción atómica aislada.

### Casos límite

El cliente actualiza su tarjeta durante el periodo de gracia de 3 días (el sistema debe reintentar el cobro y devolver la suscripción a `ACTIVE`).

### Casos de error

Manejo de excepciones por suscripción para que el fallo en un cliente no impida cobrar a los demás.

### Consideraciones de seguridad

Los cobros desatendidos utilizan tokens guardados de pasarelas de pago certificadas (Customer IDs / Payment Method Tokens).

### Consideraciones de rendimiento

Procesamiento en lotes con `.iterator(chunk_size=100)` para escalar a decenas de miles de suscriptores.

### Fundamentos de Python relacionados

Manejo de fechas relativas, bucles resilientes ante excepciones.

### Conceptos Django relacionados

`BaseCommand`, consultas filtradas por rango temporal (`current_period_end__lte=now()`).

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`SELECT * FROM subscriptions_subscription WHERE status = 'ACTIVE' AND current_period_end <= NOW();`.

### Arquitectura

El motor de facturación orquesta el cobro automático consumiendo los servicios de `apps/payments` y `apps/notifications`.

### Dependencias entre módulos

`apps.subscriptions` interactúa con `apps.payments` y `apps.notifications`.

### Antes de programar

1. ¿Qué es el Dunning Management (gestión de cobros fallidos) y por qué suspender la cuenta inmediatamente al primer milisegundo de fallo destruye la retención de clientes SaaS?
2. ¿Por qué cada intento de renovación en un comando masivo debe estar dentro de un bloque `try/except` individual?

### Pruebas mínimas

1. Crear una suscripción vencida, ejecutar el comando con cobro simulado exitoso -> Verificar que la suscripción extienda su fecha de fin en 1 mes y continúe en `ACTIVE`.
2. Probar con una suscripción marcada con `cancel_at_period_end=True` -> Verificar que pase a `CANCELED` sin cobrar.

### Pruebas negativas

1. Simular un fallo en la tarjeta y comprobar que la suscripción cambie a estado `PAST_DUE` y se registre la notificación.

### Documentación

Documentar la periodicidad de ejecución y los estados de Dunning en el manual de facturación recurrente.

### Explicación posterior

Explica cómo se estructuran los motores de facturación recurrente en empresas SaaS (ej. Stripe Billing, Chargebee) y cómo se implementan los reintentos exponenciales de cobro.

### Aplicación profesional

Arquitectura de monetización SaaS, plataformas de suscripción y servicios de membresía corporativa.

### Reto adicional

Implementar la cancelación automática definitiva si una suscripción permanece en `PAST_DUE` por más de 7 días consecutivos sin pago exitoso.
