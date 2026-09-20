# Ejercicio 001 — Inventario de extensiones de riesgo

[Índice](README.md#indice) · [Siguiente](ejercicio_002.md)

### Escenario de seguridad

El área de soporte recibe un listado de adjuntos y necesita revisar nombres sin abrirlos.

### Contexto profesional

Ámbito: **Archivos**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Estación de recepción documental. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **inventario de extensiones de riesgo**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Inventario por extensión, motivos de revisión y registros inválidos**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 001](ejercicio_001/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/inventario.csv](ejercicio_001/datos/inventario.csv) — Nombres y tamaños declarados; no existen ejecutables detrás de estas rutas.

### Requisitos

- Comparar última extensión sin distinguir mayúsculas.
- revisar exe, js, ps1 y nombres con una extensión anterior pdf/docx seguida de ejecutable.
- no modificar ni abrir rutas.
- bytes deben ser enteros no negativos.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Inventario por extensión, motivos de revisión y registros inválidos. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Cadenas, comparación y validación**: Conservar la entrada original y definir exactamente qué se normaliza.
- **Archivos, rutas, bytes y excepciones**: Separar el objeto observado de la forma de leerlo, sin alterar evidencia.

### Conceptos de ciberseguridad relacionados

El nombre, la extensión y el contenido son evidencias distintas. Una política de recepción reduce riesgos, pero no certifica inocuidad.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **str, métodos de cadenas**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **pathlib y lectura con context managers**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **nombre observado, extensión final, tamaño declarado, motivo de revisión**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué puedes afirmar del nombre sin conocer el contenido?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?

### Casos de prueba

1. F02 factura.pdf.exe → revisión por ejecutable y doble extensión.
2. F01 informe.PDF → sin regla activada.
3. F06 tamaño negativo → inválido.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un archivo sin extensión no es necesariamente inocuo. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un script administrativo legítimo también activa la regla. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un archivo sin extensión no es necesariamente inocuo. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Métodos de Cadenas**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [OWASP: carga de archivos](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/re.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Un archivo sin extensión no es necesariamente inocuo.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En archivos, este razonamiento ayuda a proteger **estación de recepción documental** mediante inventario de extensiones de riesgo. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Incorporar una lista de excepciones con propietario y fecha de caducidad. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
