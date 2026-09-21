## Ejercicio 073 — Diagnosticador de Pre-requisitos de Entorno (`env-doctor`)

> [← Ejercicio 072](../ejercicio_072/README.md) · [Índice General](../README.md) · [Ejercicio 074 →](../ejercicio_074/README.md)

### Contexto profesional
Antes de que un nuevo desarrollador configure un repositorio complejo o antes de ejecutar un pipeline de despliegue en un servidor, es necesario validar que el entorno cumpla con decenas de pre-requisitos (versión mínima de Python, versiones de binarios del sistema como `git`, `docker`, `psql`, espacio libre en disco, puertos libres, conectividad a bases de datos y variables de entorno requeridas).

### Problema
Construir una CLI de diagnóstico de entorno (similar a `brew doctor` o `flutter doctor`), configurada mediante un archivo declarativo YAML/JSON, que ejecute una batería de comprobaciones en paralelo, clasifique los resultados en estados (`PASS`, `WARN`, `FAIL`), proporcione instrucciones de solución paso a paso ante fallos y retorne códigos de salida acordes para CI.

### Usuario objetivo
Desarrolladores, ingenieros de onboarding y DevOps.

### Objetivo
Crear una herramienta de diagnóstico pre-vuelo (preflight checker) con catálogo de verificadores extensibles, sugerencias de remediación y reporte visual.

### Ejemplo conceptual de uso
```bash
# Ejecutar diagnóstico completo del entorno de desarrollo
python env_doctor.py check --config doctor_rules.json

# Diagnosticar solo requerimientos de base de datos y Docker
python env_doctor.py check --categories "database,docker"

# Modo estricto para CI (falla si hay cualquier advertencia)
python env_doctor.py check --strict --format json
```

### Requisitos funcionales
- Sistema modular de verificadores de entorno:
  - `python_version`: comprueba que la versión actual de Python sea `>=` al mínimo requerido (ej. `>= 3.11`).
  - `binary_installed`: comprueba la existencia y versión mínima de binarios en el PATH (`git`, `docker`, `psql`, `pg_dump`).
  - `env_variables`: verifica que variables críticas estén declaradas (`DATABASE_URL`, `SECRET_KEY`).
  - `port_availability`: verifica que los puertos locales necesarios (ej. 5432, 8000) estén libres.
  - `disk_space`: comprueba que haya al menos N gigabytes libres en el disco.
  - `db_connection`: prueba una conexión real hacia la base de datos PostgreSQL o SQLite configurada.
- Subcomando `check`: ejecuta todos los verificadores y emite un reporte con iconos visuales (`✓`, `!`, `✗`) y sugerencias de corrección.
- Subcomando `fix-suggestions`: imprime la lista consolidada de comandos del sistema para corregir los fallos encontrados.

### Requisitos de CLI
- Subcomandos: `check`, `fix-suggestions`.
- Opción `--config <RUTA>` (default `doctor_rules.json`).
- Opción `--categories <LISTA>`.
- Flag `--strict`: trata las advertencias (`WARN`) como errores fatales.
- Opción `--format [table|json|markdown]`.
- Exit code 0 si todos los checks pasan (o solo hay warnings en modo no estricto), 1 si hay checks en `FAIL` (o warnings en `--strict`), 2 en errores.

### Entradas
- Archivo de reglas de diagnóstico y estado del sistema.

### Salidas
- Reporte interactivo formateado en terminal o JSON.

### Persistencia
Sin persistencia.

### Validaciones
- Validar la estructura del archivo de reglas de diagnóstico.
- Validar formato de especificaciones de versión semántica.

### Casos límite
- Binarios que no soportan el flag `--version` estándar.
- Comprobación de puertos sin privilegios de administrador.
- Sistemas operativos diferentes (rutas de instalación de binarios en Windows vs Linux/macOS).

### Manejo de errores
- `subprocess.TimeoutExpired` al invocar binarios externos.
- Captura de excepciones en cada verificador sin interrumpir el resto de comprobaciones.

### Fundamentos de Python relacionados
- Invocación de utilidades con `shutil.which` y `subprocess.run`.
- Comparación de versiones con módulo `packaging.version` o parsing manual de tuplas `(major, minor, patch)`.
- Módulos `sys`, `platform`, `socket`, `shutil`.
- Conexión a base de datos PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Diagnóstico pre-flight interactivo y visual.
- Sugerencias accionables de remediación en mensajes de error.

### Herramientas o módulos para investigar
- `shutil.which`.
- `sys.version_info`.
- `subprocess` y `socket`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para exportar el diagnóstico a un archivo Markdown para adjuntar en tickets de soporte?

### Diseño de argumentos
¿Cómo nombrarías la opción para ignorar un check específico por ID (`--skip-check CHK_DOCKER`)?

### Diseño de variables
`preflight_rules_config`, `check_results_registry`, `passed_checks_count`, `failed_checks_count`, `remediation_instructions_map`.

### Antes de programar
1. ¿Cómo parsear la salida de `git --version` (`git version 2.43.0`) para extraer la tupla numérica `(2, 43, 0)` y compararla contra `(2, 30, 0)`?
2. ¿Cómo probar si un puerto local está libre intentando hacer `bind()` con un socket TCP sin dejar el puerto tomado?

### Arquitectura
Motor de diagnóstico (`doctor_core.py`), catálogo de checks (`checks/`), formateador de reportes (`report_view.py`) y CLI.

### Pruebas mínimas
1. Ejecutar `check` con una regla de Python >= 3.10 y verificar que pase exitosamente con marca verde `[PASS]`.
2. Probar un check de binario inexistente `binario_falso_xyz` y verificar que reporte `[FAIL]` con sugerencia de instalación.

### Pruebas de error
1. Ejecutar con `--strict` en presencia de advertencias -> Exit code 1.

### Experiencia de usuario
Reporte visual impactante con iconos y colores: `[✓] Python >= 3.11 (Detectado: 3.12.2)`, `[✗] PostgreSQL en localhost:5432 (Conexión rechazada -> Inicia el servicio con 'systemctl start postgresql')`.

### Explicación posterior
Explica cómo las herramientas de diagnóstico pre-flight reducen el tiempo de incorporación de nuevos desarrolladores (Developer Onboarding Time) de días a minutos.

### Aplicación profesional
Scripts de onboarding en empresas de tecnología, pre-requisitos en instaladores de software y verificadores de pipelines de CI.

### Reto adicional
Implementar un flag `--auto-fix` que intente ejecutar automáticamente los comandos de instalación o configuración recomendados bajo confirmación del usuario.

---
> [← Ejercicio 072](../ejercicio_072/README.md) · [Índice General](../README.md) · [Ejercicio 074 →](../ejercicio_074/README.md)
