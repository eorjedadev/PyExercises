# Ejercicio 029 — Cifrado autenticado y datos asociados

[Índice](README.md#indice) · [Anterior](ejercicio_028.md) · [Siguiente](ejercicio_030.md)

### Escenario de seguridad

Una muestra AES-GCM permite distinguir descifrado auténtico de mera transformación de bytes.

### Contexto profesional

Ámbito: **Criptografía aplicada**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Paquete sintético confidencial. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **cifrado autenticado y datos asociados**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Resultado autenticado o fallo uniforme y explicación de confidencialidad frente a integridad**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 029](ejercicio_029/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/vector.json](ejercicio_029/datos/vector.json) — Vector público AES-128-GCM de laboratorio. La etiqueta se almacena separada; la API puede pedir ciphertext y etiqueta concatenados. No generar nuevos mensajes con esta clave/nonce.
- [datos/variantes.json](ejercicio_029/datos/variantes.json) — Aplicar cada variante sobre una copia independiente del vector, sin modificarlo.
- [config/dependencia.json](ejercicio_029/config/dependencia.json) — Única dependencia externa de implementación obligatoria en estos ejercicios; el generador del material no requiere instalarla.

### Requisitos

- Verificar y descifrar con API mantenida AESGCM.
- entradas y clave son vectores públicos de laboratorio.
- no publicar texto parcial si falla etiqueta.
- registrar solo estado y longitud.
- no reutilizar clave/nonce de pruebas para nuevos mensajes reales.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Resultado autenticado o fallo uniforme y explicación de confidencialidad frente a integridad. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Contratos de APIs criptográficas y manejo de errores**: Usar primitivas mantenidas con entradas bien definidas, sin diseñar criptografía propia.
- **Representación binaria, codificación y límites de tamaño**: Medir y conservar los bytes que sustentan una comprobación.

### Conceptos de ciberseguridad relacionados

Codificación, hash, HMAC, firma y cifrado ofrecen propiedades distintas. La clave, el formato exacto y el modelo de confianza forman parte del contrato.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Investiga AESGCM de cryptography: clave, nonce, AAD y ciphertext con etiqueta. No liberes datos si falla la autenticación.

### Diseño de variables

Identifica estas entidades: **nonce, datos asociados, etiqueta, resultado autenticado**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Por qué no debes interpretar plaintext obtenido antes de autenticarlo?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 009](ejercicio_009.md), [ejercicio 026](ejercicio_026.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Vector de 16 bytes → recupera16 bytes.
2. Etiqueta alterada → rechazo sin texto.
3. AAD distinto del original vacío → rechazo.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

El fallo puede venir de clave, nonce, AAD o datos equivocados; no revela cuál. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un error de transporte produce el mismo fallo que una alteración intencional. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- El fallo puede venir de clave, nonce, AAD o datos equivocados; no revela cuál. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Bytes, Unicode y Codificación**; busca ese título en el índice.
- [OWASP: almacenamiento criptográfico](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://cryptography.io/en/stable/hazmat/primitives/aead/) — consulta el contrato y las excepciones, no copies una solución.
- [cryptography: cifrado autenticado AESGCM](https://cryptography.io/en/stable/hazmat/primitives/aead/).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **El fallo puede venir de clave, nonce, AAD o datos equivocados; no revela cuál.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En criptografía aplicada, este razonamiento ayuda a proteger **paquete sintético confidencial** mediante cifrado autenticado y datos asociados. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Diseñar una política de unicidad de nonce sin crear criptografía propia. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
