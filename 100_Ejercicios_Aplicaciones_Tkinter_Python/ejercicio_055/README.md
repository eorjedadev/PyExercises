## Ejercicio 055 — Sistema de Préstamo de Herramientas de Taller Mecánico (`ToolCribSqliteApp`)

> [Índice General](../README.md) · [← Ejercicio 054](../ejercicio_054/README.md) · [Ejercicio 056 →](../ejercicio_056/README.md)

### Contexto profesional
En talleres mecánicos de aviación y mantenimiento industrial (Tool Crib), los encargados de pañol controlan el préstamo diario de herramientas especializadas a mecánicos para evitar pérdidas de equipo crítico.

### Usuario objetivo
Encargado de pañol de herramientas o supervisor de taller.

### Problema
El extravío de herramientas de alto costo y la falta de control de devoluciones en mal estado generan gastos elevados y riesgos operativos.

### Objetivo
Desarrollar una aplicación de control de pañol de herramientas con SQLite (`herramientas.db`), control de stock disponible vs prestado, registro de préstamo con asignación a mecánico y registro de devolución con dictamen de condición física (Óptima, Con Desgaste, Dañada, Perdida).

### Flujo principal
El pañolero selecciona una herramienta del catálogo y presiona 'Prestar'. Ingresa el código o nombre del mecánico y la orden de trabajo. La herramienta pasa a estatus 'En Préstamo' y su stock disponible se decrementa. Al ser devuelta, el pañolero presiona 'Devolver', selecciona la condición física y observaciones. El stock disponible se incrementa y la transacción se sella en SQLite.

### Requisitos funcionales
- Esquema SQLite con tablas `herramientas` y `prestamos`.
- Campos de herramienta: ID, Código Herramienta, Nombre, Categoría, Stock Total, Stock Disponible, Ubicación (Estante/Cajón).
- Operación de Préstamo: disminuye Stock Disponible en 1, registra mecánico, fecha/hora y crea ticket de préstamo.
- Operación de Devolución: aumenta Stock Disponible en 1 (si no está perdida), registra fecha de devolución y condición física.
- Alerta si se intenta prestar una herramienta con Stock Disponible igual a 0.
- Filtro por herramientas actualmente prestadas.

### Requisitos de interfaz
- Panel de catálogo de herramientas con visualización clara de stock disponible vs prestado.
- Diálogo o panel modal de préstamo y devolución.
- Resalte visual de herramientas agotadas o en préstamo prolongado.

### Datos
- Herramienta: id, codigo, nombre, categoria, stock_total, stock_disponible, ubicacion.
- Préstamo: id, herramienta_id, mecanico, orden_trabajo, fecha_prestamo, fecha_devolucion, condicion, notas.

### Estado
- Herramienta seleccionada en memoria.
- Estado del catálogo.

### Persistencia
Base de datos relacional SQLite (`datos/herramientas.db`).

### Validaciones
- No permitir prestar si el stock disponible es 0.
- Nombre de mecánico y orden de trabajo obligatorios al prestar.
- No permitir registrar devolución sobre un préstamo ya devuelto.

### Casos límite
- Mecánico devuelve herramienta declarándola 'Perdida' (no se debe incrementar el stock disponible y debe descontarse del stock total).
- Intento de préstamo simultáneo.

### Manejo de errores
- Emplear transacciones de base de datos para garantizar que el decremento de stock y la inserción del préstamo ocurran atómicamente.

### Fundamentos de Python relacionados
- Transacciones atómicas de actualización e inserción simultánea.
- Control de inventarios y stock de seguridad.

### Conceptos Tkinter relacionados
- Diálogos de acción con captura de parámetros condicionales.
- Formateo de celdas de stock en `Treeview`.

### Herramientas para investigar
- Transacciones con `sqlite3` para sincronizar stock e histórico.
- Flujos de pañol industrial (Tool Crib Management).

### Diseño de interfaz
¿Cómo asegurarías que el pañolero distinga al instante qué herramientas tienen unidades disponibles en estante de aquellas que están agotadas?

### Diseño de variables
Usa nombres como `tools_tree`, `borrow_btn`, `return_btn`, `mechanic_entry`, `condition_combo`, `active_loans_tree`, `db_crib`.

### Antes de programar
1. ¿Qué regla de negocio se aplica si una herramienta es devuelta en condición 'Perdida' respecto al stock total y stock disponible?
2. ¿Cómo se asegura en SQLite que el stock disponible nunca sea menor que cero usando una restricción `CHECK`?

### Arquitectura
```
ejercicio_055/
├── app.py           # Vistas de pañol y préstamos activos
├── crib_repo.py     # Transacciones de préstamo, devolución y stock en SQLite
└── datos/
    └── herramientas.db # Base de datos del taller
```

### Pruebas mínimas
1. Herramienta con Stock Disponible 1 -> Prestar a 'Mecánico Pérez' -> Stock Disponible debe pasar a 0 y registrarse el préstamo.
2. Devolver en condición 'Óptima' -> Stock Disponible debe volver a 1.
3. Reiniciar la app -> Los stocks deben persistir correctamente en SQLite.

### Pruebas de error
1. Intentar prestar una herramienta con Stock Disponible 0 -> Debe rechazar la operación indicando 'No hay unidades disponibles en bodega'.

### Experiencia de usuario
El botón 'Prestar' debe inhabilitarse automáticamente cuando la herramienta seleccionada tenga 0 unidades disponibles.

### Explicación posterior
¿Cómo garantiza el uso de restricciones de tabla (`CHECK (stock_disponible >= 0)`) en SQLite la integridad del inventario ante posibles errores de código?

### Aplicación profesional
Gestión de pañoles en talleres aeronáuticos, centros de maquinado industrial y laboratorios universitarios de electrónica.

### Reto adicional
Añade una advertencia visual para aquellas herramientas que lleven más de 24 horas en préstamo continuo sin haber sido devueltas.

---
> [Índice General](../README.md) · [← Ejercicio 054](../ejercicio_054/README.md) · [Ejercicio 056 →](../ejercicio_056/README.md)
