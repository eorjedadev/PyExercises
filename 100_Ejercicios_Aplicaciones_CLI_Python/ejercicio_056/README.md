## Ejercicio 056 — Procesador y Agregador de Streams de Logs Masivos (`stream-aggregator`)

> [← Ejercicio 055](../ejercicio_055/README.md) · [Índice General](../README.md) · [Ejercicio 057 →](../ejercicio_057/README.md)

### Contexto profesional
En infraestructuras de alto tráfico, los servidores web y microservicios producen archivos de log de decenas de gigabytes por hora. Procesar estos archivos cargándolos completos en memoria RAM colapsa el sistema (Out-Of-Memory / OOM). Se requieren herramientas de terminal capaces de procesar flujos masivos en streaming constante con consumo de memoria acotado e invariable.

### Problema
Construir una CLI que procese archivos de log masivos o flujos por STDIN (ej. volcados de millones de líneas de Nginx/Cloudflare), calcule agregados estadísticos en tiempo real (peticiones por segundo, códigos de estado HTTP agrupados, top 10 IPs con mayor tráfico, percentiles de tiempo de respuesta) usando generadores y estructuras de memoria fija, emitiendo salida dual (tabla formateada en terminal o JSON para graficadores).

### Usuario objetivo
Ingenieros de SRE, DevOps y analistas de datos.

### Objetivo
Crear un motor de agregación de streams de texto de alto rendimiento con consumo constante de memoria (O(1) memory complexity) y salida dual.

### Ejemplo conceptual de uso
```bash
# Analizar archivo de 10 GB en streaming limitando memoria
python stream_aggregator.py /var/log/nginx/access_huge.log

# Procesar flujo continuo desde STDIN y emitir resumen en JSON
cat access.log | python stream_aggregator.py --format json --top-ips 5
```

### Requisitos funcionales
- Procesar líneas en streaming mediante iteradores y generadores de Python sin almacenar líneas completas en listas.
- Extraer métricas por línea: código HTTP (2xx, 3xx, 4xx, 5xx), dirección IP, método HTTP, tamaño de respuesta en bytes y tiempo de respuesta en milisegundos.
- Agregados calculados: Total de peticiones, Tasa de error % (4xx+5xx), Ancho de banda total transferido, Top N direcciones IP más activas y Percentiles de latencia aproximados (p50, p90, p99).
- Salida dual: tabla visual en terminal o payload estructurado con `--format json`.
- Opción `--window-size N` para emitir métricas parciales cada N líneas procesadas.

### Requisitos de CLI
- Argumento posicional opcional: archivo de log (lee de `sys.stdin` si se omite).
- Opción `--format [table|json]` (default `table`).
- Opción `--top-ips <N>` (default 10).
- Opción `--window-size <N>`.
- Exit code 0 en éxito, 1 si no se procesaron líneas válidas, 2 en errores.

### Entradas
- Archivo de log o flujo continuo STDIN.

### Salidas
- Resumen estadístico formateado en STDOUT.

### Persistencia
Sin persistencia en disco.

### Validaciones
- Comprobar que al menos una línea cumpla el formato de log esperado.
- Validar que `--top-ips` y `--window-size` sean enteros positivos.

### Casos límite
- Flujo infinito de logs (ej. `tail -f access.log | python stream_aggregator.py`).
- Líneas corruptas o con formatos heterogéneos (ignorar o contar en métrica de líneas descartadas).
- Logs de 100 GB procesados sin superar 50 MB de memoria RAM residente.

### Manejo de errores
- `UnicodeDecodeError` con descarte seguro.
- `BrokenPipeError` al cortar el flujo de salida.

### Fundamentos de Python relacionados
- Generadores y expresiones generadoras (`yield`).
- Módulo `collections.Counter` y `collections.defaultdict`.
- Algoritmos de estimación de percentiles en streaming (T-Digest, P-Square o histograma de cubos fijos).
- Medición de memoria con módulo `tracemalloc` en pruebas.

### Conceptos CLI relacionados
- Arquitecturas de streaming puro y procesamiento con memoria constante.
- Soporte universal para pipelines Unix.

### Herramientas o módulos para investigar
- `collections.Counter`.
- `sys.stdin`.
- `tracemalloc`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para filtrar previamente por rango horario o método HTTP antes de agregar (`--filter-method POST`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para mostrar una tasa de procesamiento en líneas por segundo (`--throughput`)?

### Diseño de variables
`log_line_generator`, `http_status_counter`, `ip_address_counter`, `total_bytes_transferred`, `latency_bucket_histogram`.

### Antes de programar
1. ¿Por qué el uso de listas acumulativas `lines = file.readlines()` provoca fallos de Out-Of-Memory en archivos grandes y cómo garantizar que el generador libere cada línea tras procesarla?
2. ¿Cómo estimar percentiles de latencia de 100 millones de números sin guardarlos todos en un array ordenado?

### Arquitectura
Pipeline de generadores: `line_reader()` -> `log_parser()` -> `stream_accumulator()` -> `report_formatter()`.

### Pruebas mínimas
1. Procesar un dataset de prueba con 10,000 líneas y verificar que los totales de peticiones y códigos HTTP coincidan exactamente con un conteo manual.
2. Ejecutar con `--format json` y validar que el JSON sea parseable sintácticamente.

### Pruebas de error
1. Pasar un archivo vacío -> Exit code 1 con advertencia de 0 registros procesados.

### Experiencia de usuario
En modo interactivo, mostrar una barra de progreso o contador de líneas procesadas en STDERR mientras emite el reporte final en STDOUT.

### Explicación posterior
Explica la diferencia entre complejidad espacial $O(1)$ y $O(N)$ en el procesamiento de flujos masivos de datos.

### Aplicación profesional
Diagnóstico rápido en incidentes de producción, pre-procesamiento de telemetría y generadores de dashboards de tráfico.

### Reto adicional
Implementar el algoritmo P-Square o Reservoir Sampling para calcular percentiles exactos con memoria fija de menos de 100 KB.

---
> [← Ejercicio 055](../ejercicio_055/README.md) · [Índice General](../README.md) · [Ejercicio 057 →](../ejercicio_057/README.md)
