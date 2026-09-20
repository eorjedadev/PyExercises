# Ejercicio 086 — Revisión de manifiestos de contenedores

[Índice](README.md#indice) · [Anterior](ejercicio_085.md) · [Siguiente](ejercicio_087.md)

### Escenario de seguridad

Manifiestos JSON simplificados describen controles antes de un despliegue ficticio.

### Contexto profesional

Ámbito: **DevSecOps**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Aislamiento de cargas de laboratorio. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **revisión de manifiestos de contenedores**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Informe de controles y contexto de excepciones**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 086](ejercicio_086/README.md). Su README describe formatos, campos y procedencia sintética.

- [config/cargas.json](ejercicio_086/config/cargas.json) — Modelo JSON explícito, no manifiesto ejecutable ni comando para desplegar.
- [datos/excepciones.json](ejercicio_086/datos/excepciones.json) — La excepción aporta contexto; conservar la observación del control elevado.

### Requisitos

- Revisar privileged verdadero, run_as_uid0, montaje de socket del motor y rootfs no readonly.
- ausencia → no especificado.
- no ejecutar contenedores.
- cada control produce observación separada.
- no asumir escape de contenedor.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Informe de controles y contexto de excepciones. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Estructuras anidadas, tipos y contratos de entrada.
- Condiciones, tipos y precedencia de políticas.

### Conceptos de ciberseguridad relacionados

La configuración declarada, su contexto de despliegue y su estado efectivo deben distinguirse. La revisión automatizada cubre un contrato específico.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **carga, identidad de ejecución, privilegio declarado, montaje sensible**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué controles efectivos solo conocerías al observar el entorno desplegado?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 015](ejercicio_015.md), [ejercicio 046](ejercicio_046.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. C1 privileged verdadero → revisión.
2. C2 uid1000 y controles conformes → sin desviación del perfil.
3. UID ausente → no especificado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un valor explícito no prueba el estado del runtime. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Agentes de infraestructura pueden requerir capacidades elevadas aprobadas. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un valor explícito no prueba el estado del runtime. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Condicionales**; busca ese título en el índice.
- [CIS Controls: contexto de defensa de activos](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Un valor explícito no prueba el estado del runtime.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En devsecops, este razonamiento ayuda a proteger **aislamiento de cargas de laboratorio** mediante revisión de manifiestos de contenedores. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir lista de capacidades permitidas por rol de carga. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
