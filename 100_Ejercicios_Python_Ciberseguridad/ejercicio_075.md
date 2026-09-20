# Ejercicio 075 — Adaptación de esquemas de eventos

[Índice](README.md#indice) · [Anterior](ejercicio_074.md) · [Siguiente](ejercicio_076.md)

### Escenario de seguridad

Dos versiones del sensor nombran distinto los campos y los estados.

### Contexto profesional

Ámbito: **Automatización**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Compatibilidad de reglas defensivas. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **adaptación de esquemas de eventos**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Eventos normalizados y diferencias de cobertura por versión**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 075](ejercicio_075/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/versiones.json](ejercicio_075/logs/versiones.json) — La semántica de status/outcome es la declarada por este contrato, no la de todos los sensores reales.

### Requisitos

- v1 user/status donde success/failure.
- v2 principal/outcome donde ok/denied.
- producir cuenta/resultado común con id, fuente y hora.
- desconocidos → no evaluable.
- no traducir denied a prueba de credencial errónea fuera del contrato suministrado.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Eventos normalizados y diferencias de cobertura por versión. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Responsabilidades, interfaces y compatibilidad.
- Estructuras anidadas, tipos y contratos de entrada.

### Conceptos de ciberseguridad relacionados

La herramienta también debe fallar de forma visible y proteger evidencia. Un resultado parcial no puede presentarse como ausencia de hallazgos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **versión de esquema, valor original, evento común, campo no representable**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué significado debes conservar además del nombre normalizado?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 043](ejercicio_043.md), [ejercicio 063](ejercicio_063.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. v1 success → ok común.
2. v2 denied → fail común según contrato.
3. v3 → no evaluable.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Normalización puede ocultar distinciones útiles de la fuente. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una actualización de sensor puede aparentar cambio de comportamiento. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Normalización puede ocultar distinciones útiles de la fuente. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Módulos y Paquetes**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [OWASP: registro y fallos de logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Normalización puede ocultar distinciones útiles de la fuente.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En automatización, este razonamiento ayuda a proteger **compatibilidad de reglas defensivas** mediante adaptación de esquemas de eventos. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Mantener compatibilidad de una regla existente al añadir versión3. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
