## Ejercicio 070 — Simulador de Sensor IoT y Adquisición Continua de Datos (`IotTelemetrySimulatorApp`)

> [Índice General](../README.md) · [← Ejercicio 069](../ejercicio_069/README.md) · [Ejercicio 071 →](../ejercicio_071/README.md)

### Contexto profesional
En plantas químicas y salas de servidores de centros de datos, los operadores de monitoreo supervisan en tiempo real la telemetría de sensores industriales de temperatura, presión y humedad.

### Usuario objetivo
Operador de planta o ingeniero de automatización y control.

### Problema
El flujo ininterrumpido de telemetría de alta frecuencia puede saturar el hilo principal de la interfaz si se intenta procesar cada paquete de datos de forma síncrona.

### Objetivo
Construir una consola de adquisición de telemetría IoT donde un hilo secundario (`threading`) genere lecturas de sensores (Temperatura en °C, Presión en PSI, Humedad en %) a una tasa constante de 5 lecturas por segundo, enviando las muestras a través de `queue.Queue`, mientras el hilo principal de Tkinter sondea la cola cada 200 ms con `after()` para actualizar medidores visuales y una tabla de registro continuo.

### Flujo principal
El operador presiona 'Iniciar Adquisición'. El hilo simulador comienza a emitir paquetes de telemetría a la cola. El hilo principal de Tkinter consume los paquetes acumulados cada 200 ms, actualiza las etiquetas con los valores instantáneos, ajusta una barra de nivel visual y agrega la fila al historial del `Treeview`. Si la temperatura supera los 80 °C, se activa una alarma visual en rojo.

### Requisitos funcionales
- Generador de telemetría en hilo de fondo (`threading.Thread(daemon=True)`) que produzca lecturas periódicas con `random.gauss` o fluctuaciones realistas.
- Sensores simulados: Temperatura (20 a 100 °C), Presión (30 a 70 PSI) y Humedad (20 a 90 %).
- Envío seguro de paquetes mediante `queue.Queue`.
- Bucle de sondeo reactivo en el hilo de Tkinter con `root.after(200, polling_callback)` que consuma todos los eventos pendientes con `queue.get_nowait()`.
- Visualización en tiempo real: Panel de lectura instantánea y `ttk.Treeview` con historial de las últimas 50 lecturas.
- Alarma visual si la temperatura excede el umbral crítico de 80 °C.

### Requisitos de interfaz
- Panel superior con tarjetas de lectura instantánea destacadas en tipografía grande.
- Indicador de alarma en rojo parpadeante cuando se excedan los umbrales de seguridad.
- `Treeview` de histórico con scrollbar que mantenga como máximo 50 filas para evitar consumo excesivo de memoria.

### Datos
- Paquete de telemetría: timestamp, sensor_id, temperatura (float), presion (float), humedad (float), estado_alarma (bool).

### Estado
- Estado de adquisición activa.
- Cola de telemetría thread-safe.
- Buffer de las últimas 50 muestras.

### Persistencia
No requiere persistencia en disco en esta fase (telemetría volátil en vivo).

### Validaciones
- Verificar que el bucle de sondeo no bloquee la interfaz si la cola acumula muchos paquetes (procesar en lote hasta vaciar con `Empty`).

### Casos límite
- Pausar y reanudar la adquisición.
- Cierre de la ventana mientras el hilo emisor está en plena generación de datos.

### Manejo de errores
- Capturar `queue.Empty` limpiamente en el bucle de consumo de eventos.

### Fundamentos de Python relacionados
- Simulación de variables físicas continuas con fluctuaciones gaussianas (`random.gauss`).
- Manejo de estructuras de cola con límite de capacidad o buffers circulares (`collections.deque`).

### Conceptos Tkinter relacionados
- Consumo exhaustivo de colas con bucle `while True: try queue.get_nowait() ... except Empty: break`.
- Desplazamiento automático de tablas manteniendo un número fijo de filas visibles.

### Herramientas para investigar
- Excepción `queue.Empty` en Python.
- Métodos de manipulación rápida de filas en `ttk.Treeview`.

### Diseño de interfaz
¿Cómo asegurarías que las tarjetas de lectura instantánea sean legibles a distancia para un operador de panel de control?

### Diseño de variables
Usa nombres como `telemetry_tree`, `temp_gauge_label`, `press_gauge_label`, `humidity_gauge_label`, `alarm_banner`, `start_stream_btn`, `telemetry_queue`.

### Antes de programar
1. ¿Cómo se vacía completamente una cola en cada ciclo de `after()` usando un bucle `while True` con `get_nowait()` para no acumular retraso en la interfaz?
2. ¿Cómo se limita el `Treeview` a un máximo de 50 filas eliminando la fila más antigua cuando se agrega una nueva?

### Arquitectura
```
ejercicio_070/
├── app.py             # Consola de monitoreo, medidores y Treeview
├── iot_simulator.py   # Hilo emisor de paquetes de telemetría física
└── telemetry_model.py # Estructura de paquetes y evaluación de alarmas
```

### Pruebas mínimas
1. Iniciar adquisición -> Comprobar que las tarjetas de temperatura y presión se actualicen suavemente cada 200 ms sin tirones.
2. Verificar que el Treeview se mantenga en un máximo de 50 filas sin crecer indefinidamente.

### Pruebas de error
1. Simular un pico de temperatura mayor a 80 °C -> La tarjeta debe tornarse roja y el banner de alarma debe activarse de inmediato.

### Experiencia de usuario
La actualización debe sentirse suave, continua y sin parpadeos perceptibles en los medidores numéricos.

### Explicación posterior
¿Cómo garantiza el patrón de consumo exhaustivo de la cola con `get_nowait()` que la interfaz gráfica no sufra de desfase temporal respecto a los datos producidos?

### Aplicación profesional
Paneles SCADA de supervisión industrial, consolas de monitoreo de centros de cómputo y estaciones meteorológicas locales.

### Reto adicional
Añade un botón 'Exportar Muestras Recientes a CSV' que guarde las últimas 50 lecturas capturadas en un archivo delimitado por comas.

---
> [Índice General](../README.md) · [← Ejercicio 069](../ejercicio_069/README.md) · [Ejercicio 071 →](../ejercicio_071/README.md)
