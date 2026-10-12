## Ejercicio 001 — Calculadora de Presupuesto Rápido de Viaje (`TravelBudgetApp`)

> [Índice General](../README.md) · [Ejercicio 002 →](../ejercicio_002/README.md)

### Contexto profesional
En agencias de viajes corporativas y departamentos de recursos humanos, los coordinadores necesitan estimar rápidamente el viático estimado de un empleado antes de emitir una orden de compra formal.

### Usuario objetivo
Coordinador de operaciones o gestor de viajes corporativos.

### Problema
El cálculo manual de viáticos (hospedaje por noche, alimentación diaria y traslados) genera discrepancias en decimales, omisiones de días de estancia y retrasos al elaborar cotizaciones preliminares.

### Objetivo
Desarrollar una aplicación de escritorio que reciba días de estancia, tarifa diaria de hotel, viático diario de alimentos y gastos de traslado, validando los valores y calculando subtotales y el costo total proyectado.

### Flujo principal
El usuario abre la ventana, ingresa el número de días y los montos correspondientes a hospedaje, comida y transporte, presiona el botón de cálculo y visualiza de inmediato el desglose y monto total. Puede presionar un botón de limpieza para restablecer los valores iniciales.

### Requisitos funcionales
- Permitir la captura de días de estancia (entero positivo).
- Capturar costo diario de hotel, costo diario de alimentos y costo fijo de transporte (flotantes positivos).
- Calcular subtotal de hospedaje (días * hotel).
- Calcular subtotal de alimentación (días * alimentos).
- Calcular monto total (subtotal hospedaje + subtotal alimentos + transporte).
- Proporcionar acción para limpiar todos los campos y restablecer resultados a cero.

### Requisitos de interfaz
- Ventana con título descriptivo y dimensiones iniciales adecuadas que impida distorsión de controles.
- Disposición organizada en cuadrícula (`grid`) con alineación clara entre etiquetas y campos de entrada.
- Sección diferenciada visualmente para los resultados calculados.
- Botones claramente identificables para la acción principal ('Calcular Presupuesto') y secundaria ('Limpiar').

### Datos
- Días de estancia: entero (`int`).
- Tarifa hotelera diaria: flotante (`float`, moneda local).
- Tarifa alimentaria diaria: flotante (`float`, moneda local).
- Monto de transporte: flotante (`float`, moneda local).
- Subtotales y Total: valores calculados con 2 decimales.

### Estado
- Variables de control de Tkinter (`StringVar` o `DoubleVar`) para enlazar los campos de entrada.
- Variable para mostrar el total acumulado y subtotales en las etiquetas de salida.

### Persistencia
No requiere persistencia en disco; opera en memoria volátil durante la sesión de la ventana.

### Validaciones
- Verificar que el número de días sea un número entero mayor o igual a 1.
- Verificar que las tarifas y costos sean números reales mayores o iguales a 0.0.
- Comprobar que ningún campo obligatorio se encuentre en blanco al presionar calcular.

### Casos límite
- El usuario ingresa texto no numérico en los campos de entrada.
- El usuario ingresa números negativos o valores con formato de coma en vez de punto decimal.
- El usuario presiona 'Calcular' con todos los campos vacíos.
- El usuario ingresa números extremadamente grandes (desbordamiento visual de la etiqueta).

### Manejo de errores
- Notificar errores de entrada mediante una etiqueta de estado visible en color de advertencia o diálogo informativo sin abortar la aplicación.
- Capturar `ValueError` durante la conversión de tipos en la capa de procesamiento.

### Fundamentos de Python relacionados
- Conversión de tipos de datos (`int()`, `float()`).
- Manejo de excepciones con bloques `try...except ValueError`.
- Formateo de cadenas numéricas con especificadores de formato (`f'${total:,.2f}'`).
- Funciones puras para el cálculo matemático desacoplado de la interfaz.

### Conceptos Tkinter relacionados
- Creación de ventana principal con `Tk()`.
- Distribución geométrica mediante `grid(row=..., column=..., padx=..., pady=...)`.
- Widgets: `Label`, `Entry`, `Button`.
- Variables de Tkinter: `StringVar`, `DoubleVar`, `IntVar`.

### Herramientas para investigar
- Métodos de widgets Tkinter: `.get()`, `.set()`, `.delete()`.
- Documentación oficial de Python sobre `tkinter` y gestor de geometría `grid`.
- Función integrada `round()` y formateo de cadenas con formato de moneda.

### Diseño de interfaz
¿Cómo garantizarías que las etiquetas queden alineadas a la derecha y los campos de entrada a la izquierda en una cuadrícula? ¿Qué espaciado interno (`padx`, `pady`) evita que los elementos se sientan amontonados?

### Diseño de variables
Utiliza nombres semánticos como `days_entry`, `hotel_rate_var`, `food_allowance_var`, `transport_cost_var`, `total_display_label`. Evita `e1`, `e2`, `v1`, `btn_calc`.

### Antes de programar
1. ¿La lógica de cálculo de subtotales debe residir dentro de la función del botón o en una función matemática pura independiente?
2. ¿Qué ocurre si el usuario escribe `$150.00` en lugar de `150.00`?
3. ¿Cómo evitarás que la ventana parpadee o cambie de tamaño al mostrar los resultados?

### Arquitectura
```
ejercicio_001/
├── app.py           # Configuración de ventana Tkinter y widgets
└── calculator.py    # Lógica de cálculo matemático puro y validación
```

### Pruebas mínimas
1. Ingresar 5 días, $100 hotel, $40 comida, $50 transporte -> Validar que el total proyectado sea $750.00 exactos.
2. Presionar el botón 'Limpiar' -> Verificar que todas las entradas queden en blanco y el total en $0.00.

### Pruebas de error
1. Ingresar 'cinco' en días -> Debe mostrar un mensaje de validación indicando que los días deben ser enteros numéricos.
2. Ingresar un valor negativo en transporte (-50) -> Debe indicar que los costos no pueden ser negativos.

### Experiencia de usuario
El cursor debe iniciar enfocado en el primer campo de entrada (`days_entry.focus()`). El resultado debe distinguirse con tipografía más grande o en negrita respecto a las etiquetas secundarias.

### Explicación posterior
¿Por qué es una buena práctica separar la función que calcula el monto de la función asociada al evento del botón? ¿Cómo gestionaste la actualización de las etiquetas de resultados?

### Aplicación profesional
Este patrón de entrada-cálculo-salida en memoria es la base de cotizadores en tiempo real, simuladores financieros de sucursal y calculadoras de fletes.

### Reto adicional
Añade un selector de tipo de moneda (USD, EUR, MXN) que actualice automáticamente el símbolo monetario de los resultados sin alterar los cálculos subyacentes.

---
> [Índice General](../README.md) · [Ejercicio 002 →](../ejercicio_002/README.md)
