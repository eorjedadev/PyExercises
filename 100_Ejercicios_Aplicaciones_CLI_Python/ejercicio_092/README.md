## Ejercicio 092 — Suite de Micro-Benchmarking y Detección de Regresiones (`perf-bench-cli`)

> [← Ejercicio 091](../ejercicio_091/README.md) · [Índice General](../README.md) · [Ejercicio 093 →](../ejercicio_093/README.md)

### Contexto profesional
Al optimizar algoritmos críticos (funciones de hashing, serialización JSON, transformaciones de datos, consultas de base de datos PostgreSQL), los desarrolladores necesitan medir el tiempo de ejecución con rigor estadístico (iteraciones de calentamiento / warmup, múltiples repeticiones, cálculo de medianas y percentiles) y comparar los resultados contra una línea base para detectar regresiones de rendimiento en CI/CD.

### Problema
Construir una CLI de benchmarking de rendimiento que ejecute funciones de Python o comandos de terminal externos con calentamiento previo, tome N muestras estadísticas, calcule métricas (media, mediana, desviación estándar, p95, p99), compare los resultados contra un archivo de baseline previo y falle con exit code 1 si se detecta una degradación de rendimiento superior a un porcentaje de tolerancia.

### Usuario objetivo
Desarrolladores de software, ingenieros de rendimiento y optimizadores de algoritmos.

### Objetivo
Crear una suite de benchmarking estadístico para terminal con detección automática de regresiones de rendimiento y exportación de reportes.

### Ejemplo conceptual de uso
```bash
# Ejecutar benchmark de una función o script con 100 iteraciones y 5 de warmup
python perf_bench_cli.py run "./process_data.py" --iterations 100 --warmup 5 -o bench_results.json

# Comparar resultados contra la línea base y fallar si hay una regresión > 5%
python perf_bench_cli.py compare --baseline baseline_v1.json --current bench_results.json --max-regression 5.0
```

### Requisitos funcionales
- Subcomando `run <TARGET>`: ejecuta el comando o función especificada con las iteraciones de calentamiento (`--warmup N`) para estabilizar cachés de CPU/disco y JIT, seguidas de N iteraciones de medición con temporizadores de alta resolución (`time.perf_counter_ns`).
- Métricas estadísticas calculadas: Mínimo, Máximo, Media, Mediana, Desviación Estándar, Rango Intercuartílico (IQR), p95 y p99.
- Subcomando `compare`: compara dos archivos de resultados de benchmark (`--baseline` vs `--current`), calcula la variación porcentual de la mediana de tiempo ($\% \Delta = \frac{T_{curr} - T_{base}}{T_{base}} \times 100$) e indica si hubo mejora (`SPEEDUP`) o degradación (`REGRESSION`).
- Persistencia de resultados históricos en PostgreSQL (o SQLite opcional) para graficar la evolución del rendimiento a través de los commits de Git.
- Subcomando `history`: consulta la tendencia de rendimiento de un benchmark a lo largo del tiempo.

### Requisitos de CLI
- Subcomandos: `run`, `compare`, `history`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `-n / --iterations <N>` (default 50).
- Opción `-w / --warmup <N>` (default 5).
- Opción `--max-regression <PORCENTAJE>` (default 5.0).
- Opción `--format [table|json|markdown]`.
- Exit code 0 si no hay regresiones de rendimiento, 1 si se superó el límite de regresión tolerado en `compare`, 2 en errores.

### Entradas
- Comandos o scripts a medir y archivos de resultados de benchmark.

### Salidas
- Tablas estadísticas, comparativas de rendimiento y reportes en STDOUT.

### Persistencia
Archivos JSON de resultados y base de datos relacional PostgreSQL / SQLite para histórico.

### Validaciones
- Las iteraciones deben ser enteros positivos mayores a 0.
- El archivo de baseline debe existir y tener un formato válido.

### Casos límite
- Tareas que tardan microsegundos vs tareas que tardan varios minutos por iteración (adaptar formateo de unidades: ns, µs, ms, s).
- Mediciones con alta variabilidad por procesos en segundo plano del sistema (detectar y alertar sobre ruido ambiental con desviación estándar alta).
- Comandos que retornan errores durante la ejecución.

### Manejo de errores
- `subprocess.CalledProcessError` si el comando objetivo falla.
- Errores de lectura de JSONs de benchmark.

### Fundamentos de Python relacionados
- Temporización de ultra-alta precisión con `time.perf_counter_ns` y `time.process_time`.
- Análisis estadístico avanzado con módulo estándar `statistics` (`median`, `stdev`, `quantiles`).
- Invocación de procesos con `subprocess.run`.
- Persistencia relacional con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Metodología rigurosa de benchmarking y micro-benchmarking de software.
- Detección de regresiones de rendimiento en pipelines de CI/CD.

### Herramientas o módulos para investigar
- `time.perf_counter_ns`.
- `statistics`.
- `subprocess`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para aislar la afinidad de CPU del proceso a un solo núcleo para reducir la variabilidad de las mediciones en Linux?

### Diseño de argumentos
¿Cómo nombrarías la opción para realizar pruebas de significancia estadística (como el test t de Student o Mann-Whitney U) antes de declarar una regresión?

### Diseño de variables
`benchmark_target_command`, `execution_time_nanoseconds_samples`, `warmup_iterations_count`, `statistical_summary_dto`, `regression_delta_percentage`.

### Antes de programar
1. ¿Por qué la mediana es una métrica mucho más robusta que el promedio simple para benchmarks de rendimiento (porque la mediana es inmune a valores atípicos aislados causados por pausas del recolector de basura o interrupciones del SO)?
2. ¿Por qué es fundamental ejecutar iteraciones de calentamiento (warmup) antes de medir?

### Arquitectura
Motor de ejecución (`benchmark_runner.py`), calculador estadístico (`stats_engine.py`), comparador de regresiones (`regression_checker.py`), repositorio (`bench_repo.py`) y CLI.

### Pruebas mínimas
1. Ejecutar benchmark sobre un script rápido de prueba con 20 iteraciones y verificar que devuelva media, mediana y p95 con unidades correctas.
2. Comparar un baseline de 100ms contra un resultado actual de 110ms con `--max-regression 5.0` y verificar que detecte una regresión del 10% y retorne exit code 1.

### Pruebas de error
1. Pasar un archivo de baseline inexistente a `compare` -> Exit code 2 con error claro.

### Experiencia de usuario
Tabla comparativa clara con colores: Verde para mejoras de rendimiento (`+15.2% SPEEDUP`), Amarillo para cambios dentro de la tolerancia, y Rojo para degradaciones (`-8.4% REGRESSION`).

### Explicación posterior
Explica la diferencia entre ruido de medición (Measurement Noise) y regresión real de rendimiento, y cómo el calentamiento de cachés estabiliza las mediciones.

### Aplicación profesional
Quality gates de rendimiento en CI/CD para librerías de alto rendimiento, optimización de motores de bases de datos y algoritmos críticos.

### Reto adicional
Implementar medición simultánea del consumo de memoria RAM máxima residente (Peak RSS) durante cada iteración del benchmark.

---
> [← Ejercicio 091](../ejercicio_091/README.md) · [Índice General](../README.md) · [Ejercicio 093 →](../ejercicio_093/README.md)
