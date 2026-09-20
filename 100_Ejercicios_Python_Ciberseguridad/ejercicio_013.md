# Ejercicio 013 — Ventanas autorizadas de mantenimiento

[Índice](README.md#indice) · [Anterior](ejercicio_012.md) · [Siguiente](ejercicio_014.md)

### Escenario de seguridad

Se observan acciones fuera de horarios declarados por el equipo responsable.

### Contexto profesional

Ámbito: **SOC**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Actividad administrativa. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **ventanas autorizadas de mantenimiento**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Eventos dentro/fuera/sin ventana y referencias de autorización**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 013](ejercicio_013/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/actividad.json](ejercicio_013/logs/actividad.json) — Acciones declaradas, sin instrucciones ejecutables.
- [config/ventanas.json](ejercicio_013/config/ventanas.json) — Ventanas autorizadas de este laboratorio.

### Requisitos

- Intervalos autorizados incluyen inicio y excluyen fin.
- comparar por activo y UTC.
- actividad fuera se marca para revisión, nunca se descarta la evidencia dentro.
- ventanas superpuestas se permiten.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Eventos dentro/fuera/sin ventana y referencias de autorización. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Zonas, intervalos, orden e incertidumbre**: Comparar instantes y fronteras temporales con una referencia explícita.
- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.

### Conceptos de ciberseguridad relacionados

Una alerta es una solicitud de revisión basada en una regla. La cobertura, los datos descartados y las excepciones condicionan su interpretación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **datetime y timedelta**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **dict, list, collections**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **activo, instante observado, ventana aprobada, estado de cobertura**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cómo conservarías la autorización sin convertirla en prueba de inocuidad?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?
- Recupera razonamiento de [ejercicio 004](ejercicio_004.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. A1 en 09:00 para srv1 → dentro.
2. A2 en 10:00 al final → fuera.
3. A3 en srv2 sin ventana → sin ventana.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un cambio urgente puede aprobarse después; no debe ocultarse retroactivamente. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Mantenimiento legítimo fuera de una ventana mal registrada. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un cambio urgente puede aprobarse después; no debe ocultarse retroactivamente. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
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

Contrasta tu resultado con esta limitación: **Un cambio urgente puede aprobarse después; no debe ocultarse retroactivamente.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En soc, este razonamiento ayuda a proteger **actividad administrativa** mediante ventanas autorizadas de mantenimiento. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir propietario de aprobación y motivo del cambio. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
