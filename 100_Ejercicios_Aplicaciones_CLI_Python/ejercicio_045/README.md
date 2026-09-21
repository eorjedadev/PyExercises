## Ejercicio 045 — Agente de Monitoreo de Uptime y Latencia de Servicios (`uptime-agent`)

> [← Ejercicio 044](../ejercicio_044/README.md) · [Índice General](../README.md) · [Ejercicio 046 →](../ejercicio_046/README.md)

### Contexto profesional
En infraestructuras de servidores distribuidos, se instalan agentes ligeros de monitoreo en segundo plano o mediante tareas programadas (cron) que verifican la salud de bases de datos, APIs y servidores web, persistiendo cada muestra en una base de datos centralizada para auditar SLAs (Service Level Agreements).

### Problema
Construir una CLI que actúe como agente de sondeo de disponibilidad, lea una lista de servicios a monitorear desde un archivo de configuración, realice pruebas de conexión (HTTP, TCP, DNS), registre las métricas de latencia y código de estado en PostgreSQL (o SQLite opcional), aplique rotación de logs de aplicación y genere reportes de SLA.

### Usuario objetivo
Ingenieros de SRE, DevOps y administradores de sistemas.

### Objetivo
Desarrollar un agente de recolección de métricas de red con persistencia relacional, registro estructurado mediante módulo `logging` y cálculo de SLAs.

### Ejemplo conceptual de uso
```bash
# Ejecutar una ronda de sondeo de todos los servicios configurados
python uptime_agent.py poll --config monitors.json

# Ver reporte de SLA y porcentaje de uptime de los últimos 30 días
python uptime_agent.py report --service "Payment Gateway" --period 30d
```

### Requisitos funcionales
- Subcomando `poll`: lee los monitores configurados (tipo HTTP, TCP o DNS), ejecuta las sondas con timeout estricto, mide latencia precisa y persiste la muestra (`timestamp`, `service_id`, `status`, `latency_ms`, `error_message`) en base de datos.
- Subcomando `report`: calcula porcentaje de disponibilidad (SLA %: $\frac{\text{muestras exitosas}}{\text{total muestras}} \times 100$), tiempo medio entre fallos (MTBF) y percentiles de latencia p50, p95 y p99.
- Subcomando `add-target`: registra un nuevo servicio a monitorear en la configuración o base de datos.
- Implementación de logging jerárquico con el módulo estándar `logging` hacia archivo y terminal, con niveles `DEBUG`, `INFO`, `WARNING`, `ERROR`.
- Modo silencioso `--quiet` para ejecución en cron desatendido.

### Requisitos de CLI
- Subcomandos: `poll`, `report`, `add-target`, `list-targets`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--log-level [debug|info|warning|error]`.
- Flag `--quiet / -q`.
- Exit code 0 en éxito, 1 si algún servicio crítico está caído durante `poll`, 2 en errores de configuración.

### Entradas
- Archivo de configuración de monitores y credenciales de BD.

### Salidas
- Reportes tabulares en STDOUT y trazas de auditoría en archivo de log (`uptime_agent.log`).

### Persistencia
PostgreSQL (con particionado mensual o índices por timestamp) o SQLite opcional para almacenar millones de muestras históricas.

### Validaciones
- Los timeouts deben ser enteros positivos en segundos.
- Validar formato de URL, hostname y puertos en los monitores configurados.

### Casos límite
- Monitoreo de servicios que devuelven timeouts o errores DNS.
- Caída temporal de la base de datos de métricas (el agente debe guardar las muestras localmente en un buffer de archivo y reintentar la inserción en la siguiente ronda).

### Manejo de errores
- Errores de socket y HTTP (`urllib.error.URLError`, `ConnectionResetError`).
- Errores de base de datos.

### Fundamentos de Python relacionados
- Módulo estándar `logging` (`logging.getLogger`, `RotatingFileHandler`, `StreamHandler`, formateadores estructurados).
- Módulo `socket` para comprobaciones de puertos TCP.
- Cálculo estadístico de percentiles (p50, p95, p99) con módulo `statistics` o consultas SQL.

### Conceptos CLI relacionados
- Configuración de logging profesional en herramientas CLI.
- Ejecución desatendida mediante cron y persistencia de series temporales.

### Herramientas o módulos para investigar
- `logging` y `logging.handlers`.
- `statistics`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `daemon --interval 60` para ejecutar el sondeo en bucle continuo?

### Diseño de argumentos
¿Cómo nombrarías la opción para enviar una alerta webhook si un servicio acumula N fallos consecutivos (`--alert-webhook <URL> --threshold 3`)?

### Diseño de variables
`probe_target`, `latency_performance_timer`, `uptime_log_record`, `sla_availability_percentage`, `p95_latency_metric`.

### Antes de programar
1. ¿Por qué el percentil 95 (p95) y p99 son métricas de latencia mucho más representativas que el promedio simple en sistemas de producción?
2. ¿Cómo configurar `logging` para que los mensajes `INFO` vayan a un archivo rotativo y los errores críticos aparezcan en `STDERR`?

### Arquitectura
Motor de sondeo (`prober.py`), evaluador de métricas (`sla_engine.py`), repositorio de telemetría (`metrics_repo.py`) y CLI.

### Pruebas mínimas
1. Ejecutar una ronda de `poll` sobre 2 endpoints de prueba (uno disponible y otro cerrado) y verificar que ambas muestras se registren en la base de datos con sus respectivos estados `UP` y `DOWN`.
2. Ejecutar `report` y verificar el cálculo del porcentaje de SLA.

### Pruebas de error
1. Ejecutar con archivo de configuración inexistente -> Exit code 2 con mensaje claro en el log.

### Experiencia de usuario
Salida limpia en STDOUT cuando se consulta interactivamente, y ejecución completamente silenciosa con `--quiet` apta para cron.

### Explicación posterior
Explica la diferencia entre los cuatro nueves de disponibilidad (99.99% SLA = ~4.3 minutos de inactividad al mes) y tres nueves (99.9% = ~43 minutos).

### Aplicación profesional
Monitoreo sintético de infraestructura, observabilidad de microservicios y generación de reportes de cumplimiento de SLA.

### Reto adicional
Implementar un buffer local en disco (offline queue) que almacene las métricas si la base de datos PostgreSQL está inaccesible y las envíe automáticamente cuando se restablezca la conexión.

---
> [← Ejercicio 044](../ejercicio_044/README.md) · [Índice General](../README.md) · [Ejercicio 046 →](../ejercicio_046/README.md)
