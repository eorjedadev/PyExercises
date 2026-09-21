## Ejercicio 050 — Benchmark de Servidores DNS y Latencia de Resolución (`dns-bench`)

> [← Ejercicio 049](../ejercicio_049/README.md) · [Índice General](../README.md) · [Ejercicio 051 →](../ejercicio_051/README.md)

### Contexto profesional
Los ingenieros de redes y administradores de sistemas necesitan evaluar el rendimiento y la fiabilidad de diferentes servidores DNS (Cloudflare 1.1.1.1, Google 8.8.8.8, Quad9 9.9.9.9, DNS locales de la empresa) midiendo tiempos de respuesta de consultas en milisegundos, tasas de pérdida de paquetes y consistencia de resolución.

### Problema
Construir una CLI que ejecute pruebas de rendimiento de resolución DNS concurrentes contra una lista de servidores DNS públicos y privados, midiendo latencias mínimas, medias y máximas, registrando los resultados históricos en PostgreSQL (o SQLite opcional) y generando reportes comparativos con gráficos de distribución.

### Usuario objetivo
Ingenieros de redes, administradores de sistemas y DevOps.

### Objetivo
Desarrollar una herramienta de benchmarking de resolución DNS con sockets de red o cliente DNS, persistencia relacional y análisis estadístico comparativo.

### Ejemplo conceptual de uso
```bash
# Ejecutar benchmark de resolución para un dominio contra servidores DNS estándar
python dns_bench.py run --domain "google.com" --servers "1.1.1.1,8.8.8.8,9.9.9.9" --queries 20

# Ver historial comparativo de rendimiento de DNS en PostgreSQL
python dns_bench.py history --domain "google.com"
```

### Requisitos funcionales
- Subcomando `run`: ejecuta N consultas DNS consecutivas hacia cada servidor DNS especificado, midiendo el tiempo exacto de resolución en milisegundos (`time.perf_counter`).
- Tipos de registros soportados: `A`, `AAAA`, `MX`, `TXT`, `CNAME`.
- Calcular estadísticas por servidor: latencia mínima, media, mediana, desviación estándar, percentil 95 y tasa de pérdida de paquetes (% packet loss).
- Subcomando `compare`: tabla comparativa clasificando los servidores del más rápido al más lento.
- Persistir los resultados de cada sesión de benchmark en PostgreSQL (o SQLite opcional) con timestamps y metadatos de red.
- Subcomando `history`: consulta el rendimiento histórico de servidores DNS para detectar degradaciones temporales.

### Requisitos de CLI
- Subcomandos: `run`, `compare`, `history`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `-d / --domain <DOMINIO>` (default `example.com`).
- Opción `-s / --servers <IPS>` (default lista de DNS públicos globales).
- Opción `-q / --queries <N>` (default 10 consultas por servidor).
- Opción `--timeout <SEG>` (default 2.0s).
- Exit code 0 en éxito, 1 si todos los servidores fallaron o la pérdida superó el 50%, 2 en errores de sintaxis.

### Entradas
- Dominios objetivo, listas de IPs de servidores DNS y parámetros de prueba.

### Salidas
- Tabla comparativa de benchmarks en terminal con estadísticas completas.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `dns_benchmarks` y `dns_query_samples`.

### Validaciones
- Validar que las direcciones IP de los servidores DNS sean válidas.
- Validar formato del nombre de dominio.
- Las consultas `--queries` deben ser enteros positivos entre 1 y 1000.

### Casos límite
- Servidores DNS inalcanzables que provocan timeouts repetidos.
- Respuestas DNS con paquetes truncados (manejo de UDP vs TCP fallback).
- Dominios inexistentes (NXDOMAIN; medir el tiempo de respuesta del servidor incluso si el dominio no existe).

### Manejo de errores
- `socket.timeout` y `socket.gaierror`.
- Errores de base de datos.

### Fundamentos de Python relacionados
- Conexiones de red con módulo `socket` o librería `dnspython`.
- Módulo `time` (`time.perf_counter()`) para medición de alta precisión.
- Módulo `statistics` (`mean`, `median`, `stdev`).
- Conexión y persistencia con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Benchmarking y pruebas de rendimiento en terminal.
- Presentación visual de análisis estadístico multivariable.

### Herramientas o módulos para investigar
- `socket`.
- `statistics` y `time`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para probar resolución concurrente de múltiples dominios simultáneamente?

### Diseño de argumentos
¿Cómo nombrarías la opción para vaciar la caché DNS del sistema operativo antes de iniciar la prueba si fuera necesario?

### Diseño de variables
`target_domain_name`, `dns_server_ip`, `query_latency_samples_list`, `min_latency_ms`, `avg_latency_ms`, `packet_loss_ratio`.

### Antes de programar
1. ¿Cómo construir una consulta DNS UDP cruda hacia el puerto 53 o usar sockets/librerías para medir exclusivamente el tiempo de respuesta de ese servidor sin usar la caché del SO?
2. ¿Cómo calcular la desviación estándar de latencia para evaluar la estabilidad del servidor DNS?

### Arquitectura
Motor de benchmarking (`dns_runner.py`), módulo estadístico (`stats_calc.py`), repositorio relacional (`bench_repo.py`) y CLI.

### Pruebas mínimas
1. Ejecutar benchmark de 5 consultas contra `1.1.1.1` y `8.8.8.8` para `example.com` y verificar que la tabla muestre los tiempos en ms de ambos servidores.
2. Verificar que los resultados se persistan en la base de datos.

### Pruebas de error
1. Pasar una IP de servidor DNS inalcanzable `192.0.2.1` con timeout de 1s -> Debe reportar 100% packet loss sin colapsar el programa.

### Experiencia de usuario
Tabla ordenada de menor a mayor latencia media, destacando con color verde el servidor ganador de la prueba.

### Explicación posterior
Explica la importancia de la latencia DNS en el tiempo de carga inicial de aplicaciones web y microservicios (DNS lookup overhead).

### Aplicación profesional
Optimización de conectividad en centros de datos, selección de resolutores DNS en arquitecturas cloud y diagnóstico de redes.

### Reto adicional
Generar un gráfico de barras ASCII comparativo de latencias en terminal para visualizar la diferencia de velocidad entre servidores.

---
> [← Ejercicio 049](../ejercicio_049/README.md) · [Índice General](../README.md) · [Ejercicio 051 →](../ejercicio_051/README.md)
