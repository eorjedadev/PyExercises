# Ejercicio 099 — Informe técnico con afirmaciones graduadas

[Índice](README.md#indice) · [Anterior](ejercicio_098.md) · [Siguiente](ejercicio_100.md)

### Escenario de seguridad

Un expediente contiene observaciones, aseveraciones ajenas y huecos que deben distinguirse.

### Contexto profesional

Ámbito: **Respuesta a incidentes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Decisiones basadas en evidencia. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **informe técnico con afirmaciones graduadas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Informe legible y matriz de afirmaciones verificables, contradichas o no sustentadas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 099](ejercicio_099/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/afirmaciones.json](ejercicio_099/datos/afirmaciones.json) — Afirmaciones para evaluar, no conclusiones del material.
- [datos/evidencias.json](ejercicio_099/datos/evidencias.json) — Hashes de dos capturas declaradas del mismo archivo y una declaración no corroborada.
- [datos/cobertura.json](ejercicio_099/datos/cobertura.json) — Sin cobertura de procesos. El testimonio no agrega esa cobertura.

### Requisitos

- Producir hallazgo, evidencia, interpretación, confianza razonada, información faltante y recomendación.
- toda afirmación factual enlaza ids.
- citas de un testigo son declaraciones, no hechos verificados.
- confianza alta/media/baja corresponde a solidez de afirmación concreta, no puntuación de riesgo.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Informe legible y matriz de afirmaciones verificables, contradichas o no sustentadas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Selección, correlación y comunicación de resultados.
- Identidad, agregación y relaciones entre registros.

### Conceptos de ciberseguridad relacionados

Relaciona afirmaciones con evidencia, documenta incertidumbre y distingue propuesta de acción de autorización para ejecutarla.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **afirmación, referencia de evidencia, hipótesis, confianza justificada**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué afirmación eliminarías por no tener evidencia suficiente?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 073](ejercicio_073.md), [ejercicio 080](ejercicio_080.md), [ejercicio 081](ejercicio_081.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Afirmación de acceso con log fail solo → no sustentada.
2. Huella distinta documentada → cambio respaldado, no autoría.
3. Fuente requerida ausente → limitación explícita.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Varias fuentes pueden repetir el mismo dato en vez de corroborarlo independientemente. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un cambio autorizado puede explicar un hallazgo verdadero. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Varias fuentes pueden repetir el mismo dato en vez de corroborarlo independientemente. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [NIST SP 800-61r3: respuesta a incidentes](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Varias fuentes pueden repetir el mismo dato en vez de corroborarlo independientemente.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En respuesta a incidentes, este razonamiento ayuda a proteger **decisiones basadas en evidencia** mediante informe técnico con afirmaciones graduadas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Incorporar evidencia contradictoria y revisar solo las conclusiones afectadas. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
