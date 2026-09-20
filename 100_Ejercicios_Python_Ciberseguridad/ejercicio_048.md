# Ejercicio 048 — Timestamps normalizados con procedencia

[Índice](README.md#indice) · [Anterior](ejercicio_047.md) · [Siguiente](ejercicio_049.md)

### Escenario de seguridad

Fuentes distintas registran zonas horarias diferentes y no se pueden comparar como texto.

### Contexto profesional

Ámbito: **Forense**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Cronología de evidencias. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **timestamps normalizados con procedencia**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Cronología y eventos con tiempo incierto**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 048](ejercicio_048/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/tiempos.json](ejercicio_048/logs/tiempos.json) — Fechas con zona, sin zona e imposibles. No corregir silenciosamente.

### Requisitos

- Aceptar ISO8601 con zona explícita.
- producir UTC y conservar original.
- sin zona se marca no ordenable, no se asume local.
- ordenar por UTC e id.
- no inventar precisión adicional.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Cronología y eventos con tiempo incierto. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Zonas, intervalos, orden e incertidumbre**: Comparar instantes y fronteras temporales con una referencia explícita.
- **Lectura de eventos, validación y procedencia**: Conservar posición, fuente e identificador aunque un registro se descarte.

### Conceptos de ciberseguridad relacionados

Conserva origen, integridad y trazabilidad. Un cambio observado no identifica su causa ni autor; una copia transformada no debe presentarse como el original.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- datetime y timedelta; justifica su necesidad y el límite de su garantía.
- csv, json y funciones de validación; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **timestamp original, zona declarada, instante UTC, precisión**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué perderías al sustituir el timestamp original por uno normalizado?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 012](ejercicio_012.md), [ejercicio 013](ejercicio_013.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. 10:00Z y 05:00-05:00 → mismo instante.
2. Hora sin zona → no ordenable.
3. Fecha imposible → inválida.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Dos eventos con misma marca temporal no tienen orden causal demostrado. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Diferencias de zona pueden aparentar actividad fuera de horario. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Dos eventos con misma marca temporal no tienen orden causal demostrado. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Logging**; busca ese título en el índice.
- [NIST SP 800-61r3: contexto de respuesta](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/datetime.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Dos eventos con misma marca temporal no tienen orden causal demostrado.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En forense, este razonamiento ayuda a proteger **cronología de evidencias** mediante timestamps normalizados con procedencia. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir correcciones de reloj por fuente como dato separado. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
