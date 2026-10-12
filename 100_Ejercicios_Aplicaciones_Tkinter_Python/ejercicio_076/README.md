## Ejercicio 076 — Visor de Métricas con Gráfico de Barras Nativo en Canvas (`CanvasBarChartApp`)

> [Índice General](../README.md) · [← Ejercicio 075](../ejercicio_075/README.md) · [Ejercicio 077 →](../ejercicio_077/README.md)

### Contexto profesional
En tableros de control ejecutivos y aplicaciones embebidas sin dependencias externas pesadas, los desarrolladores construyen componentes de visualización gráfica de barras nativos utilizando exclusivamente la biblioteca estándar.

### Usuario objetivo
Analista de negocios o desarrollador de tableros ejecutivos.

### Problema
Instalar librerías científicas pesadas como matplotlib solo para mostrar un gráfico simple de barras de 5 categorías incrementa el tamaño del ejecutable en cientos de megabytes innecesariamente.

### Objetivo
Desarrollar un componente reutilizable de gráfico de barras interactivo dibujado desde cero en `Canvas` de Tkinter, que reciba un diccionario de categorías y valores numéricos, calcule el escalamiento de coordenadas, dibuje los ejes cartesianos, barras proporcionadas con colores alternados y muestre un tooltip flotante con el valor exacto al pasar el cursor sobre una barra.

### Flujo principal
El usuario ingresa o carga un conjunto de datos (ej. Ventas por Trimestre o Gasto por Departamento). Presiona 'Dibujar Gráfica'. El componente en el `Canvas` limpia el lienzo, calcula el valor máximo de la serie, traza el eje Y graduado y el eje X, y dibuja las barras proporcionales. Al posar el puntero del ratón sobre cualquier barra, aparece un recuadro flotante (tooltip) con el valor numérico exacto.

### Requisitos funcionales
- Entrada o edición rápida de categorías y valores numéricos (tabla o campos de entrada).
- Cálculo automático de la escala vertical según el valor máximo de la serie de datos ($y_{max}$).
- Dibujo de ejes cartesianos graduados con líneas guía horizontales tenues.
- Representación de barras rectangulares con colores distinguibles y etiquetas de categoría en la base.
- Sistema de tooltips o etiquetas flotantes en `Canvas` que aparezcan al pasar el ratón (`<Enter>`, `<Motion>`, `<Leave>`) sobre cada barra.
- Redibujado automático si la ventana o el lienzo cambia de tamaño (`<Configure>`).

### Requisitos de interfaz
- Panel lateral izquierdo para la gestión de datos (lista de categorías y valores con botones Añadir/Modificar).
- Área principal ocupada por el `Canvas` de la gráfica de barras con fondo limpio.
- Tooltip con sombra o borde sutil que siga al cursor.

### Datos
- Serie de datos: lista de tuplas o diccionario `{'Categoría': valor_float}`.

### Estado
- Datos de la serie activa.
- Barra actualmente resaltada bajo el cursor.
- Identificador del tooltip activo en el Canvas.

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- Los valores deben ser números flotantes o enteros mayores o iguales a cero.
- Debe existir al menos una categoría para poder renderizar la gráfica.

### Casos límite
- Serie donde todos los valores son 0 (el escalador debe evitar división por cero).
- Serie con una sola barra vs serie con 15 barras (el ancho de las barras debe ajustarse dinámicamente).
- Redimensionar la ventana a un tamaño muy pequeño.

### Manejo de errores
- Prevenir divisiones por cero cuando el valor máximo de la serie sea 0.

### Fundamentos de Python relacionados
- Escalamiento y geometría analítica para transformación de coordenadas de pantalla.
- Manejo de diccionarios y tuplas ordenadas.

### Conceptos Tkinter relacionados
- Widget `Canvas` para renderizado de gráficos vectoriales 2D.
- Manejo del evento `<Configure>` para implementar gráficos reactivos al tamaño de la ventana.
- Tags de Canvas para asociar eventos interactivos a elementos específicos (`canvas.tag_bind()`).

### Herramientas para investigar
- Método `canvas.tag_bind()` en Tkinter para eventos por elemento gráfico.
- Evento de redimensionamiento de ventana `<Configure>`.

### Diseño de interfaz
¿Cómo asegurarías que las etiquetas de texto de las categorías en el eje X no se solapen entre sí si los nombres son largos?

### Diseño de variables
Usa nombres como `chart_canvas`, `data_series_tree`, `cat_name_entry`, `value_entry`, `render_chart_btn`, `tooltip_id`, `max_data_value`.

### Antes de programar
1. ¿Cómo se escala un valor de datos $V$ a una altura en píxeles $H$ en el Canvas usando la fórmula $h_{barra} = \frac{V}{V_{max}} \times (H_{canvas} - margen)$?
2. ¿Cómo se utiliza `tag_bind()` para mostrar y ocultar un tooltip cuando el cursor entra y sale de una barra específica?

### Arquitectura
```
ejercicio_076/
├── app.py             # Formulario de datos y ventana principal
├── bar_chart.py       # Componente de gráfico vectorial reutilizable en Canvas
└── chart_tooltip.py   # Lógica flotante de tooltips en Canvas
```

### Pruebas mínimas
1. Renderizar datos: `{Q1: 100, Q2: 250, Q3: 180, Q4: 320}` -> Comprobar que dibuje 4 barras escaladas proporcionalmente.
2. Pasar el cursor sobre la barra Q4 -> Comprobar que aparezca el tooltip indicando 'Q4: 320'.
3. Redimensionar la ventana -> La gráfica debe redibujarse adaptándose al nuevo ancho y alto.

### Pruebas de error
1. Ingresar valores todos en cero -> La gráfica debe trazar los ejes sin arrojar `ZeroDivisionError`.

### Experiencia de usuario
Al pasar el cursor sobre una barra, esta debe cambiar ligeramente su tono de color (hover effect) para brindar retroalimentación táctil al usuario.

### Explicación posterior
¿Cómo se implementa el evento `<Configure>` en un `Canvas` para construir gráficos dinámicos y responsive que se adapten a cualquier resolución?

### Aplicación profesional
Componentes de visualización embebidos en software administrativo sin dependencias pesadas, monitores de rendimiento y herramientas livianas de reporting.

### Reto adicional
Añade una opción para alternar la orientación de la gráfica entre Barras Verticales y Barras Horizontales con recálculo automático de coordenadas.

---
> [Índice General](../README.md) · [← Ejercicio 075](../ejercicio_075/README.md) · [Ejercicio 077 →](../ejercicio_077/README.md)
