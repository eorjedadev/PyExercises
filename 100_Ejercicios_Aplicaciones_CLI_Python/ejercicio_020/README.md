## Ejercicio 020 — Parser y Filtro de Syslog RFC5424/RFC3164 (`syslog-filter`)

> [← Ejercicio 019](../ejercicio_019/README.md) · [Índice General](../README.md) · [Ejercicio 021 →](../ejercicio_021/README.md)

### Contexto profesional
Los servidores Linux y dispositivos de red (switches, routers, firewalls) generan miles de eventos por segundo en formato syslog estándar. Los administradores necesitan filtrar eventos por nivel de severidad (Emergency, Alert, Critical, Error, Warning, Notice, Info, Debug) o por facilidad (auth, daemon, kern, mail) sin lidiar con expresiones regulares complejas manualmente.

### Problema
Construir una CLI que procese archivos de syslog o entradas en tiempo real, decodifique el valor numérico de prioridad (`PRI = Facility * 8 + Severity`), extraiga timestamps, hostnames y nombres de proceso, y filtre según criterios definidos.

### Usuario objetivo
Administradores de sistemas Linux, operadores de NOC e ingenieros de seguridad.

### Objetivo
Crear un parser de eventos syslog conforme a RFC 3164/5424 con cálculo de PRI, filtrado por severidad y formateo estructurado.

### Ejemplo conceptual de uso
```bash
# Filtrar eventos con severidad Error o superior (<= 3)
python syslog_filter.py /var/log/syslog --min-severity error

# Filtrar solo eventos de autenticación (facility auth/authpriv) en formato JSON
python syslog_filter.py /var/log/secure --facility auth,authpriv --json
```

### Requisitos funcionales
- Parsear líneas con formato syslog estándar: `<PRI>TIMESTAMP HOSTNAME APP-NAME[PID]: MSG` o formato clásico `/var/log/syslog`.
- Decodificar el campo `<PRI>`: $Facility = \lfloor PRI / 8 \rfloor$, $Severity = PRI \pmod 8$.
- Filtrar por severidad mínima (ej. `--min-severity warning` muestra Warning, Error, Critical, Alert, Emergency).
- Filtrar por lista de facilidades (`--facility daemon,kern`).
- Filtrar por nombre de aplicación (`--app nginx`).
- Emitir salida en formato legible o JSON.

### Requisitos de CLI
- Argumento posicional opcional: archivo de syslog (default STDIN).
- Opción `--min-severity`: `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`.
- Opción `--facility`: lista de facilidades.
- Opción `--app`: nombre de proceso/aplicación.
- Flag `--json`.
- Exit code 0 en éxito, 1 si no se encontraron coincidencias, 2 en errores de archivo.

### Entradas
- Archivo de syslog o flujo continuo.

### Salidas
- Eventos filtrados en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Validar que los nombres de severidad y facilidad ingresados sean válidos según el estándar RFC.

### Casos límite
- Mensajes de log multilínea.
- Líneas de syslog que no contienen el campo `<PRI>` explícito (formato local sin cabecera PRI).
- Eventos con marcas de tiempo en formato BSD antiguo (`Oct 11 22:14:15`) vs ISO 8601.

### Manejo de errores
- Descarte o marcado de líneas mal formadas sin interrumpir el procesamiento del resto del archivo.

### Fundamentos de Python relacionados
- Expresiones regulares con grupos nombrados (`(?P<name>...)`).
- Operaciones aritméticas y mapas de constantes para severidades y facilidades.
- Módulo `sys` e iteradores.

### Conceptos CLI relacionados
- Decodificación de protocolos estándar en terminal.
- Filtrado basado en rangos jerárquicos de severidad.

### Herramientas o módulos para investigar
- `re`.
- `sys.stdin`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para mostrar una tabla de estadísticas con el recuento de eventos por severidad (`--stats`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para buscar un texto específico en el cuerpo del mensaje (`--message-contains "segfault"`)?

### Diseño de variables
`pri_value`, `facility_code`, `facility_name`, `severity_code`, `severity_name`, `parsed_syslog_entry`.

### Antes de programar
1. ¿Cómo se calcula la severidad a partir del número PRI `<134>`? ($134 = 16 \times 8 + 6$, donde 16 es `local0` y 6 es `info`).
2. ¿Cómo diseñar la expresión regular para que admita tanto RFC 3164 como RFC 5424?

### Arquitectura
Módulo de decodificación y parsing (`syslog_parser.py`), evaluador de filtros (`filter_evaluator.py`) y CLI.

### Pruebas mínimas
1. Procesar un dataset de prueba con eventos de diversas severidades y validar que `--min-severity err` solo deje pasar códigos 0, 1, 2 y 3.
2. Validar que la decodificación de `<34>` resulte en Facility `auth` (4) y Severity `crit` (2).

### Pruebas de error
1. Pasar `--min-severity no_existe` -> Exit code 2 con la lista de severidades válidas.

### Experiencia de usuario
Colorear la severidad según nivel (Rojo para emergencias/errores, Amarillo para warnings, Azul para info).

### Explicación posterior
Explica la arquitectura del protocolo syslog según RFC 5424 y por qué la separación en facility/severity facilita el enrutamiento de logs.

### Aplicación profesional
Diagnóstico en servidores de producción, ingestión en pipelines SIEM y monitoreo de seguridad.

### Reto adicional
Implementar un modo de escucha UDP en vivo (`--listen-udp 5140`) para recibir y filtrar eventos syslog en tiempo real por la red.

---
> [← Ejercicio 019](../ejercicio_019/README.md) · [Índice General](../README.md) · [Ejercicio 021 →](../ejercicio_021/README.md)
