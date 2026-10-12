## Ejercicio 079 — Visor de Tarjetas Kanban con Columnas Arrastrables o Interactivas (`MiniKanbanBoardApp`)

> [Índice General](../README.md) · [← Ejercicio 078](../ejercicio_078/README.md) · [Ejercicio 080 →](../ejercicio_080/README.md)

### Contexto profesional
En equipos de desarrollo ágil y gestión operativa de tareas, los líderes de proyecto coordinan el flujo de trabajo mediante tableros visuales Kanban organizados en columnas de estado.

### Usuario objetivo
Scrum Master, líder técnico o coordinador de operaciones.

### Problema
Las listas tabulares planas no transmiten con suficiente claridad el volumen de trabajo en progreso (WIP) ni los cuellos de botella entre etapas.

### Objetivo
Desarrollar un tablero visual Kanban interactivo con tres columnas fijas ('Por Hacer', 'En Curso', 'Terminado') construidas con contenedores `Frame` o `Canvas`, donde cada tarjeta sea un componente compuesto con título, prioridad, responsable y botones de acción rápida para mover la tarjeta a la columna adyacente izquierda o derecha, calculando el conteo de ítems por columna y persistiendo en `kanban.json`.

### Flujo principal
El usuario crea una nueva tarjeta mediante un botón superior. La tarjeta aparece en la columna 'Por Hacer'. Al hacer clic en el botón 'Mover a la Derecha' (`->`) de la tarjeta, esta desaparece de 'Por Hacer' y se reconstruye fluidamente en 'En Curso'. El usuario puede arrastrar o transicionar la tarjeta hasta 'Terminado'. El conteo de tareas de cada columna se actualiza de inmediato y los cambios se guardan en el archivo JSON.

### Requisitos funcionales
- Tablero con tres columnas visuales: 'Por Hacer', 'En Curso' y 'Terminado'.
- Componente de tarjeta compuesto: Título, Descripción corta, Responsable, Etiqueta de prioridad (Baja, Media, Alta con colores) y botones de movimiento (`<-` y `->`).
- Formulario modal o barra superior para crear nuevas tarjetas.
- Movimiento fluido de tarjetas entre columnas adyacentes.
- Acción para eliminar una tarjeta con confirmación.
- Conteo dinámico de tareas en el encabezado de cada columna (ej. 'En Curso (3)').
- Persistencia automática de las tarjetas y sus columnas en `datos/kanban.json`.

### Requisitos de interfaz
- Columnas claramente diferenciadas con fondo ligeramente contrastado y bordes redondeados o limpios.
- Área de cada columna con capacidad de scroll vertical si hay muchas tarjetas.
- Tarjetas con apariencia de post-it digital con relieve (`relief='raised'` o borde sutil).

### Datos
- Tarjeta Kanban: id, titulo, descripcion, responsable, prioridad, columna ('todo'|'in_progress'|'done').

### Estado
- Lista de tarjetas en memoria organizadas por columna.
- Tablero activo.

### Persistencia
Archivo JSON (`datos/kanban.json`).

### Validaciones
- Título de tarjeta obligatorio (al menos 3 caracteres).
- Las tarjetas no pueden moverse más allá de los extremos (el botón izquierdo está deshabilitado en 'Por Hacer' y el derecho en 'Terminado').

### Casos límite
- Columna completamente vacía (debe mostrar un mensaje tenue de 'Sin tareas en esta etapa').
- Tarjetas con descripciones largas (deben ajustarse automáticamente con `wraplength`).

### Manejo de errores
- Manejar la persistencia en JSON de forma segura tras cada movimiento de tarjeta.

### Fundamentos de Python relacionados
- Programación orientada a objetos: clase `KanbanCard` derivada de `ttk.Frame` o encapsulada.
- Filtrado y agrupación de diccionarios por clave de columna.

### Conceptos Tkinter relacionados
- Composición de componentes personalizados reutilizables en Tkinter.
- Reorganización dinámica de widgets hijos dentro de contenedores usando gestores de geometría.

### Herramientas para investigar
- Patrón de componentes compuestos en Tkinter (subclases de `Frame`).
- Parámetro `wraplength` en widgets `Label`.

### Diseño de interfaz
¿Cómo asegurarías que las tres columnas se mantengan con anchos idénticos y se expandan armónicamente si la ventana se amplía?

### Diseño de variables
Usa nombres como `todo_column_frame`, `progress_column_frame`, `done_column_frame`, `add_card_btn`, `new_card_modal`, `kanban_storage`.

### Antes de programar
1. ¿Cómo se diseña una clase `KanbanCard` que herede de `ttk.Frame` y encapsule sus propios botones de movimiento emitiendo eventos al tablero padre?
2. ¿Cómo se implementa el scroll independiente en cada una de las tres columnas si contienen muchas tarjetas?

### Arquitectura
```
ejercicio_079/
├── app.py             # Ventana principal y layout de tres columnas
├── kanban_card.py     # Clase componente para la tarjeta visual interactiva
├── column_view.py     # Contenedor de columna con scroll y encabezado dinámico
└── datos/
    └── kanban.json    # Archivo de persistencia del tablero
```

### Pruebas mínimas
1. Crear una tarjeta en 'Por Hacer' -> Moverla a 'En Curso' -> El contador de 'Por Hacer' debe decrecer en 1 y el de 'En Curso' aumentar en 1.
2. Reiniciar la app -> La tarjeta debe permanecer en la columna 'En Curso' desde el archivo JSON.

### Pruebas de error
1. En una tarjeta ubicada en 'Terminado', comprobar que el botón de avanzar a la derecha esté inhabilitado o no exista.

### Experiencia de usuario
Las tarjetas deben tener un padding cómodo y una sombra visual sutil para facilitar la lectura del tablero completo.

### Explicación posterior
¿Cómo facilita la creación de clases derivadas de `ttk.Frame` la modularización y reutilización de componentes visuales complejos en interfaces de escritorio?

### Aplicación profesional
Herramientas de gestión de tareas ágiles, tableros de control de despacho de órdenes y seguimiento de incidencias operativas.

### Reto adicional
Añade un límite de WIP (Work in Progress) configurable para la columna 'En Curso' que alerte en color rojo si se tienen más de 3 tarjetas simultáneas.

---
> [Índice General](../README.md) · [← Ejercicio 078](../ejercicio_078/README.md) · [Ejercicio 080 →](../ejercicio_080/README.md)
