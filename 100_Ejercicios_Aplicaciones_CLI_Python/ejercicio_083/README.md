## Ejercicio 083 — Detector de Fragmentos de Código Duplicado (`code-clone-finder`)

> [← Ejercicio 082](../ejercicio_082/README.md) · [Índice General](../README.md) · [Ejercicio 084 →](../ejercicio_084/README.md)

### Contexto profesional
En grandes bases de código de software corporativo con años de evolución, los desarrolladores copian y pegan funciones enteras con ligeras modificaciones de variables, generando duplicación de código (Code Clones). Esto infla la deuda técnica, dificulta el mantenimiento y propaga vulnerabilidades cuando se corrige un bug en una copia pero se olvida en las demás.

### Problema
Construir una CLI de análisis estático que escanee repositorios de código fuente (archivos Python, JavaScript, Java, C), normalice el código eliminando comentarios/espacios, genere fragmentos de tokens o n-gramas (AST o tokenización), compare similitudes mediante algoritmos de hashing/Jaccard y reporte bloques de código duplicados o casi idénticos con porcentaje de similitud configurable.

### Usuario objetivo
Revisores de código, líderes técnicos y auditores de calidad de software.

### Objetivo
Desarrollar un detector de código duplicado (Type-1 y Type-2 Code Clones) con tokenización, cálculo de similitud y reporte visual de clones.

### Ejemplo conceptual de uso
```bash
# Escanear proyecto buscando duplicaciones con similitud >= 85% y mínimo 6 líneas
python code_clone_finder.py scan ./src --min-lines 6 --threshold 0.85

# Exportar reporte de duplicación en formato JSON para métricas de calidad
python code_clone_finder.py scan ./src --format json -o duplicados.json
```

### Requisitos funcionales
- Recorrer archivos de código fuente según extensiones configuradas (`.py`, `.js`, `.ts`, `.java`, `.go`, `.cpp`).
- Normalización de código:
  - Remover comentarios y líneas en blanco.
  - En modo Type-2: normalizar nombres de variables locales y literales para detectar código copiado donde solo se cambiaron nombres de variables.
- Algoritmo de detección de clones:
  - Segmentar el código en bloques de N líneas deslizantes (`--min-lines`, default 6).
  - Calcular firmas de hash o n-gramas de tokens por bloque.
  - Identificar pares o grupos de bloques con similitud superior a `--threshold` (default 0.85 = 85%).
- Subcomando `scan`: genera reporte con pares de archivos duplicados, números de línea de inicio/fin, porcentaje de similitud y fragmentos de código comparados lado a lado.
- Subcomando `stats`: calcula el porcentaje global de duplicación del proyecto (Duplicated Lines %: $\frac{\text{líneas duplicadas}}{\text{total líneas}} \times 100$).

### Requisitos de CLI
- Subcomando `scan`, `stats`.
- Argumento posicional: directorio o archivos a analizar.
- Opción `--min-lines <N>` (default 6).
- Opción `--threshold <FLOAT>` (0.5 a 1.0, default 0.85).
- Opción `--ignore <DIRS>` (default `node_modules,.git,venv`).
- Opción `--format [table|json|html]`.
- Exit code 0 si la duplicación global está por debajo del umbral de calidad, 1 si supera el límite permitido, 2 en errores.

### Entradas
- Código fuente y parámetros de sensibilidad de detección.

### Salidas
- Reporte de clones de código y estadísticas de duplicación en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Validar que el directorio exista.
- Validar que `--threshold` esté entre 0.0 y 1.0.

### Casos límite
- Bloques repetitivos triviales (ej. sentencias `import`, getters/setters simples o cabeceras de licencia; ofrecer opción de ignorar imports/boilerplate con `--ignore-boilerplate`).
- Archivos muy grandes con miles de líneas de código.
- Proyectos políglotas con múltiples lenguajes.

### Manejo de errores
- `UnicodeDecodeError` en archivos binarios o no UTF-8 (descartar automáticamente sin abortar el análisis).

### Fundamentos de Python relacionados
- Tokenización con módulo estándar `tokenize` (para Python) o expresiones regulares genéricas.
- Cálculo de coeficientes de similitud (Jaccard Index, Levenshtein o MinHash).
- `collections.defaultdict` para indexación de firmas de hash de bloques.
- `difflib` para comparación visual de diferencias.

### Conceptos CLI relacionados
- Análisis de calidad de código y detección de anti-patrones en terminal.
- Implementación de algoritmos de comparación y hashing difuso.

### Herramientas o módulos para investigar
- `tokenize` y `difflib`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `refactor-suggest` que proponga extraer el código duplicado a una función compartida?

### Diseño de argumentos
¿Cómo nombrarías la opción para fallar en CI si el porcentaje de duplicación global del proyecto supera el 5% (`--max-duplication-percent 5.0`)?

### Diseño de variables
`source_code_files_list`, `tokenized_code_blocks_index`, `detected_clone_pairs_list`, `jaccard_similarity_score`, `duplicated_lines_percentage`.

### Antes de programar
1. ¿Cómo funciona la detección de clones Tipo 1 (copia exacta sin contar espacios/comentarios) vs Tipo 2 (copia con renombramiento de variables y tipos)?
2. ¿Cómo indexar los hashes de bloques de N líneas en una tabla hash en memoria para comparar en $O(N)$ en lugar de comparar todos los pares de bloques entre sí en $O(N^2)$?

### Arquitectura
Normalizador y tokenizer (`code_normalizer.py`), motor de indexación de bloques (`block_indexer.py`), calculador de similitud (`similarity_calc.py`) y CLI.

### Pruebas mínimas
1. Escanear un directorio de prueba con 2 funciones idénticas en archivos diferentes y verificar que detecte el clon con 100% de similitud.
2. Modificar nombres de variables en una de las funciones y verificar que en modo normalizado siga detectando el clon con alta similitud.

### Pruebas de error
1. Pasar un umbral inválido `--threshold 1.5` -> Exit code 2 con error de validación.

### Experiencia de usuario
Reporte visual en terminal mostrando los dos bloques de código encontrados lado a lado con resaltado de líneas coincidentes.

### Explicación posterior
Explica el principio DRY (Don't Repeat Yourself) y la taxonomía de clones de software (Clones Tipo 1 a Tipo 4).

### Aplicación profesional
Auditorías de calidad de software previas a compras corporativas, linters de CI/CD para control de deuda técnica y refactorización.

### Reto adicional
Generar automáticamente un reporte HTML interactivo con navegación entre los bloques de código duplicados.

---
> [← Ejercicio 082](../ejercicio_082/README.md) · [Índice General](../README.md) · [Ejercicio 084 →](../ejercicio_084/README.md)
