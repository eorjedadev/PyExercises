# Ejercicio 089 — Agrupación explicable de alertas relacionadas

[Índice](README.md#indice) · [Anterior](ejercicio_088.md) · [Siguiente](ejercicio_090.md)

### Escenario de seguridad

Múltiples reglas alertan sobre un mismo activo y deben relacionarse sin borrar eventos.

### Contexto profesional

Ámbito: **SOC**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Carga de investigación del analista. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **agrupación explicable de alertas relacionadas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Grupos y vínculos justificativos, sin afirmar una sola campaña**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 089](ejercicio_089/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/alertas.json](ejercicio_089/logs/alertas.json) — Cada id es una alerta distinta; no perder categorías al agrupar.
- [datos/contexto.json](ejercicio_089/datos/contexto.json) — Contexto deliberadamente incompleto, no etiquetas de incidente.

### Requisitos

- Formar vínculos entre alertas de mismo activo y separadas como máximo 60s.
- grupos por conectividad de vínculos.
- explicar efecto de encadenamiento aunque extremos superen60.
- no fusionar activos por IP compartida.
- conservar todos los ids.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Grupos y vínculos justificativos, sin afirmar una sola campaña. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Identidad, agregación y relaciones entre registros.
- Zonas, intervalos, orden e incertidumbre.

### Conceptos de ciberseguridad relacionados

Una alerta es una solicitud de revisión basada en una regla. La cobertura, los datos descartados y las excepciones condicionan su interpretación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **alerta, activo, vínculo temporal, grupo provisional**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cuándo convendría partir un grupo aunque exista conexión temporal?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 048](ejercicio_048.md), [ejercicio 052](ejercicio_052.md), [ejercicio 074](ejercicio_074.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. A0, A50, A100 mismo activo → un grupo con encadenamiento.
2. Otro activo a50 → otro grupo.
3. A161 → separado de A100.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Conectividad temporal puede unir incidentes independientes. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una sesión de mantenimiento produce varias alertas heterogéneas. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Conectividad temporal puede unir incidentes independientes. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [OWASP: registro de eventos](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Conectividad temporal puede unir incidentes independientes.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En soc, este razonamiento ayuda a proteger **carga de investigación del analista** mediante agrupación explicable de alertas relacionadas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Exigir categoría compatible además del tiempo. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
