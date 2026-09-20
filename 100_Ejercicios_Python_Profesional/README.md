# 100 ejercicios de razonamiento profesional con Python

Esta colección propone **100 entrenamientos integradores**, sin soluciones. El propósito es aprender a interpretar necesidades, diseñar, implementar, probar, leer y explicar código, y adaptarlo cuando cambian las reglas. Terminar cien programas no sustituye comprenderlos.

Cada ejercicio reúne varios fundamentos en un contexto concreto. No hay bloques de sintaxis aislada ni etiquetas de nivel. La cantidad de decisiones, la responsabilidad sobre los datos y la autonomía aumentan progresivamente.

## Cómo trabajar cada ejercicio

Sigue el ciclo **Comprender → interpretar → diseñar → implementar → probar → explicar → mejorar**:

1. **Comprender:** explica con tus palabras quién necesita el resultado y qué problema tiene. Distingue el contexto del contrato exigido.
2. **Interpretar:** anota entradas, unidades, salidas, restricciones, errores y casos límite. Distingue dato ausente, cero, vacío e inválido. Si algo parece contradictorio, registra la duda antes de programar.
3. **Diseñar:** prepara dos o tres ejemplos a mano. Esboza responsabilidades, representaciones e invariantes, sin traducir todavía cada frase a código. Propón nombres y justifica su intención.
4. **Implementar:** construye tu solución con el alcance del enunciado. No añadas menús, bases de datos, redes, clases o dependencias si no responden a una necesidad concreta.
5. **Probar:** escribe los resultados esperados antes de ejecutar. Comprueba ejemplos, fronteras, rechazos y efectos sobre datos o archivos. Añade al menos un caso propio que pueda refutar tu diseño.
6. **Explicar:** recorre un caso leyendo tu código. Explica decisiones, nombres, validaciones y limitaciones. Contrasta tus predicciones con lo que realmente sucede.
7. **Mejorar:** cambia un nombre, elimina una responsabilidad mezclada o aplica el reto opcional. Repite las pruebas afectadas y explica por qué la modificación conserva o cambia el contrato.

Antes de comenzar, debes poder responder: ¿qué problema resuelvo?, ¿qué recibo?, ¿qué produzco?, ¿qué reglas existen?, ¿qué casos especiales hay?, ¿qué herramientas podrían ayudar?, ¿cómo dividir responsabilidades?, ¿cómo comprobarlo?, ¿cómo hacerlo legible? y ¿cómo explicarlo a otra persona?

Guarda tus implementaciones en una carpeta propia separada de estos enunciados, por ejemplo `mis_practicas/ejercicio_001/`. Allí puedes mantener código, pruebas, datos sintéticos y notas. La colección distribuida solo contiene Markdown: no hay archivos que resuelvan los problemas.

<a id="convenciones-comunes"></a>
## Convenciones comunes

Estas convenciones completan los contratos; una regla explícita de un ejercicio tiene prioridad:

- Usa Python 3 y biblioteca estándar. No hace falta instalar paquetes. Para automatizar pruebas puedes usar `unittest` o aserciones en un entorno controlado; no uses `assert` como validación de entradas de producción. Las referencias a `pytest` son alternativas de estudio.
- Los datos en memoria pueden prepararse directamente como valores de Python. No se exige consola interactiva salvo que se pida. Si añades consola, separa sus conversiones y mensajes de las reglas del dominio.
- Los campos mencionados son obligatorios salvo que se indique que son opcionales. Un campo extra no participa en el cálculo salvo que el contrato lo rechace explícitamente. Elige y documenta tu forma concreta de representar registros, sin cambiar sus significados.
- Un entero excluye booleanos. Las cantidades numéricas excluyen NaN e infinitos. No conviertas silenciosamente texto en número salvo en fronteras que reciben texto, CSV, JSON o entrada de consola. Un número decimal no es un entero por contener `.0`.
- Un texto es sensible a mayúsculas y conserva espacios salvo que se indique normalización. Los identificadores son textos no vacíos; no inventes equivalencias. Un orden alfabético o lexicográfico corresponde al orden de cadenas de Python, sin adaptación regional. Los empates adicionales deben seguir el contrato del ejercicio.
- No inventes reglas fiscales, legales, de seguridad o de autenticación. Los importes y las políticas de negocio son simulaciones pedagógicas cerradas. Mantén las unidades indicadas: céntimos, minutos, segundos, bytes o unidades.
- Si no se especifica otra política, una entrada fuera del tipo, rango o estructura declarados rechaza la unidad de trabajo completa con causa identificable y sin efectos. Cuando se pide rechazar filas, continuar o devolver resultados parciales, aplica esa política específica y haz visible que el resultado es parcial.
- No hay correcciones automáticas fuera de las normalizaciones expresas. El cero, la ausencia y una cadena vacía no son equivalentes. Si el enunciado no permite una entrada vacía y no puede satisfacer su contrato, se rechaza; si permite una colección vacía, debe poder producir el resultado vacío correspondiente.
- Las entradas son de solo lectura salvo que el contrato pida cambios. Si devuelves un nuevo estado independiente, evita compartir partes mutables que permitan alterar el original desde el resultado.
- Las pruebas son independientes: cada una prepara un estado inicial limpio, salvo que describa expresamente una secuencia de operaciones. Si se reutiliza un conjunto de datos de otro caso, vuelve a prepararlo. Una flecha indica entrada y resultado observable, no un algoritmo. Las abreviaturas de registros se interpretan según «Datos de entrada». Cuando se destaca solo un campo o frontera, completa los demás con valores válidos de tu elección: la decisión indicada no debe depender de ellos.
- Fechas ISO usan el calendario de `datetime`; los ejercicios con instantes enteros usan un reloj simulado y la unidad indicada. No dependas de la fecha actual, de esperas reales ni de servicios externos.
- Crea tú los archivos de prueba a partir de los casos mínimos en una carpeta temporal de práctica. El formato textual es UTF-8 salvo que se indique contenido binario. No trabajes sobre archivos personales. Para simular fallos, sustituye la dependencia de lectura o escritura en la prueba; no hace falta alterar permisos del equipo.
- El texto exacto de un mensaje es libre, pero el resultado debe distinguir éxito, ausencia, rechazo y fallo operativo cuando corresponda. Documenta la interfaz elegida y haz que las pruebas la comprueben.

## Progresión y recuperación de conocimientos

La progresión completa se diseñó antes de generar los archivos. Cada tramo incorpora responsabilidades nuevas y conserva las anteriores; los fundamentos se mezclan en todos ellos.

| Recorrido | Decisiones que se incorporan | Evidencia para continuar |
| --- | --- | --- |
| 001–010 | Interpretación, unidades, fronteras, texto y primeras colecciones | Explicar entradas y salidas, predecir un rechazo y elegir nombres comprensibles |
| 011–020 | Reglas que compiten, identidad, acumulación y cambios sucesivos | Justificar prioridades, igualdad y qué cambia después de cada operación |
| 021–030 | Funciones, agregación, orden, ausencias y comparaciones | Separar cálculo y presentación; probar vacíos, ceros, empates y orden |
| 031–040 | Relaciones, intervalos, recorridos, colas y permisos conceptuales | Representar vínculos y explicar invariantes sin depender de un caso feliz |
| 041–050 | Archivos, formatos, errores, fechas y persistencia | Distinguir error global y registro rechazado; conservar evidencia y unidades |
| 051–060 | Organización, migración, propiedad de datos y objetos con responsabilidad | Proteger contratos y demostrar independencia de estado e integridad |
| 061–070 | Servicios simulados, tiempo controlado, procesamiento incremental y combinación de cambios | Elegir representaciones y dependencias comprobables con menos pistas |
| 071–080 | Dependencias, políticas de selección, refactorización y propiedades | Defender decisiones, reconocer límites y leer código antes de modificarlo |
| 081–090 | Vistas previas, reanudación, coherencia, expiración y reproducibilidad | Explicar qué se confirma, cuándo y qué se conserva ante un fallo |
| 091–100 | Compatibilidad, almacenamiento intercambiable, fallos inyectados e integración acotada | Modificar sin regresiones, probar contratos entre componentes y entregar algo mantenible |

Las referencias cruzadas de «Antes de programar» recuperan mecanismos ya practicados. Antes de copiar código, compara los contratos: que dos problemas compartan un patrón no significa que acepten los mismos datos o tengan idéntica política de error. Los ejercicios 076, 077, 078, 091 y 093 piden revisar expresamente implementaciones tuyas anteriores. Si llegaste directamente a uno de ellos, completa primero su antecedente.

Las clases aparecen cuando ayudan a proteger estado, el tiempo se introduce como dato para poder probarlo y las integraciones son locales. Los últimos problemas aumentan decisiones y posibilidades de fallo, no exigen una aplicación de tamaño artificial.

## Uso de la biblioteca técnica

Se revisaron los índices, la organización y secciones pertinentes de los cinco documentos disponibles. Son material de consulta, no requisitos externos ni respuestas a estos ejercicios:

| Documento local | Para qué consultarlo |
| --- | --- |
| [Universidad Python](../Universidad_Python.md) | Conceptos, colecciones, funciones, errores, archivos, organización y objetos; buscar el encabezado indicado en cada ejercicio |
| [Diccionario Python](../Diccionario_Python.md) | Significado de métodos y funciones, palabras clave, módulos y vocabulario de razonamiento |
| [Guía de Matthes](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md) | Capítulos 8, 10 y 11 para funciones, persistencia, excepciones y pruebas; es una guía de repaso local |
| [Notas para profesionales](../NotasdePythonparaprofesionales.md) | Consultas puntuales, especialmente fechas y JSON; incluye material histórico y referencias a Python 2 que no debes trasladar sin revisión |
| [Guía de Ramalho](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md) | Texto Unicode, referencias y mutabilidad, objetos e iteración incremental; es una guía de estudio, no el libro completo |

Los enlaces señalan archivos reales y, cuando el formato lo permite, secciones verificadas. Algunas notas usan anclas extendidas que no todos los visores reconocen: por eso se proporciona el título exacto para buscarlo dentro del archivo. Si una entrada de módulo es breve, úsala para ubicar el concepto y explora su ayuda local; no asumas que la guía desarrolla cada detalle del ejercicio.

Antes de consultar, escribe una duda específica: «¿Qué información pierde un conjunto?» resulta más útil que «¿Cómo se hace este ejercicio?». Lee solo el concepto necesario, cierra el ejemplo y redacta con tus palabras cómo podría ayudarte. Comprueba las interfaces con la ayuda de tu instalación si encuentras sintaxis histórica. No se necesita navegación web para seguir la colección.

## Evitar soluciones prematuras

Primero deja por escrito tu interpretación, un ejemplo manual y al menos un diseño tentativo. Si te bloqueas, identifica si falta comprensión del problema, una regla de negocio, una herramienta o una forma de verificar. Consulta el concepto correspondiente, no una solución equivalente al problema completo.

Si pides ayuda a otra persona o a una IA, solicita una pregunta orientadora, revisión del contrato o explicación de un error concreto. Evita pedir la implementación, pseudocódigo completo o una lista de pasos que solo tengas que traducir. Si viste una respuesta accidentalmente, registra esa ayuda y vuelve a intentarlo más tarde con un caso distinto antes de afirmar autonomía.

## Cuaderno de dudas y decisiones

Mantén una nota por ejercicio con estos campos; escribe razonamientos breves, no una transcripción de la sesión:

| Campo | Qué registrar |
| --- | --- |
| Interpretación | Problema, entradas, salida y restricciones con tus palabras |
| Duda | Pregunta concreta y ejemplo que la hace visible |
| Hipótesis | Qué esperabas antes de consultar o ejecutar |
| Consulta | Documento, sección y concepto aprendido |
| Decisión | Alternativa elegida, alternativa descartada y motivo |
| Nombres | Entidades importantes, unidades y un nombre que mejoraste |
| Prueba | Entrada, expectativa previa, resultado obtenido y diagnóstico |
| Lectura | Predicción al leer tu código y explicación de cualquier diferencia |
| Pendiente | Límite conocido, nueva duda o posible mejora |
| Ayuda | Qué apoyo recibiste y qué puedes repetir sin él |

Una duda de contrato no debe esconderse dentro de una decisión de implementación. Revisa primero las convenciones y las reglas; si persiste una contradicción, descríbela con dos resultados incompatibles y deja constancia de la interpretación provisional.

## Cómo comprobar el aprendizaje

Valora cada dimensión por separado con **pendiente**, **con apoyo** o **autónomo**, y adjunta evidencia. No promedies todo para ocultar una carencia importante.

| Dimensión | Evidencia observable |
| --- | --- |
| Interpretación | Reformulas el contrato y separas requisitos de suposiciones |
| Diseño | Comparas representaciones y justificas responsabilidades e invariantes |
| Corrección | Cubres casos normales, fronteras y fallos con resultados esperados escritos antes |
| Legibilidad | Nombres y funciones permiten explicar intención, unidades y efectos |
| Lectura | Predices el comportamiento sin ejecutar y localizas dónde ocurre una decisión |
| Explicación | Sigues un dato desde la entrada hasta la salida y justificas por qué funciona |
| Modificación | Cambias una regla identificando pruebas que se conservan y pruebas que cambian |
| Transferencia | Reconoces una similitud con otro problema y también una diferencia importante |
| Autonomía | Resuelves una variación sin consultar una implementación equivalente |

Un ejercicio puede funcionar y seguir pendiente en explicación, lectura o diseño. Para considerarlo revisado, ejecuta las pruebas mínimas, añade una propia, explica un rechazo y modifica una regla pequeña sin romper las demás. El reto adicional es opcional; la capacidad de razonar sobre una modificación no lo es.

## Revisar y volver a practicar

Al terminar cada diez ejercicios, vuelve a dos anteriores y lee el código antes de ejecutarlo. Predice un caso nuevo, mejora un nombre y busca una dependencia oculta. Registra si cambiarías el diseño y por qué; evita reescribir solo para usar una herramienta recién aprendida.

Vuelve unos días después a un ejercicio que necesitó ayuda. Reconstruye su contrato sin mirar tu implementación, resuélvelo con datos nuevos y explica qué patrón reconociste. Tras los ejercicios 050, 075 y 100, revisa tu cuaderno para detectar lagunas repetidas: pérdida de ceros, confusión de identidad, modificaciones inesperadas, errores ocultos o falta de pruebas de límites.

## Criterios de revisión de esta colección

Cada enunciado tiene contexto, entradas, reglas, salida, límites, escenarios comprobables, nombres, reflexión, referencias, explicación y modificación opcional. El recorrido distribuye decisiones distintas y reutiliza conceptos con contratos nuevos. Se verifican numeración, títulos únicos, las 18 secciones, enlaces locales y ausencia de bloques de soluciones. La evidencia de aprendizaje, sin embargo, la produce tu trabajo: el criterio central es entender, explicar, modificar y transferir el razonamiento.

<a id="indice-de-ejercicios"></a>
## Índice de ejercicios

Los nombres describen encargos profesionales; el orden propone una trayectoria de trabajo.

| Número | Encargo | Recupera razonamiento de |
| --- | --- | --- |
| 001 | [Confirmación de un pedido pequeño](ejercicio_001.md) | — |
| 002 | [Etiqueta para un envío interno](ejercicio_002.md) | — |
| 003 | [Control de aforo de un taller](ejercicio_003.md) | — |
| 004 | [Cotización de mensajería](ejercicio_004.md) | — |
| 005 | [Identificador de una solicitud](ejercicio_005.md) | — |
| 006 | [Duración de una visita técnica](ejercicio_006.md) | — |
| 007 | [Reparto del coste de una comida](ejercicio_007.md) | — |
| 008 | [Resumen de una cesta](ejercicio_008.md) | — |
| 009 | [Lecturas de temperatura de una sala](ejercicio_009.md) | — |
| 010 | [Depuración de etiquetas de catálogo](ejercicio_010.md) | — |
| 011 | [Prioridad de una incidencia](ejercicio_011.md) | 003 |
| 012 | [Validación de un formulario de contacto](ejercicio_012.md) | 005 |
| 013 | [Lista de preparación de paquetes](ejercicio_013.md) | — |
| 014 | [Turnos pendientes sin duplicados](ejercicio_014.md) | — |
| 015 | [Comparación de dos presupuestos](ejercicio_015.md) | 001, 004 |
| 016 | [Palabras destacadas de una reseña](ejercicio_016.md) | — |
| 017 | [Consolidación de materiales solicitados](ejercicio_017.md) | 008, 010 |
| 018 | [Cruce de invitados y asistentes](ejercicio_018.md) | — |
| 019 | [Historial de saldo de una tarjeta](ejercicio_019.md) | 003 |
| 020 | [Comparador de versiones de un aviso](ejercicio_020.md) | — |
| 021 | [Descuento de una cesta con exclusiones](ejercicio_021.md) | 004, 008 |
| 022 | [Registro de notas con recuperación](ejercicio_022.md) | — |
| 023 | [Disponibilidad de herramientas compartidas](ejercicio_023.md) | 019 |
| 024 | [Agenda de contactos sin colisiones](ejercicio_024.md) | 010, 017 |
| 025 | [Clasificación estable de tareas](ejercicio_025.md) | 011 |
| 026 | [Conciliación de un arqueo](ejercicio_026.md) | 007 |
| 027 | [Detección de rachas de retrasos](ejercicio_027.md) | 009 |
| 028 | [Resumen de respuestas de una encuesta](ejercicio_028.md) | 016 |
| 029 | [Asignación circular de responsables](ejercicio_029.md) | 014 |
| 030 | [Comparación de inventarios declarados](ejercicio_030.md) | 018 |
| 031 | [Presupuesto de compras por departamento](ejercicio_031.md) | 019, 023 |
| 032 | [Unión de clientes con sus pedidos](ejercicio_032.md) | 017, 024 |
| 033 | [Resolución de alias de productos](ejercicio_033.md) | 024 |
| 034 | [Selección de candidaturas por requisitos](ejercicio_034.md) | 018, 025 |
| 035 | [Agrupación de eventos de navegación](ejercicio_035.md) | 027, 032 |
| 036 | [Agenda de reservas sin solapamientos](ejercicio_036.md) | 006 |
| 037 | [Resumen semanal de dedicación](ejercicio_037.md) | 017 |
| 038 | [Distribución de plazas con lista de espera](ejercicio_038.md) | 014, 023 |
| 039 | [Política de acceso por roles](ejercicio_039.md) | 018, 034 |
| 040 | [Compatibilidad de versiones publicadas](ejercicio_040.md) | 005, 015 |
| 041 | [Importación de una lista de tareas](ejercicio_041.md) | 010, 020 |
| 042 | [Carga de precios desde CSV](ejercicio_042.md) | 012, 017 |
| 043 | [Persistencia de preferencias personales](ejercicio_043.md) | 012, 024 |
| 044 | [Informe de incidencias de un registro](ejercicio_044.md) | 016, 041 |
| 045 | [Fechas de vencimiento de préstamos](ejercicio_045.md) | 006 |
| 046 | [Exportación de un resumen comercial](ejercicio_046.md) | 017, 042 |
| 047 | [Configuración con precedencia explícita](ejercicio_047.md) | 012, 024 |
| 048 | [Lectura de movimientos con decimales exactos](ejercicio_048.md) | 007, 026 |
| 049 | [Inspección de un directorio de entregas](ejercicio_049.md) | 041 |
| 050 | [Bitácora de cambios de estado](ejercicio_050.md) | 019, 041 |
| 051 | [Catálogo consultable desde consola](ejercicio_051.md) | 024, 043 |
| 052 | [Migración de fichas de clientes](ejercicio_052.md) | 043 |
| 053 | [Importación con aceptación total](ejercicio_053.md) | 023, 037 |
| 054 | [Reconstrucción de existencias desde eventos](ejercicio_054.md) | 019, 050 |
| 055 | [Reserva de ejemplares como objeto](ejercicio_055.md) | 023, 050 |
| 056 | [Presupuesto compuesto por partidas](ejercicio_056.md) | 001, 053 |
| 057 | [Ventanas de disponibilidad de una sala](ejercicio_057.md) | 036 |
| 058 | [Plazos de atención con calendario](ejercicio_058.md) | 045 |
| 059 | [Detección de archivos con contenido repetido](ejercicio_059.md) | 030, 049 |
| 060 | [Evaluación de calidad de un conjunto de datos](ejercicio_060.md) | 012, 042 |
| 061 | [Consumo de páginas de una API simulada](ejercicio_061.md) | 033, 043 |
| 062 | [Plan de reintentos de una operación](ejercicio_062.md) | 050 |
| 063 | [Límite de solicitudes por ventana temporal](ejercicio_063.md) | 035, 061 |
| 064 | [Caché con vencimiento comprobable](ejercicio_064.md) | 055, 062 |
| 065 | [Traducción entre dos contratos de proveedor](ejercicio_065.md) | 040, 048, 051 |
| 066 | [Procesamiento incremental de un registro extenso](ejercicio_066.md) | 041, 044 |
| 067 | [Página de resultados con desempate](ejercicio_067.md) | 025 |
| 068 | [Normalización Unicode de nombres de catálogo](ejercicio_068.md) | 010, 016 |
| 069 | [Combinación de propuestas de edición](ejercicio_069.md) | 020, 030, 053 |
| 070 | [Duplicados de notificaciones con contradicciones](ejercicio_070.md) | 054, 061 |
| 071 | [Dependencias entre tareas de entrega](ejercicio_071.md) | 033, 034 |
| 072 | [Planificador de ejecución por rondas](ejercicio_072.md) | 029, 071 |
| 073 | [Asignación de envíos a vehículos](ejercicio_073.md) | 013, 031 |
| 074 | [Presupuesto de recursos indivisibles](ejercicio_074.md) | 015, 034 |
| 075 | [Reglas de clasificación configurables](ejercicio_075.md) | 011, 047 |
| 076 | [Refactorización de un reporte sin cambios visibles](ejercicio_076.md) | 037, 051 |
| 077 | [Corrección de una fuga entre presupuestos](ejercicio_077.md) | 056 |
| 078 | [Pruebas de propiedades de un reparto](ejercicio_078.md) | 007 |
| 079 | [Conciliación de cargos y devoluciones](ejercicio_079.md) | 019, 032 |
| 080 | [Seudonimización de un conjunto de práctica](ejercicio_080.md) | 024, 032 |
| 081 | [Plan de renombrado sin colisiones](ejercicio_081.md) | 030, 049 |
| 082 | [Vista previa y confirmación de cambios de precios](ejercicio_082.md) | 042, 053 |
| 083 | [Reanudación de un procesamiento interrumpido](ejercicio_083.md) | 054, 066 |
| 084 | [Consistencia de un índice de búsqueda](ejercicio_084.md) | 017, 024, 030 |
| 085 | [Retenciones de plazas con expiración](ejercicio_085.md) | 038, 064 |
| 086 | [Seguimiento de un envío por eventos](ejercicio_086.md) | 050, 055 |
| 087 | [Edición por lotes con reversión completa](ejercicio_087.md) | 053, 069 |
| 088 | [Distribución proporcional de un descuento](ejercicio_088.md) | 007, 021, 048 |
| 089 | [Vigencia de datos de varios proveedores](ejercicio_089.md) | 035, 067 |
| 090 | [Reporte reproducible de cierre](ejercicio_090.md) | 045, 046, 067 |
| 091 | [Evolución compatible de un resultado público](ejercicio_091.md) | 025, 076 |
| 092 | [Repositorio intercambiable de contactos](ejercicio_092.md) | 024, 043, 055 |
| 093 | [Diagnóstico de fallos sin ocultar causas](ejercicio_093.md) | 042, 060 |
| 094 | [Pruebas de fallos durante una exportación](ejercicio_094.md) | 046, 093 |
| 095 | [Duración efectiva de atención de incidencias](ejercicio_095.md) | 006, 050, 086 |
| 096 | [Plantillas de mensajes con contrato acotado](ejercicio_096.md) | 005, 016, 068 |
| 097 | [Editor con deshacer y rehacer](ejercicio_097.md) | 053, 077, 087 |
| 098 | [Actualización incremental de un tablero](ejercicio_098.md) | 054, 079, 084 |
| 099 | [Cola de trabajo con reintentos diferidos](ejercicio_099.md) | 062, 063, 072 |
| 100 | [Entrega de un importador profesional acotado](ejercicio_100.md) | 042, 076, 082, 090, 094 |
