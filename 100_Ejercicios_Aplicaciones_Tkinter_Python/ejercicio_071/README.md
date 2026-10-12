## Ejercicio 071 — Convertidor Masivo de Codificación de Archivos (ANSI a UTF-8) (`EncodingConverterApp`)

> [Índice General](../README.md) · [← Ejercicio 070](../ejercicio_070/README.md) · [Ejercicio 072 →](../ejercicio_072/README.md)

### Contexto profesional
En proyectos de migración de sistemas heredados (legacy) y modernización de código, los equipos de desarrollo reciben carpetas con miles de archivos de código fuente guardados en codificaciones antiguas (Latin-1, CP1252, Windows-ANSI) que deben migrarse a UTF-8 estándar.

### Usuario objetivo
Desarrollador de software o ingeniero de migración de datos.

### Problema
Convertir codificaciones de texto en archivos masivos mediante scripts mal gestionados congela la máquina y puede corromper caracteres especiales con tildes o eñes si la detección de codificación es errónea.

### Objetivo
Desarrollar una aplicación de conversión masiva de codificación de archivos que procese carpetas en segundo plano con `threading`, detecte o permita seleccionar la codificación de origen (CP1252, ISO-8859-1, ANSI), convierta los archivos a UTF-8 limpio sin BOM, muestre una barra de progreso en vivo y reporte un log de conversiones exitosas y fallidas.

### Flujo principal
El usuario selecciona la carpeta con los archivos legacy. Elige la codificación origen esperada (ej. `cp1252`) y la extensión de los archivos a procesar (ej. `.py`, `.c`, `.txt`, `.sql`). Presiona 'Iniciar Conversión'. El hilo secundario procesa cada archivo, lee los bytes, decodifica con la codificación elegida y reescribe el archivo codificado en `utf-8`. La barra de progreso avanza en tiempo real y la tabla lista los archivos convertidos y el número de caracteres transformados.

### Requisitos funcionales
- Selección de carpeta de origen con `filedialog.askdirectory`.
- Selector de codificación de origen (`Combobox`: `cp1252`, `iso-8859-1`, `latin-1`, `mac_roman`).
- Filtro por extensiones de archivo a convertir.
- Conversión de codificación ejecutada en hilo secundario (`threading.Thread`).
- Opción para generar respaldo (`.bak`) de cada archivo antes de sobreescribirlo.
- Barra de progreso determinada que indique el avance del lote.
- Visualización en `ttk.Treeview`: Archivo, Codificación Origen, Estado ('Convertido', 'Omitido', 'Error'), Tamaño.
- Botón de cancelación del proceso en cualquier momento.

### Requisitos de interfaz
- Formulario superior ordenado con selectores de codificación y extensiones.
- `Treeview` de resultados con tags de colores.
- Barra de progreso y panel inferior con el recuento final de archivos transformados.

### Datos
- Ficha de conversión: ruta_archivo, encoding_origen, encoding_destino, estado, bytes_convertidos.

### Estado
- Hilo de conversión activo.
- Cola de eventos thread-safe.

### Persistencia
Modificación y sobreescritura de archivos de texto en disco con nueva codificación.

### Validaciones
- Verificar que la codificación de origen seleccionada sea un códec válido en Python.
- Asegurar que solo se procesen archivos de texto que coincidan con la extensión seleccionada.

### Casos límite
- Archivo que ya está en UTF-8 y se intenta decodificar como CP1252 (debe manejarse con cuidado o verificar si ya es UTF-8 válido).
- Archivos con permisos de solo lectura (`PermissionError`).
- Cancelar la conversión a medio camino.

### Manejo de errores
- Capturar `UnicodeDecodeError` si un archivo no coincide con la codificación de origen seleccionada y reportarlo como 'Error de Códec' sin colapsar el resto.

### Fundamentos de Python relacionados
- Manejo de codificaciones y códecs estándar en Python (`codecs`, `encoding='utf-8'`).
- Manejo de excepciones de codificación (`UnicodeDecodeError`, `UnicodeEncodeError`).
- Creación de copias de respaldo con `shutil.copy2`.

### Conceptos Tkinter relacionados
- Coordinación de tareas pesadas de modificación de archivos con interfaces gráficas.
- Desacoplamiento de operaciones de entrada/salida de disco.

### Herramientas para investigar
- Códecs estándar de Python (documentación oficial de `codecs`).
- Manejo de archivos de texto y creación de respaldos con `shutil`.

### Diseño de interfaz
¿Cómo asegurarías que la casilla 'Crear copia de respaldo .bak' esté visible y marcada por defecto para evitar pérdidas accidentales de datos?

### Diseño de variables
Usa nombres como `enc_source_combo`, `ext_filter_entry`, `backup_check_var`, `convert_btn`, `cancel_btn`, `progress_bar`, `results_tree`, `convert_queue`.

### Antes de programar
1. ¿Cuál es la diferencia técnica entre `iso-8859-1` y `cp1252` en el manejo de caracteres especiales como el símbolo de euro o comillas tipográficas?
2. ¿Cómo se lee un archivo en una codificación y se escribe en otra de forma segura utilizando bloques `with open(...)`?

### Arquitectura
```
ejercicio_071/
├── app.py             # Formulario de configuración, barra y tabla de archivos
├── converter_worker.py # Hilo de lectura y sobreescritura segura en disco
└── backup_helper.py   # Creación de respaldos .bak y validaciones de rutas
```

### Pruebas mínimas
1. Crear un archivo en CP1252 con caracteres 'canción' y 'año' -> Convertir a UTF-8 -> Abrir el archivo y verificar que los acentos se lean perfectamente en UTF-8.
2. Activar opción de respaldo -> Verificar que se cree el archivo `.bak` intacto antes de la sobreescritura.

### Pruebas de error
1. Intentar decodificar un archivo binario o con códec incompatible -> Debe registrar 'Error de Decodificación' en la tabla y continuar con los demás.

### Experiencia de usuario
La tabla debe ir mostrando cada archivo en cuanto termina de ser procesado para que el usuario observe el avance progresivo.

### Explicación posterior
¿Cómo garantiza la separación en hilos que operaciones lentas de lectura y escritura masiva en disco no bloqueen la interfaz de usuario de Tkinter?

### Aplicación profesional
Herramientas de migración de bases de código legacy, procesadores de transcripciones internacionales y sanitizadores de datos para pipelines de ML.

### Reto adicional
Añade una rutina heurística preliminar que intente detectar automáticamente si el archivo ya era UTF-8 válido antes de intentar reconvertirlo.

---
> [Índice General](../README.md) · [← Ejercicio 070](../ejercicio_070/README.md) · [Ejercicio 072 →](../ejercicio_072/README.md)
