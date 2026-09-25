# Ejercicio 045 — Inventario con catálogo de productos

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_044/README.md) · [Siguiente](../ejercicio_046/README.md)

### Contexto

Un almacén cruza saldos y clasificación de productos. Sector: **inventarios**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

La priorización desconoce el valor y plazo de reposición. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Dónde se combinan cobertura insuficiente y mayor exposición económica?

### Preguntas secundarias

- ¿Qué días y almacenes quedan representados en la comparación?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un producto-almacén-fecha**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **1,250 registros**, 9 campos. Fuente principal: un producto-almacén-fecha.
- [productos](datos/productos.csv): **12 registros**, 4 campos. Catálogo vigente para todo el período.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Son observaciones muestreadas de inventario, no un libro completo de movimientos. Saldo es inicial, demanda y reposición se observan durante el día; no se conoce toda demanda perdida ni se impone conservación entre días no observados.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de instantánea | texto |
| `fecha` | Día de observación al inicio de jornada | fecha |
| `almacen` | Almacén | categoría |
| `producto` | Código de producto | texto |
| `saldo` | Unidades disponibles al inicio | entero |
| `demanda` | Unidades solicitadas durante ese día | entero |
| `reposicion` | Unidades recibidas durante el día | entero |
| `plazo_dias` | Plazo contractual de reposición en días | entero |
| `coste_unitario` | Coste unitario de referencia en PEN | real |

**productos**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `producto` | Clave de producto | texto |
| `familia` | Familia comercial | categoría |
| `coste_referencia` | PEN por unidad, fijo en el período, sin costes indirectos | real |
| `plazo_catalogo` | Días de reposición contractual | entero |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un producto-almacén-fecha** y qué dejaría de representar si agregas por `producto`?
- ¿Qué significan `saldo` y `demanda`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **No multiplicar saldos al unir días de demanda; demanda observada no es demanda perdida.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Relaciona claves compuestas y catálogo; compara demanda, saldo, coste y plazo; revisa integridad y ausencia de catálogo.

La pregunta está delimitada, pero debes elegir transformaciones, métricas y representación. Compara al menos dos decisiones plausibles de preparación y explica si alteran el mensaje.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Módulos para lectura, validación y análisis; claves como tuplas cuando corresponda; context managers para archivos o conexiones; parámetros y validaciones de cardinalidad. Diseña comprobaciones de conservación de filas o importes.

### Conceptos de Ciencia de Datos relacionados

**Claves compuestas; riesgo operativo; priorización.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Investiga cardinalidad y validación de uniones antes de combinar fuentes. Decide el tipo de unión según la población que quieres conservar. Organiza un notebook con contexto, código propio, resultados e interpretación, o un script con informe equivalente.

### Diseño de variables

Identifica nombres para la fuente de **un producto-almacén-fecha**, el subconjunto elegible, la comparación por `producto`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **inventario con catálogo de productos**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué días y almacenes quedan representados en la comparación? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Dónde se combinan cobertura insuficiente y mayor exposición económica?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- No multiplicar saldos al unir días de demanda; demanda observada no es demanda perdida.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **No multiplicar saldos al unir días de demanda; demanda observada no es demanda perdida.**

### Consulta recomendada

- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/): consulta cuadernos, kernel y ejecución ordenada.

Antes de consultar, escribe una pregunta concreta sobre **claves compuestas**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **No multiplicar saldos al unir días de demanda; demanda observada no es demanda perdida.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Revisión de abastecimiento y cobertura de demanda. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Propón una prioridad si el presupuesto de revisión permite solo cinco productos. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
