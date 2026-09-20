# Ejercicio 090 — Simulación de contención con dependencias

[Índice](README.md#indice) · [Anterior](ejercicio_089.md) · [Siguiente](ejercicio_091.md)

### Escenario de seguridad

Se proponen aislamientos de hosts y se necesita estimar impacto antes de cualquier acción.

### Contexto profesional

Ámbito: **Respuesta a incidentes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Disponibilidad y alcance del incidente. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **simulación de contención con dependencias**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Activos propuestos, servicios afectados, riesgos y datos faltantes**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 090](ejercicio_090/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/servicios.json](ejercicio_090/datos/servicios.json) — Modelo: basta uno de los hosts declarados para disponibilidad de cada servicio.
- [datos/activos.json](ejercicio_090/datos/activos.json) — Inventario cerrado de hosts del modelo.
- [datos/propuestas.json](ejercicio_090/datos/propuestas.json) — Escenarios independientes de planificación, nunca comandos de aislamiento.

### Requisitos

- Solo plan sin ejecutar.
- dependencias servicio → hosts.
- servicio afectado si pierde todos sus hosts por aislamiento.
- hosts desconocidos rechazan plan.
- incluir aprobación requerida y reversión conceptual.
- propuesta no implica autorización real.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Activos propuestos, servicios afectados, riesgos y datos faltantes. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Selección, correlación y comunicación de resultados.
- Pertenencia, diferencia y conservación de identidad.

### Conceptos de ciberseguridad relacionados

Relaciona afirmaciones con evidencia, documenta incertidumbre y distingue propuesta de acción de autorización para ejecutarla.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **activo candidato, dependencia, impacto estimado, condición de reversión**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué evidencia y aprobación necesitarías antes de ejecutar el plan?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 056](ejercicio_056.md), [ejercicio 081](ejercicio_081.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Servicio con A, B y aislar A → no pierde todos.
2. Aislar A, B → afectado.
3. Aislar X desconocido → plan rechazado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Redundancia declarada puede no ser funcional. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un host señalado puede ser esencial y la contención precipitada amplía el daño. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Redundancia declarada puede no ser funcional. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Conjuntos**; busca ese título en el índice.
- [NIST SP 800-61r3: respuesta a incidentes](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Redundancia declarada puede no ser funcional.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En respuesta a incidentes, este razonamiento ayuda a proteger **disponibilidad y alcance del incidente** mediante simulación de contención con dependencias. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir dependencias transitivas de servicios detectando ciclos. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
