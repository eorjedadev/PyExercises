## Ejercicio 065 — Tablero de Estado de Servicios en Tiempo Real (`status-board`)

> [← Ejercicio 064](../ejercicio_064/README.md) · [Índice General](../README.md) · [Ejercicio 066 →](../ejercicio_066/README.md)

### Contexto profesional
En centros de operaciones de red (NOC) y salas de control de ingeniería, se requiere proyectar en pantallas dedicadas el estado en vivo de todos los servicios e infraestructura (APIs, bases de datos PostgreSQL, clústeres Kubernetes, colas de mensajería, balanceadores de carga) mediante un tablero visual en terminal auto-actualizable.

### Problema
Construir una CLI que lea una configuración de servicios e infraestructura, ejecute pruebas periódicas de conectividad y salud en segundo plano de forma concurrente, dibuje un tablero de control TUI (Terminal User Interface) con actualización en tiempo real, cálculo de uptime, gráficos de latencia en texto (sparklines) y soporte para modo observador (`--watch`).

### Usuario objetivo
Operadores de NOC, ingenieros de SRE y líderes de infraestructura.

### Objetivo
Crear un dashboard de estado de servicios interactivo en terminal con actualización dinámica sin parpadeo (flicker-free), cálculo de métricas y soporte de temas.

### Ejemplo conceptual de uso
```bash
# Iniciar el tablero de estado en tiempo real con actualización cada 5 segundos
python status_board.py watch --config services.json --interval 5

# Obtener una instantánea única del tablero en formato JSON o tabla estática
python status_board.py snapshot --config services.json --format table
```

### Requisitos funcionales
- Subcomando `watch`: limpia la pantalla de terminal y dibuja el tablero en vivo, actualizándose cada N segundos sin parpadeo usando secuencias de escape ANSI o posicionamiento de cursor.
- Monitoreo concurrente de servicios mediante `ThreadPoolExecutor` para que un servicio lento o caído no congele el refresco del resto del tablero.
- Mostrar por cada servicio: Nombre, Tipo (HTTP, TCP, Postgres, Ping), Estado (`OPERATIONAL`, `DEGRADED`, `OUTAGE`), Latencia actual en ms, Sparkline ASCII de tendencia de latencia reciente (` ▂▃▅▆▇`) y Uptime de la sesión %.
- Subcomando `snapshot`: emite una sola captura del estado actual en tabla o JSON para consumo de scripts.
- Interrupción limpia con `Ctrl+C` o tecla `q` restaurando el cursor y estado normal de la terminal.

### Requisitos de CLI
- Subcomandos: `watch`, `snapshot`.
- Opción `--config <RUTA>` (default `services.json`).
- Opción `-i / --interval <SEG>` (default 5).
- Flag `--no-color`: desactiva colores ANSI.
- Exit code 0 en terminación limpia, 1 si en `snapshot` hay servicios caídos, 2 en errores de configuración.

### Entradas
- Archivo de configuración de servicios y parámetros de refresco.

### Salidas
- TUI interactiva en tiempo real en terminal o tabla estática.

### Persistencia
Sin persistencia o guardado opcional de métricas en PostgreSQL/SQLite.

### Validaciones
- Comprobar que el archivo de configuración sea JSON válido.
- Validar que el intervalo de refresco sea un entero mayor o igual a 1 segundo.

### Casos límite
- Redimensionamiento de la ventana de la terminal durante la ejecución (manejo de señal `SIGWINCH` para recalcular dimensiones).
- Servicios que caen en timeout repetidamente.
- Decenas de servicios monitoreados simultáneamente.

### Manejo de errores
- Captura de errores de red en cada hilo individual sin afectar a los demás.
- Restauración de la terminal ante excepciones inesperadas.

### Fundamentos de Python relacionados
- Secuencias de control ANSI (limpieza de pantalla `\033[2J`, posicionamiento de cursor `\033[H`, ocultar/mostrar cursor `\033[?25l` / `\033[?25h`).
- Concurrencia con `concurrent.futures.ThreadPoolExecutor`.
- Módulo `time` y `shutil.get_terminal_size()`.
- Generación de caracteres Sparkline Unicode (` ▂▃▄▅▆▇█`).

### Conceptos CLI relacionados
- Interfaces de usuario en terminal (TUI) sin parpadeo.
- Monitoreo en vivo desatendido.

### Herramientas o módulos para investigar
- `shutil.get_terminal_size`.
- `concurrent.futures`.
- `time` y `socket`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para alternar entre vista compacta y vista detallada con una pulsación de tecla durante la ejecución?

### Diseño de argumentos
¿Cómo nombrarías la opción para enviar un sonido de campana audible (`\a`) cuando un servicio pase a estado `OUTAGE` (`--bell-on-outage`)?

### Diseño de variables
`monitored_services_list`, `probe_results_buffer`, `sparkline_latency_history`, `terminal_width_height`, `overall_system_status`.

### Antes de programar
1. ¿Cómo redibujar la pantalla de terminal sin parpadeos (flicker) construyendo todo el frame en una sola cadena de texto en memoria antes de hacer `sys.stdout.write(frame)`?
2. ¿Cómo mapear una serie de números de latencia a caracteres sparkline Unicode ` ▂▃▄▅▆▇█` según su valor relativo?

### Arquitectura
Sonda concurrente (`health_checker.py`), generador de TUI (`tui_renderer.py`), motor de sparklines (`sparkline.py`) y CLI.

### Pruebas mínimas
1. Ejecutar `snapshot` con un archivo de 3 servicios (incluyendo localhost y un endpoint externo) y verificar que la tabla estática muestre el estado de los 3.
2. Probar que `watch` responda inmediatamente a `Ctrl+C` restaurando la terminal.

### Pruebas de error
1. Pasar un archivo de configuración inexistente -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Tablero visual impactante: Encabezado con hora actual y estado global, filas alineadas con insignias verdes `[OK]` y rojas `[DOWN]`, y sparklines fluidos.

### Explicación posterior
Explica cómo funcionan los buffers de doble página y el renderizado atómico de frames en interfaces de terminal modernas.

### Aplicación profesional
Tableros de operaciones para equipos de guardia (NOC Dashboards), monitoreo de infraestructura de eventos masivos y consolas de SRE.

### Reto adicional
Implementar soporte para agrupar servicios por categoría o entorno (ej. sección `Databases`, sección `External APIs`, sección `Core Services`).

---
> [← Ejercicio 064](../ejercicio_064/README.md) · [Índice General](../README.md) · [Ejercicio 066 →](../ejercicio_066/README.md)
