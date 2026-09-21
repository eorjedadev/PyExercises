## Ejercicio 053 — Recolector de Métricas del Sistema y Evaluador de Alertas (`metric-guard`)

> [← Ejercicio 052](../ejercicio_052/README.md) · [Índice General](../README.md) · [Ejercicio 054 →](../ejercicio_054/README.md)

### Contexto profesional
En servidores de producción sin agentes pesados de observabilidad, se requiere una herramienta de monitoreo ligera que recolecte métricas del sistema operativo (uso de CPU %, consumo de memoria RAM %, espacio libre en disco %, tasa de I/O y carga promedio), evalúe reglas de alerta configurables y emita códigos de salida específicos para alertar a sistemas de monitoreo o disparar auto-escalado.

### Problema
Construir una CLI que recopile métricas del sistema mediante APIs del sistema operativo o el sistema de archivos virtual (`/proc` en Linux o librerías estándar/multiplataforma), compare las métricas contra un archivo de umbrales de alerta (`rules.json`), persista las muestras en PostgreSQL o SQLite opcional y emita alertas en formato JSON o tabular.

### Usuario objetivo
Administradores de sistemas, ingenieros de SRE y DevOps.

### Objetivo
Desarrollar un recolector de métricas de host con motor de evaluación de reglas de umbral, persistencia en series temporales y códigos de salida para alertamiento.

### Ejemplo conceptual de uso
```bash
# Recolectar métricas actuales y evaluar contra reglas
python metric_guard.py check --rules alert_rules.json

# Ver métricas en tiempo real en formato JSON
python metric_guard.py collect --format json

# Ver historial de alertas disparadas en PostgreSQL
python metric_guard.py history --severity critical
```

### Requisitos funcionales
- Subcomando `collect`: recopila métricas instantáneas del sistema:
  - CPU: porcentaje de uso y load average (1m, 5m, 15m).
  - Memoria: RAM total, usada, libre y porcentaje de uso.
  - Disco: espacio total, usado, disponible y porcentaje por partición.
  - Procesos: cantidad total de procesos y procesos en estado zombie.
- Subcomando `check`: evalúa las métricas contra reglas (ej. `cpu_usage_percent > 85.0`, `disk_free_gb < 10.0`), determinando nivel de alerta (`WARNING`, `CRITICAL`).
- Persistencia de muestras y eventos de alerta en PostgreSQL (o SQLite opcional).
- Subcomando `history`: consulta alertas pasadas y duración de incidentes.
- Códigos de salida según el estado del sistema: 0 si todo está OK, 1 si hay alertas WARNING, 2 si hay alertas CRITICAL o errores.

### Requisitos de CLI
- Subcomandos: `collect`, `check`, `history`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--rules <RUTA>` (default `alert_rules.json`).
- Opción `--format [table|json]` (default `table`).
- Exit code 0 en estado OK, 1 en Warning, 2 en Critical o error de ejecución.

### Entradas
- Reglas de alerta y métricas del sistema operativo.

### Salidas
- Reporte de métricas, estado de alertas y resumen en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `system_metrics` y `alert_events`.

### Validaciones
- Validar sintaxis y operadores en las reglas de alerta (`>`, `<`, `>=`, `<=`, `==`).
- Validar que los nombres de métricas en las reglas existan.

### Casos límite
- Sistemas con múltiples discos o particiones montadas.
- Servidores bajo carga extrema (el recolector debe ejecutarse con mínimo consumo de CPU).
- Plataformas multiplataforma (compatibilidad con Linux y Windows).

### Manejo de errores
- `PermissionError` al consultar ciertas métricas del sistema.
- Errores de acceso a base de datos.

### Fundamentos de Python relacionados
- Módulos estándar `os` (`os.getloadavg`, `os.statvfs` en Unix), `shutil` (`shutil.disk_usage`) o librería `psutil`.
- Módulo `time` para marcas de tiempo precisas.
- Persistencia relacional con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Convención de códigos de salida estilo Nagios/Icinga/Prometheus (0=OK, 1=WARNING, 2=CRITICAL).
- Herramientas de telemetría de bajo consumo de recursos.

### Herramientas o módulos para investigar
- `shutil.disk_usage` y `os`.
- `psutil` (si está disponible) o lectura de `/proc`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `top-processes --sort memory --limit 5` para identificar los procesos que consumen más recursos cuando se dispara una alerta?

### Diseño de argumentos
¿Cómo nombrarías la opción para enviar una notificación webhook ante alertas CRITICAL (`--notify-webhook <URL>`)?

### Diseño de variables
`cpu_metrics_dict`, `memory_metrics_dict`, `disk_metrics_map`, `active_alert_events_list`, `overall_health_status`.

### Antes de programar
1. ¿Cómo calcular el porcentaje de uso de memoria RAM a partir de los bytes totales y disponibles?
2. ¿Cómo diseñar el evaluador de reglas para procesar expresiones como `{"metric": "disk_usage_percent", "operator": ">=", "threshold": 90.0, "severity": "CRITICAL"}`?

### Arquitectura
Recolector de métricas (`collector.py`), evaluador de reglas (`alert_evaluator.py`), repositorio de telemetría (`metrics_repo.py`) y CLI.

### Pruebas mínimas
1. Ejecutar `collect` y verificar que devuelva CPU, RAM y disco con valores numéricos válidos (0 a 100%).
2. Ejecutar `check` con una regla forzada de CPU > 0% y verificar que retorne exit code 1 (Warning) o 2 (Critical) según la severidad.

### Pruebas de error
1. Pasar un archivo de reglas con métricas inexistentes -> Exit code 2 con error descriptivo.

### Experiencia de usuario
Tabla clara con colores: Verde para OK, Amarillo para Warning, Rojo para Critical, y salida JSON pura con `--format json` para integraciones.

### Explicación posterior
Explica el estándar de estados de monitoreo en la industria y cómo los códigos de retorno 0/1/2 permiten la integración nativa con orquestadores y sistemas de alerta.

### Aplicación profesional
Health checks para balanceadores de carga, scripts de monitoreo periódicos en cron y agentes de telemetría livianos.

### Reto adicional
Implementar cálculo de tendencia (rate of change) para alertar si el espacio en disco se está llenando a una velocidad anormal en la última hora.

---
> [← Ejercicio 052](../ejercicio_052/README.md) · [Índice General](../README.md) · [Ejercicio 054 →](../ejercicio_054/README.md)
