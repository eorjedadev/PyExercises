## Ejercicio 075 — Auditor de Aislamiento Multi-Inquilino en Consultas SQL (`tenant-auditor`)

> [← Ejercicio 074](../ejercicio_074/README.md) · [Índice General](../README.md) · [Ejercicio 076 →](../ejercicio_076/README.md)

### Contexto profesional
En arquitecturas SaaS multi-inquilino (Multi-Tenant) con base de datos compartida (PostgreSQL), el aislamiento de datos entre clientes depende de que todas las consultas SQL filtren obligatoriamente por la columna del inquilino (ej. `WHERE tenant_id = :current_tenant`). Olvidar esta cláusula en una sola consulta provoca fugas de datos críticas entre empresas clientes (Data Leak / Cross-Tenant Data Access).

### Problema
Construir una CLI de análisis estático que examine consultas SQL y código fuente de repositorios (archivos `.sql`, `.py`, `.js`), parsee las sentencias `SELECT`, `UPDATE`, `DELETE` y `JOIN`, verifique que todas las tablas multi-inquilino contengan la restricción `tenant_id` en sus cláusulas `WHERE` o `ON`, y reporte las consultas vulnerables con número de línea y severidad.

### Usuario objetivo
Auditores de seguridad, desarrolladores backend y arquitectos SaaS.

### Objetivo
Desarrollar un analizador estático de seguridad para consultas SQL que detecte omisiones de aislamiento multi-inquilino y fugas de datos.

### Ejemplo conceptual de uso
```bash
# Auditar consultas en un directorio de código fuente
python tenant_auditor.py audit ./src --tenant-col "tenant_id" --tables "users,orders,invoices,settings"

# Fallar el pipeline de CI si se detecta cualquier consulta sin filtro de tenant
python tenant_auditor.py audit ./src --fail-on-violation --format table
```

### Requisitos funcionales
- Recorrer archivos de código buscando sentencias SQL (en archivos `.sql` o cadenas de texto SQL incrustadas en código Python/JS/Go).
- Parsear la estructura sintáctica de cada sentencia `SELECT`, `UPDATE`, `DELETE`:
  - Identificar las tablas consultadas en `FROM` y `JOIN`.
  - Comprobar si las tablas pertenecen a la lista de tablas multi-inquilino vigiladas.
  - Analizar el árbol de condiciones de la cláusula `WHERE` y `JOIN ON` buscando la presencia obligatoria de la condición `tenant_id = ...` o `tenant_id IN (...)`.
- Detectar consultas potencialmente peligrosas: `SELECT * FROM orders WHERE status = 'PENDING'` (falta `tenant_id`).
- Permitir excepciones explícitas mediante comentarios en el código (ej. `-- tenant-audit:allow-global`).
- Subcomando `audit`: genera reporte de hallazgos con archivo, línea, tabla infractora y fragmento de consulta.

### Requisitos de CLI
- Subcomando `audit`.
- Argumento posicional: directorio o archivo a escanear.
- Opción `--tenant-col <NOMBRE>` (default `tenant_id`).
- Opción `--tables <TABLAS>` (lista separada por comas de tablas que requieren aislamiento).
- Flag `--fail-on-violation`: retorna exit code 1 si hay vulnerabilidades detectadas.
- Opción `--format [table|json|sarif]`.
- Exit code 0 si todas las consultas están correctamente aisladas, 1 si hay violaciones con `--fail-on-violation`, 2 en errores.

### Entradas
- Archivos de código fuente y lista de tablas protegidas.

### Salidas
- Reporte de seguridad de aislamiento en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Comprobar que el directorio a escanear exista.
- Validar que se especifique al menos una tabla vigilada.

### Casos límite
- Consultas SQL con subconsultas y CTEs (`WITH` clauses; cada subconsulta debe validar su propio `tenant_id`).
- Consultas dinámicas construidas mediante concatenación de cadenas o Query Builders.
- Tablas globales del sistema que intencionalmente no tienen `tenant_id` (ej. tabla `plans` o `countries`).

### Manejo de errores
- Errores de lectura de archivos.
- Manejo de consultas SQL complejas que no puedan ser parseadas completamente (emitir advertencia de revisión manual).

### Fundamentos de Python relacionados
- Análisis estático de código y expresiones regulares avanzadas o AST de Python (`ast.parse`).
- Tokenización y parsing de sintaxis SQL.
- `pathlib.Path` para recorrido del proyecto.

### Conceptos CLI relacionados
- Análisis estático de seguridad (SAST) especializado en terminal.
- Verificación de políticas de seguridad multi-inquilino en CI/CD.

### Herramientas o módulos para investigar
- `re`.
- `ast`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para cargar la lista de tablas protegidas directamente desde el esquema de la base de datos PostgreSQL conectándose a `information_schema.columns`?

### Diseño de argumentos
¿Cómo nombrarías la opción para auditar también el uso de Row Level Security (RLS) en scripts DDL de PostgreSQL (`--check-rls`)?

### Diseño de variables
`target_source_files`, `monitored_tenant_tables_set`, `tenant_column_name`, `extracted_sql_queries_list`, `tenant_isolation_violations`.

### Antes de programar
1. ¿Cómo extraer cadenas SQL multilínea de archivos de Python usando el módulo nativo `ast` buscando llamadas a métodos como `cursor.execute("...")` o `db.query("...")`?
2. ¿Cómo analizar la cláusula `WHERE` para verificar que la condición `tenant_id` no esté anulada por una condición `OR` mal estructurada (ej. `WHERE tenant_id = 1 OR status = 'ALL'`)?

### Arquitectura
Extractor de SQL desde código (`sql_extractor.py`), analizador de cláusulas (`where_analyzer.py`), motor de auditoría (`tenant_checker.py`) y CLI.

### Pruebas mínimas
1. Auditar un archivo con 2 queries (una con `WHERE tenant_id = ? AND id = ?` y otra sin `tenant_id`); verificar que solo marque como vulnerable la segunda query.
2. Probar exclusión con comentario `-- tenant-audit:allow-global` y verificar que no genere alerta.

### Pruebas de error
1. Ejecutar sobre un directorio vacío o sin archivos de código -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Tabla de hallazgos de seguridad con severidad `CRITICAL` en rojo brillante, indicando: `ARCHIVO:LÍNEA`, `TABLA EXPUESTA`, `SQL DETECTADO` y `RECOMENDACIÓN DE AISLAMIENTO`.

### Explicación posterior
Explica la diferencia entre aislamiento lógico mediante cláusulas WHERE y aislamiento a nivel de base de datos mediante PostgreSQL Row Level Security (RLS) y políticas de seguridad (`CREATE POLICY`).

### Aplicación profesional
Security gates en CI/CD para arquitecturas SaaS multi-tenant, auditorías de cumplimiento SOC2 e inspección de código de microservicios.

### Reto adicional
Implementar verificación de políticas de Row Level Security (RLS) en scripts de migración de PostgreSQL asegurando que contengan `ALTER TABLE ... ENABLE ROW LEVEL SECURITY`.

---
> [← Ejercicio 074](../ejercicio_074/README.md) · [Índice General](../README.md) · [Ejercicio 076 →](../ejercicio_076/README.md)
