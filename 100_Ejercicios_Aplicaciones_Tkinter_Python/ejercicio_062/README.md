## Ejercicio 062 — Procesador Masivo de Renombrado de Archivos por Lotes (`BatchFileRenamerApp`)

> [Índice General](../README.md) · [← Ejercicio 061](../ejercicio_061/README.md) · [Ejercicio 063 →](../ejercicio_063/README.md)

### Contexto profesional
En agencias de fotografía digital y digitalización de documentos jurídicos, los archivistas reciben carpetas con cientos de imágenes con nombres crudos de cámara (`IMG_001.JPG`) y necesitan renombrarlas según reglas estructuradas.

### Usuario objetivo
Archivista digital o fotógrafo profesional.

### Problema
Renombrar cientos de archivos en el hilo de interfaz congela el explorador e impide cancelar el proceso si el usuario advierte un error a medio camino.

### Objetivo
Desarrollar una aplicación de renombrado masivo de archivos con `threading`, barra de progreso determinada (`ttk.Progressbar`), previsualización de nombres antes de ejecutar y botón de cancelación segura de la operación.

### Flujo principal
El archivista selecciona una carpeta con `filedialog.askdirectory`. La tabla lista los archivos encontrados. Define la regla de renombrado (Prefijo, Contador secuencial de dígitos, Sufijo, Extensión). Puede presionar 'Previsualizar' para ver cómo quedarán los nombres en una columna adyacente. Al presionar 'Ejecutar Renombrado', un hilo secundario procesa los archivos uno a uno actualizando la barra de progreso de 0% a 100%. Si presiona 'Cancelar', el proceso se detiene en el siguiente archivo.

### Requisitos funcionales
- Selección de carpeta de origen mediante `filedialog`.
- Generación de previsualización en `ttk.Treeview`: Nombre Original vs Nombre Nuevo proyectado.
- Reglas de nombrado configurables: Prefijo de texto, Número inicial, Relleno de ceros (ej. 3 dígitos: 001, 002), Sufijo.
- Procesamiento en hilo de fondo (`threading.Thread`) usando `os.rename` o `pathlib.Path.rename`.
- Barra de progreso determinada (`ttk.Progressbar`) que refleje el avance porcentual exacto.
- Botón de 'Cancelar' que interrumpa el ciclo del hilo de forma controlada.
- Comunicación de progreso mediante `queue.Queue`.

### Requisitos de interfaz
- Cuadrícula superior para configuración de la regla de renombrado.
- `Treeview` amplio con dos columnas comparativas (Antes / Después).
- Panel inferior con la barra de progreso, porcentaje numérico y botones de ejecución/cancelación.

### Datos
- Archivo a renombrar: ruta_original, nombre_original, nombre_nuevo, estado.

### Estado
- Lista de archivos en memoria.
- Bandera booleana de cancelación (`threading.Event`).
- Contador de archivos procesados.

### Persistencia
Modificación directa en el sistema de archivos local.

### Validaciones
- Verificar que la carpeta tenga archivos regulares para procesar.
- Comprobar que la regla de nuevo nombre no genere colisiones (dos archivos con el mismo nombre nuevo).

### Casos límite
- Intentar renombrar a un nombre de archivo que ya existe en la misma carpeta.
- Presionar cancelar en el primer 5% del proceso.
- Archivos protegidos contra escritura o abiertos por otro programa (`PermissionError`).

### Manejo de errores
- Capturar `FileExistsError` y `PermissionError` en el hilo de fondo y notificar el fallo específico en la cola sin abortar el resto de la cola.

### Fundamentos de Python relacionados
- Módulo `pathlib.Path` y métodos `.rename()`.
- Formateo de números con relleno de ceros (`f'{numero:0{padding}d}'`).
- Banderas de parada entre hilos (`threading.Event`).

### Conceptos Tkinter relacionados
- Widget `ttk.Progressbar` en modo determinado (`mode='determinate'`).
- Enlace de cancelación mediante eventos de hilos.
- Comunicación thread-safe con `queue.Queue`.

### Herramientas para investigar
- Clase `ttk.Progressbar` y propiedades `maximum`, `value`.
- Método `pathlib.Path.rename()` y manejo de colisiones de archivos.

### Diseño de interfaz
¿Cómo asegurarías que el botón 'Cancelar' esté habilitado únicamente mientras el proceso de renombrado esté corriendo en segundo plano?

### Diseño de variables
Usa nombres como `rename_tree`, `prefix_entry`, `start_num_entry`, `padding_spinbox`, `progress_bar`, `run_btn`, `cancel_btn`, `cancel_event`.

### Antes de programar
1. ¿Cómo se previene el riesgo de sobreescritura accidental si dos archivos proyectan el mismo nombre nuevo antes de iniciar el renombrado real?
2. ¿Cómo verifica el hilo trabajador periódicamente si la bandera `cancel_event.is_set()` ha sido activada por el usuario?

### Arquitectura
```
ejercicio_062/
├── app.py           # Interfaz gráfica, controles y barra de progreso
├── rename_worker.py # Hilo de renombrado en disco y despacho por colas
└── rule_builder.py  # Lógica pura de proyección y validación de nombres
```

### Pruebas mínimas
1. Cargar carpeta con 20 archivos de prueba -> Previsualizar con prefijo 'DOC_' -> Comprobar que la columna proyectada muestre 'DOC_001.txt', 'DOC_002.txt', etc.
2. Ejecutar renombrado -> Comprobar que la barra avance hasta el 100% y los archivos se renombren físicamente en disco.

### Pruebas de error
1. Presionar 'Cancelar' a mitad del proceso -> Comprobar que el hilo se detenga limpiamente y la interfaz informe cuántos archivos quedaron sin procesar.

### Experiencia de usuario
La barra de progreso debe avanzar de forma suave y mostrar una etiqueta adyacente con 'Procesando X de Y (Z%)'.

### Explicación posterior
¿Cómo se coordina una bandera `threading.Event` para permitir la cancelación segura de una tarea larga sin terminar abruptamente el proceso?

### Aplicación profesional
Herramientas de organización de activos digitales en agencias creativas, ingestión de documentos jurídicos y ordenamiento de fotografías.

### Reto adicional
Añade una opción para 'Revertir Último Renombrado' (Undo) guardando un registro en memoria de los nombres anteriores para restaurarlos si el usuario lo solicita.

---
> [Índice General](../README.md) · [← Ejercicio 061](../ejercicio_061/README.md) · [Ejercicio 063 →](../ejercicio_063/README.md)
