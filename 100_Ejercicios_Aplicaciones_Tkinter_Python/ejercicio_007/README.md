## Ejercicio 007 — Selector Interactivo de Paletas de Color RGB/HEX (`ColorPickerApp`)

> [Índice General](../README.md) · [← Ejercicio 006](../ejercicio_006/README.md) · [Ejercicio 008 →](../ejercicio_008/README.md)

### Contexto profesional
En agencias de diseño web y desarrollo de software, los maquetadores necesitan inspeccionar y ajustar colores en formato RGB y hexadecimal con previsualización en vivo y copia inmediata.

### Usuario objetivo
Diseñador de interfaces, maquetador web o desarrollador frontend.

### Problema
Abrir suites de diseño pesadas para obtener el código hexadecimal de un ajuste menor de color consume tiempo y memoria innecesariamente.

### Objetivo
Construir una herramienta interactiva con tres controles deslizantes (`Scale`) para los canales Rojo, Verde y Azul (0 a 255), un área de muestra visual que cambie instantáneamente de color, etiquetas con los códigos RGB y HEX, y un botón de copia.

### Flujo principal
El usuario arrastra cualquiera de los tres deslizadores (R, G o B). El panel de muestra actualiza su color de fondo en tiempo real, las etiquetas reflejan los valores numéricos decimales y el código `#RRGGBB` equivalente. Un clic en el botón copia el valor hexadecimal.

### Requisitos funcionales
- Tres controles deslizantes para Rojo, Verde y Azul con rango de 0 a 255.
- Visualización en tiempo real de los valores numéricos individuales.
- Cálculo del código hexadecimal en formato `#RRGGBB`.
- Panel o Canvas que refleje visualmente el color resultante.
- Botón para copiar el código hexadecimal al portapapeles del sistema.

### Requisitos de interfaz
- Distribución organizada con deslizadores claramente identificados con sus respectivos colores base.
- Recuadro de muestra con dimensiones generosas (al menos 150x150 píxeles).
- Etiqueta de código hexadecimal con tipografía monoespaciada de tamaño grande.

### Datos
- Canales R, G, B: enteros entre 0 y 255.
- Código hexadecimal: cadena de 7 caracteres iniciando con `#`.

### Estado
- Variables de control de Tkinter para cada canal.
- Cadena con el color hexadecimal actual.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Asegurar que los valores de cada canal se mantengan estrictamente en el rango entero [0, 255].

### Casos límite
- Ajuste a los límites extremos (0, 0, 0 para negro y 255, 255, 255 para blanco).
- Redimensionamiento de ventana (el recuadro de color debe permanecer visible y centrado).

### Manejo de errores
- Proteger la conversión a hexadecimal contra valores flotantes formateando explícitamente a enteros.

### Fundamentos de Python relacionados
- Formateo de números enteros a cadenas hexadecimales con relleno de ceros (`f'#{r:02X}{g:02X}{b:02X}'`).
- Desempaquetado de tuplas y manipulación de cadenas.

### Conceptos Tkinter relacionados
- Widget `Scale` o `ttk.Scale` con parámetro `command=` para actualización continua.
- Modificación dinámica de la propiedad `background` (o `bg`) de un `Frame` o `Canvas`.
- Portapapeles con `clipboard_clear()` y `clipboard_append()`.

### Herramientas para investigar
- Formateadores de formato hexadecimal en Python (`:02X`).
- Enlace de comandos en widgets `Scale` de Tkinter.

### Diseño de interfaz
¿Cómo asegurarías que el texto de la etiqueta que muestra el código de color sea legible tanto si el fondo del cuadro es completamente blanco como si es negro?

### Diseño de variables
Usa nombres como `red_scale`, `green_scale`, `blue_scale`, `color_preview_frame`, `hex_value_label`, `copy_hex_btn`.

### Antes de programar
1. ¿Por qué el evento de `Scale` pasa el valor como argumento de cadena a su callback?
2. ¿Cómo se convierte un trío de números `(255, 128, 0)` en una cadena `#FF8000`?

### Arquitectura
```
ejercicio_007/
├── app.py           # Ventana, deslizadores y visualización
└── color_utils.py   # Lógica matemática de conversión RGB a HEX y viceversa
```

### Pruebas mínimas
1. Mover los tres controles a 255 -> El panel debe ser blanco y el código `#FFFFFF`.
2. Mover a R=255, G=0, B=0 -> El panel debe ser rojo puro y el código `#FF0000`.

### Pruebas de error
1. Intentar copiar antes de mover controles -> Debe copiar el color inicial por defecto sin arrojar excepciones.

### Experiencia de usuario
La actualización del color en el recuadro debe ser inmediata y suave mientras el usuario arrastra el cursor.

### Explicación posterior
¿Cómo procesa Tkinter el callback continuo de un control `Scale` sin saturar la cola de eventos de la interfaz?

### Aplicación profesional
Selectores de color para editores de estilo en software interno, utilidades de diseño gráfico y herramientas de accesibilidad de contraste.

### Reto adicional
Calcula el valor inverso o complementario del color actual y muéstralo en un botón que permita invertir la paleta con un solo clic.

---
> [Índice General](../README.md) · [← Ejercicio 006](../ejercicio_006/README.md) · [Ejercicio 008 →](../ejercicio_008/README.md)
