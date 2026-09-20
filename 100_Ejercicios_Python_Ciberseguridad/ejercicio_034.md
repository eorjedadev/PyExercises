# Ejercicio 034 — Atributos de cookies de sesión

[Índice](README.md#indice) · [Anterior](ejercicio_033.md) · [Siguiente](ejercicio_035.md)

### Escenario de seguridad

El equipo exporta cookies de una aplicación HTTPS para revisar una política local.

### Contexto profesional

Ámbito: **Web**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Credenciales de sesión del navegador. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **atributos de cookies de sesión**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Desviaciones y excepciones por nombre de cookie**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 034](ejercicio_034/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/cookies.json](ejercicio_034/datos/cookies.json) — No incluye valores de cookies. Campos de controles son booleanos reales.

### Requisitos

- Para tipo sesion exigir Secure, HttpOnly y SameSite Lax o Strict.
- SameSite None solo con excepción aprobada y Secure.
- cookies de preferencia se informan sin imponer HttpOnly.
- no incluir valores de cookies.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Desviaciones y excepciones por nombre de cookie. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Interpretación de campos, formatos y resultados de controles**: No confundir un texto declarado por el cliente con un dato confiado.
- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.

### Conceptos de ciberseguridad relacionados

Autenticación, autorización y controles del navegador tienen alcances distintos. Una respuesta HTTP o una cabecera aislada no acredita todos ellos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- Funciones de validación; urllib.parse para URLs cuando corresponda; justifica su necesidad y el límite de su garantía.
- json, dict y excepciones específicas; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **nombre de cookie, propósito, atributos declarados, excepción**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué amenaza trata cada atributo y cuál no trata?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 008](ejercicio_008.md), [ejercicio 012](ejercicio_012.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. sid sin HttpOnly → desviación.
2. sid2 con todos y Lax → conforme.
3. pref de tipo preferencia → fuera de regla de sesión.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Los atributos declarados no prueban rotación o revocación correctas. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una integración entre sitios puede requerir una excepción SameSite documentada. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Los atributos declarados no prueban rotación o revocación correctas. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [OWASP: autorización](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) — consulta el contrato y las excepciones, no copies una solución.
- [OWASP: sesiones y cookies](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Los atributos declarados no prueban rotación o revocación correctas.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En web, este razonamiento ayuda a proteger **credenciales de sesión del navegador** mediante atributos de cookies de sesión. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Revisar amplitud de Path y Domain con política recibida. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
