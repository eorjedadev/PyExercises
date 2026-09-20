# Ejercicio 057 — Consultas a dominios nuevos respecto de una base

[Índice](README.md#indice) · [Anterior](ejercicio_056.md) · [Siguiente](ejercicio_058.md)

### Escenario de seguridad

Se compara actividad actual con una base histórica acotada.

### Contexto profesional

Ámbito: **Redes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Visibilidad DNS. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **consultas a dominios nuevos respecto de una base**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Nombres nuevos para la base y clientes observadores**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 057](ejercicio_057/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/base_dns.json](ejercicio_057/datos/base_dns.json) — Base histórica acotada a una captura ficticia, no reputación global.
- [logs/dns_actual.json](ejercicio_057/logs/dns_actual.json) — Comparación del nombre completo; todos los nombres son de documentación.
- [config/cobertura.json](ejercicio_057/config/cobertura.json) — Cobertura declarada; no representa toda la historia de los clientes.

### Requisitos

- Normalizar nombre completo a minúsculas y retirar un punto final.
- diferencia exacta, sin calcular dominio registrable.
- base es cobertura declarada, no lista global.
- consultas inválidas se separan.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Nombres nuevos para la base y clientes observadores. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Cadenas, comparación y validación**: Conservar la entrada original y definir exactamente qué se normaliza.
- **Pertenencia, diferencia y conservación de identidad**: Comparar grupos sin confundir ausencia con un valor vacío.

### Conceptos de ciberseguridad relacionados

Una dirección, puerto o nombre no identifica intención ni persona. Compara contra alcance e inventario explícitos y conserva el contexto de la observación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- str, métodos de cadenas; justifica su necesidad y el límite de su garantía.
- set y dict cuando la identidad lo justifique; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **nombre normalizado, cobertura histórica, nombre no visto, cliente**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cuándo puedes afirmar nuevo para esta base y no nuevo en Internet?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 014](ejercicio_014.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. A.EXAMPLE.TEST. en base a.example.test → conocido.
2. nuevo.example.test ausente → nuevo.
3. Cadena vacía → inválida.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Una base corta exagera novedad. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una actualización de software puede introducir dominios nuevos. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Una base corta exagera novedad. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Métodos de Cadenas**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Conjuntos**; busca ese título en el índice.
- [CIS Controls: contexto de inventario y defensa](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/re.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Una base corta exagera novedad.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En redes, este razonamiento ayuda a proteger **visibilidad dns** mediante consultas a dominios nuevos respecto de una base. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Agregar fecha de primera observación sin consultar WHOIS. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
