## Ejercicio 034 — Gestor de Menús y Precios de Restaurante (`RestaurantMenuManagerApp`)

> [Índice General](../README.md) · [← Ejercicio 033](../ejercicio_033/README.md) · [Ejercicio 035 →](../ejercicio_035/README.md)

### Contexto profesional
En establecimientos gastronómicos y franquicias de restaurantes, los gerentes de alimentos y bebidas actualizan la carta digital de platillos, precios y costos de insumos.

### Usuario objetivo
Gerente de restaurante o chef ejecutivo.

### Problema
El cambio desordenado de precios sin calcular el margen de ganancia respecto al costo de los ingredientes genera pérdidas operativas en platillos clave.

### Objetivo
Desarrollar una aplicación de gestión de menú con `ttk.Treeview` jerárquico por categorías (Entradas, Platos Fuertes, Postres, Bebidas), persistencia en JSON, cálculo del margen bruto de ganancia (%) por platillo y edición de precios.

### Flujo principal
El gerente visualiza el menú estructurado. Al registrar o editar un platillo, ingresa nombre, categoría, costo de insumos y precio de venta. La aplicación calcula el margen de ganancia $(\text{Precio} - \text{Costo}) / \text{Precio} \times 100$. Si el margen es inferior al 60%, se marca con advertencia en la tabla. Guarda los cambios en `menu.json`.

### Requisitos funcionales
- Carga y guardado estructurado en `menu.json`.
- Visualización en `ttk.Treeview` con categorías agrupadas o columna de categoría.
- Columnas: Código, Platillo, Categoría, Costo Insumos, Precio Venta, Margen Bruto (%).
- Formulario de alta y edición de platillos.
- Resalte visual (en color rojo/amarillo) de platillos con margen inferior al umbral recomendado (60%).
- Cálculo del precio promedio por categoría y margen promedio del menú.

### Requisitos de interfaz
- Treeview con doble scrollbar y formato monetario estricto.
- Formulario en marco lateral o superior con validaciones numéricas en vivo.
- Panel de métricas con el platillo más rentable y el menos rentable.

### Datos
- Platillo: id, nombre, categoria, costo (float), precio (float), margen (float).

### Estado
- Lista de platillos en memoria.
- Platillo en edición activa.

### Persistencia
Archivo JSON (`datos/menu.json`).

### Validaciones
- Precio de venta debe ser estrictamente mayor al costo de insumos.
- Costo y precio deben ser mayores a cero.
- Nombre de platillo obligatorio.

### Casos límite
- Ingresar costo igual o mayor al precio (margen 0% o negativo, debe alertar fuertemente).
- Platillos sin categoría asignada.

### Manejo de errores
- Impedir registrar platillos con precios menores al costo sin confirmación explícita del gerente.

### Fundamentos de Python relacionados
- Fórmulas de margen comercial y rentabilidad porcentual.
- Serialización JSON con listas de diccionarios.

### Conceptos Tkinter relacionados
- Uso de tags en `Treeview` para clasificar rentabilidad cromáticamente.
- Manejo de selecciones y precarga de datos en formularios para edición.

### Herramientas para investigar
- Fórmulas de margen de contribución en gastronomía (Food Cost).
- Métodos de inspección y edición de ítems en `ttk.Treeview`.

### Diseño de interfaz
¿Cómo diseñarías el formulario para que el cálculo del margen se actualice de inmediato conforme se escriben el costo y el precio?

### Diseño de variables
Usa nombres como `menu_tree`, `dish_name_entry`, `category_combo`, `cost_entry`, `price_entry`, `margin_display_label`, `save_menu_btn`.

### Antes de programar
1. ¿Cuál es la diferencia entre margen sobre venta $(P-C)/P$ y margen sobre costo $(P-C)/C$?
2. ¿Cómo se actualizan los valores de una fila en el Treeview cuando el usuario edita un platillo existente?

### Arquitectura
```
ejercicio_034/
├── app.py           # Vistas y tabla del menú
├── menu_service.py  # Fórmulas de costos, márgenes y métricas de rentabilidad
└── datos/
    └── menu.json    # Archivo de datos de platillos
```

### Pruebas mínimas
1. Registrar platillo con Costo $30 y Precio $100 -> Verificar margen del 70% y tag verde.
2. Registrar platillo con Costo $50 y Precio $100 -> Verificar margen del 50% y tag rojo de advertencia.

### Pruebas de error
1. Ingresar Costo $100 y Precio $80 -> Debe advertir que el costo supera al precio de venta.

### Experiencia de usuario
El margen debe calcularse en vivo conforme el usuario digita los números en los campos de costo y precio.

### Explicación posterior
¿Cómo se gestiona el flujo de edición (cargar datos seleccionados al formulario y guardar cambios) en una interfaz con `Treeview`?

### Aplicación profesional
Sistemas de punto de venta gastronómicos (POS), ingeniería de menú en cadenas de restaurantes y software de costeo.

### Reto adicional
Añade un filtro desplegable que permita visualizar únicamente los platillos de una categoría específica o aquellos con margen deficiente.

---
> [Índice General](../README.md) · [← Ejercicio 033](../ejercicio_033/README.md) · [Ejercicio 035 →](../ejercicio_035/README.md)
