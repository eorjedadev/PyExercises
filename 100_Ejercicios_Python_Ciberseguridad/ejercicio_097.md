# Ejercicio 097 — Análisis incremental con límites de memoria

[Índice](README.md#indice) · [Anterior](ejercicio_096.md) · [Siguiente](ejercicio_098.md)

### Escenario de seguridad

Un archivo de laboratorio de miles de eventos debe resumirse sin materializarlo entero.

### Contexto profesional

Ámbito: **Automatización**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Procesamiento de telemetría voluminosa. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **análisis incremental con límites de memoria**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Resumen, conteo de rechazados y argumento verificable de memoria**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 097](ejercicio_097/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/volumen.log](ejercicio_097/logs/volumen.log) — 20000 líneas JSONL con50 cuentas sintéticas y3 líneas defectuosas; no leer todas a una lista.
- [logs/muestra.log](ejercicio_097/logs/muestra.log) — Muestra independiente para comprobar un resultado manual.

### Requisitos

- Contar ok/fail por cuenta con memoria proporcional a cuentas únicas y no número de eventos.
- errores se emiten incrementalmente.
- no guardar lista completa.
- comparar con muestra pequeña conocida.
- no medir un tiempo absoluto dependiente del equipo.
- la entrada es JSONL con id, account y outcome exacto ok/fail.
- registro mal formado se rechaza por línea y se continúa.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Resumen, conteo de rechazados y argumento verificable de memoria. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Lectura incremental y complejidad de memoria.
- Lectura de eventos, validación y procedencia.

### Conceptos de ciberseguridad relacionados

La herramienta también debe fallar de forma visible y proteger evidencia. Un resultado parcial no puede presentarse como ausencia de hallazgos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **evento actual, estado por cuenta, errores emitidos, volumen procesado**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué estado mínimo exige cada métrica y qué limitación permanece?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 043](ejercicio_043.md), [ejercicio 047](ejercicio_047.md), [ejercicio 094](ejercicio_094.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Muestra ana fail, fail, ok → 2/1.
2. Línea inválida → rechazada sin perder siguientes.
3. Archivo vacío → sin cuentas.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Muchísimas identidades únicas también aumentan memoria. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Carga alta puede ser un lote de mantenimiento legítimo. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Muchísimas identidades únicas también aumentan memoria. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md) — **Capítulo 17. Iteradores, generadores y corrutinas clásicas**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Logging**; busca ese título en el índice.
- [OWASP: registro y fallos de logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Muchísimas identidades únicas también aumentan memoria.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En automatización, este razonamiento ayuda a proteger **procesamiento de telemetría voluminosa** mediante análisis incremental con límites de memoria. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Imponer cardinalidad máxima y declarar resultados incompletos al superarla. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
