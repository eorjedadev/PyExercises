# Ejercicio 087 — Probabilidades y calibración

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_086/README.md) · [Siguiente](../ejercicio_088/README.md)

### Contexto

Una cadena usa probabilidades de cancelación para planificar. Sector: **turismo**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Una buena clasificación no garantiza probabilidades fiables. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿La frecuencia observada coincide con las probabilidades estimadas?

### Preguntas secundarias

- ¿Los canales tienen la misma anticipación y composición de hoteles?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **una reserva**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **3,010 registros**, 9 campos. Fuente principal: una reserva.
- [hoteles](datos/hoteles.csv): **3 registros**, 3 campos. Catálogo hotelero constante.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Las reservas se registran durante la cobertura indicada y pueden llegar hasta 150 días después. Se completó seguimiento de cancelación hasta 2026-05-30. El dataset no confirma check-in ni ocupación real. Para simular cortes históricos, no uses resultados que aún no se conocerían.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de reserva | texto |
| `fecha_reserva` | Fecha en que se hizo la reserva | fecha |
| `fecha_llegada` | Fecha prevista de llegada | fecha |
| `hotel` | Hotel reservado | texto |
| `canal` | directo, agencia o plataforma | categoría |
| `noches` | Noches reservadas | entero |
| `tarifa` | Precio por noche en PEN | real |
| `cancelada` | 1 si cancelada antes de llegada, resultado posterior a reserva | booleano |
| `pais` | País de origen ficticio | categoría |

**hoteles**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `hotel` | Clave | texto |
| `zona` | Ubicación ficticia | categoría |
| `habitaciones` | Capacidad nominal, no ocupación realizada | entero |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **una reserva** y qué dejaría de representar si agregas por `hotel`?
- ¿Qué significan `tarifa` y `noches`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Un grupo pequeño puede aparentar mala calibración por ruido; no calibrar con test.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Reserva evaluación temporal, compara discriminación y calibración con grupos de probabilidad y Brier score; analiza tamaños por grupo.

Antes de entrenar, escribe una ficha con objetivo, horizonte, información disponible, baseline, particiones y métrica. Justifica generalización y coste de errores; conserva una evaluación final sin usar para ajustar decisiones.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Funciones de transformación con contratos; separación entre configuración y ejecución; semillas en simulaciones; validaciones temporales y registro de versiones. Una clase solo aporta valor si encapsula estado y responsabilidades que una función no expresa bien.

### Conceptos de Ciencia de Datos relacionados

**Calibración; Brier score; incertidumbre.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Elige el método después de definir objetivo, momento de uso y evaluación. Consulta en scikit-learn las hipótesis del estimador, las particiones y la preparación de datos. Un modelo más complejo debe justificar su utilidad frente a una referencia reproducible; no se prescribe una secuencia de llamadas.

### Diseño de variables

Identifica nombres para la fuente de **una reserva**, el subconjunto elegible, la comparación por `hotel`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **probabilidades y calibración**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Los canales tienen la misma anticipación y composición de hoteles? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿La frecuencia observada coincide con las probabilidades estimadas?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Un grupo pequeño puede aparentar mala calibración por ruido; no calibrar con test.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Un grupo pequeño puede aparentar mala calibración por ruido; no calibrar con test.**

### Consulta recomendada

- [Evaluación en scikit-learn](https://scikit-learn.org/stable/model_selection.html): consulta particiones, validación y selección de métricas.
- [Errores habituales en scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html): consulta fuga de datos y preparación consistente.

Antes de consultar, escribe una pregunta concreta sobre **calibración**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Un grupo pequeño puede aparentar mala calibración por ruido; no calibrar con test.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Planificación de reservas y comunicación de incertidumbre. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Compara utilidad de probabilidades frente a decisiones binarias con costes explícitos. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
