## Ejercicio 073 — Generador Interactivo de Diagramas de Flujo y Nodos (`NodeGraphEditorApp`)

> [Índice General](../README.md) · [← Ejercicio 072](../ejercicio_072/README.md) · [Ejercicio 074 →](../ejercicio_074/README.md)

### Contexto profesional
En diseño de procesos industriales y flujos de trabajo de automatización, los ingenieros modelan diagramas de estados y diagramas de flujo interactivos arrastrando y conectando bloques visuales.

### Usuario objetivo
Ingeniero de procesos, diseñador de flujos o analista de automatización.

### Problema
El uso de herramientas de dibujo genéricas no permite interactuar con bloques como entidades individuales con propiedades y conexiones estructuradas.

### Objetivo
Desarrollar un editor interactivo de nodos visuales utilizando el widget `Canvas` de Tkinter, que permita crear nodos rectangulares con texto, arrastrarlos libremente por el lienzo con el ratón (`<B1-Motion>`), conectar dos nodos mediante una línea de enlace que se actualice dinámicamente al moverlos, y eliminar nodos seleccionados con la tecla `Supr`.

### Flujo principal
El usuario hace clic en el botón 'Crear Nodo' y hace clic en el Canvas para colocar un bloque rotulado. Puede hacer clic sobre cualquier nodo para seleccionarlo y arrastrarlo por el lienzo; el bloque se mueve suavemente siguiendo el cursor. Puede presionar 'Conectar' y seleccionar dos nodos consecutivos para dibujar una línea que los una. Al mover cualquiera de los dos nodos conectados, la línea se recalcula automáticamente.

### Requisitos funcionales
- Widget `Canvas` interactivo con dimensiones amplias y cuadrícula sutil de fondo.
- Creación de nodos gráficos: rectángulos con texto centrado creados mediante `canvas.create_rectangle` y `canvas.create_text`.
- Arrastre interactivo de nodos: enlace de eventos de ratón `<Button-1>`, `<B1-Motion>` y `<ButtonRelease-1>`.
- Sistema de conexiones: dibujo de líneas de enlace entre nodos mediante `canvas.create_line` con flechas direccionales (`arrow='last'`).
- Actualización dinámica de coordenadas de las líneas conectadas conforme los nodos son desplazados.
- Selección y eliminación de nodo y sus líneas conectadas mediante la tecla `Delete` o botón de interfaz.
- Botón para limpiar todo el lienzo con confirmación previa.

### Requisitos de interfaz
- Barra superior de herramientas: 'Crear Nodo', 'Conectar Nodos', 'Eliminar Seleccionado', 'Limpiar Lienzo'.
- Área central ocupada por el widget `Canvas` con fondo claro o cuadrícula.
- Barra de estado que indique 'Nodo seleccionado: X' o 'Modo: Conexión'.

### Datos
- Nodo: id_rect, id_texto, etiqueta, x, y, ancho, alto.
- Conexión: id_linea, nodo_origen_id, nodo_destino_id.

### Estado
- Diccionario de nodos activos y sus identificadores de Canvas.
- Lista de conexiones activas.
- Nodo actualmente seleccionado o en arrastre.
- Modo activo ('Normal', 'Conectando').

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- No permitir conectar un nodo consigo mismo.
- Al arrastrar un nodo, mantenerlo dentro de los límites visibles del Canvas.

### Casos límite
- Mover un nodo rápidamente hacia los bordes del Canvas.
- Eliminar un nodo que tiene múltiples líneas conectadas (todas sus conexiones asociadas deben destruirse limpiamente).
- Hacer clic en el fondo vacío del Canvas (debe deseleccionar el nodo activo).

### Manejo de errores
- Controlar referencias de identificadores de Canvas para evitar manipular elementos ya destruidos.

### Fundamentos de Python relacionados
- Programación orientada a objetos para encapsular la entidad `Node` y sus métodos de movimiento.
- Aritmética de coordenadas cartesianas $(x, y)$ y cálculo de puntos medios.

### Conceptos Tkinter relacionados
- Widget `Canvas` y métodos `.create_rectangle()`, `.create_text()`, `.create_line()`, `.coords()`, `.delete()`, `.find_withtag()`.
- Enlace de eventos de ratón con coordenadas de evento (`event.x`, `event.y`).
- Agrupación de elementos gráficos de Canvas mediante tags comunes.

### Herramientas para investigar
- Métodos de manipulación de elementos en `tkinter.Canvas` (`coords`, `move`, `delete`).
- Manejo de coordenadas y eventos de arrastre (`<B1-Motion>`).

### Diseño de interfaz
¿Cómo indicarías visualmente al usuario qué nodo está actualmente seleccionado (ej. cambiando el color de su borde o agregando un contorno más grueso)?

### Diseño de variables
Usa nombres como `diagram_canvas`, `add_node_btn`, `connect_nodes_btn`, `delete_btn`, `active_node_id`, `drag_start_coords`, `nodes_registry`.

### Antes de programar
1. ¿Cómo se agrupan el rectángulo y el texto de un nodo usando el mismo tag de Canvas para mover ambos elementos simultáneamente con `canvas.move(tag, dx, dy)`?
2. ¿Cómo se recalculan las coordenadas de inicio y fin de una línea cuando uno de los dos nodos conectados se mueve?

### Arquitectura
```
ejercicio_073/
├── app.py           # Ventana gráfica, barra de herramientas y Canvas
├── node_model.py    # Clase lógica para representar nodos y sus geometrías
└── graph_manager.py # Control de conexiones, arrastre y actualización de líneas
```

### Pruebas mínimas
1. Crear dos nodos y arrastrar uno por el lienzo -> Debe desplazarse fluidamente siguiendo el puntero del ratón.
2. Conectar ambos nodos con una línea y mover uno de ellos -> La línea debe permanecer unida a los nodos recalculando sus coordenadas en tiempo real.

### Pruebas de error
1. Eliminar un nodo conectado -> La línea de enlace asociada debe eliminarse automáticamente del Canvas sin dejar líneas huérfanas.

### Experiencia de usuario
El arrastre debe responder de manera instantánea a 60 FPS sin retraso visual respecto al cursor.

### Explicación posterior
¿Cómo funciona el sistema de identificación y coordenadas de elementos gráficos en el widget `Canvas` de Tkinter para manipular gráficos interactivos?

### Aplicación profesional
Editores de diagramas de flujo de procesos, modeladores de máquinas de estado, diseñadores de esquemas de pipelines y herramientas pedagógicas de algoritmos.

### Reto adicional
Añade una opción para exportar la disposición del diagrama (posiciones de nodos y lista de conexiones) a un archivo `diagrama.json` para persistencia.

---
> [Índice General](../README.md) · [← Ejercicio 072](../ejercicio_072/README.md) · [Ejercicio 074 →](../ejercicio_074/README.md)
