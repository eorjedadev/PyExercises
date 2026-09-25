# Ejercicio 049 — Muestra frente a padrón

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_048/README.md) · [Siguiente](../ejercicio_050/README.md)

### Contexto

Una red de servicios dispone del marco de invitaciones por zona. Sector: **servicios y opinión**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Se desconoce cuánto se apartan los encuestados de la población objetivo. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué zonas quedan subrepresentadas y cómo afecta una estimación global?

### Preguntas secundarias

- ¿Qué zonas y canales están menos representados entre quienes responden?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **una persona ficticia invitada**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **1,294 registros**, 8 campos. Fuente principal: una persona ficticia invitada.
- [marco](datos/marco.csv): **3 registros**, 3 campos. Muestreo aleatorio de igual cantidad por zona; respuesta voluntaria posterior.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Marco ficticio fijo: norte 2400, centro 6000, sur 3600 personas. Se selecciona igual número de invitaciones por zona sin reemplazo; la respuesta es voluntaria. Peso es población de zona dividida por invitaciones originales de esa zona, sin ajuste por respuesta.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de persona ficticia invitada | texto |
| `fecha` | Fecha de invitación | fecha |
| `zona` | norte, centro o sur | categoría |
| `canal` | web o telefono | categoría |
| `invitado` | 1 si recibió invitación | booleano |
| `responde` | 1 si respondió | booleano |
| `satisfaccion` | Valor ordinal 1 a 5, ausente sin respuesta | entero |
| `peso` | Inverso de probabilidad de inclusión por zona, no ajustado por no respuesta | real |

**marco**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `zona` | Estrato territorial | categoría |
| `poblacion_elegible` | Personas del marco poblacional | entero |
| `invitaciones` | Personas seleccionadas sin reemplazo | entero |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **una persona ficticia invitada** y qué dejaría de representar si agregas por `zona`?
- ¿Qué significan `satisfaccion` y `peso`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Los totales del marco no se suman repetidos por encuestado; ponderar no garantiza ignorabilidad.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Relaciona marco y respuestas, concilia invitados, evalúa pesos y distribución de respondentes frente a elegibles.

La pregunta está delimitada, pero debes elegir transformaciones, métricas y representación. Compara al menos dos decisiones plausibles de preparación y explica si alteran el mensaje.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Módulos para lectura, validación y análisis; claves como tuplas cuando corresponda; context managers para archivos o conexiones; parámetros y validaciones de cardinalidad. Diseña comprobaciones de conservación de filas o importes.

### Conceptos de Ciencia de Datos relacionados

**Marco muestral; postestratificación; no respuesta.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Investiga cardinalidad y validación de uniones antes de combinar fuentes. Decide el tipo de unión según la población que quieres conservar. Organiza un notebook con contexto, código propio, resultados e interpretación, o un script con informe equivalente.

### Diseño de variables

Identifica nombres para la fuente de **una persona ficticia invitada**, el subconjunto elegible, la comparación por `zona`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **muestra frente a padrón**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué zonas y canales están menos representados entre quienes responden? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué zonas quedan subrepresentadas y cómo afecta una estimación global?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Los totales del marco no se suman repetidos por encuestado; ponderar no garantiza ignorabilidad.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Los totales del marco no se suman repetidos por encuestado; ponderar no garantiza ignorabilidad.**

### Consulta recomendada

- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/): consulta cuadernos, kernel y ejecución ordenada.

Antes de consultar, escribe una pregunta concreta sobre **marco muestral**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Los totales del marco no se suman repetidos por encuestado; ponderar no garantiza ignorabilidad.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Diseño de encuestas y evaluación de representatividad. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Diseña una segunda ronda de recogida priorizando cobertura. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
