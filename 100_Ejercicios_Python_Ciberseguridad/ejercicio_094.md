# Ejercicio 094 — Resistencia de un parser ante evidencia defectuosa

[Índice](README.md#indice) · [Anterior](ejercicio_093.md) · [Siguiente](ejercicio_095.md)

### Escenario de seguridad

Se suministra JSON Lines con datos válidos, dañados y tipos inesperados.

### Contexto profesional

Ámbito: **Automatización**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Fiabilidad de la herramienta de análisis. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **resistencia de un parser ante evidencia defectuosa**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Eventos aceptados, errores por línea y estado completo/parcial**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 094](ejercicio_094/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/defectuoso.log](ejercicio_094/logs/defectuoso.log) — JSONL intencionalmente defectuoso: máximo se mide sin LF, conservar línea física. El archivo completo no se carga como un único JSON.
- [config/parametros.json](ejercicio_094/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Una línea física es unidad.
- máximo 2048 bytes por línea.
- exigir id, ts con zona y outcome ok/fail.
- rechazar duplicación de claves dentro de un objeto.
- continuar tras errores de línea conservando posición.
- no devolver limpio si hay rechazos.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Eventos aceptados, errores por línea y estado completo/parcial. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Excepciones, resultados parciales y diagnóstico.
- Representación binaria, codificación y límites de tamaño.

### Conceptos de ciberseguridad relacionados

La herramienta también debe fallar de forma visible y proteger evidencia. Un resultado parcial no puede presentarse como ausencia de hallazgos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **línea física, tamaño, causa de rechazo, eventos aceptados**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué datos debes conservar sin repetir contenido sensible en un error?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 043](ejercicio_043.md), [ejercicio 047](ejercicio_047.md), [ejercicio 077](ejercicio_077.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Línea JSON mal cerrada → rechazo y siguiente se procesa.
2. Dos claves outcome → rechazo.
3. Línea2049 bytes → rechazo por tamaño.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Distintas bibliotecas pueden aceptar duplicados quedándose con último valor. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una escritura interrumpida genera líneas truncadas legítimamente. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Distintas bibliotecas pueden aceptar duplicados quedándose con último valor. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Manejo de Errores y Excepciones**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Bytes, Unicode y Codificación**; busca ese título en el índice.
- [OWASP: registro y fallos de logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Distintas bibliotecas pueden aceptar duplicados quedándose con último valor.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En automatización, este razonamiento ayuda a proteger **fiabilidad de la herramienta de análisis** mediante resistencia de un parser ante evidencia defectuosa. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir pruebas de anidación excesiva sin agotar el proceso. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
