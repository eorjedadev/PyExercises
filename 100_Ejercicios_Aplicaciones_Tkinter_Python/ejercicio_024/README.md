## Ejercicio 024 — Simulador de Tarifas de Envíos y Paquetería (`ShippingCalculatorApp`)

> [Índice General](../README.md) · [← Ejercicio 023](../ejercicio_023/README.md) · [Ejercicio 025 →](../ejercicio_025/README.md)

### Contexto profesional
En empresas de comercio electrónico y operadores logísticos, los dependientes de mostrador cotizan el costo de envío de paquetes según su peso físico y su peso volumétrico.

### Usuario objetivo
Operador de mostrador de paquetería o asistente de logística.

### Problema
Ignorar el peso volumétrico en paquetes grandes pero ligeros genera pérdidas de flete para la empresa de transporte.

### Objetivo
Desarrollar una aplicación de cotización logística que reciba dimensiones del paquete (largo, ancho, alto en cm) y peso real en kg, calcule el peso volumétrico según factor IATA, determine el peso tasable mayor y aplique la tarifa según destino y tipo de servicio (Estándar o Exprés).

### Flujo principal
El operador ingresa las tres dimensiones y el peso en báscula. Selecciona la zona de destino y el tipo de servicio. La aplicación calcula el peso volumétrico ($L \times W \times H / 5000$), resalta cuál de los dos pesos es el tasable (el mayor de ambos) y muestra el costo total desglosado con IVA.

### Requisitos funcionales
- Captura de: Largo, Ancho, Alto (cm) y Peso real (kg).
- Selector de Zona de destino (`Combobox`: Local, Nacional, Internacional).
- Selector de Servicio (`Radiobutton`: Estándar, Exprés con recargo del 40%).
- Cálculo del peso volumétrico: $(\text{largo} \times \text{ancho} \times \text{alto}) / 5000$.
- Determinación automática del peso tasable: $\max(\text{peso real}, \text{peso volumétrico})$.
- Cálculo del subtotal de envío, IVA (16%) y total final a cobrar.

### Requisitos de interfaz
- Cuadrícula ordenada para las dimensiones físicas.
- Panel comparativo destacado: Peso Real vs Peso Volumétrico con indicación del peso tasable aplicado.
- Panel de factura/recibo a la derecha con el desglose numérico claro.

### Datos
- Dimensiones: floats positivos.
- Peso real y volumétrico: floats.
- Tarifas base por zona y recargos por servicio.

### Estado
- Variables de dimensiones y opciones de envío.
- Desglose financiero calculado.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Todas las medidas deben ser estrictamente números positivos mayores a cero.
- Peso real no puede ser cero ni negativo.

### Casos límite
- Paquetes pequeños pero muy pesados (el peso real domina).
- Paquetes enormes pero muy ligeros (el peso volumétrico domina).
- Números decimales en dimensiones.

### Manejo de errores
- Notificar con claridad si alguna dimensión falta o no es un número válido.

### Fundamentos de Python relacionados
- Función estándar `max()` para determinar el mayor entre dos valores numéricos.
- Operaciones aritméticas y cálculo de impuestos porcentuales.

### Conceptos Tkinter relacionados
- Distribución multipanel con `grid` y `pack` combinados ordenadamente.
- Formateo de salidas y actualización reactiva de etiquetas.

### Herramientas para investigar
- Fórmula de peso volumétrico estándar de la IATA (divisor 5000).
- Función `max()` en Python.

### Diseño de interfaz
¿Cómo estructurarías los paneles para que el operador vea claramente por qué se le está cobrando por peso volumétrico y no por peso físico?

### Diseño de variables
Usa nombres como `length_entry`, `width_entry`, `height_entry`, `actual_weight_entry`, `volumetric_weight_label`, `billable_weight_label`, `total_price_label`.

### Antes de programar
1. ¿Qué es el peso tasable en logística y por qué se utiliza `max(peso_real, peso_volumetrico)`?
2. ¿Cómo se calcula el IVA desglosado del subtotal?

### Arquitectura
```
ejercicio_024/
├── app.py           # Interfaz de mostrador y cotización
└── logistics_core.py # Motor de cálculo volumétrico y matriz de tarifas
```

### Pruebas mínimas
1. Paquete de 50x50x50 cm (peso volumétrico = 25 kg) con peso real de 5 kg -> Debe tasar por 25 kg.
2. Paquete de 10x10x10 cm (peso volumétrico = 0.2 kg) con peso real de 8 kg -> Debe tasar por 8 kg.

### Pruebas de error
1. Ingresar dimensión 0 o negativa -> Debe advertir error en dimensiones físicas.

### Experiencia de usuario
El peso tasable debe aparecer remarcado en negrita para facilitar la explicación al cliente final en mostrador.

### Explicación posterior
¿Cómo ayuda la función `max()` a simplificar la lógica de determinación de la tarifa tasable frente a estructuras condicionales complejas?

### Aplicación profesional
Software de punto de venta en sucursales de mensajería (DHL, FedEx, correos nacionales) y módulos de flete en comercio electrónico.

### Reto adicional
Añade una opción de 'Seguro de envío opcional' que sume el 1.5% del valor declarado del paquete si el usuario marca la casilla correspondiente.

---
> [Índice General](../README.md) · [← Ejercicio 023](../ejercicio_023/README.md) · [Ejercicio 025 →](../ejercicio_025/README.md)
