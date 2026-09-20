# Ejercicio 017 — Clasificación de rutas de una carga

[Índice](README.md#indice) · [Anterior](ejercicio_016.md) · [Siguiente](ejercicio_018.md)

### Escenario de seguridad

La aplicación recibe nombres de archivo ajenos y necesita validar su forma antes de escribir.

### Contexto profesional

Ámbito: **Archivos**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Directorio de recepción de ficheros. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **clasificación de rutas de una carga**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Aceptación o causas por nombre propuesto**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 017](ejercicio_017/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/nombres.json](ejercicio_017/datos/nombres.json) — Nombres como datos; no crear,abrir ni resolver ninguna ruta propuesta.

### Requisitos

- Solo nombre simple: rechazar vacío, . y .., separadores / o barra inversa, NUL, dos puntos y rutas absolutas.
- no crear archivos.
- explicar que validación de nombre no controla enlaces simbólicos ni carreras.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Aceptación o causas por nombre propuesto. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Identidad de rutas y semántica por plataforma**: Analizar rutas como datos sin abrir ni seguir destinos ajenos al laboratorio.
- **Archivos, rutas, bytes y excepciones**: Separar el objeto observado de la forma de leerlo, sin alterar evidencia.

### Conceptos de ciberseguridad relacionados

El nombre, la extensión y el contenido son evidencias distintas. Una política de recepción reduce riesgos, pero no certifica inocuidad.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **pathlib, PurePosixPath y PureWindowsPath según el contrato**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **pathlib y lectura con context managers**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **nombre no confiable, causa de rechazo, nombre admitido, ámbito de validación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué garantías faltan entre aceptar un nombre y abrir un archivo seguro?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?
- Recupera razonamiento de [ejercicio 001](ejercicio_001.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. informe.txt → aceptado.
2. ../secreto.txt y C:nota.txt → rechazados.
3. carpeta/nota.txt → rechazado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Los nombres reservados Windows requieren una política adicional. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un cliente puede enviar una ruta completa por error sin intento malicioso. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Los nombres reservados Windows requieren una política adicional. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [OWASP: carga de archivos](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/pathlib.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Los nombres reservados Windows requieren una política adicional.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En archivos, este razonamiento ayuda a proteger **directorio de recepción de ficheros** mediante clasificación de rutas de una carga. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Incorporar nombres reservados de Windows con pruebas comparables. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
