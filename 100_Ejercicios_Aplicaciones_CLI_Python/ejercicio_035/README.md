## Ejercicio 035 — Rastreador de Gastos y Presupuestos con Reportes CSV (`expense-tracker`)

> [← Ejercicio 034](../ejercicio_034/README.md) · [Índice General](../README.md) · [Ejercicio 036 →](../ejercicio_036/README.md)

### Contexto profesional
Los profesionales independientes (freelancers), consultores y pequeños equipos necesitan registrar gastos operativos diarios (software, hosting, viajes, suministros), clasificarlos por categoría y generar reportes mensuales consolidados para contabilidad sin depender de hojas de cálculo lentas o aplicaciones en la nube de pago.

### Problema
Construir una CLI para registrar gastos e ingresos, categorizarlos, consultar resúmenes por rango de fechas o categoría, calcular el balance neto (ingresos menos gastos), alertar si se supera un presupuesto mensual definido y exportar reportes tabulares y CSV.

### Usuario objetivo
Freelancers, desarrolladores independientes y administradores de proyectos.

### Objetivo
Desarrollar un sistema de registro financiero personal en terminal con agregación de datos, control de presupuestos y persistencia CSV.

### Ejemplo conceptual de uso
```bash
# Registrar un gasto de hosting
python expense_tracker.py add expense 49.99 --category "Hosting" --desc "Servidor AWS producción"

# Registrar un ingreso por consultoría
python expense_tracker.py add income 1500.00 --category "Servicios" --desc "Desarrollo API cliente X"

# Ver resumen financiero del mes actual
python expense_tracker.py summary --month 2026-06
```

### Requisitos funcionales
- Subcomando `add [expense|income] <MONTO>`: registra una transacción con monto, categoría, descripción y fecha (default hoy `YYYY-MM-DD`).
- Subcomando `list`: lista transacciones con filtros opcionales (`--category`, `--from-date`, `--to-date`, `--type`).
- Subcomando `summary`: calcula total de ingresos, total de gastos, balance neto y desglose porcentual por categoría.
- Subcomando `budget set <CATEGORIA> <LIMITE>`: establece un presupuesto mensual para una categoría y alerta en `summary` si el gasto real supera dicho límite.
- Subcomando `export`: exporta el libro contable a un nuevo archivo CSV filtrado.

### Requisitos de CLI
- Subcomandos: `add`, `list`, `summary`, `budget`, `export`.
- Opciones de filtrado y fechas.
- Exit code 0 en éxito, 1 si se superó algún presupuesto crítico en modo estricto, 2 en argumentos inválidos.

### Entradas
- Montos decimales, categorías, fechas y descripciones.

### Salidas
- Tablas financieras, resúmenes consolidados y alertas de presupuesto en STDOUT.

### Persistencia
Archivo CSV para transacciones (`expenses.csv`) y archivo JSON/CSV para presupuestos (`budgets.json`).

### Validaciones
- El monto debe ser un número estrictamente positivo.
- Las fechas deben cumplir el formato ISO `YYYY-MM-DD`.
- No permitir categorías vacías.

### Casos límite
- Mes sin transacciones registradas (debe mostrar balance 0.00 sin errores).
- Gastos registrados con fechas futuras.
- Transacciones con decimales de centavos (manejo de redondeo exacto).

### Manejo de errores
- `ValueError` en montos o fechas.
- Manejo de archivo CSV corrupto o bloqueado.

### Fundamentos de Python relacionados
- Módulo `decimal.Decimal` para precisión financiera.
- Módulos `csv` y `datetime`.
- Agrupación y agregación de datos con `collections.defaultdict` o comprensiones de diccionarios.

### Conceptos CLI relacionados
- Cálculos y agregaciones estadísticas en herramientas de terminal.
- Persistencia tabular estructurada.

### Herramientas o módulos para investigar
- `decimal`.
- `csv`.
- `datetime`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `delete <ID>` para anular una transacción por su identificador?

### Diseño de argumentos
¿Cómo nombrarías la opción para mostrar el reporte en una divisa específica o con símbolo monetario (`--currency USD|EUR`)?

### Diseño de variables
`transaction_type`, `amount_decimal`, `category_name`, `transaction_date`, `monthly_aggregates`, `budget_limits`.

### Antes de programar
1. ¿Cómo calcular el balance y los porcentajes por categoría acumulando con `Decimal` para evitar desajustes de un centavo?
2. ¿Cómo estructurar el archivo CSV con encabezados consistentes (`id,date,type,category,amount,description`)?

### Arquitectura
Estructura:
```
ejercicio_035/
├── expense_tracker.py
├── ledger_repository.py
├── budget_service.py
└── views.py
```

### Pruebas mínimas
1. Agregar 1 ingreso de 1000 y 2 gastos de 200 y 300; verificar que `summary` reporte exactamente 1000 de ingresos, 500 de gastos y 500 de balance neto.
2. Fijar presupuesto de 100 en hosting, gastar 150 y verificar que `summary` emita la alerta de presupuesto excedido.

### Pruebas de error
1. Intentar registrar un monto negativo `-50` -> Exit code 2 con error de validación.

### Experiencia de usuario
Tabla visualmente atractiva con colores: verde para ingresos y balances positivos, rojo para gastos y advertencias de sobregiro.

### Explicación posterior
Explica la importancia del principio de partida doble y la inmutabilidad de registros contables (ledger audit trail).

### Aplicación profesional
Gestión contable personal, auditoría de gastos de proyectos y control de micro-presupuestos operativos.

### Reto adicional
Generar un gráfico de barras horizontal en texto ASCII que represente la distribución porcentual de gastos por categoría en terminal.

---
> [← Ejercicio 034](../ejercicio_034/README.md) · [Índice General](../README.md) · [Ejercicio 036 →](../ejercicio_036/README.md)
