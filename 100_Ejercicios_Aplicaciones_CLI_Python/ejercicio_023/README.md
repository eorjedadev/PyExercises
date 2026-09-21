## Ejercicio 023 — Escáner de Comentarios TODO/FIXME en Código Fuente (`todo-scan`)

> [← Ejercicio 022](../ejercicio_022/README.md) · [Índice General](../README.md) · [Ejercicio 024 →](../ejercicio_024/README.md)

### Contexto profesional
Durante revisiones de código, auditorías de deuda técnica y preparación de releases, los líderes técnicos necesitan inventariar todos los comentarios pendientes (`TODO`, `FIXME`, `HACK`, `BUG`, `OPTIMIZE`, `NOTE`) dispersos en el código fuente de un proyecto políglota.

### Problema
Construir una CLI que analice un árbol de directorios de código fuente, detecte comentarios de deuda técnica respetando las sintaxis de comentarios de múltiples lenguajes (Python `#`, C/Java/JS `//` y `/* */`, SQL `--`, HTML `<!-- -->`), extraiga el autor o ticket asociado (ej. `TODO(juan): refactorizar`) y genere reportes tabulares o estructurados.

### Usuario objetivo
Desarrolladores de software, tech leads y revisores de calidad.

### Objetivo
Crear un linter de deuda técnica políglota con extracción de metadatos, filtrado por etiquetas y umbrales de fallo para CI/CD.

### Ejemplo conceptual de uso
```bash
# Escanear el proyecto buscando todos los TODOs y FIXMEs
python todo_scan.py ./src

# Filtrar solo por etiquetas críticas y fallar si hay más de 0 FIXMEs
python todo_scan.py ./src --tags "FIXME,BUG" --max-allowed 0

# Exportar reporte a JSON o CSV
python todo_scan.py . --format json -o deuda_tecnica.json
```

### Requisitos funcionales
- Reconocer sintaxis de comentarios según extensión de archivo (`.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, `.go`, `.rs`, `.sql`, `.html`, `.css`).
- Detectar etiquetas estándar: `TODO`, `FIXME`, `HACK`, `BUG`, `XXX`, `OPTIMIZE`.
- Extraer opcionalmente autor o ticket asociado entre paréntesis (ej. `TODO(PROJ-123): fix query`).
- Extraer texto del comentario, ruta del archivo y número de línea.
- Opción `--max-allowed N`: define un umbral máximo tolerado de items (si se supera, retorna exit code 1 para romper el pipeline de CI).

### Requisitos de CLI
- Argumento posicional: directorio o archivo a escanear (default `.`).
- Opción `-t / --tags <TAGS>`: lista de etiquetas a buscar (default `TODO,FIXME,HACK,BUG`).
- Opción `--format [table|json|csv|markdown]` (default `table`).
- Opción `--max-allowed <N>`: umbral máximo permitido.
- Opción `--ignore <DIRS>`: carpetas a omitir (default `node_modules,.git,venv,__pycache__`).
- Exit code 0 si los items están dentro del umbral, 1 si se supera `--max-allowed`, 2 en errores.

### Entradas
- Directorio de código fuente.
- Filtros de etiquetas y umbrales.

### Salidas
- Reporte estructurado en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Validar que el directorio exista.
- Validar que el umbral sea un entero mayor o igual a 0.

### Casos límite
- Palabras como 'TODO' dentro de cadenas de texto literales (ej. `msg = "TODO list"`).
- Comentarios multilínea en bloques `/* ... */`.
- Archivos con codificaciones no UTF-8.

### Manejo de errores
- `UnicodeDecodeError`: Omitir archivos binarios automáticamente sin abortar el escaneo.

### Fundamentos de Python relacionados
- `pathlib.Path`.
- Expresiones regulares para detección de patrones y comentarios.
- Mapeo de extensiones a sintaxis con diccionarios.
- Serialización JSON y CSV.

### Conceptos CLI relacionados
- Integración como quality gate en CI/CD con códigos de salida condicionales.
- Detección automática de tipo de archivo.

### Herramientas o módulos para investigar
- `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías una opción para agrupar los resultados por autor detectado (`--group-by-author`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para mostrar el contexto de código (2 líneas anteriores y posteriores al comentario)?

### Diseño de variables
`source_tree`, `detected_todos_list`, `tag_filter_set`, `comment_regex`, `max_allowed_threshold`.

### Antes de programar
1. ¿Cómo distinguir un comentario real `# TODO: ...` de una línea dentro de un docstring multilínea `""" TODO """`?
2. ¿Cómo diseñar la expresión regular para capturar tanto `TODO: mensaje` como `TODO(autor): mensaje`?

### Arquitectura
Módulo extractor por lenguaje (`extractors.py`), recopilador (`collector.py`) y formateador de reportes.

### Pruebas mínimas
1. Escanear un directorio de prueba con 3 archivos (`.py`, `.js`, `.sql`) y comprobar que detecte todos los TODOs.
2. Probar con `--max-allowed 0` y verificar que retorne exit code 1 si encuentra al menos un item.

### Pruebas de error
1. Pasar un directorio inexistente -> Exit code 2.

### Experiencia de usuario
Tabla atractiva en terminal con columnas: `ARCHIVO:LÍNEA`, `ETIQUETA`, `AUTOR` y `MENSAJE`.

### Explicación posterior
Explica cómo la deuda técnica no gestionada degrada la velocidad de desarrollo y cómo automatizar su control en Pull Requests.

### Aplicación profesional
Quality gates en CI/CD, auditorías de código previas a adquisiciones tecnológicas y métricas de ingeniería.

### Reto adicional
Integrar con Git (`git blame`) para extraer automáticamente el autor del commit y la antigüedad del comentario si no está explícito en el texto.

---
> [← Ejercicio 022](../ejercicio_022/README.md) · [Índice General](../README.md) · [Ejercicio 024 →](../ejercicio_024/README.md)
