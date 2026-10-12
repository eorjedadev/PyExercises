## Ejercicio 082 — Selector de Asientos de Cine o Teatro con Estados de Color (`SeatBookingCanvasApp`)

> [Índice General](../README.md) · [← Ejercicio 081](../ejercicio_081/README.md) · [Ejercicio 083 →](../ejercicio_083/README.md)

### Contexto profesional
En taquillas de teatros, cines independientes y auditorios culturales, los dependientes de boletería seleccionan butacas numeradas en una cuadrícula gráfica de sala para asignar asientos a los espectadores.

### Usuario objetivo
Cajero de taquilla o espectador en kiosco de autoservicio.

### Problema
La selección de asientos en tablas de texto ordinarias no permite al cliente saber qué tan cerca de la pantalla o del pasillo quedará ubicado.

### Objetivo
Desarrollar una interfaz de reserva de butacas visual en `Canvas` que dibuje una sala con pantalla curva superior y una matriz de asientos (ej. 6 filas x 8 columnas), donde cada butaca sea interactiva y cambie de color según su estado (Libre = Verde, Seleccionada = Amarillo, Ocupada = Rojo), calculando en tiempo real el costo total de las butacas seleccionadas y permitiendo confirmar la compra.

### Flujo principal
El usuario observa la disposición de la sala en el `Canvas`. Los asientos ocupados aparecen en rojo y no responden a clics. El usuario hace clic en butacas libres (verdes); estas cambian a amarillo ('Seleccionadas') y se añaden a su orden. Si vuelve a hacer clic sobre una butaca seleccionada, se deselecciona y regresa a verde. El panel lateral muestra el detalle de las butacas elegidas (ej. 'A3, A4') y el precio total. Al pulsar 'Confirmar Boletos', los asientos pasan definitivamente a rojo ('Ocupados').

### Requisitos funcionales
- Dibujo vectorial de la sala en `Canvas`: Pantalla curva en la parte superior (`create_arc` o `create_line` curva) y matriz de butacas numeradas (Filas A-F, Columnas 1-8).
- Butacas dibujadas como rectángulos con bordes redondeados y texto de número de asiento.
- Tres estados visuales por butaca: Libre (verde tenue), Seleccionada por el cliente actual (amarillo brillante), Ocupada previamente (rojo oscuro deshabilitado).
- Enlace de clic interactivo en el Canvas para alternar el estado de las butacas libres/seleccionadas.
- Panel lateral con: Lista de asientos seleccionados, Tarifa unitaria por butaca y Costo total a pagar.
- Botón 'Confirmar Compra' que selle los asientos seleccionados como ocupados y limpie la orden.

### Requisitos de interfaz
- `Canvas` central con la distribución del teatro centrada y espaciada.
- Panel lateral derecho con el resumen de la compra y botón de pago.
- Leyenda visual inferior con los tres colores explicativos.

### Datos
- Butaca: id_asiento (ej. 'B4'), fila, columna, estado ('libre'|'seleccionado'|'ocupado'), precio.

### Estado
- Matriz de estados de todas las butacas en memoria.
- Lista de butacas actualmente seleccionadas en la orden activa.

### Persistencia
No requiere persistencia en disco en esta fase (opera en memoria de sesión).

### Validaciones
- No permitir confirmar la compra si hay 0 butacas seleccionadas.
- No permitir hacer clic ni modificar butacas que ya se encuentran en estado 'Ocupado'.

### Casos límite
- Intentar seleccionar más de 6 butacas simultáneas (establecer un límite de compra por persona).
- Clics en los pasillos o espacios vacíos entre butacas (no deben producir ninguna acción).

### Manejo de errores
- Identificar los clics con precisión sobre las coordenadas de cada asiento ignorando áreas fuera de los rectángulos.

### Fundamentos de Python relacionados
- Diccionarios para indexar butacas por clave de coordenadas o código `'FilaColumna'`.
- Manejo de listas y cálculo de totales acumulados.

### Conceptos Tkinter relacionados
- Identificación de elementos en `Canvas` con tags específicos por butaca (`tag=f'seat_{fila}_{col}'`).
- Enlace de clics con `canvas.tag_bind()` o detección por coordenadas con `canvas.find_withtag(tk.CURRENT)`.

### Herramientas para investigar
- Pseudo-tag `tk.CURRENT` en el widget `Canvas` de Tkinter.
- Patrones de selección múltiple interactiva en lienzos.

### Diseño de interfaz
¿Cómo diseñarías la pantalla curva y los pasillos para que el espectador entienda inmediatamente cuál es la orientación del escenario?

### Diseño de variables
Usa nombres como `theater_canvas`, `selected_seats_list`, `seats_summary_label`, `total_price_label`, `confirm_booking_btn`, `seats_state_map`.

### Antes de programar
1. ¿Cómo se asocia a cada butaca un tag único (ej. `'seat_A3'`) para responder selectivamente a los eventos de clic del ratón?
2. ¿Cómo se utiliza el identificador `tk.CURRENT` de Canvas para saber exactamente qué butaca está bajo el puntero del ratón en el evento de clic?

### Arquitectura
```
ejercicio_082/
├── app.py             # Interfaz de taquilla y panel de resumen
├── seating_canvas.py  # Renderizado de la sala y gestión de clics en Canvas
└── booking_service.py # Lógica de estados de butacas y cálculo de tarifas
```

### Pruebas mínimas
1. Hacer clic en butacas A1 y A2 libres -> Deben cambiar a amarillo y el total marcar $200 (si la tarifa es $100).
2. Presionar 'Confirmar Compra' -> Deben pasar a rojo y quedar bloqueadas para futuros clics.
3. Hacer clic en una butaca roja -> No debe seleccionarse ni modificar el total.

### Pruebas de error
1. Presionar 'Confirmar' sin haber seleccionado ninguna butaca -> Debe advertir 'Seleccione al menos una butaca para continuar'.

### Experiencia de usuario
El cambio de color debe ser instantáneo y los asientos seleccionados deben listarse de forma ordenada (ej. 'A1, A2') en el panel lateral.

### Explicación posterior
¿Cómo optimiza el uso del tag dinámico `tk.CURRENT` la detección de clics sobre cientos de elementos independientes dentro de un `Canvas`?

### Aplicación profesional
Sistemas de boletaje para teatros, salas de cine, estadios deportivos y reserva de asientos en autobuses de pasajeros.

### Reto adicional
Añade diferentes tarifas según la zona de la sala (ej. Filas A y B 'Zona VIP' a mayor precio, Filas C a F 'General').

---
> [Índice General](../README.md) · [← Ejercicio 081](../ejercicio_081/README.md) · [Ejercicio 083 →](../ejercicio_083/README.md)
