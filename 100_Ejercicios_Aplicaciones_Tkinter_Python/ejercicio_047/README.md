## Ejercicio 047 — Explorador de Esquema de Datos y Diccionario de Campos (`DataDictionaryApp`)

> [Índice General](../README.md) · [← Ejercicio 046](../ejercicio_046/README.md) · [Ejercicio 048 →](../ejercicio_048/README.md)

### Contexto profesional
En áreas de arquitectura de datos y gobierno de TI, los ingenieros documentan metadatos, descripciones comerciales y restricciones técnicas de tablas de bases de datos.

### Usuario objetivo
Arquitecto de datos, administrador de bases de datos (DBA) o analista de BI.

### Problema
La falta de un diccionario de datos accesible obliga a los analistas a consultar esquemas en consolas complejas de base de datos para saber qué significa cada columna.

### Objetivo
Construir un visor de diccionario de datos con dos paneles (Lista de tablas a la izquierda y `Treeview` de campos con tipos, nulabilidad y descripciones a la derecha), con barra de menú y ventana secundaria para consultar métricas del esquema.

### Flujo principal
El analista carga un esquema estructurado en JSON. En el panel izquierdo selecciona una tabla (ej. `clientes`, `facturas`). En el panel derecho se despliegan automáticamente todos sus atributos (Nombre de Columna, Tipo de Dato, Clave Primaria, Permite Nulos, Descripción Comercial). En el menú 'Herramientas > Estadísticas', abre una ventana modal con el resumen del esquema.

### Requisitos funcionales
- Carga de esquema de base de datos desde `datos/schema_metadata.json`.
- Panel izquierdo: `Listbox` con las tablas del modelo de datos.
- Panel derecho: `ttk.Treeview` con columnas: Columna, Tipo de Dato, PK (`Sí`/`No`), Nulo (`Sí`/`No`), Descripción.
- Filtro para buscar columnas por nombre a través de todas las tablas.
- Menú principal con opciones: 'Archivo' (Abrir Esquema, Salir), 'Herramientas' (Estadísticas del Esquema, Exportar a CSV).
- Ventana secundaria con estadísticas: total de tablas, total de columnas y conteo de tipos de datos.

### Requisitos de interfaz
- Disposición de paneles en dos columnas (maestro-detalle).
- Treeview ordenado y formateado con alineación adecuada.
- Ventana secundaria de estadísticas modal y limpia.

### Datos
- Diccionario de datos: tablas con listas de atributos y metadatos asociados.

### Estado
- Tabla actualmente seleccionada en el Listbox.
- Esquema completo cargado en memoria.

### Persistencia
Lectura desde JSON (`datos/schema_metadata.json`).

### Validaciones
- Verificar que el archivo JSON cumpla con el esquema requerido de tablas y atributos.

### Casos límite
- Tablas sin columnas registradas.
- Búsqueda de una columna inexistente.

### Manejo de errores
- Manejar archivos JSON con estructura incompatible notificando el error.

### Fundamentos de Python relacionados
- Recorrido de estructuras JSON complejas y diccionarios anidados.
- Funciones de agregación para calcular estadísticas de columnas por tipo.

### Conceptos Tkinter relacionados
- Patrón maestro-detalle dividiendo la ventana en dos paneles coordinados.
- Enlace del evento `<<ListboxSelect>>` para actualizar el Treeview adyacente.

### Herramientas para investigar
- Evento virtual `<<ListboxSelect>>` en `tkinter.Listbox`.
- Diseño de interfaces maestro-detalle.

### Diseño de interfaz
¿Cómo asegurarías que el panel de tablas izquierdo mantenga un ancho adecuado y el panel de columnas derecho se expanda al maximizar la ventana?

### Diseño de variables
Usa nombres como `tables_listbox`, `fields_tree`, `search_col_entry`, `schema_menu`, `stats_window`, `stats_summary_label`.

### Antes de programar
1. ¿Cómo se conecta la selección en un `Listbox` para que actualice automáticamente el contenido de un `Treeview`?
2. ¿Cómo se obtiene la tabla seleccionada en el callback de `<<ListboxSelect>>`?

### Arquitectura
```
ejercicio_047/
├── app.py             # Interfaz maestro-detalle y menú
├── stats_dialog.py    # Ventana secundaria de métricas de esquema
├── schema_service.py  # Carga y análisis del esquema de datos
└── datos/
    └── schema_metadata.json # Archivo con el esquema documentado
```

### Pruebas mínimas
1. Seleccionar la tabla 'facturas' -> El Treeview debe poblarse inmediatamente con los atributos de esa tabla.
2. Abrir 'Estadísticas' en el menú -> Debe mostrar el total de tablas y columnas del esquema.

### Pruebas de error
1. Hacer clic en una zona vacía del Listbox -> No debe provocar excepciones de índice fuera de rango.

### Experiencia de usuario
La navegación entre tablas debe ser instantánea y el Treeview debe limpiarse y repoblarse sin parpadeos.

### Explicación posterior
¿Cómo se implementa de forma robusta el patrón maestro-detalle coordinando eventos entre distintos tipos de widgets de selección?

### Aplicación profesional
Catálogos de metadatos en almacenes de datos (Data Warehouses), herramientas de gobierno de datos y suites de arquitectura de software.

### Reto adicional
Añade un campo de búsqueda en la parte superior que filtre en tiempo real el listado de tablas disponibles.

---
> [Índice General](../README.md) · [← Ejercicio 046](../ejercicio_046/README.md) · [Ejercicio 048 →](../ejercicio_048/README.md)
