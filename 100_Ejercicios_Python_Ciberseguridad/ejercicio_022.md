# Ejercicio 022 — Intentos distribuidos sobre varias cuentas

[Índice](README.md#indice) · [Anterior](ejercicio_021.md) · [Siguiente](ejercicio_023.md)

### Escenario de seguridad

El equipo quiere detectar un patrón de errores dispersos sin mirar contraseñas.

### Contexto profesional

Ámbito: **Detección**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Directorio de usuarios. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **intentos distribuidos sobre varias cuentas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Orígenes candidatos, cuentas distintas y observaciones compatibles con spraying, no prueba definitiva**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 022](ejercicio_022/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/auth.json](ejercicio_022/logs/auth.json) — Lote con patrón distribuido,repetición concentrada y ruido legítimo.
- [config/parametros.json](ejercicio_022/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Por origen en ventana fija suministrada [inicio, fin), candidato si falla contra al menos 4 cuentas distintas y ninguna recibe más de 2 fallos.
- no incluir contraseñas.
- éxitos se muestran aparte.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Orígenes candidatos, cuentas distintas y observaciones compatibles con spraying, no prueba definitiva. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.
- **Lectura de eventos, validación y procedencia**: Conservar posición, fuente e identificador aunque un registro se descarte.

### Conceptos de ciberseguridad relacionados

Separa indicador, hipótesis y conclusión. Mide cobertura y considera causas legítimas antes de asignar intención a un patrón.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **dict, list, collections**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **csv, json y funciones de validación**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **origen agregado, cuentas distintas, frecuencia por cuenta, ventana fija**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Por qué la IP no identifica necesariamente a una persona?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?
- Recupera razonamiento de [ejercicio 002](ejercicio_002.md), [ejercicio 014](ejercicio_014.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Origen A falla una vez en 4 cuentas → candidato.
2. Origen B falla4 veces en una → no cumple.
3. Evento en fin → fuera.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

NAT puede reunir a muchas personas legítimas. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un agente de sincronización puede probar varias cuentas por error. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- NAT puede reunir a muchas personas legítimas. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Logging**; busca ese título en el índice.
- [CIS Controls: contexto de monitoreo defensivo](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/collections.html) — consulta el contrato y las excepciones, no copies una solución.
- [MITRE ATT&CK T1110: comportamientos de intentos de autenticación; no atribución automática](https://attack.mitre.org/techniques/T1110/).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **NAT puede reunir a muchas personas legítimas.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En detección, este razonamiento ayuda a proteger **directorio de usuarios** mediante intentos distribuidos sobre varias cuentas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Comparar ventanas sucesivas sin duplicar el mismo hallazgo. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
