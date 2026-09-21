# 100 Ejercicios Profesionales de Aplicaciones CLI con Python

> Programa integral de formación de ingeniería de software orientado exclusivamente al diseño, arquitectura, persistencia relacional con PostgreSQL / SQLite, observabilidad y distribución de herramientas de línea de comandos (CLI) profesionales con Python.

---

## 1. Filosofía y Manifiesto de Ingeniería CLI

Una herramienta de línea de comandos (CLI) profesional no es simplemente un script con `input()` y `print()`. Una CLI es un **componente de software de grado de ingeniería**, diseñado para:

1. **Composabilidad Unix**: Cumplir la filosofía Unix (*'Haz que cada programa haga una sola cosa bien y trabaje con flujos de texto'*), interactuando limpiamente a través de `stdin`, `stdout` y `stderr` mediante tuberías (`|`).
2. **Contratos e Idempotencia**: Códigos de salida semánticos (`exit codes`), comportamiento predecible y operaciones que puedan ejecutarse repetidamente sin efectos adversos colaterales.
3. **Persistencia Relacional Desacoplada**: Integración empresarial con **PostgreSQL** como motor principal (soportando variables `DATABASE_URL`, pooling de conexiones y transacciones ACID) y **SQLite** como opción embebida local mediante el *Patrón Repositorio*.
4. **Operación Segura**: Soporte indispensable de `--dry-run`, confirmaciones interactivas de seguridad y bypass forzado `--force` para pipelines de CI/CD.
5. **Salida Dual**: Experiencia de usuario de élite para humanos (tablas alineadas, colores ANSI inteligentes, barras de progreso) y formatos estructurados para máquinas (`--format json`, `--format csv`).
6. **Empaquetado y Distribución**: Estructura modular estándar PEP 621 con `pyproject.toml`, puntos de entrada ejecutables (`[project.scripts]`) y suites de pruebas automatizadas.

---

## 2. Convenciones de Códigos de Salida (Exit Codes)

| Código de Salida | Significado Estándar | Caso de Uso |
| :--- | :--- | :--- |
| `0` | **Éxito (Success)** | La operación finalizó correctamente. En aserciones o evaluaciones booleanas representa `True`. |
| `1` | **Error de Negocio / Fallo de Validación** | Aserción fallida, registros no encontrados, condiciones de límite excedidas, o evaluación booleana `False`. |
| `2` | **Error de Sintaxis / Argumentos Inválidos** | Flags no reconocidos, argumentos obligatorios faltantes o parámetros fuera de rango. |
| `127` | **Comando / Plugin No Encontrado** | Subcomando inexistente o plugin dinámico no registrado. |
| `130` | **Interrupción de Usuario (`Ctrl+C`)** | Captura limpia de la señal `SIGINT` con liberación de recursos. |

---

## 3. Estrategia de Persistencia: PostgreSQL & SQLite

En todos los ejercicios que requieren almacenamiento relacional estructurado se adopta el siguiente estándar arquitectónico:

```
┌────────────────────────────────────────────────────────┐
│                   Interfaz CLI / Core                  │
└───────────────────────────┬────────────────────────────┘
                            │ Invoca
                            ▼
┌────────────────────────────────────────────────────────┐
│           Repositorio Abstracto (Repository ABC)       │
└─────────────┬────────────────────────────┬─────────────┘
              │ Implementación              │ Implementación
              ▼                             ▼
┌───────────────────────────┐ ┌──────────────────────────┐
│ PostgreSQL Repo (psycopg) │ │ SQLite Repo (sqlite3)    │
│ [Motor Principal / Prod]  │ │ [Opción Local Embebida]  │
└───────────────────────────┘ └──────────────────────────┘
```

- **PostgreSQL (Principal)**: Configurable mediante flag `--db-url <URL>` o variable de entorno `DATABASE_URL` (ej. `postgresql://user:pass@localhost:5432/app_db`).
- **SQLite (Opción Local)**: Configurable mediante `--driver sqlite` y `--sqlite-path <RUTA>` para pruebas rápidas y desarrollo sin servidor.

---

## 4. Metodología de Resolución Paso a Paso

Cada ejercicio debe abordarse siguiendo este ciclo riguroso antes de escribir código:

```
Comprender Requisitos ➔ Diseñar Interfaz CLI ➔ Modelar Datos & BD ➔ Implementar Lógica
         ▲                                                               │
         │                                                               ▼
Refactorizar & Documentar ◄── Explicar Decisiones ◄── Escribir Pruebas & Validar
```

---

## 5. Catálogo Completo de los 100 Ejercicios

A continuación se detalla la lista completa de las 100 herramientas CLI profesionales, organizadas en 7 bloques de evolución técnica:

### Bloque 1: Fundamentos CLI & Scripts Robustos (001 - 012)

| N° | Herramienta | Dominio | Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 001 | **Contador y Analizador de Frecuencia de Palabras (`word-stats`)** | Terminal & Ops | No requiere persistencia en disco | [001](ejercicio_001/README.md) |
| 002 | **Codificador y Decodificador Base64 para Terminal (`b64codec`)** | Terminal & Ops | Escritura directa en el sistema de ar... | [002](ejercicio_002/README.md) |
| 003 | **Calculadora de Subredes y Validador CIDR (`ip-calc`)** | Terminal & Ops | Sin persistencia | [003](ejercicio_003/README.md) |
| 004 | **Explorador y Consultor de Códigos HTTP (`http-status`)** | Terminal & Ops | Diccionario estructurado interno o ar... | [004](ejercicio_004/README.md) |
| 005 | **Verificador de Integridad de Archivos por Hash (`hash-check`)** | Terminal & Ops | Sin persistencia | [005](ejercicio_005/README.md) |
| 006 | **Extractor y Validador de Enlaces Markdown (`md-links`)** | Terminal & Ops | Sin persistencia | [006](ejercicio_006/README.md) |
| 007 | **Extractor y Filtro de Columnas CSV (`csv-cut`)** | Terminal & Ops | Sin persistencia (orientado a streaming) | [007](ejercicio_007/README.md) |
| 008 | **Inspector y Validador de Claves JSON (`json-probe`)** | Terminal & Ops | Sin persistencia | [008](ejercicio_008/README.md) |
| 009 | **Ajustador de Marcas de Tiempo en Logs (`log-shifter`)** | Terminal & Ops | Escritura en archivo si se usa `-o` | [009](ejercicio_009/README.md) |
| 010 | **Inspector y Auditor de Variables de Entorno (`env-inspect`)** | Terminal & Ops | Sin persistencia | [010](ejercicio_010/README.md) |
| 011 | **Analizador de Extensiones y Espacio en Directorios (`ext-stats`)** | Terminal & Ops | Sin persistencia | [011](ejercicio_011/README.md) |
| 012 | **Generador Criptográfico de Contraseñas y UUIDs (`sec-gen`)** | Terminal & Ops | Sin persistencia | [012](ejercicio_012/README.md) |

### Bloque 2: Opciones, Flags, STDIN/STDOUT & Componibilidad (013 - 025)

| N° | Herramienta | Dominio | Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 013 | **Visualizador de Tablas ASCII/Markdown (`tab-view`)** | Terminal & Ops | Sin persistencia | [013](ejercicio_013/README.md) |
| 014 | **Filtro de Reemplazo y Grep en Pipelines (`stream-replace`)** | Terminal & Ops | Sin persistencia | [014](ejercicio_014/README.md) |
| 015 | **Detector de Archivos Duplicados por Hash (`dedup-scan`)** | Terminal & Ops | Modificación del sistema de archivos ... | [015](ejercicio_015/README.md) |
| 016 | **Limpiador Seguro de Archivos Temporales (`clean-tmp`)** | Terminal & Ops | Eliminación en el sistema de archivos | [016](ejercicio_016/README.md) |
| 017 | **Conversor Bidireccional JSON ↔ CSV (`data-conv`)** | Terminal & Ops | Escritura en archivo si se usa `-o` | [017](ejercicio_017/README.md) |
| 018 | **Redactor y Enmascarador de Secretos en Logs (`log-redact`)** | Terminal & Ops | Escritura de archivo sanitizado si se... | [018](ejercicio_018/README.md) |
| 019 | **Inspector de Cabeceras HTTP y Latencia (`net-peek`)** | Terminal & Ops | Sin persistencia | [019](ejercicio_019/README.md) |
| 020 | **Parser y Filtro de Syslog RFC5424/RFC3164 (`syslog-filter`)** | Terminal & Ops | Sin persistencia | [020](ejercicio_020/README.md) |
| 021 | **Generador de Árbol de Directorios ASCII (`dir-tree`)** | Terminal & Ops | Sin persistencia | [021](ejercicio_021/README.md) |
| 022 | **Divisor y Reensamblador de Archivos en Chunks (`chunk-split`)** | Terminal & Ops | Creación y lectura de múltiples archi... | [022](ejercicio_022/README.md) |
| 023 | **Escáner de Comentarios TODO/FIXME en Código Fuente (`todo-scan`)** | Terminal & Ops | Sin persistencia | [023](ejercicio_023/README.md) |
| 024 | **Conversor de Archivos INI/Properties a JSON Estructurado (`ini2json`)** | Terminal & Ops | Escritura en archivo si se usa `-o` | [024](ejercicio_024/README.md) |
| 025 | **Conversor de Horarios y Planificador de Zonas Horarias (`tz-shift`)** | Terminal & Ops | Sin persistencia | [025](ejercicio_025/README.md) |

### Bloque 3: Subcomandos, Persistencia Estructurada & Modularización (026 - 040)

| N° | Herramienta | Dominio | Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 026 | **Gestor Local de Marcadores Web (`bm-cli`)** | Terminal & Ops | Archivo JSON transaccional (ej | [026](ejercicio_026/README.md) |
| 027 | **Bóveda de Snippets de Código (`snip-vault`)** | Terminal & Ops | Directorio de archivos individuales (... | [027](ejercicio_027/README.md) |
| 028 | **Conversor de Divisas con Caché Local de Tasas (`unit-calc`)** | Terminal & Ops | Archivo JSON local con tasas y timest... | [028](ejercicio_028/README.md) |
| 029 | **Gestor y Generador de Changelogs KeepAChangelog (`chg-log`)** | Terminal & Ops | Lectura y escritura estructurada de `... | [029](ejercicio_029/README.md) |
| 030 | **Navegador y Conmutador Rápido de Workspaces (`ws-jump`)** | Terminal & Ops | Archivo JSON en el directorio de usua... | [030](ejercicio_030/README.md) |
| 031 | **Auditor y Limpiador de Ramas Git Obsoletas (`git-prune-helper`)** | Terminal & Ops | Modificación del estado del repositor... | [031](ejercicio_031/README.md) |
| 032 | **Monitor de Salud de Endpoints API (`api-ping`)** | Terminal & Ops | Archivo JSON o base de datos local co... | [032](ejercicio_032/README.md) |
| 033 | **Linter de Reglas de Seguridad para Dockerfile (`docker-lint`)** | Terminal & Ops | Sin persistencia | [033](ejercicio_033/README.md) |
| 034 | **Gestor de Alias y Conexiones SSH Config (`ssh-manager`)** | Terminal & Ops | Lectura y modificación del archivo `~/ | [034](ejercicio_034/README.md) |
| 035 | **Rastreador de Gastos y Presupuestos con Reportes CSV (`expense-tracker`)** | Terminal & Ops | Archivo CSV para transacciones (`expe... | [035](ejercicio_035/README.md) |
| 036 | **Comparador de Esquemas DDL de Bases de Datos (`schema-diff`)** | Terminal & Ops | Escritura de archivo de migración si ... | [036](ejercicio_036/README.md) |
| 037 | **Temporizador y Registro de Sesiones de Enfoque Pomodoro (`pomo-cli`)** | Terminal & Ops | Archivo JSON o SQLite local en `~/ | [037](ejercicio_037/README.md) |
| 038 | **Auditor de Matrices de Traducción e i18n (`i18n-check`)** | Terminal & Ops | Modificación de archivos de traducció... | [038](ejercicio_038/README.md) |
| 039 | **Simulador y Explicador de Expresiones Cron (`cron-sim`)** | Terminal & Ops | Sin persistencia | [039](ejercicio_039/README.md) |
| 040 | **Bóveda de Notas Markdown con Búsqueda por Etiquetas (`note-cli`)** | Terminal & Ops | Directorio de archivos individuales M... | [040](ejercicio_040/README.md) |

### Bloque 4: Persistencia en Bases de Datos (PostgreSQL / SQLite Opcional), Config & Logging (041 - 055)

| N° | Herramienta | Dominio | Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 041 | **Registro de Inventario de Hardware y Activos IT (`asset-db`)** | Terminal & Ops | Base de datos relacional PostgreSQL (... | [041](ejercicio_041/README.md) |
| 042 | **Bóveda Cifrada de Credenciales y Tokens API (`vault-cli`)** | Terminal & Ops | Tabla relacional cifrada en PostgreSQ... | [042](ejercicio_042/README.md) |
| 043 | **Gestor de Licencias y Suscripciones de Software (`sub-tracker`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [043](ejercicio_043/README.md) |
| 044 | **Caché y Buscador de Vulnerabilidades CVE (`vuln-cache`)** | Terminal & Ops | Base de datos relacional PostgreSQL (... | [044](ejercicio_044/README.md) |
| 045 | **Agente de Monitoreo de Uptime y Latencia de Servicios (`uptime-agent`)** | Terminal & Ops | PostgreSQL (con particionado mensual ... | [045](ejercicio_045/README.md) |
| 046 | **Gestor y Ejecutor de Migraciones SQL Versionadas (`migrator-cli`)** | Terminal & Ops | Base de datos PostgreSQL o SQLite y s... | [046](ejercicio_046/README.md) |
| 047 | **Despachador y Gestor de Tickets de Soporte Técnico (`ticket-cli`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [047](ejercicio_047/README.md) |
| 048 | **Motor de Rotación, Compresión y Retención de Logs (`log-rotator`)** | Terminal & Ops | Renombrado, compresión y eliminación ... | [048](ejercicio_048/README.md) |
| 049 | **Validador de Conventional Commits y Hook de Git (`commit-lint`)** | Terminal & Ops | Creación del hook ejecutable en ` | [049](ejercicio_049/README.md) |
| 050 | **Benchmark de Servidores DNS y Latencia de Resolución (`dns-bench`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [050](ejercicio_050/README.md) |
| 051 | **Sincronizador Unidireccional con Storage Mock (`s3-sync-sim`)** | Terminal & Ops | Directorio mock en disco para los obj... | [051](ejercicio_051/README.md) |
| 052 | **Sincronizador Jerárquico de Configuraciones Multi-Entorno (`config-sync`)** | Terminal & Ops | Escritura de archivos de configuració... | [052](ejercicio_052/README.md) |
| 053 | **Recolector de Métricas del Sistema y Evaluador de Alertas (`metric-guard`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [053](ejercicio_053/README.md) |
| 054 | **Orquestador de Backups y Dumps de Bases de Datos (`db-dump-orchestrator`)** | Terminal & Ops | Creación y mantenimiento de archivos ` | [054](ejercicio_054/README.md) |
| 055 | **Gestor de Feature Flags con Backend Relacional (`feature-flag-cli`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [055](ejercicio_055/README.md) |

### Bloque 5: Arquitectura Avanzada, Concurrencia, Formatos Duales & Testing (056 - 070)

| N° | Herramienta | Dominio | Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 056 | **Procesador y Agregador de Streams de Logs Masivos (`stream-aggregator`)** | Terminal & Ops | Sin persistencia en disco | [056](ejercicio_056/README.md) |
| 057 | **Extractor Concurrente de Metadatos de Archivos Multimedia (`media-meta`)** | Terminal & Ops | Escritura de catálogo en CSV/JSON o p... | [057](ejercicio_057/README.md) |
| 058 | **Monitor y Alerta de Expiración de Certificados SSL/TLS (`cert-watch`)** | Terminal & Ops | PostgreSQL o SQLite opcional para reg... | [058](ejercicio_058/README.md) |
| 059 | **Conciliador de Datos entre CSV y Base de Datos (`data-reconcile`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [059](ejercicio_059/README.md) |
| 060 | **Generador Automatizado de Release Notes desde Git (`rel-notes-gen`)** | Terminal & Ops | Escritura del archivo Markdown si se ... | [060](ejercicio_060/README.md) |
| 061 | **Servidor Mock de APIs REST con Rutas Dinámicas (`mock-api-cli`)** | Terminal & Ops | Archivo JSON de rutas (`routes | [061](ejercicio_061/README.md) |
| 062 | **Simulador y Reintentador de Envíos de Webhooks (`webhook-tester`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [062](ejercicio_062/README.md) |
| 063 | **Empaquetador y Minificador de Assets Estáticos (`asset-bundler`)** | Terminal & Ops | Creación y actualización de archivos ... | [063](ejercicio_063/README.md) |
| 064 | **Simulador de Colas de Mensajería FIFO con Persistencia (`queue-tool`)** | Terminal & Ops | PostgreSQL como motor principal (apro... | [064](ejercicio_064/README.md) |
| 065 | **Tablero de Estado de Servicios en Tiempo Real (`status-board`)** | Terminal & Ops | Sin persistencia o guardado opcional ... | [065](ejercicio_065/README.md) |
| 066 | **Auditor y Enforcer de Tags en Recursos Cloud (`tag-auditor`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [066](ejercicio_066/README.md) |
| 067 | **Linter y Formateador Estricto de Consultas SQL (`sql-lint-fmt`)** | Terminal & Ops | Modificación de archivos en disco si ... | [067](ejercicio_067/README.md) |
| 068 | **Escáner de Puertos y Captura de Banners de Red (`port-peek`)** | Terminal & Ops | Registro opcional de escaneos en Post... | [068](ejercicio_068/README.md) |
| 069 | **Detector de Desviación de Configuración del Sistema (`drift-checker`)** | Terminal & Ops | Archivo JSON de snapshot y base de da... | [069](ejercicio_069/README.md) |
| 070 | **Generador de Software Bill of Materials SBOM (`sbom-gen`)** | Terminal & Ops | Escritura del archivo SBOM en disco | [070](ejercicio_070/README.md) |

### Bloque 6: Frameworks CLI, Empaquetado, Plugins & CI/CD (071 - 085)

| N° | Herramienta | Dominio | Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 071 | **Scaffolder de Proyectos y CLI Profesionales en Python (`cli-scaffold`)** | Terminal & Ops | Creación completa de directorios y ar... | [071](ejercicio_071/README.md) |
| 072 | **Motor de Ejecución de Tareas Basado en Plugins (`task-runner`)** | Terminal & Ops | Directorio de plugins en disco y regi... | [072](ejercicio_072/README.md) |
| 073 | **Diagnosticador de Pre-requisitos de Entorno (`env-doctor`)** | Terminal & Ops | Sin persistencia | [073](ejercicio_073/README.md) |
| 074 | **Generador de Semillas de Datos para PostgreSQL / SQLite (`db-seeder`)** | Terminal & Ops | Inserción directa en base de datos Po... | [074](ejercicio_074/README.md) |
| 075 | **Auditor de Aislamiento Multi-Inquilino en Consultas SQL (`tenant-auditor`)** | Terminal & Ops | Sin persistencia | [075](ejercicio_075/README.md) |
| 076 | **Gestor y Ejecutor de Git Pre-Commit Hooks (`pre-commit-lite`)** | Terminal & Ops | Creación del hook ejecutable en ` | [076](ejercicio_076/README.md) |
| 077 | **Validador de Especificaciones OpenAPI y Cambios Rupturistas (`openapi-check`)** | Terminal & Ops | Sin persistencia | [077](ejercicio_077/README.md) |
| 078 | **Recolector de Basura y Limpiador de Artefactos CI/CD (`ci-cleaner`)** | Terminal & Ops | Eliminación de archivos en disco y ac... | [078](ejercicio_078/README.md) |
| 079 | **Simulador de Bloqueos Distribuidos Basado en Archivos y BD (`file-lock-cli`)** | Terminal & Ops | Archivos ` | [079](ejercicio_079/README.md) |
| 080 | **Detector de Picos y Anomalías en Tasas de Error (`anomaly-detector`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [080](ejercicio_080/README.md) |
| 081 | **Conmutador Blue-Green de Configuraciones con Rollback (`bg-switcher`)** | Terminal & Ops | Manipulación atómica de symlinks en d... | [081](ejercicio_081/README.md) |
| 082 | **Coordinador y Orquestador de Rotación de Secretos (`secret-rotator`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [082](ejercicio_082/README.md) |
| 083 | **Detector de Fragmentos de Código Duplicado (`code-clone-finder`)** | Terminal & Ops | Sin persistencia | [083](ejercicio_083/README.md) |
| 084 | **Visualizador de Mapas de Dependencias entre Microservicios (`service-map`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [084](ejercicio_084/README.md) |
| 085 | **Auditor de Costos Cloud y Detección de Recursos Huérfanos (`cost-auditor`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [085](ejercicio_085/README.md) |

### Bloque 7: Ingeniería CLI Autónoma & Sistemas Empresariales (086 - 100)

| N° | Herramienta | Dominio | Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 086 | **Orquestador de Migración de Objetos Multi-Cloud con Resume (`cloud-migrator`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [086](ejercicio_086/README.md) |
| 087 | **Monitor de Quórum y Heartbeat en Clústeres de Alta Disponibilidad (`cluster-heartbeat`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [087](ejercicio_087/README.md) |
| 088 | **Replayer de Streams de Eventos con Control de Velocidad (`event-replayer`)** | Terminal & Ops | Sin persistencia | [088](ejercicio_088/README.md) |
| 089 | **Ejecutor de Transacciones Sintéticas End-to-End (`synthetic-probe`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [089](ejercicio_089/README.md) |
| 090 | **Controlador de Despliegues Canary con Rollback Automatizado (`canary-ctl`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [090](ejercicio_090/README.md) |
| 091 | **Recolector de Evidencias Forenses para Respuesta a Incidentes (`incident-collector`)** | Terminal & Ops | Creación de archivos ` | [091](ejercicio_091/README.md) |
| 092 | **Suite de Micro-Benchmarking y Detección de Regresiones (`perf-bench-cli`)** | Terminal & Ops | Archivos JSON de resultados y base de... | [092](ejercicio_092/README.md) |
| 093 | **Sincronizador y Traductor de Esquemas Políglotas PostgreSQL ↔ SQLite (`polyglot-schema`)** | Terminal & Ops | Escritura de archivos SQL o modificac... | [093](ejercicio_093/README.md) |
| 094 | **Simulador de Rate Limiting con Algoritmo Token Bucket (`rate-limiter-cli`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [094](ejercicio_094/README.md) |
| 095 | **Inyector de Fallas para Pruebas de Chaos Engineering (`chaos-cli`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [095](ejercicio_095/README.md) |
| 096 | **Divisor y Reconstructor de Secretos con Esquema Shamir (`secret-splitter`)** | Terminal & Ops | Escritura y lectura de archivos de fr... | [096](ejercicio_096/README.md) |
| 097 | **Correlador de Trazas Distribuidas e Inyector de Trace IDs (`trace-stitcher`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [097](ejercicio_097/README.md) |
| 098 | **Motor de Evaluación de Reglas de Gobernanza y Compliance (`compliance-engine`)** | Terminal & Ops | PostgreSQL como motor principal (o SQ... | [098](ejercicio_098/README.md) |
| 099 | **Motor de Refactorización Automatizada y Codemods AST (`codemod-cli`)** | Terminal & Ops | Modificación directa de archivos de c... | [099](ejercicio_099/README.md) |
| 100 | **Ecosistema Master de Gestión de Operaciones CLI (`ops-master`)** | Terminal & Ops | PostgreSQL como motor de datos empres... | [100](ejercicio_100/README.md) |

---

## 6. Instrucciones para Ejecutar y Probar

Para trabajar en cualquier ejercicio:
1. Navega al directorio del ejercicio correspondiente: `cd ejercicio_XXX`.
2. Lee el `README.md` detallado para analizar el problema, requisitos de CLI y casos límite.
3. Inspecciona los archivos de prueba en `datos/`, `config/` o `fixtures/` si existen.
4. Diseña tu arquitectura desacoplada y escribe tu código de implementación.
5. Verifica tu herramienta ejecutando las pruebas mínimas y de error descritas en el README.

**¡Éxito en el dominio de la ingeniería de software CLI con Python!**