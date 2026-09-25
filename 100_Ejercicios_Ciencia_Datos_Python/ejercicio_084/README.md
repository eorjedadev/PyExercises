# Ejercicio 084 — Segmentos de comportamiento

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_083/README.md) · [Siguiente](../ejercicio_085/README.md)

### Contexto

Una plataforma quiere describir patrones de uso. Sector: **desarrollo web y comercio electrónico**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Se solicita segmentar usuarios sin una variable objetivo. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué agrupaciones son estables y útiles para describir comportamiento?

### Preguntas secundarias

- ¿Qué cambia al distinguir sesiones de usuarios y al comparar dispositivos?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **una sesión**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.json): **3,010 registros**, 12 campos. Fuente principal: una sesión.
- [usuarios](datos/usuarios.csv): **600 registros**, 3 campos. Perfiles registrados antes o en la primera sesión observada.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Los registros describen observaciones del sistema ficticio; no garantizan representar a todas las personas u operaciones fuera de él.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de sesión | texto |
| `fecha` | Fecha de inicio de sesión | fecha |
| `usuario` | Identificador ficticio, puede repetirse | texto |
| `canal` | organico, anuncio o referido | categoría |
| `dispositivo` | movil o escritorio | categoría |
| `variante` | Versión A o B observada, sin asignación experimental garantizada | categoría |
| `visita` | 1 si sesión registrada | booleano |
| `carrito` | 1 si añadió al carrito | booleano |
| `compra` | 1 si compró en sesión | booleano |
| `ingreso` | Ingreso de la sesión en PEN | real |
| `duracion_seg` | Duración de sesión en segundos | real |
| `campana_id` | Campaña de entrada o ninguna | texto |

**usuarios**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `usuario` | Clave de usuario | texto |
| `alta` | Fecha de registro | fecha |
| `pais` | País ficticio | categoría |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **una sesión** y qué dejaría de representar si agregas por `usuario`?
- ¿Qué significan `ingreso` y `duracion_seg`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Identificadores no son características numéricas; silhouette no prueba valor comercial.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Agrega a usuario, justifica características y escala, compara agrupamientos y estabilidad entre semillas; interpreta perfiles y tamaños.

Antes de entrenar, escribe una ficha con objetivo, horizonte, información disponible, baseline, particiones y métrica. Justifica generalización y coste de errores; conserva una evaluación final sin usar para ajustar decisiones.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Funciones de transformación con contratos; separación entre configuración y ejecución; semillas en simulaciones; validaciones temporales y registro de versiones. Una clase solo aporta valor si encapsula estado y responsabilidades que una función no expresa bien.

### Conceptos de Ciencia de Datos relacionados

**Clustering; escalado; estabilidad.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Elige el método después de definir objetivo, momento de uso y evaluación. Consulta en scikit-learn las hipótesis del estimador, las particiones y la preparación de datos. Un modelo más complejo debe justificar su utilidad frente a una referencia reproducible; no se prescribe una secuencia de llamadas.

### Diseño de variables

Identifica nombres para la fuente de **una sesión**, el subconjunto elegible, la comparación por `usuario`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **segmentos de comportamiento**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué cambia al distinguir sesiones de usuarios y al comparar dispositivos? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué agrupaciones son estables y útiles para describir comportamiento?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Identificadores no son características numéricas; silhouette no prueba valor comercial.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Identificadores no son características numéricas; silhouette no prueba valor comercial.**

### Consulta recomendada

- [Clustering en scikit-learn](https://scikit-learn.org/stable/modules/clustering.html): consulta supuestos y criterios de agrupación.
- [Errores habituales en scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html): consulta fuga de datos y preparación consistente.

Antes de consultar, escribe una pregunta concreta sobre **clustering**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Identificadores no son características numéricas; silhouette no prueba valor comercial.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Analítica de producto, embudos y comportamiento digital. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Repite con otra ventana y evalúa estabilidad de perfiles sin exigir etiquetas idénticas. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
