# Ejercicio 038 — Límites de detección

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_037/README.md) · [Siguiente](../ejercicio_039/README.md)

### Contexto

Un laboratorio analiza concentraciones sintéticas. Sector: **salud sintética y control de laboratorio**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

Las lecturas bajo el límite se tratan como ceros exactos. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué conclusiones cambian con el tratamiento de lecturas no cuantificables?

### Preguntas secundarias

- ¿Cuántas muestras independientes respaldan cada resumen?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **una réplica de muestra e instrumento**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **541 registros**, 9 campos. Fuente principal: una réplica de muestra e instrumento.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Muestras enteramente sintéticas de un laboratorio docente de control sanitario, sin pacientes. Cada muestra prevé tres réplicas por instrumento A y B. Los límites son analíticos, no umbrales clínicos; no corresponde diagnosticar ni recomendar tratamientos.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de medición | texto |
| `fecha` | Fecha de ensayo | fecha |
| `muestra` | Código de muestra sintética sin datos personales | texto |
| `replica` | Repetición técnica dentro de muestra e instrumento | entero |
| `instrumento` | Instrumento A o B | texto |
| `concentracion` | Concentración en mg/L, ausente si no cuantificable | real |
| `limite` | Límite inferior de cuantificación en mg/L | real |
| `bajo_limite` | 1 si lectura inferior al límite | booleano |
| `unidad` | mg/L | categoría |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **una réplica de muestra e instrumento** y qué dejaría de representar si agregas por `muestra`?
- ¿Qué significan `concentracion` y `limite`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **La sustitución no recupera mediciones ausentes; censura no es valor perdido ordinario.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Distingue resultado cuantificable y bajo límite; compara escenarios de 0, mitad del límite y límite, sin afirmar valores verdaderos.

La pregunta está delimitada, pero debes elegir transformaciones, métricas y representación. Compara al menos dos decisiones plausibles de preparación y explica si alteran el mensaje.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Funciones reutilizables con nombres que expliquen su intención; parámetros para filtros y umbrales; rutas con pathlib, fechas, excepciones específicas y módulos. Evita capturar cualquier excepción y continuar silenciosamente.

### Conceptos de Ciencia de Datos relacionados

**Censura de medición; sensibilidad; incertidumbre.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Elige las operaciones de selección, transformación y resumen que respondan al encargo. Revisa en la documentación sus supuestos sobre tipos, valores ausentes e índices. Justifica cuándo una operación vectorizada aporta claridad respecto a un ciclo. No se prescribe un gráfico ni una cadena de métodos.

### Diseño de variables

Identifica nombres para la fuente de **una réplica de muestra e instrumento**, el subconjunto elegible, la comparación por `muestra`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **límites de detección**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Cuántas muestras independientes respaldan cada resumen? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué conclusiones cambian con el tratamiento de lecturas no cuantificables?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- La sustitución no recupera mediciones ausentes; censura no es valor perdido ordinario.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **La sustitución no recupera mediciones ausentes; censura no es valor perdido ordinario.**

### Consulta recomendada

- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Guía de Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html): consulta figura, ejes y representación de variables.
- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): consulta supuestos, análisis exploratorio y diseño experimental.

Antes de consultar, escribe una pregunta concreta sobre **censura de medición**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión técnica de 180–250 palabras y una ejecutiva de 80–120. Ambas deben expresar la misma evidencia: métrica con unidad o denominador, incertidumbre pertinente, decisión propuesta y límite principal. Evita vocabulario técnico innecesario en la segunda. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **La sustitución no recupera mediciones ausentes; censura no es valor perdido ordinario.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Control de medición en laboratorios docentes; sin interpretación clínica. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Resume por instrumento y evalúa si sus límites son comparables. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
