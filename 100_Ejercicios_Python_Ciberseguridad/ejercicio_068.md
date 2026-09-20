# Ejercicio 068 — Autenticación remota y conexión de red

[Índice](README.md#indice) · [Anterior](ejercicio_067.md) · [Siguiente](ejercicio_069.md)

### Escenario de seguridad

Dos fuentes pueden respaldar una misma actividad remota.

### Contexto profesional

Ámbito: **Detección**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Acceso administrativo entre hosts. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **autenticación remota y conexión de red**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Relaciones con distancia temporal y casos no corroborados**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 068](ejercicio_068/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/auth.json](ejercicio_068/logs/auth.json) — Éxitos y fallos de autenticación: usar solo éxitos para la correlación solicitada.
- [logs/firewall.json](ejercicio_068/logs/firewall.json) — Origen coincide con IP textual de auth; destino con id de host de la misma fuente. N3 queda a31s.

### Requisitos

- Relacionar éxito de auth por origen/destino con conexión allow tcp3389 del mismo par en intervalo [auth-30s, auth+30s].
- conservar todos los candidatos.
- varios eventos no equivalen a varias intrusiones.
- ausencia de pareja → no corroborado.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Relaciones con distancia temporal y casos no corroborados. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Representación y comparación de direcciones y redes.
- Zonas, intervalos, orden e incertidumbre.

### Conceptos de ciberseguridad relacionados

Separa indicador, hipótesis y conclusión. Mide cobertura y considera causas legítimas antes de asignar intención a un patrón.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **evento de autenticación, flujo candidato, par de hosts, diferencia temporal**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué demuestra la correlación que no demuestra cada fuente por separado?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 021](ejercicio_021.md), [ejercicio 048](ejercicio_048.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. N1 y A1 mismo par a10s → correlacionados.
2. Otro origen mismo tiempo → no.
3. Distancia31s → fuera.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

La coincidencia no acredita usuario detrás de NAT. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Soporte remoto autorizado cumple el mismo patrón. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- La coincidencia no acredita usuario detrás de NAT. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [CIS Controls: contexto de monitoreo defensivo](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **La coincidencia no acredita usuario detrás de NAT.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En detección, este razonamiento ayuda a proteger **acceso administrativo entre hosts** mediante autenticación remota y conexión de red. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Cruzar solicitud de asistencia autorizada. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
