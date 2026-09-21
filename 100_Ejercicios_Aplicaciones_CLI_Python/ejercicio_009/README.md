## Ejercicio 009 — Ajustador de Marcas de Tiempo en Logs (`log-shifter`)

> [← Ejercicio 008](../ejercicio_008/README.md) · [Índice General](../README.md) · [Ejercicio 010 →](../ejercicio_010/README.md)

### Contexto profesional
Al correlacionar logs de múltiples servidores distribuidos con zonas horarias desincronizadas, o al reproducir escenarios de prueba donde los logs deben parecer recientes, los ingenieros necesitan desplazar todas las marcas de tiempo de un archivo de logs en un delta específico (ej. +2 horas, -15 minutos).

### Problema
Construir una CLI que procese archivos de log, detecte marcas de tiempo en formato ISO 8601 o estándar (`YYYY-MM-DD HH:MM:SS`), sume o reste un intervalo de tiempo y emita el archivo resultante preservando el contenido original.

### Usuario objetivo
Ingenieros de fiabilidad de sitios (SRE), analistas de incidentes y desarrolladores.

### Objetivo
Desarrollar un transformador de logs con parsing de fechas, cálculo de deltas y preservación de formato.

### Ejemplo conceptual de uso
```bash
# Adelantar todas las fechas 2 horas y 30 minutos
python log_shifter.py app.log --shift "+2h30m"

# Retrasar fechas 1 día y guardar en nuevo archivo
python log_shifter.py access.log --shift "-1d" -o access_shifted.log
```

### Requisitos funcionales
- Detectar marcas de tiempo estándar en el inicio de cada línea de log.
- Parsear expresiones de desplazamiento temporal (ej. `+3h`, `-45m`, `+1d12h`, `-30s`).
- Aplicar el cálculo de `datetime.timedelta` a cada timestamp encontrado.
- Formatear el timestamp nuevo con el mismo patrón exacto del original.
- Emitir las líneas modificadas preservando el resto del mensaje intacto.

### Requisitos de CLI
- Argumento posicional: archivo de log a procesar.
- Opción obligatoria `--shift <DELTA>` (ej. `+2h`, `-15m`).
- Opción opcional `-o / --output <RUTA>` (si no se define, emite a STDOUT).
- Exit code 0 en éxito, 1 si el formato del delta es inválido, 2 en errores de archivo.

### Entradas
- Archivo de log.
- Expresión de delta temporal.

### Salidas
- Logs transformados en STDOUT o en archivo de salida.

### Persistencia
Escritura en archivo si se usa `-o`.

### Validaciones
- Validar la sintaxis del delta con regex (debe iniciar con `+` o `-` seguido de pares número-unidad: `d`, `h`, `m`, `s`).
- Comprobar que el archivo de entrada exista.

### Casos límite
- Líneas de log sin marca de tiempo (líneas de continuación de stack trace multilínea; deben emitirse sin cambios).
- Cambios de año bisiesto o saltos de mes al aplicar el desplazamiento.
- Archivos con mezclas de formatos de fecha.

### Manejo de errores
- Error de parseo de delta.
- Errores de lectura/escritura de archivos.

### Fundamentos de Python relacionados
- Módulo estándar `datetime` (`datetime.datetime`, `datetime.timedelta`).
- Expresiones regulares (`re.sub`, grupos de captura con `re.compile`).
- Procesamiento de archivos línea a línea.

### Conceptos CLI relacionados
- Flags obligatorios vs posicionales.
- Streaming de archivos para evitar saturación de memoria.

### Herramientas o módulos para investigar
- `datetime`.
- `re`.
- `argparse`.

### Diseño de comandos
¿Cómo permitirías especificar un formato de fecha personalizado mediante `--date-format` (ej. `"%b %d %H:%M:%S"` para syslog clásico)?

### Diseño de argumentos
¿Cómo soportarías especificar una zona horaria de origen y destino (`--from-tz UTC --to-tz America/Bogota`)?

### Diseño de variables
`shift_delta`, `time_pattern`, `delta_timedelta`, `matched_timestamp`, `shifted_timestamp`, `line_buffer`.

### Antes de programar
1. ¿Cómo parsear un string como `+2h30m` para convertirlo en un objeto `timedelta(hours=2, minutes=30)`?
2. ¿Cómo asegurar que las líneas que no coincidan con el patrón de fecha pasen directamente a la salida?

### Arquitectura
Función `parse_delta(delta_str)`, función `shift_line(line, delta, regex)` y función `process_stream(input_file, output_stream)`.

### Pruebas mínimas
1. Procesar un log con fecha `2026-03-01 10:00:00` con `--shift "+2h"` y comprobar que resulte `2026-03-01 12:00:00`.
2. Comprobar que los stack traces multilínea mantengan su indentación.

### Pruebas de error
1. Pasar `--shift "invalido"` -> Exit code 1 con explicación del formato admitido.

### Experiencia de usuario
La salida por STDOUT debe ser limpia para posibilitar pipes (`python log_shifter.py app.log --shift "+1h" | grep ERROR`).

### Explicación posterior
Explica la diferencia entre fechas naive (ingenuas) y fechas aware (con información de zona horaria) en Python.

### Aplicación profesional
Normalización de telemetría forense e inyección de datos para pruebas de estrés en motores SIEM (Elasticsearch, Splunk).

### Reto adicional
Añadir soporte para timestamps en formato UNIX epoch en milisegundos y segundos.

---
> [← Ejercicio 008](../ejercicio_008/README.md) · [Índice General](../README.md) · [Ejercicio 010 →](../ejercicio_010/README.md)
