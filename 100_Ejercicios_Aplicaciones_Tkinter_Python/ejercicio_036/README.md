## Ejercicio 036 — Visor de Metadatos de Archivos en Directorio (`DirectoryMetadataViewerApp`)

> [Índice General](../README.md) · [← Ejercicio 035](../ejercicio_035/README.md) · [Ejercicio 037 →](../ejercicio_037/README.md)

### Contexto profesional
En auditorías de seguridad y administración de servidores de almacenamiento (NAS), los administradores inspeccionan carpetas compartidas para identificar archivos antiguos o de peso excesivo.

### Usuario objetivo
Administrador de sistemas o auditor de almacenamiento.

### Problema
El explorador nativo del sistema no ofrece ordenamiento avanzado ni filtros combinados por tamaño y extensión para auditar carpetas masivas de forma rápida.

### Objetivo
Construir una herramienta de inspección de directorios que permita elegir una carpeta mediante `filedialog.askdirectory`, liste todos los archivos en un `ttk.Treeview` con metadatos (Nombre, Extensión, Tamaño formateado en KB/MB, Fecha de Modificación), y permita filtrar por extensión y peso mínimo.

### Flujo principal
El usuario presiona 'Seleccionar Carpeta' y elige un directorio local. La aplicación escanea los archivos no recursivamente y los despliega en el `Treeview`. El usuario puede filtrar por extensión (ej. `.pdf`, `.mp4`) o ingresar un umbral de tamaño mínimo (ej. mayores a 10 MB). El panel inferior calcula el tamaño total consumido por los archivos listados.

### Requisitos funcionales
- Selección de carpeta local mediante `filedialog.askdirectory`.
- Escaneo de archivos del directorio seleccionado utilizando `pathlib` u `os.scandir`.
- Columnas en Treeview: Nombre, Extensión, Tamaño (formateado en B, KB, MB, GB), Tamaño en Bytes (para ordenamiento), Última Modificación (YYYY-MM-DD HH:MM).
- Filtro por extensión de archivo (`Combobox` con extensiones detectadas en la carpeta).
- Filtro por tamaño mínimo en MB.
- Cálculo de total de archivos y espacio acumulado en disco de la selección.

### Requisitos de interfaz
- Botón superior de selección de carpeta y barra que muestre la ruta seleccionada.
- Controles de filtrado por extensión y tamaño organizados en fila horizontal.
- `ttk.Treeview` amplio con scrollbar vertical.
- Barra inferior con el peso total formateado.

### Datos
- Archivo metadatos: nombre, extensión, tamaño_bytes, tamaño_humano, fecha_modificacion.

### Estado
- Ruta de la carpeta activa.
- Lista completa de metadatos de archivos del directorio actual en memoria.

### Persistencia
No requiere persistencia en disco; opera sobre el sistema de archivos en tiempo real.

### Validaciones
- Verificar que la carpeta seleccionada exista y se tengan permisos de lectura.
- Manejar carpetas con miles de archivos sin bloquear la creación de la interfaz.

### Casos límite
- Carpeta vacía o sin archivos regulares (solo subcarpetas).
- Archivos de 0 bytes o archivos de sistema sin permisos de lectura de metadatos (`PermissionError`).
- Cancelar el diálogo de selección de carpeta.

### Manejo de errores
- Capturar `PermissionError` al intentar leer metadatos de archivos restringidos y marcarlos con estado 'Sin Acceso'.

### Fundamentos de Python relacionados
- Módulo `pathlib.Path` y `os.stat`.
- Conversión de timestamps POSIX (`stat.st_mtime`) a formato legible con `datetime.fromtimestamp`.
- Función para convertir bytes a magnitudes legibles (KB, MB, GB).

### Conceptos Tkinter relacionados
- Diálogo `filedialog.askdirectory`.
- Población eficiente de datos en `ttk.Treeview`.
- Ordenamiento de columnas numéricas usando el valor en bytes oculto.

### Herramientas para investigar
- Función `filedialog.askdirectory`.
- Módulo `pathlib.Path` y métodos `.is_file()`, `.stat()`, `.suffix`.

### Diseño de interfaz
¿Cómo dispondrías la ruta del directorio seleccionado para que no deforme la ventana si la ruta tiene 200 caracteres de largo?

### Diseño de variables
Usa nombres como `files_tree`, `select_dir_btn`, `dir_path_label`, `ext_filter_combo`, `min_size_entry`, `total_space_label`.

### Antes de programar
1. ¿Cómo se formatea un número de bytes (ej. 15,485,760 B) a una cadena legible como `'14.77 MB'`?
2. ¿Cómo se convierte el timestamp retornado por `path.stat().st_mtime` a una fecha y hora estándar?

### Arquitectura
```
ejercicio_036/
├── app.py           # Explorador gráfico y Treeview
└── scanner_core.py  # Escaneo de rutas, extracción de metadatos y filtros
```

### Pruebas mínimas
1. Seleccionar una carpeta con archivos -> Verificar que la tabla liste los nombres, extensiones, pesos legibles y fechas.
2. Filtrar por extensión `.txt` -> Verificar que la tabla muestre únicamente archivos de texto y actualice el tamaño acumulado.

### Pruebas de error
1. Cancelar el diálogo de selección -> La interfaz debe mantener su estado previo sin lanzar errores.

### Experiencia de usuario
La ruta seleccionada debe mostrarse truncada o en una etiqueta con desplazamiento si es muy larga.

### Explicación posterior
¿Cómo se optimiza la inspección de metadatos en disco usando `os.scandir` o `pathlib` frente a listar solo nombres con `os.listdir`?

### Aplicación profesional
Herramientas de auditoría de almacenamiento para administradores de sistemas, limpiadores de archivos temporales y organizadores de descargas.

### Reto adicional
Añade un botón 'Abrir en Explorador del Sistema' que abra la carpeta seleccionada en el explorador nativo de archivos (Explorer en Windows o xdg-open en Linux).

---
> [Índice General](../README.md) · [← Ejercicio 035](../ejercicio_035/README.md) · [Ejercicio 037 →](../ejercicio_037/README.md)
