# Ejercicio 018 — Copias con contenido idéntico

[Índice](README.md#indice) · [Anterior](ejercicio_017.md) · [Siguiente](ejercicio_019.md)

### Escenario de seguridad

Una revisión forense necesita detectar copias sin perder sus distintas ubicaciones.

### Contexto profesional

Ámbito: **Forense**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Colección de documentos adquiridos. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **copias con contenido idéntico**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Grupos de equivalencia de contenido y manifestación de límites**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 018](ejercicio_018/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/archivos/a.txt](ejercicio_018/datos/archivos/a.txt) — Muestra inerte de equivalencia de contenido.
- [datos/archivos/copia.txt](ejercicio_018/datos/archivos/copia.txt) — Muestra inerte de equivalencia de contenido.
- [datos/archivos/otro.txt](ejercicio_018/datos/archivos/otro.txt) — Muestra inerte de equivalencia de contenido.
- [datos/archivos/vacio1](ejercicio_018/datos/archivos/vacio1) — Muestra inerte de equivalencia de contenido.
- [datos/archivos/vacio2](ejercicio_018/datos/archivos/vacio2) — Muestra inerte de equivalencia de contenido.

### Requisitos

- Comparar bytes y agrupar iguales.
- SHA-256 puede apoyar agrupación pero conservar todas las rutas.
- incluir vacíos.
- archivos ilegibles separados.
- no borrar duplicados.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Grupos de equivalencia de contenido y manifestación de límites. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Bytes, comparación de huellas y validación de formatos**: Comprobar igualdad respecto de una referencia sin confundirla con procedencia.
- **Archivos, rutas, bytes y excepciones**: Separar el objeto observado de la forma de leerlo, sin alterar evidencia.

### Conceptos de ciberseguridad relacionados

Conserva origen, integridad y trazabilidad. Un cambio observado no identifica su causa ni autor; una copia transformada no debe presentarse como el original.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **hashlib y lectura binaria**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **pathlib y lectura con context managers**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **ruta adquirida, huella, grupo de contenido, error de lectura**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Por qué no debes borrar una copia durante el análisis de evidencia?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?
- Recupera razonamiento de [ejercicio 006](ejercicio_006.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. a.txt y copia.txt → mismo grupo.
2. otro.txt → no duplica.
3. vacio1 y vacio2 → mismo grupo.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Coincidir contenido no prueba que dos rutas tengan el mismo origen. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Distribución legítima de plantillas produce duplicados. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Coincidir contenido no prueba que dos rutas tengan el mismo origen. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [NIST SP 800-61r3: contexto de respuesta](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/hashlib.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Coincidir contenido no prueba que dos rutas tengan el mismo origen.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En forense, este razonamiento ayuda a proteger **colección de documentos adquiridos** mediante copias con contenido idéntico. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Incorporar tiempos declarados sin usarlos para decidir igualdad. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
