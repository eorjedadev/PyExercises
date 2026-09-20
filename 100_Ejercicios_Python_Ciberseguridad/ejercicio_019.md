# Ejercicio 019 — Comparación de inventarios de integridad

[Índice](README.md#indice) · [Anterior](ejercicio_018.md) · [Siguiente](ejercicio_020.md)

### Escenario de seguridad

Hay dos manifiestos de una aplicación antes y después de un cambio.

### Contexto profesional

Ámbito: **Integridad**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Archivos de una aplicación. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **comparación de inventarios de integridad**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Cambios y resumen por categoría**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 019](ejercicio_019/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/antes.json](ejercicio_019/datos/antes.json) — Mapa ruta→huella. No requiere leer archivos fuera del paquete.
- [datos/despues.json](ejercicio_019/datos/despues.json) — Segunda captura del mismo alcance declarado.

### Requisitos

- Comparar por ruta exacta.
- clasificar añadido, retirado, huella distinta y sin cambio.
- validar huellas y rutas únicas.
- no tratar ausencia como hash vacío.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Cambios y resumen por categoría. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Bytes, comparación de huellas y validación de formatos**: Comprobar igualdad respecto de una referencia sin confundirla con procedencia.
- **Pertenencia, diferencia y conservación de identidad**: Comparar grupos sin confundir ausencia con un valor vacío.

### Conceptos de ciberseguridad relacionados

Una huella comprueba una relación entre bytes y referencia. Autenticidad, custodia de la referencia y origen son preguntas adicionales.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **hashlib y lectura binaria**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **set y dict cuando la identidad lo justifique**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **manifiesto anterior, manifiesto posterior, ruta, categoría de cambio**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué fuente confirmaría que ambas capturas cubren el mismo ámbito?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?
- Recupera razonamiento de [ejercicio 006](ejercicio_006.md), [ejercicio 018](ejercicio_018.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. app.cfg huella diferente → modificado.
2. nuevo.txt solo después → añadido.
3. viejo.txt solo antes → retirado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un manifiesto incompleto puede aparentar eliminaciones. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una entrega autorizada también modifica archivos. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un manifiesto incompleto puede aparentar eliminaciones. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Conjuntos**; busca ese título en el índice.
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

Contrasta tu resultado con esta limitación: **Un manifiesto incompleto puede aparentar eliminaciones.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En integridad, este razonamiento ayuda a proteger **archivos de una aplicación** mediante comparación de inventarios de integridad. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Cruzar con un registro de despliegue autorizado. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
