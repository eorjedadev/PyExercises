# Ejercicio 093 — Abastecimiento con presupuesto limitado

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_092/README.md) · [Siguiente](../ejercicio_094/README.md)

### Contexto

Una empresa reúne inventario, catálogo y pedidos a proveedores. Sector: **inventarios**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Se necesitan prioridades sin una medida única de riesgo. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué revisión de abastecimiento priorizarías y con qué sensibilidad?

### Preguntas secundarias

- ¿Qué días y almacenes quedan representados en la comparación?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un producto-almacén-fecha**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **4,515 registros**, 9 campos. Fuente principal: un producto-almacén-fecha.
- [productos](datos/productos.csv): **12 registros**, 4 campos. Catálogo vigente para todo el período.
- [pedidos](datos/pedidos.csv): **300 registros**, 6 campos. Pedidos históricos; no representan demanda final de clientes.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Son observaciones muestreadas de inventario, no un libro completo de movimientos. Saldo es inicial, demanda y reposición se observan durante el día; no se conoce toda demanda perdida ni se impone conservación entre días no observados.

La documentación operativa es deliberadamente parcial: no se conocen criterios completos de selección ni costes de oportunidad. No inventes esos datos; declara supuestos y solicitudes de información.

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

**pedidos**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `pedido_id` | Pedido de abastecimiento | texto |
| `producto` | Producto | texto |
| `almacen` | Destino | texto |
| `fecha_pedido` | Fecha de emisión | fecha |
| `unidades_pedidas` | Cantidad contratada | entero |
| `demora_dias` | Plazo hasta recepción observada | entero |

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

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **No hay demanda no atendida completa; una recomendación no es política óptima demostrada.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Define riesgo y unidad de análisis, relaciona fuentes sin duplicar stock, compara escenarios de demanda y entrega y justifica una cartera de revisión.

Redacta tu propio encargo analítico: población, pregunta prioritaria, criterio de decisión y evidencia necesaria. Descubre cómo relacionar las fuentes, propone dos métodos y justifica tu elección. La respuesta puede ser pedir más información o diseñar un piloto.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Diseño de módulos y funciones a partir de responsabilidades; configuración explícita, manejo de errores y ejecución reproducible. Justifica la estructura elegida y el uso o descarte de clases; no añadas arquitectura sin una necesidad del análisis.

### Conceptos de Ciencia de Datos relacionados

**Escenarios; inventario; integración y decisión.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Decide y justifica el conjunto mínimo de herramientas. Usa el índice de documentación para resolver dudas concretas y registra una alternativa descartada. Puedes concluir que no corresponde entrenar un modelo si la pregunta o la evidencia no lo justifican.

### Diseño de variables

Identifica nombres para la fuente de **un producto-almacén-fecha**, el subconjunto elegible, la comparación por `producto`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **abastecimiento con presupuesto limitado**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué días y almacenes quedan representados en la comparación? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué revisión de abastecimiento priorizarías y con qué sensibilidad?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- No hay demanda no atendida completa; una recomendación no es política óptima demostrada.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **No hay demanda no atendida completa; una recomendación no es política óptima demostrada.**

### Consulta recomendada

- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): consulta supuestos, análisis exploratorio y diseño experimental.
- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/): consulta cuadernos, kernel y ejecución ordenada.

Antes de consultar, escribe una pregunta concreta sobre **escenarios**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **No hay demanda no atendida completa; una recomendación no es política óptima demostrada.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Revisión de abastecimiento y cobertura de demanda. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Introduce una demora adicional de siete días y explica qué prioridades cambian. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
