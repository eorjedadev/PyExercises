# Ejercicio 077 — Predecir consumo sin mirar el futuro

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_076/README.md) · [Siguiente](../ejercicio_078/README.md)

### Contexto

Una administración planifica consumo diario. Sector: **energía**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Se propone usar temperatura observada del día que se intenta predecir. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué predicción es evaluable al cierre del día anterior?

### Preguntas secundarias

- ¿Qué cambia al considerar ocupación, clima y superficie?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un edificio y día**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **2,158 registros**, 8 campos. Fuente principal: un edificio y día.
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

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Temperatura realizada no es pronóstico; ajustar escalas con todo el período filtra futuro.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Define información disponible, crea características retrasadas por edificio y compara baseline semanal y regresión con corte temporal.

Antes de entrenar, escribe una ficha con objetivo, horizonte, información disponible, baseline, particiones y métrica. Justifica generalización y coste de errores; conserva una evaluación final sin usar para ajustar decisiones.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Funciones de transformación con contratos; separación entre configuración y ejecución; semillas en simulaciones; validaciones temporales y registro de versiones. Una clase solo aporta valor si encapsula estado y responsabilidades que una función no expresa bien.

### Conceptos de Ciencia de Datos relacionados

**Características temporales; fuga; validación temporal.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Elige el método después de definir objetivo, momento de uso y evaluación. Consulta en scikit-learn las hipótesis del estimador, las particiones y la preparación de datos. Un modelo más complejo debe justificar su utilidad frente a una referencia reproducible; no se prescribe una secuencia de llamadas.

### Diseño de variables

Identifica nombres para la fuente de **un edificio y día**, el subconjunto elegible, la comparación por `edificio`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **predecir consumo sin mirar el futuro**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia al considerar ocupación, clima y superficie? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué predicción es evaluable al cierre del día anterior?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Temperatura realizada no es pronóstico; ajustar escalas con todo el período filtra futuro.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Temperatura realizada no es pronóstico; ajustar escalas con todo el período filtra futuro.**

### Consulta recomendada

- [Evaluación en scikit-learn](https://scikit-learn.org/stable/model_selection.html): consulta particiones, validación y selección de métricas.
- [Errores habituales en scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html): consulta fuga de datos y preparación consistente.

Antes de consultar, escribe una pregunta concreta sobre **características temporales**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Temperatura realizada no es pronóstico; ajustar escalas con todo el período filtra futuro.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Auditoría de consumo y planificación de recursos. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Compara escenarios con y sin un pronóstico hipotético, etiquetándolo como tal. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
