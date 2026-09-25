# 100 ejercicios de Ciencia de Datos con Python

Una colección de **100 experiencias de razonamiento con datos**, con enunciados completos y datasets sintéticos locales. Python se utiliza para comprender problemas, inspeccionar evidencia, analizar y comunicar decisiones. No incluye soluciones, scripts de análisis ni notebooks resueltos.

Consulta el [registro de validación de la colección](VALIDACION.md) para conocer los archivos y comprobaciones realizados.

## Propósito y metodología

Trabaja con el ciclo **comprender → preguntar → inspeccionar → limpiar → transformar → explorar → analizar → visualizar → interpretar → comunicar → cuestionar**. Los conocimientos se combinan en encargos de comercio, educación, servicios, salud sintética, energía, logística, industria y otros sectores. No hay clasificaciones tradicionales de dificultad.

La progresión se apoya en mayor volumen, más fuentes, decisiones metodológicas, incertidumbre y autonomía. Los conjuntos son independientes entre ejercicios; volver a un sector cambia la pregunta y los datos. Una respuesta profesional puede reconocer evidencia insuficiente.

## Requisitos y entorno

Debes poder ejecutar Python y comprender variables, condicionales y ciclos. Puedes repasar las referencias locales de [REFERENCIAS_LOCALES.md](REFERENCIAS_LOCALES.md). Usa una instalación de Python compatible con las dependencias que elijas y un editor; no necesitas cuentas externas ni descargar datasets.

Los primeros ejercicios pueden resolverse con la biblioteca estándar y una herramienta gráfica. Pandas, NumPy y Matplotlib responden después a necesidades tabulares, numéricas y visuales. SciPy se incorpora para procedimientos estadísticos; SQLite ya viene con Python para las bases locales. JupyterLab es opcional. Excel requiere un lector como openpyxl. Scikit-learn se reserva para la parte de modelado.

Puedes crear un entorno local desde esta carpeta con `python -m venv .venv`. En Windows puedes invocar `.venv\Scripts\python.exe -m pip install -r requirements.txt` sin activar el entorno; en sistemas POSIX usa `.venv/bin/python`. Instala todas las dependencias del archivo solo si vas a recorrer la colección completa; al comenzar basta instalar las que utilices. Estos comandos preparan el entorno, no resuelven ejercicios.

El archivo [requirements.txt](requirements.txt) enumera dependencias, **no es un bloqueo de versiones**. Registra `python --version` y guarda las versiones efectivas del entorno de tu trabajo mediante `python -m pip freeze`. Consulta documentación acorde a esas versiones. No se presupone que una versión futura mantenga todos los comportamientos.

## Cómo trabajar cada ejercicio

1. Lee contexto, pregunta, unidad de observación y diccionario. Escribe qué necesitas descubrir y qué no sabes todavía.
2. Conserva `datos/` intacto. Crea tu trabajo en una carpeta propia, por ejemplo `mis_analisis/ejercicio_001`, con rutas relativas a una raíz definida. No modifiques fuentes para que un resultado coincida con tu expectativa.
3. Inspecciona forma, tipos, claves, cobertura, ausencias, duplicados, rangos y unidades. No todo extremo es error ni toda repetición es duplicado.
4. Mantén un registro de decisiones con problema, evidencia, acción, motivo, registros afectados e impacto. Diferencia ausencia, cero, dato inválido y resultado todavía no observado.
5. Define población y denominadores antes de calcular. Explica a mano una parte pequeña y luego usa Python para ampliar el razonamiento.
6. Elige métricas, comparaciones y visualizaciones por la pregunta. En inferencia, declara supuestos y unidad independiente. En modelado, fija objetivo, momento de uso, particiones y baseline antes del entrenamiento.
7. Contrasta la conclusión con otra decisión de preparación o metodología plausible. Expón qué evidencia podría refutarla.
8. Entrega código propio, tabla de evidencia, visualización con propósito, conclusiones y bitácora. Desde el 031 hay dos audiencias explícitas; desde el 041 se exige especial atención a relaciones entre fuentes.

## Entregables y reproducibilidad

Un script con informe y un notebook narrativo son alternativas válidas. En un notebook, separa **contexto, código, resultado e interpretación**. Reinicia el kernel y ejecuta todo en orden antes de entregar. No se incluyen carpetas de notebooks vacías: créalas solo si las necesitas.

Desde los ejercicios con varias fuentes, organiza etapas reutilizables de lectura, validación, transformación y análisis. Registra dependencias, rutas, parámetros, fecha de corte y semillas de simulación. Los archivos `datos/procedencia.json` contienen el esquema observado, ventana nominal y huellas SHA-256 de las fuentes; permiten comprobar que el análisis utiliza el mismo dataset. La semilla de autoría es metadato de procedencia, no sustituye un generador: la fuente reproducible entregada es el archivo congelado.

## Cómo investigar y utilizar documentación

Consulta [RECURSOS.md](RECURSOS.md). Formula una duda concreta; encuentra el apartado relevante; lee parámetros, valores devueltos y supuestos; realiza una prueba pequeña propia; explica qué aprendiste. No copies una receta cuya población o supuestos no comprendes. Las referencias oficiales se verificaron el 2026-09-22; pueden evolucionar.

Si solicitas ayuda, sigue **pregunta orientadora → razonamiento → concepto → pista → documentación → revisión del intento**. Comparte qué crees que ocurre y un intento acotado. La ayuda debe permitirte descubrir el problema, no entregarte inmediatamente el análisis terminado.

## Cómo comprobar resultados

Comprueba conteos antes y después, claves, cardinalidades, unidades y conciliación de sumas. Verifica manualmente una muestra y un caso límite propio. Una tasa necesita denominador; una media necesita distribución y tamaño; una comparación temporal necesita cobertura equivalente. Para joins, explica qué filas permanecen y por qué. Para simulaciones, documenta semilla y variabilidad Monte Carlo.

No existe una única cifra de respuesta para todas las políticas de limpieza. Tu decisión debe ser trazable, coherente y sensible a alternativas. Si un grupo queda vacío, reporta que no puede estimarse; no lo conviertas en cero. No se exige significancia, correlación alta ni mejora de un modelo: un resultado negativo también puede estar bien sustentado.

## Interpretación y límites

Todos los patrones pertenecen a escenarios sintéticos; no representan parámetros reales. Correlación no implica causalidad. Ponderar, imputar o ajustar un modelo no elimina automáticamente sesgos. Un p valor no mide relevancia práctica y una buena métrica predictiva no demuestra que una intervención funcione. Documenta supuestos, explicaciones rivales y qué información falta.

En laboratorio no hay pacientes ni umbrales clínicos; recursos humanos usa personas ficticias. Los registros monetarios describen contabilidad simulada. La finalidad es analítica y formativa.

## Progreso y revisión

Usa [REGISTRO_APRENDIZAJE.md](REGISTRO_APRENDIZAJE.md). Evalúa por separado comprensión, Python, calidad, metodología, comprobación, interpretación y comunicación. Marca cada dimensión como **sin evidencia, con apoyo o autónomo**, con una evidencia concreta; son estados de tu trabajo, no etiquetas de dificultad del ejercicio.

Cada cinco ejercicios revisa uno anterior: ejecútalo desde cero, mejora un nombre y reconsidera una decisión. Cada diez compara tu primera conclusión con una reescrita para otra audiencia. Avanza cuando puedas explicar y reproducir tu análisis, no solo cuando el programa termine. Si una dimensión queda sin evidencia, formula una práctica deliberada para el siguiente encargo.

## Recorrido

| Tramo | Evolución del encargo |
| --- | --- |
| 001–020 | Preguntas delimitadas, muestras pequeñas, fundamentos y significado de métricas. |
| 021–040 | Distribuciones, transformaciones, confusión y decisiones de representación. |
| 041–050 | Claves, fuentes relacionadas, cardinalidades y comparabilidad. |
| 051–060 | Muestreo, intervalos, efectos, contrastes y evaluación experimental. |
| 061–065 | Extracción desde cinco bases SQLite y análisis con Python. |
| 066–075 | Tiempo, seguimiento, estacionalidad, composición y simulación. |
| 076–088 | Modelado con baselines, evaluación, fuga, sobreajuste y monitoreo. |
| 089–100 | Encargos abiertos, integración, elección metodológica y recomendaciones. |

Estas son transiciones de autonomía, no módulos aislados de bibliotecas. Calidad, Python, interpretación y comunicación atraviesan todo el recorrido. Consulta el [mapa completo de progresión](PROGRESION.md).

## Índice de ejercicios

| Ejercicio | Encargo | Contexto | Formatos de datos |
| --- | --- | --- | --- |
| [001](ejercicio_001/README.md) | Una espera que el promedio oculta | servicios públicos | csv |
| [002](ejercicio_002/README.md) | El ingreso de una pequeña caja | comercio | csv |
| [003](ejercicio_003/README.md) | Tickets y categorías de entrada | soporte informático | csv |
| [004](ejercicio_004/README.md) | Una cohorte que no cabe en una nota | educación | csv |
| [005](ejercicio_005/README.md) | Existencias frente a solicitudes | inventarios | csv |
| [006](ejercicio_006/README.md) | Mediciones con distintas unidades | ambiente | txt |
| [007](ejercicio_007/README.md) | Visitas que llegan a compra | desarrollo web y comercio electrónico | json |
| [008](ejercicio_008/README.md) | Puntualidad de las entregas | transporte y logística | csv |
| [009](ejercicio_009/README.md) | Escuchar también las no respuestas | servicios y opinión | csv |
| [010](ejercicio_010/README.md) | Consumo de edificios desiguales | energía | csv |
| [011](ejercicio_011/README.md) | Reservas y noches comprometidas | turismo | csv |
| [012](ejercicio_012/README.md) | Horas de formación y participación | recursos humanos sintéticos | csv |
| [013](ejercicio_013/README.md) | Defectos con tamaños de lote diferentes | industria | csv |
| [014](ejercicio_014/README.md) | Consumo y planes contratados | telecomunicaciones | csv |
| [015](ejercicio_015/README.md) | Facturas comparables | finanzas empresariales | xlsx |
| [016](ejercicio_016/README.md) | Préstamos y devoluciones | servicios culturales | csv |
| [017](ejercicio_017/README.md) | Recogida y población atendida | servicios urbanos | csv |
| [018](ejercicio_018/README.md) | Resultados y repetibilidad | salud sintética y control de laboratorio | csv |
| [019](ejercicio_019/README.md) | Plazos de abastecimiento | compras y abastecimiento | csv |
| [020](ejercicio_020/README.md) | Leer un ensayo antes de compararlo | tecnología y marketing | json |
| [021](ejercicio_021/README.md) | Una distribución de espera completa | servicios públicos | csv |
| [022](ejercicio_022/README.md) | Descuentos y valor de compra | comercio | csv |
| [023](ejercicio_023/README.md) | Tiempo típico y carga extrema | soporte informático | csv |
| [024](ejercicio_024/README.md) | Asistencia y resultados | educación | csv |
| [025](ejercicio_025/README.md) | Datos que llegan como tabla ancha | inventarios | csv |
| [026](ejercicio_026/README.md) | Cobertura desigual entre estaciones | ambiente | txt |
| [027](ejercicio_027/README.md) | ¿El tráfico o la conversión cambió? | desarrollo web y comercio electrónico | json |
| [028](ejercicio_028/README.md) | Distancia y duración | transporte y logística | csv |
| [029](ejercicio_029/README.md) | Satisfacción en poblaciones desiguales | servicios y opinión | csv |
| [030](ejercicio_030/README.md) | Frío, calor y consumo | energía | csv |
| [031](ejercicio_031/README.md) | Cancelaciones y anticipación | turismo | csv |
| [032](ejercicio_032/README.md) | Comparaciones salariales responsables | recursos humanos sintéticos | csv |
| [033](ejercicio_033/README.md) | Variabilidad más allá del promedio | industria | csv |
| [034](ejercicio_034/README.md) | Incidencias y abandono observado | telecomunicaciones | csv |
| [035](ejercicio_035/README.md) | Gastos concentrados | finanzas empresariales | xlsx |
| [036](ejercicio_036/README.md) | Renovación y género literario | servicios culturales | csv |
| [037](ejercicio_037/README.md) | Días y composición de la recogida | servicios urbanos | csv |
| [038](ejercicio_038/README.md) | Límites de detección | salud sintética y control de laboratorio | csv |
| [039](ejercicio_039/README.md) | Entregas parciales y servicio | compras y abastecimiento | csv |
| [040](ejercicio_040/README.md) | Balance antes del resultado | tecnología y marketing | json |
| [041](ejercicio_041/README.md) | Sedes y capacidad disponible | servicios públicos | csv |
| [042](ejercicio_042/README.md) | Margen con catálogo de costes | comercio | csv |
| [043](ejercicio_043/README.md) | Historial de eventos y tickets | soporte informático | csv |
| [044](ejercicio_044/README.md) | Tutorías y selección de alumnos | educación | csv |
| [045](ejercicio_045/README.md) | Inventario con catálogo de productos | inventarios | csv |
| [046](ejercicio_046/README.md) | Estaciones y comparabilidad espacial | ambiente | csv, txt |
| [047](ejercicio_047/README.md) | Usuarios frente a sesiones | desarrollo web y comercio electrónico | csv, json |
| [048](ejercicio_048/README.md) | Servicio y costes de transportistas | transporte y logística | csv |
| [049](ejercicio_049/README.md) | Muestra frente a padrón | servicios y opinión | csv |
| [050](ejercicio_050/README.md) | Facturación y medición | energía | csv, xlsx |
| [051](ejercicio_051/README.md) | Incertidumbre en cancelaciones | turismo | csv |
| [052](ejercicio_052/README.md) | Una muestra de trabajadores | recursos humanos sintéticos | csv |
| [053](ejercicio_053/README.md) | Incertidumbre en tasa de defectos | industria | csv |
| [054](ejercicio_054/README.md) | Bajas y probabilidades condicionales | telecomunicaciones | csv |
| [055](ejercicio_055/README.md) | Estimación de gasto típico | finanzas empresariales | csv |
| [056](ejercicio_056/README.md) | Renovación entre sucursales | servicios culturales | csv |
| [057](ejercicio_057/README.md) | Campaña y cambio aparente | servicios urbanos | csv |
| [058](ejercicio_058/README.md) | Comparación emparejada de instrumentos | salud sintética y control de laboratorio | csv |
| [059](ejercicio_059/README.md) | Muchos proveedores, muchas pruebas | compras y abastecimiento | csv |
| [060](ejercicio_060/README.md) | Resultado de un ensayo A/B | tecnología y marketing | csv, json |
| [061](ejercicio_061/README.md) | Extracción analítica desde SQLite | soporte informático | sqlite |
| [062](ejercicio_062/README.md) | Ingresos y catálogo en una base local | comercio | sqlite |
| [063](ejercicio_063/README.md) | Historia de existencias en SQL | inventarios | sqlite |
| [064](ejercicio_064/README.md) | Cuentas pendientes al corte | finanzas empresariales | sqlite |
| [065](ejercicio_065/README.md) | Cohortes de conversión con SQL | desarrollo web y comercio electrónico | sqlite |
| [066](ejercicio_066/README.md) | Estacionalidad de consumo | energía | csv |
| [067](ejercicio_067/README.md) | Promesas de servicio a lo largo del tiempo | transporte y logística | csv |
| [068](ejercicio_068/README.md) | Estacionalidad de las reservas | turismo | csv |
| [069](ejercicio_069/README.md) | Huecos y agregación temporal | ambiente | csv, txt |
| [070](ejercicio_070/README.md) | Señales de cambio en producción | industria | csv |
| [071](ejercicio_071/README.md) | Llegadas y resolución de solicitudes | soporte informático | csv |
| [072](ejercicio_072/README.md) | Comparar períodos con distinta cobertura | servicios urbanos | csv |
| [073](ejercicio_073/README.md) | Cambios en la base de clientes | telecomunicaciones | csv |
| [074](ejercicio_074/README.md) | Una cartera con entregas pendientes | compras y abastecimiento | csv |
| [075](ejercicio_075/README.md) | Mirar el experimento cada día | tecnología y marketing | csv, json |
| [076](ejercicio_076/README.md) | Primera predicción de duración | transporte y logística | csv |
| [077](ejercicio_077/README.md) | Predecir consumo sin mirar el futuro | energía | csv |
| [078](ejercicio_078/README.md) | Anticipar bajas de clientes | telecomunicaciones | csv |
| [079](ejercicio_079/README.md) | Fallos poco frecuentes | industria | csv |
| [080](ejercicio_080/README.md) | Cancelación antes de la llegada | turismo | csv |
| [081](ejercicio_081/README.md) | Preparación que aprende solo del entrenamiento | educación | csv |
| [082](ejercicio_082/README.md) | Complejidad y sobreajuste | transporte y logística | csv |
| [083](ejercicio_083/README.md) | Umbral con capacidad de contacto | telecomunicaciones | csv |
| [084](ejercicio_084/README.md) | Segmentos de comportamiento | desarrollo web y comercio electrónico | csv, json |
| [085](ejercicio_085/README.md) | Alertas sin etiquetas operativas completas | industria | csv |
| [086](ejercicio_086/README.md) | Pronóstico y validación móvil | energía | csv |
| [087](ejercicio_087/README.md) | Probabilidades y calibración | turismo | csv |
| [088](ejercicio_088/README.md) | Cambio de población y evaluación | telecomunicaciones | csv |
| [089](ejercicio_089/README.md) | Encargo abierto de atención municipal | servicios públicos | csv |
| [090](ejercicio_090/README.md) | Rentabilidad de una operación comercial | comercio | csv |
| [091](ejercicio_091/README.md) | Reorganización de una mesa de ayuda | soporte informático | csv |
| [092](ejercicio_092/README.md) | Evaluación de un programa educativo | educación | csv |
| [093](ejercicio_093/README.md) | Abastecimiento con presupuesto limitado | inventarios | csv |
| [094](ejercicio_094/README.md) | Informe ambiental con cobertura incompleta | ambiente | csv, txt |
| [095](ejercicio_095/README.md) | Decisión de producto con evidencia fragmentada | desarrollo web y comercio electrónico | csv, json |
| [096](ejercicio_096/README.md) | Diagnóstico de una red logística | transporte y logística | csv |
| [097](ejercicio_097/README.md) | Una encuesta para decidir inversión | servicios y opinión | csv |
| [098](ejercicio_098/README.md) | Auditoría energética reproducible | energía | csv, xlsx |
| [099](ejercicio_099/README.md) | Mantenimiento con evidencia y costes | industria | csv |
| [100](ejercicio_100/README.md) | Informe final de retención | telecomunicaciones | csv |
