# Ejercicio 048 — Webhooks de Pagos y Verificación de Firma Criptográfica

[← Ejercicio 047](../ejercicio_047/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 049 →](../ejercicio_049/README.md)

---

### Contexto de negocio

Muchas pasarelas de pago procesan transacciones de forma asíncrona (ej. pagos con transferencias bancarias, billeteras digitales o 3D Secure) y notifican el resultado final al backend mediante Webhooks (llamadas HTTP POST desde los servidores de la pasarela). El backend debe exponer un endpoint público de Webhook y verificar rigurosamente la firma criptográfica HMAC para evitar que atacantes simulen pagos exitosos falsos.

### Estado actual del sistema

Módulo de pagos con adaptador de pasarela operativo.

### Nueva necesidad

Crear el endpoint `POST /api/v1/payments/webhooks/` en `apps/payments`, desactivando autenticación JWT/CSRF pero exigiendo la verificación de la cabecera de firma criptográfica `X-Signature-SHA256` antes de procesar el evento.

### Objetivo

Dominar el diseño y aseguramiento de Webhooks en APIs REST, implementando verificación de firmas HMAC-SHA256 sobre el payload crudo (`request.body`) y procesando eventos de forma idempotente.

### Actor

Servidor de la Pasarela de Pagos (Webhook Caller)

### Módulo responsable

`apps/payments` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`PaymentWebhookAPIView`, `WebhookEventLog`, servicio `process_webhook_event`, `apps.orders.services.mark_order_as_paid`.

### Reglas de negocio

1. El endpoint de Webhook debe ser público en cuanto a JWT pero validado por firma criptográfica HMAC.
2. La firma se calcula como `hmac.new(webhook_secret, request.body, hashlib.sha256).hexdigest()` y debe compararse usando `hmac.compare_digest` para evitar ataques de tiempo (Timing Attacks).
3. Si la firma no coincide, responder inmediatamente `401 Unauthorized` o `400 Bad Request` sin procesar el contenido.
4. Si el evento es `payment.succeeded`, se confirma la transacción y se marca la orden como `PAID`.
5. El endpoint debe responder `200 OK` rápidamente para confirmar la recepción a la pasarela.

### Contrato esperado

Recepción de Webhook Válido:
- `POST /api/v1/payments/webhooks/`
  Header: `X-Signature-SHA256: 7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069`
  Body:
  ```json
  {
    "event_id": "evt_sim_12345",
    "event_type": "payment.succeeded",
    "data": {
      "payment_id": "uuid-pago",
      "provider_tx_id": "ch_real_987654",
      "amount": "149.80"
    }
  }
  ```
  Response: `200 OK` `{"status": "received"}`

### Persistencia

Inserción en `payments_webhookeventlog` para auditoría y actualización de `payments_paymenttransaction`.

### Relaciones

`PaymentTransaction`, `Order`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Verificación criptográfica de firma sobre bytes crudos antes de parsear JSON.

### Transacciones

Transacción atómica: registrar evento + actualizar pago + marcar orden pagada.

### Casos límite

Reenvío del mismo webhook múltiple veces por reintentos de la pasarela (debe ser procesado de forma idempotente sin duplicar cobros).

### Casos de error

`400 Bad Request` si la firma HMAC no coincide o el payload está corrupto.

### Consideraciones de seguridad

Usar siempre `hmac.compare_digest()` para prevenir timing attacks; nunca usar `==` estándar para hashes de seguridad.

### Consideraciones de rendimiento

Responder `200 OK` en menos de 2 segundos; delegar tareas secundarias pesadas a procesamiento en background.

### Fundamentos de Python relacionados

Módulo `hmac`, módulo `hashlib`, comparación segura en tiempo constante.

### Conceptos Django relacionados

Lectura de `request.body` crudo antes de que sea consumido por parsers de DRF.

### Conceptos DRF relacionados

`authentication_classes = []`, `permission_classes = [AllowAny]`, `APIView` para control total del flujo HTTP.

### PostgreSQL

`INSERT INTO payments_webhookeventlog (event_id, payload, is_processed, ...) ...`.

### Arquitectura

`apps/payments/views.py` recibe el webhook y delega al servicio `process_webhook_event`.

### Dependencias entre módulos

`apps/payments` invoca `apps.orders.services.mark_order_as_paid` tras validar el webhook.

### Antes de programar

1. ¿Por qué comparar dos firmas criptográficas con `if signature == calculated_signature` es vulnerable a ataques de tiempo (Timing Attacks) y cómo lo soluciona `hmac.compare_digest`?
2. ¿Por qué se debe verificar la firma sobre `request.body` (los bytes exactos recibidos) y no sobre el diccionario serializado?

### Pruebas mínimas

1. Generar un payload JSON, calcular su firma HMAC válida con la clave secreta de test, enviar petición al webhook -> Verificar `200 OK` y que la orden pase a `PAID`.
2. Enviar el mismo webhook por segunda vez -> Verificar que responda `200 OK` sin fallar ni duplicar estados.

### Pruebas negativas

1. Enviar petición con firma HMAC manipulada o incorrecta -> Verificar que responda `400 Bad Request` y que ningún dato cambie en base de datos.

### Documentación

Documentar la URL de webhook y los secretos en la guía de integraciones.

### Explicación posterior

Explica cómo operan los Webhooks en la arquitectura web moderna y por qué la combinación de HMAC + Idempotencia es el estándar dorado de seguridad para eventos asíncronos.

### Aplicación profesional

Integración con Stripe Webhooks, GitHub Webhooks, Shopify, WhatsApp Business API y pasarelas bancarias.

### Reto adicional

Registrar el log del webhook en base de datos incluso si la firma es inválida para detectar posibles intentos de intrusión.
