## Ejercicio 046 — Gestor de Proyectos con Ventana de Detalles de Tarea (`ProjectWorkspaceApp`)

> [Índice General](../README.md) · [← Ejercicio 045](../ejercicio_045/README.md) · [Ejercicio 047 →](../ejercicio_047/README.md)

### Contexto profesional
En agencias de diseño y firmas de consultoría, los directores de proyecto organizan las entregas mediante una estructura jerárquica de proyectos, fases y tareas.

### Usuario objetivo
Director de proyectos (Project Manager) o consultor líder.

### Problema
La falta de detalle en tableros planos dificulta registrar notas técnicas, impedimentos y avances específicos de cada tarea.

### Objetivo
Desarrollar un explorador de proyectos con `ttk.Treeview` en árbol jerárquico (Proyecto -> Fase -> Tarea), donde hacer doble clic en una tarea abra una ventana secundaria `Toplevel` con los detalles ampliados, bitácora de comentarios y selector de porcentaje de avance.

### Flujo principal
El director visualiza los proyectos y sus ramas en el árbol del Treeview. Al hacer doble clic sobre una tarea hoja, se abre una ventana `Toplevel` que muestra el título, responsable, fecha límite, barra de avance y un área de notas. El usuario actualiza el avance (ej. de 50% a 75%), agrega un comentario a la bitácora y guarda. El árbol principal actualiza el porcentaje de la tarea.

### Requisitos funcionales
- Visualización jerárquica en `ttk.Treeview` con carpetas y nodos hijos (Proyectos como nodos raíz, Fases como ramas, Tareas como hojas).
- Captura del evento de doble clic (`<Double-1>`) en el Treeview para abrir la ventana de detalles.
- Ventana `Toplevel` con detalles: Título, Responsable, Selector de avance porcentual (`Scale` de 0 a 100%), Historial de comentarios (`Text`).
- Guardado de notas y porcentaje actualizado.
- Actualización visual inmediata del árbol principal.

### Requisitos de interfaz
- Treeview con iconos o prefijos de texto que distingan proyectos de tareas (`[P]`, `[T]`).
- Ventana secundaria de detalles limpia con panel de bitácora.
- Barra inferior de estado con conteo de tareas completadas en el proyecto.

### Datos
- Estructura jerárquica de proyectos, fases y tareas con avances y listas de comentarios.

### Estado
- Árbol de proyectos en memoria.
- Tarea actualmente abierta en la ventana secundaria.

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- El doble clic solo debe abrir detalles si el nodo seleccionado es una tarea hoja (no un proyecto o fase raíz).

### Casos límite
- Doble clic en un espacio vacío de la tabla o en el encabezado.
- Modificar el avance y cerrar la ventana con la 'X' sin guardar (solicitar confirmación).

### Manejo de errores
- Ignorar silenciosamente eventos de doble clic sobre elementos que no representen tareas finales.

### Fundamentos de Python relacionados
- Estructuras de datos arbóreas y recursión simple para recorrer proyectos y tareas.
- Diccionarios anidados con listas de hijos.

### Conceptos Tkinter relacionados
- Creación de árboles jerárquicos en `ttk.Treeview` usando el parámetro `parent` en `.insert(parent_id, ...)`.
- Enlace del evento `<Double-Button-1>` en el Treeview.

### Herramientas para investigar
- Jerarquías y parámetro `parent` en `ttk.Treeview.insert()`.
- Evento `<Double-1>` de Tkinter.

### Diseño de interfaz
¿Cómo estructurarías visualmente la ventana de detalles para que el historial de comentarios sea legible y el control de avance fácil de ajustar?

### Diseño de variables
Usa nombres como `project_tree`, `task_detail_window`, `progress_scale`, `notes_text`, `save_task_btn`, `task_status_var`.

### Antes de programar
1. ¿Cómo se utiliza el parámetro `parent` de `tree.insert()` para anidar tareas dentro de proyectos en un Treeview?
2. ¿Cómo se determina si un ítem seleccionado en el Treeview tiene hijos o es un nodo hoja?

### Arquitectura
```
ejercicio_046/
├── app.py             # Árbol principal de proyectos y eventos
├── task_detail_dlg.py # Ventana Toplevel de detalle y notas
└── project_model.py   # Estructura jerárquica de proyectos y tareas
```

### Pruebas mínimas
1. Desplegar el árbol y hacer doble clic en una tarea -> La ventana de detalles debe abrirse con los datos de esa tarea específica.
2. Modificar el avance al 80% y guardar -> El árbol principal debe mostrar el nuevo porcentaje.

### Pruebas de error
1. Hacer doble clic en el nodo raíz de un proyecto -> No debe abrir la ventana de detalles de tarea.

### Experiencia de usuario
El árbol debe permitir expandir y colapsar ramas suavemente con clics en los indicadores estándar.

### Explicación posterior
¿Cómo gestiona `ttk.Treeview` la relación padre-hijo para renderizar estructuras en árbol jerárquico?

### Aplicación profesional
Herramientas de gestión de proyectos, exploradores de tareas corporativas y planificadores de ingeniería.

### Reto adicional
Calcula automáticamente el avance promedio del proyecto en el nodo raíz a partir de los porcentajes de sus tareas hijas.

---
> [Índice General](../README.md) · [← Ejercicio 045](../ejercicio_045/README.md) · [Ejercicio 047 →](../ejercicio_047/README.md)
