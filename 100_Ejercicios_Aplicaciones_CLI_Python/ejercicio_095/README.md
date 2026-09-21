## Ejercicio 095 — Inyector de Fallas para Pruebas de Chaos Engineering (`chaos-cli`)

> [← Ejercicio 094](../ejercicio_094/README.md) · [Índice General](../README.md) · [Ejercicio 096 →](../ejercicio_096/README.md)

### Contexto profesional
Para verificar que una arquitectura de microservicios sea verdaderamente resiliente ante desastres en producción (principios de Chaos Engineering / Chaos Monkey), los ingenieros de confiabilidad inyectan fallas controladas de forma programada (latencia artificial en red, saturación de CPU, consumo extremo de RAM, caída forzada de procesos secundarios, descarte de conexiones de base de datos) para comprobar que los sistemas degraden elegantemente sin colapsar.

### Problema
Construir una CLI de inyección de fallas de Chaos Engineering que permita ejecutar experimentos controlados con duración delimitada (`--duration`), inyectando estrés de CPU/memoria, introduciendo latencia o pérdida de paquetes en conexiones locales, enviando señales de terminación a procesos específicos y abortando inmediatamente ante una condición de parada de emergencia (Safety Abort Switch).

### Usuario objetivo
Ingenieros de Chaos Engineering, SREs y arquitectos de resiliencia.

### Objetivo
Crear un inyector de fallas y experimentos de caos con temporización segura, parada de emergencia automática y registro de auditoría en base de datos.

### Ejemplo conceptual de uso
```bash
# Inyectar 80% de carga de CPU en 4 núcleos durante 30 segundos
python chaos_cli.py inject cpu --load 80 --cores 4 --duration 30s

# Inyectar latencia de 200ms en el puerto 5432 de PostgreSQL
python chaos_cli.py inject latency --port 5432 --delay 200ms --duration 1m

# Abortar inmediatamente todos los experimentos de caos activos (Kill Switch)
python chaos_cli.py kill-switch
```

### Requisitos funcionales
- Subcomando `inject cpu`: genera carga de procesamiento en N núcleos mediante bucles de cálculo calibrados con pausas activas para alcanzar exactamente el porcentaje de utilización deseado (`--load`).
- Subcomando `inject memory`: asigna y llena un bloque de memoria RAM de N megabytes/gigabytes durante el tiempo estipulado y lo libera limpiamente al finalizar.
- Subcomando `inject process-kill`: envía señales `SIGTERM` o `SIGKILL` a procesos que coincidan con un nombre o patrón de forma aleatoria.
- Subcomando `inject latency`: introduce un retardo artificial interponiendo un proxy TCP local que añade `--delay` a todas las conexiones hacia un puerto de destino (ej. PostgreSQL).
- Parámetro de seguridad obligatorio `--duration <TIEMPO>` (ej. `30s`, `2m`): garantiza que el experimento finalice automáticamente sin dejar el servidor estresado indefinidamente.
- Subcomando `kill-switch`: botón de parada de emergencia que cancela inmediatamente todos los experimentos y libera recursos.
- Registro de auditoría de experimentos en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `inject`, `kill-switch`, `history`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--duration <TIEMPO>` (default `10s`).
- Flag `--force` para saltarse confirmaciones de seguridad.
- Exit code 0 en experimento completado exitosamente, 1 si se activó el kill switch de emergencia, 2 en errores.

### Entradas
- Parámetros de experimento de caos, límites de recursos y credenciales de BD.

### Salidas
- Resumen del experimento, telemetría de estrés y confirmaciones en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `chaos_experiments`, `chaos_metrics` y `safety_events`.

### Validaciones
- Exigir confirmación interactiva explícita antes de iniciar cualquier experimento destructivo.
- La duración máxima de un experimento no puede superar un límite de seguridad configurable (ej. máximo 10 minutos).

### Casos límite
- Interrupción del proceso de la CLI con `Ctrl+C` (el manejador de señales debe limpiar inmediatamente la memoria asignada y detener los procesos hijos de estrés antes de salir).
- Servidores con pocos recursos (evitar provocar congelamiento total del kernel del sistema operativo).
- Experimentos concurrentes simultáneos.

### Manejo de errores
- `MemoryError` si la memoria solicitada no puede asignarse.
- `PermissionError` al enviar señales a procesos de otros usuarios.

### Fundamentos de Python relacionados
- Multiprocesamiento con `multiprocessing.Process` para distribución de carga de CPU.
- Gestión de señales POSIX con módulo `signal`.
- Manipulación de arrays de bytes en memoria con `bytearray` para consumo de RAM.
- Proxy TCP con módulo `socket` y `threading` para inyección de latencia.
- Persistencia de auditoría en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Principios de Chaos Engineering y pruebas de resiliencia en sistemas de producción.
- Implementación rigurosa de mecanismos de seguridad (Blast Radius Control & Emergency Kill Switch).

### Herramientas o módulos para investigar
- `multiprocessing`.
- `signal`.
- `socket` y `threading`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para abortar automáticamente el experimento de caos si el health check del servicio principal falla durante más de 5 segundos (`--abort-on-failure http://localhost:8080/health`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para registrar la hipótesis del experimento antes de ejecutar (ej. `--hypothesis "El servicio degrada a caché sin caer"`)?

### Diseño de variables
`chaos_experiment_id`, `target_fault_type`, `stress_worker_processes_list`, `experiment_duration_timer`, `safety_abort_triggered_flag`.

### Antes de programar
1. ¿Cómo calibrar un proceso de estrés de CPU para que consuma exactamente el 80% de un núcleo alternando entre un bucle de cálculo activo durante 80ms y `time.sleep(0.02)` durante 20ms en cada ciclo de 100ms?
2. ¿Cómo capturar `SIGINT` y `SIGTERM` para garantizar que todos los procesos hijos de estrés sean terminados con `process.terminate()` y no queden corriendo como procesos huérfanos?

### Arquitectura
Orquestador de caos (`chaos_orchestrator.py`), inyector de CPU (`cpu_stresser.py`), inyector de memoria (`memory_stresser.py`), proxy de latencia (`latency_proxy.py`), guardián de seguridad (`safety_guard.py`) y CLI.

### Pruebas mínimas
1. Inyectar estrés de memoria de 100 MB durante 3 segundos y verificar que la memoria se asigne, se mantenga y se libere limpiamente al finalizar el tiempo.
2. Probar el `kill-switch` y verificar que detenga cualquier experimento en curso de forma inmediata.

### Pruebas de error
1. Intentar inyectar una duración inválida `invalido` -> Exit code 2 con error de formato.

### Experiencia de usuario
Cuenta regresiva visual en terminal: `[CAOS ACTIVO: CPU STRESS 80%] Tiempo restante: 18s/30s | [Ctrl+C] Parada de Emergencia`.

### Explicación posterior
Explica la filosofía de Chaos Engineering: *'Encontrar debilidades antes de que se manifiesten como incidentes en producción'*, y la regla fundamental de contar siempre con un Kill Switch.

### Aplicación profesional
GameDays de resiliencia en equipos de ingeniería, validación de políticas de auto-escalado en Kubernetes y pruebas de conmutación de bases de datos.

### Reto adicional
Implementar un inyector de fallas a nivel de llamadas de base de datos PostgreSQL simulando desconexiones aleatorias o timeouts en consultas específicas.

---
> [← Ejercicio 094](../ejercicio_094/README.md) · [Índice General](../README.md) · [Ejercicio 096 →](../ejercicio_096/README.md)
