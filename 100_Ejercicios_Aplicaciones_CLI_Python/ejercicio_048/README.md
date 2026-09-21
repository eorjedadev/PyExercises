## Ejercicio 048 — Motor de Rotación, Compresión y Retención de Logs (`log-rotator`)

> [← Ejercicio 047](../ejercicio_047/README.md) · [Índice General](../README.md) · [Ejercicio 049 →](../ejercicio_049/README.md)

### Contexto profesional
En servidores web (Nginx, Apache) y aplicaciones empresariales que generan gigabytes de logs diarios, los archivos de registro deben rotarse periódicamente (renombrarse secuencialmente), comprimirse con Gzip para ahorrar hasta un 90% de espacio en disco y eliminarse tras superar una política de retención (ej. conservar últimos 30 días).

### Problema
Construir una CLI que actúe como motor de rotación de logs (similar a `logrotate` de Linux), leyendo reglas desde un archivo de configuración JSON/YAML, evaluando criterios de rotación (por tamaño máximo o por antigüedad en días), comprimiendo logs antiguos, enviando señales de reapertura (`SIGHUP`) a procesos de aplicación y registrando auditoría en base de datos o archivo.

### Usuario objetivo
Administradores de sistemas Linux, operadores de infraestructura y SREs.

### Objetivo
Desarrollar una utilidad de mantenimiento y compresión de archivos de registro con soporte de políticas de retención y compresión en streaming.

### Ejemplo conceptual de uso
```bash
# Ejecutar rotación de logs según configuración
python log_rotator.py run --config /etc/log_rotator.json

# Simular rotación mostrando qué archivos se comprimirían o borrarían
python log_rotator.py run --config /etc/log_rotator.json --dry-run

# Forzar rotación inmediata ignorando umbrales de tamaño/tiempo
python log_rotator.py run --config /etc/log_rotator.json --force
```

### Requisitos funcionales
- Leer archivo de configuración con lista de reglas por directorio/archivo:
  - `max_size_mb`: rotar si el archivo supera N megabytes.
  - `rotate_interval`: `daily`, `weekly`, `monthly`.
  - `compress`: booleano (comprimir con Gzip `.gz`).
  - `retention_count`: número de copias históricas a conservar (ej. 7 copias).
  - `post_rotate_command`: comando opcional a ejecutar tras rotar.
- Rotación secuencial: renombrar `app.log` -> `app.log.1`, `app.log.1` -> `app.log.2`, etc.
- Compresión en segundo plano usando streaming con módulo `gzip`.
- Eliminación automática de archivos que excedan el límite de retención.
- Registrar métricas de espacio liberado y eventos de rotación en PostgreSQL o SQLite opcional.

### Requisitos de CLI
- Subcomando `run`.
- Opción `--config <RUTA>` (default `config.json`).
- Flag `--dry-run`.
- Flag `-f / --force`.
- Exit code 0 en éxito, 1 si alguna regla falló, 2 en errores de configuración.

### Entradas
- Archivo de configuración y archivos de log en disco.

### Salidas
- Resumen de operaciones de rotación y compresión en STDOUT.

### Persistencia
Renombrado, compresión y eliminación de archivos en el sistema de archivos; registro de auditoría en base de datos.

### Validaciones
- Comprobar que los directorios y archivos declarados en la configuración existan.
- Validar que el archivo de log principal no esté bloqueado.

### Casos límite
- Archivos de log muy grandes (varios gigabytes; comprimir en streaming sin cargar en RAM).
- Rotación de archivos de 0 bytes (no rotar a menos que se use `--force`).
- Renombrado seguro para evitar sobreescrituras si falta una copia intermedia.

### Manejo de errores
- `PermissionError` al mover o comprimir archivos protegidos.
- Manejo de fallos en el comando `post_rotate_command`.

### Fundamentos de Python relacionados
- Módulo estándar `gzip` (`gzip.open()`, `shutil.copyfileobj()`).
- `pathlib.Path` y `shutil.move`.
- Módulo `json` para configuración.
- Manejo de subprocesos con `subprocess.run` para comandos post-rotación.

### Conceptos CLI relacionados
- Gestión de almacenamiento y compresión en servidores.
- Implementación de políticas de ciclo de vida de datos (Data Lifecycle Policies).

### Herramientas o módulos para investigar
- `gzip` y `shutil`.
- `pathlib`.
- `json`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `status` para ver el tamaño actual de todos los logs monitoreados y cuándo les corresponde su próxima rotación?

### Diseño de argumentos
¿Cómo nombrarías la opción para especificar el nivel de compresión Gzip de 1 a 9 (`--compress-level 6`)?

### Diseño de variables
`rotation_config_rules`, `log_target_path`, `compressed_archive_path`, `rotation_history_queue`, `freed_disk_bytes`.

### Antes de programar
1. ¿Cómo rotar los archivos en orden inverso (`app.log.3` -> `app.log.4`, luego `app.log.2` -> `app.log.3`, etc.) para evitar sobrescribir el archivo más reciente?
2. ¿Cómo comprimir un archivo de 2 GB en un `.gz` usando `shutil.copyfileobj` en bloques de 64 KB sin consumir más de 10 MB de memoria RAM?

### Arquitectura
Lector de configuración (`config_loader.py`), motor de rotación (`rotator_core.py`), compresor (`compressor.py`) y CLI.

### Pruebas mínimas
1. Crear un log de prueba de 2 MB con regla de rotación en 1 MB, ejecutar y verificar que se genere `log.1.gz`, el log original se vacíe o recree, y el archivo comprimido sea menor.
2. Probar `--dry-run` y verificar que ningún archivo sea modificado.

### Pruebas de error
1. Pasar un archivo de configuración con JSON corrupto -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Reporte claro en terminal con tabla de archivos rotados, porcentaje de compresión logrado y MB liberados.

### Explicación posterior
Explica la técnica de rotación *copytruncate* vs *create/move* y por qué ciertos procesos requieren una señal `SIGHUP` para reabrir el descriptor de archivo.

### Aplicación profesional
Mantenimiento automatizado de logs en servidores web, bases de datos y nodos de clústeres Kubernetes.

### Reto adicional
Implementar soporte para mover automáticamente los logs comprimidos antiguos a un almacenamiento secundario o bucket S3 simulado.

---
> [← Ejercicio 047](../ejercicio_047/README.md) · [Índice General](../README.md) · [Ejercicio 049 →](../ejercicio_049/README.md)
