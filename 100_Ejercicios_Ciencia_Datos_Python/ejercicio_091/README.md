# Ejercicio 091 — Reorganización de una mesa de ayuda

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_090/README.md) · [Siguiente](../ejercicio_092/README.md)

### Contexto

La gerencia quiere cambiar la distribución de equipos. Sector: **soporte informático**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Tickets, eventos y capacidad de equipos no ofrecen una explicación única. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué reorganización merece un piloto y qué evidencia la sustenta?

### Preguntas secundarias

- ¿Qué cambia al distinguir prioridad y estado al corte?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un ticket**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **4,515 registros**, 8 campos. Fuente principal: un ticket.
- [eventos](datos/eventos.csv): **9,229 registros**, 4 campos. Historial de aperturas, cierres y reaperturas. No hay backlog anterior a la primera fecha.
- [equipos](datos/equipos.csv): **3 registros**, 3 campos. Dotación constante; no mide esfuerzo por ticket.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

La fecha de cabecera es apertura. Los eventos tienen resolución diaria; diferencias menores a un día no se reconstruyen desde ellos. La duración en minutos viene del sistema de tickets y no mide esfuerzo efectivo. El historial registra cierres hasta 2026-01-30; aplica el corte que analices.

La documentación operativa es deliberadamente parcial: no se conocen criterios completos de selección ni costes de oportunidad. No inventes esos datos; declara supuestos y solicitudes de información.

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

**equipos**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `equipo` | Equipo | texto |
| `personas` | Dotación | entero |
| `horas_semana` | Capacidad nominal semanal en horas | entero |

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

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Tiempo de resolución no equivale a esfuerzo; productividad aparente depende de complejidad.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Define demanda, servicio y backlog, elige ventanas y segmentos, contrasta hipótesis rivales y diseña indicadores de seguimiento del piloto.

Redacta tu propio encargo analítico: población, pregunta prioritaria, criterio de decisión y evidencia necesaria. Descubre cómo relacionar las fuentes, propone dos métodos y justifica tu elección. La respuesta puede ser pedir más información o diseñar un piloto.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Diseño de módulos y funciones a partir de responsabilidades; configuración explícita, manejo de errores y ejecución reproducible. Justifica la estructura elegida y el uso o descarte de clases; no añadas arquitectura sin una necesidad del análisis.

### Conceptos de Ciencia de Datos relacionados

**Diagnóstico operacional; hipótesis rivales; diseño de evaluación.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Decide y justifica el conjunto mínimo de herramientas. Usa el índice de documentación para resolver dudas concretas y registra una alternativa descartada. Puedes concluir que no corresponde entrenar un modelo si la pregunta o la evidencia no lo justifican.

### Diseño de variables

Identifica nombres para la fuente de **un ticket**, el subconjunto elegible, la comparación por `equipo`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **reorganización de una mesa de ayuda**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia al distinguir prioridad y estado al corte? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué reorganización merece un piloto y qué evidencia la sustenta?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Tiempo de resolución no equivale a esfuerzo; productividad aparente depende de complejidad.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Tiempo de resolución no equivale a esfuerzo; productividad aparente depende de complejidad.**

### Consulta recomendada

- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): consulta supuestos, análisis exploratorio y diseño experimental.
- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/): consulta cuadernos, kernel y ejecución ordenada.

Antes de consultar, escribe una pregunta concreta sobre **diagnóstico operacional**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Tiempo de resolución no equivale a esfuerzo; productividad aparente depende de complejidad.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Planificación de capacidad y seguimiento de solicitudes. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

La capacidad total no puede aumentar: declara compromisos entre indicadores. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
