# Ejercicio 053 — Incertidumbre en tasa de defectos

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_052/README.md) · [Siguiente](../ejercicio_054/README.md)

### Contexto

Una planta debe decidir qué máquina inspeccionar. Sector: **industria**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Diferencias pequeñas de tasas se interpretan como problemas confirmados. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué diferencias son compatibles con variación entre lotes?

### Preguntas secundarias

- ¿Qué cambia al comparar turnos y tamaños de lote?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un lote producido**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **1,334 registros**, 12 campos. Fuente principal: un lote producido.
- [maquinas](datos/maquinas.csv): **6 registros**, 3 campos. Registro técnico de máquinas.

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

**maquinas**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `maquina` | Clave | texto |
| `antiguedad_anios` | Años al comienzo del período | entero |
| `familia` | Familia de equipo | categoría |

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

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Los defectos de un lote pueden depender entre sí; no simules independencia sin justificarla.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Estima diferencias de tasas con intervalos y remuestreo por lote; distingue unidad producida de lote observado.

Define población, estimando, unidad independiente y supuestos antes de calcular. Distingue hallazgos exploratorios de comprobaciones previstas y evalúa sensibilidad de una decisión metodológica.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Módulos para lectura, validación y análisis; claves como tuplas cuando corresponda; context managers para archivos o conexiones; parámetros y validaciones de cardinalidad. Diseña comprobaciones de conservación de filas o importes.

### Conceptos de Ciencia de Datos relacionados

**Bootstrap; agrupación; estimandos.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Selecciona un procedimiento estadístico a partir de la unidad independiente y del estimando, no de su disponibilidad en una biblioteca. Consulta supuestos, parámetros y significado de intervalos o contrastes; SciPy puede implementar procedimientos y NumPy las simulaciones. Debes justificar la elección.

### Diseño de variables

Identifica nombres para la fuente de **un lote producido**, el subconjunto elegible, la comparación por `maquina`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **incertidumbre en tasa de defectos**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia al comparar turnos y tamaños de lote? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué diferencias son compatibles con variación entre lotes?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Los defectos de un lote pueden depender entre sí; no simules independencia sin justificarla.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Los defectos de un lote pueden depender entre sí; no simules independencia sin justificarla.**

### Consulta recomendada

- [Estadística con SciPy](https://docs.scipy.org/doc/scipy/tutorial/stats.html): consulta distribuciones, estimación y contrastes.
- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): consulta supuestos, análisis exploratorio y diseño experimental.

Antes de consultar, escribe una pregunta concreta sobre **bootstrap**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Los defectos de un lote pueden depender entre sí; no simules independencia sin justificarla.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Control de procesos y evaluación de mantenimiento. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Compara ponderación por unidades con una pregunta sobre el lote típico. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
