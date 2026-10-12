## Ejercicio 003 — Temporizador y Cronómetro de Presentaciones (`StageTimerApp`)

> [Índice General](../README.md) · [← Ejercicio 002](../ejercicio_002/README.md) · [Ejercicio 004 →](../ejercicio_004/README.md)

### Contexto profesional
En auditorios corporativos y congresos académicos, los moderadores de sala necesitan controlar con precisión el tiempo de exposición de cada ponente, con avisos cromáticos evidentes a distancia.

### Usuario objetivo
Moderador de eventos técnicos o presentador en conferencias.

### Problema
El uso de teléfonos móviles distrae a los moderadores y carece de dígitos lo suficientemente grandes y legibles para ser vistos desde el estrado a varios metros de distancia.

### Objetivo
Desarrollar una aplicación de temporizador regresivo de alta visibilidad con controles de Inicio, Pausa, Reanudar y Reiniciar, que cambie de color de fondo según el tiempo restante (verde, amarillo de advertencia y rojo parpadeante al vencer).

### Flujo principal
El usuario configura el tiempo total en minutos/segundos mediante botones o campo numérico, presiona 'Iniciar', el cronómetro descuenta segundo a segundo con números gigantes. A los 2 minutos restantes el panel cambia a amarillo; al llegar a cero, el fondo se torna rojo y emite aviso.

### Requisitos funcionales
- Configuración de tiempo inicial en minutos y segundos.
- Controles para Iniciar, Pausar y Reiniciar el temporizador.
- Descuento continuo de segundos utilizando el método `.after()` de Tkinter.
- Alertas visuales: fondo normal/verde, advertencia en amarillo (últimos 120 segundos) y rojo al llegar a 00:00.
- Capacidad de alternar a modo cronómetro progresivo (hacia adelante).

### Requisitos de interfaz
- Pantalla principal con tipografía de reloj digital de gran escala (ej. tamaño de fuente 48 o 64 puntos en negrita).
- Botones de control con tamaño generoso para fácil pulsación.
- Contenedor con capacidad de redimensionarse dinámicamente si la ventana se amplía.

### Datos
- Tiempo configurado: entero en segundos.
- Tiempo restante: entero en segundos.
- Estado del temporizador: cadena ('DETENIDO', 'CORRIENDO', 'PAUSADO', 'FINALIZADO').

### Estado
- Identificador del callback programado con `.after()` para permitir cancelación limpia (`after_cancel`).
- Estado booleano de ejecución activa.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- No permitir iniciar un conteo con 0 minutos y 0 segundos configurados.
- Impedir el registro de valores negativos en la configuración de tiempo.

### Casos límite
- El usuario presiona repetidamente 'Iniciar' (debe evitarse que se creen múltiples bucles concurrentes con `.after()` que aceleren el reloj).
- La ventana se minimiza o cambia de tamaño durante el conteo.
- El usuario cierra la ventana mientras el temporizador está corriendo.

### Manejo de errores
- Cancelar explícitamente cualquier llamada pendiente a `.after()` al pausar, reiniciar o cerrar la aplicación.

### Fundamentos de Python relacionados
- Manejo de división entera y módulo para formateo de tiempo (`divmod(segundos, 60)`).
- Formateo de números con ceros a la izquierda (`f'{minutos:02d}:{segundos:02d}'`).
- Máquina de estados finita simple para controlar transiciones de ejecución.

### Conceptos Tkinter relacionados
- Método reactivo `root.after(ms, callback)` y `root.after_cancel(id)`.
- Modificación dinámica de estilos de fuentes con `font.Font`.
- Protocolo de cierre de ventana `WM_DELETE_WINDOW` para limpieza de tareas programadas.

### Herramientas para investigar
- Documentación de `after` y `after_cancel` en Tkinter.
- Manejo de protocolos de ventana en Tkinter (`protocol('WM_DELETE_WINDOW', ...)`).

### Diseño de interfaz
¿Cómo estructurarías los frames para que el área de dígitos ocupe el 80% superior de la pantalla y la barra de controles el 20% inferior, expandiéndose proporcionalmente?

### Diseño de variables
Usa nombres como `remaining_seconds`, `timer_after_id`, `timer_state`, `time_display_label`, `start_button`, `pause_button`.

### Antes de programar
1. ¿Qué grave error ocurre si llamas a `time.sleep(1)` dentro del bucle de eventos de Tkinter?
2. ¿Por qué debes almacenar el ID que retorna `.after()` en una variable?

### Arquitectura
```
ejercicio_003/
├── app.py           # Interfaz gráfica y actualización de widgets
└── timer_engine.py  # Lógica del temporizador (segundos, formato y estados)
```

### Pruebas mínimas
1. Configurar 10 segundos, presionar 'Iniciar' -> Verificar que descuente 1 segundo por ciclo y se detenga en 00:00.
2. Presionar 'Pausar' a los 5 segundos -> Verificar que el tiempo se congele; al presionar 'Reanudar', continúe desde 5.

### Pruebas de error
1. Presionar 'Iniciar' 10 veces consecutivas -> Comprobar que el cronómetro avance a velocidad normal de 1 segundo por segundo (no acelerado).

### Experiencia de usuario
Los dígitos deben ser legibles a contraluz. Al pausar, el botón de 'Iniciar' debe cambiar su texto a 'Reanudar' para reflejar el estado actual.

### Explicación posterior
¿Cómo garantiza `.after()` que la interfaz gráfica permanezca interactiva y no se congele durante una cuenta regresiva?

### Aplicación profesional
Herramientas de control de tiempo en cabinas de locución, salas de juntas para conferencias y cronómetros de evaluación en exámenes cronometrados.

### Reto adicional
Implementa un sonido audible de campana o pitido sintetizado (usando el módulo estándar `winsound` en Windows o pitido de terminal) cuando el contador llegue a cero.

---
> [Índice General](../README.md) · [← Ejercicio 002](../ejercicio_002/README.md) · [Ejercicio 004 →](../ejercicio_004/README.md)
