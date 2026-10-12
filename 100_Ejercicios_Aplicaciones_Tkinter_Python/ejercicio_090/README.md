## Ejercicio 090 — Gestor de Tareas con Historial de Acciones y Deshacer (`UndoRedoTaskApp`)

> [Índice General](../README.md) · [← Ejercicio 089](../ejercicio_089/README.md) · [Ejercicio 091 →](../ejercicio_091/README.md)

### Contexto profesional
En procesadores de texto, editores de audio y herramientas de planificación, los usuarios exigen la capacidad de deshacer (`Ctrl+Z`) y rehacer (`Ctrl+Y`) acciones para recuperarse de eliminaciones o modificaciones accidentales.

### Usuario objetivo
Planificador de tareas o usuario corporativo de gestión.

### Problema
La falta de una pila de deshacer en aplicaciones de gestión obliga al usuario a reescribir manualmente tareas eliminadas o restaurar cambios por error.

### Objetivo
Desarrollar una aplicación de gestión de tareas con `ttk.Treeview` que implemente formalmente el Patrón Command con dos pilas (Pila de Deshacer / Undo y Pila de Rehacer / Redo), soportando operaciones reversibles de Creación, Edición, Cambio de Estado y Eliminación de tareas, con atajos de teclado estándar `Ctrl+Z` y `Ctrl+Y` y habilitación dinámica de botones de acción.

### Flujo principal
El usuario crea una tarea 'Elaborar reporte'. Presiona `Ctrl+Z` (Deshacer) y la tarea desaparece de la tabla. Presiona `Ctrl+Y` (Rehacer) y la tarea vuelve a crearse exactamente igual. Si elimina una tarea y se arrepiente, presiona 'Deshacer' y la tarea se restaura en su posición y estado original con todos sus datos intactos.

### Requisitos funcionales
- Implementación formal del Patrón Command: Interfaz base `Command` con métodos `execute()` y `undo()`.
- Comandos concretos reversibles: `AddTaskCommand`, `DeleteTaskCommand`, `UpdateTaskCommand`, `ChangeStateCommand`.
- Pila de Deshacer (`undo_stack`) y Pila de Rehacer (`redo_stack`).
- Al ejecutar una acción nueva, la pila de Redo debe vaciarse automáticamente.
- Botones 'Deshacer' y 'Rehacer' en la barra de herramientas que se habiliten (`state='normal'`) o deshabiliten (`state='disabled'`) según haya acciones disponibles en sus pilas.
- Enlace de atajos de teclado globales: `Ctrl+Z` para Deshacer y `Ctrl+Y` (o `Ctrl+Shift+Z`) para Rehacer.
- Visualización en `ttk.Treeview` de las tareas activas.

### Requisitos de interfaz
- Barra superior con botones 'Deshacer' y 'Rehacer' acompañados de iconos o texto descriptivo.
- Formulario rápido de creación y edición.
- `Treeview` central con doble barra de desplazamiento.
- Barra de estado que informe la última acción realizada (ej. 'Deshecho: Eliminación de tarea X').

### Datos
- Tarea: id, titulo, prioridad, estado.
- Comandos: objetos con el estado previo y posterior de la entidad modificada.

### Estado
- Pilas de comandos `undo_stack` y `redo_stack` en memoria.
- Tareas activas en el repositorio.

### Persistencia
No requiere persistencia en disco en esta fase (gestión de memoria de comandos).

### Validaciones
- No permitir ejecutar Deshacer si la pila de Undo está vacía.
- No permitir ejecutar Rehacer si la pila de Redo está vacía.

### Casos límite
- Ejecutar 20 acciones consecutivas y deshacerlas todas hasta el estado inicial vacío.
- Deshacer una acción y luego ejecutar una acción completamente nueva (la pila de Redo debe limpiarse).

### Manejo de errores
- Proteger las pilas contra excepciones de índice asegurando que cada comando contenga la copia profunda de los datos necesarios.

### Fundamentos de Python relacionados
- Patrón de diseño Command (Comando).
- Estructuras de datos tipo Pila (LIFO) utilizando listas estándar de Python (`append()`, `pop()`).
- Copia profunda de objetos con `copy.deepcopy` para guardar instantáneas de estado.

### Conceptos Tkinter relacionados
- Enlace de atajos globales multinivel con `root.bind_all('<Control-z>', ...)` y `<Control-y>`.
- Actualización dinámica de estados de botones de herramientas.

### Herramientas para investigar
- Patrón Command en el libro 'Design Patterns' (GoF).
- Módulo `copy` y función `copy.deepcopy()`.

### Diseño de interfaz
¿Cómo asegurarías que los botones 'Deshacer' y 'Rehacer' muestren en un tooltip o texto qué acción específica van a revertir (ej. 'Deshacer: Eliminar tarea')?

### Diseño de variables
Usa nombres como `command_manager`, `undo_btn`, `redo_btn`, `task_tree`, `undo_stack`, `redo_stack`, `last_action_status_label`.

### Antes de programar
1. ¿Por qué es fundamental vaciar la pila de Rehacer (`redo_stack.clear()`) en el momento exacto en que el usuario ejecuta una nueva acción tras haber deshecho una anterior?
2. ¿Por qué se debe usar `copy.deepcopy()` al capturar el estado anterior de un objeto para que no se modifique por referencia mutada?

### Arquitectura
```
ejercicio_090/
├── app.py             # Interfaz gráfica y enlace de atajos Ctrl+Z / Ctrl+Y
├── command_manager.py # Gestor de pilas de Undo/Redo y despacho de comandos
├── commands.py        # Clases de comando: AddCommand, DeleteCommand, EditCommand
└── task_model.py      # Entidad Tarea y repositorio en memoria
```

### Pruebas mínimas
1. Crear una tarea -> Presionar `Ctrl+Z` -> La tarea debe desaparecer y el botón Rehacer debe habilitarse.
2. Presionar `Ctrl+Y` -> La tarea debe reaparecer intacta en la tabla.

### Pruebas de error
1. Eliminar una tarea, presionar `Ctrl+Z` -> La tarea debe restaurarse en su misma posición con todos sus atributos intactos.

### Experiencia de usuario
La reversión de acciones debe ser imperceptible en tiempo y restaurar la selección adecuada en la tabla para no desorientar al usuario.

### Explicación posterior
¿Cómo garantiza el Patrón Command desacoplar las acciones que modifican el estado de la aplicación de la interfaz que solicita la reversión?

### Aplicación profesional
Editores gráficos, procesadores de datos empresariales, tableros de control y herramientas de modelado de software.

### Reto adicional
Añade un límite configurable a la pila de Undo (ej. recordar únicamente las últimas 25 acciones) para evitar consumo excesivo de memoria RAM.

---
> [Índice General](../README.md) · [← Ejercicio 089](../ejercicio_089/README.md) · [Ejercicio 091 →](../ejercicio_091/README.md)
