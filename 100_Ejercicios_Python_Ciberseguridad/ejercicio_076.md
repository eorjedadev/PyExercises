# Ejercicio 076 — Reglas declarativas con contratos verificables

[Índice](README.md#indice) · [Anterior](ejercicio_075.md) · [Siguiente](ejercicio_077.md)

### Escenario de seguridad

El SOC necesita cambiar umbrales sin ejecutar expresiones recibidas como configuración.

### Contexto profesional

Ámbito: **Detección**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Mantenibilidad de un motor local de reglas. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **reglas declarativas con contratos verificables**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Coincidencias por evento y diagnóstico de configuración**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 076](ejercicio_076/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/eventos.json](ejercicio_076/datos/eventos.json) — Campos admitidos por regla: failures entero no negativo y type texto.
- [config/reglas_validas.json](ejercicio_076/config/reglas_validas.json) — Configuración válida; devolver todas las coincidencias, no solo primera.
- [config/reglas_invalidas.json](ejercicio_076/config/reglas_invalidas.json) — Caso negativo independiente; no mezclar con la configuración válida.

### Requisitos

- Reglas admiten campo permitido, operador eq/ge y valor del tipo declarado.
- primera coincidencia no oculta otras: devolver todas.
- configuración inválida aborta antes de procesar.
- no eval ni ejecución de texto.
- conservar versión de regla.
- ge solo admite failures, eq admite failures y type.
- campo faltante se informa por regla sin fabricar un valor cero.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Coincidencias por evento y diagnóstico de configuración. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Responsabilidades, interfaces y compatibilidad.
- Pruebas de contrato, regresión y fallos simulados.

### Conceptos de ciberseguridad relacionados

Separa indicador, hipótesis y conclusión. Mide cobertura y considera causas legítimas antes de asignar intención a un patrón.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **versión de regla, campo permitido, condición declarada, coincidencias**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué validación pertenece al lenguaje de reglas y cuál al dato?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 015](ejercicio_015.md), [ejercicio 053](ejercicio_053.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Regla fallos ge3 con evento 3 → coincide.
2. Operador run → configuración inválida.
3. Evento sin campo → no evaluable para esa regla.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Una regla bien formada puede representar una mala hipótesis. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Umbrales genéricos afectan aplicaciones con comportamientos distintos. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Una regla bien formada puede representar una mala hipótesis. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Módulos y Paquetes**; busca ese título en el índice.
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

Contrasta tu resultado con esta limitación: **Una regla bien formada puede representar una mala hipótesis.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En detección, este razonamiento ayuda a proteger **mantenibilidad de un motor local de reglas** mediante reglas declarativas con contratos verificables. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir condición compuesta sin convertir el formato en lenguaje arbitrario. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
