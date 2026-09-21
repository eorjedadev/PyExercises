## Ejercicio 039 — Simulador y Explicador de Expresiones Cron (`cron-sim`)

> [← Ejercicio 038](../ejercicio_038/README.md) · [Índice General](../README.md) · [Ejercicio 040 →](../ejercicio_040/README.md)

### Contexto profesional
Al configurar tareas programadas en servidores Linux (`crontab`), flujos de trabajo de CI/CD (GitHub Actions schedules) o tareas periódicas en Kubernetes (`CronJobs`), los ingenieros necesitan comprender exactamente cuándo se ejecutará una expresión cron y simular las próximas N fechas de ejecución para evitar programaciones accidentales en horarios indebidos.

### Problema
Construir una CLI que parsee expresiones cron estándar de 5 campos (Minuto, Hora, Día del Mes, Mes, Día de la Semana), explique en lenguaje humano natural su significado, simule y liste las próximas N ejecuciones a partir de una fecha/hora dada y valide si una marca de tiempo específica coincide con la regla.

### Usuario objetivo
Administradores de sistemas, DevOps y desarrolladores.

### Objetivo
Crear un motor de parsing, explicación en lenguaje natural y simulación temporal de expresiones cron conforme al estándar POSIX.

### Ejemplo conceptual de uso
```bash
# Explicar una expresión cron en lenguaje natural
python cron_sim.py explain "*/15 2,4 * * 1-5"

# Simular las próximas 5 fechas de ejecución a partir de ahora
python cron_sim.py next "0 0 1 * *" --count 5

# Verificar si una fecha específica coincide con la expresión
python cron_sim.py test-match "0 12 * * *" --datetime "2026-06-15 12:00:00"
```

### Requisitos funcionales
- Parsear los 5 campos clásicos de cron: Minuto (0-59), Hora (0-23), Día del mes (1-31), Mes (1-12 o JAN-DEC), Día de la semana (0-7 o SUN-SAT, donde 0 y 7 son Domingo).
- Soportar operadores: comodín (`*`), listas (`1,2,5`), rangos (`10-15`), pasos (`*/5`, `1-30/2`).
- Subcomando `explain`: traduce la expresión a texto claro en español o inglés (ej. *'Cada 15 minutos, a las horas 02:00 y 04:00, de lunes a viernes'*).
- Subcomando `next`: calcula y muestra las próximas N fechas exactas de ejecución considerando la zona horaria indicada.
- Subcomando `test-match`: evalúa si una fecha dada hace match con la expresión (devuelve exit code 0 si coincide, 1 si no coincide).
- Soportar atajos estándar: `@yearly`, `@monthly`, `@weekly`, `@daily`, `@hourly`, `@reboot`.

### Requisitos de CLI
- Subcomandos: `explain`, `next`, `test-match`.
- Opción `-c / --count <N>` (default 5).
- Opción `--from-time <DATETIME>` (default ahora).
- Opción `--tz <TIMEZONE>` (default local).
- Exit code 0 en éxito, 1 si no hay match en `test-match`, 2 en sintaxis cron inválida.

### Entradas
- Cadena de expresión cron y parámetros de fecha.

### Salidas
- Explicación textual o lista de timestamps futuros en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Validar que la expresión tenga exactamente 5 campos separados por espacios (o sea un atajo reconocido).
- Validar rangos numéricos de cada campo (ej. minutos no pueden superar 59).
- Validar que los pasos (`/step`) sean enteros positivos mayores a 0.

### Casos límite
- Días del mes y días de la semana combinados (en cron estándar, si ambos están especificados no como `*`, la condición es una unión OR, no un AND estricto).
- Años bisiestos (ej. ejecuciones el 29 de febrero).
- Horarios de verano (cambios de hora DST).

### Manejo de errores
- `ValueError`: Explicar exactamente qué campo falló la validación.

### Fundamentos de Python relacionados
- Algoritmos de parsing de cadenas y rangos numéricos.
- Módulo `datetime` (`datetime.datetime`, `datetime.timedelta`) para simulación hacia adelante.
- Módulo `zoneinfo` para gestión de zonas horarias.

### Conceptos CLI relacionados
- Parsing de lenguajes de dominio específico (DSL).
- Herramientas de explicación y simulación de contratos temporales.

### Herramientas o módulos para investigar
- `datetime` y `zoneinfo`.
- `re`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías una opción para exportar la simulación de próximas ejecuciones a formato iCalendar (`.ics`) para importar en Google Calendar?

### Diseño de argumentos
¿Cómo nombrarías la opción para soportar cron de 6 campos con segundos (usado en Spring Framework / Quartz Scheduler)?

### Diseño de variables
`cron_tokens`, `minute_set`, `hour_set`, `day_set`, `month_set`, `weekday_set`, `simulated_dates_list`.

### Antes de programar
1. ¿Cómo expandir un token como `1-10/3` en el conjunto de enteros `{1, 4, 7, 10}`?
2. ¿Cómo simular el avance temporal minuto a minuto hasta encontrar las próximas N coincidencias sin caer en bucles infinitos para fechas imposibles (ej. 30 de febrero)?

### Arquitectura
Parser cron (`cron_parser.py`), motor de simulación (`cron_simulator.py`), traductor a lenguaje natural (`cron_explainer.py`) y CLI.

### Pruebas mínimas
1. Explicar `0 0 * * *` y verificar que traduzca 'Todos los días a medianoche'.
2. Simular `0 12 * * *` a partir de `2026-01-01 10:00` y verificar que las próximas 2 fechas sean `2026-01-01 12:00` y `2026-01-02 12:00`.

### Pruebas de error
1. Pasar `65 * * * *` (minuto inválido) -> Exit code 2 con mensaje de error.

### Experiencia de usuario
Explicación en lenguaje fluido y lista de fechas futuras numeradas con el día de la semana explícito.

### Explicación posterior
Explica la semántica especial de la especificación POSIX cuando se combinan día del mes (`DOM`) y día de la semana (`DOW`).

### Aplicación profesional
Diagnóstico de tareas programadas en servidores Linux, configuración de Kubernetes CronJobs y validación de pipelines.

### Reto adicional
Soportar la sintaxis de días hábiles (`W`) y último día del mes (`L`) propia de planificadores avanzados tipo Quartz.

---
> [← Ejercicio 038](../ejercicio_038/README.md) · [Índice General](../README.md) · [Ejercicio 040 →](../ejercicio_040/README.md)
