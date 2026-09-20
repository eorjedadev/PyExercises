# Ejercicio 037 — Preinspección de un archivo comprimido

[Índice](README.md#indice) · [Anterior](ejercicio_036.md) · [Siguiente](ejercicio_038.md)

### Escenario de seguridad

Se entrega un manifiesto de miembros de archivo, no un comprimido peligroso.

### Contexto profesional

Ámbito: **Archivos**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Carpeta de extracción de laboratorio. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **preinspección de un archivo comprimido**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Plan admisible o rechazado y causas por miembro y paquete**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 037](ejercicio_037/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/miembros.json](ejercicio_037/datos/miembros.json) — Manifiesto ficticio, no ZIP real: analizar cada miembro y decisión global. Z1 puede probarse solo en una copia.

### Requisitos

- No extraer.
- rutas relativas POSIX sin .. ni raíz ni enlaces.
- máximos100 miembros,1MiB por miembro y 5MiB total.
- razón descomprimido/comprimido mayor 100 se revisa, tamaño comprimido0 con contenido positivo se rechaza.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Plan admisible o rechazado y causas por miembro y paquete. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Identidad de rutas y semántica por plataforma**: Analizar rutas como datos sin abrir ni seguir destinos ajenos al laboratorio.
- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.

### Conceptos de ciberseguridad relacionados

El nombre, la extensión y el contenido son evidencias distintas. Una política de recepción reduce riesgos, pero no certifica inocuidad.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- pathlib, PurePosixPath y PureWindowsPath según el contrato; justifica su necesidad y el límite de su garantía.
- dict, list, collections; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **ruta del miembro, tipo declarado, bytes previstos, presupuesto de extracción**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Por qué la extracción necesitaría límites durante la escritura aunque el manifiesto pase?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 001](ejercicio_001.md), [ejercicio 017](ejercicio_017.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. docs/a.txt pequeño → admisible.
2. ../fuera.txt → rechazado.
3. Miembro de 2MiB → excede límite.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Metadatos declarados no garantizan tamaño real durante extracción. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Texto altamente repetitivo puede comprimir mucho legítimamente. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Metadatos declarados no garantizan tamaño real durante extracción. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
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

Contrasta tu resultado con esta limitación: **Metadatos declarados no garantizan tamaño real durante extracción.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En archivos, este razonamiento ayuda a proteger **carpeta de extracción de laboratorio** mediante preinspección de un archivo comprimido. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir límite real de bytes escritos en un laboratorio propio. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
