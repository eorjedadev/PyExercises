## Ejercicio 019 — Inspector de Cabeceras HTTP y Latencia (`net-peek`)

> [← Ejercicio 018](../ejercicio_018/README.md) · [Índice General](../README.md) · [Ejercicio 020 →](../ejercicio_020/README.md)

### Contexto profesional
Al depurar balanceadores de carga, proxies inversos (Cloudflare, AWS ALB) y configuraciones de seguridad web (CORS, CSP, HSTS), los desarrolladores necesitan inspeccionar cabeceras de respuesta, tiempos de resolución DNS y latencias HTTP directamente en terminal.

### Problema
Construir una CLI similar a `curl -I` que realice peticiones HTTP/HTTPS a una URL, mida la latencia de respuesta, muestre todas las cabeceras recibidas formateadas y analice la presencia de cabeceras de seguridad recomendadas.

### Usuario objetivo
Desarrolladores web, DevOps y auditores de seguridad.

### Objetivo
Desarrollar una herramienta de diagnóstico HTTP con medición de tiempos, auditoría de cabeceras de seguridad y soporte de redirecciones.

### Ejemplo conceptual de uso
```bash
# Inspeccionar cabeceras de una URL
python net_peek.py https://api.ejemplo.com

# Seguir redirecciones y auditar cabeceras de seguridad
python net_peek.py https://ejemplo.com --follow-redirects --audit-security
```

### Requisitos funcionales
- Realizar peticiones HTTP usando métodos `HEAD` o `GET`.
- Medir tiempo total de respuesta en milisegundos con alta precisión (`time.perf_counter`).
- Mostrar código de estado y texto canónico (ej. `200 OK`, `403 Forbidden`).
- Listar cabeceras de respuesta ordenadas alfabéticamente o agrupadas.
- Soportar seguimiento de redirecciones (`--follow-redirects / -L`).
- Modo `--audit-security`: evalúa si están presentes cabeceras clave como `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options` y reporta ausencias.

### Requisitos de CLI
- Argumento posicional: URL objetivo.
- Opción `-X / --method`: `HEAD`, `GET`, `POST`, `OPTIONS` (default `HEAD`).
- Opción `--timeout <SEG>`: tiempo máximo de espera en segundos (default 10).
- Flag `-L / --follow-redirects`.
- Flag `--audit-security`.
- Flag `--json`: salida estructurada con métricas y cabeceras.
- Exit code 0 si la petición fue exitosa (2xx/3xx), 1 si devolvió error de cliente/servidor (4xx/5xx), 2 en error de conexión/DNS.

### Entradas
- URL y opciones de petición.

### Salidas
- Resumen de petición, latencia y cabeceras en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Validar formato de URL (debe incluir esquema `http://` o `https://`).
- Validar timeout positivo.

### Casos límite
- Certificados SSL autofirmados o caducados (opción `--insecure / -k`).
- Bucles infinitos de redirección (límite máximo de 10 saltos).
- URLs que resuelven a múltiples direcciones IP.

### Manejo de errores
- `urllib.error.URLError` / `socket.timeout`: Errores de red y DNS.
- `ssl.SSLError`: Errores de verificación de certificados.

### Fundamentos de Python relacionados
- Biblioteca estándar `urllib.request`, `http.client` o librería `urllib`.
- Módulo `time` (`time.perf_counter()`).
- Módulo `ssl` para control de contexto TLS.

### Conceptos CLI relacionados
- Medición precisa de métricas en herramientas de red.
- Salida dual (humano con colores vs JSON para automatización).

### Herramientas o módulos para investigar
- `urllib.request` y `urllib.error`.
- `http.client`.
- `time` y `argparse`.

### Diseño de comandos
¿Cómo permitirías enviar cabeceras personalizadas en la petición con `-H "Authorization: Bearer xyz"`?

### Diseño de argumentos
¿Cómo nombrarías la opción para mostrar únicamente el valor de una cabecera específica (ej. `--header-only Content-Type`)?

### Diseño de variables
`target_url`, `http_method`, `response_headers`, `latency_ms`, `security_audit_results`, `redirect_history`.

### Antes de programar
1. ¿Por qué usar `HEAD` en lugar de `GET` cuando solo se quieren consultar cabeceras, y cuándo un servidor podría rechazar `HEAD`?
2. ¿Cómo medir la latencia aislando el tiempo de red sin incluir el tiempo de procesamiento de la CLI?

### Arquitectura
Cliente HTTP (`http_client.py`), auditor de seguridad (`security_checker.py`) y CLI (`net_peek.py`).

### Pruebas mínimas
1. Consultar un dominio público conocido y verificar que muestre el código de estado y tiempo en ms.
2. Ejecutar con `--audit-security` y verificar el reporte de cabeceras recomendadas.

### Pruebas de error
1. Consultar un dominio inexistente `https://dominio-invalido-xyz.test` -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Formateo visual con colores: cabeceras destacadas, valores alineados y resumen final de latencia.

### Explicación posterior
Explica el propósito de la cabecera `Strict-Transport-Security` (HSTS) y los riesgos de `X-Frame-Options` ausente.

### Aplicación profesional
Diagnóstico rápido en operaciones de red, auditorías de seguridad perimetral y verificación de deploys.

### Reto adicional
Desglosar la latencia en fases: tiempo de resolución DNS, tiempo de conexión TCP y tiempo de respuesta HTTP inicial (TTFB).

---
> [← Ejercicio 018](../ejercicio_018/README.md) · [Índice General](../README.md) · [Ejercicio 020 →](../ejercicio_020/README.md)
