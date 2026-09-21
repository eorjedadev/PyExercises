## Ejercicio 094 — Simulador de Rate Limiting con Algoritmo Token Bucket (`rate-limiter-cli`)

> [← Ejercicio 093](../ejercicio_093/README.md) · [Índice General](../README.md) · [Ejercicio 095 →](../ejercicio_095/README.md)

### Contexto profesional
En pasarelas de API (API Gateways), microservicios y sistemas de protección contra ataques de denegación de servicio (DDoS / Brute Force), se implementan algoritmos de limitación de tasa (Rate Limiting) como *Token Bucket* o *Leaky Bucket* para controlar cuántas peticiones por segundo puede realizar cada cliente/IP, permitiendo ráfagas cortas (bursts) mientras se mantiene una tasa media constante.

### Problema
Construir una CLI que simule y evalúe algoritmos de Rate Limiting (Token Bucket y Ventana Deslizante) con persistencia de estado en base de datos relacional (PostgreSQL como motor principal, o SQLite local opcional), permitiendo simular ráfagas de tráfico concurrentes desde múltiples clientes, evaluar si una petición es aceptada (`200 OK`) o rechazada (`429 Too Many Requests`), calcular el tiempo de espera hasta el próximo token (`Retry-After`) y generar reportes de saturación.

### Usuario objetivo
Desarrolladores de APIs, arquitectos de backend e ingenieros de seguridad.

### Objetivo
Implementar un simulador y motor de Rate Limiting con algoritmo Token Bucket atómico, persistencia relacional y pruebas de estrés concurrentes.

### Ejemplo conceptual de uso
```bash
# Evaluar si una petición individual de una IP es permitida
python rate_limiter_cli.py check --client-ip "198.51.100.25" --capacity 10 --refill-rate 2.0

# Simular ráfaga de 50 peticiones concurrentes de 5 clientes distintos
python rate_limiter_cli.py simulate --clients 5 --requests 50 --capacity 10 --refill-rate 5.0

# Ver estado actual de los buckets de tokens en PostgreSQL
python rate_limiter_cli.py status
```

### Requisitos funcionales
- Implementar el algoritmo **Token Bucket** matemático:
  - Cada cliente tiene un cubo con una capacidad máxima de tokens ($C$) y una tasa de recarga de tokens por segundo ($r$).
  - Al llegar una petición en el tiempo $t$: se calcula el tiempo transcurrido desde la última recarga $\Delta t = t - t_{\text{last}}$, se añaden $\Delta t \times r$ tokens (sin superar $C$).
  - Si hay al menos 1 token disponible: restar 1 token, aceptar la petición (`ALLOWED`) y actualizar $t_{\text{last}}$.
  - Si no hay tokens disponibles: rechazar la petición (`RATE_LIMITED`), calcular segundos necesarios para acumular 1 token y devolver cabecera `Retry-After: <segundos>`.
- Subcomando `check`: evalúa una sola petición atómica para un cliente dado.
- Subcomando `simulate`: lanza un generador de tráfico concurrente con múltiples hilos/procesos simulando peticiones y midiendo porcentaje de rechazos (HTTP 429).
- Subcomando `reset <CLIENT_IP>`: restablece el cubo de tokens de un cliente a su capacidad máxima.
- Persistencia de estados de bucket (`client_id`, `tokens_count`, `last_refill_timestamp`) en PostgreSQL con bloqueos de fila atómicos (`SELECT ... FOR UPDATE`) o SQLite.

### Requisitos de CLI
- Subcomandos: `check`, `simulate`, `status`, `reset`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--capacity <N>`: capacidad máxima del bucket (default 10).
- Opción `--refill-rate <FLOAT>`: tokens recargados por segundo (default 2.0).
- Exit code 0 si la petición fue permitida (`ALLOWED`), 1 si fue rechazada por límite de tasa (`RATE_LIMITED`), 2 en errores.

### Entradas
- Identificadores de cliente (IP / API Key), parámetros de capacidad/recarga y configuraciones de simulación.

### Salidas
- Estado de aceptación/rechazo, tokens restantes y cabeceras `Retry-After` en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `rate_limit_buckets` y `rate_limit_audit_log`.

### Validaciones
- La capacidad debe ser un entero mayor o igual a 1.
- La tasa de recarga debe ser un flotante estrictamente positivo.

### Casos límite
- Múltiples peticiones simultáneas del mismo cliente en el mismo milisegundo (garantizar atomicidad mediante transacciones con bloqueo de fila en PostgreSQL para evitar race conditions).
- Clientes inactivos durante días (al recibir una petición tras mucho tiempo, el cálculo de recarga debe acotar los tokens a la capacidad máxima $C$, no acumular tokens infinitos).
- Parámetros de recarga fraccionarios (ej. 0.5 tokens/seg = 1 token cada 2 segundos).

### Manejo de errores
- Excepciones de concurrencia y base de datos.

### Fundamentos de Python relacionados
- Matemáticas de algoritmos de Token Bucket y Leaky Bucket.
- Concurrencia con `concurrent.futures.ThreadPoolExecutor` para pruebas de estrés.
- Transacciones atómicas con bloqueo de fila (`SELECT ... FOR UPDATE` en PostgreSQL).
- Módulo `time` (`time.time()`).

### Conceptos CLI relacionados
- Diseño e implementación de algoritmos de Rate Limiting y control de flujo en terminal.
- Gestión de cabeceras HTTP de limitación de tasa (RFC 6585: HTTP 429 y Retry-After).

### Herramientas o módulos para investigar
- `time`.
- `concurrent.futures`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `benchmark-cost` para medir la latencia adicional en microsegundos que introduce la verificación del rate limiter en PostgreSQL?

### Diseño de argumentos
¿Cómo nombrarías la opción para permitir costo variable por petición (ej. una búsqueda pesada consume 5 tokens en lugar de 1 con `--cost 5`)?

### Diseño de variables
`token_bucket_capacity`, `token_refill_rate_per_sec`, `current_tokens_balance`, `last_refill_timestamp_float`, `retry_after_seconds_wait`.

### Antes de programar
1. ¿Cómo formular el cálculo atómico de tokens en SQL o en memoria: $\text{tokens} = \min(\text{capacidad}, \text{tokens\_previos} + (t_{\text{actual}} - t_{\text{previo}}) \times r)$?
2. ¿Cómo calcular con precisión los segundos de espera para la cabecera `Retry-After`: $\text{espera} = \frac{1.0 - \text{tokens}}{r}$?

### Arquitectura
Motor de Token Bucket (`token_bucket.py`), repositorio relacional atómico (`bucket_repository.py`), simulador de carga concurrente (`traffic_simulator.py`) y CLI.

### Pruebas mínimas
1. Crear bucket de capacidad 3 con recarga de 1 token/seg; realizar 3 peticiones consecutivas inmediatas y verificar que las 3 sean `ALLOWED` (tokens restantes: 2, 1, 0).
2. Realizar una 4ta petición inmediata y verificar que sea `RATE_LIMITED` (HTTP 429) con `Retry-After: 1.0s` y retorne exit code 1.
3. Esperar 1 segundo, reintentar y verificar que sea `ALLOWED`.

### Pruebas de error
1. Pasar una capacidad negativa `--capacity -5` -> Exit code 2 con error de validación.

### Experiencia de usuario
Respuesta clara en terminal con cabeceras simuladas: `HTTP/1.1 429 Too Many Requests`, `X-RateLimit-Limit: 10`, `X-RateLimit-Remaining: 0`, `Retry-After: 1.5s`.

### Explicación posterior
Explica la diferencia entre el algoritmo Token Bucket (permite ráfagas de tamaño C), Leaky Bucket (emite tráfico a tasa constante fija) y Fixed Window Counter (sufre del problema del borde de ventana).

### Aplicación profesional
Protección de endpoints de login contra fuerza bruta, limitación de consumo de APIs públicas y control de cuotas en plataformas SaaS.

### Reto adicional
Implementar el algoritmo Sliding Window Log (Registro de Ventana Deslizante) y comparar su precisión y consumo de memoria frente a Token Bucket.

---
> [← Ejercicio 093](../ejercicio_093/README.md) · [Índice General](../README.md) · [Ejercicio 095 →](../ejercicio_095/README.md)
