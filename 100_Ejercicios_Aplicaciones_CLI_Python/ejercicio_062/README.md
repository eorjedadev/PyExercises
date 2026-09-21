## Ejercicio 062 — Simulador y Reintentador de Envíos de Webhooks (`webhook-tester`)

> [← Ejercicio 061](../ejercicio_061/README.md) · [Índice General](../README.md) · [Ejercicio 063 →](../ejercicio_063/README.md)

### Contexto profesional
En arquitecturas orientadas a eventos y pasarelas de pago (Stripe, Shopify, GitHub), los sistemas envían eventos HTTP POST firmados criptográficamente (webhooks) hacia aplicaciones cliente. Si el receptor falla temporalmente, el emisor debe reintentar con retroceso exponencial (Exponential Backoff) y registrar los intentos.

### Problema
Construir una CLI que simule el envío de eventos webhook hacia un endpoint HTTP, firme el payload usando HMAC-SHA256 con una clave secreta compartida en la cabecera `X-Signature-SHA256`, ejecute una política de reintentos con retroceso exponencial ante fallos de red o errores 5xx y persista el historial de intentos en base de datos relacional (PostgreSQL o SQLite opcional).

### Usuario objetivo
Desarrolladores backend, ingenieros de integración y DevOps.

### Objetivo
Crear un despachador de webhooks resiliente con firma criptográfica HMAC, reintentos con retroceso exponencial y persistencia relacional.

### Ejemplo conceptual de uso
```bash
# Enviar un evento webhook con firma HMAC y hasta 3 reintentos
python webhook_tester.py send https://api.cliente.com/webhooks/orders --event "order.created" --payload order.json --secret "whsec_abc123" --max-retries 3

# Ver historial de entregas de webhooks en PostgreSQL
python webhook_tester.py history --event "order.created"
```

### Requisitos funcionales
- Subcomando `send <URL>`: envía una petición HTTP POST con el payload JSON especificado.
- Firma criptográfica HMAC-SHA256: calcula la firma de la carga útil usando la clave secreta y la inyecta en la cabecera `X-Signature-SHA256` o `Stripe-Signature` (con timestamp para mitigar ataques de repetición).
- Política de reintentos con retroceso exponencial: ante fallos de conexión o códigos 5xx/429, reintentar esperando $t = \text{base\_delay} \times 2^{\text{intento}} + \text{jitter}$.
- Registrar cada intento de entrega (`delivery_id`, `url`, `event_type`, `status_code`, `attempts_count`, `duration_ms`, `response_body`, `success`) en PostgreSQL o SQLite opcional.
- Subcomando `history`: consulta el historial de entregas y tasas de éxito.
- Subcomando `resend <DELIVERY_ID>`: reenvía manualmente un webhook fallido anterior.

### Requisitos de CLI
- Subcomandos: `send`, `history`, `resend`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--secret <SECRET>`.
- Opción `--max-retries <N>` (default 3).
- Opción `--base-delay <SEG>` (default 1.0).
- Opción `--timeout <SEG>` (default 5.0).
- Exit code 0 si el webhook fue entregado exitosamente (código 2xx), 1 si se agotaron los reintentos sin éxito, 2 en errores de configuración.

### Entradas
- URL de destino, payload JSON, clave secreta y parámetros de reintento.

### Salidas
- Resumen de entrega y tiempos en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `webhook_deliveries` y `webhook_attempts`.

### Validaciones
- Validar formato de URL y sintaxis JSON del payload.
- El número de reintentos debe ser un entero entre 0 y 10.

### Casos límite
- Servidor receptor que responde con cabecera `Retry-After` (respetar el tiempo indicado por el receptor si existe).
- Servidor receptor que cae en timeout reiteradamente.
- Payloads gigantes de varios megabytes.

### Manejo de errores
- `urllib.error.HTTPError` y `urllib.error.URLError`.
- Errores de persistencia en base de datos.

### Fundamentos de Python relacionados
- Módulo `hmac` y `hashlib` para cálculo de firmas criptográficas HMAC-SHA256.
- Módulo `time` (`time.sleep()`, `time.perf_counter()`).
- Módulo `random` para cálculo de Jitter en el retroceso exponencial.
- Conexión y transacciones con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Implementación de patrones de resiliencia de red (Exponential Backoff with Jitter).
- Firma criptográfica de mensajes para autenticación de origen.

### Herramientas o módulos para investigar
- `hmac` y `hashlib`.
- `urllib.request`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para enviar un lote masivo de webhooks en paralelo desde un archivo CSV (`send-batch`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para simular eventos de plataformas específicas como Stripe, GitHub o Shopify con sus formatos de firma correspondientes (`--provider stripe|github|custom`)?

### Diseño de variables
`webhook_target_url`, `raw_payload_bytes`, `hmac_signature_hex`, `retry_attempt_count`, `exponential_backoff_delay`, `delivery_history_record`.

### Antes de programar
1. ¿Cómo calcular la firma HMAC-SHA256: `hmac.new(secret.encode(), payload_bytes, hashlib.sha256).hexdigest()`?
2. ¿Por qué agregar una pequeña variación aleatoria (Jitter) al tiempo de espera previene el problema de estampida (Thundering Herd Problem) cuando muchos eventos reintentan simultáneamente?

### Arquitectura
Firmador criptográfico (`signer.py`), cliente de reintentos (`retry_dispatcher.py`), repositorio de entregas (`delivery_repo.py`) y CLI.

### Pruebas mínimas
1. Enviar webhook a un servidor local mock con clave secreta y verificar que la cabecera `X-Signature-SHA256` coincida con la firma calculada manualmente.
2. Probar reintentos contra un endpoint que responde 500 y verificar que intente exactamente N veces antes de marcar fallo.

### Pruebas de error
1. Pasar un payload con JSON inválido -> Exit code 2 con error descriptivo.

### Experiencia de usuario
Progreso en tiempo real indicando: `[Intento 1/4] Falló (HTTP 503). Esperando 2.1s...`, `[Intento 2/4] Éxito (HTTP 200 OK en 142ms)`.

### Explicación posterior
Explica la importancia de la idempotencia en el consumo de webhooks y cómo los receptores deben procesar claves de idempotencia (`idempotency_key`) para no duplicar acciones.

### Aplicación profesional
Pruebas de integración de webhooks de pago, depuración de pasarelas de eventos y desarrollo de arquitecturas event-driven.

### Reto adicional
Implementar un subcomando `listen --port 9000 --secret "..."` que levante un servidor receptor para recibir, verificar la firma HMAC y mostrar webhooks entrantes en tiempo real.

---
> [← Ejercicio 061](../ejercicio_061/README.md) · [Índice General](../README.md) · [Ejercicio 063 →](../ejercicio_063/README.md)
