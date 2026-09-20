# 100 ejercicios de Python aplicados a ciberseguridad

Esta colección contiene **100 problemas defensivos con recursos de laboratorio**, sin implementaciones ni archivos de soluciones. Python sirve para validar, transformar y relacionar evidencia; el aprendizaje se evalúa también por la calidad de las conclusiones y sus límites.

El propósito es aprender a resolver problemas reales de análisis, desarrollo seguro, administración defensiva y respuesta a incidentes. No se necesita escanear ni atacar servicios de terceros. Los datos son sintéticos, salvo vectores criptográficos públicos identificados como tales.

## Organización

Cada ejercicio tiene un enunciado en la raíz: ejercicio_001.md hasta ejercicio_100.md. Sus recursos están en una carpeta del mismo número con README.md y los subdirectorios datos, logs o config que necesite. El README del paquete indica formato, campos observados, unidades y defectos deliberados. No todos los paquetes necesitan los tres subdirectorios.

Guarda tu trabajo en una carpeta distinta, por ejemplo mis_practicas_seguridad/ejercicio_001, y conserva intactos los recursos recibidos. Las rutas en los logs son texto para analizar, no destinos que debas abrir. Los enlaces de referencia locales apuntan a los cinco documentos de la carpeta superior; mueve la biblioteca junto con la colección si quieres conservarlos.

## Metodología

Sigue **Observar → comprender → formular hipótesis → diseñar → implementar → validar → explicar → mejorar**:

1. **Observar:** lee primero el encargo y una muestra de cada fuente. Identifica activo, procedencia, formato y cobertura.
2. **Comprender:** separa comportamiento observado, comportamiento esperado por política y lo que todavía no conoces.
3. **Formular hipótesis:** escribe una explicación que investigarás y otra explicación legítima o alternativa. Anota qué dato podría refutarlas.
4. **Diseñar:** decide identidades, unidades, representaciones, relaciones temporales, contratos y responsabilidades. Calcula algunos ejemplos manualmente.
5. **Implementar:** construye tu herramienta con parámetros explícitos y efectos delimitados. Elige nombres que comuniquen intención y procedencia.
6. **Validar:** escribe expectativas antes de ejecutar; prueba casos normales, fronteras, registros inválidos, fuentes ausentes y condiciones que contradigan tu hipótesis.
7. **Explicar:** lee tu código sin ejecutarlo y predice un resultado. Explica después las decisiones, las limitaciones y la evidencia que respalda la conclusión.
8. **Mejorar:** cambia una regla pequeña o aplica el reto opcional, identificando pruebas que deben conservar su resultado y pruebas cuyo contrato cambió.

Antes de programar responde: ¿qué ocurre?, ¿qué activo protejo?, ¿qué datos tengo?, ¿qué sería normal?, ¿qué podría ser sospechoso?, ¿qué evidencia lo comprobaría?, ¿qué automatizará Python?, ¿qué errores de análisis puedo cometer?, ¿qué explicación legítima existe? y ¿cómo comunicaré el hallazgo?

## Reglas del laboratorio

Trabaja únicamente con los recursos entregados y copias que prepares en un entorno propio. Los nombres personales, cuentas, tickets, claves y tokens son ficticios. Las direcciones 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 y 2001:db8::/32 sirven como datos de documentación; los dominios example.test no deben resolverse para completar los ejercicios.

Ningún ejercicio requiere enviar tráfico, realizar DNS, bloquear cuentas reales, cambiar permisos, ejecutar comandos tomados de registros, extraer archivos peligrosos o borrar evidencia. Las propuestas de contención y retención son planes revisables, no autorización de ejecución. No se entrega malware, un exploit ni un servicio vulnerable que debas publicar.

Windows, Linux, Ubuntu, Kali Linux y CachyOS pueden usarse como entornos de trabajo. Los ejercicios de plataformas específicas usan exportaciones sintéticas para que puedas resolverlos desde otra plataforma. Kali se trata como entorno de laboratorio, no como señal de intención ofensiva. No hace falta una máquina virtual para resolver la colección.

Si decides explorar una variante con una VM o contenedor propio, define el alcance, crea una instantánea, utiliza una red aislada o solo anfitrión y evita publicar servicios. Lleva únicamente datos ficticios. La variante no cambia el contrato del ejercicio original ni autoriza interacción con terceros.

## Preparación técnica

Usa Python 3 en un entorno propio y registra la versión. La biblioteca estándar basta para todos los ejercicios salvo **028 y 029**, donde debes investigar e instalar la biblioteca mantenida cryptography en un entorno virtual para verificar firmas y cifrado autenticado. Consulta su [documentación estable](https://cryptography.io/en/stable/hazmat/primitives/aead/) y registra la versión y el origen del paquete. No escribas una implementación casera de la primitiva.

Las claves y nonces públicos de los vectores son solo material de prueba. El ejercicio 027 sí exige generar valores nuevos con una fuente apropiada durante tu implementación; no utiliza los tokens de otras muestras como aleatoriedad.

No se exige un framework web, una plataforma SIEM, una cuenta cloud ni una herramienta de Kali. Las interfaces pueden ser funciones, una CLI propia o una salida estructurada. La libertad de interfaz no permite alterar las reglas de seguridad del escenario.

<a id="contratos-comunes"></a>
## Contratos comunes de datos y resultados

Las reglas específicas de cada ejercicio prevalecen sobre estas convenciones:

- **Origen:** archivos de entrada de solo lectura. Una copia redactada, normalizada o filtrada se identifica como derivada; no se presenta como original.
- **Texto:** UTF-8. La igualdad es exacta y sensible a mayúsculas salvo normalización expresa. Conserva la forma original cuando la uses como evidencia.
- **Tipos:** identificadores textuales salvo excepciones documentadas; cantidades enteras excluyen booleanos; números excluyen NaN e infinito. CSV requiere conversión desde texto. No conviertas silenciosamente un texto false en booleano falso.
- **Ausencia:** null, campo faltante, cero, falso y vacío no son equivalentes. Si una conclusión necesita contexto que falta, devuelve no evaluable o información insuficiente según el contrato.
- **Esquema:** exige los campos usados por las reglas; los campos adicionales se conservan como evidencia y no se interpretan por intuición. Un JSON válido puede contener un registro inválido. Los campos observados del README de recursos describen la muestra, no eliminan las exigencias del enunciado.
- **Errores por registro:** si no hay una política distinta, rechaza el registro mal formado, informa archivo e id o posición y continúa con los demás. No incluyas su contenido sensible completo en el error. En consultas o transiciones individuales, rechazar no produce efectos.
- **Errores globales:** configuración inválida o documento que no puede interpretarse impide analizar esa unidad. No declares análisis completo. En JSON Lines puedes rechazar líneas independientes; el ejercicio 047 establece una política de parada para proteger el punto de control.
- **Identidad:** usa ids únicos dentro de una fuente salvo ejercicios sobre reenvíos, colisiones o identidad compuesta. Ante una colisión no prevista, informa ambigüedad y excluye sus registros de conclusiones que dependan de identidad inequívoca; no sobrescribas silenciosamente.
- **Tiempo:** usa el corte del paquete, nunca la hora real del equipo. ISO8601 requiere zona explícita salvo ejercicio que evalúe su ausencia. Los relojes relativos son segundos. Para empates usa id ascendente como orden reproducible, pero no lo presentes como orden causal.
- **Intervalos:** respeta los extremos publicados. No inventes una ventana temporal cuando la regla habla del lote completo. Una fecha normalizada no corrige por sí sola un reloj desajustado.
- **Unidades:** bytes, segundos y km cuando se indiquen; MiB significa 1048576 bytes. Distingue tamaño de texto codificado y número de caracteres.
- **Cobertura:** no encontrar coincidencias solo describe las fuentes procesadas y las reglas aplicadas. Si hubo rechazos, fuentes ausentes o límites alcanzados, indica estado parcial.
- **Resultados:** conserva referencia a archivo y registro, reglas o perfil utilizado y condiciones del análisis. Si no se exige otro orden, ordena hallazgos por id y agrupaciones por su clave textual; conserva orden cuando sea parte del contrato.
- **Pruebas:** son independientes. Un caso puede usar un subconjunto de la muestra o cambiar un valor en una copia. Si destaca un solo campo, elige valores válidos para los demás. La flecha del enunciado expresa comportamiento esperado, no pasos de implementación.
- **Secretos:** no vuelques configuraciones completas, valores de tokens ni contraseñas en reportes. Una huella tampoco demuestra que un dato de baja entropía sea anónimo.
- **Recursos:** los fallos de escritura o lectura se simulan sustituyendo una dependencia durante pruebas. No necesitas alterar permisos del sistema ni desconectar discos. No abras URLs ni rutas que aparecen solo como evidencia.

Los ejercicios 047 y 094 contienen logs deliberadamente incompletos o inválidos. El ejercicio 097 contiene 20000 líneas, incluidas tres defectuosas, para comprobar procesamiento incremental. No los repares antes de analizarlos.

## Aprender a interpretar evidencia

No confundas **dato, evento, observación, indicador, hipótesis, evidencia y conclusión**. Un dato puede apoyar una observación; al evaluar su procedencia, integridad, cobertura y significado decides qué afirmación respalda. Un indicador orienta una investigación, pero no reemplaza la comprobación. La evidencia también puede refutar una hipótesis.

Ejemplo conceptual: varios fallos de autenticación respaldan que la fuente registró errores. No demuestran por sí solos acceso exitoso, identidad humana, intención ni compromiso. Un acceso posterior y una segunda fuente pueden aportar contexto, pero sus relojes, identidades y cobertura también deben evaluarse.

Usa expresiones acotadas: «coincide con la regla», «no cubierto por la aprobación recibida», «compatible con», «no determinado con estas fuentes». No llames atacante a una IP ni malicioso a un archivo solo por su extensión. Una excepción aprobada no vuelve invisible el evento ni demuestra inocuidad.

La confianza alta, media o baja se aplica a una afirmación concreta y se justifica con evidencia; no son etiquetas de dificultad ni equivalen a probabilidad numérica. Distingue confianza, impacto potencial y prioridad operativa.

## Progresión y distribución de dominios

El plan completo se elaboró antes de crear los enunciados. Los tramos mezclan fundamentos y áreas; no son bloques de sintaxis ni categorías de dificultad.

| Recorrido | Responsabilidades que se incorporan | Autonomía esperada |
| --- | --- | --- |
| 001–020 | Contratos de datos, observaciones de archivos, logs, red, integridad y controles declarados | Reconocer entidades y unidades, comprobar fronteras y evitar inferencias injustificadas |
| 021–040 | Secuencias, estado, autenticación, primitivas criptográficas y desarrollo web seguro | Elegir representaciones, separar funciones y justificar garantías de cada control |
| 041–060 | Dependencias, configuración, custodia, calidad de datos y patrones de detección | Distinguir variación normal, información faltante y resultado parcial |
| 061–080 | Correlación entre fuentes, plataformas, versiones, cobertura e incertidumbre temporal | Seleccionar estructuras y módulos por cuenta propia; justificar uniones y límites |
| 081–100 | Expedientes mixtos, priorización, contención conceptual, recuperación y mantenimiento de herramientas | Formular hipótesis rivales, seleccionar evidencia, probar cambios y entregar un reporte defendible |

| Área | Ejercicios representativos |
| --- | --- |
| Seguridad de archivos e integridad | 001, 005, 006, 017–019, 037–038, 078–079 |
| Logs y eventos | 002, 010, 020–022, 043, 047–048, 063–065, 094, 097 |
| Redes | 003–004, 014, 030, 055–060, 068, 071–072, 088 |
| Autenticación y sesiones | 011–012, 021–025, 027, 034–035, 061 |
| Criptografía aplicada | 006, 009, 025–029, 060, 078 |
| Desarrollo seguro y seguridad web | 007–008, 015–017, 031–040, 042–046, 069 |
| Análisis defensivo y falsos positivos | 051–060, 068–076, 083, 089, 093, 098 |
| Respuesta a incidentes | 049–050, 062, 081–085, 090–092, 099–100 |
| Forense y procedencia | 018–019, 048–050, 065, 073–074, 078–080, 092 |
| DevSecOps y configuración | 015, 041–046, 066–067, 085–088 |
| Automatización y mantenibilidad | 047, 074–077, 093–098, 100 |

Las referencias cruzadas recuperan patrones, no soluciones intercambiables. El 096 requiere tu implementación del 021. El resto proporciona sus propias copias de datos cuando reutiliza un escenario; no depende de que un archivo anterior haya sido modificado.

## Biblioteca local y documentación profesional

Se revisaron los índices y secciones pertinentes de los cinco documentos disponibles en la carpeta superior:

| Documento | Utilidad y límite |
| --- | --- |
| [Diccionario Python](../Diccionario_Python.md) | Métodos, funciones e imports de ciberseguridad; es una referencia breve, no un manual completo de seguridad |
| [Universidad Python](../Universidad_Python.md) | Colecciones, funciones, errores, archivos, logging, objetos y organización |
| [Guía de Matthes](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md) | Funciones, archivos y pruebas; es una guía local de repaso |
| [Notas para profesionales](../NotasdePythonparaprofesionales.md) | Fechas, JSON y pruebas; incluye material histórico y sintaxis de Python 2 que debes contrastar |
| [Guía de Ramalho](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md) | Mutabilidad, Unicode e iteración; es una guía de estudio, no el libro íntegro |

Las referencias de cada ejercicio indican títulos reales que puedes buscar. No copies soluciones de ejemplos. En el diccionario, términos breves como «firmas HMAC» necesitan precisión: HMAC autentica con una clave compartida y no es una firma digital verificable mediante una clave pública.

Para seguridad se consultaron fuentes primarias: [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html), [MITRE ATT&CK T1110](https://attack.mitre.org/techniques/T1110/), [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [CIS Controls](https://www.cisecurity.org/controls/v8), [documentación oficial de Python](https://docs.python.org/3/library/ipaddress.html), [Microsoft para eventos Windows](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624) y documentación de cryptography. Consulta realizada para esta edición: 19 de septiembre de 2026.

Los marcos contextualizan: no hay una equivalencia automática entre cada ejercicio y una técnica ATT&CK, ni una afirmación de cumplimiento NIST o CIS. Los umbrales, políticas de bloqueo, retención y prioridades son reglas locales del laboratorio, no recomendaciones universales. Para APIs cambiantes consulta la documentación de la versión instalada.

## Evitar soluciones prematuras y pedir ayuda

Antes de consultar ayuda, escribe interpretación, hipótesis, un ejemplo manual y una decisión tentativa de diseño. Identifica si el bloqueo está en el problema, el concepto de seguridad, la representación de datos o una herramienta de Python.

Al pedir ayuda sigue esta secuencia: **preguntas orientadoras → explicación conceptual → pistas → documentación → revisión del razonamiento**. Pide revisión de una hipótesis o de un error específico, no el programa completo ni pseudocódigo que solo debas traducir. Registra qué ayuda recibiste y vuelve a resolver una variación sin consultarla.

La colección no contiene soluciones, respuestas completas a los expedientes ni programas de referencia. Los casos mínimos permiten comprobar contratos sin quitarte la responsabilidad de diseñar el análisis.

## Registro de hipótesis y hallazgos

Mantén un cuaderno por ejercicio con estas entradas:

| Entrada | Qué registrar |
| --- | --- |
| Activo y pregunta | Qué proteges y qué decisión deseas respaldar |
| Fuentes | Archivo, procedencia, cobertura, formato y límites |
| Hipótesis | Explicación a investigar y alternativa legítima o contradictoria |
| Predicción | Qué observación esperarías si cada hipótesis fuese cierta |
| Diseño | Identidades, unidades, responsabilidades y nombres |
| Prueba | Entrada, expectativa previa, resultado y explicación de diferencias |
| Hallazgo | Observación acotada, sin intención atribuida gratuitamente |
| Evidencia | Archivo e id o línea que respalda cada hecho |
| Interpretación | Qué podría significar y qué no demuestra |
| Confianza | Justificación por afirmación, considerando independencia y cobertura |
| Información faltante | Fuente o comprobación que discriminaría entre hipótesis |
| Recomendación | Próxima acción defensiva proporcional; aprobación necesaria si tendría efectos |
| Revisión | Ayuda recibida, limitación pendiente y modificación comprobada |

No trates varias copias del mismo evento como corroboración independiente. Una evidencia contradictoria obliga a revisar la conclusión, no a retirarla del dataset para proteger la hipótesis preferida.

## Revisión de código

Comprueba que los nombres comuniquen entidad, unidad y estado. Lee una función sin ejecutar, predice un resultado y señala dónde se validan los datos. Revisa que la presentación no repita secretos, que los errores no desaparezcan, que los originales no se modifiquen y que los efectos estén separados de las decisiones.

Las pruebas deben cubrir comportamiento y garantías, no reproducir el algoritmo. En cambios de código conserva casos de regresión y anota qué contrato cambió. Usa una dependencia simulada para reloj o escritura cuando corresponda; no duermas realmente ni dañes un recurso para probar un fallo.

## Medición del progreso en dos dimensiones

Evalúa cada criterio como pendiente, con apoyo o autónomo y conserva una evidencia observable. No promedies ambas dimensiones para ocultar una carencia.

| Dimensión Python | Evidencia de aprendizaje |
| --- | --- |
| Diseño | Justificas estructuras, contratos, funciones y efectos |
| Implementación | Validaciones y errores respetan el contrato |
| Lectura | Predices el recorrido de los datos sin ejecutar |
| Pruebas | Incluyes fronteras, fallos y datos que refutan una suposición |
| Mantenimiento | Modificas una regla y conservas las garantías anteriores |

| Dimensión ciberseguridad | Evidencia de aprendizaje |
| --- | --- |
| Activo y alcance | Sabes qué proteges y qué observas realmente |
| Evidencia | Conservas procedencia y citas datos concretos |
| Interpretación | Distingues observación, indicador, hipótesis y conclusión |
| Falsos positivos | Ofreces una explicación legítima y una comprobación discriminante |
| Comunicación | Explicas confianza, información faltante y siguiente acción proporcional |

Un ejercicio no está terminado solo porque el programa corre. Debes explicar ambas dimensiones, reconocer al menos una limitación y adaptar una condición sin perder el control del resultado.

## Volver a ejercicios anteriores

Cada diez ejercicios vuelve a dos que resolviste antes: interpreta de nuevo el contrato, predice un caso límite leyendo el código y mejora un nombre o una responsabilidad. Después de 050, 075 y 100 revisa tu cuaderno buscando fallos repetidos: identidad, zonas horarias, ausencia confundida con cero, mutación de fuentes, datos filtrados sin registro o conclusiones de ataque sin respaldo.

Repite unos días después un ejercicio que necesitó mucha ayuda, con una variante nueva. La señal de progreso es reconocer un patrón y también sus límites, no recordar la implementación.

<a id="indice"></a>
## Índice de los 100 ejercicios

| Número | Encargo | Área principal |
| --- | --- | --- |
| 001 | [Inventario de extensiones de riesgo](ejercicio_001.md) | Archivos |
| 002 | [Resumen de fallos de autenticación](ejercicio_002.md) | Autenticación |
| 003 | [Validación de direcciones de origen](ejercicio_003.md) | Redes |
| 004 | [Exposición declarada de servicios](ejercicio_004.md) | Redes |
| 005 | [Higiene de permisos declarados](ejercicio_005.md) | Sistemas |
| 006 | [Comprobación de huellas de archivos](ejercicio_006.md) | Integridad |
| 007 | [Redacción de secretos en eventos](ejercicio_007.md) | Desarrollo seguro |
| 008 | [Inspección de controles HTTP declarados](ejercicio_008.md) | Web |
| 009 | [Diferencia entre codificar y proteger](ejercicio_009.md) | Criptografía aplicada |
| 010 | [Conteo de decisiones de firewall](ejercicio_010.md) | Redes |
| 011 | [Identidades duplicadas y cuentas compartidas](ejercicio_011.md) | Autenticación |
| 012 | [Sesiones pendientes de expiración](ejercicio_012.md) | Autenticación |
| 013 | [Ventanas autorizadas de mantenimiento](ejercicio_013.md) | SOC |
| 014 | [DNS con alta tasa de respuestas negativas](ejercicio_014.md) | Redes |
| 015 | [Revisión de ajustes inseguros](ejercicio_015.md) | DevSecOps |
| 016 | [Búsqueda acotada de marcas de secreto](ejercicio_016.md) | Desarrollo seguro |
| 017 | [Clasificación de rutas de una carga](ejercicio_017.md) | Archivos |
| 018 | [Copias con contenido idéntico](ejercicio_018.md) | Forense |
| 019 | [Comparación de inventarios de integridad](ejercicio_019.md) | Integridad |
| 020 | [Picos de errores HTTP con denominador](ejercicio_020.md) | Web |
| 021 | [Fallos consecutivos antes de un acceso](ejercicio_021.md) | Autenticación |
| 022 | [Intentos distribuidos sobre varias cuentas](ejercicio_022.md) | Detección |
| 023 | [Modelo de bloqueo y recuperación](ejercicio_023.md) | Autenticación |
| 024 | [Cobertura de MFA y excepciones](ejercicio_024.md) | Autenticación |
| 025 | [Auditoría conceptual de verificadores de contraseña](ejercicio_025.md) | Criptografía aplicada |
| 026 | [Autenticidad de mensajes con HMAC](ejercicio_026.md) | Criptografía aplicada |
| 027 | [Emisión y consumo de tokens de laboratorio](ejercicio_027.md) | Autenticación |
| 028 | [Firma de un artefacto inerte](ejercicio_028.md) | Criptografía aplicada |
| 029 | [Cifrado autenticado y datos asociados](ejercicio_029.md) | Criptografía aplicada |
| 030 | [Vigencia declarada de certificados](ejercicio_030.md) | Redes |
| 031 | [Autorización por propietario de objeto](ejercicio_031.md) | Web |
| 032 | [Pruebas de consultas parametrizadas](ejercicio_032.md) | Desarrollo seguro |
| 033 | [Salida HTML en contexto de texto](ejercicio_033.md) | Web |
| 034 | [Atributos de cookies de sesión](ejercicio_034.md) | Web |
| 035 | [Validación de origen para acciones con sesión](ejercicio_035.md) | Web |
| 036 | [Decisión de destino de un conector](ejercicio_036.md) | Web |
| 037 | [Preinspección de un archivo comprimido](ejercicio_037.md) | Archivos |
| 038 | [Auditoría de metadatos de carga](ejercicio_038.md) | Web |
| 039 | [Exposición en mensajes de error](ejercicio_039.md) | Desarrollo seguro |
| 040 | [Exportación de reportes sin fórmulas activas](ejercicio_040.md) | Desarrollo seguro |
| 041 | [Cruce de dependencias con avisos ficticios](ejercicio_041.md) | DevSecOps |
| 042 | [Secretos recibidos por configuración externa](ejercicio_042.md) | Desarrollo seguro |
| 043 | [Eventos resistentes a saltos de línea inyectados](ejercicio_043.md) | Desarrollo seguro |
| 044 | [Permisos efectivos en una matriz acotada](ejercicio_044.md) | Sistemas |
| 045 | [Deriva de configuración entre capturas](ejercicio_045.md) | DevSecOps |
| 046 | [Auditoría portable de modos POSIX y ACL exportadas](ejercicio_046.md) | Sistemas |
| 047 | [Recolección incremental de un log](ejercicio_047.md) | Automatización |
| 048 | [Timestamps normalizados con procedencia](ejercicio_048.md) | Forense |
| 049 | [Cadena de custodia de un paquete](ejercicio_049.md) | Forense |
| 050 | [Plan de retención y preservación](ejercicio_050.md) | Respuesta a incidentes |
| 051 | [Indicadores tipados con vigencia](ejercicio_051.md) | Detección |
| 052 | [Excepciones auditables de detección](ejercicio_052.md) | SOC |
| 053 | [Evaluación de una regla con etiquetas sintéticas](ejercicio_053.md) | Detección |
| 054 | [Silencio de sensores frente a ausencia de incidentes](ejercicio_054.md) | SOC |
| 055 | [Dispersión de puertos observada](ejercicio_055.md) | Redes |
| 056 | [Expansión de conexiones entre activos](ejercicio_056.md) | Detección |
| 057 | [Consultas a dominios nuevos respecto de una base](ejercicio_057.md) | Redes |
| 058 | [Transferencias voluminosas frente a referencia](ejercicio_058.md) | Detección |
| 059 | [Periodicidad de conexiones con ruido](ejercicio_059.md) | Detección |
| 060 | [Cambios de huella TLS declarada](ejercicio_060.md) | Redes |
| 061 | [Accesos después de una baja de cuenta](ejercicio_061.md) | Autenticación |
| 062 | [Cambios de privilegios y tickets](ejercicio_062.md) | Respuesta a incidentes |
| 063 | [Normalización de eventos Windows de inicio de sesión](ejercicio_063.md) | Sistemas |
| 064 | [Contexto de elevaciones sudo](ejercicio_064.md) | Sistemas |
| 065 | [Árbol de procesos con reutilización de PID](ejercicio_065.md) | Forense |
| 066 | [Modificaciones de tareas programadas](ejercicio_066.md) | Sistemas |
| 067 | [Entradas de inicio automático declaradas](ejercicio_067.md) | Sistemas |
| 068 | [Autenticación remota y conexión de red](ejercicio_068.md) | Detección |
| 069 | [Auditoría de decisiones de autorización web](ejercicio_069.md) | Web |
| 070 | [Acceso a muchos objetos frente a trabajo previsto](ejercicio_070.md) | Detección |
| 071 | [Desplazamiento aparente entre accesos](ejercicio_071.md) | Autenticación |
| 072 | [Cabeceras de origen y proxies confiados](ejercicio_072.md) | Web |
| 073 | [Cobertura temporal antes de concluir ausencia](ejercicio_073.md) | Forense |
| 074 | [Reenvíos y contradicciones entre recolectores](ejercicio_074.md) | Automatización |
| 075 | [Adaptación de esquemas de eventos](ejercicio_075.md) | Automatización |
| 076 | [Reglas declarativas con contratos verificables](ejercicio_076.md) | Detección |
| 077 | [Presupuesto de procesamiento y decisiones incompletas](ejercicio_077.md) | Automatización |
| 078 | [Cadena de eventos con huellas enlazadas](ejercicio_078.md) | Integridad |
| 079 | [Verificación de un paquete recibido](ejercicio_079.md) | Forense |
| 080 | [Cronología con incertidumbre de reloj](ejercicio_080.md) | Forense |
| 081 | [Investigación de una cuenta con señales mixtas](ejercicio_081.md) | Respuesta a incidentes |
| 082 | [Investigación de transferencia atípica](ejercicio_082.md) | Respuesta a incidentes |
| 083 | [Cambios masivos de archivos sin atribución precipitada](ejercicio_083.md) | Detección |
| 084 | [Correlación de actividad web y procesos](ejercicio_084.md) | Respuesta a incidentes |
| 085 | [Priorización contextual de avisos de dependencias](ejercicio_085.md) | DevSecOps |
| 086 | [Revisión de manifiestos de contenedores](ejercicio_086.md) | DevSecOps |
| 087 | [Evaluación de una política IAM de juguete](ejercicio_087.md) | Desarrollo seguro |
| 088 | [Alcance de una política de segmentación](ejercicio_088.md) | Redes |
| 089 | [Agrupación explicable de alertas relacionadas](ejercicio_089.md) | SOC |
| 090 | [Simulación de contención con dependencias](ejercicio_090.md) | Respuesta a incidentes |
| 091 | [Verificación de recuperación con criterios separados](ejercicio_091.md) | Respuesta a incidentes |
| 092 | [Paquete compartible con minimización de datos](ejercicio_092.md) | Forense |
| 093 | [Resultados reproducibles al actualizar indicadores](ejercicio_093.md) | Detección |
| 094 | [Resistencia de un parser ante evidencia defectuosa](ejercicio_094.md) | Automatización |
| 095 | [Publicación de reportes sin perder la versión anterior](ejercicio_095.md) | Automatización |
| 096 | [Refactorización de una correlación existente](ejercicio_096.md) | Automatización |
| 097 | [Análisis incremental con límites de memoria](ejercicio_097.md) | Automatización |
| 098 | [Comparación de versiones de una regla](ejercicio_098.md) | Detección |
| 099 | [Informe técnico con afirmaciones graduadas](ejercicio_099.md) | Respuesta a incidentes |
| 100 | [Investigación defensiva de un caso acotado](ejercicio_100.md) | Respuesta a incidentes |
