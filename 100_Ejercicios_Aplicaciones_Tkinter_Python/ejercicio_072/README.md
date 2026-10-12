## Ejercicio 072 — Revisor de Calidad de Código y Conteo de Líneas (`CodebaseMetricsApp`)

> [Índice General](../README.md) · [← Ejercicio 071](../ejercicio_071/README.md) · [Ejercicio 073 →](../ejercicio_073/README.md)

### Contexto profesional
En auditorías de ingeniería de software y estimación de proyectos de refactorización, los líderes técnicos analizan repositorios de código para calcular el volumen de líneas, comentarios, funciones y complejidad básica de un proyecto Python.

### Usuario objetivo
Líder técnico, arquitecto de software o evaluador de calidad de código.

### Problema
Analizar proyectos grandes con miles de archivos de código fuente recorriendo el sistema de archivos de forma síncrona bloquea la herramienta de auditoría e impide presentar resúmenes en tiempo real.

### Objetivo
Construir un analizador de proyectos de software en segundo plano con `threading` que escanee recursivamente una carpeta con scripts `.py`, calcule métricas por archivo (Líneas Totales, Líneas de Código Real, Líneas de Comentarios, Líneas en Blanco, Conteo de Funciones y Clases usando el módulo estándar `ast`), muestre una barra de progreso y consolide las estadísticas en un `ttk.Treeview` jerárquico.

### Flujo principal
El auditor selecciona la carpeta raíz del proyecto de software con `filedialog`. Presiona 'Analizar Código'. Un hilo secundario recorre los archivos `.py`, parsea el árbol de sintaxis abstracta (`ast`) de cada archivo para contar clases y funciones, y clasifica las líneas. La interfaz actualiza la barra de progreso. Al concluir, el Treeview muestra la tabla de archivos y un panel de resumen con el porcentaje de comentarios del proyecto.

### Requisitos funcionales
- Selección de carpeta raíz del repositorio de software mediante `filedialog`.
- Recorrido recursivo en hilo de fondo (`threading.Thread`) buscando archivos con extensión `.py`.
- Análisis de cada archivo: Total de Líneas, Líneas en Blanco, Líneas de Comentarios (iniciadas con `#` o docstrings simples) y Líneas de Código Lógico (SLOC).
- Conteo de `def` (funciones/métodos) y `class` (clases) mediante inspección de sintaxis con el módulo estándar `ast`.
- Despacho de métricas por archivo mediante `queue.Queue`.
- Visualización en `ttk.Treeview` con columnas para cada métrica.
- Resumen consolidado: Total de archivos analizados, Total SLOC del proyecto, Densidad de comentarios (%) y Promedio de funciones por archivo.

### Requisitos de interfaz
- Barra superior con selector de carpeta y botón de análisis.
- Barra de progreso determinada activa durante el escaneo.
- `Treeview` amplio con alineación numérica a la derecha y columnas ordenables.
- Panel inferior con tarjetas destacadas para los totales consolidados de la base de código.

### Datos
- Ficha de métricas: archivo_relativo, total_lineas, sloc, comentarios, blanco, funciones_count, clases_count.

### Estado
- Hilo de auditoría activo.
- Cola de métricas thread-safe.
- Totales consolidados del proyecto.

### Persistencia
Exportación del informe consolidado a archivo CSV o TXT mediante diálogo de guardado.

### Validaciones
- Verificar que la carpeta seleccionada contenga al menos un archivo con extensión `.py`.
- Manejar archivos con errores de sintaxis (`SyntaxError`) sin detener el análisis de los demás archivos.

### Casos límite
- Archivos de Python vacíos (0 líneas).
- Archivos con sintaxis inválida o código de versiones incompatibles de Python.
- Carpetas virtuales o dependencias (ej. `.venv`, `__pycache__`) que deben ignorarse opcionalmente.

### Manejo de errores
- Capturar excepciones de lectura y `SyntaxError` al parsear con `ast.parse()` registrando el archivo con estado 'Error de Sintaxis'.

### Fundamentos de Python relacionados
- Módulo estándar `ast` (Abstract Syntax Tree) para inspección segura de código sin ejecutarlo (`ast.parse`, `ast.walk`, `ast.FunctionDef`, `ast.ClassDef`).
- Análisis léxico simple de líneas de texto.
- Recorrido de árboles de directorios con `pathlib.Path.rglob`.

### Conceptos Tkinter relacionados
- Integración de análisis sintáctico en segundo plano con tablas de visualización en Tkinter.
- Manejo de interfaces responsivas durante operaciones de cálculo intensivo.

### Herramientas para investigar
- Módulo estándar `ast` de Python.
- Nodos `ast.FunctionDef`, `ast.AsyncFunctionDef` y `ast.ClassDef`.

### Diseño de interfaz
¿Cómo asegurarías que las columnas numéricas del Treeview tengan suficiente espacio y formato alineado para comparar archivos grandes con archivos pequeños?

### Diseño de variables
Usa nombres como `metrics_tree`, `repo_path_entry`, `analyze_btn`, `progress_bar`, `total_sloc_label`, `comment_ratio_label`, `metrics_queue`, `scanner_thread`.

### Antes de programar
1. ¿Por qué es infinitamente más robusto contar funciones usando el módulo estándar `ast` en lugar de buscar la palabra `'def '` con expresiones regulares o búsquedas de texto plano?
2. ¿Cómo se excluyen automáticamente del análisis carpetas como `.git`, `__pycache__` o `.venv` para no distorsionar las métricas?

### Arquitectura
```
ejercicio_072/
├── app.py             # Interfaz de métricas, tarjetas y Treeview
├── code_worker.py     # Hilo de escaneo recursivo y emisor por colas
└── ast_analyzer.py    # Análisis sintáctico con ast y clasificación de líneas
```

### Pruebas mínimas
1. Analizar una carpeta con 5 archivos `.py` -> La barra debe avanzar hasta el 100% y la tabla debe mostrar el conteo exacto de líneas, SLOC, funciones y clases de cada archivo.
2. Verificar que los totales consolidados inferiores coincidan con la suma de las columnas de la tabla.

### Pruebas de error
1. Incluir un archivo con un error de sintaxis intencional -> Debe registrar el error en la tabla sin interrumpir el escaneo de los demás archivos.

### Experiencia de usuario
La tabla debe permitir ordenar por SLOC al hacer clic en el encabezado para identificar de inmediato los archivos más grandes y complejos del proyecto.

### Explicación posterior
¿Cómo permite el módulo `ast` de la biblioteca estándar de Python inspeccionar la estructura lógica de un programa sin necesidad de ejecutar su código?

### Aplicación profesional
Herramientas internas de auditoría de calidad de código, linters corporativos, preparación de cotizaciones de refactorización y dashboards de deuda técnica.

### Reto adicional
Añade una casilla de verificación 'Excluir carpetas virtuales (.venv, env, site-packages)' para asegurar que solo se audite el código propio del proyecto.

---
> [Índice General](../README.md) · [← Ejercicio 071](../ejercicio_071/README.md) · [Ejercicio 073 →](../ejercicio_073/README.md)
