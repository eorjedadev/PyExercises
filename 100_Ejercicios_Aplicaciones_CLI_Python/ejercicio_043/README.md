## Ejercicio 043 — Gestor de Licencias y Suscripciones de Software (`sub-tracker`)

> [← Ejercicio 042](../ejercicio_042/README.md) · [Índice General](../README.md) · [Ejercicio 044 →](../ejercicio_044/README.md)

### Contexto profesional
Las empresas y agencias de desarrollo gastan miles de dólares mensuales en decenas de suscripciones SaaS (GitHub, AWS, Datadog, Slack, Figma, JetBrains). Con frecuencia, las suscripciones se renuevan automáticamente sin revisión previa o se pagan licencias de empleados que ya no pertenecen a la empresa.

### Problema
Construir una CLI con base de datos relacional para registrar suscripciones de software, proveedores, costos recurrentes, fechas de renovación, cantidad de licencias contratadas vs asignadas y generar alertas de vencimiento próximo y proyecciones de gasto anual.

### Usuario objetivo
Líderes de ingeniería, directores de tecnología (CTO) y gestores de compras.

### Objetivo
Desarrollar una herramienta de gestión financiera de suscripciones con backend en PostgreSQL (o SQLite opcional), cálculo de métricas financieras y reportes de alertas.

### Ejemplo conceptual de uso
```bash
# Registrar una nueva suscripción SaaS
python sub_tracker.py add "Figma Enterprise" --vendor "Figma" --cost 45.00 --billing monthly --seats 20 --renewal "2026-07-01"

# Consultar suscripciones que vencen en los próximos 30 días
python sub_tracker.py expiring --days 30

# Ver proyección de costos anuales y gasto por proveedor
python sub_tracker.py costs --forecast annual
```

### Requisitos funcionales
- Subcomando `add`: registra suscripción con nombre, proveedor, costo recurrente, periodicidad (`monthly`, `yearly`, `quarterly`), cantidad de asientos (`seats`), fecha de renovación y estado (`ACTIVE`, `CANCELLED`, `TRIAL`).
- Subcomando `list`: consulta de suscripciones activas con cálculo del costo mensual normalizado.
- Subcomando `expiring`: lista suscripciones con fecha de renovación próxima dentro de N días para evitar renovaciones no deseadas.
- Subcomando `costs`: calcula el gasto total mensual consolidado, proyección anual y distribución porcentual de costos por proveedor.
- Subcomando `cancel <ID>`: marca una suscripción como cancelada con fecha de término de contrato.
- Subcomando `audit-seats`: compara licencias contratadas vs asignadas para identificar desperdicio.

### Requisitos de CLI
- Subcomandos: `add`, `list`, `expiring`, `costs`, `cancel`, `audit-seats`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--format [table|json|csv]`.
- Exit code 0 en éxito, 1 si existen suscripciones críticas en riesgo de renovación no autorizada en modo auditoría, 2 en errores.

### Entradas
- Parámetros de suscripciones y credenciales de base de datos.

### Salidas
- Tablas financieras, alertas de renovación y reportes de costes en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `subscriptions`, `seat_allocations` y `cost_history`.

### Validaciones
- El costo debe ser un decimal mayor a 0.
- La periodicidad debe pertenecer al catálogo (`monthly`, `yearly`, `quarterly`).
- Las fechas deben tener formato ISO `YYYY-MM-DD`.

### Casos límite
- Suscripciones con periodicidad anual o trimestral (calcular correctamente la normalización a costo mensual equivalente).
- Fechas de renovación en años bisiestos (ej. 29 de febrero).
- Suscripciones canceladas que aún tienen vigencia hasta el fin del ciclo de facturación.

### Manejo de errores
- Errores de conexión a base de datos.
- Fechas inválidas o en el pasado.

### Fundamentos de Python relacionados
- Precisión decimal con `decimal.Decimal`.
- Manejo de fechas y aritmética de intervalos con `datetime.date` y `datetime.timedelta`.
- Repositorio relacional con soporte para PostgreSQL y SQLite.

### Conceptos CLI relacionados
- Generación de reportes de proyección y forecasting en terminal.
- Normalización de métricas heterogéneas.

### Herramientas o módulos para investigar
- `decimal`.
- `datetime`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `import-csv` para cargar un listado masivo de suscripciones desde un extracto bancario o reporte contable?

### Diseño de argumentos
¿Cómo nombrarías la opción para filtrar por moneda o aplicar una tasa de conversión a USD (`--target-currency USD`)?

### Diseño de variables
`subscription_record`, `monthly_normalized_cost`, `annual_forecast_total`, `days_until_renewal`, `vendor_cost_aggregates`.

### Antes de programar
1. ¿Cómo normalizar una suscripción de $1,200/año y una de $100/mes para sumarlas en un costo mensual consolidado exacto?
2. ¿Cómo construir la consulta SQL en PostgreSQL/SQLite para filtrar suscripciones cuya fecha de renovación caiga en el rango `[CURRENT_DATE, CURRENT_DATE + INTERVAL '30 days']`?

### Arquitectura
Modelos (`models.py`), repositorio (`subscription_repo.py`), servicio financiero (`financial_calc.py`) y CLI.

### Pruebas mínimas
1. Registrar 1 suscripción mensual de $10 y 1 anual de $120; verificar que `costs` reporte exactamente $20/mes de gasto consolidado y $240/año.
2. Probar `expiring --days 15` con una suscripción que vence en 5 días y verificar que aparezca en la lista.

### Pruebas de error
1. Intentar registrar una suscripción con periodicidad desconocida `semanal` -> Exit code 2.

### Experiencia de usuario
Tablas claras con colores: Amarillo para suscripciones que vencen en menos de 15 días, Verde para estado activo, Gris para canceladas.

### Explicación posterior
Explica el concepto de MRR (Monthly Recurring Revenue / Cost) y cómo las herramientas de optimización SaaS (SaaS spend management) ahorran costos a las empresas.

### Aplicación profesional
Control de presupuesto operativo de TI, auditorías de contratos de proveedores y optimización de licencias de software.

### Reto adicional
Generar automáticamente un archivo de calendario `.ics` con eventos recordatorios 7 días antes de cada fecha de renovación registrada.

---
> [← Ejercicio 042](../ejercicio_042/README.md) · [Índice General](../README.md) · [Ejercicio 044 →](../ejercicio_044/README.md)
