## Ejercicio 069 — Limpiador de Duplicados en Carpetas con Cancelación (`DuplicateCleanerApp`)

> [Índice General](../README.md) · [← Ejercicio 068](../ejercicio_068/README.md) · [Ejercicio 070 →](../ejercicio_070/README.md)

### Contexto profesional
En servidores de archivos compartidos y almacenamiento de marketing, los analistas de TI identifican y eliminan copias duplicadas de archivos multimedia para recuperar espacio en disco.

### Usuario objetivo
Administrador de sistemas o gestor de almacenamiento.

### Problema
Escanear miles de archivos para detectar duplicados por contenido consume varios minutos y puede congelar la interfaz, además de ser peligroso si no se permite cancelar antes de ejecutar borrados accidentales.

### Objetivo
Desarrollar una aplicación de detección y limpieza de archivos duplicados con `threading`, que realice el escaneo por hash MD5/SHA-256 en segundo plano, muestre una barra de progreso durante la búsqueda, liste los grupos de archivos duplicados en un `ttk.Treeview` con casillas de selección, y permita eliminar las copias redundantes con confirmación formal.

### Flujo principal
El usuario selecciona una carpeta para auditar y presiona 'Escanear Duplicados'. Un hilo trabajador agrupa los archivos por tamaño y luego calcula sus hashes para confirmar duplicados reales. La interfaz muestra el progreso en vivo. Al terminar, la tabla agrupa los duplicados. El usuario marca cuáles copias desea borrar y presiona 'Eliminar Seleccionados', liberando espacio en disco de forma segura.

### Requisitos funcionales
- Selección de directorio a auditar mediante `filedialog`.
- Escaneo de dos fases en hilo secundario: Fase 1 (Agrupación rápida por tamaño en bytes) y Fase 2 (Comparación por hash de los archivos con tamaño coincidente).
- Visualización en `ttk.Treeview` agrupando los duplicados con indicador de cuál es el archivo original y cuáles las copias.
- Casilla o selección de archivos a eliminar.
- Botón de 'Cancelar Escaneo' que detenga la búsqueda en cualquier instante mediante una bandera `threading.Event`.
- Eliminación segura de archivos seleccionados con confirmación modal y cálculo del espacio total recuperado.

### Requisitos de interfaz
- Barra superior con selector de carpeta y botones 'Escanear' y 'Cancelar'.
- Barra de progreso que refleje el avance del escaneo.
- `Treeview` organizado con sangría o tags que diferencien originales de copias redundantes.
- Panel inferior con el espacio en disco que se recuperará (en MB/GB).

### Datos
- Archivo duplicado: ruta, tamano_bytes, hash, es_original (bool), seleccionado_borrar (bool).

### Estado
- Hilo de escaneo activo.
- Grupos de duplicados detectados en memoria.
- Espacio recuperable calculado.

### Persistencia
Eliminación directa de archivos redundantes en el sistema de archivos.

### Validaciones
- Verificar que al menos una copia del archivo original permanezca sin marcar para borrado (evitar eliminar todas las instancias de un archivo).
- Confirmación explícita con advertencia antes de proceder al borrado físico de archivos.

### Casos límite
- Archivos de tamaño idéntico pero contenido diferente (el hash evita falsos positivos).
- Archivos en uso que no se pueden eliminar (`PermissionError`).
- Cancelar el escaneo a medio camino.

### Manejo de errores
- Manejar excepciones de eliminación de archivos reportando qué archivos no pudieron borrarse por estar en uso o bloqueados.

### Fundamentos de Python relacionados
- Optimización de algoritmos de detección: agrupar primero por tamaño (`os.path.getsize`) antes de calcular hashes costosos de CPU.
- Módulos `os`, `send2trash` (o `os.remove`) y `hashlib`.

### Conceptos Tkinter relacionados
- Presentación de datos agrupados en `ttk.Treeview`.
- Cancelación segura de hilos mediante `threading.Event` y colas.

### Herramientas para investigar
- Algoritmo de dos fases para detección de duplicados (tamaño primero, hash después).
- Uso de `threading.Event` para cancelación cooperativa de bucles.

### Diseño de interfaz
¿Cómo diseñarías la vista para que el usuario nunca cometa el error de borrar por accidente el archivo original junto con las copias?

### Diseño de variables
Usa nombres como `duplicates_tree`, `scan_btn`, `cancel_scan_btn`, `delete_copies_btn`, `space_reclaimed_label`, `scan_progress_bar`, `scan_queue`.

### Antes de programar
1. ¿Por qué comparar primero el tamaño de los archivos antes de calcular hashes reduce drásticamente el tiempo de escaneo en carpetas masivas?
2. ¿Cómo se protege al usuario para que la interfaz nunca permita marcar para eliminación la copia designada como original?

### Arquitectura
```
ejercicio_069/
├── app.py             # Visor de duplicados, controles y barra de progreso
├── dedup_scanner.py   # Hilo de escaneo de dos fases (tamaño + hash)
└── safe_deleter.py    # Lógica de eliminación y cálculo de espacio recuperado
```

### Pruebas mínimas
1. Crear una carpeta con 3 archivos idénticos -> Escanear -> Debe agruparlos correctamente identificando 1 original y 2 duplicados.
2. Seleccionar 1 duplicado y eliminar -> Comprobar que se elimine físicamente del disco y se actualice el espacio recuperado.

### Pruebas de error
1. Intentar marcar todas las copias de un archivo para borrar -> Debe bloquear la selección indicando que debe conservarse al menos una copia original.

### Experiencia de usuario
El total de espacio que se recuperará debe actualizarse en tiempo real conforme el usuario marca o desmarca casillas en la tabla.

### Explicación posterior
¿Cómo optimiza la estrategia de filtrado previo por tamaño de archivo la velocidad de detección de duplicados frente a calcular hashes sobre todo el directorio?

### Aplicación profesional
Herramientas de optimización de almacenamiento en servidores de archivos corporativos, gestores de bibliotecas multimedia y utilidades de limpieza de disco.

### Reto adicional
Añade una opción para mover los duplicados a una 'Carpeta de Cuarentena' en lugar de eliminarlos permanentemente de forma inmediata.

---
> [Índice General](../README.md) · [← Ejercicio 068](../ejercicio_068/README.md) · [Ejercicio 070 →](../ejercicio_070/README.md)
