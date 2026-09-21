## Ejercicio 044 — Caché y Buscador de Vulnerabilidades CVE (`vuln-cache`)

> [← Ejercicio 043](../ejercicio_043/README.md) · [Índice General](../README.md) · [Ejercicio 045 →](../ejercicio_045/README.md)

### Contexto profesional
Los equipos de seguridad y DevSecOps necesitan auditar dependencias y paquetes de software contra bases de datos de vulnerabilidades conocidas (CVEs del NVD de NIST o GitHub Advisory Database). Realizar consultas repetidas a través de la red es lento y sujeto a límites de tasa (rate-limits), por lo que mantener una base de datos relacional local sincronizada permite análisis ultra-rápidos fuera de línea.

### Problema
Construir una CLI que mantenga un catálogo local en PostgreSQL (o SQLite opcional) de vulnerabilidades y exposiciones comunes (CVEs), permitiendo sincronizar datos desde un feed JSON/API, buscar por identificador (ej. `CVE-2024-3094`), filtrar por paquete de software afectado y consultar según puntuación de severidad CVSS.

### Usuario objetivo
Analistas de seguridad (SecOps), auditores de código y DevOps.

### Objetivo
Crear un buscador y sincronizador de vulnerabilidades con almacenamiento relacional optimizado, soporte de transacciones por lotes y filtros por vector CVSS.

### Ejemplo conceptual de uso
```bash
# Sincronizar catálogo de CVEs desde un archivo de feed de seguridad
python vuln_cache.py sync --feed-file ./fixtures/nvd_feed_sample.json

# Buscar detalles de un CVE específico
python vuln_cache.py get CVE-2024-3094

# Buscar vulnerabilidades críticas (CVSS >= 9.0) que afecten a 'openssh'
python vuln_cache.py search --package "openssh" --min-cvss 9.0
```

### Requisitos funcionales
- Subcomando `init-db`: crea las tablas relacionales (`cve_entries`, `affected_packages`, `references`) con índices en identificadores y puntajes CVSS.
- Subcomando `sync`: procesa archivos de feed de vulnerabilidades e inserta/actualiza registros en la base de datos usando transacciones por lotes (`batch inserts / upserts`).
- Subcomando `get <CVE_ID>`: muestra la ficha técnica completa del CVE: descripción, fecha de publicación, puntuación CVSS v3 (base score, vector string), nivel de severidad (Critical, High, Medium, Low) y paquetes afectados.
- Subcomando `search`: búsqueda combinada por nombre de paquete, palabra clave en descripción, rango de fechas y puntaje CVSS mínimo.
- Subcomando `scan-file <REQUIREMENTS.TXT>`: lee un archivo de dependencias de Python y consulta si alguna de las librerías tiene CVEs reportados en la base de datos local.

### Requisitos de CLI
- Subcomandos: `init-db`, `sync`, `get`, `search`, `scan-file`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--min-cvss <SCORE>` (float de 0.0 a 10.0).
- Exit code 0 en éxito, 1 si en `scan-file` se detectan vulnerabilidades críticas (CVSS >= 9.0), 2 en errores.

### Entradas
- Archivos de feed de seguridad, identificadores CVE y archivos de requerimientos.

### Salidas
- Fichas técnicas, tablas de vulnerabilidades y resúmenes de escaneo en STDOUT.

### Persistencia
Base de datos relacional PostgreSQL (aprovechando índices GIN para búsqueda de texto o JSONB) o SQLite local opcional.

### Validaciones
- El identificador debe cumplir el formato estándar `CVE-YYYY-NNNN+` con regex.
- El puntaje CVSS debe estar entre 0.0 y 10.0.

### Casos límite
- Ingestión de feeds con decenas de miles de registros (usar inserciones en lotes con `executemany` o `COPY` en PostgreSQL para no saturar memoria).
- CVEs sin puntuación CVSS asignada (estado RESERVED o UNDER_REVIEW).
- CVEs que afectan a múltiples versiones de un mismo paquete.

### Manejo de errores
- Errores de parsing de feeds JSON gigantes.
- Manejo de registros duplicados mediante sentencias `ON CONFLICT DO UPDATE` (upsert).

### Fundamentos de Python relacionados
- Inserciones masivas por lotes (batch processing).
- Expresiones regulares para validación de CVEs y versiones de paquetes.
- Conexión a PostgreSQL / SQLite con transacciones eficientes.

### Conceptos CLI relacionados
- Sincronización de bases de conocimiento para operación disconnected / offline.
- Escaneo de seguridad automatizado en terminal.

### Herramientas o módulos para investigar
- `json` e `ijson` (para streaming de JSONs gigantes).
- `psycopg` / `sqlite3`.
- `re` y `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `stats` para mostrar un resumen de la base de datos (total de CVEs, distribución por severidad, última fecha de sincronización)?

### Diseño de argumentos
¿Cómo nombrarías la opción para exportar los resultados del escaneo a formato SARIF (`--format sarif`)?

### Diseño de variables
`cve_identifier`, `cvss_base_score`, `severity_rating`, `affected_product_name`, `batch_records_chunk`, `vulnerability_repository`.

### Antes de programar
1. ¿Por qué procesar un archivo JSON de 500 MB con `json.load()` completo puede agotar la memoria RAM y cómo estructurar la lectura por fragmentos?
2. ¿Cómo diseñar la sentencia `UPSERT` en PostgreSQL (`INSERT ... ON CONFLICT (cve_id) DO UPDATE ...`) y en SQLite (`INSERT OR REPLACE INTO ...`)?

### Arquitectura
Estructura:
```
ejercicio_044/
├── vuln_cache.py
├── feed_importer.py
├── scanner.py
├── repositories/
│   ├── base_repo.py
│   ├── postgres_vuln_repo.py
│   └── sqlite_vuln_repo.py
└── fixtures/
    └── nvd_sample.json
```

### Pruebas mínimas
1. Sincronizar el dataset de prueba fixture en PostgreSQL (o SQLite), consultar `CVE-2024-3094` y verificar que retorne la severidad `CRITICAL` y score `10.0`.
2. Escanear un `requirements.txt` de prueba y verificar que detecte el paquete vulnerable.

### Pruebas de error
1. Consultar un formato de CVE inválido `CVE-INVALIDO` -> Exit code 2 con error de formato.

### Experiencia de usuario
Ficha técnica con código de colores según severidad CVSS: Rojo brillante para Crítico (9.0-10.0), Rojo para Alto (7.0-8.9), Amarillo para Medio (4.0-6.9), Verde para Bajo.

### Explicación posterior
Explica la estructura de la métrica CVSS v3.1 (Common Vulnerability Scoring System) y qué significan vectores como `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`.

### Aplicación profesional
Motores de auditoría de software composition analysis (SCA) integrados en pipelines de despliegue continuo.

### Reto adicional
Implementar comparación semántica de rangos de versión de paquetes (ej. determinar si la versión instalada `2.4.1` cae dentro del rango vulnerable `< 2.4.5`).

---
> [← Ejercicio 043](../ejercicio_043/README.md) · [Índice General](../README.md) · [Ejercicio 045 →](../ejercicio_045/README.md)
