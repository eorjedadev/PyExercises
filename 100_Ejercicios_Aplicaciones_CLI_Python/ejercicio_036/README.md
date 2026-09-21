## Ejercicio 036 — Comparador de Esquemas DDL de Bases de Datos (`schema-diff`)

> [← Ejercicio 035](../ejercicio_035/README.md) · [Índice General](../README.md) · [Ejercicio 037 →](../ejercicio_037/README.md)

### Contexto profesional
Durante el ciclo de desarrollo de software, los desarrolladores modifican esquemas de bases de datos relacionales en sus entornos locales. Antes de desplegar a producción, es vital comparar dos archivos de esquema DDL (SQL Data Definition Language) para detectar tablas faltantes, columnas añadidas/eliminadas o cambios en tipos de datos y restricciones.

### Problema
Construir una CLI que reciba dos archivos SQL con sentencias DDL `CREATE TABLE` (soportando sintaxis de PostgreSQL y SQLite), parsee la estructura de tablas, columnas, tipos de datos y llaves primarias, y genere un reporte de diferencias (diff) junto con un script SQL de migración tentativo.

### Usuario objetivo
Administradores de bases de datos (DBA), desarrolladores backend y DevOps.

### Objetivo
Crear un motor de comparación de esquemas relacionales DDL con generación de scripts de parche SQL (`ALTER TABLE`).

### Ejemplo conceptual de uso
```bash
# Comparar dos esquemas DDL de PostgreSQL
python schema_diff.py schema_v1.sql schema_v2.sql --dialect postgresql

# Generar el script SQL de migración hacia schema_v2
python schema_diff.py schema_v1.sql schema_v2.sql --generate-patch -o migration.sql
```

### Requisitos funcionales
- Parsear sentencias `CREATE TABLE` extrayendo: nombre de tabla, lista de columnas, tipo de dato de cada columna, nulabilidad (`NULL`/`NOT NULL`), valores por defecto (`DEFAULT`) y llaves primarias (`PRIMARY KEY`).
- Soportar dialectos: `postgresql` (con tipos como `SERIAL`, `VARCHAR`, `TIMESTAMPTZ`, `JSONB`, `UUID`) y `sqlite` (con `INTEGER PRIMARY KEY`, `TEXT`, `REAL`, `BLOB`).
- Comparar Esquema A (origen) vs Esquema B (destino) e identificar:
  - Tablas creadas o eliminadas.
  - Columnas añadidas o eliminadas dentro de tablas existentes.
  - Columnas cuyos tipos de datos o restricciones fueron modificados.
- Modo `--generate-patch`: genera las sentencias `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE ... ADD COLUMN`, `ALTER TABLE ... DROP COLUMN` correspondientes al dialecto seleccionado.

### Requisitos de CLI
- Argumentos posicionales: `schema_source.sql` y `schema_target.sql`.
- Opción `--dialect [postgresql|sqlite]` (default `postgresql`).
- Flag `--generate-patch`.
- Opción `-o / --output <FILE>`: guarda el script SQL generado.
- Exit code 0 si los esquemas son idénticos, 1 si existen diferencias estructurales, 2 en errores de sintaxis DDL.

### Entradas
- Dos archivos SQL DDL.
- Dialecto de base de datos.

### Salidas
- Reporte de diferencias en STDOUT o script SQL de migración.

### Persistencia
Escritura de archivo de migración si se usa `-o`.

### Validaciones
- Comprobar que ambos archivos existan y contengan sentencias `CREATE TABLE` válidas.
- Validar compatibilidad de dialectos.

### Casos límite
- Columnas con nombres entre comillas dobles o reservadas.
- Tipos de datos con modificadores de precisión (ej. `VARCHAR(255)`, `DECIMAL(10,2)`).
- Orden alterado de columnas en la definición de la tabla.

### Manejo de errores
- Errores de parsing de sintaxis DDL.
- Tipos de datos incompatibles o no soportados.

### Fundamentos de Python relacionados
- Expresiones regulares avanzadas o tokenizer básico de SQL.
- Comparación de estructuras de datos con diccionarios y conjuntos (`set` operations).
- Modelado de datos orientado a objetos (`TableSchema`, `ColumnSchema`).

### Conceptos CLI relacionados
- Herramientas de diffing semántico vs textual.
- Automatización de migraciones en bases de datos.

### Herramientas o módulos para investigar
- `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para ignorar el orden de las columnas o comentarios SQL en la comparación?

### Diseño de argumentos
¿Cómo nombrarías el flag para advertir sobre operaciones destructivas como `DROP TABLE` o `DROP COLUMN` (`--warn-destructive`)?

### Diseño de variables
`source_tables_map`, `target_tables_map`, `added_tables_set`, `dropped_tables_set`, `modified_columns_dict`, `patch_statements_list`.

### Antes de programar
1. ¿Por qué una comparación textual línea a línea (`diff` estándar) no sirve para SQL si las columnas están en orden distinto o tienen espacios en blanco diferentes?
2. ¿Cómo generar la sentencia `ALTER TABLE` correcta según el dialecto (PostgreSQL vs SQLite, sabiendo que SQLite histórico tiene soporte limitado de ALTER)?

### Arquitectura
Parser DDL (`ddl_parser.py`), motor de comparación (`diff_engine.py`), generador de SQL (`patch_generator.py`) y CLI.

### Pruebas mínimas
1. Comparar un esquema con tabla `users (id, name)` vs `users (id, name, email)` y verificar que detecte la adición de la columna `email`.
2. Probar `--generate-patch` en dialecto PostgreSQL y verificar que emita `ALTER TABLE users ADD COLUMN email VARCHAR;`.

### Pruebas de error
1. Pasar un archivo SQL con sintaxis inválida -> Exit code 2 con línea del error.

### Experiencia de usuario
Reporte visual claro con símbolos de diff: `+ Tabla nueva`, `- Tabla eliminada`, `~ Columna modificada`.

### Explicación posterior
Explica la diferencia entre migraciones basadas en estado (state-based diffing) y migraciones basadas en cambios secuenciales (migration scripts).

### Aplicación profesional
Validación de coherencia en pipelines de CI/CD, sincronización de ambientes de desarrollo y auditoría de esquemas de bases de datos.

### Reto adicional
Detectar modificaciones en restricciones de clave foránea (`FOREIGN KEY`) e índices (`CREATE INDEX`).

---
> [← Ejercicio 035](../ejercicio_035/README.md) · [Índice General](../README.md) · [Ejercicio 037 →](../ejercicio_037/README.md)
