# Ejercicio 095 — Publicación de reportes sin perder la versión anterior

[Índice](README.md#indice) · [Anterior](ejercicio_094.md) · [Siguiente](ejercicio_096.md)

### Escenario de seguridad

Una escritura interrumpida no debe sustituir un informe válido por uno incompleto.

### Contexto profesional

Ámbito: **Automatización**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Disponibilidad del reporte confirmado. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **publicación de reportes sin perder la versión anterior**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Reporte nuevo confirmado o error con versión anterior intacta**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 095](ejercicio_095/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/reporte_previo.json](ejercicio_095/datos/reporte_previo.json) — Copiar a un directorio de salida de práctica; nunca usar el recurso original como destino.
- [datos/reporte_nuevo.json](ejercicio_095/datos/reporte_nuevo.json) — Objeto a publicar en escenarios de prueba, no implementación de escritura.
- [config/fallos.json](ejercicio_095/config/fallos.json) — Sustituir dependencia de escritura para simular fallo; no dañar permisos ni disco.

### Requisitos

- Preparar resultado completo antes de publicar.
- fallo de serialización, escritura o sustitución conserva destino previo.
- fallos simulados sin cortar energía.
- limpieza de temporales con diagnóstico.
- éxito verificable.
- no prometer resistencia universal a fallos del sistema.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Reporte nuevo confirmado o error con versión anterior intacta. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Archivos, rutas, bytes y excepciones.
- Pruebas de contrato, regresión y fallos simulados.

### Conceptos de ciberseguridad relacionados

La herramienta también debe fallar de forma visible y proteger evidencia. Un resultado parcial no puede presentarse como ausencia de hallazgos.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **reporte provisional, destino confirmado, fase de fallo, estado de publicación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué frontera separa preparado de publicado?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 047](ejercicio_047.md), [ejercicio 079](ejercicio_079.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Fallo a mitad de escritura → destino previo idéntico.
2. Fallo de sustitución → previo intacto.
3. Éxito → JSON completo validable.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un archivo existente no implica última ejecución exitosa. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un fallo de disco es operativo, no indicador suficiente de sabotaje. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un archivo existente no implica última ejecución exitosa. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Archivos y Context Managers**; busca ese título en el índice.
- [INTENSIVO DE PYTHON (Eric Matthes).md](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md) — **11. Probar el código**; busca ese título en el índice.
- [OWASP: registro y fallos de logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Un archivo existente no implica última ejecución exitosa.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En automatización, este razonamiento ayuda a proteger **disponibilidad del reporte confirmado** mediante publicación de reportes sin perder la versión anterior. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Agregar manifiesto de integridad al resultado publicado. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
