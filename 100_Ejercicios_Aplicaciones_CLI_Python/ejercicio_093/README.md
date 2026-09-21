## Ejercicio 093 — Sincronizador y Traductor de Esquemas Políglotas PostgreSQL ↔ SQLite (`polyglot-schema`)

> [← Ejercicio 092](../ejercicio_092/README.md) · [Índice General](../README.md) · [Ejercicio 094 →](../ejercicio_094/README.md)

### Contexto profesional
En arquitecturas híbridas donde los desarrolladores trabajan localmente con bases de datos embebidas SQLite (para velocidad y pruebas aisladas) pero despliegan en producción sobre clústeres empresariales de PostgreSQL, mantener la paridad exacta entre ambos dialectos SQL (traducción de tipos de datos, restricciones de clave foránea, triggers, índices y dialectos DDL) evita inconsistencias y bugs de producción.

### Problema
Construir una CLI que traduzca y sincronice esquemas de base de datos de forma bidireccional entre PostgreSQL y SQLite, mapeando tipos de datos equivalentes (`SERIAL` <-> `INTEGER PRIMARY KEY AUTOINCREMENT`, `JSONB` <-> `TEXT`, `TIMESTAMPTZ` <-> `DATETIME`, `BOOLEAN` <-> `INTEGER`), adaptando restricciones sintácticas, validando paridad de datos y ejecutando migraciones cruzadas entre ambos motores.

### Usuario objetivo
DBAs, desarrolladores backend y arquitectos de datos.

### Objetivo
Desarrollar un traductor y sincronizador de esquemas DDL políglotas entre PostgreSQL y SQLite con transpilación de tipos y verificación de paridad.

### Ejemplo conceptual de uso
```bash
# Traducir un esquema DDL de PostgreSQL hacia sintaxis de SQLite
python polyglot_schema.py translate schema_pg.sql --from postgresql --to sqlite -o schema_sqlite.sql

# Sincronizar estructura directamente de una BD PostgreSQL a un archivo SQLite local
python polyglot_schema.py sync --src-url "postgresql://user:pass@localhost:5432/app_db" --dest-sqlite "./local_dev.db"
```

### Requisitos funcionales
- Subcomando `translate <ARCHIVO_SQL>`: lee un script DDL y transpila todas las sentencias `CREATE TABLE`, `CREATE INDEX`, `ALTER TABLE` entre los dialectos seleccionados (`postgresql` <-> `sqlite`):
  - Mapeo de tipos PostgreSQL -> SQLite:
    - `SERIAL / BIGSERIAL` -> `INTEGER PRIMARY KEY AUTOINCREMENT`
    - `VARCHAR(N) / TEXT` -> `TEXT`
    - `JSON / JSONB` -> `TEXT` (con check de JSON válido opcional)
    - `UUID` -> `TEXT`
    - `BOOLEAN` -> `INTEGER` (con check `IN (0, 1)`)
    - `TIMESTAMP WITH TIME ZONE` -> `DATETIME` o `TEXT`
  - Mapeo de tipos SQLite -> PostgreSQL:
    - `INTEGER PRIMARY KEY AUTOINCREMENT` -> `SERIAL PRIMARY KEY`
    - `TEXT` con nombres tipo `*_json` -> `JSONB`
    - `INTEGER` con nombres tipo `is_*` -> `BOOLEAN`
- Subcomando `sync`: conecta directamente a una base de datos PostgreSQL de origen, extrae el esquema desde `information_schema` y lo aplica en una base de datos SQLite de destino (o viceversa).
- Subcomando `validate-parity`: comprueba que dos bases de datos (una en PostgreSQL y otra en SQLite) tengan exactamente las mismas tablas, columnas y tipos de datos conceptualmente equivalentes.

### Requisitos de CLI
- Subcomandos: `translate`, `sync`, `validate-parity`.
- Opción `--from [postgresql|sqlite]`.
- Opción `--to [postgresql|sqlite]`.
- Opciones de conexión: `--src-url`, `--dest-url`, `--src-sqlite`, `--dest-sqlite`.
- Opción `-o / --output <RUTA>`.
- Exit code 0 en éxito (o paridad perfecta), 1 si hay discrepancias de esquema en `validate-parity`, 2 en errores.

### Entradas
- Archivos DDL o conexiones activas a bases de datos PostgreSQL y SQLite.

### Salidas
- Script SQL traducido en STDOUT o base de datos sincronizada.

### Persistencia
Escritura de archivos SQL o modificación de bases de datos relacionales PostgreSQL / SQLite.

### Validaciones
- Comprobar que los dialectos de origen y destino sean diferentes.
- Validar que las conexiones a ambas bases de datos sean exitosas antes de iniciar `sync`.

### Casos límite
- Tablas con claves compuestas o restricciones `CHECK` complejas.
- Tipos de datos personalizados (Enums `CREATE TYPE ... AS ENUM` en PostgreSQL -> mapear a restricciones `CHECK` en SQLite).
- Nombres de columnas que son palabras reservadas en uno de los dos dialectos.

### Manejo de errores
- Errores de parsing de sintaxis DDL.
- `psycopg.Error` y `sqlite3.Error`.

### Fundamentos de Python relacionados
- Tokenización y parsing de sintaxis SQL con expresiones regulares o AST SQL.
- Mapeo de diccionarios de tipos de datos políglotas.
- Conexión y consulta de metadatos de esquema (`information_schema` en PostgreSQL / `PRAGMA table_info` en SQLite).
- Subparsers de `argparse`.

### Conceptos CLI relacionados
- Transpilación y traducción de dialectos de bases de datos en terminal.
- Gestión de paridad de esquemas en entornos híbridos de desarrollo/producción.

### Herramientas o módulos para investigar
- `psycopg`.
- `sqlite3`.
- `re`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para migrar también los datos de las filas además de la estructura DDL (`--include-data`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para generar comentarios explicativos en el SQL generado sobre las decisiones de traducción de tipos (`--annotate-types`)?

### Diseño de variables
`source_ddl_statements_list`, `translated_ddl_buffer`, `type_mapping_rules_matrix`, `schema_parity_differences_list`, `db_connection_instances`.

### Antes de programar
1. ¿Cómo consultar los metadatos de columnas en PostgreSQL (`SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = ...`) vs SQLite (`PRAGMA table_info('table_name')`)?
2. ¿Cómo traducir un enum de PostgreSQL `CREATE TYPE user_role AS ENUM ('admin', 'user')` a una columna SQLite `role TEXT CHECK(role IN ('admin', 'user'))`?

### Arquitectura
Parser DDL (`ddl_lexer.py`), motor de transpilación (`transpiler.py`), extractor de esquemas en vivo (`live_inspector.py`), validador de paridad (`parity_checker.py`) y CLI.

### Pruebas mínimas
1. Traducir un DDL de PostgreSQL con tipos `SERIAL`, `JSONB` y `BOOLEAN` hacia SQLite y verificar que el archivo generado sea ejecutable sin errores en SQLite.
2. Ejecutar `validate-parity` entre una base PostgreSQL y una SQLite con el esquema traducido y verificar que retorne 100% de paridad.

### Pruebas de error
1. Pasar un dialecto no soportado -> Exit code 2 con lista de dialectos válidos.

### Experiencia de usuario
Resumen de transpilación claro: `[✓] Tabla 'users' traducida: SERIAL -> INTEGER PRIMARY KEY, JSONB -> TEXT, BOOLEAN -> INTEGER`.

### Explicación posterior
Explica los trade-offs de diseño entre motores de base de datos embebidos sin tipado estricto (Type Affinity de SQLite) y motores cliente-servidor con tipado rígido (PostgreSQL).

### Aplicación profesional
Preparación de entornos de desarrollo local y testing ligero, herramientas de migración entre proveedores y compatibilidad multi-base de datos.

### Reto adicional
Implementar transpilación automática de funciones almacenadas y triggers sencillos entre PL/pgSQL y triggers de SQLite.

---
> [← Ejercicio 092](../ejercicio_092/README.md) · [Índice General](../README.md) · [Ejercicio 094 →](../ejercicio_094/README.md)
