## Ejercicio 028 — Visor y Buscador de Transacciones Financieras (`TransactionViewerApp`)

> [Índice General](../README.md) · [← Ejercicio 027](../ejercicio_027/README.md) · [Ejercicio 029 →](../ejercicio_029/README.md)

### Contexto profesional
En departamentos de contabilidad y auditoría fiscal, los auditores reciben volcados masivos de extractos bancarios en CSV y necesitan filtrar movimientos por rangos de fecha y categorías de gasto.

### Usuario objetivo
Auditor contable o analista financiero.

### Problema
Revisar cientos de transacciones bancarias en hojas de cálculo pesadas resulta lento y no permite calcular rápidamente saldos acumulados de selecciones específicas.

### Objetivo
Desarrollar una aplicación para cargar y visualizar extractos de transacciones en un `ttk.Treeview`, con filtros por rango de fechas (desde/hasta), categoría y tipo (Ingreso/Egreso), calculando en tiempo real el saldo neto de los registros visibles.

### Flujo principal
El auditor carga el extracto de transacciones bancarias. La tabla despliega fecha, concepto, categoría, tipo y monto. Conforme aplica filtros de fecha o categoría, la tabla actualiza los registros mostrados y la barra de totales recalcula de inmediato el total de ingresos, total de egresos y el saldo neto de la vista actual.

### Requisitos funcionales
- Carga de archivo CSV de transacciones (`datos/transacciones.csv`).
- Visualización en `ttk.Treeview` con formateo de moneda y colores (verde para ingresos, rojo para egresos).
- Filtros combinables: Categoría (`Combobox`), Tipo (`Radiobutton`), Fecha Inicial y Fecha Final.
- Botón para limpiar todos los filtros y restaurar la vista completa.
- Cálculo automático del resumen: Total Ingresos, Total Egresos, Saldo Neto de los registros actualmente mostrados.

### Requisitos de interfaz
- Barra superior con controles de filtrado agrupados ordenadamente.
- Treeview central con scrollbar.
- Panel inferior destacado con tarjetas o etiquetas para Total Ingresos, Total Egresos y Saldo Neto.

### Datos
- Transacción: ID, Fecha (YYYY-MM-DD), Concepto, Categoría, Tipo ('INGRESO' | 'EGRESO'), Monto (float).

### Estado
- Lista maestra completa de transacciones.
- Lista filtrada de transacciones visibles.
- Variables de filtro activas.

### Persistencia
Lectura desde archivo CSV (`datos/transacciones.csv`).

### Validaciones
- Validar formato de fechas al filtrar (YYYY-MM-DD).
- Comprobar que la fecha final sea igual o posterior a la inicial si ambas están presentes.

### Casos límite
- El filtro no coincide con ninguna transacción (tabla vacía, ingresos 0, egresos 0, saldo neto 0).
- Transacciones con montos en cero o decimales extensos.

### Manejo de errores
- Manejar fechas mal ingresadas en los filtros mostrando aviso de formato sin romper el flujo.

### Fundamentos de Python relacionados
- Filtrado avanzado con predicados y funciones lambda o comprensiones de listas.
- Parseo de fechas para comparaciones cronológicas (`datetime.strptime`).
- Manejo de CSV y conversiones de tipos.

### Conceptos Tkinter relacionados
- Tags de colores por fila en `Treeview` para diferenciar ingresos de egresos.
- Separación estricta entre lista maestra de datos y lista proyectada en la interfaz.

### Herramientas para investigar
- Métodos de filtrado en colecciones de Python.
- Formateo condicional con `tree.tag_configure()`.

### Diseño de interfaz
¿Cómo asegurarías que el panel inferior de totales tenga suficiente contraste para distinguir claramente ingresos (positivo) de egresos (negativo)?

### Diseño de variables
Usa nombres como `trans_tree`, `cat_filter_combo`, `start_date_entry`, `end_date_entry`, `total_income_label`, `total_expense_label`, `net_balance_label`.

### Antes de programar
1. ¿Por qué es vital que el cálculo del balance neto se ejecute sobre la lista filtrada y no sobre la lista maestra completa?
2. ¿Cómo evitas tener que recargar el archivo CSV del disco cada vez que el usuario cambia un filtro?

### Arquitectura
```
ejercicio_028/
├── app.py              # Interfaz gráfica y controles de filtro
├── ledger_service.py   # Lógica de filtrado y cálculo de balances
└── datos/
    └── transacciones.csv # Dataset de transacciones bancarias
```

### Pruebas mínimas
1. Aplicar filtro de categoría 'Servicios' -> La tabla debe mostrar solo esas transacciones y el saldo neto debe reflejar la suma exacta de sus montos.
2. Limpiar filtros -> La tabla debe mostrar el universo completo de transacciones.

### Pruebas de error
1. Ingresar fecha '2026-15-40' en el filtro -> Debe advertir error de fecha sin cerrar la app.

### Experiencia de usuario
La respuesta al presionar 'Aplicar Filtros' debe ser instantánea y los números deben estar alineados a la derecha en la tabla.

### Explicación posterior
¿Por qué mantener los datos maestros en memoria permite un filtrado instantáneo sin latencia de disco?

### Aplicación profesional
Extractores bancarios de tesorería, visores contables para auditoría interna y módulos de flujo de caja.

### Reto adicional
Añade un botón 'Exportar Vista Actual a CSV' que guarde exclusivamente las filas filtradas en un nuevo archivo seleccionado por el usuario con `filedialog.asksaveasfilename`.

---
> [Índice General](../README.md) · [← Ejercicio 027](../ejercicio_027/README.md) · [Ejercicio 029 →](../ejercicio_029/README.md)
