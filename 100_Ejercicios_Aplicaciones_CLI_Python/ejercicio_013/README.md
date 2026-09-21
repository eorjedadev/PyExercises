## Ejercicio 013 — Visualizador de Tablas ASCII/Markdown (`tab-view`)

> [← Ejercicio 012](../ejercicio_012/README.md) · [Índice General](../README.md) · [Ejercicio 014 →](../ejercicio_014/README.md)

### Contexto profesional
Al consultar reportes tabulares o volcados CSV en servidores remotos vía SSH sin entorno gráfico, es indispensable visualizar la información en tablas legibles con anchos de columna autoajustables y estilos intercambiables (Markdown, Grid ASCII, Unicode).

### Problema
Construir una CLI que reciba un archivo CSV/TSV o lea desde STDIN y renderice una tabla alineada, calculando el ancho máximo de cada columna y truncando celdas excesivamente largas si se define un límite.

### Usuario objetivo
Administradores de sistemas, desarrolladores y analistas de datos.

### Objetivo
Diseñar un motor de renderizado tabular para terminal con cálculo dinámico de dimensiones y soporte de estilos.

### Ejemplo conceptual de uso
```bash
# Renderizar un archivo CSV con estilo grid
python tab_view.py datos/ventas.csv --style grid

# Recibir datos desde un pipe y limitar ancho de columnas a 20 caracteres
cat datos/reporte.tsv | python tab_view.py --delimiter "\t" --max-width 20 --style markdown
```

### Requisitos funcionales
- Leer datos tabulares desde archivo o `sys.stdin`.
- Detectar o configurar delimitador de columnas (coma, tabulador, pipe, punto y coma).
- Calcular anchos máximos de columnas según contenido y cabeceras.
- Estilos de renderizado: `simple`, `grid` (ASCII `+---+`), `markdown` (`|---|`) y `plain`.
- Truncado inteligente de celdas con elipses (`...`) si exceden `--max-width`.
- Alineación: texto a la izquierda, números a la derecha.

### Requisitos de CLI
- Argumento posicional opcional: archivo de datos (lee STDIN si se omite).
- Opción `-d / --delimiter`: delimitador (default `,`).
- Opción `-s / --style`: `simple`, `grid`, `markdown`, `plain` (default `grid`).
- Opción `-w / --max-width`: entero positivo para ancho máximo por columna.
- Flag `--no-header`: trata la primera fila como datos regulares.
- Exit code 0 en éxito, 1 en datos corruptos, 2 en argumentos inválidos.

### Entradas
- Archivo tabular o flujo STDIN.
- Parámetros de estilo y delimitación.

### Salidas
- Tabla formateada en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Validar que el archivo o flujo contenga al menos una fila.
- Validar que el estilo seleccionado esté entre las opciones permitidas.
- Comprobar que `--max-width` sea mayor o igual a 4 si se especifica.

### Casos límite
- Filas con diferente número de columnas (rellenar celdas vacías).
- Celdas con caracteres de ancho cero o emojis (manejo de longitud visual).
- Flujo STDIN vacío.

### Manejo de errores
- `csv.Error` en datos mal formados.
- Captura de `BrokenPipeError` si el visor (ej. `less`) se cierra antes de terminar de emitir.

### Fundamentos de Python relacionados
- Módulo `csv`.
- Formateo avanzado de strings (`str.ljust()`, `str.rjust()`, especificadores de formato f-string).
- Módulo `sys` y detección de `sys.stdin.isatty()`.

### Conceptos CLI relacionados
- Detección de terminal interactiva (TTY) vs tubería (pipe).
- Manejo de señales de salida estándar.

### Herramientas o módulos para investigar
- `csv`.
- `sys.stdin`.
- `argparse`.

### Diseño de comandos
¿Cómo permitirías ordenar las filas por una columna específica antes de renderizar (`--sort-by COL`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para mostrar número de fila en la primera columna (`--line-numbers`)?

### Diseño de variables
`column_widths`, `header_row`, `data_rows`, `table_style`, `cell_content`, `truncated_cell`.

### Antes de programar
1. ¿Cómo calcular el ancho visual de una columna considerando tanto la cabecera como todas las filas de datos?
2. ¿Cómo diseñar bordes decorativos sin duplicar código para cada estilo?

### Arquitectura
Módulo lector (`reader.py`), módulo formateador (`formatter.py`) y CLI (`tab_view.py`).

### Pruebas mínimas
1. Renderizar un CSV de prueba con 3 columnas en modo `markdown` y validar la sintaxis de cabecera `|---|`.
2. Pasar datos por pipe `echo "a,b\n1,2" | python tab_view.py` y verificar la tabla generada.

### Pruebas de error
1. Pasar `--style desconocido` -> Exit code 2.

### Experiencia de usuario
La tabla debe lucir perfectamente alineada, sin descuadrar columnas ni desbordar la terminal.

### Explicación posterior
Explica cómo detectar si la entrada proviene de un archivo o de una tubería (`sys.stdin.isatty()`).

### Aplicación profesional
Componente fundamental en herramientas de monitorización, clientes CLI de bases de datos y utilidades de auditoría.

### Reto adicional
Implementar paginación automática en terminal usando el paginador del sistema (`less` o `more`) cuando la tabla supere el alto de la ventana.

---
> [← Ejercicio 012](../ejercicio_012/README.md) · [Índice General](../README.md) · [Ejercicio 014 →](../ejercicio_014/README.md)
