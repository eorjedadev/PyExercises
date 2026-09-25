# Ejercicio 052 — Una muestra de trabajadores

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_051/README.md) · [Siguiente](../ejercicio_053/README.md)

### Contexto

Recursos humanos estudia horas de formación sin revisar todas las filas. Sector: **recursos humanos sintéticos**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Una muestra por conveniencia puede distorsionar áreas pequeñas. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Cómo difieren estimaciones obtenidas con muestreo simple y estratificado?

### Preguntas secundarias

- ¿La jornada y antigüedad explican parte de la composición de los grupos?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un trabajador ficticio en un mes**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **1,324 registros**, 9 campos. Fuente principal: un trabajador ficticio en un mes.
- [areas](datos/areas.csv): **3 registros**, 2 campos. Presupuesto no equivale a gasto ejecutado.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Los registros describen observaciones del sistema ficticio; no garantizan representar a todas las personas u operaciones fuera de él.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador ficticio de trabajador, una fila por persona | texto |
| `fecha` | Mes de referencia | fecha |
| `area` | operaciones, administracion o comercial | categoría |
| `contrato` | completo o parcial | categoría |
| `antiguedad_meses` | Meses en la empresa | entero |
| `horas` | Horas remuneradas del mes | real |
| `formacion_h` | Horas de formación del mes | real |
| `salario` | Remuneración mensual en PEN | real |
| `absentismo_dias` | Días de ausencia del mes | entero |

**areas**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `area` | Área | categoría |
| `presupuesto_formacion_pen` | Presupuesto anual de formación en PEN | real |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un trabajador ficticio en un mes** y qué dejaría de representar si agregas por `area`?
- ¿Qué significan `salario` y `formacion_h`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Muestrear filas repetidas puede contar dos veces a una persona; registra unidad de selección.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Diseña ambos muestreos desde el conjunto sintético, repite con semilla y compara distribución de estimaciones con la población suministrada.

Define población, estimando, unidad independiente y supuestos antes de calcular. Distingue hallazgos exploratorios de comprobaciones previstas y evalúa sensibilidad de una decisión metodológica.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Módulos para lectura, validación y análisis; claves como tuplas cuando corresponda; context managers para archivos o conexiones; parámetros y validaciones de cardinalidad. Diseña comprobaciones de conservación de filas o importes.

### Conceptos de Ciencia de Datos relacionados

**Muestreo; error muestral; simulación.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Selecciona un procedimiento estadístico a partir de la unidad independiente y del estimando, no de su disponibilidad en una biblioteca. Consulta supuestos, parámetros y significado de intervalos o contrastes; SciPy puede implementar procedimientos y NumPy las simulaciones. Debes justificar la elección.

### Diseño de variables

Identifica nombres para la fuente de **un trabajador ficticio en un mes**, el subconjunto elegible, la comparación por `area`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **una muestra de trabajadores**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿La jornada y antigüedad explican parte de la composición de los grupos? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Cómo difieren estimaciones obtenidas con muestreo simple y estratificado?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Muestrear filas repetidas puede contar dos veces a una persona; registra unidad de selección.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Muestrear filas repetidas puede contar dos veces a una persona; registra unidad de selección.**

### Consulta recomendada

- [Estadística con SciPy](https://docs.scipy.org/doc/scipy/tutorial/stats.html): consulta distribuciones, estimación y contrastes.
- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): consulta supuestos, análisis exploratorio y diseño experimental.

Antes de consultar, escribe una pregunta concreta sobre **muestreo**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Muestrear filas repetidas puede contar dos veces a una persona; registra unidad de selección.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Informes de personas sin atribuir causas no identificadas. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Reduce el presupuesto muestral a la mitad y compara precisión. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
