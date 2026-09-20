# Ejercicio 030 — Vigencia declarada de certificados

[Índice](README.md#indice) · [Anterior](ejercicio_029.md) · [Siguiente](ejercicio_031.md)

### Escenario de seguridad

Se revisan metadatos ya exportados sin conectarse a ningún servidor.

### Contexto profesional

Ámbito: **Redes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Identidad TLS de servicios internos. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **vigencia declarada de certificados**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Vigencia, coincidencia de nombre y necesidad de revisión separadas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 030](ejercicio_030/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/certificados.json](ejercicio_030/datos/certificados.json) — Metadatos extraídos ficticios; no son certificados que acrediten identidad.
- [config/parametros.json](ejercicio_030/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Por certificado, comparar corte UTC con not_before y not_after.
- vigente si ambos extremos incluidos.
- advertir renovación cuando faltan como máximo 7 días completos.
- SAN debe contener hostname exacto sin comodines en este ejercicio.
- no verificar cadena criptográfica.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Vigencia, coincidencia de nombre y necesidad de revisión separadas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Zonas, intervalos, orden e incertidumbre**: Comparar instantes y fronteras temporales con una referencia explícita.
- **Interpretación de campos, formatos y resultados de controles**: No confundir un texto declarado por el cliente con un dato confiado.

### Conceptos de ciberseguridad relacionados

Una dirección, puerto o nombre no identifica intención ni persona. Compara contra alcance e inventario explícitos y conserva el contexto de la observación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- datetime y timedelta; justifica su necesidad y el límite de su garantía.
- Funciones de validación; urllib.parse para URLs cuando corresponda; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **corte UTC, intervalo de certificado, SAN declarado, nombre esperado**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué comprobaciones de TLS no estás realizando?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 008](ejercicio_008.md), [ejercicio 012](ejercicio_012.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. C1 vigente y nombre en SAN → dos controles conformes.
2. C2 expirado → no vigente.
3. C3 nombre ausente → no coincide.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Metadatos no acreditan firma, revocación ni confianza en emisor. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un alias omitido del inventario puede causar aparente discordancia de nombre. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Metadatos no acreditan firma, revocación ni confianza en emisor. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [CIS Controls: contexto de inventario y defensa](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/datetime.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Metadatos no acreditan firma, revocación ni confianza en emisor.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En redes, este razonamiento ayuda a proteger **identidad tls de servicios internos** mediante vigencia declarada de certificados. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir comodines con una regla explícita de una sola etiqueta. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
