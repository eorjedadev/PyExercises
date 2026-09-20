# Ejercicio 079 — Verificación de un paquete recibido

[Índice](README.md#indice) · [Anterior](ejercicio_078.md) · [Siguiente](ejercicio_080.md)

### Escenario de seguridad

Se entrega un paquete con archivos, manifiesto y acta de adquisición incompleta.

### Contexto profesional

Ámbito: **Forense**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Integridad y procedencia de evidencia. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **verificación de un paquete recibido**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Dos conclusiones separadas: integridad contra referencia y suficiencia documental**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 079](ejercicio_079/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/paquete/documento.txt](ejercicio_079/datos/paquete/documento.txt) — Archivo recibido inerte.
- [datos/paquete/extra.txt](ejercicio_079/datos/paquete/extra.txt) — Archivo recibido que no figura en el manifiesto.
- [datos/manifiesto.json](ejercicio_079/datos/manifiesto.json) — Paths relativos a datos/paquete; solo archivos de esa carpeta son objetos del manifiesto.
- [datos/acta.json](ejercicio_079/datos/acta.json) — Método de adquisición ausente intencionalmente; no completarlo por deducción.

### Requisitos

- Verificar huellas y tamaños, detectar rutas extra y ausentes.
- no seguir enlaces.
- procedencia se evalúa por campos recolector, instante, método, alcance.
- faltantes → procedencia incompleta aunque hashes coincidan.
- no modificar paquete.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Dos conclusiones separadas: integridad contra referencia y suficiencia documental. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Bytes, comparación de huellas y validación de formatos.
- Identidad de rutas y semántica por plataforma.

### Conceptos de ciberseguridad relacionados

Conserva origen, integridad y trazabilidad. Un cambio observado no identifica su causa ni autor; una copia transformada no debe presentarse como el original.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **archivo recibido, declaración del manifiesto, dato de procedencia, límite de confianza**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué conclusiones puedes sostener sin conocer el método de adquisición?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 006](ejercicio_006.md), [ejercicio 049](ejercicio_049.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Archivo coincidente con acta incompleta → integridad conforme, procedencia incompleta.
2. Extra no declarado → inventario divergente.
3. Ausente → no verificable.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Manifiesto recibido junto al paquete no es por sí mismo una fuente confiada. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un empaquetado manual puede olvidar una entrada. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Manifiesto recibido junto al paquete no es por sí mismo una fuente confiada. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [NIST SP 800-61r3: contexto de respuesta](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Manifiesto recibido junto al paquete no es por sí mismo una fuente confiada.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En forense, este razonamiento ayuda a proteger **integridad y procedencia de evidencia** mediante verificación de un paquete recibido. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Registrar una nueva adquisición conservando la versión recibida. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
