# Ejercicio 028 — Firma de un artefacto inerte

[Índice](README.md#indice) · [Anterior](ejercicio_027.md) · [Siguiente](ejercicio_029.md)

### Escenario de seguridad

Se aporta un vector Ed25519 público de prueba y variantes de un archivo para estudiar autenticidad.

### Contexto profesional

Ámbito: **Criptografía aplicada**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Procedencia de una entrega. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **firma de un artefacto inerte**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Verificación y explicación de por qué confianza en la clave es un requisito separado**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 028](ejercicio_028/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/mensaje.bin](ejercicio_028/datos/mensaje.bin) — Mensaje de longitud cero del vector público Ed25519; es un archivo vacío intencional.
- [datos/alterado.bin](ejercicio_028/datos/alterado.bin) — Mensaje alterado: un byte adicional.
- [config/verificacion.json](ejercicio_028/config/verificacion.json) — Vector público de RFC8032 sección7.1 TEST1; no se entrega clave privada.
- [datos/clave_truncada.json](ejercicio_028/datos/clave_truncada.json) — Caso de formato incorrecto; no reemplaza la configuración válida.
- [config/dependencia.json](ejercicio_028/config/dependencia.json) — Única dependencia externa de implementación obligatoria en estos ejercicios; el generador del material no requiere instalarla.

### Requisitos

- Usar una biblioteca mantenida para verificar Ed25519.
- vector de RFC8032 es público y no se usa en producción.
- clave pública fijada por el laboratorio.
- distinguir firma incorrecta, formato inválido y verificación correcta.
- no implementar algoritmo criptográfico.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Verificación y explicación de por qué confianza en la clave es un requisito separado. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Contratos de APIs criptográficas y manejo de errores**: Usar primitivas mantenidas con entradas bien definidas, sin diseñar criptografía propia.
- **Representación binaria, codificación y límites de tamaño**: Medir y conservar los bytes que sustentan una comprobación.

### Conceptos de ciberseguridad relacionados

Codificación, hash, HMAC, firma y cifrado ofrecen propiedades distintas. La clave, el formato exacto y el modelo de confianza forman parte del contrato.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Investiga Ed25519PublicKey.verify en cryptography y sus excepciones. Se usa una clave pública fijada por el laboratorio; no implementes aritmética criptográfica.

### Diseño de variables

Identifica estas entidades: **clave pública confiada, firma, bytes firmados, estado de verificación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Quién vincula una clave pública con el editor que dices reconocer?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 006](ejercicio_006.md), [ejercicio 026](ejercicio_026.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. mensaje vacío del vector → firma válida.
2. mismo vector con byte extra → inválida.
3. clave pública truncada → formato inválido.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Una firma válida de un archivo no afirma que el archivo sea seguro. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Transformaciones inocentes de bytes invalidan firmas. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Una firma válida de un archivo no afirma que el archivo sea seguro. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Bytes, Unicode y Codificación**; busca ese título en el índice.
- [OWASP: almacenamiento criptográfico](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://cryptography.io/en/stable/hazmat/primitives/asymmetric/ed25519/) — consulta el contrato y las excepciones, no copies una solución.
- [cryptography: verificación Ed25519](https://cryptography.io/en/stable/hazmat/primitives/asymmetric/ed25519/).
- [RFC8032: vectores Ed25519, sección7.1](https://www.rfc-editor.org/rfc/rfc8032.html#section-7.1).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Una firma válida de un archivo no afirma que el archivo sea seguro.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En criptografía aplicada, este razonamiento ayuda a proteger **procedencia de una entrega** mediante firma de un artefacto inerte. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir dos editores y seleccionar clave solo desde un registro confiado. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
