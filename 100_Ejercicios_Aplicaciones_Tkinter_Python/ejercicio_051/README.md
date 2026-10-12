## Ejercicio 051 — Sistema de Registro de Horas de Trabajo (`TimesheetTrackerApp`)

> [Índice General](../README.md) · [← Ejercicio 050](../ejercicio_050/README.md) · [Ejercicio 052 →](../ejercicio_052/README.md)

### Contexto profesional
En consultorías profesionales y agencias de desarrollo de software, los consultores registran diariamente las horas invertidas por proyecto para facturación a clientes.

### Usuario objetivo
Consultor de proyectos o analista de control de gestión.

### Problema
El registro tardío o impreciso de horas de trabajo en hojas de cálculo produce cobros incompletos a clientes y distorsiona el cálculo de rentabilidad de los proyectos.

### Objetivo
Desarrollar una aplicación de control de horas trabajadas con SQLite (`timesheets.db`), formulario diario con selección de proyecto y empleado, validación estricta de un máximo de 24 horas por día por empleado y consultas agregadas por semana.

### Flujo principal
El consultor selecciona el empleado y la fecha, elige el proyecto asignado e ingresa las horas laboradas junto con una breve descripción de actividades. La aplicación valida que la suma de horas registradas para ese empleado en esa fecha no exceda 24 horas. Guarda el registro en SQLite y actualiza la tabla semanal con el total acumulado.

### Requisitos funcionales
- Base de datos SQLite con tablas `empleados`, `proyectos` y `registros_horas`.
- Captura diaria: Empleado (`Combobox`), Fecha (YYYY-MM-DD), Proyecto (`Combobox`), Horas (float entre 0.5 y 24), Descripción.
- Validación en base de datos: verificar mediante consulta `SUM(horas)` que el empleado no supere 24 horas en el mismo día.
- Visualización en `ttk.Treeview`: Fecha, Proyecto, Horas, Tareas, Facturable (`Sí`/`No`).
- Panel de métricas semanales: Total de horas de la semana y porcentaje de horas facturables.

### Requisitos de interfaz
- Formulario superior ordenado para captura rápida.
- `Treeview` central con doble barra de desplazamiento.
- Resumen inferior con total de horas trabajadas en la semana activa.

### Datos
- Registro de horas: id, empleado_id, fecha, proyecto_id, horas (float), descripcion, facturable (bool).

### Estado
- Empleado y semana activos en el filtro.
- Registros consultados en memoria.

### Persistencia
Base de datos relacional SQLite (`datos/timesheets.db`).

### Validaciones
- Horas deben ser mayores a 0 y menores o iguales a 24.
- Suma diaria por empleado <= 24.0 horas.
- Fecha con formato ISO válido.

### Casos límite
- Intentar registrar horas en una fecha futura lejana.
- Registrar horas con fracciones de 15 minutos (ej. 1.25, 2.50).

### Manejo de errores
- Notificar con claridad si el nuevo registro haría que el colaborador exceda el límite diario de 24 horas.

### Fundamentos de Python relacionados
- Consultas SQL con funciones de agregación (`SUM`, `COUNT`, `GROUP BY`).
- Manejo de fechas y semanas del año con `datetime.isocalendar()`.

### Conceptos Tkinter relacionados
- Manejo de fechas y sincronización entre base de datos y vistas de Tkinter.
- Formularios de entrada rápida con selección enlazada.

### Herramientas para investigar
- Consultas agregadas con `SUM()` en SQL.
- Método `isocalendar()` del módulo `datetime`.

### Diseño de interfaz
¿Cómo asegurarías que el total de horas de la semana resalte claramente para que el consultor sepa si ya cumplió su meta de 40 horas semanales?

### Diseño de variables
Usa nombres como `timesheet_tree`, `employee_combo`, `project_combo`, `hours_entry`, `date_entry`, `desc_entry`, `weekly_hours_label`.

### Antes de programar
1. ¿Cómo se diseña la consulta SQL para sumar las horas que un empleado ya tiene registradas en una fecha dada antes de permitir un nuevo insert?
2. ¿Por qué es vital usar `GROUP BY` para obtener el total de horas por proyecto en la semana?

### Arquitectura
```
ejercicio_051/
├── app.py             # Formulario de horas y tabla de la semana
├── timesheet_repo.py  # Consultas SQL a SQLite y validaciones de tope de horas
└── datos/
    └── timesheets.db  # Base de datos relacional SQLite
```

### Pruebas mínimas
1. Registrar 8 horas el 2026-04-10 para Proyecto Alfa -> Debe guardarse y mostrarse en la tabla.
2. Registrar 6 horas más el mismo día para Proyecto Beta -> Total diario debe ser 14 horas y permitirse.

### Pruebas de error
1. Intentar registrar 12 horas más el mismo día (suma = 26 horas) -> Debe rechazar el registro indicando que excede las 24 horas diarias permitidas.

### Experiencia de usuario
La fecha debe prellenarse automáticamente con la fecha de hoy para agilizar la captura diaria.

### Explicación posterior
¿Cómo se coordina una validación previa mediante consulta de agregación en base de datos antes de ejecutar una inserción de registro?

### Aplicación profesional
Sistemas de timesheet en consultoras globales (Big 4), agencias de publicidad y software de gestión de despachos legales.

### Reto adicional
Añade un selector de semana anterior/semana siguiente que refresque la tabla y los totales acumulados al cambiar de semana.

---
> [Índice General](../README.md) · [← Ejercicio 050](../ejercicio_050/README.md) · [Ejercicio 052 →](../ejercicio_052/README.md)
