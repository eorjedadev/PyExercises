## Ejercicio 001 — Contador y Analizador de Frecuencia de Palabras (`word-stats`)

> [Índice General](../README.md) · [Ejercicio 002 →](../ejercicio_002/README.md)

### Contexto profesional
En auditorías de contenido, procesamiento de transcripciones y análisis forense de texto plano, se requiere extraer métricas básicas de documentos directamente en terminal sin abrir editores gráficos ni consumir memoria excesiva.

### Problema
Se necesita una herramienta de línea de comandos que reciba una ruta a un archivo de texto, cuente líneas, palabras, caracteres y determine las N palabras más frecuentes ignorando mayúsculas y signos de puntuación comunes.

### Usuario objetivo
Desarrolladores, analistas de datos y administradores de sistemas que procesan archivos de log o volcados de texto.

### Objetivo
Construir una CLI que reciba la ruta de un archivo mediante argumentos posicionales, procese el texto de forma segura y devuelva un reporte formateado con estadísticas precisas y códigos de salida apropiados.

### Ejemplo conceptual de uso
```bash
# Análisis estándar de un archivo
python word_stats.py datos/documento.txt

# Especificando el top 5 de palabras más frecuentes
python word_stats.py datos/documento.txt --top 5
```

### Requisitos funcionales
- Abrir y leer el archivo especificado en modo lectura UTF-8.
- Contar total de líneas, total de palabras y total de caracteres.
- Normalizar palabras (convertir a minúsculas y limpiar signos de puntuación como `.,:;!?"'()[]`).
- Calcular las N palabras más frecuentes (por defecto top 10).
- Mostrar las métricas en un formato limpio y alineado en terminal.

### Requisitos de CLI
- Argumento posicional obligatorio: ruta al archivo de texto.
- Opción opcional: `--top N` (número entero positivo de palabras a mostrar, default 10).
- Opción de ayuda `--help` descriptiva.
- Código de salida 0 si el análisis es exitoso.
- Código de salida 1 si el archivo no existe o no tiene permisos de lectura.
- Código de salida 2 si los argumentos son inválidos (ej. `--top` no es un entero positivo).

### Entradas
- Ruta del archivo (`pathlib.Path` o `str`).
- Parámetro opcional `--top` (entero).

### Salidas
Reporte en STDOUT con:
- Total de líneas
- Total de palabras
- Total de caracteres
- Tabla o lista de frecuencia del top de palabras.
Mensajes de error formateados en STDERR.

### Persistencia
No requiere persistencia en disco; opera en memoria sobre el flujo del archivo.

### Validaciones
- Comprobar que la ruta ingresada exista y sea un archivo regular.
- Validar que el archivo no esté vacío (archivo de 0 bytes).
- Validar que el argumento `--top` sea un entero estrictamente mayor a 0.

### Casos límite
- Archivo de texto vacío (debe reportar 0 líneas/palabras o mensaje controlado sin fallar con ZeroDivisionError).
- Archivo que contiene únicamente caracteres de espacio en blanco y saltos de línea.
- Archivo con caracteres multibyte o emojis en UTF-8.
- Archivo con palabras compuestas o con guiones.

### Manejo de errores
- `FileNotFoundError`: Notificar en STDERR que el archivo no existe.
- `PermissionError`: Notificar en STDERR la falta de permisos de lectura.
- `UnicodeDecodeError`: Notificar que el archivo no posee codificación UTF-8 válida.
- `ValueError`: Capturar errores al parsear el argumento `--top`.

### Fundamentos de Python relacionados
- Manejo de archivos con context managers (`with open(...)`).
- Estructuras de datos: diccionarios (`dict`), listas, tuplas y `collections.Counter`.
- Métodos de cadenas (`str.lower()`, `str.split()`, `str.strip()`).
- Módulo `sys` (`sys.argv`, `sys.exit`, `sys.stderr`).

### Conceptos CLI relacionados
- Argumentos posicionales vs nombrados.
- Separación estricta de STDOUT y STDERR.
- Códigos de salida del proceso (`exit codes`).
- Validación de contratos de interfaz en terminal.

### Herramientas o módulos para investigar
- `sys.argv` o módulo `argparse` de la biblioteca estándar.
- `pathlib.Path` para inspección de rutas.
- `collections.Counter` y módulo `string`.

### Diseño de comandos
¿El comando debe invocarse como script único o admitirá en el futuro subcomandos como `word-stats analyze` o `word-stats compare`?

### Diseño de argumentos
- ¿Cómo nombrarías la opción para omitir palabras vacías (stopwords)?
- ¿Cómo permitirías que el usuario elija si desea distinguir mayúsculas de minúsculas (`--case-sensitive`)?

### Diseño de variables
Diseña nombres claros y descriptivos como `source_path`, `total_lines`, `total_words`, `word_frequencies`, `top_limit`, `normalized_word`. Evita nombres como `f`, `d`, `temp`, `res`.

### Antes de programar
1. ¿Qué ocurriría si el usuario pasa un archivo de 1 GB? ¿Tu solución leería todo en memoria con `.read()` o iteraría línea a línea?
2. ¿Cómo asegurar que los signos de puntuación adyacentes a una palabra no se cuenten como parte de ella?
3. ¿Qué código de salida debe retornar si el archivo existe pero no tiene palabras?

### Arquitectura
Estructura sugerida para este ejercicio:
```
ejercicio_001/
├── word_stats.py       # Punto de entrada y lógica CLI
└── datos/
    └── sample.txt      # Archivo de prueba con texto multilínea
```

### Pruebas mínimas
1. Ejecutar `python word_stats.py datos/sample.txt` y verificar que el conteo coincida con `wc -w` y `wc -l`.
2. Ejecutar `python word_stats.py datos/sample.txt --top 3` y validar que devuelva exactamente 3 palabras.

### Pruebas de error
1. Ejecutar `python word_stats.py archivo_fantasma.txt` -> Comprobar que imprime error en STDERR y retorna código 1.
2. Ejecutar `python word_stats.py datos/sample.txt --top -5` -> Comprobar error de validación y código 2.

### Experiencia de usuario
La salida debe ser visualmente legible, con etiquetas claras y alineación en columnas para las frecuencias. Los mensajes de error deben ser directos y no exponer tracebacks crudos de Python.

### Explicación posterior
Explica por qué es fundamental cerrar los descriptores de archivo con `with`, cómo optimizaste la tokenización de palabras y cómo gestionaste los códigos de retorno para permitir la integración en scripts bash.

### Aplicación profesional
Este tipo de procesadores es la base de herramientas de indexación, motores de búsqueda interna, linters de redacción técnica y filtros de procesamiento de logs.

### Reto adicional
Añade un flag opcional `--min-len N` para filtrar palabras con una longitud menor a N caracteres y una opción `--ignore-stopwords` para excluir artículos y preposiciones comunes.

---
> [Índice General](../README.md) · [Ejercicio 002 →](../ejercicio_002/README.md)
