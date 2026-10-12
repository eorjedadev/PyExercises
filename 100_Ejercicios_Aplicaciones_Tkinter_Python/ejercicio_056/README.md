## Ejercicio 056 — Gestor de Órdenes de Trabajo para Servicios Técnicos (`ServiceWorkOrdersApp`)

> [Índice General](../README.md) · [← Ejercicio 055](../ejercicio_055/README.md) · [Ejercicio 057 →](../ejercicio_057/README.md)

### Contexto profesional
En talleres de servicio técnico de electrónica y línea blanca, los recepcionistas e ingenieros coordinan el flujo de reparación de equipos de clientes desde la recepción hasta la entrega.

### Usuario objetivo
Técnico de reparación o recepcionista de taller.

### Problema
El seguimiento de órdenes en papeles sueltos provoca equipos olvidados, piezas pedidas sin presupuesto aprobado y falta de trazabilidad con el cliente.

### Objetivo
Construir un gestor de órdenes de trabajo con base de datos SQLite (`ordenes_servicio.db`), implementando una máquina de estados estricta (Recibido -> En Diagnóstico -> Presupuestado -> Aprobado -> En Reparación -> Terminado -> Entregado), con registro de costo de refacciones y mano de obra.

### Flujo principal
El usuario registra un equipo recibido (Cliente, Equipo, Falla reportada). La orden inicia en 'Recibido'. Conforme el técnico trabaja, avanza el estado mediante un botón de transición controlada. Al pasar a 'Presupuestado', ingresa los montos de refacciones y mano de obra. Una vez 'Terminado', el cliente recoge el equipo y la orden pasa a 'Entregado'.

### Requisitos funcionales
- Esquema SQLite con tabla `ordenes_trabajo`.
- Campos: Folio (OT-XXXX), Cliente, Teléfono, Dispositivo, Falla Reportada, Estado, Diagnóstico Técnico, Costo Refacciones, Mano de Obra, Total, Fecha Ingreso, Fecha Entrega.
- Máquina de estados con transiciones válidas controladas por código.
- Formulario para actualizar diagnóstico y cotización económica.
- Visualización en `ttk.Treeview` con filtrado por estado activo.
- Cálculo automático del total a pagar (Refacciones + Mano de Obra).

### Requisitos de interfaz
- Formulario estructurado para datos del equipo y del cliente.
- `Treeview` de órdenes con tags cromáticos por estado.
- Barra de herramientas con botones de transición de estado contextuales.

### Datos
- Orden de trabajo: folio, cliente, telefono, dispositivo, falla, estado, diagnostico, refacciones, mano_obra, total, fecha_ingreso, fecha_entrega.

### Estado
- Orden seleccionada en la tabla.
- Estado actual de la orden.

### Persistencia
Base de datos relacional SQLite (`datos/ordenes_servicio.db`).

### Validaciones
- No permitir transicionar a 'En Reparación' si el estado actual no fue previamente 'Aprobado'.
- No permitir transicionar a 'Presupuestado' sin ingresar montos numéricos válidos.

### Casos límite
- Cliente rechaza el presupuesto (transición directa a 'Cancelado / Devuelto sin Reparar').
- Orden completada sin costo de refacciones (solo mano de obra).

### Manejo de errores
- Validar transiciones ilegales de estado mostrando mensaje de flujo no permitido.

### Fundamentos de Python relacionados
- Modelado de máquinas de estado finito (FSM) con diccionarios de transiciones permitidas.
- Actualizaciones atómicas en SQLite.

### Conceptos Tkinter relacionados
- Habilitación de botones de acción según el estado actual del ítem seleccionado.
- Actualización selectiva de columnas en el `Treeview`.

### Herramientas para investigar
- Patrón State Machine en Python.
- Métodos de actualización condicional en `sqlite3`.

### Diseño de interfaz
¿Cómo estructurarías los botones de avance de estado para que el técnico no pueda presionar una transición no autorizada por el flujo?

### Diseño de variables
Usa nombres como `orders_tree`, `filter_status_combo`, `advance_state_btn`, `parts_cost_entry`, `labor_cost_entry`, `current_state_label`, `db_service`.

### Antes de programar
1. ¿Cómo se define formalmente un diccionario de transiciones válidas para que `'Recibido'` solo pueda transicionar a `'En Diagnóstico'` o `'Cancelado'`?
2. ¿Cómo se actualizan los campos de costos y diagnóstico en la base de datos sin sobreescribir la fecha de ingreso original?

### Arquitectura
```
ejercicio_056/
├── app.py             # Interfaz de taller y tabla de órdenes
├── state_machine.py   # Lógica de estados y transiciones permitidas
├── order_repo.py      # Persistencia de órdenes en SQLite
└── datos/
    └── ordenes_servicio.db # Base de datos de servicios técnicos
```

### Pruebas mínimas
1. Crear orden 'Recibido' -> Avanzar a 'En Diagnóstico' -> Comprobar que el estado se actualice en la tabla y en SQLite.
2. Presupuestar $500 refacciones y $300 mano de obra -> Total debe ser $800 y estado 'Presupuestado'.

### Pruebas de error
1. Intentar pasar una orden de 'Recibido' directamente a 'Terminado' -> Debe rechazar la transición por violar el flujo de trabajo.

### Experiencia de usuario
El botón de avance debe mostrar el nombre del siguiente estado lógico (ej. 'Enviar a Diagnóstico', 'Aprobar Presupuesto') para guiar al usuario.

### Explicación posterior
¿Por qué es crucial implementar una máquina de estados formal en lugar de permitir que el usuario elija cualquier estado arbitrariamente en un desplegable?

### Aplicación profesional
Sistemas de servicio técnico en talleres mecánicos, centros autorizados de telefonía móvil y servicio postventa.

### Reto adicional
Añade un botón que genere una 'Orden de Recepción' imprimible en archivo de texto plano con los datos del equipo y firma de conformidad.

---
> [Índice General](../README.md) · [← Ejercicio 055](../ejercicio_055/README.md) · [Ejercicio 057 →](../ejercicio_057/README.md)
