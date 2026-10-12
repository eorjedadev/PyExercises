## Ejercicio 075 — Diseñador de Croquis y Distribución de Mesas para Eventos (`FloorPlanDesignerApp`)

> [Índice General](../README.md) · [← Ejercicio 074](../ejercicio_074/README.md) · [Ejercicio 076 →](../ejercicio_076/README.md)

### Contexto profesional
En hoteles, salones de convenciones y banquetes de bodas, los coordinadores de eventos diseñan la distribución espacial de mesas y sillas según la capacidad del recinto.

### Usuario objetivo
Coordinador de eventos o maître de sala de banquetes.

### Problema
Dibujar planos en papel o no respetar las dimensiones de paso provoca saturación del salón, bloqueo de salidas de emergencia e incomodidad para los comensales.

### Objetivo
Construir una herramienta de diseño de planos de distribución de salón con `Canvas`, que permita colocar mesas redondas y rectangulares con capacidad de comensales, moverlas libremente con el ratón, rotar o cambiar el tamaño de la mesa seleccionada, calcular la capacidad total de asientos del salón y exportar la distribución a un archivo `plano_evento.json`.

### Flujo principal
El coordinador hace clic en 'Añadir Mesa Redonda' o 'Añadir Mesa Rectangular'. El elemento aparece en el centro del plano. El usuario arrastra las mesas para distribuirlas armónicamente en el salón. Al seleccionar una mesa, un panel lateral permite cambiar su etiqueta (ej. 'Mesa 1'), su capacidad de personas (ej. 8 comensales) o eliminarla. El panel inferior calcula el número total de mesas y la capacidad total de invitados en tiempo real.

### Requisitos funcionales
- Widget `Canvas` con cuadrícula de referencia cuadriculada (grid de 20x20 píxeles).
- Creación de dos tipos de mesas: Redondas (`create_oval`) y Rectangulares (`create_rectangle`) con etiqueta de número y sillas representadas visualmente.
- Arrastre interactivo de mesas con el ratón (`<Button-1>`, `<B1-Motion>`).
- Opción de ajuste magnético a la cuadrícula ('Snap to Grid') opcional para alineación perfecta.
- Panel de propiedades para la mesa seleccionada: Número de Mesa, Capacidad de Sillas, Tipo.
- Cálculo automático continuo: Total de Mesas en Sala y Capacidad Total de Asientos.
- Guardado y carga del plano en archivo JSON (`datos/plano_evento.json`).

### Requisitos de interfaz
- Barra superior de herramientas (Añadir Redonda, Añadir Rectangular, Snap to Grid, Guardar Plano).
- Área central con el lienzo del plano de salón amplio con barras de desplazamiento.
- Panel lateral derecho con las propiedades de la mesa seleccionada.
- Barra inferior con el conteo de aforo consolidado.

### Datos
- Mesa: id, tipo ('redonda'|'rectangular'), x, y, ancho, alto, etiqueta, capacidad_sillas.

### Estado
- Lista de mesas activas en el plano.
- Mesa actualmente seleccionada.
- Estado del ajuste magnético ('snap to grid').

### Persistencia
Archivo JSON (`datos/plano_evento.json`).

### Validaciones
- No permitir capacidades de sillas menores a 1.
- Etiqueta de mesa obligatoria.

### Casos límite
- Intentar arrastrar una mesa fuera de los límites del lienzo.
- Cargar un archivo JSON de plano que contiene mesas fuera de escala.

### Manejo de errores
- Manejar la carga de archivos JSON asegurando que las coordenadas numéricas sean válidas.

### Fundamentos de Python relacionados
- Serialización y deserialización de estructuras gráficas a diccionarios JSON.
- Algoritmo de ajuste magnético a cuadrícula: $x_{snap} = \text{round}(x / 20) \times 20$.

### Conceptos Tkinter relacionados
- Manipulación de múltiples elementos agrupados en `Canvas`.
- Implementación de barras de desplazamiento bidireccionales en `Canvas` usando el parámetro `scrollregion`.
- Deselección de elementos al hacer clic en el fondo.

### Herramientas para investigar
- Parámetro `scrollregion` en `tkinter.Canvas`.
- Algoritmo de 'Snap to Grid' en interfaces de diseño gráfico.

### Diseño de interfaz
¿Cómo diseñarías el fondo del Canvas para que la cuadrícula de referencia sea visible pero lo suficientemente tenue para no estorbar la lectura de las mesas?

### Diseño de variables
Usa nombres como `floor_canvas`, `add_round_table_btn`, `add_rect_table_btn`, `snap_grid_check`, `selected_table_entry`, `capacity_spinbox`, `total_guests_label`.

### Antes de programar
1. ¿Cómo se implementa la fórmula matemática de 'Snap to Grid' para redondear las coordenadas del ratón al múltiplo más cercano del tamaño de celda?
2. ¿Cómo se configura `canvas.config(scrollregion=...)` para que las barras de desplazamiento funcionen correctamente en un lienzo de grandes dimensiones?

### Arquitectura
```
ejercicio_075/
├── app.py             # Interfaz del diseñador, herramientas y Canvas
├── table_element.py   # Clase gráfica para renderizar y mover mesas en Canvas
├── floor_storage.py   # Guardado y carga del plano en formato JSON
└── datos/
    └── plano_evento.json # Archivo de persistencia del diseño de sala
```

### Pruebas mínimas
1. Añadir una mesa redonda de 8 sillas y una rectangular de 10 sillas -> Comprobar que la capacidad total marque 18 invitados.
2. Arrastrar las mesas por el lienzo -> Las mesas deben moverse fluidamente junto con sus etiquetas de texto.
3. Guardar en JSON y reiniciar la app -> El plano debe recargarse en las posiciones y capacidades exactas.

### Pruebas de error
1. Intentar poner capacidad 0 en una mesa -> Debe rechazar el valor exigiendo al menos 1 comensal.

### Experiencia de usuario
La mesa seleccionada debe destacarse con un contorno de selección azul o guiones punteados para indicar claramente que está activa para edición.

### Explicación posterior
¿Cómo se estructuran los datos de un diseño gráfico en el widget `Canvas` para permitir su serialización limpia a un archivo JSON estándar?

### Aplicación profesional
Planificadores de salones de eventos, diseño de plantas arquitectónicas simples, distribución de oficinas y software de gestión de restaurantes.

### Reto adicional
Añade una validación visual que detecte colisiones entre mesas (si dos mesas se solapan en sus coordenadas) y las pinte de color ámbar de advertencia.

---
> [Índice General](../README.md) · [← Ejercicio 074](../ejercicio_074/README.md) · [Ejercicio 076 →](../ejercicio_076/README.md)
