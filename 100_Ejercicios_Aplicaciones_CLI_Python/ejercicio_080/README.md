## Ejercicio 080 — Detector de Picos y Anomalías en Tasas de Error (`anomaly-detector`)

> [← Ejercicio 079](../ejercicio_079/README.md) · [Índice General](../README.md) · [Ejercicio 081 →](../ejercicio_081/README.md)

### Contexto profesional
En operaciones de sitios web y APIs de misión crítica, los fallos no siempre se manifiestan como caídas totales (100% downtime), sino como incrementos anómalos repentinos en la tasa de errores HTTP 5xx o 4xx (ej. pasar de un error rate habitual de 0.1% a 4.5% tras un nuevo despliegue), lo que indica bugs silenciosos en producción.

### Problema
Construir una CLI que procese series temporales de métricas o logs de acceso (desde archivo, STDIN o base de datos relacional PostgreSQL/SQLite), calcule la tasa de error por ventana deslizante de tiempo (Sliding Window), evalúe desviaciones estadísticas usando el algoritmo Z-Score o Media Móvil con Desviación Estándar, detecte anomalías en tiempo real y emita alertas estructuradas.

### Usuario objetivo
Ingenieros de SRE, analistas de observabilidad y DevOps.

### Objetivo
Crear un detector de anomalías estadísticas en series temporales con algoritmos de ventana deslizante, cálculo de Z-Score y salida dual.

### Ejemplo conceptual de uso
```bash
# Analizar flujo de logs detectando picos anómalos de errores 5xx
cat access_stream.log | python anomaly_detector.py analyze --window 5m --z-threshold 3.0

# Consultar anomalías históricas registradas en PostgreSQL
python anomaly_detector.py history --service "checkout-api" --days 7
```

### Requisitos funcionales
- Procesar eventos de telemetría con timestamp y código de estado/resultado.
- Algoritmo de ventana deslizante (Sliding Time Window): agrupa eventos en cubos de tiempo (ej. ventanas de 1 minuto o 5 minutos) y calcula la tasa de error: $ER = \frac{\text{errores}}{\text{total peticiones}}$.
- Algoritmo de detección de anomalías Z-Score: calcula la media móvil ($\mu$) y la desviación estándar ($\sigma$) del histórico base. Si una ventana actual tiene $Z = \frac{ER - \mu}{\sigma} > \text{umbral}$, clasificar como ANOMALÍA.
- Subcomando `analyze`: procesa el flujo en streaming o desde archivo y reporta las ventanas anómalas detectadas.
- Subcomando `history`: consulta las anomalías detectadas y registradas en PostgreSQL o SQLite opcional.
- Salida dual: tabla de incidentes en terminal o flujo JSON para disparar webhooks de alerta.

### Requisitos de CLI
- Subcomandos: `analyze`, `history`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `-w / --window <INTERVALO>` (ej. `1m`, `5m`, `15m`, default `5m`).
- Opción `--z-threshold <FLOAT>` (desviaciones estándar para considerar anomalía, default 3.0).
- Opción `--min-samples <N>` (mínimo de peticiones por ventana para tener significancia estadística, default 30).
- Opción `--format [table|json]`.
- Exit code 0 si no se detectaron anomalías críticas, 1 si se detectaron picos anómalos de error, 2 en errores.

### Entradas
- Flujo de eventos o logs con timestamps y códigos de respuesta.

### Salidas
- Reporte de anomalías detectadas, métricas Z-score y severidad en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) para almacenar el histórico de ventanas temporales y alertas.

### Validaciones
- Validar formato de intervalo de ventana temporal.
- El umbral Z-score debe ser un número positivo (típicamente entre 2.0 y 5.0).

### Casos límite
- Ventanas de tiempo con muy pocas peticiones (ej. 2 peticiones y 1 error = 50% de error, pero sin significancia estadística; ignorar si está por debajo de `--min-samples`).
- Desviación estándar cero ($\\sigma = 0$, cuando la tasa de error es completamente plana; evitar división por cero).
- Picos de tráfico generalizados vs picos reales de tasa de error.

### Manejo de errores
- Errores de parsing de fechas y timestamps.
- Errores de base de datos.

### Fundamentos de Python relacionados
- Módulo `math` y `statistics` para cálculo de medias y desviaciones estándar.
- Módulo `datetime` para agrupación por ventanas de tiempo.
- Estructuras de datos de cola de doble extremo (`collections.deque`) para implementar ventanas deslizantes de tamaño fijo en memoria.
- Conexión y persistencia en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Procesamiento analítico y estadístico en streaming.
- Detección probabilística de anomalías en observabilidad de sistemas.

### Herramientas o módulos para investigar
- `statistics` y `math`.
- `collections.deque`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para enviar un evento de alerta a PagerDuty / Slack cuando se confirme una anomalía consecutiva en N ventanas?

### Diseño de argumentos
¿Cómo nombrarías la opción para establecer un piso mínimo absoluto de tasa de error antes de alertar (ej. no alertar si la tasa de error es menor al 1% incluso si el Z-score es alto con `--min-error-rate 0.01`)?

### Diseño de variables
`sliding_window_deque`, `window_total_requests`, `window_error_requests`, `historical_baseline_mean`, `historical_baseline_stdev`, `calculated_z_score`.

### Antes de programar
1. ¿Cómo funciona la fórmula de Z-Score ($Z = (x - \mu) / \sigma$) y por qué un valor $Z > 3.0$ indica un evento que ocurre con menos del 0.3% de probabilidad bajo una distribución normal?
2. ¿Cómo mantener una ventana deslizante de las últimas 50 mediciones en memoria usando `collections.deque(maxlen=50)` para calcular la media móvil en tiempo real sin recalcular todo el historial?

### Arquitectura
Agrupador de ventanas (`time_window_aggregator.py`), detector estadístico (`zscore_detector.py`), repositorio de anomalías (`anomaly_repo.py`) y CLI.

### Pruebas mínimas
1. Procesar una serie de 20 ventanas con tasa de error normal del 0.1% seguida de 1 ventana con tasa de error del 10%; verificar que detecte exactamente esa ventana como ANOMALÍA con Z-Score alto.
2. Verificar que retorne exit code 1 ante la detección de la anomalía.

### Pruebas de error
1. Pasar un archivo de logs vacío -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Tabla de alertas con columnas: `TIMESTAMP VENTANA`, `TOTAL REQS`, `ERRORES`, `ERROR RATE %`, `BASELINE %`, `Z-SCORE` y estado `CRITICAL SPIKE` en rojo brillante.

### Explicación posterior
Explica la diferencia entre alertas basadas en umbrales estáticos fijos (ej. Error Rate > 5%) y alertas adaptativas basadas en anomalías estadísticas.

### Aplicación profesional
Monitoreo en tiempo real de deploys, detección temprana de caídas parciales de microservicios y sistemas de auto-remediación.

### Reto adicional
Implementar el algoritmo EWMA (Exponentially Weighted Moving Average) para dar mayor peso a las mediciones más recientes en la línea base histórica.

---
> [← Ejercicio 079](../ejercicio_079/README.md) · [Índice General](../README.md) · [Ejercicio 081 →](../ejercicio_081/README.md)
