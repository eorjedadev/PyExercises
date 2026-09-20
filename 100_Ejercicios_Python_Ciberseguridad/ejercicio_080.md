# Ejercicio 080 — Cronología con incertidumbre de reloj

[Índice](README.md#indice) · [Anterior](ejercicio_079.md) · [Siguiente](ejercicio_081.md)

### Escenario de seguridad

Tres fuentes tienen desfases estimados y márgenes de error distintos.

### Contexto profesional

Ámbito: **Forense**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Orden temporal de un incidente. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **cronología con incertidumbre de reloj**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Cronología de intervalos y relaciones de orden respaldadas o inciertas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 080](ejercicio_080/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/tiempos.json](ejercicio_080/logs/tiempos.json) — Instantes observados; la corrección no reemplaza el texto original.
- [datos/calibracion.json](ejercicio_080/datos/calibracion.json) — offset = reloj de fuente menos referencia. Error simétrico en segundos; se permiten intervalos que cruzan la fecha.

### Requisitos

- Instante corregido igual observado menos desfase declarado.
- representar intervalo corregido±error no negativo.
- afirmar A antes B solo si límite superiorA es menor que inferiorB.
- intervalos que se tocan → orden no asegurado.
- conservar originales.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Cronología de intervalos y relaciones de orden respaldadas o inciertas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Zonas, intervalos, orden e incertidumbre.
- Identidad, agregación y relaciones entre registros.

### Conceptos de ciberseguridad relacionados

Conserva origen, integridad y trazabilidad. Un cambio observado no identifica su causa ni autor; una copia transformada no debe presentarse como el original.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **tiempo observado, desfase estimado, margen de error, orden parcial**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué hipótesis siguen siendo posibles si cambia el orden de dos eventos?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 048](ejercicio_048.md), [ejercicio 073](ejercicio_073.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. A intervalo[0,2] y B puntual en 4 → A antes.
2. En una copia, A[0,4] y B puntual en 4 → no asegurar.
3. Fuente sin calibración → incertidumbre no cuantificada.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

No convertir una estimación en timestamp exacto. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Relojes desincronizados pueden aparentar secuencias imposibles. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- No convertir una estimación en timestamp exacto. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [NIST SP 800-61r3: contexto de respuesta](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **No convertir una estimación en timestamp exacto.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En forense, este razonamiento ayuda a proteger **orden temporal de un incidente** mediante cronología con incertidumbre de reloj. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir latencia de recolección como dimensión diferente. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
