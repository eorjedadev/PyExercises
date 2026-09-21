## Ejercicio 067 — Linter y Formateador Estricto de Consultas SQL (`sql-lint-fmt`)

> [← Ejercicio 066](../ejercicio_066/README.md) · [Índice General](../README.md) · [Ejercicio 068 →](../ejercicio_068/README.md)

### Contexto profesional
En equipos de ingeniería de datos y desarrollo backend, mantener consultas SQL consistentes, legibles y libres de anti-patrones (ej. uso de `SELECT *` en producción, palabras clave en minúsculas, falta de alias explícitos en joins, comparaciones con `NULL` usando `=` en lugar de `IS NULL`) es crucial para el rendimiento y la mantenibilidad.

### Problema
Construir una CLI que analice y formatee archivos con sentencias SQL (soportando dialectos de PostgreSQL y SQLite), aplique reglas de estilo (palabras clave en mayúsculas, indentación consistente de cláusulas `SELECT`, `FROM`, `WHERE`, `GROUP BY`), detecte malas prácticas y anti-patrones, y soporte el modo `--check` para integración en CI/CD.

### Usuario objetivo
Desarrolladores backend, ingenieros de datos y DBAs.

### Objetivo
Crear un linter y formateador de SQL con tokenizer léxico, soporte de dialectos y modo de verificación para pipelines.

### Ejemplo conceptual de uso
```bash
# Formatear un archivo SQL in-place
python sql_lint_fmt.py format queries.sql --write

# Verificar reglas de linter y fallar si hay anti-patrones en CI
python sql_lint_fmt.py lint ./sql/ --dialect postgresql --fail-on warning

# Comprobar si los archivos necesitan formateo sin modificarlos
python sql_lint_fmt.py format ./sql/ --check
```

### Requisitos funcionales
- Subcomando `format`: formatea sentencias SQL: palabras clave estándar (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `FROM`, `WHERE`, `JOIN`, `ON`, `GROUP BY`, `ORDER BY`, `HAVING`, `LIMIT`) en mayúsculas, cláusulas principales en nuevas líneas con indentación estándar de 2 o 4 espacios, y comas alineadas.
- Flag `--check` en `format`: devuelve exit code 1 si el archivo necesita formateo (sin modificar el archivo), o 0 si ya está formateado (estilo `black --check` / `prettier --check`).
- Subcomando `lint`: evalúa reglas de calidad:
  - `SQL001`: Prohibir `SELECT *` (exigir proyección explícita de columnas).
  - `SQL002`: Prohibir comparaciones `= NULL` o `!= NULL` (exigir `IS NULL` / `IS NOT NULL`).
  - `SQL003`: Prohibir sentencias `DELETE` o `UPDATE` sin cláusula `WHERE` (salvo que se use comentario de excepción explícito).
  - `SQL004`: Exigir alias explícitos en subconsultas (`FROM (SELECT ...) AS subq`).
  - `SQL005`: Prohibir el uso de `ORDER BY` en subconsultas a menos que se use `LIMIT`.

### Requisitos de CLI
- Subcomandos: `format`, `lint`.
- Opción `--dialect [postgresql|sqlite]` (default `postgresql`).
- Flag `--write / -w` (modifica el archivo directamente en `format`).
- Flag `--check`.
- Opción `--indent <N>` (default 2).
- Exit code 0 en éxito, 1 si hay violaciones de linter o archivos sin formatear con `--check`, 2 en errores de sintaxis SQL.

### Entradas
- Archivos SQL o directorios de scripts.

### Salidas
- Código SQL formateado en STDOUT o reporte de linter.

### Persistencia
Modificación de archivos en disco si se usa `-w / --write`.

### Validaciones
- Comprobar que los archivos existan y contengan sentencias SQL válidas.

### Casos límite
- Consultas complejas con CTEs (`WITH ... AS (...)`), funciones de ventana (`OVER (PARTITION BY ...)`).
- Strings literales que contienen palabras clave SQL (ej. `WHERE name = 'SELECT * FROM test'`; no deben modificarse las mayúsculas dentro de cadenas).
- Comentarios SQL de línea (`--`) y bloque (`/* */`).

### Manejo de errores
- Errores de tokenización de SQL.
- `PermissionError` al intentar sobreescribir archivos.

### Fundamentos de Python relacionados
- Tokenización léxica de código SQL o uso de expresiones regulares especializadas.
- Manipulación y formateo de cadenas con indentación jerárquica.
- `pathlib.Path` para recorrido recursivo de archivos `.sql`.

### Conceptos CLI relacionados
- Implementación de herramientas de formateo de código con semántica `--check` / `--write`.
- Linters de calidad de código para pipelines de integración continua.

### Herramientas o módulos para investigar
- `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para ignorar una regla específica en una línea mediante un comentario (ej. `-- sql-lint:disable SQL001`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para formatear el SQL recibido directamente a través de un pipe Unix desde STDIN?

### Diseño de variables
`sql_token_stream`, `formatted_sql_buffer`, `lint_violations_list`, `is_check_mode`, `indent_level_spaces`.

### Antes de programar
1. ¿Cómo tokenizar una consulta SQL para separar palabras clave, identificadores, cadenas entre comillas y comentarios sin alterar el contenido de las cadenas?
2. ¿Cómo implementar la regla `--check` comparando la cadena original con la formateada y retornando exit code 1 si difieren?

### Arquitectura
Tokenizer SQL (`sql_tokenizer.py`), formateador (`sql_formatter.py`), motor de reglas de linter (`lint_rules.py`) y CLI.

### Pruebas mínimas
1. Formatear `select id,name from users where id=1` y verificar que resulte `SELECT
  id,
  name
FROM users
WHERE id = 1`.
2. Ejecutar `lint` sobre una consulta con `where status = null` y verificar que detecte la violación `SQL002`.

### Pruebas de error
1. Ejecutar `format --check` sobre un archivo sin formatear -> Exit code 1.

### Experiencia de usuario
En modo linter, reporte claro con línea, columna, código de regla y sugerencia de corrección.

### Explicación posterior
Explica por qué la comparación `= NULL` en SQL estándar evalúa a `UNKNOWN` (falso en filtros WHERE) debido a la lógica trivaluada de SQL.

### Aplicación profesional
Pre-commit hooks en repositorios de software, linters de CI/CD para bases de datos y herramientas de formateo de consultas.

### Reto adicional
Implementar detección y advertencia de consultas SQL vulnerables a inyección SQL por concatenación de cadenas en lugar de parámetros preparados.

---
> [← Ejercicio 066](../ejercicio_066/README.md) · [Índice General](../README.md) · [Ejercicio 068 →](../ejercicio_068/README.md)
