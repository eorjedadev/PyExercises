# Ejercicio 055 — Estimación de gasto típico

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_054/README.md) · [Siguiente](../ejercicio_056/README.md)

### Contexto

Administración quiere una referencia mensual de facturas. Sector: **finanzas empresariales**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

El tamaño desigual y las colas hacen inestable la media. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué estimador describe el importe y qué incertidumbre tiene?

### Preguntas secundarias

- ¿Qué diferencias dependen de moneda, categoría y fecha de pago?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **una factura**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **1,350 registros**, 8 campos. Fuente principal: una factura.
- [proveedores](datos/proveedores.csv): **12 registros**, 3 campos. Catálogo de proveedores; no infieras que R1 es mejor que R2.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Corte administrativo de estados: 2025-12-31. Una duración de seguimiento de un caso pendiente no es duración final del proceso.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de factura | texto |
| `fecha` | Fecha de emisión | fecha |
| `proveedor` | Código de proveedor | texto |
| `categoria` | material, servicio o alquiler | categoría |
| `importe` | Importe total en moneda indicada | real |
| `moneda` | PEN o USD | categoría |
| `vencimiento` | Fecha límite de pago | fecha |
| `pago` | Fecha de pago, ausente si no pagada al corte | fecha |

**proveedores**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `proveedor` | Clave | texto |
| `region` | Región | categoría |
| `categoria_riesgo` | Clasificación interna; significado operativo no documentado | categoría |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **una factura** y qué dejaría de representar si agregas por `proveedor`?
- ¿Qué significan `importe` y `moneda`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **El bootstrap empírico no descubre facturas ausentes ni gastos futuros no representados.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Trabaja dentro de una moneda; compara media y mediana con remuestreo, explica unidad de muestreo y sensibilidad a proveedores dominantes.

Define población, estimando, unidad independiente y supuestos antes de calcular. Distingue hallazgos exploratorios de comprobaciones previstas y evalúa sensibilidad de una decisión metodológica.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Módulos para lectura, validación y análisis; claves como tuplas cuando corresponda; context managers para archivos o conexiones; parámetros y validaciones de cardinalidad. Diseña comprobaciones de conservación de filas o importes.

### Conceptos de Ciencia de Datos relacionados

**Distribución muestral; bootstrap; robustez.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Selecciona un procedimiento estadístico a partir de la unidad independiente y del estimando, no de su disponibilidad en una biblioteca. Consulta supuestos, parámetros y significado de intervalos o contrastes; SciPy puede implementar procedimientos y NumPy las simulaciones. Debes justificar la elección.

### Diseño de variables

Identifica nombres para la fuente de **una factura**, el subconjunto elegible, la comparación por `proveedor`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **estimación de gasto típico**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué diferencias dependen de moneda, categoría y fecha de pago? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué estimador describe el importe y qué incertidumbre tiene?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- El bootstrap empírico no descubre facturas ausentes ni gastos futuros no representados.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **El bootstrap empírico no descubre facturas ausentes ni gastos futuros no representados.**

### Consulta recomendada

- [Estadística con SciPy](https://docs.scipy.org/doc/scipy/tutorial/stats.html): consulta distribuciones, estimación y contrastes.
- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): consulta supuestos, análisis exploratorio y diseño experimental.

Antes de consultar, escribe una pregunta concreta sobre **distribución muestral**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **El bootstrap empírico no descubre facturas ausentes ni gastos futuros no representados.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Control de gastos y seguimiento contable; no inversión financiera. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Remuestrea por proveedor y compara con remuestrear facturas. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
