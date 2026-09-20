# Ejercicio 073 — Cobertura temporal antes de concluir ausencia

[Índice](README.md#indice) · [Anterior](ejercicio_072.md) · [Siguiente](ejercicio_074.md)

### Escenario de seguridad

Se solicitan conclusiones sobre un intervalo con fuentes incompletas.

### Contexto profesional

Ámbito: **Forense**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Fiabilidad de una investigación. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **cobertura temporal antes de concluir ausencia**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Matriz de cobertura, huecos y límites de conclusiones**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 073](ejercicio_073/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/cobertura.json](ejercicio_073/datos/cobertura.json) — Intervalos de observación declarados; endpoint no tiene cobertura.
- [config/parametros.json](ejercicio_073/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Unir intervalos de cobertura de cada fuente.
- extremos [inicio, fin).
- calcular huecos frente al periodo solicitado.
- fuentes requeridas enumeradas.
- no afirmar ausencia de actividad en huecos.
- cobertura no prueba calidad de detección.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Matriz de cobertura, huecos y límites de conclusiones. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Zonas, intervalos, orden e incertidumbre.
- Pertenencia, diferencia y conservación de identidad.

### Conceptos de ciberseguridad relacionados

Conserva origen, integridad y trazabilidad. Un cambio observado no identifica su causa ni autor; una copia transformada no debe presentarse como el original.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **periodo investigado, cobertura declarada, hueco, fuente requerida**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué parte de tu conclusión cambia al descubrir un hueco?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 013](ejercicio_013.md), [ejercicio 054](ejercicio_054.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Coberturas[0,10),[10,20) → sin hueco en[0,20).
2. [0,9),[10,20) → hueco[9,10).
3. Fuente sin cobertura → todo incierto.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Eventos puntuales no definen por sí mismos un intervalo de observación completo. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Mantenimiento y rotación incompleta explican lagunas. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Eventos puntuales no definen por sí mismos un intervalo de observación completo. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Conjuntos**; busca ese título en el índice.
- [NIST SP 800-61r3: contexto de respuesta](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Eventos puntuales no definen por sí mismos un intervalo de observación completo.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En forense, este razonamiento ayuda a proteger **fiabilidad de una investigación** mediante cobertura temporal antes de concluir ausencia. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir estado de salud por clase de evento. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
