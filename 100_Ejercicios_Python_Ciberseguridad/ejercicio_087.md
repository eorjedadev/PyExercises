# Ejercicio 087 — Evaluación de una política IAM de juguete

[Índice](README.md#indice) · [Anterior](ejercicio_086.md) · [Siguiente](ejercicio_088.md)

### Escenario de seguridad

Una política acotada permite practicar mínimos privilegios sin conectarse a ninguna nube.

### Contexto profesional

Ámbito: **Desarrollo seguro**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Recursos de un servicio simulado. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **evaluación de una política iam de juguete**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Decisiones, trazas y amplitud declarada de cada permiso**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 087](ejercicio_087/README.md). Su README describe formatos, campos y procedencia sintética.

- [config/politica.json](ejercicio_087/config/politica.json) — Solo comodín total *. Ninguna sintaxis de proveedor cloud real.
- [datos/solicitudes.json](ejercicio_087/datos/solicitudes.json) — Solicitudes de evaluación offline; no acciones contra recursos reales.

### Requisitos

- Reglas allow/deny sobre actor, acción, recurso exactos o wildcard total *.
- deny prevalece.
- sin allow denegar.
- no implementar comodines parciales.
- este lenguaje no emula proveedor real.
- informar reglas demasiado amplias.
- también se admite wildcard total en actor.
- nombres de actor, acción y recurso se comparan exactamente.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Decisiones, trazas y amplitud declarada de cada permiso. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Transiciones, invariantes y funciones con efectos delimitados.
- Pruebas de contrato, regresión y fallos simulados.

### Conceptos de ciberseguridad relacionados

Toda entrada externa requiere un contrato. Validar, codificar según contexto y minimizar datos de salida son responsabilidades diferentes.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **actor, acción, recurso, reglas coincidentes**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué pruebas demostrarían que agregar deny no concede permisos nuevos?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 031](ejercicio_031.md), [ejercicio 044](ejercicio_044.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Allow ana read doc1 → permite esa consulta.
2. Deny equivalente prevalece.
3. Acción write sin allow → deniega.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Una política sintácticamente amplia puede tener controles externos no incluidos. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Cuentas de operación de emergencia pueden requerir alcance amplio controlado. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Una política sintácticamente amplia puede tener controles externos no incluidos. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Programación Orientada a Objetos**; busca ese título en el índice.
- [INTENSIVO DE PYTHON (Eric Matthes).md](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md) — **11. Probar el código**; busca ese título en el índice.
- [OWASP: logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Una política sintácticamente amplia puede tener controles externos no incluidos.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En desarrollo seguro, este razonamiento ayuda a proteger **recursos de un servicio simulado** mediante evaluación de una política iam de juguete. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Separar alcance del recurso y condiciones temporales mediante versión de contrato. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
