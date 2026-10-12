## Ejercicio 058 — Registro de Donaciones y Padrinos en ONG (`DonationsTrackerApp`)

> [Índice General](../README.md) · [← Ejercicio 057](../ejercicio_057/README.md) · [Ejercicio 059 →](../ejercicio_059/README.md)

### Contexto profesional
En organizaciones no gubernamentales (ONG) y fundaciones benéficas, los coordinadores de procuración de fondos gestionan aportes de donantes recurrentes y esporádicos.

### Usuario objetivo
Coordinador de procuración de fondos o asistente administrativo de la ONG.

### Problema
La falta de registro ordenado de donantes y sus aportes dificulta la emisión de recibos deducibles y el seguimiento a padrinos de programas benéficos.

### Objetivo
Construir una aplicación de recaudación de fondos con SQLite (`donaciones.db`), tablas relacionales de Donantes y Aportes, cálculo de donaciones acumuladas por persona, emisión de recibos digitales en formato texto y consulta de metas de recaudación de campañas.

### Flujo principal
El usuario registra a un donante con sus datos de contacto y tipo (Individual, Empresa). Cuando se recibe un aporte, lo registra vinculándolo al donante, indicando monto, fecha, campaña y método de pago. La aplicación almacena el aporte en SQLite y permite generar con un clic un recibo formal en texto con folio único listo para enviar al donante.

### Requisitos funcionales
- Esquema SQLite con tablas `donantes` y `aportes` relacionadas por clave foránea.
- Registro y edición de donantes (Nombre, RFC/Identificación, Teléfono, Correo, Tipo).
- Registro de aportes: Donante (`Combobox`), Fecha, Monto, Campaña (`Educación`, `Salud`, `Nutrición`), Método de Pago.
- Visualización en `ttk.Treeview` de los aportes recibidos con datos del donante obtenidos mediante consulta `JOIN`.
- Generación de 'Recibo de Aporte' en archivo de texto plano con folio, fecha, monto en letra/número y datos de la fundación.
- Panel con el total recaudado por campaña y porcentaje de avance respecto a la meta institucional.

### Requisitos de interfaz
- Formulario para registro de aportes.
- `Treeview` de transacciones amplio y bien formateado.
- Botón 'Emitir Recibo de Aporte' que abra una previsualización o guarde el archivo de texto.

### Datos
- Donante: id, nombre, rfc, correo, tipo.
- Aporte: id, donante_id, folio, fecha, monto, campana, metodo.

### Estado
- Donante seleccionado en memoria.
- Lista de aportes consultados.

### Persistencia
Base de datos relacional SQLite (`datos/donaciones.db`).

### Validaciones
- Monto de donación estrictamente mayor a 0.0.
- Donante seleccionado obligatorio.
- Fechas con formato ISO válido.

### Casos límite
- Donante anónimo (debe existir un registro genérico 'Donante Anónimo' en la base de datos).
- Registro de múltiples donaciones del mismo donante el mismo día.

### Manejo de errores
- Emplear transacciones de base de datos para la generación del folio y el guardado del aporte.

### Fundamentos de Python relacionados
- Consultas SQL con `INNER JOIN` para unir donantes y aportes.
- Formateo de recibos de texto con alineación y números.

### Conceptos Tkinter relacionados
- Diálogos de selección de archivos para guardar el recibo emitido (`filedialog.asksaveasfilename`).
- Integración con base de datos relacional.

### Herramientas para investigar
- Consultas relacionales `JOIN` en SQLite.
- Generación de plantillas de recibos en texto plano.

### Diseño de interfaz
¿Cómo asegurarías que el botón de emisión de recibo sea claramente accesible al seleccionar un aporte de la tabla?

### Diseño de variables
Usa nombres como `donations_tree`, `donor_combo`, `amount_entry`, `campaign_combo`, `generate_receipt_btn`, `campaign_total_label`, `db_donations`.

### Antes de programar
1. ¿Cómo se construye la consulta `JOIN` para obtener el nombre del donante junto con cada registro de aporte?
2. ¿Cómo se genera un texto formateado de recibo listo para guardar en disco?

### Arquitectura
```
ejercicio_058/
├── app.py             # Registro de aportes y tabla de recaudación
├── donation_repo.py   # Consultas JOIN y persistencia en SQLite
├── receipt_maker.py   # Generador de recibos de texto plano
└── datos/
    └── donaciones.db  # Base de datos de la organización benéfica
```

### Pruebas mínimas
1. Registrar donante 'Fundación Azteca' y aportar $5,000 a 'Educación' -> Comprobar que aparezca en la tabla uniendo el nombre.
2. Presionar 'Emitir Recibo' -> Comprobar que genere el archivo `.txt` con los datos del aporte.

### Pruebas de error
1. Intentar registrar donación sin seleccionar donante -> Debe advertir que el donante es obligatorio.

### Experiencia de usuario
El total recaudado debe actualizarse en cuanto se registre un nuevo aporte sin requerir recargar la pantalla.

### Explicación posterior
¿Cómo optimiza una consulta con `JOIN` la recuperación de datos relacionales frente a realizar múltiples consultas independientes?

### Aplicación profesional
Sistemas de CRM para organizaciones benéficas, gestión de patronatos universitarios y recaudación de fondos comunitarios.

### Reto adicional
Añade un filtro por campaña en el Treeview que recalcule el total de recaudación de esa causa específica.

---
> [Índice General](../README.md) · [← Ejercicio 057](../ejercicio_057/README.md) · [Ejercicio 059 →](../ejercicio_059/README.md)
