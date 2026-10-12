## Ejercicio 060 — Gestor de Suscripciones y Pagos Periódicos (`SubscriptionVaultApp`)

> [Índice General](../README.md) · [← Ejercicio 059](../ejercicio_059/README.md) · [Ejercicio 061 →](../ejercicio_061/README.md)

### Contexto profesional
En áreas de finanzas operativas de empresas y pequeños negocios, los administradores supervisan contratos de suscripción de software (SaaS), licencias en la nube y servicios recurrentes.

### Usuario objetivo
Administrador financiero o encargado de operaciones.

### Problema
La renovación automática imprevista de suscripciones que ya no se utilizan genera fugas de capital mensuales y anuales no presupuestadas.

### Objetivo
Construir un gestor integral de suscripciones con SQLite (`suscripciones.db`), cálculo automático de la próxima fecha de renovación según ciclo (Mensual, Trimestral, Anual), cálculo del costo anual proyectado, exportación e importación masiva de datos en CSV y alertas de renovación próxima.

### Flujo principal
El usuario gestiona sus servicios contratados (Servicio, Proveedor, Costo, Frecuencia, Fecha de Inicio, Método de Pago, Estado: Activo/Cancelado). La aplicación calcula automáticamente la próxima fecha de cobro y el gasto anualizado de cada servicio. El usuario puede exportar todo el catálogo a CSV para reportes o importar un lote de suscripciones desde un archivo CSV externo.

### Requisitos funcionales
- Esquema SQLite con tabla `suscripciones`.
- Campos: ID, Servicio, Proveedor, Costo (float), Moneda, Ciclo (`Mensual`, `Trimestral`, `Anual`), Fecha Inicio, Proxima Renovacion, Estado (`Activo`, `Pausado`, `Cancelado`).
- Cálculo automático de la próxima fecha de renovación a partir de la fecha de inicio y el ciclo contratado.
- Cálculo del Costo Anual Proyectado por servicio y total consolidado de la empresa.
- Importación masiva desde archivo CSV (`filedialog.askopenfilename`) con inserción en la base de datos.
- Exportación del catálogo a CSV (`filedialog.asksaveasfilename`).
- Alerta visual en color amarillo/rojo para aquellas suscripciones cuya renovación ocurrirá en los próximos 7 días.

### Requisitos de interfaz
- Barra superior con botones de acción rápida (Nueva Suscripción, Importar CSV, Exportar CSV).
- `Treeview` central con scrollbars y columnas formateadas.
- Panel inferior destacado con tarjetas para: Gasto Mensual Promedio y Gasto Anual Proyectado.

### Datos
- Suscripción: id, servicio, proveedor, costo, moneda, ciclo, fecha_inicio, prox_renovacion, estado, costo_anual.

### Estado
- Lista de suscripciones cargadas.
- Totales anuales proyectados.

### Persistencia
Base de datos relacional SQLite (`datos/suscripciones.db`) con soporte de intercambio en CSV.

### Validaciones
- Costo estrictamente mayor a 0.0.
- Nombre de servicio y proveedor obligatorios.
- Formato de archivo CSV compatible al importar.

### Casos límite
- Archivo CSV de importación con encabezados incorrectos o filas vacías.
- Suscripción con fecha de inicio en año bisiesto (29 de febrero).

### Manejo de errores
- Manejar excepciones de parseo de CSV durante la importación reportando cuántas filas fueron importadas con éxito y cuántas fallaron.

### Fundamentos de Python relacionados
- Módulo `csv` integrado con el módulo `sqlite3`.
- Cálculos de fechas cíclicas y normalización anual de costos (ej. mensual $\times 12$, trimestral $\times 4$).

### Conceptos Tkinter relacionados
- Diálogos de archivo para importación y exportación de datos.
- Confirmaciones modales y actualización masiva de tablas.

### Herramientas para investigar
- Cálculos de recurrencia de fechas con `datetime` y `dateutil.relativedelta` o lógica manual.
- Manejo de CSV y SQLite combinados.

### Diseño de interfaz
¿Cómo asegurarías que el botón de importación CSV comunique claramente el formato esperado de archivo para evitar errores del usuario?

### Diseño de variables
Usa nombres como `sub_tree`, `import_csv_btn`, `export_csv_btn`, `annual_spend_label`, `monthly_spend_label`, `db_subs`.

### Antes de programar
1. ¿Cómo se calcula la próxima fecha de renovación si una suscripción mensual inició el 15 de enero y hoy es 20 de marzo?
2. ¿Cómo se ejecuta una importación masiva de CSV a SQLite dentro de una sola transacción para maximizar la velocidad y seguridad?

### Arquitectura
```
ejercicio_060/
├── app.py             # Gestor de suscripciones, métricas y tabla
├── sub_repo.py        # Consultas y persistencia en SQLite
├── csv_io.py          # Lógica de importación y exportación de archivos CSV
└── datos/
    └── suscripciones.db # Base de datos de servicios contratados
```

### Pruebas mínimas
1. Registrar servicio de $10/mes -> El costo anual proyectado debe ser $120.00 y calcular su próxima fecha de cobro.
2. Exportar a CSV -> Comprobar que el archivo resultante contenga todas las suscripciones de la base de datos.

### Pruebas de error
1. Intentar importar un archivo CSV corrupto o con columnas faltantes -> Debe capturar el error y no romper la base de datos.

### Experiencia de usuario
Las suscripciones que vencen en menos de una semana deben resaltarse con un tag de color llamativo para permitir cancelar a tiempo si no se desea renovar.

### Explicación posterior
¿Cómo se coordina el patrón de intercambio de datos (CSV) con una base de datos relacional estructurada (SQLite) garantizando atomicidad?

### Aplicación profesional
Gestores de SaaS en departamentos de TI corporativos, control de suscripciones personales y auditorías de gastos recurrentes.

### Reto adicional
Añade un botón 'Cancelar Suscripción' que cambie el estado a 'Cancelado' y lo descuente inmediatamente del gasto anual proyectado.

---
> [Índice General](../README.md) · [← Ejercicio 059](../ejercicio_059/README.md) · [Ejercicio 061 →](../ejercicio_061/README.md)
