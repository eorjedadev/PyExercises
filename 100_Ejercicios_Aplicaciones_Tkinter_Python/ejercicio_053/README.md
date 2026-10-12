## Ejercicio 053 — Control de Mermas y Desperdicios en Línea de Producción (`WasteTrackingApp`)

> [Índice General](../README.md) · [← Ejercicio 052](../ejercicio_052/README.md) · [Ejercicio 054 →](../ejercicio_054/README.md)

### Contexto profesional
En plantas de manufactura de alimentos y ensamble industrial, los supervisores de turno registran los desperdicios y piezas defectuosas generadas en cada línea de ensamble para análisis de costos de no calidad.

### Usuario objetivo
Supervisor de producción o analista de calidad de planta.

### Problema
La falta de registro en tiempo real de mermas oculta desviaciones en maquinaria defectuosa hasta el cierre mensual de inventarios.

### Objetivo
Construir una aplicación de registro de desperdicios industriales con SQLite (`mermas.db`), captura de lote, motivo de merma (Rotura, Calibración, Defecto de Materia Prima, Caducidad), costo monetario perdido y reporte acumulado filtrable por fecha y línea.

### Flujo principal
El supervisor selecciona la línea de producción (Línea 1, 2, 3), el código de lote y el motivo de desperdicio. Ingresa la cantidad de unidades mermadas y el costo unitario. La aplicación calcula el costo total de la merma, lo almacena en SQLite y actualiza la tabla del turno. Un panel superior muestra el costo acumulado de pérdidas del día en tiempo real.

### Requisitos funcionales
- Base de datos SQLite con tabla `registros_merma`.
- Captura: Fecha y Hora, Línea de Producción (`Combobox`), Código de Lote, Motivo (`Combobox`), Cantidad Mermada (entero), Costo Unitario (flotante).
- Cálculo automático del Costo Total Perdido: $\text{Cantidad} \times \text{Costo Unitario}$.
- Visualización en `ttk.Treeview`: Folio, Fecha, Línea, Lote, Motivo, Unidades, Pérdida ($).
- Filtro por Línea y por Rango de Fechas.
- Panel de métricas: Total de Unidades Desperdiciadas y Pérdida Financiera Acumulada del Turno.

### Requisitos de interfaz
- Formulario superior ordenado con cálculo del costo en tiempo real.
- `Treeview` central con doble scrollbar y formato de moneda.
- Tarjeta de alerta destacada con el monto total de pérdidas en color rojo.

### Datos
- Merma: id, folio, fecha, linea, lote, motivo, cantidad, costo_unitario, costo_total.

### Estado
- Lista de mermas consultadas en memoria.
- Filtros activos de línea y fecha.

### Persistencia
Base de datos SQLite local (`datos/mermas.db`).

### Validaciones
- Cantidad mermada debe ser entero positivo mayor a cero.
- Costo unitario debe ser mayor a cero.
- Lote y motivo son campos obligatorios.

### Casos límite
- Registrar merma con costo unitario de céntimos (ej. $0.15 por tornillo).
- Turnos nocturnos que cruzan la medianoche.

### Manejo de errores
- Validar entradas numéricas notificando cualquier fallo de tipo o valor.

### Fundamentos de Python relacionados
- Agrupación y sumas acumuladas con SQL (`GROUP BY motivo`).
- Generación de folios de merma formateados con marcas de tiempo.

### Conceptos Tkinter relacionados
- Enlaces reactivos para cálculo de costo total mientras se digita cantidad o costo unitario.
- Actualización dinámica de etiquetas de impacto financiero.

### Herramientas para investigar
- Consultas de resumen financiero en SQLite.
- Eventos de teclado en campos numéricos.

### Diseño de interfaz
¿Cómo asegurarías que el total acumulado de pérdidas resalte con suficiente urgencia para motivar acciones correctivas inmediatas en el piso de planta?

### Diseño de variables
Usa nombres como `waste_tree`, `line_combo`, `lot_entry`, `reason_combo`, `qty_entry`, `unit_cost_entry`, `total_loss_display_label`, `db_waste`.

### Antes de programar
1. ¿Cómo se diseña una consulta SQL para obtener el costo acumulado de pérdidas agrupado por motivo?
2. ¿Cómo se actualiza el costo total estimado en la interfaz conforme el usuario modifica la cantidad mermada?

### Arquitectura
```
ejercicio_053/
├── app.py           # Formulario de mermas y tabla de producción
├── waste_repo.py    # Consultas SQL e inserción de pérdidas en SQLite
└── datos/
    └── mermas.db    # Base de datos de mermas industriales
```

### Pruebas mínimas
1. Registrar 100 unidades de Lote 'L-500' a $2.50 cada una -> Pérdida $250.00, debe guardarse en SQLite y sumarse al total del día.
2. Filtrar por Línea 1 -> Debe mostrar únicamente las mermas originadas en esa línea.

### Pruebas de error
1. Ingresar cantidad 0 o negativa -> Debe rechazar el registro indicando que la cantidad debe ser positiva.

### Experiencia de usuario
El cálculo del costo total del lote debe ser instantáneo mientras se teclea sin requerir presionar ningún botón intermedio.

### Explicación posterior
¿Cómo ayuda la persistencia relacional a generar reportes agregados de costos de no calidad agrupados por motivo de defecto?

### Aplicación profesional
Control de piso de planta en industrias químicas, alimentarias, metalmecánicas y maquiladoras.

### Reto adicional
Añade un gráfico textual o desglose porcentual que indique cuál de los cuatro motivos generó la mayor pérdida económica del turno.

---
> [Índice General](../README.md) · [← Ejercicio 052](../ejercicio_052/README.md) · [Ejercicio 054 →](../ejercicio_054/README.md)
