# Ejercicio 056 — Expansión de conexiones entre activos

[Índice](README.md#indice) · [Anterior](ejercicio_055.md) · [Siguiente](ejercicio_057.md)

### Escenario de seguridad

Un host pasa a contactar múltiples servidores administrativos.

### Contexto profesional

Ámbito: **Detección**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Segmentación interna. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **expansión de conexiones entre activos**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Abanico de conexiones, candidatos y eventos sin activo conocido**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 056](ejercicio_056/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/inventario.json](ejercicio_056/datos/inventario.json) — El alcance interno depende de este inventario y no de is_private.
- [logs/conexiones.json](ejercicio_056/logs/conexiones.json) — Hosts como identidades de inventario; origen fuera de inventario se conserva con contexto faltante.
- [config/parametros.json](ejercicio_056/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Por origen en ventana fija contar destinos distintos por tcp445 o3389.
- candidato con 4 destinos.
- destino debe pertenecer al inventario interno, no basarse en is_private.
- falta de inventario se informa.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Abanico de conexiones, candidatos y eventos sin activo conocido. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Representación y comparación de direcciones y redes**: Distinguir validez, versión y pertenencia a una red explícita.
- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.

### Conceptos de ciberseguridad relacionados

Separa indicador, hipótesis y conclusión. Mide cobertura y considera causas legítimas antes de asignar intención a un patrón.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- ipaddress; justifica su necesidad y el límite de su garantía.
- dict, list, collections; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **activo origen, destinos internos, servicio observado, abanico**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué señal de autenticación correlacionarías antes de hablar de movimiento lateral?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 003](ejercicio_003.md), [ejercicio 055](ejercicio_055.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. hA contacta4 internos por 445 → candidato.
2. hB repite un destino → no.
3. Destino no inventariado → sin contexto.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Conexión de red no demuestra ejecución remota. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un servidor de gestión puede tener abanico legítimo. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Conexión de red no demuestra ejecución remota. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [CIS Controls: contexto de monitoreo defensivo](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/ipaddress.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Conexión de red no demuestra ejecución remota.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En detección, este razonamiento ayuda a proteger **segmentación interna** mediante expansión de conexiones entre activos. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Separar rol de administración del rol de estación de usuario. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
