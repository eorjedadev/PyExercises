## Ejercicio 088 — Replayer de Streams de Eventos con Control de Velocidad (`event-replayer`)

> [← Ejercicio 087](../ejercicio_087/README.md) · [Índice General](../README.md) · [Ejercicio 089 →](../ejercicio_089/README.md)

### Contexto profesional
Al probar sistemas de procesamiento de datos en tiempo real (pipelines de Kafka, motores de detección de fraude, backends de analítica web), los ingenieros necesitan reproducir millones de eventos históricos grabados en disco (JSON Lines / CSV) hacia un endpoint HTTP, socket TCP o cola de mensajería, manteniendo los intervalos de tiempo relativos originales o acelerando la reproducción (ej. reproducir 24 horas de tráfico en 15 minutos a velocidad 10x).

### Problema
Construir una CLI de alto rendimiento que lea archivos de eventos históricos con timestamps, reproduzca los eventos hacia un destino configurado respetando los deltas de tiempo originales, soporte multiplicadores de velocidad (`--speed 2.0`, `--speed 10.0` o `--max-speed`), permita pausar/reanudar interactivamente y reporte métricas de emisión en tiempo real.

### Usuario objetivo
Ingenieros de datos, desarrolladores de streaming y QA engineers.

### Objetivo
Crear un reproductor de streams de eventos con control de tasa temporal de alta precisión, streaming de archivos gigantes y múltiples destinos de salida.

### Ejemplo conceptual de uso
```bash
# Reproducir eventos hacia un webhook HTTP al doble de velocidad original (2x)
python event_replayer.py play events.jsonl --target-url "http://localhost:8000/events" --speed 2.0

# Reproducir eventos hacia un socket TCP a máxima velocidad posible
python event_replayer.py play events.csv --target-tcp "localhost:9092" --speed max --timestamp-field "created_at"
```

### Requisitos funcionales
- Leer archivos de eventos estructurados en JSON Lines (`.jsonl`) o CSV línea a línea en streaming constante.
- Extraer la marca de tiempo de cada evento según el campo configurado (`--timestamp-field`).
- Calcular el delta de tiempo relativo entre eventos consecutivos: $\Delta t = t_{n} - t_{n-1}$.
- Control de velocidad mediante multiplicador `--speed <FACTOR>`: tiempo de espera real = $\frac{\Delta t}{\text{factor}}$. Si `--speed max`, emitir sin pausas intermedias.
- Soportar destinos de emisión:
  - `HTTP POST`: envía cada evento como payload JSON.
  - `TCP Socket`: escribe los bytes del evento en un socket de red.
  - `STDOUT`: emite en consola con las pausas temporales para encadenar con pipes.
- Control interactivo por teclado durante la reproducción: barra espaciadora para Pausar/Reanudar, teclas `+` y `-` para aumentar o reducir la velocidad al vuelo.
- Subcomando `stats`: analiza el archivo histórico calculando duración total grabada, tasa promedio de eventos por segundo y picos de tráfico.

### Requisitos de CLI
- Subcomandos: `play`, `stats`.
- Argumento posicional: archivo de eventos a reproducir.
- Opción `--speed <FACTOR>` (default `1.0`, o valor `max`).
- Opción `--target-url <URL>` o `--target-tcp <HOST:PORT>`.
- Opción `--timestamp-field <CAMPO>` (default `timestamp`).
- Opción `--loop`: repite la reproducción indefinidamente al llegar al final.
- Exit code 0 en reproducción completada, 1 en fallo de destino de red, 2 en errores de archivo.

### Entradas
- Archivo de eventos con timestamps y opciones de destino.

### Salidas
- Emisión de eventos hacia el destino configurado y métricas de reproducción en terminal.

### Persistencia
Sin persistencia.

### Validaciones
- Comprobar que el archivo de eventos exista y contenga el campo de timestamp indicado.
- El factor de velocidad debe ser un número positivo mayor a 0 o `max`.

### Casos límite
- Eventos desordenados cronológicamente en el archivo (ofrecer opción `--sort-buffer` para ordenar en ventanas de memoria).
- Pausas históricas gigantes entre eventos (ej. 8 horas nocturnas sin eventos; opción `--max-pause <SEG>` para limitar la pausa máxima).
- Archivos de eventos de decenas de gigabytes.

### Manejo de errores
- `urllib.error.URLError` o `socket.error` al enviar eventos.
- Errores de parsing de fechas ISO / Epoch.

### Fundamentos de Python relacionados
- Módulos `time` (`time.sleep()`, `time.perf_counter()`) para temporización de alta precisión.
- Generadores e iteradores para streaming de archivos sin cargar todo en RAM.
- Módulos `urllib.request` y `socket` para despacho de red.
- Captura de pulsaciones de teclas en terminal interactiva sin bloqueo (`sys.stdin` con `termios`/`msvcrt`).

### Conceptos CLI relacionados
- Simulación de cargas de trabajo de producción y replay de eventos en terminal.
- Control interactivo de ejecución al vuelo.

### Herramientas o módulos para investigar
- `time` y `datetime`.
- `socket` y `urllib.request`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para reescribir los timestamps de los eventos para que parezcan recién generados en el instante actual (`--rewrite-timestamps`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para limitar la cantidad máxima de eventos por segundo (Rate Throttling, ej. `--max-eps 500`)?

### Diseño de variables
`event_stream_generator`, `previous_event_timestamp`, `current_event_timestamp`, `scaled_sleep_duration_seconds`, `emitted_events_counter`.

### Antes de programar
1. ¿Cómo calcular el tiempo de espera relativo preciso compensando el tiempo que toma procesar y enviar la petición HTTP para evitar desfases acumulativos de reloj (Clock Drift)?
2. ¿Cómo parsear timestamps que pueden venir tanto en formato ISO 8601 (`2026-06-15T12:00:00Z`) como en enteros de milisegundos Epoch (`1781524800000`)?

### Arquitectura
Lector de streams (`stream_reader.py`), temporizador de precisión (`rate_controller.py`), despachador de destinos (`sink_dispatcher.py`) y CLI.

### Pruebas mínimas
1. Reproducir un archivo de 5 eventos con deltas de 1 segundo a velocidad `2.0x` hacia un servidor HTTP local y verificar que la reproducción total tarde exactamente 2.0 segundos (la mitad del tiempo original).
2. Probar `--speed max` y verificar que emita todos los eventos instantáneamente.

### Pruebas de error
1. Pasar un archivo con campo de timestamp inexistente -> Exit code 2 con error descriptivo.

### Experiencia de usuario
Barra de estado dinámica en terminal: `[REPRODUCIENDO 2.0x] Evento 1,420/10,000 | Tasa: 84 ev/s | Progreso: 14.2% | [Espacio] Pausar`.

### Explicación posterior
Explica el valor de las pruebas de regresión basadas en replay de tráfico real (Traffic Shadowing / Replay Testing) frente a datos sintéticos aleatorios.

### Aplicación profesional
Pruebas de estrés de pipelines de datos Kafka/Flink, validación de modelos de Machine Learning y benchmarking de sistemas de eventos.

### Reto adicional
Implementar un destino de salida directo hacia topics de Apache Kafka o colas RabbitMQ mediante adaptadores modulares.

---
> [← Ejercicio 087](../ejercicio_087/README.md) · [Índice General](../README.md) · [Ejercicio 089 →](../ejercicio_089/README.md)
