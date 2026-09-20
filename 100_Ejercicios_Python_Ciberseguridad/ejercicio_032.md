# Ejercicio 032 — Pruebas de consultas parametrizadas

[Índice](README.md#indice) · [Anterior](ejercicio_031.md) · [Siguiente](ejercicio_033.md)

### Escenario de seguridad

Debes construir una búsqueda exacta sobre SQLite usando datos de ejemplo sin interpretar entradas como SQL.

### Contexto profesional

Ámbito: **Desarrollo seguro**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Directorio de una aplicación local. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **pruebas de consultas parametrizadas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Resultados exactos y pruebas de entradas tratadas como datos**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 032](ejercicio_032/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/usuarios.json](ejercicio_032/datos/usuarios.json) — Semilla para tabla SQLite temporal usuarios(id entero único,nombre texto); solo estos campos.
- [datos/consultas.json](ejercicio_032/datos/consultas.json) — Entradas literales de consulta para probar que no cambian la estructura SQL.

### Requisitos

- Crear base temporal desde usuarios.json.
- búsqueda exacta por nombre mediante parámetros, no concatenación.
- no aceptar nombres de tabla del usuario.
- mostrar solo id y nombre.
- no modificar datos al consultar.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Resultados exactos y pruebas de entradas tratadas como datos. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Consultas parametrizadas y datos persistidos localmente**: Separar valores recibidos de la estructura de una consulta.
- **Pruebas de contrato, regresión y fallos simulados**: Contrastar observaciones esperadas sin reproducir el algoritmo como oráculo.

### Conceptos de ciberseguridad relacionados

Toda entrada externa requiere un contrato. Validar, codificar según contexto y minimizar datos de salida son responsabilidades diferentes.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Investiga sqlite3, parámetros de consulta y cierre de conexiones. El problema exige una base temporal, no un servidor.

### Diseño de variables

Identifica estas entidades: **término literal, parámetro de consulta, filas encontradas, conexión temporal**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Por qué rechazar toda comilla dañaría el contrato?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 015](ejercicio_015.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Ana → solo Ana.
2. O'Neil → su registro literal.
3. texto que parece expresión SQL → sin coincidencia si no existe literal.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Parametrizar valores no parametriza identificadores de tablas. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Nombres legítimos pueden contener comillas. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Parametrizar valores no parametriza identificadores de tablas. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Bases de Datos con Python**; busca ese título en el índice.
- [INTENSIVO DE PYTHON (Eric Matthes).md](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md) — **11. Probar el código**; busca ese título en el índice.
- [OWASP: logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/sqlite3.html) — consulta el contrato y las excepciones, no copies una solución.
- [OWASP: prevención de inyección SQL](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Parametrizar valores no parametriza identificadores de tablas.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En desarrollo seguro, este razonamiento ayuda a proteger **directorio de una aplicación local** mediante pruebas de consultas parametrizadas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir búsqueda por prefijo definiendo cómo se tratan comodines. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
