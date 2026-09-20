# Ejercicio 036 — Decisión de destino de un conector

[Índice](README.md#indice) · [Anterior](ejercicio_035.md) · [Siguiente](ejercicio_037.md)

### Escenario de seguridad

Una función debe decidir si una URL pertenece al único servicio permitido antes de plantear una conexión.

### Contexto profesional

Ámbito: **Web**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Conector que procesa URLs ajenas. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **decisión de destino de un conector**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Aceptación de forma y motivos, con limitaciones explícitas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 036](ejercicio_036/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/urls.json](ejercicio_036/datos/urls.json) — URLs de documentación; nunca resolver ni contactar estos destinos.

### Requisitos

- Sin realizar solicitudes ni DNS.
- permitir solo https, hostname exacto api.example.test, puerto omitido o443 y sin credenciales.
- ruta cualquiera.
- URL malformada rechazada.
- decisión lexical no resuelve DNS rebinding ni redirecciones.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Aceptación de forma y motivos, con limitaciones explícitas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Interpretación de campos, formatos y resultados de controles**: No confundir un texto declarado por el cliente con un dato confiado.
- **Identidad de rutas y semántica por plataforma**: Analizar rutas como datos sin abrir ni seguir destinos ajenos al laboratorio.

### Conceptos de ciberseguridad relacionados

Autenticación, autorización y controles del navegador tienen alcances distintos. Una respuesta HTTP o una cabecera aislada no acredita todos ellos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- Funciones de validación; urllib.parse para URLs cuando corresponda; justifica su necesidad y el límite de su garantía.
- pathlib, PurePosixPath y PureWindowsPath según el contrato; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **URL recibida, hostname analizado, puerto efectivo, decisión lexical**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué controles faltan antes de permitir salida de red real?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 003](ejercicio_003.md), [ejercicio 017](ejercicio_017.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. https://api.example.test/v1 → aceptada en forma.
2. https://api.example.test.evil.test → rechazada.
3. http://api.example.test → rechazada.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

El nombre permitido podría resolver inesperadamente; el ejercicio no garantiza seguridad de conexión. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una URL con puerto8443 legítimo se rechaza por política. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- El nombre permitido podría resolver inesperadamente; el ejercicio no garantiza seguridad de conexión. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [OWASP: autorización](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/urllib.parse.html) — consulta el contrato y las excepciones, no copies una solución.
- [OWASP: prevención de SSRF](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **El nombre permitido podría resolver inesperadamente; el ejercicio no garantiza seguridad de conexión.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En web, este razonamiento ayuda a proteger **conector que procesa urls ajenas** mediante decisión de destino de un conector. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Analizar respuestas DNS sintéticas antes de aprobar destino. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
