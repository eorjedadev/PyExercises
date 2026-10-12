## Ejercicio 027 — Gestor de Tareas Pendientes con Prioridades (`TaskMasterApp`)

> [Índice General](../README.md) · [← Ejercicio 026](../ejercicio_026/README.md) · [Ejercicio 028 →](../ejercicio_028/README.md)

### Contexto profesional
En oficinas de proyectos y equipos de desarrollo ágil, los líderes de equipo gestionan una lista diaria de tareas asignadas con prioridades y fechas límite.

### Usuario objetivo
Líder de proyecto o coordinador operativo.

### Problema
El seguimiento de tareas en notas sueltas provoca retrasos en entregables críticos y falta de visibilidad del estado de avance.

### Objetivo
Construir una aplicación de tareas con `ttk.Treeview` que soporte prioridades (Alta, Media, Baja), cambio de estado con un clic (Pendiente, En Curso, Completada), filtrado por estado y persistencia estructurada en un archivo `tareas.json`.

### Flujo principal
El usuario visualiza sus tareas organizadas en una tabla. Puede registrar una nueva tarea indicando título, responsable, fecha límite y prioridad. Seleccionando una tarea, puede pulsar 'Avanzar Estado' para transicionar de Pendiente a En Curso y a Completada. Los datos se sincronizan automáticamente en `tareas.json`.

### Requisitos funcionales
- Carga y guardado en archivo `tareas.json` estructurado con indentación legible.
- Columnas en tabla: ID, Título, Responsable, Prioridad, Estado, Fecha Límite.
- Formulario de alta de tareas con validación de campos obligatorios.
- Botón para avanzar el estado del ítem seleccionado.
- Filtro por estado (`Combobox`: Todas, Pendientes, En Curso, Completadas).
- Botón de eliminación de tarea con confirmación modal.

### Requisitos de interfaz
- Treeview con estilos o etiquetas visuales para identificar tareas con prioridad 'Alta' (resaltadas en color ámbar o rojo).
- Barra de herramientas superior con botones de acción rápida.
- Panel inferior con contador de tareas completadas vs pendientes.

### Datos
- Tarea: ID (`str`), Título (`str`), Responsable (`str`), Prioridad (`str`), Estado (`str`), Fecha (`str`).
- Archivo de almacenamiento: JSON.

### Estado
- Lista de diccionarios de tareas en memoria.
- Filtro activo seleccionado.

### Persistencia
Archivo JSON (`datos/tareas.json`).

### Validaciones
- Título de tarea no puede estar vacío y debe tener al menos 5 caracteres.
- Responsable es obligatorio.
- Fecha límite debe tener formato ISO válido.

### Casos límite
- Archivo `tareas.json` inexistente o corrupto (inicializar con lista vacía).
- Filtrar por un estado que no tiene tareas (mostrar tabla vacía sin fallos).
- Avanzar el estado de una tarea que ya está 'Completada' (mantenerla en Completada o reiniciar).

### Manejo de errores
- Manejar `json.JSONDecodeError` si el archivo está dañado ofreciendo crear uno nuevo o cargar respaldo.

### Fundamentos de Python relacionados
- Módulo estándar `json` (`json.load`, `json.dump` con `indent=4`).
- Modelado de estados mediante máquinas de estado simples (`dict` de transiciones).

### Conceptos Tkinter relacionados
- Tags de filas en `ttk.Treeview` (`tree.tag_configure('alta_prioridad', background=...)`).
- Sincronización entre modelo de datos y vista.

### Herramientas para investigar
- Módulo `json` de Python.
- Método `tree.tag_configure()` y `tree.item(..., tags=...)` en `ttk.Treeview`.

### Diseño de interfaz
¿Cómo estructurarías las etiquetas o tags cromáticos en el Treeview para que las prioridades altas resalten sin dificultar la lectura del texto?

### Diseño de variables
Usa nombres como `tasks_tree`, `task_title_entry`, `assignee_entry`, `priority_combo`, `status_filter_combo`, `advance_status_btn`.

### Antes de programar
1. ¿Por qué el formato JSON es preferible a CSV para entidades con estados mutables y campos estructurados?
2. ¿Cómo se implementa la lógica de transición cíclica de estados (`Pendiente -> En Curso -> Completada`)?

### Arquitectura
```
ejercicio_027/
├── app.py           # Vistas, Treeview y acciones de usuario
├── task_service.py  # Lógica de estados y filtrado en memoria
├── json_storage.py  # Serialización y deserialización JSON
└── datos/
    └── tareas.json  # Archivo de persistencia de datos
```

### Pruebas mínimas
1. Registrar tarea con prioridad Alta -> Comprobar que aparezca en el Treeview con su tag cromático.
2. Presionar 'Avanzar Estado' en una tarea 'Pendiente' -> Comprobar que cambie a 'En Curso' y se guarde en el JSON.

### Pruebas de error
1. Intentar avanzar estado sin seleccionar fila -> Debe mostrar aviso 'Seleccione una tarea para modificar'.

### Experiencia de usuario
Al cambiar de estado, la selección del ítem en la tabla debe mantenerse activa para que el usuario no pierda su lugar.

### Explicación posterior
¿Cómo se utilizan los tags en un `ttk.Treeview` para aplicar estilos visuales condicionales a filas específicas?

### Aplicación profesional
Tableros operativos de supervisión de proyectos, sistemas de seguimiento de órdenes de trabajo y gestores personales de productividad.

### Reto adicional
Añade una opción de búsqueda por palabra clave en el título que funcione conjuntamente con el filtro de estado seleccionado.

---
> [Índice General](../README.md) · [← Ejercicio 026](../ejercicio_026/README.md) · [Ejercicio 028 →](../ejercicio_028/README.md)
