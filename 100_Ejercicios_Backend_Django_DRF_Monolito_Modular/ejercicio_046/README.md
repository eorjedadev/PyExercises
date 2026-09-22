# Ejercicio 046 — Módulo de Pagos (apps/payments) y Registro de Intentos de Cobro

[← Ejercicio 045](../ejercicio_045/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 047 →](../ejercicio_047/README.md)

---

### Contexto de negocio

Para cobrar los pedidos confirmados, se debe construir el módulo de pagos (`apps/payments`). Un cliente puede intentar pagar una orden múltiples veces (ej. si su tarjeta es rechazada inicialmente y luego usa otra). Por ello, una orden puede tener múltiples `PaymentAttempt` (intentos de pago), pero solo un pago exitoso final (`PAID`).

### Estado actual del sistema

Módulos de catálogo, clientes, órdenes e inventario operativos.

### Nueva necesidad

Crear el módulo `apps/payments`, modelar `PaymentTransaction` y `PaymentAttempt`, y definir el flujo de inicio de pago vinculado a una orden en estado `PENDING`.

### Objetivo

Diseñar el dominio de pagos en una arquitectura modular, separando la orden comercial de los intentos y transacciones financieras asociadas.

### Actor

Cliente Autenticado / Sistema de Pagos autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/payments` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`PaymentTransaction` (`id` UUID, `order_id` UUID, `customer_id` UUID, `amount`, `currency`, `status`, `payment_method`, `provider_reference`, `created_at`, `updated_at`), `PaymentAttempt`.

### Reglas de negocio

1. Solo se pueden iniciar pagos para órdenes en estado `PENDING`.
2. El monto del pago debe coincidir exactamente con el `total_amount` de la orden.
3. Los estados de una transacción de pago son: `INITIATED`, `AUTHORIZED`, `CAPTURED`, `FAILED`, `REFUNDED`.
4. Si un pago es exitoso (`CAPTURED`), el servicio de pagos debe notificar a `apps/orders` para transicionar la orden a `PAID`.

### Contrato esperado

Iniciar Intento de Pago:
- `POST /api/v1/payments/initiate/`
  Header: `Authorization: Bearer <token>`
  Body: `{"order_id": "uuid-orden", "payment_method": "CREDIT_CARD"}`
  Response: `201 Created`
  ```json
  {
    "payment_id": "uuid-pago",
    "order_id": "uuid-orden",
    "amount": "149.80",
    "currency": "USD",
    "status": "INITIATED",
    "client_secret": "pi_simulated_secret_123456"
  }
  ```

### Persistencia

Tabla `payments_paymenttransaction` en PostgreSQL con restricciones `CHECK (amount > 0)`.

### Relaciones

`PaymentTransaction` referencia `order_id` como UUID.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Solo el propietario de la orden puede iniciar el pago.

### Validaciones

Validar que la orden exista, pertenezca al usuario y esté en estado `PENDING`.

### Transacciones

Transacción atómica al registrar la transacción de pago.

### Casos límite

Intentar pagar una orden que ya está en estado `PAID` o `CANCELLED` (debe ser rechazada con error de dominio).

### Casos de error

`409 Conflict` si la orden ya fue pagada; `400 Bad Request` si los datos del método de pago son inválidos.

### Consideraciones de seguridad

Nunca almacenar números de tarjeta de crédito (PAN) ni códigos CVV en la base de datos (cumplimiento estricto PCI-DSS).

### Consideraciones de rendimiento

Índice compuesto sobre `(order_id, status)` en PostgreSQL.

### Fundamentos de Python relacionados

Generación de tokens y secretos simulados seguros con `secrets.token_urlsafe(32)`.

### Conceptos Django relacionados

`models.TextChoices` para estados de pago y métodos de pago.

### Conceptos DRF relacionados

Serializadores de inicio de pago y vistas dedicadas.

### PostgreSQL

`CREATE TABLE payments_paymenttransaction (id UUID PRIMARY KEY, order_id UUID NOT NULL, amount NUMERIC(12,2) NOT NULL, status VARCHAR(30) NOT NULL, ...)`.

### Arquitectura

`apps/payments` aísla toda la complejidad transaccional y financiera del resto del sistema.

### Dependencias entre módulos

`apps.payments.services` consulta `apps.orders.selectors` para validar la orden.

### Antes de programar

1. ¿Por qué es un delito y una violación crítica de seguridad almacenar números completos de tarjeta o códigos CVV en nuestra base de datos?
2. ¿Por qué una orden debe admitir múltiples transacciones de pago asociadas (1 a N) en lugar de una relación 1 a 1 rígida?

### Pruebas mínimas

1. Crear una orden pendiente, iniciar un pago mediante el endpoint -> Verificar `201 Created` y transacción en estado `INITIATED`.
2. Verificar que `amount` en el pago coincida exactamente con el total de la orden.

### Pruebas negativas

1. Intentar iniciar un pago para una orden ya pagada -> Verificar rechazo `409 Conflict`.
2. Usuario B intentando pagar la orden del Usuario A -> Verificar rechazo por ownership.

### Documentación

Documentar el modelo de pagos y los estados de transacción en el README de `apps/payments`.

### Explicación posterior

Explica los estándares de seguridad PCI-DSS (Payment Card Industry Data Security Standard) y el concepto de Tokenización provisto por pasarelas modernas.

### Aplicación profesional

Integración de pagos en pasarelas bancarias, Stripe, PayPal, MercadoPago y procesadores adquirentes.

### Reto adicional

Agregar un campo `failure_reason` que registre el motivo exacto devuelto por el procesador si la transacción falla.
