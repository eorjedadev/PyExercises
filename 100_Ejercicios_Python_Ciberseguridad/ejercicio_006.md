# Ejercicio 006 — Comprobación de huellas de archivos

[Índice](README.md#indice) · [Anterior](ejercicio_005.md) · [Siguiente](ejercicio_007.md)

### Escenario de seguridad

El analista recibe archivos inertes y un manifiesto SHA-256 de referencia.

### Contexto profesional

Ámbito: **Integridad**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Paquete de evidencia local. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **comprobación de huellas de archivos**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Resultado por ruta, huella observada y limitación de confianza**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 006](ejercicio_006/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/archivos/normal.txt](ejercicio_006/datos/archivos/normal.txt) — Archivo inerte para leer como bytes; conservar sin modificar.
- [datos/archivos/cambiado.txt](ejercicio_006/datos/archivos/cambiado.txt) — Archivo inerte para leer como bytes; conservar sin modificar.
- [datos/archivos/vacio.txt](ejercicio_006/datos/archivos/vacio.txt) — Archivo inerte para leer como bytes; conservar sin modificar.
- [datos/manifiesto.json](ejercicio_006/datos/manifiesto.json) — Rutas relativas a datos/archivos; referencia hipotética no autenticada.

### Requisitos

- Leer bytes de archivos regulares del paquete.
- comparar SHA-256 exacto tras validar 64 hexadecimales.
- ausente, distinto y verificado son estados separados.
- manifiesto no autenticado no prueba origen.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Resultado por ruta, huella observada y limitación de confianza. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Bytes, comparación de huellas y validación de formatos**: Comprobar igualdad respecto de una referencia sin confundirla con procedencia.
- **Archivos, rutas, bytes y excepciones**: Separar el objeto observado de la forma de leerlo, sin alterar evidencia.

### Conceptos de ciberseguridad relacionados

Una huella comprueba una relación entre bytes y referencia. Autenticidad, custodia de la referencia y origen son preguntas adicionales.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **hashlib y lectura binaria**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **pathlib y lectura con context managers**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **ruta relativa, huella de referencia, huella calculada, estado de integridad**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Quién respalda la referencia y qué significa realmente coincidir?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?

### Casos de prueba

1. normal.txt → coincide.
2. cambiado.txt → distinto.
3. ausente.txt → ausente.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un archivo vacío tiene una huella válida. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una actualización legítima cambia la huella. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un archivo vacío tiene una huella válida. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [Python: alcance de funciones hash](https://docs.python.org/3/library/hashlib.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/hashlib.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Un archivo vacío tiene una huella válida.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En integridad, este razonamiento ayuda a proteger **paquete de evidencia local** mediante comprobación de huellas de archivos. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir tamaño esperado sin reemplazar la comparación de huella. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
