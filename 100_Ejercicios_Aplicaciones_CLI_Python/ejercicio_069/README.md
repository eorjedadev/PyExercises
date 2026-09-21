## Ejercicio 069 — Detector de Desviación de Configuración del Sistema (`drift-checker`)

> [← Ejercicio 068](../ejercicio_068/README.md) · [Índice General](../README.md) · [Ejercicio 070 →](../ejercicio_070/README.md)

### Contexto profesional
En infraestructuras inmutables y gestión de configuración declarativa (GitOps / Ansible / Chef), los servidores de producción deben coincidir exactamente con una línea base (baseline) aprobada. Las modificaciones manuales no autorizadas (paquetes instalados a mano, puertos abiertos, usuarios creados, permisos alterados en archivos sensibles) se conocen como *Configuration Drift* (desviación de configuración) y deben detectarse y alertarse inmediatamente.

### Problema
Construir una CLI que compare el estado actual del sistema contra un archivo de configuración base (baseline JSON/YAML), detecte desviaciones en paquetes de software instalados, usuarios del sistema, variables de entorno y permisos/hashes de archivos críticos, reporte las discrepancias categorizadas por severidad y persista el histórico en PostgreSQL o SQLite opcional.

### Usuario objetivo
Auditores de seguridad, ingenieros de SRE y administradores de sistemas.

### Objetivo
Desarrollar un detector de Configuration Drift con generación de snapshots base, comparación de estado y generación de alertas de conformidad.

### Ejemplo conceptual de uso
```bash
# Generar una línea base (baseline) del estado actual del sistema
python drift_checker.py snapshot -o baseline_prod.json

# Auditar el sistema actual contra la línea base
python drift_checker.py audit --baseline baseline_prod.json

# Fallar en CI si se detecta cualquier desviación crítica
python drift_checker.py audit --baseline baseline_prod.json --fail-on-drift
```

### Requisitos funcionales
- Subcomando `snapshot`: recopila el estado actual del sistema y lo guarda como línea base firmada con SHA256:
  - Paquetes de Python y del sistema instalados con versiones.
  - Lista de usuarios y grupos del sistema.
  - Hashes SHA256 y permisos octales de archivos críticos declarados (ej. `/etc/passwd`, `/etc/hosts`, `/etc/sudoers`, `.env`).
  - Variables de entorno del sistema.
  - Puertos de red en estado LISTEN.
- Subcomando `audit`: inspecciona el sistema en vivo, lo compara contra la línea base y clasifica las desviaciones:
  - `ADDED`: Elementos nuevos no declarados en el baseline.
  - `REMOVED`: Elementos que existían en el baseline y han desaparecido.
  - `MODIFIED`: Elementos modificados (versión cambiada, hash de archivo alterado, permisos modificados).
- Persistir los eventos de desviación en PostgreSQL (o SQLite opcional).
- Subcomando `history`: consulta desviaciones detectadas a lo largo del tiempo.

### Requisitos de CLI
- Subcomandos: `snapshot`, `audit`, `history`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--baseline <RUTA>` (default `baseline.json`).
- Flag `--fail-on-drift`: retorna exit code 1 si hay desviaciones.
- Opción `--format [table|json]`.
- Exit code 0 si no hay desviaciones (o en snapshot exitoso), 1 si se detectó drift con `--fail-on-drift`, 2 en errores.

### Entradas
- Archivo de línea base y estado del sistema operativo.

### Salidas
- Reporte detallado de desviaciones en STDOUT.

### Persistencia
Archivo JSON de snapshot y base de datos relacional PostgreSQL / SQLite para auditoría histórica.

### Validaciones
- Comprobar la integridad del archivo de baseline mediante verificación de hash.
- Validar que los archivos declarados para monitoreo de integridad existan.

### Casos límite
- Modificaciones legítimas esperadas (permitir definir reglas de exclusión/ignorado en `--ignore`).
- Ejecución en entornos multiplataforma (adaptar inspección de usuarios y paquetes según el SO).
- Archivos monitoreados sin permisos de lectura.

### Manejo de errores
- `PermissionError` en archivos protegidos.
- Baseline corrupto o incompatible.

### Fundamentos de Python relacionados
- Inspección del sistema con módulos `os`, `platform`, `hashlib`, `pathlib`.
- Comparación de estructuras de datos jerárquicas con diccionarios y conjuntos.
- Persistencia relacional con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Concepto de Configuration Drift y auditoría de integridad del sistema.
- Automatización de controles de seguridad en terminal.

### Herramientas o módulos para investigar
- `hashlib`.
- `pathlib` y `os`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `remediate --dry-run` para generar los comandos que restaurarían el estado al baseline?

### Diseño de argumentos
¿Cómo nombrarías la opción para ignorar cambios en variables de entorno volátiles como `PATH` o `TMPDIR` (`--ignore-env "PATH,TMP*"`)?

### Diseño de variables
`system_baseline_snapshot`, `live_system_state`, `drift_detected_items_list`, `file_integrity_checksum`, `drift_severity_rating`.

### Antes de programar
1. ¿Cómo estructurar el archivo de snapshot para que sea determinista y fácil de versionar en Git?
2. ¿Cómo calcular la diferencia entre dos diccionarios de estado anidados identificando adiciones, eliminaciones y modificaciones?

### Arquitectura
Recolector de estado (`state_collector.py`), motor de comparación de drift (`drift_detector.py`), repositorio de auditoría (`audit_repo.py`) y CLI.

### Pruebas mínimas
1. Generar snapshot de una carpeta y archivos de prueba, modificar 1 archivo y añadir 1 archivo nuevo; ejecutar `audit` y verificar que reporte `1 MODIFIED` y `1 ADDED`.
2. Probar `--fail-on-drift` y verificar que retorne exit code 1.

### Pruebas de error
1. Pasar un archivo de baseline inexistente -> Exit code 2 con error claro.

### Experiencia de usuario
Reporte visual con colores: Verde si el sistema está 100% alineado con el baseline, Rojo con desglose de discrepancias si hay drift.

### Explicación posterior
Explica la diferencia entre infraestructura mutable (donde el drift se acumula) e infraestructura inmutable (donde los servidores se reemplazan por completo en cada deploy).

### Aplicación profesional
Monitoreo continuo de cumplimiento en servidores de producción, auditorías de seguridad SOC2/PCI-DSS y detección de intrusiones.

### Reto adicional
Integrar cálculo y alerta de riesgo de seguridad ponderado (Drift Risk Score) según la criticidad de los componentes modificados.

---
> [← Ejercicio 068](../ejercicio_068/README.md) · [Índice General](../README.md) · [Ejercicio 070 →](../ejercicio_070/README.md)
