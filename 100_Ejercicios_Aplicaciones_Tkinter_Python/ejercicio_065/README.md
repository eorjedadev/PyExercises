## Ejercicio 065 — Buscador Rápido de Texto dentro de Archivos (`DesktopFileGrepApp`)

> [Índice General](../README.md) · [← Ejercicio 064](../ejercicio_064/README.md) · [Ejercicio 066 →](../ejercicio_066/README.md)

### Contexto profesional
En auditorías de código fuente y análisis forense de sistemas, los desarrolladores buscan cadenas específicas (ej. nombres de variables, tokens de API o palabras clave) dentro de miles de archivos de texto en un directorio.

### Usuario objetivo
Desarrollador de software, auditor forense o analista de seguridad.

### Problema
El buscador integrado del explorador de archivos es lento y buscar mediante scripts sincrónicos congela la interfaz gráfica durante el recorrido de árboles de carpetas profundos.

### Objetivo
Desarrollar una herramienta de búsqueda recursiva de texto en archivos locales (tipo 'grep' de escritorio) con `threading`, que recorra carpetas en segundo plano e inserte de manera fluida y en tiempo real las coincidencias encontradas en un `ttk.Treeview` (Ruta, Número de Línea, Fragmento de Texto Coincidente) sin congelar la ventana.

### Flujo principal
El usuario selecciona una carpeta con `filedialog`, ingresa la palabra o texto a buscar y puede marcar la opción 'Distinguir Mayúsculas' o filtrar por extensión (ej. `.py`, `.txt`, `.log`). Presiona 'Buscar'. Un hilo de fondo recorre los archivos recursivamente. Conforme encuentra líneas coincidentes, las envía a la cola y la tabla las muestra de inmediato en vivo. Un botón 'Detener Búsqueda' permite parar la exploración en cualquier momento.

### Requisitos funcionales
- Selección de carpeta raíz de búsqueda mediante `filedialog`.
- Entrada de texto para la cadena buscada y opciones: Sensible a Mayúsculas (`Checkbutton`), Extensión de archivo (`Combobox` o `Entry`).
- Búsqueda recursiva en segundo plano utilizando `os.walk` o `pathlib.Path.rglob`.
- Despacho inmediato de cada coincidencia encontrada a través de `queue.Queue`.
- Visualización en `ttk.Treeview`: Archivo (nombre relativo), Línea, Texto Coincidente.
- Barra de estado con: Archivos examinados y total de coincidencias encontradas.
- Botón para cancelar o detener la búsqueda en cualquier instante.

### Requisitos de interfaz
- Panel superior compacto para la configuración de búsqueda.
- `Treeview` central amplio con doble barra de desplazamiento.
- Barra inferior con indicador animado o contador dinámico de archivos escaneados.

### Datos
- Coincidencia: archivo_ruta, numero_linea (int), linea_texto (str).

### Estado
- Hilo de búsqueda activo.
- Bandera de interrupción (`threading.Event`).
- Cola de coincidencias.

### Persistencia
No requiere persistencia en disco (exploración en tiempo real).

### Validaciones
- Cadena de búsqueda obligatoria (al menos 2 caracteres).
- Carpeta seleccionada debe existir.

### Casos límite
- Archivos binarios o imágenes (deben detectarse y omitirse sin intentar decodificarlos como texto UTF-8).
- Directorios con permisos denegados (`PermissionError`).
- Búsqueda que arroja más de 10,000 coincidencias (limitar o paginar para no saturar memoria de la GUI).

### Manejo de errores
- Capturar `UnicodeDecodeError` silenciosamente para omitir archivos no textuales sin detener la búsqueda.

### Fundamentos de Python relacionados
- Recorrido recursivo con `pathlib.Path.rglob` o `os.walk`.
- Lectura línea por línea con enumerate (`enumerate(archivo, start=1)`).
- Banderas de parada con `threading.Event`.

### Conceptos Tkinter relacionados
- Inserción en tiempo real de lotes de datos en `ttk.Treeview` mediante sondeos periódicos con `after()`.
- Control de concurrencia y cancelación interactiva.

### Herramientas para investigar
- Métodos de recorrido de carpetas en `pathlib.Path`.
- Detección de archivos de texto frente a binarios en Python.

### Diseño de interfaz
¿Cómo estructurarías las columnas del Treeview para que la columna de fragmento de texto ocupe la mayor parte del espacio horizontal de la ventana?

### Diseño de variables
Usa nombres como `results_tree`, `search_term_entry`, `case_sensitive_check`, `start_search_btn`, `stop_search_btn`, `files_scanned_label`, `grep_queue`.

### Antes de programar
1. ¿Cómo se ignoran archivos binarios de forma segura evitando que `UnicodeDecodeError` interrumpa el escaneo del directorio?
2. ¿Cómo se insertan elementos en el Treeview en pequeños lotes desde la cola para mantener la fluidez de 60 FPS en la interfaz?

### Arquitectura
```
ejercicio_065/
├── app.py           # Visor gráfico, controles y Treeview de coincidencias
├── grep_worker.py   # Hilo de escaneo recursivo y emisor por cola
└── file_filter.py   # Detección de extensiones y archivos de texto plano
```

### Pruebas mínimas
1. Buscar la palabra 'def ' en una carpeta con scripts `.py` -> Las coincidencias deben aparecer de forma fluida en la tabla indicando el archivo y número de línea.
2. Presionar 'Detener Búsqueda' -> El escaneo debe detenerse de inmediato y reflejar el total parcial.

### Pruebas de error
1. Escanear una carpeta que contenga archivos `.png` o `.exe` -> Debe omitirlos limpiamente sin arrojar errores de decodificación.

### Experiencia de usuario
Al hacer doble clic en una fila del Treeview, se podría mostrar una ventana emergente con el bloque de líneas circundantes para dar contexto.

### Explicación posterior
¿Cómo se gestiona el flujo de inserción continua en la GUI cuando un hilo trabajador produce cientos de resultados por segundo?

### Aplicación profesional
Buscadores de código fuente para programadores, herramientas de análisis de logs para ciberseguridad y utilidades forenses locales.

### Reto adicional
Añade soporte para buscar mediante expresiones regulares (`regex`) marcando una casilla opcional en la barra de herramientas.

---
> [Índice General](../README.md) · [← Ejercicio 064](../ejercicio_064/README.md) · [Ejercicio 066 →](../ejercicio_066/README.md)
