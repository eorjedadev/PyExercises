## Ejercicio 063 — Analizador de Archivos CSV Masivos con Cálculos Estadísticos (`CsvCruncherApp`)

> [Índice General](../README.md) · [← Ejercicio 062](../ejercicio_062/README.md) · [Ejercicio 064 →](../ejercicio_064/README.md)

### Contexto profesional
En áreas de inteligencia de negocios (BI) y analítica de datos, los analistas abren archivos CSV con cientos de miles de registros para calcular métricas estadísticas (media, desviación estándar, percentiles).

### Usuario objetivo
Analista de datos o especialista en inteligencia de negocios.

### Problema
Calcular estadísticas descriptivas sobre archivos pesados en el hilo principal bloquea la aplicación por decenas de segundos, mostrando el mensaje 'No responde' del sistema operativo.

### Objetivo
Construir una herramienta de análisis de datos que cargue y procese archivos CSV masivos en un hilo secundario independiente con `threading`, mostrando una barra de progreso indeterminada durante el procesamiento y desplegando las métricas calculadas en la interfaz de forma no bloqueante.

### Flujo principal
El analista selecciona un archivo CSV grande con `filedialog`. Elige qué columna numérica desea analizar. Presiona 'Calcular Estadísticas'. La interfaz inicia una barra de progreso indeterminada (`mode='indeterminate'`). El hilo de fondo procesa los datos, calcula media, mediana, mínimo, máximo, desviación estándar y total de registros válidos. Al terminar, la cola envía los resultados y la interfaz muestra las métricas en un panel elegante.

### Requisitos funcionales
- Carga y lectura eficiente de archivos CSV grandes línea por línea.
- Selector de columna numérica detectada en los encabezados del CSV.
- Procesamiento matemático en hilo de fondo (`threading.Thread`).
- Cálculo de: Conteo de filas, Suma total, Media aritmética, Mediana, Mínimo, Máximo y Desviación estándar.
- Barra de progreso indeterminada activa durante el cálculo que se detiene al recibir los resultados.
- Comunicación no bloqueante mediante `queue.Queue` y sondeo con `after()`.

### Requisitos de interfaz
- Formulario superior para selección de archivo y columna.
- Barra de progreso indeterminada (`mode='indeterminate'`).
- Tarjetas o etiquetas destacadas con las métricas calculadas con formateo numérico claro.

### Datos
- Estadísticas resultantes: count, sum, mean, median, min, max, std_dev.

### Estado
- Estado del hilo de procesamiento (activo/inactivo).
- Cola de resultados.

### Persistencia
No requiere persistencia en disco (análisis en memoria de flujo).

### Validaciones
- Validar que la columna seleccionada contenga valores numéricos convertibles a float.
- Descartar o advertir filas con datos no numéricos o vacíos.

### Casos límite
- Archivo CSV con columnas que mezclan texto y números.
- Archivo con solo 1 fila (desviación estándar debe ser 0 o nula).
- Cerrar la ventana mientras el cálculo está en curso.

### Manejo de errores
- Ignorar de forma controlada filas con celdas vacías o corruptas llevando un contador de 'Filas omitidas'.

### Fundamentos de Python relacionados
- Módulo estándar `statistics` (`mean`, `median`, `stdev`).
- Procesamiento de archivos mediante generadores para minimizar el uso de memoria RAM.

### Conceptos Tkinter relacionados
- Widget `ttk.Progressbar` en modo indeterminado con métodos `.start(intervalo)` y `.stop()`.
- Desacoplamiento de cálculos pesados de la GUI.

### Herramientas para investigar
- Módulo `statistics` de la biblioteca estándar de Python.
- Modo indeterminado en `ttk.Progressbar`.

### Diseño de interfaz
¿Cómo asegurarías que el botón de cálculo se inhabilite durante el procesamiento para evitar que el usuario dispare múltiples hilos concurrentes idénticos?

### Diseño de variables
Usa nombres como `csv_path_entry`, `column_combo`, `compute_btn`, `crunch_progressbar`, `stats_cards_frame`, `mean_label`, `stats_queue`.

### Antes de programar
1. ¿Cómo se inicia y detiene una barra de progreso indeterminada en Tkinter con `.start()` y `.stop()`?
2. ¿Por qué es más eficiente procesar el CSV iterando línea a línea en vez de cargar todas las filas en una lista gigante en memoria?

### Arquitectura
```
ejercicio_063/
├── app.py           # Ventana gráfica y tarjetas de resultados
├── stat_worker.py   # Hilo de procesamiento estadístico en streaming
└── datos/
    └── dataset_pesado.csv # Muestra de dataset con miles de filas
```

### Pruebas mínimas
1. Procesar archivo de prueba sobre la columna 'Ventas' -> La barra debe animarse suavemente y, al terminar, mostrar la media, mediana y desviación estándar.
2. Mover la ventana durante el cálculo -> Comprobar que no se bloquee ni aparezca 'No responde'.

### Pruebas de error
1. Seleccionar una columna de texto puro y calcular -> El hilo debe capturar el error y notificar 'La columna no contiene valores numéricos válidos'.

### Experiencia de usuario
Durante el cálculo, el cursor puede cambiar a reloj de arena (`cursor='watch'`) y volver al cursor normal (`cursor=''`) al terminar.

### Explicación posterior
¿Cuándo resulta apropiado utilizar una barra de progreso indeterminada frente a una barra de progreso determinada en una aplicación de escritorio?

### Aplicación profesional
Herramientas de perfilado de datos para ingenieros de ETL, visores estadísticos de laboratorio y analítica local sin nube.

### Reto adicional
Añade el cálculo del percentil 25 (Q1) y percentil 75 (Q3) para mostrar el rango intercuartílico de los datos.

---
> [Índice General](../README.md) · [← Ejercicio 062](../ejercicio_062/README.md) · [Ejercicio 064 →](../ejercicio_064/README.md)
