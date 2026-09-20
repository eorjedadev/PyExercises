# Ejercicio 092 — Paquete compartible con minimización de datos

[Índice](README.md#indice) · [Anterior](ejercicio_091.md) · [Siguiente](ejercicio_093.md)

### Escenario de seguridad

Otro equipo necesita un subconjunto de evidencia sin recibir identificadores innecesarios.

### Contexto profesional

Ámbito: **Forense**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Privacidad de personas en un expediente. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **paquete compartible con minimización de datos**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Paquete derivado, manifiesto y registro de transformaciones**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 092](ejercicio_092/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/evidencia_original.json](ejercicio_092/datos/evidencia_original.json) — Material sintético que debe mantenerse sin cambios. Tokens son texto ficticio, no credenciales reales.
- [config/parametros.json](ejercicio_092/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Preservar original.
- copia con event_id, tiempo, acción y alias por usuario en orden de primera aparición.
- retirar correo y token.
- mapa de correspondencia no va en paquete compartido.
- manifiesto SHA-256 de copia, sin afirmar que es el original.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Paquete derivado, manifiesto y registro de transformaciones. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Bytes, comparación de huellas y validación de formatos.
- Estructuras anidadas, tipos y contratos de entrada.

### Conceptos de ciberseguridad relacionados

Conserva origen, integridad y trazabilidad. Un cambio observado no identifica su causa ni autor; una copia transformada no debe presentarse como el original.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **evidencia original, alias, campos autorizados, manifiesto derivado**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué necesitas conservar para explicar la derivación sin difundir la tabla de identidades?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 007](ejercicio_007.md), [ejercicio 049](ejercicio_049.md), [ejercicio 079](ejercicio_079.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Mismo usuario en dos eventos → mismo alias.
2. Correo y token → no aparecen.
3. Huella derivada distinta del original → documentada, no alteración oculta.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Seudónimos y tiempos todavía pueden reidentificar. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una transformación legítima cambia huellas y no debe parecer evidencia original intacta. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Seudónimos y tiempos todavía pueden reidentificar. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [NIST SP 800-61r3: contexto de respuesta](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Seudónimos y tiempos todavía pueden reidentificar.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En forense, este razonamiento ayuda a proteger **privacidad de personas en un expediente** mediante paquete compartible con minimización de datos. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir selección de rango temporal con motivo de exclusión. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
