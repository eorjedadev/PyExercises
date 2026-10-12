## Ejercicio 033 — Registro de Activos de TI y Asignación de Equipos (`AssetTrackerApp`)

> [Índice General](../README.md) · [← Ejercicio 032](../ejercicio_032/README.md) · [Ejercicio 034 →](../ejercicio_034/README.md)

### Contexto profesional
En departamentos corporativos de soporte y logística de TI, los administradores de activos deben registrar qué laptop, monitor o periférico está asignado a cada colaborador.

### Usuario objetivo
Administrador de activos de TI o analista de compras.

### Problema
La falta de registro de números de serie y marcas de los equipos asignados genera pérdidas materiales durante las bajas de personal.

### Objetivo
Construir una aplicación para gestionar el inventario de activos de TI con `ttk.Treeview`, persistencia en CSV, validación de números de serie únicos y exportación de cartas de asignación de equipos.

### Flujo principal
El analista registra un nuevo activo (Número de Serie, Tipo de Dispositivo, Marca, Modelo, Empleado Asignado, Fecha de Entrega). La aplicación valida que el número de serie no esté duplicado y lo guarda en `activos_ti.csv`. Puede filtrar por empleado para ver todos los equipos que tiene a su cargo y generar un resumen.

### Requisitos funcionales
- Carga y guardado en `activos_ti.csv`.
- Columnas: Serie, Dispositivo (`Laptop`, `Monitor`, `Teléfono`, `Periférico`), Marca, Modelo, Asignado A, Fecha Asignación, Estatus (`Asignado`, `En Bodega`, `En Reparación`).
- Validación estricta de número de serie único.
- Búsqueda por empleado o por número de serie.
- Botón para reasignar o devolver equipo a bodega.
- Exportación del listado filtrado a un archivo CSV nuevo.

### Requisitos de interfaz
- Formulario organizado en cuadrícula superior con `Combobox` para tipo y estatus.
- `ttk.Treeview` central con doble barra de desplazamiento.
- Barra de estado inferior con total de activos y cantidad de equipos en bodega.

### Datos
- Ficha de activo: serie, tipo, marca, modelo, asignado_a, fecha, estatus.

### Estado
- Lista de activos en memoria.
- Activo seleccionado en el Treeview.

### Persistencia
Archivo CSV (`datos/activos_ti.csv`).

### Validaciones
- Número de serie obligatorio, sin espacios y único en todo el catálogo.
- Marca y modelo obligatorios.
- Si el estatus es 'Asignado', el nombre del empleado es obligatorio.

### Casos límite
- Intentar poner estatus 'En Bodega' pero dejar un empleado asignado (debe limpiarse automáticamente o advertirse).
- Seriales con caracteres especiales.

### Manejo de errores
- Notificar con diálogo si el número de serie ya está en uso por otro activo.

### Fundamentos de Python relacionados
- Manejo de CSV con `csv.DictReader` y `csv.DictWriter`.
- Validación de unicidad y normalización de mayúsculas en identificadores.

### Conceptos Tkinter relacionados
- Comportamiento condicional de campos de entrada según el estatus seleccionado en un `Combobox`.
- Operaciones de actualización de celdas en `Treeview`.

### Herramientas para investigar
- Módulo `csv` de Python.
- Manejo de colecciones y diccionarios para búsqueda rápida por clave única.

### Diseño de interfaz
¿Cómo asegurarías que el campo 'Empleado Asignado' se deshabilite automáticamente si el estatus se cambia a 'En Bodega'?

### Diseño de variables
Usa nombres como `asset_tree`, `serial_entry`, `device_type_combo`, `brand_entry`, `model_entry`, `assignee_entry`, `status_combo`.

### Antes de programar
1. ¿Cómo se sincroniza la obligatoriedad del campo de empleado cuando cambia el valor de un `Combobox` de estatus?
2. ¿Por qué el número de serie debe normalizarse a mayúsculas antes de verificar unicidad?

### Arquitectura
```
ejercicio_033/
├── app.py           # Formulario y visualización de inventario
├── asset_service.py # Validaciones de negocio y unicidad de series
└── datos/
    └── activos_ti.csv # Persistencia de activos
```

### Pruebas mínimas
1. Registrar laptop con serie 'SN-9988' asignada a 'Ana Gómez' -> Verificar que se agregue a la tabla y al archivo CSV.
2. Filtrar por 'Ana Gómez' -> Verificar que solo se muestren los equipos de esa persona.

### Pruebas de error
1. Intentar registrar otro activo con la misma serie 'SN-9988' -> Debe rechazar el registro por duplicidad.

### Experiencia de usuario
Al seleccionar una fila de la tabla, los datos deben cargarse en el formulario superior para permitir una reasignación rápida.

### Explicación posterior
¿Cómo garantiza la verificación previa en memoria contra un conjunto de seriales que no se creen registros duplicados en el CSV?

### Aplicación profesional
Sistemas ITAM (IT Asset Management) en empresas medianas y grandes, gestión de garantías y almacén de sistemas.

### Reto adicional
Añade un botón que genere un archivo de texto con el formato de 'Acta de Entrega de Equipo' con fecha y líneas de firma para el empleado.

---
> [Índice General](../README.md) · [← Ejercicio 032](../ejercicio_032/README.md) · [Ejercicio 034 →](../ejercicio_034/README.md)
