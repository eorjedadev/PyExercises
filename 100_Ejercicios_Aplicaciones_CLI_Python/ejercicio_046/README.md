## Ejercicio 046 — Gestor y Ejecutor de Migraciones SQL Versionadas (`migrator-cli`)

> [← Ejercicio 045](../ejercicio_045/README.md) · [Índice General](../README.md) · [Ejercicio 047 →](../ejercicio_047/README.md)

### Contexto profesional
En el desarrollo de software empresarial con bases de datos relacionales, el esquema de la base de datos debe evolucionar mediante archivos de migración versionados secuencialmente (`001_create_users.sql`, `002_add_email_index.sql`), registrando qué migraciones ya fueron aplicadas para no reejecutarlas y permitiendo revertir cambios (`rollback`) de forma controlada.

### Problema
Construir una CLI que gestione migraciones de base de datos para PostgreSQL (con SQLite como alternativa local opcional), manteniendo una tabla interna de control `schema_migrations`, ejecutando migraciones pendientes dentro de transacciones atómicas, soportando migraciones hacia adelante (`up`) y reversiones (`down`), y ofreciendo simulación (`--dry-run`).

### Usuario objetivo
Desarrolladores backend, DBAs y DevOps.

### Objetivo
Crear un motor de migraciones SQL versionadas con control de transacciones DDL, detección de estado y migraciones reversibles.

### Ejemplo conceptual de uso
```bash
# Crear un nuevo par de archivos de migración (up y down)
python migrator_cli.py new "create_tenants_table"

# Ver el estado de las migraciones (aplicadas vs pendientes)
python migrator_cli.py status

# Aplicar todas las migraciones pendientes en PostgreSQL
python migrator_cli.py up

# Revertir la última migración aplicada (rollback 1 paso)
python migrator_cli.py down --steps 1
```

### Requisitos funcionales
- Subcomando `init`: crea la tabla de control `schema_migrations` (`version VARCHAR PRIMARY KEY`, `name VARCHAR`, `applied_at TIMESTAMPTZ`, `checksum VARCHAR`).
- Subcomando `new <NOMBRE>`: genera dos archivos con timestamp secuencial en el directorio de migraciones: `YYYYMMDDHHMMSS_<nombre>.up.sql` y `YYYYMMDDHHMMSS_<nombre>.down.sql`.
- Subcomando `status`: lista todas las migraciones del directorio indicando si están aplicadas o pendientes.
- Subcomando `up`: lee las migraciones pendientes en orden cronológico, calcula su hash SHA256 para verificar integridad, ejecuta el script dentro de una transacción y registra la versión en `schema_migrations`.
- Subcomando `down`: ejecuta los scripts `.down.sql` correspondientes en orden inverso y elimina el registro de la tabla de control.
- Flag `--dry-run`: imprime el SQL que se ejecutaría sin aplicar cambios en la base de datos.

### Requisitos de CLI
- Subcomandos: `init`, `new`, `status`, `up`, `down`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--migrations-dir <RUTA>` (default `./migrations`).
- Opción `--steps <N>` en `up` y `down` (aplica/revierte exactamente N migraciones).
- Exit code 0 en éxito, 1 si una migración falla en su ejecución o hay corrupción de checksum, 2 en errores.

### Entradas
- Archivos SQL de migración y credenciales de base de datos.

### Salidas
- Reporte de estado de migraciones y confirmaciones de aplicación en STDOUT.

### Persistencia
Base de datos PostgreSQL o SQLite y sistema de archivos local para los scripts `.sql`.

### Validaciones
- Si una migración ya aplicada fue modificada en disco (su hash SHA256 actual difiere del registrado en BD), abortar inmediatamente informando alteración de historial.
- Ejecutar cada migración dentro de una transacción (`BEGIN ... COMMIT`) para que si falla una sentencia, no quede un esquema parcialmente aplicado.

### Casos límite
- Migraciones que contienen múltiples sentencias SQL separadas por punto y coma o bloques PL/pgSQL.
- Intentar hacer `down` cuando no hay ninguna migración aplicada.
- Dialectos SQL: en PostgreSQL las sentencias DDL son transaccionales (soportan rollback de `CREATE TABLE`), mientras que en otros motores no.

### Manejo de errores
- `psycopg.Error` / `sqlite3.Error` al ejecutar el SQL.
- Detección de checksum mismatch.

### Fundamentos de Python relacionados
- Manejo de transacciones explícitas con DB-API (`conn.rollback()`).
- Módulo `hashlib` para integridad de archivos de migración.
- `pathlib.Path` para ordenamiento cronológico de archivos.
- Subparsers de `argparse`.

### Conceptos CLI relacionados
- Diseño de herramientas de migración inspiradas en `Flyway`, `Liquibase` o `Alembic`.
- Garantía de idempotencia e inmutabilidad en evolución de esquemas.

### Herramientas o módulos para investigar
- `psycopg`.
- `sqlite3`.
- `hashlib` y `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `redo` que ejecuta un `down` seguido inmediatamente de un `up` para probar la reversibilidad de una migración?

### Diseño de argumentos
¿Cómo nombrarías la opción para forzar la sincronización del checksum si una migración fue editada intencionalmente (`--repair`)?

### Diseño de variables
`migration_files_list`, `applied_versions_set`, `pending_migrations_queue`, `migration_checksum_hash`, `active_db_transaction`.

### Antes de programar
1. ¿Por qué es fundamental calcular y almacenar el hash SHA256 de cada archivo `.up.sql` en la tabla de control de la base de datos?
2. ¿Cómo separar correctamente las sentencias SQL dentro de un archivo de migración sin romper bloques que contienen funciones o triggers?

### Arquitectura
Estructura:
```
ejercicio_046/
├── migrator_cli.py
├── migration_file_manager.py
├── migration_runner.py
├── db_adapters/
│   ├── postgres_adapter.py
│   └── sqlite_adapter.py
└── migrations/
    ├── 20260615100000_create_users.up.sql
    └── 20260615100000_create_users.down.sql
```

### Pruebas mínimas
1. Crear 2 migraciones de prueba, ejecutar `up`, verificar que las tablas se creen físicamente y que `status` muestre ambas como `APPLIED`.
2. Ejecutar `down --steps 1` y verificar que la última tabla sea eliminada y su estado vuelva a `PENDING`.

### Pruebas de error
1. Alterar 1 carácter en un archivo `.up.sql` ya aplicado y ejecutar `status` -> Exit code 1 alertando de discrepancia de checksum.

### Experiencia de usuario
Tabla de estado clara: `[APLICADA] 20260615100000_create_users.sql (2026-06-15 10:05:22)` y `[PENDIENTE] 20260615110000_add_roles.sql`.

### Explicación posterior
Explica la diferencia entre DDL transaccional (soportado por PostgreSQL) y no transaccional (como MySQL), y por qué el fallo de una migración en motores no transaccionales requiere intervención manual.

### Aplicación profesional
Herramienta central de integración continua para despliegue de esquemas de base de datos en entornos de staging y producción.

### Reto adicional
Implementar soporte para scripts de migración basados en funciones nativas de Python (`.py`) además de archivos SQL puros.

---
> [← Ejercicio 045](../ejercicio_045/README.md) · [Índice General](../README.md) · [Ejercicio 047 →](../ejercicio_047/README.md)
