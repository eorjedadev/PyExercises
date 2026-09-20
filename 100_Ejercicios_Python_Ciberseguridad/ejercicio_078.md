# Ejercicio 078 — Cadena de eventos con huellas enlazadas

[Índice](README.md#indice) · [Anterior](ejercicio_077.md) · [Siguiente](ejercicio_079.md)

### Escenario de seguridad

Un formato de laboratorio encadena hashes para detectar cambios de bytes respecto de un ancla recibida.

### Contexto profesional

Ámbito: **Integridad**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Registro de auditoría exportado. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **cadena de eventos con huellas enlazadas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Primera inconsistencia y comparación con ancla, sin atribuir autor**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 078](ejercicio_078/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/cadena.json](ejercicio_078/datos/cadena.json) — Cadena sintética; payload_b64 describe bytes, no JSON que deba reserializarse.
- [config/ancla.json](ejercicio_078/config/ancla.json) — Ancla final separada por contrato de laboratorio. Esta separación de archivos no crea confianza real por sí sola.
- [datos/cadena_alterada.json](ejercicio_078/datos/cadena_alterada.json) — Variante independiente con un payload modificado y etiquetas originales.
- [datos/cadena_truncada.json](ejercicio_078/datos/cadena_truncada.json) — Variante independiente con último registro omitido; comparar con la misma ancla.

### Requisitos

- Cada registro contiene payload_b64, prev_hash, hash.
- SHA-256 sobre bytes de prev_hash ASCII concatenados con payload decodificado.
- primer prev_hash es64 ceros.
- verificar orden y ancla final externa.
- no llamar firma al hash ni resistencia a reescritura sin ancla confiada.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Primera inconsistencia y comparación con ancla, sin atribuir autor. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Bytes, comparación de huellas y validación de formatos.
- Representación binaria, codificación y límites de tamaño.

### Conceptos de ciberseguridad relacionados

Una huella comprueba una relación entre bytes y referencia. Autenticidad, custodia de la referencia y origen son preguntas adicionales.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **payload exacto, huella previa, huella declarada, ancla externa**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué protección aporta el ancla independiente que no aporta el encadenamiento solo?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 006](ejercicio_006.md), [ejercicio 026](ejercicio_026.md), [ejercicio 049](ejercicio_049.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Cadena original → coherente con ancla.
2. Payload alterado sin actualizar hash → inconsistente.
3. Cadena truncada → ancla final no coincide.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Quien reescribe cadena y ancla puede ocultar cambios; ancla debe tener otra custodia. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Exportación incompleta puede parecer truncamiento malicioso. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Quien reescribe cadena y ancla puede ocultar cambios; ancla debe tener otra custodia. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Bytes, Unicode y Codificación**; busca ese título en el índice.
- [Python: alcance de funciones hash](https://docs.python.org/3/library/hashlib.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Quien reescribe cadena y ancla puede ocultar cambios; ancla debe tener otra custodia.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En integridad, este razonamiento ayuda a proteger **registro de auditoría exportado** mediante cadena de eventos con huellas enlazadas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir firma del ancla sin inventar esquema criptográfico. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
