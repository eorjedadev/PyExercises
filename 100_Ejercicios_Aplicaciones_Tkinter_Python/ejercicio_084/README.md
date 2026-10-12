## Ejercicio 084 — Generador de Gráficos Circulares (Pastel/Torta) en Canvas (`PieChartRendererApp`)

> [Índice General](../README.md) · [← Ejercicio 083](../ejercicio_083/README.md) · [Ejercicio 085 →](../ejercicio_085/README.md)

### Contexto profesional
En sistemas de control presupuestario y resúmenes ejecutivos sin dependencias externas, los analistas representan la distribución porcentual de participaciones de mercado o desglose de gastos en gráficos de pastel nativos.

### Usuario objetivo
Analista financiero o gestor de presupuestos.

### Problema
La falta de gráficos circulares nativos en Tkinter obliga a desarrolladores a depender de paquetes de terceros pesados que complican la distribución multiplataforma.

### Objetivo
Desarrollar un componente de gráfico circular (Pie Chart) dibujado desde cero en `Canvas` de Tkinter, que reciba un conjunto de categorías y montos, calcule los ángulos trigonométricos proporcionales ($0^\circ$ a $360^\circ$), dibuje los arcos con `canvas.create_arc`, genere una leyenda con los colores y porcentajes y resalte una porción (efecto 'explode') al hacer clic sobre ella.

### Flujo principal
El usuario ingresa categorías y sus valores (ej. Marketing: $400, Nómina: $800, Servidores: $300). Presiona 'Generar Gráfica'. La aplicación calcula la suma total, obtiene los ángulos de cada rebanada y dibuja los arcos con colores vivos en el `Canvas`. Al lado derecho se despliega la leyenda de colores con sus porcentajes. Al hacer clic sobre cualquier rebanada del pastel, esta se desplaza ligeramente hacia afuera (efecto explode) destacando su porción.

### Requisitos funcionales
- Entrada y edición de categorías con montos numéricos.
- Cálculo de proporción porcentual y ángulo en grados: $\text{Ángulo} = \frac{\text{Monto}}{\text{Total}} \times 360^\circ$.
- Dibujo de los sectores circulares en `Canvas` mediante `canvas.create_arc(..., start=angulo_ini, extent=angulo_extension, fill=color)`.
- Generación de paleta de colores armónica para las rebanadas.
- Panel lateral de leyenda con cuadros de muestra de color, nombre de categoría y porcentaje desglosado.
- Interactividad: clic sobre una porción de pastel para separarla ligeramente del centro (efecto explode) y mostrar sus datos exactos.

### Requisitos de interfaz
- Disposición de dos paneles: formulario y tabla de datos a la izquierda, `Canvas` con el pastel y su leyenda a la derecha.
- Gráfico de pastel centrado con dimensiones generosas (al menos 300x300 píxeles).
- Leyenda con colores coincidentes y tipografía clara.

### Datos
- Rebanada de pastel: categoria, monto, porcentaje, angulo_inicio, extension_angulo, color.

### Estado
- Datos de la serie activa.
- Rebanada actualmente destacada (efecto explode activo).

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Todos los montos deben ser estrictamente positivos.
- La suma total de montos debe ser mayor a cero.

### Casos límite
- Solo una categoría (el gráfico debe ser un círculo completo de $360^\circ$).
- Categorías con montos muy pequeños (ej. 0.5% del total, no deben romper el cálculo de arcos).
- Clics en el área vacía fuera del círculo del pastel.

### Manejo de errores
- Prevenir divisiones por cero validando que la suma de todos los montos no sea cero.

### Fundamentos de Python relacionados
- Trigonometría básica y conversión de proporciones a grados sexagesimales.
- Generación o rotación de paletas de colores hexadecimales.

### Conceptos Tkinter relacionados
- Método `canvas.create_arc` con parámetros `start`, `extent` y `style=tk.PIESLICE`.
- Desplazamiento vectorial de elementos gráficos calculando desplazamiento con seno y coseno para el efecto explode.

### Herramientas para investigar
- Parámetros de `canvas.create_arc` en `tkinter.Canvas` (`start`, `extent`, `style`).
- Fórmulas de desplazamiento radial con `math.cos` y `math.sin`.

### Diseño de interfaz
¿Cómo asegurarías que la leyenda lateral tenga suficiente contraste y quede alineada verticalmente al lado del gráfico de pastel?

### Diseño de variables
Usa nombres como `pie_canvas`, `categories_tree`, `cat_name_entry`, `cat_value_entry`, `generate_pie_btn`, `slices_data_list`, `selected_slice_index`.

### Antes de programar
1. ¿Cómo se utiliza el método `canvas.create_arc(x1, y1, x2, y2, start=..., extent=..., style=tk.PIESLICE)` para dibujar una rebanada de pastel?
2. ¿Cómo se calcula el vector de desplazamiento $(\Delta x, \Delta y)$ hacia afuera para separar una rebanada usando el ángulo medio de su sector circular?

### Arquitectura
```
ejercicio_084/
├── app.py             # Formulario de datos y ventana principal
├── pie_renderer.py    # Cálculo trigonométrico de arcos y renderizado en Canvas
└── legend_view.py     # Generación de la leyenda visual de colores y porcentajes
```

### Pruebas mínimas
1. Ingresar dos categorías de $50 y $50 -> Debe dibujar exactamente dos semicírculos de $180^\circ$ cada uno con 50% en la leyenda.
2. Hacer clic en una rebanada -> Debe desplazarse ligeramente hacia afuera destacando visualmente.

### Pruebas de error
1. Intentar generar la gráfica con todos los valores en cero -> Debe advertir que la suma total debe ser mayor a cero.

### Experiencia de usuario
Los colores de las rebanadas deben ser contrastantes y agradables a la vista, evitando colores difíciles de distinguir.

### Explicación posterior
¿Cómo permite el método `create_arc` con estilo `PIESLICE` construir gráficos circulares matemáticamente precisos en Tkinter sin librerías externas?

### Aplicación profesional
Módulos de análisis de gastos en software contable local, tableros de encuestas de opinión y herramientas de resumen de cartera de clientes.

### Reto adicional
Añade una opción para convertir el gráfico de pastel en un gráfico de Dona (Donut Chart) dibujando un círculo blanco centrado en el medio del pastel.

---
> [Índice General](../README.md) · [← Ejercicio 083](../ejercicio_083/README.md) · [Ejercicio 085 →](../ejercicio_085/README.md)
