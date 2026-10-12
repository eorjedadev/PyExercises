## Ejercicio 050 — Control de Cuentas por Cobrar y Facturas Pendientes (`InvoicingSqliteApp`)

> [Índice General](../README.md) · [← Ejercicio 049](../ejercicio_049/README.md) · [Ejercicio 051 →](../ejercicio_051/README.md)

### Contexto profesional
En despachos contables y áreas de tesorería empresarial, los ejecutivos supervisan facturas emitidas a clientes, controlando fechas de vencimiento y saldos pendientes.

### Usuario objetivo
Analista de cobranza o contador de cuentas por cobrar.

### Problema
El seguimiento de facturas vencidas en hojas de cálculo produce cobros tardíos, descontrol de abonos parciales y falta de cálculo automático de moras.

### Objetivo
Construir una aplicación de gestión de cuentas por cobrar con base de datos SQLite relacional (`cobranza.db`), con tablas relacionadas de Clientes y Facturas, registro de abonos parciales, filtros por estado (Pagada, Pendiente, Vencida) y cálculo dinámico de cartera vencida.

### Flujo principal
El usuario visualiza las facturas en el `Treeview`. Puede registrar una nueva factura asignada a un cliente. Si la fecha de vencimiento ya pasó y el saldo es mayor a cero, la factura se marca automáticamente como 'Vencida' (rojo). Al seleccionar una factura, puede pulsar 'Registrar Pago/Abono' para ingresar un monto parcial o total, actualizando el saldo y el estado en la base de datos.

### Requisitos funcionales
- Esquema SQLite relacional con tablas `clientes` y `facturas` vinculadas por clave foránea (`FOREIGN KEY (cliente_id) REFERENCES clientes(id)`).
- Campos en factura: ID, Folio Factura, Cliente, Fecha Emisión, Fecha Vencimiento, Monto Total, Saldo Pendiente, Estado ('Pendiente', 'Pagada', 'Vencida').
- Registro de abonos parciales: descuenta del saldo pendiente y si llega a 0, transiciona a 'Pagada'.
- Detección automática de facturas vencidas comparando la fecha de vencimiento con la fecha actual del sistema.
- Filtros por estado: Todas, Solo Pendientes, Solo Vencidas, Solo Pagadas.
- Panel de métricas: Total Cartera por Cobrar ($) y Total Cartera Vencida ($).

### Requisitos de interfaz
- Formulario superior de emisión y abono.
- `ttk.Treeview` amplio con formateo de moneda y tags cromáticos por estado.
- Tarjetas de resumen financiero en la parte superior o inferior.

### Datos
- Cliente: id, razon_social, rfc, telefono.
- Factura: id, folio, cliente_id, fecha_emision, fecha_vence, total, saldo, estado.

### Estado
- Filtro activo en memoria.
- Factura seleccionada.

### Persistencia
Base de datos relacional SQLite (`datos/cobranza.db`).

### Validaciones
- El abono ingresado no puede ser mayor al saldo pendiente de la factura.
- Monto total de factura estrictamente mayor a cero.
- Fechas en formato ISO válido.

### Casos límite
- Intentar registrar un abono sobre una factura ya pagada (saldo 0).
- Abono exactamente igual al saldo restante (debe cambiar estado a 'Pagada').

### Manejo de errores
- Manejar transacciones con `try/except` y `conn.commit()` / `conn.rollback()` para garantizar integridad contable.

### Fundamentos de Python relacionados
- Relaciones relacionales entre tablas y consultas SQL con `JOIN`.
- Comparación de fechas de vencimiento con `datetime.date.today()`.
- Transacciones atómicas en SQLite.

### Conceptos Tkinter relacionados
- Diálogos para captura de montos con validación.
- Sincronización entre consultas SQL complejas y la tabla gráfica.

### Herramientas para investigar
- Cláusulas `JOIN` en consultas SQL de SQLite.
- Integridad referencial (`PRAGMA foreign_keys = ON;`).

### Diseño de interfaz
¿Cómo dispondrías las tarjetas de 'Total Cartera por Cobrar' y 'Total Cartera Vencida' para que el equipo financiero las consulte de forma prioritaria?

### Diseño de variables
Usa nombres como `invoice_tree`, `filter_status_combo`, `payment_btn`, `total_ar_label`, `overdue_total_label`, `db_service`.

### Antes de programar
1. ¿Por qué es importante ejecutar `PRAGMA foreign_keys = ON;` en SQLite para habilitar la integridad referencial de claves foráneas?
2. ¿Cómo se calculan las facturas vencidas dinámicamente comparando `fecha_vencimiento < CURRENT_DATE` en una consulta SQL?

### Arquitectura
```
ejercicio_050/
├── app.py             # Interfaz de cuentas por cobrar y métricas
├── invoice_repo.py    # Repositorio SQLite con consultas JOIN y transacciones
├── models.py          # Entidades Cliente y Factura
└── datos/
    └── cobranza.db    # Base de datos relacional SQLite
```

### Pruebas mínimas
1. Registrar factura de $1000 pendiente -> Registrar abono de $400 -> Comprobar que el saldo baje a $600 en SQLite y en la tabla.
2. Abonar los $600 restantes -> Verificar que el saldo pase a $0 y el estado a 'Pagada'.

### Pruebas de error
1. Intentar registrar un abono de $800 sobre un saldo de $600 -> Debe rechazar el pago por exceder el saldo adeudado.

### Experiencia de usuario
Las facturas vencidas deben verse en rojo inmediato para advertir al cobrador sin requerir cálculos mentales.

### Explicación posterior
¿Cómo garantiza el uso de transacciones con `commit()` y `rollback()` que no se registren abonos corruptos si ocurre un fallo a medio proceso?

### Aplicación profesional
Módulos de cuentas por cobrar en ERPs comerciales, sistemas de cobranza de servicios y facturación corporativa.

### Reto adicional
Añade un botón 'Calcular Intereses Moratorios' que aplique un 2% de recargo mensual sobre el saldo de aquellas facturas vencidas con más de 30 días de mora.

---
> [Índice General](../README.md) · [← Ejercicio 049](../ejercicio_049/README.md) · [Ejercicio 051 →](../ejercicio_051/README.md)
