## Ejercicio 011 — Calculadora de Cuotas y Préstamos Amortizados (`LoanEstimatorApp`)

> [Índice General](../README.md) · [← Ejercicio 010](../ejercicio_010/README.md) · [Ejercicio 012 →](../ejercicio_012/README.md)

### Contexto profesional
En sucursales bancarias y entidades de microcrédito, los asesores comerciales necesitan presentar a los clientes un cálculo preliminar de cuotas mensuales e intereses antes de iniciar la solicitud formal.

### Usuario objetivo
Asesor financiero o ejecutivo de créditos.

### Problema
El cálculo de la fórmula francesa de amortización en calculadoras de mano produce errores frecuentes de redondeo y desconfianza en los clientes.

### Objetivo
Construir una aplicación que reciba monto del préstamo, tasa de interés anual y plazo en meses, validando los valores y calculando la cuota mensual fija, el interés total a pagar y el costo total del crédito.

### Flujo principal
El asesor introduce el monto solicitado, la tasa anual (%) y el número de meses. Al hacer clic en 'Calcular Cuota', la interfaz presenta el desglose financiero en un panel destacado y una opción de limpieza.

### Requisitos funcionales
- Captura de Monto del préstamo (flotante positivo).
- Captura de Tasa de interés anual porcentual (flotante positivo).
- Plazo en meses (entero positivo).
- Cálculo de cuota mensual fija mediante fórmula de anualidades: $C = P \times \frac{i(1+i)^n}{(1+i)^n - 1}$.
- Cálculo del total de intereses acumulados y monto total devuelto.

### Requisitos de interfaz
- Cuadrícula ordenada con etiquetas a la izquierda y entradas numéricas a la derecha.
- Panel inferior con borde de distinción para los resultados financieros.
- Formateo estricto con signo monetario y separadores de miles.

### Datos
- Monto ($P$): float.
- Tasa anual: float.
- Tasa mensual ($i$): tasa anual / 12 / 100.
- Plazo ($n$): int.
- Cuota ($C$), Interés Total, Monto Total: float.

### Estado
- Variables `StringVar` para las entradas y los resultados calculados.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Monto debe ser mayor a 0.
- Tasa de interés debe ser mayor o igual a 0 y menor a 100.
- Plazo debe ser entero entre 1 y 360 meses.

### Casos límite
- Tasa de interés igual a 0% (préstamo sin intereses: cuota = monto / meses, evitar división por cero en la fórmula general).
- Números no válidos o caracteres alfabéticos.

### Manejo de errores
- Manejar la división por cero si la tasa es 0 implementando la rama condicional adecuada.
- Mostrar mensajes claros de error si las entradas no son números positivos válidos.

### Fundamentos de Python relacionados
- Fórmulas financieras exponenciales con el operador `**`.
- Control de ramas con `if/else` para tasa cero vs tasa con interés.
- Formateo de números con dos decimales y comas de miles.

### Conceptos Tkinter relacionados
- Widgets `ttk.Entry`, `ttk.Button`, `ttk.Label`.
- Geometría con `grid` y espaciado proporcional.

### Herramientas para investigar
- Fórmula de amortización francesa.
- Funciones matemáticas de la biblioteca estándar de Python.

### Diseño de interfaz
¿Cómo asegurarías que el resultado de la cuota mensual resalte con mayor tamaño de fuente que los subtotales secundarios?

### Diseño de variables
Usa nombres como `loan_amount_entry`, `annual_rate_entry`, `loan_term_entry`, `monthly_payment_var`, `total_interest_var`.

### Antes de programar
1. ¿Qué ocurre en la fórmula de anualidad si la tasa de interés es exactamente 0%?
2. ¿Cómo se convierte una tasa anual porcentual a tasa mensual decimal efectiva?

### Arquitectura
```
ejercicio_011/
├── app.py           # Vistas y formularios
└── loan_math.py     # Lógica matemática pura de amortización
```

### Pruebas mínimas
1. Monto $10,000, Tasa 12% anual, Plazo 12 meses -> Validar cuota mensual aproximada de $888.49.
2. Monto $12,000, Tasa 0% anual, Plazo 12 meses -> Validar cuota mensual exacta de $1,000.00.

### Pruebas de error
1. Ingresar plazo 0 o negativo -> Debe mostrar advertencia de plazo inválido.

### Experiencia de usuario
El campo de cuota mensual debe ser inmediatamente visible y tener un contraste claro con el fondo.

### Explicación posterior
¿Cómo evitaste el error de `ZeroDivisionError` cuando un usuario simula un préstamo con tasa 0%?

### Aplicación profesional
Simuladores de crédito en agencias de vehículos, terminales de asesoría hipotecaria y tiendas departamentales.

### Reto adicional
Añade un botón 'Ver Tabla de Amortización' que abra una ventana secundaria con el desglose mes a mes del saldo, capital e interés.

---
> [Índice General](../README.md) · [← Ejercicio 010](../ejercicio_010/README.md) · [Ejercicio 012 →](../ejercicio_012/README.md)
