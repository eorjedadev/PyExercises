## Ejercicio 018 — Calculadora de Huella de Carbono y Consumo Energético (`CarbonFootprintApp`)

> [Índice General](../README.md) · [← Ejercicio 017](../ejercicio_017/README.md) · [Ejercicio 019 →](../ejercicio_019/README.md)

### Contexto profesional
En iniciativas de sostenibilidad empresarial y auditorías ambientales ISO 14064, los analistas recopilan consumos energéticos de oficinas para estimar las emisiones de CO2 equivalentes.

### Usuario objetivo
Auditor ambiental, gestor de sostenibilidad o encargado de instalaciones.

### Problema
La conversión manual de kilovatios-hora, litros de combustible y kilómetros de transporte a kilogramos de CO2e suele estar dispersa en tablas desactualizadas.

### Objetivo
Construir una calculadora ambiental estructurada por categorías (Electricidad, Gas Natural, Transporte Terrestre) con factores de emisión estandarizados, cálculo de emisiones totales y desglose porcentual.

### Flujo principal
El usuario ingresa el consumo mensual de electricidad (kWh), consumo de gas (m3) y kilómetros recorridos por la flota vehicular. Presiona 'Calcular Huella'. La aplicación muestra las toneladas de CO2e emitidas por categoría y el total acumulado, sugiriendo un nivel de impacto (Bajo, Moderado, Alto).

### Requisitos funcionales
- Captura de consumo eléctrico mensual (kWh).
- Captura de consumo de gas natural (m3).
- Captura de transporte vehicular (km).
- Factores de conversión configurables (kg CO2e por unidad de consumo).
- Cálculo de emisiones individuales y suma total en Toneladas de CO2e.
- Clasificación del nivel de impacto con cambio de color en banner (Verde, Amarillo, Rojo).

### Requisitos de interfaz
- Organización por categorías mediante marcos rotulados (`ttk.LabelFrame`).
- Panel de resultados con desglose en barras o etiquetas claras con dos decimales.
- Banner de dictamen ecológico destacado.

### Datos
- Consumos: flotantes positivos.
- Factores de emisión: constantes numéricas.
- Emisiones totales: float (toneladas de CO2e).

### Estado
- Variables de entrada y de resultados.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Todos los consumos deben ser números reales mayores o iguales a cero.
- Ningún campo debe quedar vacío (asumir 0 si el usuario no consume esa fuente).

### Casos límite
- Ingresar 0 en todos los consumos (resultado debe ser 0.00 t CO2e y nivel 'Impacto Nulo').
- Números astronómicos.

### Manejo de errores
- Manejar entradas inválidas notificando qué factor numérico no pudo interpretarse.

### Fundamentos de Python relacionados
- Diccionarios de factores de conversión.
- Sumas ponderadas y cálculo de proporciones porcentuales.

### Conceptos Tkinter relacionados
- Agrupación semántica con `ttk.LabelFrame`.
- Validación y actualización de etiquetas de resumen.

### Herramientas para investigar
- Estándares de cálculo de huella de carbono (factores IPCC o locales).
- Manejo de constantes en Python.

### Diseño de interfaz
¿Cómo dispondrías las tres fuentes de emisión para que el formulario se sienta equilibrado y no sobrecargue la parte superior de la ventana?

### Diseño de variables
Usa nombres como `kwh_entry`, `gas_entry`, `km_entry`, `total_emissions_var`, `impact_level_label`.

### Antes de programar
1. ¿Cómo se estructuran los factores de emisión en un diccionario para que sean fácilmente actualizables en el futuro sin modificar la interfaz?
2. ¿Cómo se clasifica el nivel de impacto de forma desacoplada de la vista?

### Arquitectura
```
ejercicio_018/
├── app.py           # Vistas y paneles por categoría
└── carbon_math.py   # Factores de emisión y cálculo de toneladas CO2e
```

### Pruebas mínimas
1. Ingresar 1000 kWh, 100 m3 gas y 500 km -> Comprobar que calcule el total esperado según los factores definidos.
2. Limpiar formulario -> Comprobar que los resultados vuelvan a 0.00 t.

### Pruebas de error
1. Escribir texto en consumo eléctrico -> Debe advertir error numérico sin cerrar la aplicación.

### Experiencia de usuario
El banner de nivel de impacto debe cambiar su color de fondo a verde si es bajo y a rojo si es alto.

### Explicación posterior
¿Por qué es conveniente separar los coeficientes de cálculo en un módulo de configuración en lugar de colocarlos directamente en las funciones de los botones?

### Aplicación profesional
Paneles de control de responsabilidad social corporativa (ESG), auditorías de eficiencia energética y calculadoras educativas.

### Reto adicional
Añade una estimación de 'Árboles necesarios para compensar esta emisión anual' basada en la absorción promedio de un árbol adulto.

---
> [Índice General](../README.md) · [← Ejercicio 017](../ejercicio_017/README.md) · [Ejercicio 019 →](../ejercicio_019/README.md)
