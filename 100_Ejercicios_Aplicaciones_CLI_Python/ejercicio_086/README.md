## Ejercicio 086 — Orquestador de Migración de Objetos Multi-Cloud con Resume (`cloud-migrator`)

> [← Ejercicio 085](../ejercicio_085/README.md) · [Índice General](../README.md) · [Ejercicio 087 →](../ejercicio_087/README.md)

### Contexto profesional
Al migrar terabytes de datos entre proveedores de nube (ej. de AWS S3 a Google Cloud Storage o MinIO local), las transferencias masivas sufren cortes de red, caídas de sesión o límites de tasa. Se requiere un orquestador de migración concurrente capaz de pausar, reanudar desde el punto exacto de interrupción (Checkpointing), verificar sumas de integridad criptográfica y registrar telemetría en PostgreSQL.

### Problema
Construir una CLI que orqueste la transferencia concurrente de objetos entre dos almacenamientos (origen y destino), manteniendo un estado de checkpointing en base de datos relacional (PostgreSQL como motor principal, o SQLite opcional) para soportar `--resume`, verificando integridad por chunks con hashes SHA256 y generando reportes de rendimiento de transferencia.

### Usuario objetivo
Ingenieros cloud, arquitectos de datos y DevOps.

### Objetivo
Diseñar un sistema de migración de datos distribuido y resiliente con soporte de reanudación automática, verificación de integridad y control de concurrencia.

### Ejemplo conceptual de uso
```bash
# Iniciar migración concurrente con 16 workers y checkpointing en PostgreSQL
python cloud_migrator.py start --source s3://bucket-origen/ --dest gcs://bucket-destino/ --workers 16 --db-url "postgresql://user:pass@localhost:5432/migration_db"

# Reanudar una migración interrumpida desde el último checkpoint
python cloud_migrator.py resume --job-id "job_88a3f"

# Consultar estado de progreso y velocidad en MB/s
python cloud_migrator.py status --job-id "job_88a3f"
```

### Requisitos funcionales
- Subcomando `start`: inicializa un trabajo de migración (`job_id`), inventaría los objetos en origen, calcula el tamaño total y encola las transferencias.
- Subcomando `resume <JOB_ID>`: lee el estado de la base de datos, omite los objetos ya transferidos y validados exitosamente y reanuda la transferencia de los objetos pendientes o fallidos.
- Transferencia concurrente con workers configurables (`--workers N`).
- Verificación de integridad post-transferencia comparando hash SHA256/MD5 de origen y destino.
- Subcomando `status`: muestra progreso en tiempo real (% completado, objetos transferidos, gigabytes transferidos, velocidad actual en MB/s y tiempo estimado de finalización ETA).
- Subcomando `abort <JOB_ID>`: cancela el trabajo de forma segura.

### Requisitos de CLI
- Subcomandos: `start`, `resume`, `status`, `abort`, `report`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--workers <N>` (default 8).
- Opción `--chunk-size <SIZE>` (default `8M`).
- Exit code 0 en migración completada al 100%, 1 si hay objetos fallidos no recuperados, 2 en errores.

### Entradas
- URIs de almacenamiento de origen y destino, credenciales de BD y parámetros de concurrencia.

### Salidas
- Barras de progreso, estadísticas de ancho de banda y reportes de integridad en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `migration_jobs`, `migration_tasks` y `transfer_logs`.

### Validaciones
- Comprobar accesibilidad y permisos en origen y destino antes de iniciar.
- Validar que el `job_id` exista al hacer `resume`.

### Casos límite
- Objetos gigantescos de cientos de gigabytes (transferencia multipart por partes con checkpoint individual por parte).
- Interrupciones de red repetitivas (reintentos con backoff).
- Objetos en origen que se modifican mientras la migración está en curso.

### Manejo de errores
- `ConnectionError` y `TimeoutError`.
- Detección de hash mismatch con reintento automático.

### Fundamentos de Python relacionados
- Concurrencia con `concurrent.futures.ThreadPoolExecutor` o `asyncio`.
- Módulos `hashlib`, `time` y `threading`.
- Persistencia de estado transaccional en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Orquestación de flujos de larga duración con Checkpointing y Resume.
- Estimación de tiempos de finalización (ETA) y métricas de rendimiento en tiempo real.

### Herramientas o módulos para investigar
- `concurrent.futures`.
- `hashlib` y `threading`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para limitar el ancho de banda máximo de transferencia (`--rate-limit 50MBps`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para verificar únicamente la integridad de los datos sin transferir (`--verify-only`)?

### Diseño de variables
`migration_job_id`, `transfer_tasks_queue`, `completed_bytes_atomic_counter`, `active_worker_threads`, `transfer_speed_mbps`.

### Antes de programar
1. ¿Cómo estructurar la tabla `migration_tasks` para registrar el estado de cada archivo (`PENDING`, `IN_PROGRESS`, `COMPLETED`, `FAILED`) y permitir que múltiples workers reclamen tareas de forma concurrente sin colisiones usando transacciones?
2. ¿Cómo calcular la velocidad en MB/s promediando los bytes transferidos en los últimos 10 segundos?

### Arquitectura
Orquestador de migración (`migration_coordinator.py`), pool de workers (`transfer_worker.py`), repositorio de checkpoints (`checkpoint_repo.py`) y CLI.

### Pruebas mínimas
1. Iniciar migración de 50 archivos de prueba, interrumpir manualmente el proceso en el 50%, ejecutar `resume` y verificar que solo transfiera los 25 archivos restantes y complete al 100%.
2. Verificar que todos los hashes coincidan en destino.

### Pruebas de error
1. Intentar reanudar un `job_id` inexistente -> Exit code 2 con error claro.

### Experiencia de usuario
Barra de progreso visual en terminal con métricas en vivo: `[████████░░░░] 65.4% (327/500 archivos) | 45.2 MB/s | ETA: 4m 12s`.

### Explicación posterior
Explica la importancia del patrón Checkpointing en computación distribuida para tolerar fallos transitorios en operaciones de larga duración.

### Aplicación profesional
Migraciones de almacenamiento cloud masivas, respaldos entre centros de datos y replicación de datasets de Machine Learning.

### Reto adicional
Implementar transferencia por partes paralela (Multipart Upload) para archivos individuales mayores a 100 MB.

---
> [← Ejercicio 085](../ejercicio_085/README.md) · [Índice General](../README.md) · [Ejercicio 087 →](../ejercicio_087/README.md)
