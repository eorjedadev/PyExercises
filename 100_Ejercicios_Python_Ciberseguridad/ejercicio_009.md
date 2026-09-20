# Ejercicio 009 — Diferencia entre codificar y proteger

[Índice](README.md#indice) · [Anterior](ejercicio_008.md) · [Siguiente](ejercicio_010.md)

### Escenario de seguridad

Un equipo llama cifrados a unos campos Base64 y debes comprobar la afirmación.

### Contexto profesional

Ámbito: **Criptografía aplicada**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Tratamiento de datos exportados. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **diferencia entre codificar y proteger**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Clasificación válida/inválida/excede límite y conclusión sobre confidencialidad**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 009](ejercicio_009/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/codificados.json](ejercicio_009/datos/codificados.json) — Base64 textual; no son contraseñas ni material privado.

### Requisitos

- Decodificar Base64 estándar con validación estricta.
- limitar entrada a1024 caracteres.
- informar bytes recuperados, no asumir texto UTF-8.
- recuperar no implica autorización para publicar el contenido.
- salida solo tamaño y clasificación.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Clasificación válida/inválida/excede límite y conclusión sobre confidencialidad. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Representación binaria, codificación y límites de tamaño**: Medir y conservar los bytes que sustentan una comprobación.
- **Contratos de APIs criptográficas y manejo de errores**: Usar primitivas mantenidas con entradas bien definidas, sin diseñar criptografía propia.

### Conceptos de ciberseguridad relacionados

Codificación, hash, HMAC, firma y cifrado ofrecen propiedades distintas. La clave, el formato exacto y el modelo de confianza forman parte del contrato.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **bytes, encode/decode y base64 cuando el formato lo requiera**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **Elegir la API específica del mecanismo estudiado; no intercambiar hash, HMAC y cifrado**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **cadena recibida, tamaño codificado, bytes recuperados, estado de decodificación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué propiedad de confidencialidad ofrece realmente esta transformación?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?

### Casos de prueba

1. QW5h → 3 bytes recuperables.
2. %%% → inválida.
3. cadena vacía → 0 bytes, válida.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Datos binarios válidos no siempre representan texto. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Codificar datos públicos es normal y no es un hallazgo por sí solo. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Datos binarios válidos no siempre representan texto. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Bytes, Unicode y Codificación**; busca ese título en el índice.
- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [OWASP: almacenamiento criptográfico](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/base64.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Datos binarios válidos no siempre representan texto.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En criptografía aplicada, este razonamiento ayuda a proteger **tratamiento de datos exportados** mediante diferencia entre codificar y proteger. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Separar errores de codificación y errores de interpretación UTF-8. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
