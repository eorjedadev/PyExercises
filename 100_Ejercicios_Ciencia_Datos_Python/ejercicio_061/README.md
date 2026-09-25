# Ejercicio 061 — Extracción analítica desde SQLite

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_060/README.md) · [Siguiente](../ejercicio_062/README.md)

### Contexto

Soporte entrega una base local en vez de archivos planos. Sector: **soporte informático**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Un reporte SQL cuenta eventos como solicitudes. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Cómo obtener una tabla analítica sin alterar el número de tickets?

### Preguntas secundarias

- ¿Qué cambia al distinguir prioridad y estado al corte?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un ticket**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/operacion.sqlite): **2,107 registros**, 8 campos. Fuente principal: un ticket.
- [eventos](datos/operacion.sqlite): **4,320 registros**, 4 campos. Historial de aperturas, cierres y reaperturas. No hay backlog anterior a la primera fecha.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

La fecha de cabecera es apertura. Los eventos tienen resolución diaria; diferencias menores a un día no se reconstruyen desde ellos. La duración en minutos viene del sistema de tickets y no mide esfuerzo efectivo. El historial registra cierres hasta 2026-01-30; aplica el corte que analices.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de ticket | texto |
| `fecha` | Fecha de apertura | fecha |
| `equipo` | Equipo responsable | texto |
| `canal` | web, correo o telefono | categoría |
| `prioridad` | alta, normal o baja | categoría |
| `minutos_resolucion` | Tiempo de calendario desde apertura a último cierre, ausente en abierto | real |
| `estado` | abierto o cerrado | categoría |
| `reabierto` | 1 si existió reapertura, 0 si no | booleano |

**eventos**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `evento_id` | Identificador de evento | texto |
| `registro_id` | Ticket al que pertenece | texto |
| `fecha_evento` | Día del cambio de estado | fecha |
| `estado_evento` | abierto o cerrado | categoría |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un ticket** y qué dejaría de representar si agregas por `equipo`?
- ¿Qué significan `minutos_resolucion` y `reabierto`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **COUNT de filas tras un join puede inflar casos; NULL no equivale a cero.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Inspecciona esquema, extrae con SQL y parámetros, valida cardinalidad de eventos y contrasta totales con una consulta independiente.

Define población, estimando, unidad independiente y supuestos antes de calcular. Distingue hallazgos exploratorios de comprobaciones previstas y evalúa sensibilidad de una decisión metodológica.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Módulos para lectura, validación y análisis; claves como tuplas cuando corresponda; context managers para archivos o conexiones; parámetros y validaciones de cardinalidad. Diseña comprobaciones de conservación de filas o importes.

### Conceptos de Ciencia de Datos relacionados

**SQL; granularidad; conciliación.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Consulta la semántica de SQL y la conexión local mediante `sqlite3`. Decide qué extraer en la base y qué analizar en Python. Usa parámetros para valores variables; inspecciona el esquema en vez de adivinar relaciones. No se proporciona la consulta.

### Diseño de variables

Identifica nombres para la fuente de **un ticket**, el subconjunto elegible, la comparación por `equipo`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **extracción analítica desde sqlite**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia al distinguir prioridad y estado al corte? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Cómo obtener una tabla analítica sin alterar el número de tickets?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- COUNT de filas tras un join puede inflar casos; NULL no equivale a cero.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **COUNT de filas tras un join puede inflar casos; NULL no equivale a cero.**

### Consulta recomendada

- [SELECT en SQLite](https://www.sqlite.org/lang_select.html): consulta selección, agrupación y semántica de uniones.
- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.

Antes de consultar, escribe una pregunta concreta sobre **sql**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **COUNT de filas tras un join puede inflar casos; NULL no equivale a cero.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Planificación de capacidad y seguimiento de solicitudes. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Reduce columnas y filas extraídas sin cambiar la población objetivo. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
