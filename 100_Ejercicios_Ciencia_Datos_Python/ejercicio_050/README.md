# Ejercicio 050 — Facturación y medición

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_049/README.md) · [Siguiente](../ejercicio_051/README.md)

### Contexto

Un administrador relaciona lecturas y tarifas por edificio. Sector: **energía**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

La factura crece y se atribuye a mayor consumo. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué parte del cambio contable proviene de consumo y qué parte de tarifa?

### Preguntas secundarias

- ¿Qué cambia al considerar ocupación, clima y superficie?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un edificio y día**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.xlsx): **2,151 registros**, 8 campos. Fuente principal: un edificio y día.
- [edificios](datos/edificios.csv): **3 registros**, 3 campos. Registro físico de edificios.
- [tarifas](datos/tarifas.csv): **2 registros**, 3 campos. Contrato con dos períodos. Debes resolver la relación por intervalo de fechas.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

El diseño espera una fila por entidad y día en la ventana nominal. La ausencia de una fila debe distinguirse de una observación igual a cero. El intervalo nominal se documenta en procedencia.json; pueden faltar registros de ese calendario.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de lectura diaria | texto |
| `fecha` | Día de consumo | fecha |
| `edificio` | Código de edificio | texto |
| `temperatura_c` | Temperatura exterior observada ese día en Celsius | real |
| `ocupacion` | Personas presentes durante ese día | entero |
| `kwh` | Energía consumida durante ese día | real |
| `superficie_m2` | Superficie del edificio en m² | real |
| `tarifa` | Precio unitario aplicado en PEN por kWh | real |

**edificios**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `edificio` | Clave | texto |
| `uso` | Uso principal | categoría |
| `superficie_m2` | Superficie fija en m² | real |

**tarifas**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `desde` | Inicio inclusivo de vigencia | fecha |
| `hasta` | Fin inclusivo de vigencia | fecha |
| `pen_kwh` | PEN por kWh, aplicable a los tres edificios | real |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un edificio y día** y qué dejaría de representar si agregas por `edificio`?
- ¿Qué significan `kwh` y `temperatura_c`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Cambiar simultáneamente cantidades y precios genera interacción; declara dónde la asignas.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Relaciona metadatos, compara períodos completos y produce una descomposición con referencia explícita.

La pregunta está delimitada, pero debes elegir transformaciones, métricas y representación. Compara al menos dos decisiones plausibles de preparación y explica si alteran el mensaje.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Módulos para lectura, validación y análisis; claves como tuplas cuando corresponda; context managers para archivos o conexiones; parámetros y validaciones de cardinalidad. Diseña comprobaciones de conservación de filas o importes.

### Conceptos de Ciencia de Datos relacionados

**Descomposición de cambios; unidades; integración.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Investiga cardinalidad y validación de uniones antes de combinar fuentes. Decide el tipo de unión según la población que quieres conservar. Organiza un notebook con contexto, código propio, resultados e interpretación, o un script con informe equivalente.

### Diseño de variables

Identifica nombres para la fuente de **un edificio y día**, el subconjunto elegible, la comparación por `edificio`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **facturación y medición**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia al considerar ocupación, clima y superficie? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué parte del cambio contable proviene de consumo y qué parte de tarifa?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Cambiar simultáneamente cantidades y precios genera interacción; declara dónde la asignas.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Cambiar simultáneamente cantidades y precios genera interacción; declara dónde la asignas.**

### Consulta recomendada

- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/): consulta cuadernos, kernel y ejecución ordenada.

Antes de consultar, escribe una pregunta concreta sobre **descomposición de cambios**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Cambiar simultáneamente cantidades y precios genera interacción; declara dónde la asignas.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Auditoría de consumo y planificación de recursos. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Utiliza el período final como referencia y compara la atribución. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
