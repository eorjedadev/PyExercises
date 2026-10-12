## Ejercicio 035 — Monitor de Precios de Competidores (`PriceBenchmarkApp`)

> [Índice General](../README.md) · [← Ejercicio 034](../ejercicio_034/README.md) · [Ejercicio 036 →](../ejercicio_036/README.md)

### Contexto profesional
En áreas comerciales y de pricing de empresas minoristas, los analistas comparan periódicamente los precios de su catálogo frente a los precios de tres competidores clave del mercado.

### Usuario objetivo
Analista de pricing o especialista comercial.

### Problema
La falta de visibilidad del diferencial porcentual de precios provoca pérdidas de competitividad o ventas con márgenes innecesariamente reducidos.

### Objetivo
Construir una herramienta de benchmarking con `ttk.Treeview` que cargue un catálogo de productos con precio propio y precios de competidores desde un CSV, calculando la desviación porcentual, la posición de precio más bajo y el índice de competitividad.

### Flujo principal
El analista carga el archivo CSV con las cotizaciones de mercado. La tabla muestra: Producto, Nuestro Precio, Comp. A, Comp. B, Comp. C, Precio Mínimo de Mercado y Diferencial (%). Si nuestro precio es más alto que el más barato del mercado, se resalta en rojo con el porcentaje excedente; si somos el más barato, se resalta en verde.

### Requisitos funcionales
- Carga de archivo CSV (`datos/benchmark_precios.csv`).
- Columnas en Treeview: SKU, Producto, Nuestro Precio, Comp A, Comp B, Comp C, Mínimo Mercado, Diferencial %.
- Cálculo automático del precio más bajo entre los competidores mediante `min()`.
- Cálculo de la desviación porcentual: $(\text{Nuestro} - \text{Mínimo}) / \text{Mínimo} \times 100$.
- Resalte en verde si Nuestro Precio es <= Mínimo Mercado; en rojo si es más caro.
- Panel resumen: Cantidad de productos donde somos más caros, más baratos y precio promedio.

### Requisitos de interfaz
- Treeview con alineación numérica a la derecha y columnas destacadas.
- Resalte cromático de filas con tags.
- Botón para exportar informe de productos no competitivos a un nuevo CSV.

### Datos
- Producto benchmark: sku, nombre, precio_propio, comp_a, comp_b, comp_c, min_mercado, diferencial.

### Estado
- Lista de productos benchmark en memoria.
- Umbral de tolerancia de precio.

### Persistencia
Lectura desde CSV (`datos/benchmark_precios.csv`).

### Validaciones
- Todos los precios deben ser flotantes positivos mayores a cero.
- Descartar o advertir filas con precios nulos.

### Casos límite
- Un competidor no tiene precio registrado (ignorar ese competidor para el mínimo o usar promedio).
- Todos los competidores tienen exactamente el mismo precio.

### Manejo de errores
- Manejar conversiones numéricas con fallos en el CSV omitiendo la fila con mensaje en log.

### Fundamentos de Python relacionados
- Función `min()` con colecciones numéricas.
- Fórmulas de variación porcentual relativa.
- Manejo de CSV y formateo monetario.

### Conceptos Tkinter relacionados
- Tags condicionales de filas en `ttk.Treeview`.
- Cálculos en lote y actualización fluida de tablas.

### Herramientas para investigar
- Función `min()` de Python.
- Formateo de números flotantes con signo positivo explícito (`f'{diff:+.1f}%'`).

### Diseño de interfaz
¿Cómo estructurarías las columnas para que la comparación entre 'Nuestro Precio' y 'Mínimo del Mercado' sea inmediata a la vista?

### Diseño de variables
Usa nombres como `benchmark_tree`, `load_csv_btn`, `export_uncompetitive_btn`, `cheaper_count_label`, `expensive_count_label`.

### Antes de programar
1. ¿Cómo se determina el precio mínimo entre tres columnas numéricas ignorando valores vacíos o cero?
2. ¿Cómo se formatea una cadena de porcentaje para que incluya el signo '+' si el valor es positivo (ej. `+12.5%`)?

### Arquitectura
```
ejercicio_035/
├── app.py              # Visualizador y tabla de benchmark
├── benchmark_math.py   # Lógica de cálculo de desviaciones y mínimos de mercado
└── datos/
    └── benchmark_precios.csv # Dataset con precios de competidores
```

### Pruebas mínimas
1. Cargar dataset -> Comprobar que calcule el mínimo de mercado y la variación porcentual de cada fila con su color correspondiente.
2. Verificar que las filas más caras tengan tag rojo y las más baratas tag verde.

### Pruebas de error
1. Cargar archivo con una celda no numérica -> Debe omitir la fila o marcarla con error sin abortar la carga del resto.

### Experiencia de usuario
El diferencial porcentual debe resaltar claramente con su signo (+ o -) para evitar confusiones de interpretación.

### Explicación posterior
¿Cómo se calculan variaciones porcentuales relativas y cómo se traducen a estados visuales en un `Treeview`?

### Aplicación profesional
Herramientas de monitorización de precios en retail, inteligencia competitiva y gestión de márgenes de venta.

### Reto adicional
Añade un control deslizante (`Scale`) que permita simular qué pasaría si reducimos todos nuestros precios un X% (actualización en tiempo real de la tabla).

---
> [Índice General](../README.md) · [← Ejercicio 034](../ejercicio_034/README.md) · [Ejercicio 036 →](../ejercicio_036/README.md)
