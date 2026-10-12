## Ejercicio 083 — Indicador de Nivel de Tanques de Combustible y Alarma (`TankLevelGaugeApp`)

> [Índice General](../README.md) · [← Ejercicio 082](../ejercicio_082/README.md) · [Ejercicio 084 →](../ejercicio_084/README.md)

### Contexto profesional
En estaciones de almacenamiento de hidrocarburos y plantas industriales, los operarios supervisan el volumen de combustible en tanques cilíndricos verticales mediante indicadores visuales de nivel.

### Usuario objetivo
Operador de planta de combustibles o supervisor de seguridad de tanques.

### Problema
El sobrellenado o desabastecimiento imprevisto de tanques por no advertir umbrales críticos genera derrames ecológicos o paradas operativas.

### Objetivo
Construir un medidor de nivel de tanque industrial en `Canvas` que represente un cilindro de almacenamiento vertical con marcas de graduación (0% a 100%), nivel de fluido animado proporcional al porcentaje ingresado, visualización de volumen en litros y un sistema de alarma de tres estados (Bajo nivel en amarillo, Nivel seguro en verde, y Peligro de Desbordamiento > 90% en rojo parpadeante).

### Flujo principal
El operario ajusta el nivel del tanque mediante un control deslizante o ingresa el volumen actual en litros. El componente en el `Canvas` actualiza la altura del fluido dentro del cilindro con una animación suave. Si el tanque se encuentra por debajo del 15%, emite una advertencia de 'Nivel Bajo'; si supera el 90%, el fondo de la pantalla y el líquido parpadean en rojo emitiendo un estado de 'Alarma de Sobrellenado Crítico'.

### Requisitos funcionales
- Representación gráfica de tanque cilíndrico en `Canvas`: Cuerpo rectangular con tapas elípticas superior e inferior (`create_oval`) para dar efecto tridimensional de perspectiva.
- Nivel de fluido proporcional a la capacidad máxima del tanque (ej. 10,000 Litros).
- Escala graduada lateral con marcas de porcentaje (0%, 25%, 50%, 75%, 100%).
- Controles para modificar el nivel: `ttk.Scale` y `ttk.Entry` con sincronización bidireccional.
- Animación de llenado/vaciado suave con `root.after()`.
- Sistema de alarmas por umbrales: Crítico Bajo (<15%), Seguro (15-90%), Alarma Desbordamiento (>90%).
- Parpadeo visual intermitente de la alarma durante estados críticos.

### Requisitos de interfaz
- Panel izquierdo: `Canvas` vertical amplio con el cilindro tridimensional y escala de volumen.
- Panel derecho: Controles de simulación de bombeo, display digital de litros y luces piloto de estado.
- Estética industrial limpia de sala de control.

### Datos
- Tanque: capacidad_max_litros (ej. 10000), volumen_actual_litros, porcentaje_nivel, estado_alarma.

### Estado
- Volumen activo del tanque.
- ID del callback de animación y parpadeo.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Volumen no puede ser menor a 0 ni mayor a la capacidad máxima del tanque.

### Casos límite
- Nivel exactamente en 0 litros (tanque completamente vacío).
- Nivel al 100% (capacidad tope).
- Cambiar bruscamente el deslizador durante un llenado simulado.

### Manejo de errores
- Cancelar bucles de parpadeo de alarma cuando el nivel regrese a parámetros seguros.

### Fundamentos de Python relacionados
- Fórmulas de proporción matemática y escalamiento lineal.
- Control de estados intermitentes booleanos para efectos de parpadeo visual.

### Conceptos Tkinter relacionados
- Dibujo de geometrías elípticas superpuestas para simular cilindros en perspectiva isométrica.
- Parpadeo visual con `after()` alternando colores de fondo entre dos estados cromáticos.

### Herramientas para investigar
- Técnicas de dibujo de cilindros con arcos y óvalos en 2D.
- Manejo de intervalos periódicos de parpadeo con `root.after()`.

### Diseño de interfaz
¿Cómo asegurarías que el efecto de perspectiva del cilindro (óvalo superior y fondo curvo) sea claro para que el componente parezca un tanque físico real?

### Diseño de variables
Usa nombres como `tank_canvas`, `level_slider`, `liters_entry`, `fluid_rect_id`, `fluid_top_oval_id`, `alarm_pilot_label`, `pump_sim_btn`.

### Antes de programar
1. ¿Cómo se dibuja la superficie superior del líquido en un cilindro usando un óvalo (`create_oval`) que se desplace verticalmente con el nivel del fluido?
2. ¿Cómo se implementa un bucle de parpadeo que alterne el color de la alarma entre rojo y gris cada 500 ms de forma controlada?

### Arquitectura
```
ejercicio_083/
├── app.py           # Consola de monitoreo industrial y controles
├── tank_gauge.py    # Renderizado del cilindro y fluido en Canvas
└── alarm_system.py  # Evaluación de umbrales y animación de parpadeo
```

### Pruebas mínimas
1. Mover el nivel al 50% (5,000 L) -> El fluido debe subir a la mitad del cilindro y la luz de estado debe ser verde ('Seguro').
2. Mover el nivel al 95% (9,500 L) -> El fluido debe marcar nivel casi lleno y activarse la alarma roja de sobrellenado.

### Pruebas de error
1. Ingresar volumen mayor a 10,000 L -> Debe topar al máximo o advertir que excede la capacidad física del tanque.

### Experiencia de usuario
La superficie del fluido debe moverse de forma fluida y el display digital de litros debe formatearse con separador de miles.

### Explicación posterior
¿Cómo se combinan primitivas elípticas y rectangulares en `Canvas` para generar una percepción tridimensional de instrumentos industriales?

### Aplicación profesional
Sistemas SCADA de tanques de combustible, plantas de tratamiento de agua y control de silos de grano.

### Reto adicional
Añade botones 'Simular Llenado de Pipa' y 'Simular Consumo de Planta' que incrementen o decrementen el volumen automáticamente a razón de 50 litros por segundo.

---
> [Índice General](../README.md) · [← Ejercicio 082](../ejercicio_082/README.md) · [Ejercicio 084 →](../ejercicio_084/README.md)
