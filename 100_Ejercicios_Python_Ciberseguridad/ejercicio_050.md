# Ejercicio 050 — Plan de retención y preservación

[Índice](README.md#indice) · [Anterior](ejercicio_049.md) · [Siguiente](ejercicio_051.md)

### Escenario de seguridad

Hay artefactos con edades distintas y algunos están bajo preservación por incidente.

### Contexto profesional

Ámbito: **Respuesta a incidentes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Disponibilidad de evidencia. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **plan de retención y preservación**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Conservar/eligible para revisión de retiro/preservación e ids de justificación**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 050](ejercicio_050/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/artefactos.json](ejercicio_050/datos/artefactos.json) — Edad computada desde acquired_at; hold booleano. No se entrega ninguna operación de borrado.
- [config/parametros.json](ejercicio_050/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Solo generar plan, nunca borrar.
- corte explícito.
- retención local30 días desde adquisición.
- exactamente 30 cumple plazo.
- hold activo prevalece.
- fecha futura se marca inválida.
- política no representa obligación legal.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Conservar/eligible para revisión de retiro/preservación e ids de justificación. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Zonas, intervalos, orden e incertidumbre**: Comparar instantes y fronteras temporales con una referencia explícita.
- **Transiciones, invariantes y funciones con efectos delimitados**: Explicar qué puede cambiar al aceptar o rechazar una operación.

### Conceptos de ciberseguridad relacionados

Relaciona afirmaciones con evidencia, documenta incertidumbre y distingue propuesta de acción de autorización para ejecutarla.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- datetime y timedelta; justifica su necesidad y el límite de su garantía.
- Funciones; clases solo si protegen invariantes; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **fecha de adquisición, plazo local, preservación activa, decisión propuesta**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué aprobación faltaría antes de eliminar realmente algo?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 012](ejercicio_012.md), [ejercicio 049](ejercicio_049.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Edad31 sin hold → elegible para revisión.
2. Edad31 con hold → preservar.
3. Edad29 → conservar.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

La finalización de hold requiere una decisión registrada, no un cálculo de edad. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Grandes volúmenes retenidos pueden ser necesarios por investigación activa. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- La finalización de hold requiere una decisión registrada, no un cálculo de edad. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Programación Orientada a Objetos**; busca ese título en el índice.
- [NIST SP 800-61r3: respuesta a incidentes](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/datetime.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **La finalización de hold requiere una decisión registrada, no un cálculo de edad.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En respuesta a incidentes, este razonamiento ayuda a proteger **disponibilidad de evidencia** mediante plan de retención y preservación. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Separar políticas por clase de evidencia con procedencia de aprobación. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
