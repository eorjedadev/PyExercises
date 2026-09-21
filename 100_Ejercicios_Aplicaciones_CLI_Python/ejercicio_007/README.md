## Ejercicio 007 — Extractor y Filtro de Columnas CSV (`csv-cut`)

> [← Ejercicio 006](../ejercicio_006/README.md) · [Índice General](../README.md) · [Ejercicio 008 →](../ejercicio_008/README.md)

### Contexto profesional
En la administración de bases de datos y procesamiento de reportes empresariales, frecuentemente se reciben archivos CSV gigantescos con decenas de columnas de las cuales solo se necesitan 2 o 3 para un análisis posterior.

### Problema
Construir una CLI similar a la utilidad Unix `cut`, pero especializada en CSV/TSV, que permita seleccionar columnas por nombre de cabecera o por índice numérico, aplicar filtros por valor y cambiar el delimitador de salida.

### Usuario objetivo
Ingenieros de datos, analistas y administradores de sistemas.

### Objetivo
Desarrollar una herramienta rápida de filtrado y proyección de columnas CSV con soporte de streaming.

### Ejemplo conceptual de uso
```bash
# Extraer columnas por nombre
python csv_cut.py datos/usuarios.csv --columns "id,email,status"

# Filtrar filas donde status sea 'ACTIVE' y cambiar delimitador a punto y coma
python csv_cut.py datos/usuarios.csv --columns "id,email" --filter "status=ACTIVE" --delimiter ";"
```

### Requisitos funcionales
- Leer archivos CSV con manejo de comillas y delimitadores configurables.
- Proyectar columnas por nombre de cabecera (ej. `--columns id,email`) o por índice 1-indexed (ej. `--fields 1,3,5`).
- Filtrar filas con condiciones simples `--filter "COLUMNA=VALOR"` o `--filter "COLUMNA!=VALOR"`.
- Permitir especificar delimitador de entrada (`--in-delimiter`) y delimitador de salida (`--out-delimiter`).
- Emitir el resultado directamente a STDOUT para posibilitar encadenamiento en pipelines.

### Requisitos de CLI
- Argumento posicional: archivo CSV de entrada.
- Opción `--columns <COLS>` o `--fields <INDICES>`.
- Opción `--filter <EXPR>`.
- Opciones de delimitador: `-d / --delimiter`.
- Exit code 0 en éxito, 1 si las columnas especificadas no existen, 2 en errores de sintaxis.

### Entradas
- Ruta de archivo CSV.
- Listado de columnas o índices.
- Expresión de filtrado.

### Salidas
- Flujo CSV transformado en STDOUT.
- Errores en STDERR.

### Persistencia
Sin persistencia (orientado a streaming).

### Validaciones
- Comprobar que el archivo contenga encabezados válidos si se usan nombres de columna.
- Validar que los índices numéricos estén dentro del rango disponible.
- Validar formato de la expresión `--filter`.

### Casos límite
- Valores de campo que contienen el carácter delimitador o saltos de línea entrecomillados.
- Archivos CSV con codificaciones `utf-8-sig` (BOM de Windows Excel).
- Filas con número desigual de columnas.

### Manejo de errores
- `KeyError` o `IndexError` al buscar columnas.
- `csv.Error` por formato corrupto.

### Fundamentos de Python relacionados
- Módulo estándar `csv` (`csv.reader`, `csv.writer`, `csv.DictReader`).
- Generadores para procesamiento línea a línea (`yield`).
- Comprensión de listas y diccionarios.

### Conceptos CLI relacionados
- Procesamiento en streaming de flujos tabulares.
- Compatibilidad con pipes Unix (`cat datos.csv | python csv_cut.py ...`).

### Herramientas o módulos para investigar
- `csv`.
- `sys.stdin` y `sys.stdout`.
- `argparse`.

### Diseño de comandos
¿Cómo harías que la CLI lea de `sys.stdin` si no se proporciona el argumento posicional de archivo?

### Diseño de argumentos
¿Cómo soportarías operadores de comparación numérica en los filtros (ej. `--filter "edad>=18"`)?

### Diseño de variables
`input_csv_path`, `target_columns`, `column_indices`, `filter_column`, `filter_operator`, `filter_value`.

### Antes de programar
1. ¿Por qué `split(',')` falla estrepitosamente en CSVs reales y es obligatorio usar el módulo `csv`?
2. ¿Cómo procesar un archivo de 5 millones de filas sin cargarlas todas en una lista en memoria?

### Arquitectura
Estructura en generadores: `read_rows()` -> `filter_rows()` -> `project_columns()` -> `write_rows()`.

### Pruebas mínimas
1. Proyectar 2 columnas de un archivo de prueba y verificar que la cabecera y datos coincidan exactamente.
2. Aplicar filtro `--filter "status=INACTIVE"` y comprobar que solo pasen esas filas.

### Pruebas de error
1. Solicitar columna inexistente `--columns "no_existe"` -> Exit code 1.

### Experiencia de usuario
Salida limpia en STDOUT sin mensajes informativos adicionales para no ensuciar la redirección a otros archivos.

### Explicación posterior
Explica cómo `csv.DictReader` mapea cabeceras a diccionarios y el costo en rendimiento comparado con `csv.reader` basado en índices.

### Aplicación profesional
Esencial en pipelines ETL, preparación de datasets para machine learning y limpieza de volcados de datos empresariales.

### Reto adicional
Permitir omitir columnas en lugar de seleccionarlas mediante el flag `--exclude-columns "password,token"`.

---
> [← Ejercicio 006](../ejercicio_006/README.md) · [Índice General](../README.md) · [Ejercicio 008 →](../ejercicio_008/README.md)
