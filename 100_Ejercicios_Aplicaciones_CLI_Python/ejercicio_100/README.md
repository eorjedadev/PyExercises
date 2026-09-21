## Ejercicio 100 — Ecosistema Master de Gestión de Operaciones CLI (`ops-master`)

> [← Ejercicio 099](../ejercicio_099/README.md) · [Índice General](../README.md)

### Contexto profesional
En organizaciones de ingeniería de gran escala, los equipos de operaciones e infraestructura no ejecutan decenas de scripts inconexos, sino una plataforma CLI unificada de grado empresarial (Master Operations Platform / Developer Platform CLI) que integra todas las capacidades operativas: administración de infraestructura, gestión de bases de datos PostgreSQL (con fallback SQLite), seguridad, observabilidad, control de despliegues, plugins dinámicos y telemetría centralizada.

### Problema
Construir una suite CLI maestra (`ops-master`) con arquitectura empresarial desacoplada, que integre múltiples subsistemas mediante subcomandos de primer y segundo nivel (`db`, `infra`, `security`, `deploy`, `telemetry`, `plugins`), aplique resolución jerárquica de configuración (CLI flags > Variables de Entorno `OPS_*` > Archivos YAML > Defaults), soporte persistencia relacional en PostgreSQL (con SQLite opcional), ofrezca salida dual para humanos y máquinas, registre telemetría de uso y distribuya el paquete completo listo para producción mediante `pyproject.toml`.

### Usuario objetivo
Ingenieros de DevOps, arquitectos de software, SREs y toda la organización técnica.

### Objetivo
Diseñar e implementar la plataforma CLI empresarial definitiva que consolide todos los patrones arquitectónicos, diseño de interfaz, persistencia relacional políglota, testing, seguridad y distribución aprendidos en el programa.

### Ejemplo conceptual de uso
```bash
# Consultar estado general de la plataforma y servicios
python ops_master.py status --format table

# Operaciones de base de datos relacional en PostgreSQL
python ops_master.py db migrate --db-url "postgresql://user:pass@localhost:5432/enterprise_db" --steps 2
python ops_master.py db seed --recipe ./recipes/seed.json --driver postgresql

# Operaciones de seguridad y rotación de secretos
python ops_master.py security rotate-keys --service "payment-vault" --grace-period 24h

# Orquestación de despliegues Canary con observabilidad en tiempo real
python ops_master.py deploy canary start --app "core-api" --target-version "v3.0.0" --interval 30

# Gestión de plugins dinámicos de la plataforma
python ops_master.py plugins list
```

### Requisitos funcionales
- Subsistema `db`: migraciones versionadas con checksums, generación de semillas (seeding) con resolución de Foreign Keys, respaldo/restauración comprimida y verificación de paridad de esquemas entre PostgreSQL y SQLite.
- Subsistema `infra`: auditoría de inventario de recursos cloud, detección de costos huérfanos, diagnóstico de pre-requisitos (`doctor`) y conmutación Blue-Green atómica.
- Subsistema `security`: bóveda cifrada de credenciales (PBKDF2/Fernet), escaneo de vulnerabilidades CVE, rotación de secretos en 4 fases, generador de SBOM (CycloneDX) y auditoría de aislamiento multi-tenant.
- Subsistema `deploy`: controlador de despliegues Canary con análisis de salud en bucle cerrado y rollback automático garantizado.
- Subsistema `telemetry`: monitoreo de uptime, detector estadístico de anomalías de error (Z-Score), visualizador de cascadas de trazas distribuidas y tableros en vivo (TUI).
- Subsistema `plugins`: descubrimiento y carga dinámica de extensiones externas en tiempo de ejecución.
- Capa de Configuración Jerárquica Unificada: combina flags CLI, variables de entorno con prefijo `OPS_*` (ej. `OPS_DB_URL`, `OPS_LOG_LEVEL`), archivo de configuración `ops_config.yaml` y valores por defecto.
- Salida Dual Universal: todos los comandos soportan `--format [table|json|csv|yaml]` para uso interactivo o automatización en scripts.
- Empaquetado profesional listo para instalación global: `pyproject.toml` con entry point `ops-master = "ops_master.cli:main"`, tipado estático completo con type hints y suite de pruebas unitarias y de integración con `pytest`.

### Requisitos de CLI
- Estructura jerárquica de subcomandos:
  - `ops-master status`
  - `ops-master db [migrate|seed|backup|diff]`
  - `ops-master infra [doctor|audit-tags|costs|bg-switch]`
  - `ops-master security [vault|rotate-keys|scan-cve|sbom]`
  - `ops-master deploy [canary|rollback|history]`
  - `ops-master telemetry [probe|anomalies|waterfall|board]`
  - `ops-master plugins [list|install|info]`
- Opciones globales comunes:
  - `--config <RUTA>` (default `~/.ops_master/config.yaml`).
  - `--db-url <URL>` / variable `OPS_DB_URL` (PostgreSQL como motor principal).
  - `--driver [postgresql|sqlite]` (default `postgresql`).
  - `--sqlite-path <RUTA>`.
  - `--format [table|json|csv|yaml]` (default `table`).
  - `-v / --verbose` y `-q / --quiet`.
  - `--version`: muestra versión semántica del paquete.
- Exit codes normalizados: 0 = Éxito, 1 = Error de negocio / Aserción fallida / Rollback, 2 = Error de sintaxis o configuración, 127 = Plugin / Comando no encontrado.

### Entradas
- Comandos jerárquicos, credenciales de infraestructura, archivos de configuración y variables de entorno.

### Salidas
- Tablas interactivas, JSON estructurado, diagramas visuales y telemetría en STDOUT/STDERR.

### Persistencia
PostgreSQL como motor de datos empresarial principal (con soporte transaccional completo, índices y pooling) con SQLite como opción embebida local configurable.

### Validaciones
- Validación estricta de argumentos en cada nivel de subparsers.
- Validación de permisos y conectividad antes de ejecutar operaciones destructivas.
- Confirmaciones interactivas de seguridad con bypass explícito mediante `--force` para pipelines de CI.

### Casos límite
- Ejecución en entornos completamente aislados sin conexión a internet (modo offline / air-gapped).
- Caída concurrente de bases de datos o servicios monitoreados durante operaciones maestras.
- Manejo elegante de señales de interrupción (`SIGINT`, `SIGTERM`) cerrando pools de conexión y liberando locks.

### Manejo de errores
- Jerarquía de excepciones personalizadas (`OpsMasterError`, `DatabaseConnectionError`, `SecurityValidationError`, `DeploymentRollbackError`).
- Registro centralizado de errores con niveles de logging configurables.

### Fundamentos de Python relacionados
- Arquitectura de software modular de gran escala: separación estricta en capas (`cli/`, `core/`, `models/`, `repositories/`, `services/`, `plugins/`, `utils/`).
- Patrón Repositorio y Factory para soporte de PostgreSQL y SQLite.
- Concurrencia con `concurrent.futures` y programación asíncrona.
- Criptografía, análisis de AST, parsing de SQL, protocolos de red y árboles de grafos.
- Suite completa de pruebas con `pytest`, fixtures, `capsys` y `monkeypatch`.
- Empaquetado moderno PEP 621 con `pyproject.toml`.

### Conceptos CLI relacionados
- Diseño de suites de herramientas CLI de nivel empresarial (Enterprise Developer Platform CLI).
- Jerarquía de subcomandos multinivel, composabilidad Unix, salida dual y observabilidad integrada.

### Herramientas o módulos para investigar
- `argparse` con subparsers anidados o `click` / `typer`.
- `psycopg`.
- `sqlite3`.
- `pathlib`, `json`, `subprocess`, `logging`, `secrets`, `hashlib`.
- `pytest`.
- `pyproject.toml`.

### Diseño de comandos
Diseña la jerarquía completa de comandos y subcomandos para que sea intuitiva, predecible y consistente en todos los módulos de la plataforma.

### Diseño de argumentos
¿Cómo asegurar que las opciones globales (`--format`, `--db-url`, `--verbose`) puedan especificarse tanto en el comando raíz como en los subcomandos?

### Diseño de variables
Diseña nombres profesionales y precisos en todo el proyecto: `platform_configuration_context`, `database_connection_pool`, `active_deployment_controller`, `security_vault_service`, `telemetry_stream_aggregator`.

### Antes de programar
1. ¿Cómo estructurar el punto de entrada principal para despachar eficientemente hacia los diferentes módulos sin cargar dependencias pesadas innecesarias si el usuario solo pide `--help` o `--version`?
2. ¿Cómo diseñar la suite de pruebas automatizadas con `pytest` para verificar los flujos de cada subsistema de forma aislada mediante bases de datos de prueba temporales?

### Arquitectura
Arquitectura de Plataforma Empresarial:
```
ops_master/
├── pyproject.toml
├── README.md
├── src/
│   └── ops_master/
│       ├── __init__.py
│       ├── main.py              # Entry point ejecutable
│       ├── config/
│       │   ├── settings.py      # Precedencia CLI > ENV > YAML > Defaults
│       │   └── logging.py       # Configuración de logging unificada
│       ├── cli/
│       │   ├── root.py          # Parser raíz
│       │   ├── db_commands.py
│       │   ├── infra_commands.py
│       │   ├── security_commands.py
│       │   ├── deploy_commands.py
│       │   ├── telemetry_commands.py
│       │   └── plugin_commands.py
│       ├── core/
│       │   ├── exceptions.py    # Jerarquía de errores
│       │   ├── context.py       # Contexto global de ejecución
│       │   └── formatters.py    # Renderizado dual (Table, JSON, CSV, YAML)
│       ├── services/            # Lógica de negocio de cada dominio
│       ├── repositories/        # Capa de datos (PostgreSQL / SQLite)
│       └── plugins/             # Motor de carga dinámica de extensiones
└── tests/
    ├── conftest.py              # Fixtures de BD y CLI
    ├── test_db_subsystem.py
    ├── test_security_subsystem.py
    └── test_deploy_subsystem.py
```

### Pruebas mínimas
1. Ejecutar `ops_master status --format json` y validar que retorne el estado consolidado de la plataforma con exit code 0.
2. Ejecutar un ciclo completo de base de datos: `db migrate`, `db seed` y `db diff` en PostgreSQL (o SQLite con `--driver sqlite`) y verificar la consistencia.
3. Ejecutar la suite completa de pruebas con `pytest` y verificar que todos los tests pasen exitosamente.

### Pruebas de error
1. Invocar un subcomando inexistente `ops_master modulo-fantasma` -> Exit code 127 con sugerencias de comandos válidos.

### Experiencia de usuario
Experiencia de terminal de élite: banners limpios, ayuda interactiva comprensible con `--help` en cada nivel, soporte de colores ANSI inteligentes (desactivados automáticamente si se redirige a un pipe) y tiempos de respuesta instantáneos.

### Explicación posterior
Explica cómo la consolidación de herramientas operativas en una plataforma CLI unificada reduce la carga cognitiva de los equipos de ingeniería, previene errores manuales y estandariza las mejores prácticas de la organización.

### Aplicación profesional
Plataforma CLI interna de operaciones (Internal Developer Platform - IDP) utilizada por miles de ingenieros en empresas de tecnología líderes para gestionar infraestructura a escala global.

### Reto adicional
Implementar un sistema de telemetría de uso anónimo y auditoría distribuida que registre automáticamente cada comando ejecutado, usuario, tiempo de respuesta y exit code en el clúster de observabilidad central.

---
> [← Ejercicio 099](../ejercicio_099/README.md) · [Índice General](../README.md)
