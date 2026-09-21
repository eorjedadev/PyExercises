## Ejercicio 066 — Auditor y Enforcer de Tags en Recursos Cloud (`tag-auditor`)

> [← Ejercicio 065](../ejercicio_065/README.md) · [Índice General](../README.md) · [Ejercicio 067 →](../ejercicio_067/README.md)

### Contexto profesional
En arquitecturas cloud empresariales (AWS, Azure, GCP), todas las instancias de cómputo, bases de datos y buckets de almacenamiento deben contener etiquetas (tags) de gobernanza obligatorias (ej. `Environment`, `CostCenter`, `Owner`, `Project`, `Compliance`). La ausencia de estas etiquetas dificulta la asignación de costos y viola normativas de seguridad.

### Problema
Construir una CLI que audite un inventario de recursos cloud (leído desde JSON/YAML exportado de Terraform/CloudFormation o base de datos relacional PostgreSQL/SQLite), valide el cumplimiento de políticas de etiquetado (presencia de tags requeridos, formato de valores permitidos con regex), reporte recursos no conformes y permita aplicar auto-remediación (`--fix` o `--dry-run`).

### Usuario objetivo
Ingenieros de FinOps, arquitectos de seguridad cloud y DevOps.

### Objetivo
Desarrollar un motor de evaluación y cumplimiento de políticas de etiquetado cloud con soporte de auto-remediación y reportes de conformidad.

### Ejemplo conceptual de uso
```bash
# Auditar inventario de recursos contra política de tags obligatorios
python tag_auditor.py audit --inventory resources.json --policy tag_policy.json

# Generar script de remediación automática o simular con dry-run
python tag_auditor.py enforce --inventory resources.json --policy tag_policy.json --fix --dry-run
```

### Requisitos funcionales
- Parsear inventarios de recursos cloud con formato: ID de recurso, Tipo (`aws_instance`, `s3_bucket`, `rds_cluster`), Región y diccionario de Tags.
- Archivo de política `tag_policy.json` configurable:
  - `required_tags`: lista de tags obligatorios (ej. `["Environment", "Owner", "CostCenter"]`).
  - `allowed_values`: valores cerrados permitidos (ej. `Environment: ["dev", "stage", "prod"]`).
  - `value_patterns`: expresiones regulares (ej. `CostCenter: "^CC-[0-9]{4}$"`).
- Subcomando `audit`: genera reporte de no conformidad con porcentaje de cumplimiento global y listado de recursos infractores con sus tags faltantes o inválidos.
- Subcomando `enforce`: aplica valores por defecto de remediación a los recursos que admitan auto-fix o genera el script de parcheo en Terraform/AWS CLI.
- Soportar almacenamiento y seguimiento de tendencias de cumplimiento en PostgreSQL o SQLite opcional.

### Requisitos de CLI
- Subcomandos: `audit`, `enforce`, `policy-check`.
- Opción `--inventory <RUTA>`.
- Opción `--policy <RUTA>`.
- Flag `--fix`.
- Flag `--dry-run`.
- Opción `--format [table|json|csv]`.
- Exit code 0 si el 100% de los recursos cumple la política, 1 si hay recursos no conformes, 2 en errores.

### Entradas
- Archivo de inventario de recursos y archivo de políticas de tagging.

### Salidas
- Reporte de cumplimiento y estadísticas de gobernanza en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) para almacenar el histórico de auditorías.

### Validaciones
- Comprobar que el archivo de política tenga una estructura válida.
- Validar las expresiones regulares definidas en la política.

### Casos límite
- Recursos con tags vacíos o que contienen caracteres especiales.
- Inventarios gigantes con decenas de miles de recursos.
- Recursos heredados (legacy) exentos mediante lista blanca (`--exemptions`).

### Manejo de errores
- Errores de sintaxis en el inventario JSON.
- `re.error` en patrones de validación.

### Fundamentos de Python relacionados
- Validación de esquemas de datos y evaluación de expresiones regulares (`re`).
- Procesamiento de colecciones y cálculo de porcentajes.
- Persistencia de auditorías en PostgreSQL / SQLite.
- Subparsers de `argparse`.

### Conceptos CLI relacionados
- Auditoría de gobernanza (Governance as Code) en terminal.
- Mecanismos de remediación segura con `--dry-run`.

### Herramientas o módulos para investigar
- `re`.
- `json`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para calcular el costo financiero estimado de los recursos huérfanos sin etiqueta `CostCenter`?

### Diseño de argumentos
¿Cómo nombrarías la opción para auditar únicamente recursos de un tipo específico (ej. `--resource-type aws_instance`)?

### Diseño de variables
`resources_inventory_list`, `tag_policy_rules_dict`, `non_compliant_resources_list`, `compliance_score_percentage`, `remediation_patch_actions`.

### Antes de programar
1. ¿Cómo estructurar el reporte de auditoría para que indique claramente: Recurso, Tipo, Tag Faltante o Motivo de Rechazo de Valor?
2. ¿Cómo calcular el score de cumplimiento global: $\frac{\text{recursos conformes}}{\text{total recursos}} \times 100$?

### Arquitectura
Motor de políticas (`policy_engine.py`), evaluador de cumplimiento (`compliance_evaluator.py`), remediador (`remediator.py`) y CLI.

### Pruebas mínimas
1. Auditar un inventario de 5 recursos contra una política con 3 tags obligatorios; verificar que detecte los 2 recursos incompletos y retorne exit code 1.
2. Ejecutar `enforce --fix --dry-run` y verificar que muestre las acciones de remediación sin alterar el archivo original.

### Pruebas de error
1. Pasar un archivo de política con JSON corrupto -> Exit code 2 con error claro.

### Experiencia de usuario
Tabla de resumen con barra visual de porcentaje de cumplimiento: `[████████░░░░] 68.5% Cumplimiento (137/200 recursos conformes)` y lista de no conformidades.

### Explicación posterior
Explica la importancia de la gobernanza de tags en la disciplina FinOps para la asignación y atribución precisa de costos en la nube.

### Aplicación profesional
Security & Governance gates en CI/CD antes de aplicar cambios de Terraform, y auditorías periódicas de cumplimiento cloud.

### Reto adicional
Generar automáticamente los comandos de remediación en la CLI nativa del proveedor (ej. `aws ec2 create-tags --resources ... --tags Key=CostCenter,Value=CC-9999`).

---
> [← Ejercicio 065](../ejercicio_065/README.md) · [Índice General](../README.md) · [Ejercicio 067 →](../ejercicio_067/README.md)
