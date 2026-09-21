## Ejercicio 017 — Conversor Bidireccional JSON ↔ CSV (`data-conv`)

> [← Ejercicio 016](../ejercicio_016/README.md) · [Índice General](../README.md) · [Ejercicio 018 →](../ejercicio_018/README.md)

### Contexto profesional
La interoperabilidad entre bases de datos relacionales (que exportan e importan CSV) y servicios web / APIs REST (que consumen JSON) exige herramientas rápidas de terminal para convertir datos tabulares en estructuras jerárquicas y viceversa.

### Problema
Desarrollar una CLI que convierta archivos JSON a CSV y archivos CSV a JSON, admitiendo aplanamiento de objetos anidados (flattening), selección de campos y formateo configurable de salida.

### Usuario objetivo
Ingenieros de datos, desarrolladores backend y analistas.

### Objetivo
Crear un conversor universal bidireccional entre formatos estructurados con detección automática de tipo y opciones de aplanamiento.

### Ejemplo conceptual de uso
```bash
# Convertir JSON a CSV detectando esquema
python data_conv.py usuarios.json -o usuarios.csv

# Convertir CSV a JSON con indentación de 2 espacios
python data_conv.py datos.csv --to-json --indent 2 -o datos.json

# Convertir desde STDIN y aplanar objetos anidados
cat api_response.json | python data_conv.py --to-csv --flatten
```

### Requisitos funcionales
- Detectar formato de origen por extensión de archivo o mediante flags explícitos (`--to-csv` / `--to-json`).
- Al convertir JSON a CSV: extraer lista de objetos, inferir todas las cabeceras únicas y escribir filas.
- Si se usa `--flatten`, aplanar objetos anidados (ej. `{"user": {"name": "Ana"}}` -> columna `user.name`).
- Al convertir CSV a JSON: convertir cada fila en un objeto y emitir un array JSON válido.
- Opciones de formato: `--indent N` para JSON, `--delimiter` para CSV.

### Requisitos de CLI
- Argumento posicional opcional: archivo de entrada (lee STDIN si se omite).
- Opción `-o / --output <RUTA>` (escribe en archivo o emite a STDOUT).
- Flags de dirección: `--to-json` o `--to-csv`.
- Flag `--flatten` para objetos JSON.
- Opción `--indent <N>` (default 2).
- Exit code 0 en éxito, 1 en error de estructura de datos, 2 en argumentos inválidos.

### Entradas
- Archivo o flujo JSON / CSV.

### Salidas
- Archivo generado o flujo transformado en STDOUT.

### Persistencia
Escritura en archivo si se usa `-o`.

### Validaciones
- Si se convierte JSON a CSV, validar que la raíz sea un array de objetos o un objeto único convertible a fila.
- Si el CSV no tiene cabeceras, generar nombres por defecto (`col_1`, `col_2`...) si se pasa `--no-header`.

### Casos límite
- Objetos JSON con claves heterogéneas (algunos objetos tienen campos que otros no tienen; el CSV debe incluir la unión de todas las columnas).
- Valores nulos o tipos de datos booleanos en JSON que se representan en CSV.
- Arrays anidados dentro de objetos JSON (definir cómo serializarlos en CSV, ej. string JSON o lista separada por comas).

### Manejo de errores
- `json.JSONDecodeError` y `csv.Error`.
- Errores de acceso a disco.

### Fundamentos de Python relacionados
- Módulos `json` y `csv`.
- Recursividad para aplanar diccionarios (`flatten_dict`).
- Generación de conjuntos de claves únicas (`set`).

### Conceptos CLI relacionados
- Inferencia de intención basada en nombres de archivo vs flags explícitos.
- Soporte universal de pipes Unix.

### Herramientas o módulos para investigar
- `json`.
- `csv`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la herramienta para admitir también formatos adicionales en el futuro como YAML o Parquet?

### Diseño de argumentos
¿Cómo nombrarías la opción para forzar el casteo de tipos al pasar de CSV a JSON (ej. números a int/float, 'true'/'false' a booleano)?

### Diseño de variables
`input_format`, `output_format`, `flattened_records`, `all_headers_set`, `json_payload`, `csv_writer`.

### Antes de programar
1. ¿Cómo transformar un diccionario anidado como `{'a': {'b': 1, 'c': 2}}` en `{'a.b': 1, 'a.c': 2}` mediante una función recursiva?
2. ¿Cómo recopilar todas las columnas posibles si el primer objeto del JSON solo tiene 2 claves y el décimo tiene 5?

### Arquitectura
Módulo de conversión (`converters.py`), módulo de aplanamiento (`flattener.py`) y CLI (`data_conv.py`).

### Pruebas mínimas
1. Convertir un JSON de 3 registros a CSV y validar que el archivo resultante tenga cabecera y 3 filas.
2. Convertir el CSV resultante de vuelta a JSON y validar que la información se preserve.

### Pruebas de error
1. Intentar convertir a CSV un JSON que contiene un número primitivo en lugar de una lista u objeto -> Exit code 1.

### Experiencia de usuario
Salida limpia en STDOUT por defecto para facilitar encadenamiento en pipelines.

### Explicación posterior
Explica el problema de pérdida de fidelidad de tipos (type loss) al convertir datos de JSON a CSV.

### Aplicación profesional
Carga de datos en bases de datos analíticas, preparación de payloads para APIs y migración de datos.

### Reto adicional
Implementar reconstrucción inversa de objetos anidados (`--unflatten`) al convertir de CSV con nombres de columna en dot-notation a JSON.

---
> [← Ejercicio 016](../ejercicio_016/README.md) · [Índice General](../README.md) · [Ejercicio 018 →](../ejercicio_018/README.md)
