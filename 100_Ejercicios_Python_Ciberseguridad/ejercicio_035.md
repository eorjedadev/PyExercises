# Ejercicio 035 — Validación de origen para acciones con sesión

[Índice](README.md#indice) · [Anterior](ejercicio_034.md) · [Siguiente](ejercicio_036.md)

### Escenario de seguridad

Un laboratorio modela una comprobación CSRF sin servidor externo.

### Contexto profesional

Ámbito: **Web**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Cambios de estado autenticados por cookie. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **validación de origen para acciones con sesión**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Decisión por solicitud y razones de rechazo sin exponer token**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 035](ejercicio_035/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/solicitudes.json](ejercicio_035/datos/solicitudes.json) — Tokens públicos ficticios para un modelo de decisión, no generación profesional de secretos.
- [config/parametros.json](ejercicio_035/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Métodos seguros GET/HEAD no ejecutan cambios.
- POST de sesión requiere token de prueba coincidente y Origin exactamente permitido.
- ausencias deniegan.
- no presentar Origin como autenticación ni esta simulación como protección universal.
- GET/HEAD sin cambio se clasifican como lectura sin efecto, no necesitan token en este modelo.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Decisión por solicitud y razones de rechazo sin exponer token. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Interpretación de campos, formatos y resultados de controles**: No confundir un texto declarado por el cliente con un dato confiado.
- **Transiciones, invariantes y funciones con efectos delimitados**: Explicar qué puede cambiar al aceptar o rechazar una operación.

### Conceptos de ciberseguridad relacionados

Autenticación, autorización y controles del navegador tienen alcances distintos. Una respuesta HTTP o una cabecera aislada no acredita todos ellos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- Funciones de validación; urllib.parse para URLs cuando corresponda; justifica su necesidad y el límite de su garantía.
- Funciones; clases solo si protegen invariantes; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **método, origen declarado, verificación de token, acción con efecto**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué diferencia hay entre autenticación, autorización y comprobación CSRF?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 012](ejercicio_012.md), [ejercicio 031](ejercicio_031.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. POST válido y origen app.example.test → permite.
2. POST sin token → deniega.
3. GET declarado para cambio → deniega cambio.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Algunos clientes legítimos pueden no enviar Origin y requieren contrato específico. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Integraciones heredadas pueden fallar una política de navegador. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Algunos clientes legítimos pueden no enviar Origin y requieren contrato específico. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Programación Orientada a Objetos**; busca ese título en el índice.
- [OWASP: autorización](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Algunos clientes legítimos pueden no enviar Origin y requieren contrato específico.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En web, este razonamiento ayuda a proteger **cambios de estado autenticados por cookie** mediante validación de origen para acciones con sesión. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir un flujo no basado en cookies con contrato separado. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
