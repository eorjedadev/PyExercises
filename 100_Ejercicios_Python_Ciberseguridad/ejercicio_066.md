# Ejercicio 066 — Modificaciones de tareas programadas

[Índice](README.md#indice) · [Anterior](ejercicio_065.md) · [Siguiente](ejercicio_067.md)

### Escenario de seguridad

Hay capturas de tareas programadas y una agenda de cambios.

### Contexto profesional

Ámbito: **Sistemas**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Persistencia administrativa declarada. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **modificaciones de tareas programadas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Cambios con alcance de aprobación y datos faltantes**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 066](ejercicio_066/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/antes.json](ejercicio_066/datos/antes.json) — Primera captura de tareas, no comandos que deban ejecutarse.
- [datos/despues.json](ejercicio_066/datos/despues.json) — Segunda captura tomada en el instante configurado.
- [datos/tickets.json](ejercicio_066/datos/tickets.json) — Autorización exacta para alta de T2. Comparar cambios contra instante de captura.
- [config/parametros.json](ejercicio_066/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Comparar por host/task_id.
- detectar altas, bajas y cambios en ejecutable o frecuencia.
- no ejecutar acciones.
- autorización exacta por task_id y ventana.
- rutas son evidencia, no se abren.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Cambios con alcance de aprobación y datos faltantes. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Pertenencia, diferencia y conservación de identidad.
- Estructuras anidadas, tipos y contratos de entrada.

### Conceptos de ciberseguridad relacionados

Un ajuste exportado no equivale siempre al control efectivo. Distingue modelo del ejercicio, semántica de plataforma y ejecución realmente observada.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **tarea, acción anterior, acción nueva, autorización**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué evidencia sobre el archivo ejecutado aumentaría tu confianza?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 019](ejercicio_019.md), [ejercicio 062](ejercicio_062.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. T1 cambia ejecutable sin ticket → revisión.
2. T2 alta con ticket exacto → aprobada.
3. Cambio solo de descripción → informativo.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Una tarea nueva no demuestra persistencia maliciosa. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Actualizaciones legítimas crean o renuevan tareas. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Una tarea nueva no demuestra persistencia maliciosa. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Conjuntos**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [CIS Controls: contexto de configuración y auditoría](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Una tarea nueva no demuestra persistencia maliciosa.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En sistemas, este razonamiento ayuda a proteger **persistencia administrativa declarada** mediante modificaciones de tareas programadas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Cruzar huella del ejecutable con inventario autorizado. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
