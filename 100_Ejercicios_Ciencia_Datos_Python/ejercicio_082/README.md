# Ejercicio 082 — Complejidad y sobreajuste

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_081/README.md) · [Siguiente](../ejercicio_083/README.md)

### Contexto

Logística compara modelos de distinta flexibilidad. Sector: **transporte y logística**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Se escoge el modelo con menor error de entrenamiento. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué complejidad generaliza mejor a entregas posteriores?

### Preguntas secundarias

- ¿El patrón se mantiene en rutas de distinta distancia y carga?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un envío**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **3,010 registros**, 9 campos. Fuente principal: un envío.
- [transportistas](datos/transportistas.csv): **3 registros**, 3 campos. Tarifas de contrato constantes, aplicables al despacho, sin recargos.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Corte administrativo de estados: 2025-12-31. Una duración de seguimiento de un caso pendiente no es duración final del proceso.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de envío | texto |
| `fecha` | Fecha de despacho | fecha |
| `ruta` | Código de ruta | texto |
| `transportista` | Código del operador | texto |
| `distancia_km` | Distancia planificada en km | real |
| `carga_kg` | Carga al despacho en kg | real |
| `tiempo_min` | Duración hasta entrega en minutos, ausente en pendiente | real |
| `prometido_min` | Compromiso al despacho en minutos | real |
| `entregado` | 1 si entrega completada al corte | booleano |

**transportistas**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `transportista` | Clave del operador | texto |
| `fijo_pen` | PEN por envío despachado | real |
| `pen_km` | PEN por km planificado | real |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un envío** y qué dejaría de representar si agregas por `transportista`?
- ¿Qué significan `tiempo_min` y `distancia_km`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Ajustar decisiones mirando el test lo convierte en validación.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Compara regresión y árbol con capacidad variable, validación temporal y baseline; reporta errores de entrenamiento, validación y una evaluación final reservada.

Antes de entrenar, escribe una ficha con objetivo, horizonte, información disponible, baseline, particiones y métrica. Justifica generalización y coste de errores; conserva una evaluación final sin usar para ajustar decisiones.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Funciones de transformación con contratos; separación entre configuración y ejecución; semillas en simulaciones; validaciones temporales y registro de versiones. Una clase solo aporta valor si encapsula estado y responsabilidades que una función no expresa bien.

### Conceptos de Ciencia de Datos relacionados

**Overfitting; curvas de aprendizaje; selección.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Elige el método después de definir objetivo, momento de uso y evaluación. Consulta en scikit-learn las hipótesis del estimador, las particiones y la preparación de datos. Un modelo más complejo debe justificar su utilidad frente a una referencia reproducible; no se prescribe una secuencia de llamadas.

### Diseño de variables

Identifica nombres para la fuente de **un envío**, el subconjunto elegible, la comparación por `transportista`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **complejidad y sobreajuste**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿El patrón se mantiene en rutas de distinta distancia y carga? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué complejidad generaliza mejor a entregas posteriores?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Ajustar decisiones mirando el test lo convierte en validación.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Ajustar decisiones mirando el test lo convierte en validación.**

### Consulta recomendada

- [Evaluación en scikit-learn](https://scikit-learn.org/stable/model_selection.html): consulta particiones, validación y selección de métricas.
- [Errores habituales en scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html): consulta fuga de datos y preparación consistente.

Antes de consultar, escribe una pregunta concreta sobre **overfitting**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Ajustar decisiones mirando el test lo convierte en validación.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Contratos de servicio y planificación de entregas. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Reduce a la mitad el entrenamiento y compara la brecha de errores. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
