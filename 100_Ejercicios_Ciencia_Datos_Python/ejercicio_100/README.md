# Ejercicio 100 — Informe final de retención

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_099/README.md)

### Contexto

Un operador ficticio reúne clientes, planes y contactos históricos. Sector: **telecomunicaciones**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Solicita una recomendación abierta sobre retención. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué se puede demostrar, qué decisión propones y qué falta conocer?

### Preguntas secundarias

- ¿Qué cambia según plan, antigüedad y fecha de observación?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un cliente y fotografía temporal**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **2,880 registros**, 10 campos. Fuente principal: un cliente y fotografía temporal.
- [planes](datos/planes.csv): **3 registros**, 3 campos. Planes vigentes para todo el período.
- [contactos](datos/contactos.csv): **595 registros**, 5 campos. Contactos seleccionados por incidencias; no aleatorizados. No se conoce aceptación.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Fotografías de contratos activos al corte; consumo e incidencias miran treinta días hacia atrás. Baja y motivo miran treinta días hacia delante, con seguimiento completado hasta 2026-01-30. Un cliente puede volver a contratar y reaparecer; estas filas no forman una cohorte de supervivencia sin reingresos. Debes separar clientes, fechas y ventanas al evaluar.

La documentación operativa es deliberadamente parcial: no se conocen criterios completos de selección ni costes de oportunidad. No inventes esos datos; declara supuestos y solicitudes de información.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de observación cliente-fecha | texto |
| `fecha` | Fecha de fotografía del cliente | fecha |
| `cliente` | Cliente ficticio, puede aparecer en distintas fotografías | texto |
| `plan` | esencial, plus o total | categoría |
| `zona` | norte, centro o sur | categoría |
| `antiguedad_meses` | Antigüedad conocida al corte | entero |
| `consumo_gb` | GB consumidos en treinta días previos | real |
| `incidencias` | Incidencias de treinta días previos | entero |
| `baja_30d` | 1 si causa baja en treinta días posteriores al corte | booleano |
| `motivo_baja` | Motivo registrado después de la baja, ausente si no hubo baja | categoría |

**planes**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `plan` | Clave de plan | categoría |
| `cuota_pen` | Cuota mensual nominal en PEN | real |
| `capacidad_gb` | Franquicia de datos en GB | real |

**contactos**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `contacto_id` | Identificador de contacto | texto |
| `cliente` | Cliente | texto |
| `fecha_contacto` | Fecha de contacto previo al corte | fecha |
| `canal` | Medio usado | categoría |
| `oferta_pen` | Descuento ofrecido en PEN, no aceptación | real |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un cliente y fotografía temporal** y qué dejaría de representar si agregas por `cliente`?
- ¿Qué significan `consumo_gb` y `incidencias`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Contactos históricos fueron selectivos; predicción de baja no estima efecto de retención.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Formula tus propias preguntas, valida fuentes y temporalidad, elige metodología y contrástala con una alternativa; entrega informe técnico, ejecutivo y plan de evaluación prospectiva.

Redacta tu propio encargo analítico: población, pregunta prioritaria, criterio de decisión y evidencia necesaria. Descubre cómo relacionar las fuentes, propone dos métodos y justifica tu elección. La respuesta puede ser pedir más información o diseñar un piloto.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Diseño de módulos y funciones a partir de responsabilidades; configuración explícita, manejo de errores y ejecución reproducible. Justifica la estructura elegida y el uso o descarte de clases; no añadas arquitectura sin una necesidad del análisis.

### Conceptos de Ciencia de Datos relacionados

**Autonomía; análisis multifuente; evidencia y límites.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Decide y justifica el conjunto mínimo de herramientas. Usa el índice de documentación para resolver dudas concretas y registra una alternativa descartada. Puedes concluir que no corresponde entrenar un modelo si la pregunta o la evidencia no lo justifican.

### Diseño de variables

Identifica nombres para la fuente de **un cliente y fotografía temporal**, el subconjunto elegible, la comparación por `cliente`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **informe final de retención**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia según plan, antigüedad y fecha de observación? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué se puede demostrar, qué decisión propones y qué falta conocer?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Contactos históricos fueron selectivos; predicción de baja no estima efecto de retención.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Contactos históricos fueron selectivos; predicción de baja no estima efecto de retención.**

### Consulta recomendada

- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): consulta supuestos, análisis exploratorio y diseño experimental.
- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/): consulta cuadernos, kernel y ejecución ordenada.

Antes de consultar, escribe una pregunta concreta sobre **autonomía**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Contactos históricos fueron selectivos; predicción de baja no estima efecto de retención.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Analítica de clientes y evaluación de decisiones de retención. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

El comité rechaza tu supuesto principal: rehace la recomendación indicando qué evidencia todavía la sostiene. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
