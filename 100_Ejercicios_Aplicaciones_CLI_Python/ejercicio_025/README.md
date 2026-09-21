## Ejercicio 025 — Conversor de Horarios y Planificador de Zonas Horarias (`tz-shift`)

> [← Ejercicio 024](../ejercicio_024/README.md) · [Índice General](../README.md) · [Ejercicio 026 →](../ejercicio_026/README.md)

### Contexto profesional
En equipos de ingeniería globales y distribuidos geográficamente (ej. San Francisco, Londres, Bogotá, Tokio), coordinar horarios de despliegue, ventanas de mantenimiento nocturno o reuniones sin cometer errores de horario de verano (DST) es un desafío diario.

### Problema
Construir una CLI que convierta una fecha y hora dada entre múltiples zonas horarias simultáneamente, liste las horas hábiles coincidentes (overlap de jornada laboral 9:00 a 18:00) entre dos o más ciudades y reporte si alguna zona se encuentra en horario de verano.

### Usuario objetivo
Líderes de equipo, ingenieros de operaciones y gestores de proyectos globales.

### Objetivo
Crear un calculador y visualizador de zonas horarias con soporte IANA, detección de solapamiento de horarios laborales y formateo tabular.

### Ejemplo conceptual de uso
```bash
# Convertir una hora específica a múltiples zonas horarias
python tz_shift.py "2026-06-15 14:00" --from-tz "America/Bogota" --to-tz "UTC,Europe/London,Asia/Tokyo"

# Encontrar ventana de solapamiento laboral entre 3 ciudades
python tz_shift.py --overlap --zones "America/New_York,Europe/Madrid,America/Bogota"
```

### Requisitos funcionales
- Parsear fecha y hora en formatos estándar (ISO 8601 o `YYYY-MM-DD HH:MM`). Si se omite la hora, asumir la hora actual del sistema.
- Manejar base de datos de zonas horarias IANA oficial (ej. `America/Bogota`, `UTC`, `Europe/Berlin`, `Asia/Tokyo`).
- Convertir y mostrar la hora equivalente en todas las zonas solicitadas.
- Indicar offset UTC (ej. `UTC-5`, `UTC+2`) y si la zona está actualmente en Horario de Verano (DST).
- Modo `--overlap`: calcula y muestra una matriz horaria de 24 horas destacando las franjas de coincidencia de jornada laboral (9am a 6pm).

### Requisitos de CLI
- Argumento posicional opcional: fecha y hora a convertir (default `now`).
- Opción `--from-tz <ZONA>`: zona horaria de origen (default zona local del sistema).
- Opción `--to-tz <ZONAS>`: lista separada por comas de zonas de destino.
- Flag `--overlap`: modo de cálculo de solapamiento laboral.
- Opción `--zones <ZONAS>`: zonas para el modo overlap.
- Exit code 0 en éxito, 1 si el nombre de zona horaria es inválido, 2 en errores de argumentos.

### Entradas
- Fecha/hora y nombres de zonas IANA.

### Salidas
- Tabla comparativa de horarios y matriz de solapamiento en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Validar que los nombres de zona horaria existan en la base de datos `zoneinfo`.
- Validar formato de fecha/hora.

### Casos límite
- Días de cambio de horario de verano (transiciones de DST de 23 o 25 horas en primavera/otoño).
- Conversiones que cruzan la medianoche y cambian de día calendario.
- Horas ambiguas o inexistentes durante el cambio de hora (manejo con `fold` en `datetime`).

### Manejo de errores
- `zoneinfo.ZoneInfoNotFoundError`: Indicar que la zona horaria no existe y sugerir nombres válidos.
- `ValueError` en formato de fecha.

### Fundamentos de Python relacionados
- Módulo estándar `zoneinfo` (`zoneinfo.ZoneInfo`) introducido en Python 3.9+.
- Módulo `datetime` (`datetime.datetime`, `datetime.timezone`).
- Módulo `time`.
- Formateo visual y alineación de matrices horarias.

### Conceptos CLI relacionados
- Visualización interactiva de matrices temporales en terminal.
- Gestión robusta de estándares internacionales de tiempo.

### Herramientas o módulos para investigar
- `zoneinfo`.
- `datetime`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías un subcomando `list-zones` para buscar zonas por país o continente con autocompletado?

### Diseño de argumentos
¿Cómo permitirías cambiar el rango de jornada laboral (ej. `--work-hours 8-17`)?

### Diseño de variables
`source_timezone`, `target_timezones_list`, `base_datetime_aware`, `converted_datetimes`, `overlap_matrix`.

### Antes de programar
1. ¿Por qué nunca se debe calcular la hora de otra ciudad sumando o restando horas fijas a mano (ej. `utc - 5`) en lugar de usar `ZoneInfo` con la base de datos IANA?
2. ¿Cómo funciona el atributo `fold` en `datetime` para desambiguar la hora repetida durante el cambio de horario?

### Arquitectura
Motor de conversión temporal (`tz_engine.py`), generador de matriz de solapamiento (`overlap_grid.py`) y CLI.

### Pruebas mínimas
1. Convertir `2026-01-15 12:00` de `America/Bogota` a `UTC` y verificar que sea `17:00 UTC`.
2. Ejecutar `--overlap` con 2 zonas en el mismo huso horario y verificar que el solapamiento sea del 100% de la jornada laboral.

### Pruebas de error
1. Pasar `--from-tz "Zona/Falsa"` -> Exit code 1 con mensaje de zona no encontrada.

### Experiencia de usuario
Matriz visual con colores donde las horas coincidentes se muestren en verde y las horas no hábiles o nocturnas en gris/rojo.

### Explicación posterior
Explica la diferencia entre UTC (estándar de tiempo físico) y GMT/Husos horarios (definiciones políticas con DST).

### Aplicación profesional
Planificación de mantenimientos de infraestructura de alta disponibilidad y coordinación de equipos internacionales de SRE.

### Reto adicional
Generar automáticamente un enlace web de calendario (`Google Calendar / Outlook`) con la fecha y hora convertidas para compartir rápidamente con el equipo.

---
> [← Ejercicio 024](../ejercicio_024/README.md) · [Índice General](../README.md) · [Ejercicio 026 →](../ejercicio_026/README.md)
