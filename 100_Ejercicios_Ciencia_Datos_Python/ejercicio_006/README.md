# Ejercicio 006 — Mediciones con distintas unidades

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_005/README.md) · [Siguiente](../ejercicio_007/README.md)

### Contexto

Un equipo ambiental recibe lecturas de temperatura. Sector: **ambiente**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Las estaciones exportan valores con unidades diferentes. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Pueden compararse las temperaturas entre zonas después de validar unidades?

### Preguntas secundarias

- ¿Qué cobertura de horas respalda cada comparación territorial?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un sensor y día observado**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.txt): **60 registros**, 7 campos. Fuente principal: un sensor y día observado.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

El diseño espera una fila por entidad y día en la ventana nominal. La ausencia de una fila debe distinguirse de una observación igual a cero. El intervalo nominal se documenta en procedencia.json; pueden faltar registros de ese calendario.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de lectura | texto |
| `fecha` | Fecha representada por la lectura | fecha |
| `sensor` | Código de sensor | texto |
| `zona` | norte, centro o sur | categoría |
| `valor` | Temperatura media de horas observadas en la unidad indicada | real |
| `unidad` | C para Celsius o F para Fahrenheit | categoría |
| `horas_operativas` | Horas representadas por la lectura, 0 a 24 | real |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un sensor y día observado** y qué dejaría de representar si agregas por `sensor`?
- ¿Qué significan `valor` y `horas_operativas`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **La misma cifra cambia de significado según la unidad; una lectura extrema puede ser real.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Reconoce Celsius y Fahrenheit, conserva valor original y comparable, y resume rangos por sensor.

La pregunta y los cálculos a contrastar están delimitados. Antes de usar una biblioteca, explica sobre tres filas cómo obtendrías un resumen y qué registros no incluirías.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Registra ruta de entrada, reglas de inclusión y comprobaciones manuales. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Variables y tipos para distinguir cantidades de etiquetas; operadores y condicionales para expresar reglas; ciclos, listas, tuplas, conjuntos y diccionarios para recorrer registros, representar claves y contar sin perder información; lectura de archivos con codificación explícita.

### Conceptos de Ciencia de Datos relacionados

**Escalas; comparabilidad; trazabilidad.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

La biblioteca estándar permite comprender la transformación: investiga `csv` o `json` según el archivo, listas para registros, diccionarios para recuentos y `statistics` para contrastar resúmenes. Primero explica un cálculo sobre tres filas sin una operación tabular automática. Matplotlib puede representar la comparación una vez definida la pregunta; no sustituye su interpretación.

### Diseño de variables

Identifica nombres para la fuente de **un sensor y día observado**, el subconjunto elegible, la comparación por `sensor`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **mediciones con distintas unidades**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cobertura de horas respalda cada comparación territorial? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Representa la comparación que responde a «¿Pueden compararse las temperaturas entre zonas después de validar unidades?». Puedes investigar barras para grupos o una distribución para valores numéricos. Elige una sola figura, indica unidades, población y número de observaciones, y explica por qué ayuda más que una tabla.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- La misma cifra cambia de significado según la unidad; una lectura extrema puede ser real.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **La misma cifra cambia de significado según la unidad; una lectura extrema puede ser real.**

### Consulta recomendada

- [Tutorial de Python](https://docs.python.org/es/3/tutorial/): consulta estructuras, control de flujo, funciones, archivos y excepciones.
- [Guía de Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html): consulta figura, ejes y representación de variables.

Antes de consultar, escribe una pregunta concreta sobre **escalas**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión de 120–180 palabras con una cifra, su denominador o unidad, la decisión que respalda y una limitación. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **La misma cifra cambia de significado según la unidad; una lectura extrema puede ser real.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Informes de redes de medición y vigilancia ambiental. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Una estación deja de indicar la unidad: documenta qué puede y qué no puede recuperarse. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
