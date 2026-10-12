## Ejercicio 057 — Control de Gastos Personales y Presupuestos Mensuales (`BudgetExpenseSqliteApp`)

> [Índice General](../README.md) · [← Ejercicio 056](../ejercicio_056/README.md) · [Ejercicio 058 →](../ejercicio_058/README.md)

### Contexto profesional
En finanzas personales y control de presupuestos para emprendedores, los usuarios definen un tope de gasto mensual por categoría y registran sus consumos diarios.

### Usuario objetivo
Usuario particular o profesional independiente.

### Problema
El gasto descontrolado en rubros cotidianos provoca que los presupuestos mensuales se superen antes de fin de mes sin advertencias oportunas.

### Objetivo
Desarrollar una aplicación de finanzas personales en SQLite (`presupuesto.db`), con tabla de presupuestos por categoría (Alimentos, Transporte, Vivienda, Ocio), registro diario de gastos y advertencia visual inmediata (barra o etiqueta en rojo) cuando los gastos acumulados superen el 90% o 100% del límite asignado.

### Flujo principal
El usuario define el presupuesto mensual de cada categoría. Durante el mes, registra compras ingresando fecha, categoría, monto y concepto. Al registrar un gasto, la aplicación consulta el total acumulado de esa categoría; si supera el 90% del presupuesto mensual, muestra una advertencia preventiva; si excede el 100%, emite una alerta crítica y resalta la fila en rojo.

### Requisitos funcionales
- Esquema SQLite con tablas `categorias_presupuesto` (categoría, limite_mensual) y `gastos` (fecha, categoria_id, monto, concepto).
- Configuración y ajuste de topes mensuales por categoría.
- Registro rápido de gastos diarios con fecha automática.
- Consulta en tiempo real de porcentaje de presupuesto consumido: $(\text{Gasto Acumulado} / \text{Presupuesto}) \times 100$.
- Barra de progreso o indicador cromático por categoría: Verde (<75%), Amarillo (75-90%), Rojo (>90%).
- Tabla `ttk.Treeview` con el historial de gastos del mes seleccionado.

### Requisitos de interfaz
- Panel superior con formulario de captura rápida de gastos.
- Panel lateral o central con barras de consumo presupuestario por categoría.
- Tabla inferior con el historial detallado de movimientos.

### Datos
- Presupuesto: id, categoria, limite_mensual.
- Gasto: id, fecha, categoria_id, concepto, monto.

### Estado
- Mes y año activos en consulta.
- Acumulados por categoría calculados en memoria.

### Persistencia
Base de datos relacional SQLite (`datos/presupuesto.db`).

### Validaciones
- Monto de gasto estrictamente mayor a 0.0.
- Límite presupuestario mayor o igual a 0.0.
- Concepto obligatorio.

### Casos límite
- Categoría con presupuesto $0 (cualquier gasto representaría el infinito%, debe manejarse con mensaje de 'Sin presupuesto asignado').
- Gastos registrados en meses anteriores.

### Manejo de errores
- Prevenir divisiones por cero al calcular el porcentaje consumido si el presupuesto es cero.

### Fundamentos de Python relacionados
- Fórmulas de consumo porcentual y manejo de divisiones seguras.
- Consultas SQL con `SUM()` y filtro de mes con `strftime('%Y-%m', fecha)`.

### Conceptos Tkinter relacionados
- Uso de múltiples widgets `ttk.Progressbar` enlazados dinámicamente a porcentajes de datos.
- Indicadores de alerta cromáticos.

### Herramientas para investigar
- Función `strftime()` en consultas de fecha en SQLite.
- Widget `ttk.Progressbar` de Tkinter.

### Diseño de interfaz
¿Cómo asegurarías que las barras de progreso presupuestarias sean claras y no saturen la pantalla si existen 8 categorías de gasto?

### Diseño de variables
Usa nombres como `expense_tree`, `amount_entry`, `category_combo`, `desc_entry`, `food_progress_bar`, `transport_progress_bar`, `db_budget`.

### Antes de programar
1. ¿Cómo se agrupan los gastos de un mes específico en SQLite usando `strftime('%Y-%m', fecha) = ?`?
2. ¿Cómo se actualiza el valor de una barra de progreso en Tkinter con `.configure(value=porcentaje)`?

### Arquitectura
```
ejercicio_057/
├── app.py           # Vistas financieras, barras y formulario de gasto
├── budget_repo.py   # Consultas y agregaciones de gastos en SQLite
└── datos/
    └── presupuesto.db # Base de datos financiera local
```

### Pruebas mínimas
1. Presupuesto Alimentos $1000 -> Registrar gasto de $500 -> Barra debe marcar 50% en verde.
2. Registrar gasto de $450 más -> Total acumulado $950 (95%), debe alertar sobrepaso inminente en rojo.

### Pruebas de error
1. Ingresar monto $0 o negativo -> Debe rechazar el gasto indicando monto inválido.

### Experiencia de usuario
La advertencia visual de presupuesto excedido debe ser evidente pero sin bloquear el registro del gasto (el usuario debe poder registrar el gasto real a pesar del sobrepaso).

### Explicación posterior
¿Cómo se calculan consumos acumulados contra topes fijos en SQL y cómo se reflejan de forma reactiva en componentes de progreso?

### Aplicación profesional
Aplicaciones de finanzas personales, control de gastos de caja chica en empresas y presupuestos departamentales.

### Reto adicional
Añade un selector de mes que permita consultar el histórico de cumplimiento presupuestario de meses anteriores.

---
> [Índice General](../README.md) · [← Ejercicio 056](../ejercicio_056/README.md) · [Ejercicio 058 →](../ejercicio_058/README.md)
