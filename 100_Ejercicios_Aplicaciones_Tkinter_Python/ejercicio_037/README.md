## Ejercicio 037 — Editor de Texto Plano con Menús y Diálogos de Archivo (`MiniNotepadApp`)

> [Índice General](../README.md) · [← Ejercicio 036](../ejercicio_036/README.md) · [Ejercicio 038 →](../ejercicio_038/README.md)

### Contexto profesional
En estaciones de trabajo técnicas y entornos de desarrollo, los programadores requieren editores de texto ligeros para modificar archivos de configuración (`.ini`, `.yaml`, `.txt`) con controles completos de menú.

### Usuario objetivo
Desarrollador, administrador de sistemas o redactor técnico.

### Problema
La falta de menús estándar y atajos de teclado reconocibles (`Ctrl+O`, `Ctrl+S`) en herramientas caseras ocasiona descontento y pérdida de archivos no guardados.

### Objetivo
Desarrollar un editor de texto plano con barra de menú completa (`Menu`), atajos de teclado globales, diálogos estándar de archivo (Abrir, Guardar, Guardar Como), detección de cambios no guardados e interceptor del cierre de ventana.

### Flujo principal
El usuario abre la aplicación y redacta texto. Puede usar el menú 'Archivo > Abrir' (`Ctrl+O`) para cargar un archivo existente, o 'Archivo > Guardar' (`Ctrl+S`) para guardar los cambios. Si el archivo es nuevo, se solicita nombre con `filedialog.asksaveasfilename`. Si intenta salir con cambios pendientes, se abre un diálogo preguntando si desea guardar antes de salir.

### Requisitos funcionales
- Barra de menú principal con menús: 'Archivo' (Nuevo, Abrir, Guardar, Guardar Como, Salir), 'Edición' (Deshacer, Rehacer, Cortar, Copiar, Pegar, Seleccionar Todo) y 'Ayuda' (Acerca de).
- Atajos de teclado enlazados: `Ctrl+N`, `Ctrl+O`, `Ctrl+S`, `Ctrl+Q`.
- Detección de cambios mediante bandera `is_dirty`.
- Título de ventana dinámico que muestre el nombre del archivo actual y un asterisco `*` si hay cambios sin guardar.
- Intercepción del cierre de ventana (`WM_DELETE_WINDOW`) para prevenir pérdida de datos.

### Requisitos de interfaz
- Widget `Text` expandible al 100% del área de la ventana con barra de desplazamiento vertical.
- Barra de estado inferior que muestre la línea y columna actual del cursor y la codificación (UTF-8).
- Barra de menú nativa y consistente.

### Datos
- Contenido del documento: texto multilínea.
- Ruta del archivo actual: objeto `pathlib.Path` o `None` si es nuevo.

### Estado
- Ruta del archivo abierto actualmente.
- Bandera booleana de modificaciones pendientes (`is_dirty`).

### Persistencia
Lectura y escritura directa en archivos de texto plano en disco con codificación UTF-8.

### Validaciones
- Validar permisos de escritura antes de intentar guardar en la ruta destino.

### Casos límite
- Intentar abrir un archivo binario o con codificación incompatible.
- El usuario cancela el diálogo de 'Guardar Como' (no debe marcarse como guardado ni perder la ruta anterior).
- Cerrar la ventana con el archivo vacío vs con cambios sin guardar.

### Manejo de errores
- Capturar `UnicodeDecodeError` y notificar que el archivo no tiene codificación de texto compatible.
- Manejar `PermissionError` al intentar guardar en carpetas protegidas del sistema.

### Fundamentos de Python relacionados
- Manejo de archivos con codificación explícita (`encoding='utf-8'`).
- Manejo de rutas y estados nulos con `pathlib.Path`.

### Conceptos Tkinter relacionados
- Creación de barras de menú con `tk.Menu` y cascadas (`add_cascade`, `add_command`, `add_separator`).
- Enlace de atajos globales con `root.bind_all('<Control-s>', ...)`.
- Actualización de título de ventana con `root.title()`.
- Eventos de cursor de texto `<KeyRelease>` y `<ButtonRelease-1>` para actualizar línea y columna.

### Herramientas para investigar
- Clase `tk.Menu` de Tkinter.
- Índice `'insert'` en widgets `Text` para obtener coordenadas de línea y columna (`text.index(tk.INSERT)`).

### Diseño de interfaz
¿Cómo asegurarías que el widget Text ocupe todo el espacio de la ventana y la barra de estado permanezca anclada en la parte inferior?

### Diseño de variables
Usa nombres como `editor_text`, `main_menu`, `file_menu`, `edit_menu`, `current_file_path`, `is_modified_flag`, `status_bar_label`.

### Antes de programar
1. ¿Cómo se construye una barra de menús multinivel en Tkinter usando `root.config(menu=barra_menu)`?
2. ¿Cómo se obtiene la línea y columna actual del cursor en un widget `Text` para mostrarlas en la barra de estado?

### Arquitectura
```
ejercicio_037/
├── app.py           # Editor gráfico, menú y enlaces de eventos
└── file_manager.py  # Operaciones de lectura y escritura segura en disco
```

### Pruebas mínimas
1. Redactar texto, presionar `Ctrl+S` -> Debe abrir 'Guardar Como', permitir guardar y actualizar el título de la ventana.
2. Escribir más texto -> El título debe mostrar el asterisco `*` indicando cambios pendientes.

### Pruebas de error
1. Con cambios no guardados, hacer clic en la 'X' de la ventana -> Debe aparecer el diálogo con opciones Guardar, No Guardar y Cancelar.

### Experiencia de usuario
La experiencia de escritura debe sentirse ágil, con soporte para atajos universales de portapapeles y navegación estándar.

### Explicación posterior
¿Cómo se coordina el protocolo `WM_DELETE_WINDOW` con los menús de archivo para centralizar la confirmación de guardado?

### Aplicación profesional
Editores ligeros de scripts embebidos en aplicaciones de escritorio, visores de notas y consolas de configuración.

### Reto adicional
Añade en el menú de Edición la opción 'Buscar y Reemplazar' que abra una ventana secundaria pequeña para sustituir texto.

---
> [Índice General](../README.md) · [← Ejercicio 036](../ejercicio_036/README.md) · [Ejercicio 038 →](../ejercicio_038/README.md)
