# Ejercicio 025 — Auditoría conceptual de verificadores de contraseña

[Índice](README.md#indice) · [Anterior](ejercicio_024.md) · [Siguiente](ejercicio_026.md)

### Escenario de seguridad

Se recibe metadato sintético de verificadores, nunca contraseñas reales.

### Contexto profesional

Ámbito: **Criptografía aplicada**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Almacenamiento de credenciales. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **auditoría conceptual de verificadores de contraseña**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Desviaciones, información faltante y plan conceptual de migración tras autenticación legítima**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 025](ejercicio_025/README.md). Su README describe formatos, campos y procedencia sintética.

- [config/perfil_local.json](ejercicio_025/config/perfil_local.json) — Perfil pedagógico recibido, no implementar ni calcular scrypt para este ejercicio de metadatos.
- [datos/verificadores.json](ejercicio_025/datos/verificadores.json) — Solo metadatos sintéticos. No hay hashes de contraseñas que deban adivinarse.

### Requisitos

- Evaluar formato y parámetros contra perfil_local.json.
- clasificar algoritmos rápidos como no aptos para contraseña según perfil.
- salt debe cumplir tamaño local y no repetirse.
- no recuperar ni probar contraseñas.
- política es ejemplo versionado, no mínimo universal.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Desviaciones, información faltante y plan conceptual de migración tras autenticación legítima. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Contratos de APIs criptográficas y manejo de errores**: Usar primitivas mantenidas con entradas bien definidas, sin diseñar criptografía propia.
- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.

### Conceptos de ciberseguridad relacionados

Codificación, hash, HMAC, firma y cifrado ofrecen propiedades distintas. La clave, el formato exacto y el modelo de confianza forman parte del contrato.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **Elegir la API específica del mecanismo estudiado; no intercambiar hash, HMAC y cifrado**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **json, dict y excepciones específicas**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **esquema, parámetros declarados, salt sintético, versión de política**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Por qué un hash de integridad no es por sí mismo un verificador de contraseña adecuado?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?
- Recupera razonamiento de [ejercicio 006](ejercicio_006.md), [ejercicio 009](ejercicio_009.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. V1 parámetros y salt único conformes → sin desviación local.
2. V2 SHA-256 simple → no apto.
3. V3 y V4 salt repetido → revisión.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

No se puede verificar la implementación solo con metadatos declarados. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una migración puede dejar registros antiguos en transición controlada. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- No se puede verificar la implementación solo con metadatos declarados. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [OWASP: almacenamiento criptográfico](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — consulta el contrato y las excepciones, no copies una solución.
- [OWASP: almacenamiento de contraseñas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **No se puede verificar la implementación solo con metadatos declarados.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En criptografía aplicada, este razonamiento ayuda a proteger **almacenamiento de credenciales** mediante auditoría conceptual de verificadores de contraseña. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir estado pendiente de migración sin almacenar contraseñas. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
