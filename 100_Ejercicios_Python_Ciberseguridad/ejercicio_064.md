# Ejercicio 064 — Contexto de elevaciones sudo

[Índice](README.md#indice) · [Anterior](ejercicio_063.md) · [Siguiente](ejercicio_065.md)

### Escenario de seguridad

Una exportación Linux separa autenticación, ejecución y sesiones administrativas.

### Contexto profesional

Ámbito: **Sistemas**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Administración Linux. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **contexto de elevaciones sudo**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Ejecuciones con/sin contexto y evidencia temporal**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 064](ejercicio_064/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/linux.json](ejercicio_064/logs/linux.json) — Eventos ya normalizados, no promesa de formato idéntico de journal o auth.log entre distribuciones.

### Requisitos

- Correlacionar eventos por session_id exacto.
- ejecución sudo requiere evento previo auth_ok en misma sesión dentro de 120 segundos.
- sin él se marca sin contexto, no ejecución ilícita.
- no ejecutar comandos registrados.
- incluir Ubuntu, Kali yCachyOS como etiquetas, no indicadores.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Ejecuciones con/sin contexto y evidencia temporal. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Lectura de eventos, validación y procedencia.
- Zonas, intervalos, orden e incertidumbre.

### Conceptos de ciberseguridad relacionados

Un ajuste exportado no equivale siempre al control efectivo. Distingue modelo del ejercicio, semántica de plataforma y ejecución realmente observada.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **sesión Linux, evento de elevación, evidencia previa, distribución declarada**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué configuración necesitarías para interpretar ausencia de autenticación reciente?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 013](ejercicio_013.md), [ejercicio 048](ejercicio_048.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. L1 auth_ok y L2 sudo misma sesión a30s → contexto.
2. sudo en otra sesión → sin contexto.
3. auth posterior → no respalda.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Algunas políticas permiten sudo sin nueva contraseña. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Administradores autorizados y cachés de credenciales explican diferencias. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Algunas políticas permiten sudo sin nueva contraseña. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Logging**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [CIS Controls: contexto de configuración y auditoría](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Algunas políticas permiten sudo sin nueva contraseña.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En sistemas, este razonamiento ayuda a proteger **administración linux** mediante contexto de elevaciones sudo. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Cruzar comandos permitidos por política sin ejecutarlos. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
