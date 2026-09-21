## Ejercicio 085 — Auditor de Costos Cloud y Detección de Recursos Huérfanos (`cost-auditor`)

> [← Ejercicio 084](../ejercicio_084/README.md) · [Índice General](../README.md) · [Ejercicio 086 →](../ejercicio_086/README.md)

### Contexto profesional
En cuentas de infraestructura cloud (AWS, Azure, GCP), los entornos de desarrollo y pruebas acumulan constantemente recursos no utilizados pero que siguen facturándose cada hora (volúmenes de disco EBS desacoplados/unattached, direcciones IP elásticas sin asociar, balanceadores de carga sin instancias destino, snapshots de hace años, instancias de base de datos inactivas), generando miles de dólares de desperdicio mensual.

### Problema
Construir una CLI de auditoría de costos (FinOps) que analice inventarios de recursos cloud y volcados de costos (exportados en JSON/CSV desde AWS Cost Explorer o Terraform State), identifique recursos huérfanos e infrautilizados, calcule el desperdicio financiero mensual en dólares, proyecte el ahorro potencial y genere un reporte ejecutivo exportable con scripts de limpieza segura.

### Usuario objetivo
Ingenieros de FinOps, DevOps y líderes de infraestructura.

### Objetivo
Crear un auditor de costos cloud con detección de desperdicio, cálculo de proyecciones de ahorro y generación de scripts de remediación.

### Ejemplo conceptual de uso
```bash
# Auditar recursos huérfanos y calcular desperdicio mensual
python cost_auditor.py audit --inventory cloud_resources.json --pricing pricing_catalog.json

# Generar script de remediación con dry-run para eliminar recursos no utilizados
python cost_auditor.py remediate --inventory cloud_resources.json --dry-run -o cleanup.sh

# Ver reporte ejecutivo de ahorro potencial en formato Markdown
python cost_auditor.py report --inventory cloud_resources.json --format markdown
```

### Requisitos funcionales
- Reglas de detección de recursos huérfanos y desperdicio:
  - Volúmenes de almacenamiento desacoplados (ej. discos EBS en estado `available` sin instancia asociada).
  - Direcciones IP elásticas asignadas pero no asociadas a ninguna instancia activa.
  - Balanceadores de carga sin targets saludables (0 targets registrados).
  - Snapshots de disco y backups con más de 90 días de antigüedad.
  - Instancias de base de datos o máquinas virtuales con utilización media de CPU menor al 2% durante los últimos 14 días (recursos sobredimensionados / idle).
- Subcomando `audit`: calcula el costo mensual individual y acumulado de todos los recursos huérfanos usando el catálogo de precios.
- Subcomando `remediate`: genera el script bash/CLI con los comandos de eliminación segura de los recursos huérfanos identificados.
- Subcomando `report`: genera un reporte ejecutivo con métricas de FinOps: Gasto Total, Desperdicio Identificado, % de Ahorro Potencial y desglose por tipo de recurso.
- Persistencia de auditorías históricas en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `audit`, `remediate`, `report`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--inventory <RUTA>`.
- Opción `--pricing <RUTA>`.
- Flag `--dry-run`.
- Opción `--format [table|json|markdown|csv]`.
- Exit code 0 si el desperdicio mensual está por debajo del umbral de tolerancia, 1 si supera el límite de gasto innecesario (`--max-waste-usd`), 2 en errores.

### Entradas
- Archivos de inventario de recursos cloud y catálogos de precios.

### Salidas
- Reportes financieros y scripts de remediación en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `cost_audits`, `waste_findings` y `savings_projections`.

### Validaciones
- Validar la estructura del inventario de recursos y archivo de precios.
- Los costos calculados deben usar precisión decimal estricta.

### Casos límite
- Recursos compartidos que parecen huérfanos pero están en reserva (permitir lista blanca `--whitelist`).
- Inventarios con miles de recursos en múltiples regiones.
- Precios de recursos que varían según la región geográfica.

### Manejo de errores
- `KeyError` ante tipos de recursos sin precio en el catálogo.
- Errores de parsing de archivos JSON/CSV.

### Fundamentos de Python relacionados
- Precisión financiera con `decimal.Decimal`.
- Agrupaciones y agregaciones estadísticas de datos con diccionarios.
- Persistencia de auditorías en PostgreSQL / SQLite.
- Subparsers de `argparse`.

### Conceptos CLI relacionados
- Herramientas de optimización de costos en la nube (Cloud FinOps).
- Estimación de ahorro y cálculo de proyecciones financieras en terminal.

### Herramientas o módulos para investigar
- `decimal`.
- `json` y `csv`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `estimate-budget --growth-rate 0.05` para proyectar los costos a 12 meses vista?

### Diseño de argumentos
¿Cómo nombrarías la opción para filtrar por centro de costos o etiqueta de proyecto (`--cost-center "CC-104"`)?

### Diseño de variables
`cloud_resources_list`, `pricing_catalog_map`, `orphaned_resources_findings`, `monthly_waste_amount_decimal`, `potential_annual_savings_decimal`.

### Antes de programar
1. ¿Cómo calcular el costo mensual de un volumen EBS huérfano de 500 GB sabiendo que el precio unitario es `$0.08` por GB/mes ($500 \times 0.08 = \$40.00$/mes)?
2. ¿Cómo estructurar el script de remediación generado para que incluya comentarios con el costo ahorrado por cada comando `aws ec2 delete-volume --volume-id ... # Ahorra $40/mes`?

### Arquitectura
Lector de inventario (`inventory_reader.py`), motor de reglas de detección (`waste_detector.py`), calculadora de costos (`pricing_calculator.py`), generador de reportes (`report_generator.py`) y CLI.

### Pruebas mínimas
1. Auditar un inventario con 2 volúmenes desacoplados de 100 GB ($16/mes) y 1 IP elástica suelta ($3.60/mes); verificar que reporte exactamente $19.60/mes de desperdicio.
2. Ejecutar `remediate --dry-run` y verificar que genere los comandos `delete-volume` y `release-address` correspondientes.

### Pruebas de error
1. Pasar un inventario con formato JSON corrupto -> Exit code 2 con error claro.

### Experiencia de usuario
Reporte financiero ejecutivo con colores: Amarillo para advertencias de gasto, Rojo para recursos altamente costosos y Verde para el resumen de ahorro estimado.

### Explicación posterior
Explica los principios fundamentales del marco FinOps (Informar, Optimizar, Operar) y la importancia del monitoreo continuo de recursos huérfanos.

### Aplicación profesional
Optimización mensual de facturas de AWS/Azure en organizaciones de tecnología y auditorías de costos previas a renovaciones de contratos cloud.

### Reto adicional
Implementar sugerencias de optimización por compromiso de uso (Reserved Instances / Savings Plans) calculando el ahorro potencial al migrar instancias bajo demanda (On-Demand) a planes reservados de 1 o 3 años.

---
> [← Ejercicio 084](../ejercicio_084/README.md) · [Índice General](../README.md) · [Ejercicio 086 →](../ejercicio_086/README.md)
