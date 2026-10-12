## Ejercicio 052 — Administración de Socios y Cuotas de Club Deportivo (`ClubMembershipSqliteApp`)

> [Índice General](../README.md) · [← Ejercicio 051](../ejercicio_051/README.md) · [Ejercicio 053 →](../ejercicio_053/README.md)

### Contexto profesional
En clubes deportivos, gimnasios y centros de acondicionamiento físico, los administradores supervisan membresías de socios y el cobro mensual o anual de cuotas de acceso.

### Usuario objetivo
Administrador de recepción o coordinador de membresías.

### Problema
La falta de alertas sobre membresías vencidas permite el acceso no autorizado de usuarios morosos a las instalaciones deportivas.

### Objetivo
Desarrollar una aplicación de gestión de membresías en SQLite (`club.db`), con tabla de socios, estados de membresía (Vigente, Por Vencer, Vencida), renovación de suscripción con un clic y transacciones contables para asegurar la integridad de los pagos registrados.

### Flujo principal
El recepcionista busca un socio por número de membresía o nombre. La tabla muestra el estatus del socio con código de colores. Al seleccionar un socio cuya membresía vence pronto o está vencida, presiona 'Renovar Membresía', selecciona el plan (Mensual, Trimestral, Anual) y confirma el pago. El sistema actualiza la fecha de vencimiento y registra la transacción en la base de datos.

### Requisitos funcionales
- Esquema SQLite con tablas `socios` y `pagos_cuotas`.
- Campos en socio: ID, Número Socio (único), Nombre Completo, Teléfono, Plan, Fecha Alta, Fecha Vencimiento, Estado.
- Detección automática del estado: 'Vigente' (verde), 'Por Vencer' (menos de 5 días, amarillo) y 'Vencida' (rojo).
- Acción 'Renovar Cuota': suma 30, 90 o 365 días a la fecha de vencimiento y crea un registro en `pagos_cuotas` de forma atómica con transacciones.
- Registro de nuevos socios mediante formulario modal o lateral.
- Historial de pagos del socio seleccionado.

### Requisitos de interfaz
- `ttk.Treeview` central amplio con tags de colores bien diferenciados.
- Botón prominente de renovación rápida de cuota.
- Panel inferior con total de socios activos y porcentaje de morosidad.

### Datos
- Socio: id, numero_socio, nombre, telefono, plan, fecha_alta, fecha_vence, estado.
- Pago: id, socio_id, fecha_pago, monto, meses_adicionados.

### Estado
- Socio seleccionado en la tabla.
- Lista de socios consultados en memoria.

### Persistencia
Base de datos relacional SQLite (`datos/club.db`).

### Validaciones
- Número de socio único y obligatorio.
- Al renovar, si la membresía ya estaba vencida, la nueva vigencia debe computarse a partir de la fecha de pago actual.

### Casos límite
- Renovar una membresía que aún tiene 15 días vigentes (los nuevos días deben sumarse a partir de la fecha de vencimiento futura).
- Socio sin ningún pago previo registrado.

### Manejo de errores
- Utilizar transacciones atómicas (`BEGIN TRANSACTION ... COMMIT`) para evitar renovar la fecha si falla la inserción del pago.

### Fundamentos de Python relacionados
- Transacciones en SQLite con context managers (`with conn: ...`).
- Aritmética de fechas con `datetime.timedelta` y funciones de calendario.

### Conceptos Tkinter relacionados
- Actualización dinámica de estados visuales según fechas calculadas en tiempo real.
- Cuadros de diálogo modales para selección de planes de renovación.

### Herramientas para investigar
- Manejo de transacciones en el módulo `sqlite3` de Python.
- Manipulación de fechas con `timedelta`.

### Diseño de interfaz
¿Cómo asegurarías que el botón 'Renovar Membresía' sea el control principal de acción para agilizar el paso por torniquete de recepción?

### Diseño de variables
Usa nombres como `members_tree`, `search_member_entry`, `renew_membership_btn`, `new_member_btn`, `active_members_label`, `db_club`.

### Antes de programar
1. ¿Qué ocurre si la membresía ya está vencida versus si aún está vigente al sumar 30 días de renovación?
2. ¿Por qué la actualización de la fecha en la tabla de socios y la inserción del recibo en la tabla de pagos deben estar dentro de la misma transacción?

### Arquitectura
```
ejercicio_052/
├── app.py             # Interfaz de recepción y tabla de socios
├── member_repo.py     # Transacciones y consultas a SQLite
├── models.py          # Entidades Socio y Pago
└── datos/
    └── club.db        # Base de datos del club deportivo
```

### Pruebas mínimas
1. Registrar socio con vencimiento hoy -> Debe marcarse como 'Por Vencer'.
2. Renovar por 1 mes (30 días) -> La fecha de vencimiento debe extenderse 30 días y crearse el registro de pago.
3. Reiniciar la app -> El estado debe reflejar 'Vigente' en verde.

### Pruebas de error
1. Intentar registrar socio con número de membresía ya existente -> Debe advertir duplicado de número de socio.

### Experiencia de usuario
El recepcionista debe poder escanear o escribir el número de socio y presionar Enter para localizarlo de inmediato.

### Explicación posterior
¿Cómo garantiza el uso de una transacción de base de datos la atomicidad al cobrar una cuota y extender la membresía simultáneamente?

### Aplicación profesional
Control de acceso y cobranza en gimnasios, clubes campestres, academias de artes marciales y centros de yoga.

### Reto adicional
Añade un botón 'Consultar Historial de Pagos' que abra una ventana secundaria con la lista de todos los recibos pagados por el socio seleccionado.

---
> [Índice General](../README.md) · [← Ejercicio 051](../ejercicio_051/README.md) · [Ejercicio 053 →](../ejercicio_053/README.md)
