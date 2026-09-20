# Ejercicio 052 — Excepciones auditables de detección

[Índice](README.md#indice) · [Anterior](ejercicio_051.md) · [Siguiente](ejercicio_053.md)

### Escenario de seguridad

Un conjunto de alertas incluye tareas programadas autorizadas y excepciones demasiado amplias.

### Contexto profesional

Ámbito: **SOC**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Cobertura de reglas. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **excepciones auditables de detección**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Alertas activas, exceptuadas y excepciones rechazadas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 052](ejercicio_052/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/alertas.json](ejercicio_052/logs/alertas.json) — Alertas no deben desaparecer de los resultados por estar exceptuadas.
- [config/excepciones.json](ejercicio_052/config/excepciones.json) — EX2 utiliza wildcard que el lenguaje del ejercicio no permite.

### Requisitos

- Excepción aplica a regla, activo y [inicio, fin).
- requiere ticket y aprobador.
- no eliminar alerta: clasificar exceptuada y conservar razón.
- wildcard en activo no admitido.
- excepción inválida se informa.
- rechazar cada excepción inválida y continuar evaluando alertas con las demás excepciones válidas.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Alertas activas, exceptuadas y excepciones rechazadas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Zonas, intervalos, orden e incertidumbre**: Comparar instantes y fronteras temporales con una referencia explícita.
- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.

### Conceptos de ciberseguridad relacionados

Una alerta es una solicitud de revisión basada en una regla. La cobertura, los datos descartados y las excepciones condicionan su interpretación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- datetime y timedelta; justifica su necesidad y el límite de su garantía.
- dict, list, collections; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **regla, alcance de excepción, aprobador, alerta retenida**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cómo medirías qué cobertura se pierde al exceptuar?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 013](ejercicio_013.md), [ejercicio 051](ejercicio_051.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Alerta R1 hostA dentro de ventana → exceptuada.
2. Misma regla hostB → activa.
3. Fin exacto de excepción → activa.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Una excepción temporal puede ocultar un ataque dentro de la ventana. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un escáner autorizado produce alertas reales de comportamiento previsto. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Una excepción temporal puede ocultar un ataque dentro de la ventana. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [OWASP: registro de eventos](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/datetime.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Una excepción temporal puede ocultar un ataque dentro de la ventana.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En soc, este razonamiento ayuda a proteger **cobertura de reglas** mediante excepciones auditables de detección. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir límite de cantidad de alertas cubiertas por excepción. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
