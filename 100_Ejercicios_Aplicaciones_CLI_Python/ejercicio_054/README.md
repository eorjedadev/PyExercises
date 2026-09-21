## Ejercicio 054 — Orquestador de Backups y Dumps de Bases de Datos (`db-dump-orchestrator`)

> [← Ejercicio 053](../ejercicio_053/README.md) · [Índice General](../README.md) · [Ejercicio 055 →](../ejercicio_055/README.md)

### Contexto profesional
En la gestión de infraestructura empresarial, los respaldos de bases de datos deben realizarse de forma automatizada y periódica, invocando las utilidades nativas de volcado (`pg_dump` para PostgreSQL o comandos de copia/backup para SQLite), comprimiendo los volcados resultantes con compresión de alto ratio, calculando hashes de integridad y aplicando políticas de retención para eliminar copias antiguas.

### Problema
Construir una CLI que orqueste la ejecución de respaldos de bases de datos PostgreSQL (y SQLite opcional), gestione el proceso de volcado, aplique compresión (`gzip`/`zstandard`), genere un manifiesto de integridad con SHA256, aplique rotación de backups antiguos según antigüedad o cantidad máxima y registre el resultado en una tabla de auditoría.

### Usuario objetivo
Administradores de bases de datos (DBA), ingenieros de DevOps y sysadmins.

### Objetivo
Crear un orquestador de respaldos de bases de datos con integración de utilidades nativas, compresión, verificación de integridad y políticas de retención.

### Ejemplo conceptual de uso
```bash
# Ejecutar backup de base de datos PostgreSQL con compresión
python db_dump_orchestrator.py backup --db-url "postgresql://user:pass@localhost:5432/app_db" --out-dir ./backups --compress gzip

# Listar backups disponibles y verificar integridad de los archivos
python db_dump_orchestrator.py verify ./backups/app_db_20260615_120000.sql.gz

# Aplicar política de retención eliminando backups con más de 30 días
python db_dump_orchestrator.py prune ./backups --keep-days 30
```

### Requisitos funcionales
- Subcomando `backup`: invoca `pg_dump` con parámetros seguros (o realiza backup en caliente de SQLite con `sqlite3.Connection.backup()`), canaliza la salida hacia el compresor (`gzip`) en tiempo real sin crear archivos temporales gigantes sin comprimir, calcula el hash SHA256 del archivo final y guarda un manifiesto JSON con metadatos.
- Subcomando `verify <ARCHIVO>`: descomprime en memoria y valida la integridad del archivo y su hash contra el manifiesto.
- Subcomando `list <DIR>`: lista todos los backups en el directorio con tamaño comprimido, tamaño original estimado, fecha y estado de integridad.
- Subcomando `prune <DIR>`: elimina backups que superen el límite de antigüedad (`--keep-days`) o el número máximo de copias (`--keep-count`), respetando un mínimo de seguridad.
- Subcomando `restore <ARCHIVO>` (con confirmación obligatoria): restaura el volcado en la base de datos objetivo.

### Requisitos de CLI
- Subcomandos: `backup`, `verify`, `list`, `prune`, `restore`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--compress [gzip|none]` (default `gzip`).
- Flag `--force` para evitar confirmaciones interactivas en scripts.
- Exit code 0 en éxito, 1 en fallo de volcado o verificación, 2 en errores.

### Entradas
- Parámetros de base de datos y directorios de almacenamiento de backups.

### Salidas
- Resumen de backup generado, tamaño comprimido y tiempo transcurrido en STDOUT.

### Persistencia
Creación y mantenimiento de archivos `.sql.gz` y `.manifest.json` en disco.

### Validaciones
- Verificar que la utilidad `pg_dump` esté instalada en el sistema si se utiliza PostgreSQL.
- Comprobar que haya suficiente espacio libre en disco en el directorio de destino antes de iniciar el volcado.

### Casos límite
- Bases de datos de gran tamaño (decenas de gigabytes; streaming continuo hacia el compresor).
- Fallo de red a mitad del proceso (limpiar el archivo parcial corrupto automáticamente).
- Restauración sobre una base de datos con conexiones activas.

### Manejo de errores
- `subprocess.CalledProcessError` al invocar `pg_dump`.
- Errores de espacio insuficiente en disco.

### Fundamentos de Python relacionados
- Invocación de procesos externos con `subprocess.Popen` y encadenamiento de pipes de compresión.
- Módulo `hashlib` para verificación de sumas criptográficas.
- Módulo `gzip` y manipulación de archivos con `pathlib`.

### Conceptos CLI relacionados
- Orquestación segura de herramientas nativas del sistema operativo.
- Streaming de datos entre procesos para optimización de recursos.

### Herramientas o módulos para investigar
- `subprocess.Popen`.
- `gzip` y `shutil`.
- `hashlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `backup-all` para respaldar todas las bases de datos de un servidor PostgreSQL?

### Diseño de argumentos
¿Cómo nombrarías la opción para excluir tablas específicas con datos volátiles (ej. `--exclude-table "logs,sessions"`)?

### Diseño de variables
`database_dump_process`, `compressed_stream_writer`, `backup_manifest_metadata`, `sha256_checksum_calculator`, `retention_policy_rules`.

### Antes de programar
1. ¿Cómo conectar la salida `stdout` de `subprocess.Popen(['pg_dump', ...])` directamente al flujo de compresión sin escribir el archivo SQL sin comprimir en el disco primero?
2. ¿Cómo garantizar que si el comando `pg_dump` falla con error, el archivo `.gz` resultante sea eliminado y no quede registrado como un backup válido?

### Arquitectura
Orquestador de dumps (`dump_engine.py`), gestor de retención (`retention_manager.py`), verificador de integridad (`integrity_checker.py`) y CLI.

### Pruebas mínimas
1. Ejecutar backup de una base de datos PostgreSQL de prueba (o SQLite con `--driver sqlite`), verificar que se genere el archivo comprimido y el manifiesto `.json`.
2. Ejecutar `verify` y comprobar que valide el hash SHA256 exitosamente.

### Pruebas de error
1. Ejecutar backup con credenciales de base de datos inválidas -> Debe fallar limpiamente con exit code 1 y sin dejar archivos residuales.

### Experiencia de usuario
Progreso visual claro con tiempo transcurrido, ratio de compresión (ej. `45.2 MB -> 4.8 MB (89.4% ahorro)`) y hash SHA256.

### Explicación posterior
Explica la diferencia entre backups lógicos (`pg_dump` / SQL export) y backups físicos (copias de bloques de disco / WAL archiving) y sus respectivos casos de uso.

### Aplicación profesional
Automatización de backups diarios en servidores de producción y preparación de entornos de recuperación ante desastres (DRP).

### Reto adicional
Implementar cifrado simétrico opcional de los archivos de backup con AES-256 usando una clave provista mediante flag o variable de entorno (`--encrypt-key`).

---
> [← Ejercicio 053](../ejercicio_053/README.md) · [Índice General](../README.md) · [Ejercicio 055 →](../ejercicio_055/README.md)
