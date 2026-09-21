## Ejercicio 098 — Motor de Evaluación de Reglas de Gobernanza y Compliance (`compliance-engine`)

> [← Ejercicio 097](../ejercicio_097/README.md) · [Índice General](../README.md) · [Ejercicio 099 →](../ejercicio_099/README.md)

### Contexto profesional
En organizaciones reguladas (banca, salud, fintech), los sistemas y configuraciones de nube deben evaluarse continuamente contra marcos de cumplimiento normativo (CIS Benchmarks, PCI-DSS, HIPAA, GDPR). Cada regla de control de seguridad debe evaluarse de forma automatizada, calculando un índice de cumplimiento ponderado y emitiendo reportes de auditoría técnica.

### Problema
Construir una CLI que actúe como motor de evaluación de cumplimiento y gobernanza (Compliance as Code), leyendo reglas declarativas en YAML/JSON, evaluando el estado del sistema, configuraciones cloud o esquemas de base de datos relacional (PostgreSQL/SQLite), asignando puntuaciones de severidad (Critical, High, Medium, Low), generando reportes de auditoría exportables y persistiendo los resultados históricos en PostgreSQL.

### Usuario objetivo
Auditores de cumplimiento, ingenieros de seguridad y líderes de GRC (Governance, Risk and Compliance).

### Objetivo
Crear un motor de evaluación de reglas de cumplimiento normativo con DSL declarativo, cálculo de puntuación de riesgo ponderada y persistencia relacional.

### Ejemplo conceptual de uso
```bash
# Ejecutar evaluación de cumplimiento contra el marco CIS Benchmark
python compliance_engine.py evaluate --framework cis-benchmark.yaml --target-system ./system_audit.json

# Auditar configuración de seguridad de base de datos PostgreSQL en vivo
python compliance_engine.py evaluate-db --db-url "postgresql://admin:pass@localhost:5432/app_db" --rules pg_security_rules.json

# Ver reporte ejecutivo de cumplimiento y brechas de seguridad
python compliance_engine.py report --format markdown -o compliance_report.md
```

### Requisitos funcionales
- Motor de reglas declarativo con sintaxis DSL en YAML/JSON:
  - Cada regla define: `id`, `title`, `framework` (ej. `CIS-PostgreSQL-1.2`), `severity` (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`), `weight` (ponderación 1-10), `check_expression` (condición lógica) y `remediation_guidance`.
- Subcomando `evaluate`: evalúa un archivo de inventario de configuración contra las reglas del marco normativo.
- Subcomando `evaluate-db`: conecta a PostgreSQL (o SQLite opcional) y evalúa controles de seguridad nativos (ej. verificación de contraseñas no nulas, cifrado en reposo, conexiones SSL obligatorias, permisos de superusuario acotados, logging de auditoría activado).
- Cálculo del Índice de Cumplimiento Global (Compliance Score): media ponderada de los controles aprobados respecto al total de pesos posibles.
- Subcomando `report`: genera reportes ejecutivos en formato Markdown, HTML o JSON con matriz de riesgos y recomendaciones de remediación.
- Persistencia de evaluaciones históricas en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `evaluate`, `evaluate-db`, `report`, `frameworks`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--framework <RUTA>`.
- Opción `--min-score <PORCENTAJE>` (ej. 90.0 para fallar en CI si el score es inferior al 90%).
- Opción `--format [table|json|markdown|html]`.
- Exit code 0 si el score supera `--min-score` y no hay fallos críticos, 1 si no se cumple el umbral de compliance, 2 en errores.

### Entradas
- Archivos de reglas de cumplimiento, inventarios de configuración y conexiones a BD.

### Salidas
- Reporte ejecutivo de auditoría y matriz de no conformidades en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `compliance_audits`, `rule_evaluations` y `compliance_frameworks`.

### Validaciones
- Validar la estructura y sintaxis de las expresiones del marco de reglas.
- Los pesos deben ser números positivos.

### Casos límite
- Controles no aplicables (N/A; permitir marcar reglas como no aplicables con justificación documentada sin penalizar el score).
- Reglas con condiciones complejas de múltiples variables.
- Evaluación de cientos de controles normativos en paralelo.

### Manejo de errores
- Errores de evaluación de expresiones de reglas.
- Errores de conexión a base de datos.

### Fundamentos de Python relacionados
- Intérprete o evaluador de expresiones lógicas seguras (sin usar `eval()` inseguro; usar analizador de operadores o AST).
- Cálculo de medias ponderadas y matrices de riesgo.
- Persistencia relacional de auditorías con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Gobernanza, Riesgo y Cumplimiento como Código (Compliance as Code).
- Evaluación de postura de seguridad y puntuación de riesgo.

### Herramientas o módulos para investigar
- `ast` (para evaluación segura de expresiones lógicas).
- `psycopg` / `sqlite3`.
- `json` y `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `exception-grant --rule-id CIS-1.2 --reason "Legacy system" --expires "2026-12-31"` para gestionar excepciones temporales aprobadas?

### Diseño de argumentos
¿Cómo nombrarías la opción para filtrar el reporte únicamente por un nivel de severidad específico (ej. `--severity critical,high`)?

### Diseño de variables
`compliance_framework_rules`, `system_under_evaluation_dto`, `rule_evaluation_results_list`, `weighted_compliance_score`, `unresolved_findings_matrix`.

### Antes de programar
1. ¿Por qué nunca se debe utilizar la función nativa `eval()` de Python para evaluar reglas de compliance y cómo construir un evaluador seguro basado en operadores AST o diccionarios?
2. ¿Cómo formular el score de cumplimiento ponderado: $\text{Score} = \frac{\sum_{i \in \text{Aprobadas}} w_i}{\sum_{j \in \text{Aplicables}} w_j} \times 100$?

### Arquitectura
Parser de marcos (`framework_parser.py`), evaluador de expresiones seguras (`safe_evaluator.py`), auditor de base de datos (`db_auditor.py`), calculador de scores (`score_calculator.py`) y CLI.

### Pruebas mínimas
1. Evaluar un sistema de prueba contra un marco de 5 reglas (3 aprobadas con peso 10, 2 reprobadas con peso 5) y verificar que el score ponderado sea exactamente 75.0%.
2. Ejecutar con `--min-score 80.0` y verificar que retorne exit code 1.

### Pruebas de error
1. Pasar un archivo de marco normativo con formato JSON/YAML corrupto -> Exit code 2 con error claro.

### Experiencia de usuario
Reporte visual impactante con barra de porcentaje de cumplimiento: `[████████░░░░] 75.0% Compliance Score | 3 APROBADAS | 2 NO CONFORMES (1 CRITICAL)` y tabla detallada de remedios.

### Explicación posterior
Explica la diferencia entre auditorías puntuales anuales y el enfoque moderno de Cumplimiento Continuo (Continuous Compliance Monitoring).

### Aplicación profesional
Auditorías de seguridad bancaria, certificación de infraestructuras cloud ante SOC2 / ISO 27001 y quality gates en CI/CD.

### Reto adicional
Generar automáticamente la matriz de trazabilidad que cruza los hallazgos técnicos individuales con los artículos específicos de normativas como GDPR o HIPAA.

---
> [← Ejercicio 097](../ejercicio_097/README.md) · [Índice General](../README.md) · [Ejercicio 099 →](../ejercicio_099/README.md)
