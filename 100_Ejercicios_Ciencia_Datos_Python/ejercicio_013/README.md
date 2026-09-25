# Ejercicio 013 — Defectos con tamaños de lote diferentes

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_012/README.md) · [Siguiente](../ejercicio_014/README.md)

### Contexto

Una planta compara turnos de producción. Sector: **industria**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

El turno de mayor volumen registra más defectos. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué turno presenta mayor proporción de unidades defectuosas?

### Preguntas secundarias

- ¿Qué cambia al comparar turnos y tamaños de lote?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un lote producido**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **103 registros**, 12 campos. Fuente principal: un lote producido.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Vibración y parada previa están disponibles al inicio; unidades, defectos y horas se conocen al terminar el lote. Fallo_7d y reparación son posteriores y tienen seguimiento hasta 2026-01-07. Varias filas de una máquina pueden compartir un fallo futuro; no son etiquetas independientes. Mantenimiento describe una intervención registrada para ese lote durante la semana previa, no un historial exhaustivo de todas las intervenciones de la máquina.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de lote | texto |
| `fecha` | Fecha de inicio del lote | fecha |
| `maquina` | Código de máquina | texto |
| `turno` | dia o noche | categoría |
| `unidades` | Unidades producidas | entero |
| `defectos` | Unidades defectuosas, no número de defectos individuales | entero |
| `horas` | Horas operadas en lote | real |
| `parada_min` | Minutos de parada acumulados en los siete días previos | real |
| `vibracion` | Vibración en mm/s medida antes de iniciar el lote | real |
| `mantenimiento` | 1 si hubo mantenimiento en siete días previos | booleano |
| `fallo_7d` | 1 si hay fallo en los siete días posteriores al inicio | booleano |
| `reparacion_coste` | PEN de reparación posterior, disponible después del resultado | real |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un lote producido** y qué dejaría de representar si agregas por `maquina`?
- ¿Qué significan `vibracion` y `unidades`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Promediar porcentajes de lotes sin ponderar altera el indicador global.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Contrasta recuentos y tasas; concilia defectos con unidades producidas y presenta tamaños de lote.

La pregunta y los cálculos a contrastar están delimitados. Antes de usar una biblioteca, explica sobre tres filas cómo obtendrías un resumen y qué registros no incluirías.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Registra ruta de entrada, reglas de inclusión y comprobaciones manuales. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Funciones con entradas y salidas claras; comprensiones legibles; conjuntos para categorías observadas; manejo de excepciones al convertir tipos; fechas y cadenas. Separa validación, cálculo y presentación y comprueba una función con un caso manual.

### Conceptos de Ciencia de Datos relacionados

**Proporciones ponderadas; exposición; validación cruzada.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Investiga `DataFrame` para inspeccionar columnas y `groupby` para comparar entidades; una agrupación conserva la pregunta solo si la unidad de cada fila está clara. NumPy permite calcular sobre arrays: estudia qué representa cada eje y cómo se tratan ausencias. Compara un cálculo con una función propia sobre una muestra pequeña.

### Diseño de variables

Identifica nombres para la fuente de **un lote producido**, el subconjunto elegible, la comparación por `maquina`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **defectos con tamaños de lote diferentes**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia al comparar turnos y tamaños de lote? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué turno presenta mayor proporción de unidades defectuosas?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Promediar porcentajes de lotes sin ponderar altera el indicador global.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Promediar porcentajes de lotes sin ponderar altera el indicador global.**

### Consulta recomendada

- [Tutorial de Python](https://docs.python.org/es/3/tutorial/): consulta estructuras, control de flujo, funciones, archivos y excepciones.
- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Introducción a NumPy](https://numpy.org/doc/stable/user/absolute_beginners.html): consulta arrays, ejes y operaciones numéricas.

Antes de consultar, escribe una pregunta concreta sobre **proporciones ponderadas**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión de 120–180 palabras con una cifra, su denominador o unidad, la decisión que respalda y una limitación. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Promediar porcentajes de lotes sin ponderar altera el indicador global.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Control de procesos y evaluación de mantenimiento. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

La gerencia solicita además defectos por hora de operación. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
