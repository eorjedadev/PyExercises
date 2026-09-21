## Ejercicio 079 — Simulador de Bloqueos Distribuidos Basado en Archivos y BD (`file-lock-cli`)

> [← Ejercicio 078](../ejercicio_078/README.md) · [Índice General](../README.md) · [Ejercicio 080 →](../ejercicio_080/README.md)

### Contexto profesional
En entornos de microservicios y tareas de cron ejecutadas en múltiples instancias concurrentes, se requiere garantizar que solo un proceso a la vez ejecute una tarea crítica (ej. procesamiento de facturas, sincronización de catálogo) mediante bloqueos distribuidos (Distributed Locks) con tiempo de expiración (Lease Time / TTL) y reintentos.

### Problema
Construir una CLI que gestione bloqueos distribuidos (Distributed Locks) utilizando dos mecanismos intercambiables: bloqueo a nivel de sistema de archivos (`fcntl` en Linux o `msvcrt` en Windows con archivos `.lock`) o bloqueo relacional en base de datos (PostgreSQL usando *Advisory Locks* o SQLite con tabla de leases), permitiendo adquirir un bloqueo, renovarlo, liberarlo o envolver un comando externo (`exec`) garantizando ejecución exclusiva.

### Usuario objetivo
Ingenieros de backend, arquitectos de sistemas distribuidos y DevOps.

### Objetivo
Implementar un gestor de bloqueos exclusivos y distribuidos con soporte para múltiples backends (File Lock vs PostgreSQL Advisory Locks), tiempo de arrendamiento (Lease TTL) y wrapper de procesos.

### Ejemplo conceptual de uso
```bash
# Envolver un script para ejecución exclusiva usando PostgreSQL Advisory Locks
python file_lock_cli.py exec "billing-sync" --db-url "postgresql://user:pass@localhost:5432/app_db" --timeout 10 -- ./run_billing.sh

# Adquirir un bloqueo basado en archivos con TTL de 60 segundos
python file_lock_cli.py acquire "nightly-backup" --backend file --ttl 60

# Liberar el bloqueo adquirido
python file_lock_cli.py release "nightly-backup" --backend file
```

### Requisitos funcionales
- Soporte de backends de bloqueo:
  - `backend file`: utiliza llamadas atómicas del sistema operativo (`fcntl.flock` en POSIX / `msvcrt.locking` en Windows) o archivos de lease con timestamp de expiración y PID del titular.
  - `backend postgres`: utiliza bloqueos de aplicación nativos de PostgreSQL (*PostgreSQL Advisory Locks* `pg_try_advisory_lock` / `pg_advisory_unlock`) o tabla de leases relacional.
  - `backend sqlite`: utiliza transacciones exclusivas de SQLite.
- Subcomando `acquire <LOCK_NAME>`: intenta adquirir el bloqueo exclusivo. Si está ocupado, reintenta con retroceso hasta agotar `--timeout`.
- Subcomando `release <LOCK_NAME>`: libera el bloqueo si el proceso actual es el titular legítimo.
- Subcomando `exec <LOCK_NAME> -- <COMANDO>`: adquiere el bloqueo, ejecuta el comando secundario mediante subproceso, espera su finalización, captura su exit code y libera el bloqueo de forma garantizada (incluso si el comando falla o se interrumpe).
- Subcomando `status <LOCK_NAME>`: informa si el bloqueo está activo, quién es el titular (PID / Host) y cuántos segundos le quedan de vigencia.

### Requisitos de CLI
- Subcomandos: `acquire`, `release`, `exec`, `status`.
- Opción `--backend [postgres|file|sqlite]` (default `file`).
- Opciones de conexión: `--db-url` o `--driver sqlite`.
- Opción `--timeout <SEG>` (tiempo máximo de espera para adquirir el lock, default 5.0).
- Opción `--ttl <SEG>` (duración máxima del lock para evitar deadlocks por caída de procesos, default 60).
- Exit code 0 en éxito (o el exit code del subproceso en `exec`), 1 si no se pudo adquirir el lock en el timeout, 2 en errores.

### Entradas
- Nombres de bloqueo, comandos secundarios a envolver y parámetros de tiempo.

### Salidas
- Mensajes de estado de bloqueo y salida del subproceso en STDOUT/STDERR.

### Persistencia
Archivos `.lock` en disco o registros/locks en base de datos PostgreSQL / SQLite.

### Validaciones
- El nombre del lock debe ser alfanumérico.
- Los timeouts y TTLs deben ser números positivos mayores a 0.

### Casos límite
- Proceso que adquiere un bloqueo y muere abruptamente (`SIGKILL` o caída de energía; el lock debe expirar automáticamente al vencer su TTL).
- Múltiples procesos concurrentes compitiendo exactamente en el mismo milisegundo por el lock.
- Cancelación del comando envuelto mediante `Ctrl+C` (asegurar liberación limpia del lock en el bloque `finally`).

### Manejo de errores
- `TimeoutError` cuando el lock no puede adquirirse en el tiempo máximo.
- Errores de base de datos o permisos de sistema de archivos.

### Fundamentos de Python relacionados
- Bloqueos de archivos a nivel de SO (`fcntl` en Unix / `msvcrt` en Windows / `tempfile`).
- Advisory Locks en PostgreSQL (`SELECT pg_try_advisory_lock(hashtext('nombre_lock'))`).
- Context Managers de Python (`__enter__`, `__exit__`) para garantizar liberación en bloques `finally`.
- Ejecución y streaming de subprocesos con `subprocess.Popen`.

### Conceptos CLI relacionados
- Patrón Wrapper de procesos (Process Wrapping / Mutex Guard).
- Prevención de condiciones de carrera (Race Conditions) y deadlocks en sistemas distribuidos.

### Herramientas o módulos para investigar
- `fcntl` / `msvcrt`.
- `psycopg`.
- `subprocess` y `time`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción de latido de corazón (Heartbeat / Keep-Alive) en segundo plano para renovar automáticamente el TTL del lock mientras el proceso largo sigue ejecutándose?

### Diseño de argumentos
¿Cómo nombrarías la opción para salir inmediatamente sin esperar si el lock está ocupado (`--non-blocking / -n`)?

### Diseño de variables
`lock_identifier_name`, `lock_backend_adapter`, `lease_expiration_timestamp`, `wrapped_subprocess_instance`, `lock_acquired_token`.

### Antes de programar
1. ¿Por qué el uso de Advisory Locks en PostgreSQL es superior a crear y borrar filas en una tabla regular (porque los advisory locks residen en la memoria compartida del motor y se liberan automáticamente si la conexión TCP se cierra)?
2. ¿Cómo diseñar el Context Manager `with DistributedLock('task_name', timeout=5):` para encapsular la adquisición y liberación garantizada?

### Arquitectura
Interfaz de lock (`base_lock.py`), backend de archivos (`file_lock.py`), backend PostgreSQL (`postgres_lock.py`), wrapper de ejecución (`process_runner.py`) y CLI.

### Pruebas mínimas
1. Adquirir un lock con `acquire` en un proceso, intentar adquirir el mismo lock en un segundo proceso con timeout de 1s y verificar que el segundo falle con exit code 1.
2. Liberar el lock en el primer proceso y verificar que el segundo proceso ahora sí pueda adquirirlo.
3. Ejecutar `exec` envolviendo `python -c "print('Hola')"` y verificar que emita la salida y libere el lock.

### Pruebas de error
1. Intentar liberar un lock no poseído por el usuario -> Exit code 1.

### Experiencia de usuario
Mensajes claros en STDERR indicando: `[Lock] Adquiriendo bloqueo 'nightly-backup'... OK`, `[Lock] Ejecutando comando envuelto...`, `[Lock] Bloqueo liberado limpiamente`.

### Explicación posterior
Explica la diferencia entre exclusión mutua pesimista (Locks / Mutex) y control de concurrencia optimista (Optimistic Concurrency Control / Version checks).

### Aplicación profesional
Garantía de ejecución única en tareas programadas de cron en flotas de servidores, prevención de doble facturación y sincronizaciones exclusivas.

### Reto adicional
Implementar un hilo daemon en segundo plano que extienda el tiempo de vida (Lease Renewal) del bloqueo cada $TTL/2$ segundos mientras el comando hijo continúe ejecutándose.

---
> [← Ejercicio 078](../ejercicio_078/README.md) · [Índice General](../README.md) · [Ejercicio 080 →](../ejercicio_080/README.md)
