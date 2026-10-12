## Ejercicio 074 — Monitor de Temperatura y Termómetro Visual Interactivo (`VisualThermometerApp`)

> [Índice General](../README.md) · [← Ejercicio 073](../ejercicio_073/README.md) · [Ejercicio 075 →](../ejercicio_075/README.md)

### Contexto profesional
En sistemas de control de cámaras frigoríficas industriales y monitoreo de almacenes farmacéuticos de vacunas, los operarios necesitan una representación visual realista del nivel de temperatura con alertas cromáticas.

### Usuario objetivo
Operador de cámara frigorífica o supervisor de cadena de frío.

### Problema
Los valores numéricos aislados no transmiten con la misma inmediatez el riesgo de ruptura de la cadena de frío que una representación visual intuitiva.

### Objetivo
Desarrollar un componente visual interactivo de termómetro industrial dibujado desde cero en `Canvas` de Tkinter, que incluya bulbo inferior, tubo graduado con marcas de escala (-20 °C a 60 °C), columna de líquido de mercurio con altura proporcional al valor de temperatura, animación suave de cambio de nivel y cambio de color del líquido según el rango (Azul para congelación, Verde para óptimo, Rojo para sobrecalentamiento).

### Flujo principal
El usuario ajusta la temperatura mediante un deslizador (`Scale`) o campo de entrada numérico. El termómetro en el `Canvas` actualiza suavemente la altura de su columna de líquido. Si la temperatura está por debajo de 0 °C, el líquido se muestra azul; si está entre 0 y 25 °C, se muestra verde; si supera los 40 °C, se torna rojo y emite un parpadeo visual de alarma.

### Requisitos funcionales
- Dibujo vectorial del termómetro en `Canvas`: Tubo vertical con extremos redondeados, bulbo inferior esférico (`create_oval`), marcas graduadas de escala cada 10 °C y etiquetas numéricas.
- Mapeo matemático lineal entre el rango de temperatura (-20 a 60 °C) y las coordenadas verticales del Canvas ($y_{min}$ a $y_{max}$).
- Control deslizante (`ttk.Scale`) y campo de entrada numérica para ajustar la temperatura.
- Modificación dinámica de la altura y color del líquido del termómetro.
- Animación suave de transición de nivel de líquido mediante pequeños pasos con `root.after()`.
- Indicador de estado de la cadena de frío: 'Congelación', 'Rango Óptimo', 'Alerta de Temperatura'.

### Requisitos de interfaz
- Panel izquierdo con el termómetro vectorial centrado en un `Canvas` vertical de 150x400 píxeles.
- Panel derecho con los controles de ajuste numérico, controles de simulación y banner de estado.
- Diseño visual limpio con apariencia de instrumento de laboratorio.

### Datos
- Temperatura actual: float (-20.0 a 60.0 °C).
- Coordenadas de escala: $y$ base del bulbo y $y$ tope del tubo.

### Estado
- Temperatura objetivo y temperatura visual animada en curso.
- ID del callback de animación con `after()`.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Rango de temperatura restringido estrictamente entre -20.0 y 60.0 °C.

### Casos límite
- Ajuste de temperatura a los límites extremos (-20 °C y 60 °C).
- Cambiar la temperatura rápidamente mientras una animación previa aún está en curso.

### Manejo de errores
- Cancelar cualquier animación pendiente antes de iniciar una nueva para evitar artefactos visuales.

### Fundamentos de Python relacionados
- Interpolación lineal matemática: $y = y_0 + (T - T_{min}) \times \frac{y_1 - y_0}{T_{max} - T_{min}}$.
- Animaciones procedimentales mediante aproximación sucesiva por pasos discretos.

### Conceptos Tkinter relacionados
- Creación y actualización de geometrías vectoriales en `Canvas` (`canvas.coords(item_id, x1, y1, x2, y2)`).
- Animaciones fluidas no bloqueantes con `root.after()`.
- Modificación dinámica de colores en `Canvas` con `.itemconfig(item_id, fill=...)`.

### Herramientas para investigar
- Fórmula de mapeo lineal (función `map_range` o similar).
- Método `canvas.coords()` y `canvas.itemconfig()` en `tkinter.Canvas`.

### Diseño de interfaz
¿Cómo asegurarías que las marcas de escala numérica (-20, -10, 0, 10... 60) queden perfectamente alineadas al lado del tubo de vidrio del termómetro?

### Diseño de variables
Usa nombres como `thermometer_canvas`, `temp_scale`, `temp_entry`, `mercury_column_id`, `bulb_id`, `temp_status_banner`, `target_temp_val`.

### Antes de programar
1. ¿Cómo se invierten las coordenadas cartesianas teniendo en cuenta que en el `Canvas` de Tkinter el origen $(0, 0)$ está en la esquina superior izquierda (el valor $y$ aumenta hacia abajo)?
2. ¿Cómo se diseña una función recursiva con `after()` que mueva el nivel del líquido 0.5 grados por ciclo hasta alcanzar la temperatura meta?

### Arquitectura
```
ejercicio_074/
├── app.py                # Interfaz de laboratorio y controles
├── thermometer_canvas.py # Renderizado del termómetro vectorial en Canvas
└── anim_controller.py   # Lógica de interpolación y animación con after()
```

### Pruebas mínimas
1. Ajustar temperatura a 20 °C -> La columna de líquido debe subir suavemente y tornarse de color verde.
2. Ajustar temperatura a -10 °C -> La columna debe descender y tornarse azul frío.

### Pruebas de error
1. Ingresar temperatura fuera de rango (85 °C) -> Debe ajustar al límite máximo de 60 °C o advertir el error.

### Experiencia de usuario
La animación del líquido debe sentirse natural y suave, similar a la inercia del mercurio en un termómetro de vidrio físico.

### Explicación posterior
¿Cómo se resuelve la inversión del eje vertical $Y$ al mapear variables físicas de abajo hacia arriba en el sistema de coordenadas de Tkinter?

### Aplicación profesional
Instrumentación virtual de laboratorio, software HMI (Human-Machine Interface) de control industrial y simuladores de física aplicada.

### Reto adicional
Añade un botón 'Simulación de Falla Eléctrica' que incremente la temperatura a razón de 2 °C por segundo de forma autónoma hasta activar la alarma de emergencia.

---
> [Índice General](../README.md) · [← Ejercicio 073](../ejercicio_073/README.md) · [Ejercicio 075 →](../ejercicio_075/README.md)
