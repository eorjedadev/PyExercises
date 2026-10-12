## Ejercicio 066 — Simulador de Descarga y Sincronización de Recursos (`SyncDownloaderApp`)

> [Índice General](../README.md) · [← Ejercicio 065](../ejercicio_065/README.md) · [Ejercicio 067 →](../ejercicio_067/README.md)

### Contexto profesional
En aplicaciones de actualización de clientes de videojuegos y sincronizadores de archivos corporativos, los clientes descargan paquetes de actualización pesados con capacidad de pausar, reanudar y cancelar la descarga.

### Usuario objetivo
Usuario final de software corporativo o jugador de plataforma de entretenimiento.

### Problema
Las descargas que no se pueden pausar o que bloquean la ventana durante la transferencia de bytes generan frustración y consumo innecesario de ancho de banda si se interrumpe la red.

### Objetivo
Construir un simulador interactivo de descarga por bloques en segundo plano con `threading`, que actualice una barra de progreso porcentual, muestre velocidad simulada en KB/s y bytes transferidos, y soporte formalmente los estados: 'Iniciando', 'Descargando', 'Pausado', 'Reanudando' y 'Cancelado'.

### Flujo principal
El usuario elige el tamaño del paquete a simular (ej. 50 MB) y presiona 'Iniciar Descarga'. El hilo trabajador comienza a transferir bloques iterativamente. La interfaz actualiza una barra de progreso suave, los megabytes leídos y la velocidad. El usuario puede presionar 'Pausar', lo que congela la transferencia sin perder los bytes acumulados; al pulsar 'Reanudar', continúa desde ese punto. Si presiona 'Cancelar', el proceso se reinicia a cero.

### Requisitos funcionales
- Simulación de descarga en chunks de datos en un hilo secundario independiente.
- Máquina de estados completa para la descarga: `DETENIDO`, `DESCARGANDO`, `PAUSADO`, `CANCELADO`, `COMPLETADO`.
- Controles interactivos: Botones 'Iniciar', 'Pausar', 'Reanudar', 'Cancelar'.
- Actualización continua de: Porcentaje completado (0 a 100%), Bytes descargados vs Bytes totales, Velocidad de descarga estimada (KB/s) y Tiempo restante estimado (ETA).
- Comunicación segura con `queue.Queue` y sondeo reactivo con `.after()`.

### Requisitos de interfaz
- Barra de progreso estilizada destacada en el centro de la ventana.
- Panel de métricas de red: Velocidad, Descargado y Tiempo restante.
- Barra de botones de control que habilite o deshabilite opciones según el estado activo.

### Datos
- Descarga: total_bytes, bytes_descargados, velocidad_bps, estado, tiempo_restante.

### Estado
- Estado del hilo de descarga en memoria.
- Eventos de pausa (`threading.Event`) y cancelación.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- El tamaño del paquete debe ser mayor a cero.
- La velocidad de descarga simulada debe mantenerse en rangos verosímiles.

### Casos límite
- Pausar repetidamente en fracciones de segundo.
- Cancelar cuando la descarga está al 99%.
- Cerrar la ventana con la descarga corriendo.

### Manejo de errores
- Manejar la parada y liberación limpia de hilos evitando hilos huérfanos al cerrar la aplicación.

### Fundamentos de Python relacionados
- Sincronización avanzada de hilos utilizando `threading.Event` para pausar (`wait()`) y reanudar (`set()`).
- Fórmulas de estimación de tiempo restante (ETA): $\text{ETA} = \text{Bytes Restantes} / \text{Velocidad}$.

### Conceptos Tkinter relacionados
- Actualización fluida de barras de progreso y etiquetas de texto numéricas.
- Deshabilitación coordinada de botones de acción según el estado de la tarea.

### Herramientas para investigar
- Uso de `threading.Event.wait()` para pausar hilos sin bucles de espera activa (busy waiting).
- Estimación de velocidad de transferencia en streaming.

### Diseño de interfaz
¿Cómo asegurarías que el botón 'Pausar' se transforme en 'Reanudar' o se intercambie de manera coherente con la barra de herramientas?

### Diseño de variables
Usa nombres como `download_progress_bar`, `speed_label`, `downloaded_bytes_label`, `eta_label`, `start_btn`, `pause_btn`, `cancel_btn`, `pause_event`.

### Antes de programar
1. ¿Cómo se implementa una pausa en un hilo secundario usando `threading.Event` sin recurrir a un bucle `while pausado: time.sleep(0.1)` que desperdicia CPU?
2. ¿Cómo se calcula el tiempo restante (ETA) en segundos a partir de los bytes faltantes y la velocidad actual?

### Arquitectura
```
ejercicio_066/
├── app.py             # Interfaz visual, barra y métricas de red
├── download_worker.py # Hilo de transferencia por bloques con soporte de pausa/reanudación
└── network_math.py    # Estimación de velocidades y formato de tiempos (ETA)
```

### Pruebas mínimas
1. Iniciar descarga -> Presionar 'Pausar' al 40% -> Verificar que el progreso se congele y la velocidad marque 0 KB/s.
2. Presionar 'Reanudar' -> Verificar que continúe desde el 40% hasta llegar al 100% y marque 'Descarga completada'.

### Pruebas de error
1. Presionar 'Cancelar' al 60% -> Debe reiniciar la barra a 0%, detener el hilo y restaurar los botones iniciales.

### Experiencia de usuario
La barra debe llenarse con una animación visual limpia y el tiempo restante debe mostrarse en minutos y segundos legibles (ej. '01:25 restantes').

### Explicación posterior
¿Cómo permite el método `threading.Event.wait()` suspender la ejecución de un hilo de forma eficiente hasta que el usuario decida reanudarlo?

### Aplicación profesional
Lanzadores de actualizaciones de software de escritorio, gestores de descarga de archivos masivos y sincronizadores cloud.

### Reto adicional
Añade un selector de límite de ancho de banda (ej. 'Limitar a 500 KB/s', 'Sin límite') que regule la velocidad de transferencia simulada.

---
> [Índice General](../README.md) · [← Ejercicio 065](../ejercicio_065/README.md) · [Ejercicio 067 →](../ejercicio_067/README.md)
