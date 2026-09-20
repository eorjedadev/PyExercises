# Ejercicio 093 — Resultados reproducibles al actualizar indicadores

[Índice](README.md#indice) · [Anterior](ejercicio_092.md) · [Siguiente](ejercicio_094.md)

### Escenario de seguridad

Una actualización del feed cambia qué eventos coinciden y no debe reescribir el pasado.

### Contexto profesional

Ámbito: **Detección**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Trazabilidad de decisiones anteriores. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **resultados reproducibles al actualizar indicadores**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Dos resultados reproducibles y diferencias con motivo**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 093](ejercicio_093/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/feed_v1.json](ejercicio_093/datos/feed_v1.json) — Indicadores ficticios. La confianza es declaración de la fuente, no conclusión del analista.
- [logs/observaciones.json](ejercicio_093/logs/observaciones.json) — Observaciones de fuentes sintéticas; tipo controla normalización.
- [config/parametros.json](ejercicio_093/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.
- [datos/feed_v2.json](ejercicio_093/datos/feed_v2.json) — Versión2 retira IOC1, amplía vigencia de IOC2 y añade IOC5. No reescribir resultados históricos.

### Requisitos

- Ejecutar coincidencia de 51 por versión de feed y mismo corte.
- persistir solo reportes versionados, no modificar originales.
- comparar nuevas coincidencias y retiradas.
- indicador retirado no demuestra que un evento histórico fuera benigno.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Dos resultados reproducibles y diferencias con motivo. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Estructuras anidadas, tipos y contratos de entrada.
- Pruebas de contrato, regresión y fallos simulados.

### Conceptos de ciberseguridad relacionados

Separa indicador, hipótesis y conclusión. Mide cobertura y considera causas legítimas antes de asignar intención a un patrón.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **versión de feed, corte de análisis, coincidencia histórica, motivo de cambio**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cómo responderías qué sabías cuando emitiste el primer reporte?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 051](ejercicio_051.md), [ejercicio 053](ejercicio_053.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. IOC1 presente en v1 y ausente en v2 → coincidencia retirada.
2. IOC5 nuevo en v2 → nueva coincidencia.
3. Mismo evento, versión de feed y corte → mismo resultado ordenado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Cambian inteligencia y política, no necesariamente lo ocurrido. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Corrección de un indicador equivocado retira alertas legítimamente. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Cambian inteligencia y política, no necesariamente lo ocurrido. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [INTENSIVO DE PYTHON (Eric Matthes).md](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md) — **11. Probar el código**; busca ese título en el índice.
- [CIS Controls: contexto de monitoreo defensivo](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Cambian inteligencia y política, no necesariamente lo ocurrido.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En detección, este razonamiento ayuda a proteger **trazabilidad de decisiones anteriores** mediante resultados reproducibles al actualizar indicadores. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Conservar también versión de la regla de normalización. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
