## Ejercicio 002 — Convertidor de Divisas y Unidades Métricas (`UnitConverterApp`)

> [Índice General](../README.md) · [← Ejercicio 001](../ejercicio_001/README.md) · [Ejercicio 003 →](../ejercicio_003/README.md)

### Contexto profesional
En laboratorios técnicos y almacenes de importación, los operadores reciben especificaciones en unidades del sistema imperial o divisas internacionales y requieren conversiones instantáneas mientras digitan datos.

### Usuario objetivo
Técnico de laboratorio o asistente de compras internacionales.

### Problema
La necesidad de consultar conversores en la web interrumpe el flujo operativo y provoca fallos por confusión entre kilogramos/libras, metros/pies y tasas de cambio.

### Objetivo
Construir una herramienta de conversión interactiva con pestañas o selector de categoría (Longitud, Masa, Moneda) que actualice la conversión automáticamente conforme el usuario escribe (`<KeyRelease>`).

### Flujo principal
El usuario selecciona el tipo de magnitud a convertir (ej. Longitud), selecciona la unidad origen y la unidad destino en listas desplegables, ingresa el valor a convertir y ve el resultado transformado al instante sin necesidad de oprimir un botón adicional.

### Requisitos funcionales
- Permitir seleccionar categorías: Longitud (km, m, cm, millas, pies, pulgadas), Masa (kg, g, lb, oz) y Moneda (USD, EUR, GBP a tasa fija local).
- Actualización reactiva al escribir en el campo de entrada mediante bindings de eventos de teclado.
- Botón de inversión rápida para intercambiar unidades origen y destino.
- Ajuste de precisión decimal configurable (2 a 4 decimales).

### Requisitos de interfaz
- Uso de `ttk.Combobox` para selección de unidades de origen y destino.
- Campo de entrada visible y estilizado para la cifra a transformar.
- Panel de resultado con tipografía destacada que muestre el valor con su abreviatura de unidad.
- Botón con icono o texto '<->' para inversión de unidades.

### Datos
- Factores de conversión estándar a una unidad base (ej. metros para longitud, gramos para masa).
- Valor de entrada: flotante positivo o cero.
- Valor convertido: flotante con redondeo especificado.

### Estado
- Categoría actualmente activa.
- Unidad origen y destino seleccionadas en las variables de control.
- Último valor numérico ingresado.

### Persistencia
No requiere almacenamiento persistente en disco.

### Validaciones
- Validar que el valor de entrada contenga exclusivamente números y a lo sumo un punto decimal.
- Prevenir divisiones por cero o factores nulos en conversiones personalizadas.

### Casos límite
- El campo de entrada queda completamente vacío al borrar con retroceso (el resultado debe mostrar '0.00' o permanecer limpio sin lanzar excepciones).
- El usuario selecciona la misma unidad en origen y destino (el resultado debe ser idéntico a la entrada).
- Cifras con notación científica o valores extremadamente pequeños.

### Manejo de errores
- Ignorar silenciosamente entradas no numéricas o colorear suavemente el borde del campo de texto cuando se detecte un carácter inválido.

### Fundamentos de Python relacionados
- Diccionarios anidados para almacenar tablas de factores de conversión relativas a una unidad pivote.
- Expresiones lambda o funciones de despacho para aplicar la fórmula de transformación.
- Manejo de redondeo con `round()` o módulo `decimal`.

### Conceptos Tkinter relacionados
- Widget `ttk.Combobox` y su evento virtual `<<ComboboxSelected>>`.
- Enlace de eventos de teclado mediante `.bind('<KeyRelease>', callback)`.
- Gestión de foco y actualización reactiva de variables `StringVar`.

### Herramientas para investigar
- Documentación de `tkinter.ttk.Combobox`.
- Mapeo de eventos en Tkinter (`<KeyRelease>`, `<FocusIn>`, `<FocusOut>`).

### Diseño de interfaz
¿Cómo dispondrías horizontalmente la unidad origen, el botón de intercambio y la unidad destino para que la relación visual sea intuitiva?

### Diseño de variables
Define nombres como `category_selector`, `source_unit_var`, `target_unit_var`, `input_value_entry`, `result_display_var`.

### Antes de programar
1. ¿Por qué es más eficiente convertir siempre a una 'unidad base' intermedia (ej. metros) en lugar de crear fórmulas cruzadas para cada par posible de unidades?
2. ¿Qué ventaja ofrece enlazar `<KeyRelease>` sobre usar un botón 'Calcular' tradicional?

### Arquitectura
```
ejercicio_002/
├── app.py            # Vista y enlaces de eventos
└── converter_core.py # Tablas de conversión y motor matemático desacoplado
```

### Pruebas mínimas
1. Seleccionar Longitud: 1 milla a kilómetros -> Validar que devuelva ~1.6093 km.
2. Presionar el botón de intercambio de unidades -> Validar que origen y destino se inviertan y el resultado se recalcule coherentemente.

### Pruebas de error
1. Escribir 'abc' en el campo de entrada -> Validar que el sistema no lance `ValueError` en consola y el resultado se limpie o indique entrada no válida.

### Experiencia de usuario
La respuesta al teclear debe ser inmediata sin retardos perceptibles. El botón de intercambio debe actualizar instantáneamente tanto los selectores como el resultado.

### Explicación posterior
Explica la diferencia entre capturar un evento con `command=` en un botón y usar `.bind('<KeyRelease>', ...)` en un campo de entrada.

### Aplicación profesional
Este componente reactivo se implementa en módulos de facturación aduanera, software de ingeniería civil y herramientas de logística de exportación.

### Reto adicional
Agrega una categoría de temperatura (Celsius, Fahrenheit, Kelvin) considerando que requiere funciones afines ($y = mx + b$) y no meramente factores multiplicativos simples.

---
> [Índice General](../README.md) · [← Ejercicio 001](../ejercicio_001/README.md) · [Ejercicio 003 →](../ejercicio_003/README.md)
