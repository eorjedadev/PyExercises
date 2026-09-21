## Ejercicio 037 — Temporizador y Registro de Sesiones de Enfoque Pomodoro (`pomo-cli`)

> [← Ejercicio 036](../ejercicio_036/README.md) · [Índice General](../README.md) · [Ejercicio 038 →](../ejercicio_038/README.md)

### Contexto profesional
En entornos de trabajo remoto e ingeniería de software de alta concentración, aplicar técnicas de productividad como la técnica Pomodoro (bloques de 25 minutos de trabajo intenso seguidos de 5 minutos de descanso) permite mantener el enfoque y evitar el agotamiento.

### Problema
Construir una CLI interactiva que ejecute temporizadores de enfoque Pomodoro y descansos, muestre una barra de progreso en terminal en tiempo real, emita campanas audibles (ASCII bell `\a`) o notificaciones del sistema, capture la interrupción de usuario (`Ctrl+C`) de forma elegante para registrar el motivo de pausa y persista el historial de sesiones con tags y tareas.

### Usuario objetivo
Desarrolladores, estudiantes y profesionales del conocimiento.

### Objetivo
Implementar un temporizador de productividad con renderizado dinámico en terminal, manejo de señales POSIX (`SIGINT`), alertas de audio y journal histórico.

### Ejemplo conceptual de uso
```bash
# Iniciar una sesión de enfoque de 25 minutos asociada a una tarea
python pomo_cli.py start --work 25 --task "Refactorizar módulo de autenticación" --tag "dev"

# Iniciar descanso corto de 5 minutos
python pomo_cli.py break --short 5

# Ver estadísticas de horas de enfoque por tag en la semana
python pomo_cli.py stats --period week
```

### Requisitos funcionales
- Subcomando `start`: inicia cuenta regresiva de enfoque (default 25 minutos), mostrando barra de progreso animada `[████░░░░] 18:30` en la misma línea de terminal usando retorno de carro `\r`.
- Subcomando `break`: ejecuta descanso corto (default 5 min) o largo (default 15 min).
- Subcomando `history`: lista las sesiones completadas, interrumpidas y tiempo total acumulado.
- Subcomando `stats`: genera agregados de tiempo total enfocado por etiqueta y día.
- Manejo de señal `SIGINT` (`Ctrl+C`): al interrumpir, pausar el reloj, preguntar si se desea cancelar o registrar como sesión parcial y guardar los minutos reales completados.

### Requisitos de CLI
- Subcomandos: `start`, `break`, `history`, `stats`.
- Opciones de `start`: `-w / --work <MINUTOS>`, `-t / --task <TEXTO>`, `--tag <TAG>`.
- Flag `--no-sound`: desactiva alertas sonoras.
- Exit code 0 en sesión completada o consulta exitosa, 1 en sesión interrumpida/cancelada.

### Entradas
- Tiempos en minutos, descripciones de tarea y comandos.

### Salidas
- Barra de progreso animada en terminal y tablas estadísticas.

### Persistencia
Archivo JSON o SQLite local en `~/.pomo_history.json`.

### Validaciones
- Los minutos deben ser enteros positivos mayores a 0.
- Formato de etiquetas sin espacios.

### Casos límite
- Interrupción inmediata en el segundo 0.
- Ejecución en entornos sin soporte de secuencias de escape ANSI o sin sonido.

### Manejo de errores
- Captura de `KeyboardInterrupt` / señal `signal.SIGINT`.

### Fundamentos de Python relacionados
- Módulos `time` (`time.sleep()`, `time.time()`), `signal`, `sys` (`sys.stdout.write`, `sys.stdout.flush`).
- Formateo dinámico con retorno de carro `\r` para animar en una sola línea.
- Persistencia de registros con timestamps.

### Conceptos CLI relacionados
- Renderizado dinámico en línea sin salto de línea (in-place animation).
- Gestión limpia de señales del sistema operativo.

### Herramientas o módulos para investigar
- `time`.
- `signal`.
- `sys.stdout`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `config set` para guardar la duración predeterminada de trabajo y descanso?

### Diseño de argumentos
¿Cómo nombrarías la opción para encadenar automáticamente ciclos (ej. 4 pomodoros seguidos de un descanso largo con `--cycles 4`)?

### Diseño de variables
`work_duration_seconds`, `remaining_seconds`, `progress_bar_str`, `active_task_name`, `session_history_log`.

### Antes de programar
1. ¿Cómo asegurar que `\r` sobrescriba exactamente la línea anterior sin dejar caracteres residuales si la longitud del texto cambia?
2. ¿Cómo capturar `signal.signal(signal.SIGINT, handler)` para que el usuario pueda ingresar un motivo de pausa mediante `input()`?

### Arquitectura
Temporizador dinámico (`timer_engine.py`), gestor de journal (`session_repository.py`) y CLI (`pomo_cli.py`).

### Pruebas mínimas
1. Ejecutar una sesión de 5 segundos de prueba y verificar que se complete y guarde en el historial con fecha y duración exacta.
2. Ejecutar `stats` y verificar que la suma de minutos sea correcta.

### Pruebas de error
1. Interrumpir con `Ctrl+C` y verificar que registre el estado como `INTERRUPTED` sin corromper el archivo de datos.

### Experiencia de usuario
Animación fluida de la barra de progreso, cuenta regresiva clara y sonido de campana al finalizar.

### Explicación posterior
Explica la diferencia entre el caracter de salto de línea `\n` (Line Feed) y el caracter de retorno de carro `\r` (Carriage Return).

### Aplicación profesional
Herramientas de seguimiento de horas facturables (time tracking) y gestión del tiempo personal.

### Reto adicional
Integrar notificaciones de escritorio nativas del sistema operativo usando comandos nativos (`notify-send` en Linux, PowerShell Toast en Windows, `osascript` en macOS).

---
> [← Ejercicio 036](../ejercicio_036/README.md) · [Índice General](../README.md) · [Ejercicio 038 →](../ejercicio_038/README.md)
