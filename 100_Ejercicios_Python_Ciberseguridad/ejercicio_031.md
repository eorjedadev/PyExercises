# Ejercicio 031 — Autorización por propietario de objeto

[Índice](README.md#indice) · [Anterior](ejercicio_030.md) · [Siguiente](ejercicio_032.md)

### Escenario de seguridad

Una aplicación local debe decidir acceso sin confiar en un identificador elegido por el cliente.

### Contexto profesional

Ámbito: **Web**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Documentos privados de usuarios. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **autorización por propietario de objeto**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Decisiones y trazas internas por id de solicitud**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 031](ejercicio_031/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/identidades.json](ejercicio_031/datos/identidades.json) — Identidades autenticadas por supuesto del laboratorio; no implementar login.
- [datos/objetos.json](ejercicio_031/datos/objetos.json) — Inventario de propietarios. No incluir name de objetos ajenos en respuestas públicas.
- [datos/solicitudes.json](ejercicio_031/datos/solicitudes.json) — Peticiones locales como datos; no exigen servidor.

### Requisitos

- Solicitudes con actor autenticado, objeto y acción leer.
- autorizar propietario o rol auditor.
- desconocidos se deniegan.
- resultado no debe revelar nombre del objeto ajeno.
- no basta que actor esté autenticado.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Decisiones y trazas internas por id de solicitud. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.
- **Transiciones, invariantes y funciones con efectos delimitados**: Explicar qué puede cambiar al aceptar o rechazar una operación.

### Conceptos de ciberseguridad relacionados

Autenticación, autorización y controles del navegador tienen alcances distintos. Una respuesta HTTP o una cabecera aislada no acredita todos ellos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- json, dict y excepciones específicas; justifica su necesidad y el límite de su garantía.
- Funciones; clases solo si protegen invariantes; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **actor autenticado, propietario del objeto, acción, decisión**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Dónde debe decidirse el acceso aunque cambie la interfaz?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 011](ejercicio_011.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. ana lee objeto de ana → permite.
2. beto lee objeto de ana sin rol → deniega.
3. auditor lee objeto existente → permite.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Ocultar el enlace no sustituye la autorización del servidor. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una auditoría aprobada puede leer documentos de otros usuarios. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Ocultar el enlace no sustituye la autorización del servidor. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Programación Orientada a Objetos**; busca ese título en el índice.
- [OWASP: autorización](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/json.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Ocultar el enlace no sustituye la autorización del servidor.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En web, este razonamiento ayuda a proteger **documentos privados de usuarios** mediante autorización por propietario de objeto. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Separar lectura y modificación con permisos diferentes. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
