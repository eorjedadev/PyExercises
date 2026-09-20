# Ejercicio 033 — Salida HTML en contexto de texto

[Índice](README.md#indice) · [Anterior](ejercicio_032.md) · [Siguiente](ejercicio_034.md)

### Escenario de seguridad

Nombres no confiables aparecen en un reporte y no deben convertirse en marcado.

### Contexto profesional

Ámbito: **Web**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Reporte que abre un analista. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **salida html en contexto de texto**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Reporte inerte y pruebas que demuestren que el contenido no crea etiquetas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 033](ejercicio_033/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/nombres.json](ejercicio_033/datos/nombres.json) — Texto inerte sin scripts ni recursos externos. Solo se inserta en nodos de texto.

### Requisitos

- Generar HTML solo para nodos de texto dentro de celdas.
- escapar caracteres según ese contexto.
- no insertar datos en scripts, estilos, URLs o atributos.
- conservar significado visible.
- no abrir navegador necesario para validar.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Reporte inerte y pruebas que demuestren que el contenido no crea etiquetas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Interpretación de campos, formatos y resultados de controles**: No confundir un texto declarado por el cliente con un dato confiado.
- **Cadenas, comparación y validación**: Conservar la entrada original y definir exactamente qué se normaliza.

### Conceptos de ciberseguridad relacionados

Autenticación, autorización y controles del navegador tienen alcances distintos. Una respuesta HTTP o una cabecera aislada no acredita todos ellos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Investiga html.escape para nodos de texto y comprueba por qué ese contrato no cubre JavaScript, CSS ni URLs.

### Diseño de variables

Identifica estas entidades: **texto no confiable, contexto de salida, texto escapado, celda del reporte**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿En qué contexto exacto se insertan los datos?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 007](ejercicio_007.md), [ejercicio 009](ejercicio_009.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Nombre Ana → visible Ana.
2. Nombre <b>Ana</b> → texto literal, no negrita.
3. Nombre con & → entidad escapada en archivo.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Escapar para HTML no protege otros contextos. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un nombre que incluye signos puede ser completamente legítimo. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Escapar para HTML no protege otros contextos. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [Diccionario_Python.md](../Diccionario_Python.md) — **Métodos de Cadenas**; busca ese título en el índice.
- [OWASP: autorización](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://docs.python.org/3/library/html.html) — consulta el contrato y las excepciones, no copies una solución.
- [OWASP: codificación de salida por contexto](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
- [Python: html.escape](https://docs.python.org/3/library/html.html).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Escapar para HTML no protege otros contextos.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En web, este razonamiento ayuda a proteger **reporte que abre un analista** mediante salida html en contexto de texto. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir enlaces solo tras definir un contrato distinto de validación de URL. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
