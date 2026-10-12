## Ejercicio 026 — Catálogo de Inventario en Bodega (`WarehouseInventoryApp`)

> [Índice General](../README.md) · [← Ejercicio 025](../ejercicio_025/README.md) · [Ejercicio 027 →](../ejercicio_027/README.md)

### Contexto profesional
En centros de distribución y almacenes logísticos, los jefes de bodega necesitan supervisar las existencias de mercancía en tablas con columnas claras, registrando entradas y salidas con persistencia en CSV.

### Usuario objetivo
Jefe de almacén o supervisor de inventarios.

### Problema
El control de existencias en libretas manuales provoca descuadres de inventario, productos duplicados y ventas de ítems sin stock disponible.

### Objetivo
Desarrollar una aplicación de escritorio con `ttk.Treeview` que liste productos (SKU, Nombre, Categoría, Stock, Precio Unitario), permita agregar nuevos ítems mediante formulario, editar existencias y persistir los cambios en un archivo `inventario.csv`.

### Flujo principal
El usuario visualiza la tabla con los productos existentes cargados desde el archivo CSV. Puede llenar el formulario superior para añadir un producto, hacer doble clic en una fila para modificar su stock, seleccionar una fila y pulsar 'Eliminar' (con confirmación), o hacer clic en 'Guardar Cambios' para sincronizar con el disco.

### Requisitos funcionales
- Carga y parseo inicial de `inventario.csv` al iniciar la aplicación.
- Visualización en `ttk.Treeview` con 5 columnas bien formateadas y alineadas.
- Formulario de entrada con campos: SKU (código único), Nombre, Categoría (`Combobox`), Stock (entero), Precio (flotante).
- Selección de fila para eliminar ítem con confirmación previa.
- Búsqueda rápida por nombre o SKU que filtre la tabla en tiempo real.
- Exportación y sincronización de datos con el archivo CSV.

### Requisitos de interfaz
- `ttk.Treeview` con barras de desplazamiento vertical y horizontal (`Scrollbar`).
- Formulario en marco superior organizado en cuadrícula limpia.
- Barra inferior de estado con total de productos registrados y valor total del inventario en moneda.

### Datos
- Ficha de producto: SKU (`str`), Nombre (`str`), Categoría (`str`), Stock (`int`), Precio Unitario (`float`).
- Archivo de almacenamiento: CSV delimitado por comas.

### Estado
- Lista de objetos/diccionarios de productos en memoria.
- Identificador del ítem seleccionado en el Treeview (`tree.selection()`).
- Bandera booleana de cambios no guardados.

### Persistencia
Archivo CSV local (`datos/inventario.csv`).

### Validaciones
- SKU obligatorio y único (no permitir duplicados).
- Stock entero mayor o igual a 0.
- Precio flotante estrictamente mayor a 0.0.
- Nombre con al menos 3 caracteres.

### Casos límite
- Archivo CSV no existe al inicio (debe crearse con encabezados estándar).
- CSV con filas corruptas o campos numéricos mal formateados.
- Intentar agregar un SKU que ya existe en la tabla.

### Manejo de errores
- Capturar errores del módulo `csv` y notificar filas con formato inválido sin colapsar la aplicación.
- Prevenir la eliminación si no hay ninguna fila seleccionada.

### Fundamentos de Python relacionados
- Módulo estándar `csv` (`csv.DictReader`, `csv.DictWriter`).
- Manejo de rutas con `pathlib.Path`.
- Validaciones de tipos y unicidad con conjuntos (`set`) o listas.

### Conceptos Tkinter relacionados
- Widget `ttk.Treeview` y sus métodos: `.insert()`, `.delete()`, `.selection()`, `.item()`.
- Configuración de encabezados y columnas (`heading()`, `column()`, `show='headings'`).
- Barras de desplazamiento bidireccionales.

### Herramientas para investigar
- Documentación de `tkinter.ttk.Treeview`.
- Parámetro `show='headings'` en Treeview.
- Clases `csv.DictReader` y `csv.DictWriter` de Python.

### Diseño de interfaz
¿Cómo definirías el ancho y la alineación (`anchor='e'` para números y `anchor='w'` para texto) de cada columna del Treeview para maximizar la legibilidad?

### Diseño de variables
Usa nombres como `inventory_tree`, `sku_entry`, `name_entry`, `stock_entry`, `price_entry`, `save_csv_btn`, `total_stock_value_label`.

### Antes de programar
1. ¿Por qué es fundamental configurar `show='headings'` en un `Treeview` si solo se van a mostrar datos tabulares y no una estructura de árbol con jerarquías?
2. ¿Cómo se calculan el stock total y el valor monetario del inventario a partir de los datos cargados?

### Arquitectura
```
ejercicio_026/
├── app.py             # Vista con Treeview y formulario
├── inventory_repo.py  # Capa de acceso a datos CSV (lectura y guardado)
└── datos/
    └── inventario.csv # Archivo de datos de muestra
```

### Pruebas mínimas
1. Cargar la app con el CSV de muestra -> Comprobar que los productos aparezcan en la tabla con sus columnas alineadas.
2. Añadir un producto nuevo válido -> Verificar que se agregue a la tabla y que el valor total del inventario se incremente.

### Pruebas de error
1. Intentar registrar un SKU ya existente -> Debe mostrar advertencia 'El SKU ya se encuentra registrado'.
2. Ingresar stock negativo (-5) -> Debe rechazar el valor numérico.

### Experiencia de usuario
Al hacer clic en un encabezado de columna, debe mostrarse claramente la alineación y los valores deben formatearse coherentemente (ej. precios con `$`).

### Explicación posterior
¿Qué ventajas operativas ofrece `ttk.Treeview` frente a un simple `Listbox` cuando se manejan entidades con múltiples atributos estructurados?

### Aplicación profesional
Gestores de almacén en plantas fabriles, terminales de control de activos y paneles de control de mercancías.

### Reto adicional
Añade la funcionalidad de ordenar alfabética o numéricamente las filas del `Treeview` al hacer clic en el encabezado de cualquiera de las columnas.

---
> [Índice General](../README.md) · [← Ejercicio 025](../ejercicio_025/README.md) · [Ejercicio 027 →](../ejercicio_027/README.md)
