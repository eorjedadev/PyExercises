# Ejercicio 100 — Investigación defensiva de un caso acotado

[Índice](README.md#indice) · [Anterior](ejercicio_099.md)

### Escenario de seguridad

Se entrega un expediente con autenticación, red, cambios, aprobaciones y cobertura parcial para decidir qué investigar.

### Contexto profesional

Ámbito: **Respuesta a incidentes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Cuenta y servicio de un laboratorio. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **investigación defensiva de un caso acotado**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Dossier con observaciones, hipótesis rivales, correlaciones respaldadas, incertidumbre y siguiente acción defensiva justificable**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 100](ejercicio_100/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/auth.json](ejercicio_100/logs/auth.json) — Copia independiente para recuperar el contrato anterior. Caso de ana con errores y éxito, más actividad de otras cuentas.
- [logs/roles.json](ejercicio_100/logs/roles.json) — Copia independiente para recuperar el contrato anterior. Cambio P1 de ana y P2 de beto; no indican si hubo sesión interactiva real.
- [datos/tickets.json](ejercicio_100/datos/tickets.json) — Copia independiente para recuperar el contrato anterior. Solo existe autorización aportada para beto; no inventar otra para ana.
- [datos/cobertura.json](ejercicio_100/datos/cobertura.json) — Copia independiente para recuperar el contrato anterior. Ausencia explícita de fuente endpoint en el expediente recibido.
- [logs/firewall.json](ejercicio_100/logs/firewall.json) — Conexión N1 corrobora tiempo y par de A4; no identifica persona ni contenido.
- [datos/inventario.json](ejercicio_100/datos/inventario.json) — Propietarios para dirigir preguntas; no autorizan automáticamente actividad.
- [datos/encargo.json](ejercicio_100/datos/encargo.json) — Encargo acotado y carencias conocidas; otras hipótesis pueden necesitar fuentes adicionales.

### Requisitos

- Elegir y justificar evidencias.
- mínimo evaluar éxito tras fallos, cambio de rol y contexto de red usando contratos21,62 y 68.
- no requerir certeza de compromiso.
- conservar trazabilidad y versiones.
- crear herramienta reproducible, reporte técnico y plan de validación.
- contención solo propuesta.
- adaptar nombres de campo entre fuentes sin alterar significado y documentar esas equivalencias.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Dossier con observaciones, hipótesis rivales, correlaciones respaldadas, incertidumbre y siguiente acción defensiva justificable. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Selección, correlación y comunicación de resultados.
- Responsabilidades, interfaces y compatibilidad.

### Conceptos de ciberseguridad relacionados

Relaciona afirmaciones con evidencia, documenta incertidumbre y distingue propuesta de acción de autorización para ejecutarla.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **evidencia seleccionada, observación, hipótesis rival, acción propuesta**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué conclusión máxima puedes defender y qué evidencia cambiaría tu decisión?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 021](ejercicio_021.md), [ejercicio 062](ejercicio_062.md), [ejercicio 068](ejercicio_068.md), [ejercicio 081](ejercicio_081.md), [ejercicio 090](ejercicio_090.md), [ejercicio 099](ejercicio_099.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Cuenta ana:éxito tras 3 fallos → señal de 21.
2. Ticket ajeno no respalda cambio de ana → no cubierto.
3. Red mismo par a10s → corrobora conexión, no identidad humana.
4. Ausencia de endpoint → no afirmar ejecución de malware.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Puede no existir una conclusión binaria respaldada por todas las fuentes. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Soporte remoto, errores de credenciales y documentación tardía siguen siendo explicaciones a contrastar. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Puede no existir una conclusión binaria respaldada por todas las fuentes. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Módulos y Paquetes**; busca ese título en el índice.
- [NIST SP 800-61r3: respuesta a incidentes](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Puede no existir una conclusión binaria respaldada por todas las fuentes.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En respuesta a incidentes, este razonamiento ayuda a proteger **cuenta y servicio de un laboratorio** mediante investigación defensiva de un caso acotado. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Recibir una nueva fuente parcial y actualizar el reporte preservando el anterior. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
