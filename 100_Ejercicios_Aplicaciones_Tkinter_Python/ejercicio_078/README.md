## Ejercicio 078 — Visualizador de Ondas de Señal o Pulso Cardíaco (`SignalWaveViewerApp`)

> [Índice General](../README.md) · [← Ejercicio 077](../ejercicio_077/README.md) · [Ejercicio 079 →](../ejercicio_079/README.md)

### Contexto profesional
En monitores de pacientes hospitalarios y bancos de prueba de señales de instrumentación electrónica, los técnicos supervisan oscilogramas periódicos en tiempo real.

### Usuario objetivo
Técnico de biomédica o laboratorista de instrumentación electrónica.

### Problema
Visualizar señales periódicas que se desplazan en tiempo real en interfaces lentas produce parpadeos severos (flickering) o desfase temporal con los datos.

### Objetivo
Desarrollar un osciloscopio virtual en `Canvas` que dibuje una señal periódica en tiempo real (onda senoidal o trazo de electrocardiograma ECG simulado) con efecto de barrido continuo de izquierda a derecha mediante el ciclo de eventos `after()`, con controles para ajustar la frecuencia, amplitud y botón de pausa.

### Flujo principal
El usuario inicia la simulación. En el `Canvas` de fondo oscuro con cuadrícula de fósforo verde, un trazo continuo se desplaza de izquierda a derecha simulando un electrocardiograma o una onda senoidal. El usuario puede modificar los deslizadores de 'Amplitud' y 'Frecuencia' para ver cómo la señal se estira o comprime en tiempo real. Puede pulsar 'Congelar Trazo' para pausar la animación y analizar una anomalía.

### Requisitos funcionales
- Widget `Canvas` con fondo oscuro (estilo fósforo verde o azul marino) y cuadrícula cuadriculada médica.
- Generación matemática de la señal periódica: función matemática continua $y(t) = A \times \sin(2\pi f t)$ o vector de puntos ECG (complejo QRS).
- Efecto de desplazamiento continuo de la señal en el lienzo actualizando coordenadas periódicamente con `root.after(30, anim_loop)`.
- Controles interactivos: Deslizador de Amplitud ($A$), Deslizador de Frecuencia ($f$), Selector de tipo de onda (`Seno`, `ECG`).
- Botón para Congelar / Reanudar el barrido en tiempo real.
- Redibujado suave y eficiente sin parpadeos visuales reutilizando el elemento de línea con `canvas.coords()`.

### Requisitos de interfaz
- Pantalla principal dominada por el `Canvas` del osciloscopio (al menos 600x300 píxeles).
- Barra inferior de controles con deslizadores bien rotulados y perillas virtuales.
- Etiqueta digital con la frecuencia y amplitud actual en la esquina superior del osciloscopio.

### Datos
- Parámetros de señal: amplitud (float), frecuencia (float), fase (float), tipo_onda (str).

### Estado
- Estado de animación activa o congelada.
- Lista de puntos $(x, y)$ que componen la polilínea del trazo activo.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Amplitud y frecuencia restringidas a rangos que no desborden la visualización del Canvas.

### Casos límite
- Frecuencia en cero (la señal debe mostrarse como una línea horizontal continua plana).
- Redimensionamiento de ventana (adaptar el ancho de muestreo del barrido).

### Manejo de errores
- Cancelar limpiamente el bucle de `after()` al cerrar la ventana.

### Fundamentos de Python relacionados
- Módulo estándar `math` (`math.sin`, `math.pi`).
- Comprensiones de listas y transformaciones geométricas de series de puntos.

### Conceptos Tkinter relacionados
- Reutilización del identificador de línea con `canvas.coords(line_id, *puntos)` para evitar destruir y recrear objetos gráficos en cada fotograma.
- Animación suave a 30-60 fotogramas por segundo con `root.after()`.

### Herramientas para investigar
- Función trigonométrica `math.sin()` en Python.
- Técnica de redibujado eficiente con `coords()` en `tkinter.Canvas`.

### Diseño de interfaz
¿Cómo asegurarías que la cuadrícula de fondo se mantenga estática mientras la señal de onda se desplaza de forma independiente?

### Diseño de variables
Usa nombres como `scope_canvas`, `amplitude_scale`, `frequency_scale`, `wave_type_combo`, `freeze_btn`, `waveform_line_id`, `phase_accumulator`.

### Antes de programar
1. ¿Por qué es infinitamente más eficiente actualizar las coordenadas de una sola línea existente con `canvas.coords(line_id, ...)` que borrar todo el Canvas y recrear la línea en cada fotograma?
2. ¿Cómo se genera la forma de onda de un complejo QRS de pulso cardíaco mediante la combinación de picos matemáticos?

### Arquitectura
```
ejercicio_078/
├── app.py             # Osciloscopio virtual y controles de perillas
├── signal_math.py     # Generadores matemáticos de ondas (seno, pulsos, ECG)
└── scope_renderer.py  # Renderizado y ciclo de barrido en Canvas con after()
```

### Pruebas mínimas
1. Iniciar animación de onda senoidal -> La señal debe ondular de forma continua y fluida de izquierda a derecha.
2. Mover la amplitud al doble -> La altura de las crestas de la onda debe duplicarse instantáneamente.
3. Presionar 'Congelar' -> El trazo debe detenerse en seco.

### Pruebas de error
1. Ajustar frecuencia al máximo -> La onda debe comprimirse limpiamente sin generar retrasos perceptibles en la animación.

### Experiencia de usuario
El contraste del trazo brillante sobre el fondo oscuro debe emular con precisión los monitores de tubo de rayos catódicos o pantallas médicas hospitalarias.

### Explicación posterior
¿Cómo previene la actualización de coordenadas con `canvas.coords()` el problema de fuga de memoria o saturación de objetos en el servidor gráfico de Tkinter?

### Aplicación profesional
Software médico de simulación de signos vitales, visualizadores de sensores de audio y consolas de prueba de hardware electrónico.

### Reto adicional
Añade un cursor o línea de barrido vertical que avance borrando y redibujando la señal periódicamente al estilo de los monitores de quirófano reales.

---
> [Índice General](../README.md) · [← Ejercicio 077](../ejercicio_077/README.md) · [Ejercicio 079 →](../ejercicio_079/README.md)
