## Ejercicio 097 — Correlador de Trazas Distribuidas e Inyector de Trace IDs (`trace-stitcher`)

> [← Ejercicio 096](../ejercicio_096/README.md) · [Índice General](../README.md) · [Ejercicio 098 →](../ejercicio_098/README.md)

### Contexto profesional
En arquitecturas de microservicios con docenas de servicios comunicándose entre sí, una sola petición de usuario genera cientos de líneas de log dispersas en diferentes servidores y bases de datos. Para reconstruir el flujo de la petición durante la resolución de incidentes, es imprescindible correlacionar los logs mediante un identificador único de traza (`trace_id`) y de tramo (`span_id`) conforme al estándar W3C Trace Context.

### Problema
Construir una CLI que procese múltiples archivos de log desordenados provenientes de diferentes microservicios, parsee y extraiga los identificadores `trace_id`, `span_id` y `parent_span_id`, reconstruya el árbol de llamadas distribuido en orden cronológico, detecte tramos lentos (cuellos de botella de latencia) y genere una visualización gráfica de cascada (Waterfall) en terminal o en formato JSON/HTML.

### Usuario objetivo
Ingenieros de observabilidad, desarrolladores de microservicios y SREs.

### Objetivo
Crear un reconstructor y correlador de trazas distribuidas con análisis de árboles de tramos (Span Trees), detección de cuellos de botella y visualización en cascada.

### Ejemplo conceptual de uso
```bash
# Correlacionar múltiples archivos de log y reconstruir una traza específica
python trace_stitcher.py trace --trace-id "4bf92f3577b34da6a3ce929d0e0e4736" --logs-dir ./logs/

# Buscar las 5 trazas con mayor latencia total en el sistema
python trace_stitcher.py slow-traces --logs-dir ./logs/ --top 5

# Generar diagrama en cascada de una traza en formato terminal o HTML
python trace_stitcher.py waterfall "4bf92f3577b34da6a3ce929d0e0e4736" --format tui
```

### Requisitos funcionales
- Ingestión y parsing de logs estructurados (JSON) o semi-estructurados de múltiples servicios buscando campos de correlación estándar: `trace_id`, `span_id`, `parent_span_id`, `service_name`, `operation_name`, `timestamp`, `duration_ms` y `error`.
- Subcomando `trace <TRACE_ID>`: recopila todas las entradas asociadas a la traza, construye el árbol de spans resolviendo las relaciones padre-hijo y emite la jerarquía de ejecución en orden cronológico.
- Subcomando `waterfall <TRACE_ID>`: dibuja un diagrama en cascada en terminal (estilo DevTools Network / Jaeger) mostrando barras horizontales proporcionales al tiempo de inicio y duración de cada tramo:
  ```
  [api-gateway]       ████████████████████ (250ms)
    [auth-service]    ████ (45ms)
    [orders-service]       ██████████ (180ms)
      [postgres-db]          ████ (50ms)
  ```
- Subcomando `slow-traces`: identifica y lista las trazas completas con mayor tiempo total de respuesta o que contienen errores en alguno de sus spans.
- Persistencia opcional de trazas correlacionadas en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `trace`, `waterfall`, `slow-traces`, `index`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--logs-dir <RUTA>` (directorio con archivos de log de múltiples servicios).
- Opción `--format [tui|json|html]` (default `tui`).
- Exit code 0 en éxito, 1 si el `trace_id` no fue encontrado, 2 en errores de sintaxis.

### Entradas
- Archivos de logs de microservicios y parámetros de búsqueda de traza.

### Salidas
- Diagramas en cascada, jerarquías de spans y análisis de cuellos de botella en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `spans`, `traces` y `trace_service_map`.

### Validaciones
- El `trace_id` debe cumplir el formato estándar W3C (32 caracteres hexadecimales).
- Validar formato de fecha y duraciones.

### Casos límite
- Trazas incompletas (un microservicio perdió logs y un span hijo no tiene registro de su span padre; manejar como nodo huérfano en la raíz).
- Logs con relojes de servidor desincronizados (reajustar timestamps relativos al span raíz).
- Trazas gigantescas con miles de spans (ej. llamadas en bucle $N+1$ a bases de datos).

### Manejo de errores
- Errores de lectura de archivos de log.
- Formatos de log corruptos.

### Fundamentos de Python relacionados
- Teoría de árboles jerárquicos y relaciones padre-hijo con diccionarios y referencias.
- Módulo `datetime` para cálculo de tiempos relativos y offsets de inicio.
- Renderizado gráfico de barras de tiempo en terminal usando caracteres de bloque Unicode (`█`, `░`, `│`).
- Conexión y consultas relacionales en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Observabilidad distribuida y análisis de trazas (Distributed Tracing) en terminal.
- Visualización gráfica de cascadas de ejecución temporal (Waterfall Charts).

### Herramientas o módulos para investigar
- `re` y `json`.
- `pathlib`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para detectar automáticamente consultas $N+1$ repetidas en la traza (`--detect-n-plus-one`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para filtrar solo spans que terminaron en estado de error (`--errors-only`)?

### Diseño de variables
`span_records_map`, `trace_spans_tree_root`, `relative_start_offset_ms`, `span_execution_duration_ms`, `critical_path_bottleneck_span`.

### Antes de programar
1. ¿Cómo calcular la posición y el ancho de la barra gráfica en terminal para cada span hijo respecto a la duración total de la traza raíz?
2. ¿Cómo construir el árbol de spans recursivamente a partir de una lista plana de registros resolviendo `parent_span_id`?

### Arquitectura
Parser de logs (`log_ingester.py`), constructor del árbol de spans (`span_tree_builder.py`), analizador de cuellos de botella (`critical_path.py`), renderizador de cascada (`waterfall_tui.py`) y CLI.

### Pruebas mínimas
1. Procesar un conjunto de logs de 3 servicios con una traza compartida, reconstruir el árbol y verificar que `api-gateway` sea la raíz y `postgres-db` sea el nodo hoja.
2. Ejecutar `waterfall` y validar que el diagrama en terminal muestre las barras alineadas con sus duraciones en ms.

### Pruebas de error
1. Consultar un `trace_id` que no existe en los logs -> Exit code 1 con mensaje claro.

### Experiencia de usuario
Diagrama en cascada en terminal de alta legibilidad, destacando en rojo los spans con errores y en amarillo los spans que representan más del 50% del tiempo total.

### Explicación posterior
Explica la especificación W3C Trace Context (`traceparent` header) y la diferencia entre métricas, logs y trazas distribuidas (los tres pilares de la observabilidad).

### Aplicación profesional
Diagnóstico de latencia en microservicios, análisis de causas raíz en caídas de producción y optimización de flujos distribuidos.

### Reto adicional
Calcular automáticamente la 'Ruta Crítica' (Critical Path) de la traza para identificar exactamente qué secuencia síncrona de operaciones determina la duración total mínima de la petición.

---
> [← Ejercicio 096](../ejercicio_096/README.md) · [Índice General](../README.md) · [Ejercicio 098 →](../ejercicio_098/README.md)
