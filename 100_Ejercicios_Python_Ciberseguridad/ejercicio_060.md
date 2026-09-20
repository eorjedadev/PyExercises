# Ejercicio 060 — Cambios de huella TLS declarada

[Índice](README.md#indice) · [Anterior](ejercicio_059.md) · [Siguiente](ejercicio_061.md)

### Escenario de seguridad

Un cliente registró huellas de certificado distintas para el mismo endpoint.

### Contexto profesional

Ámbito: **Redes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Continuidad de servicios. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **cambios de huella tls declarada**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Transiciones de huella y relación con renovación declarada**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 060](ejercicio_060/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/tls.json](ejercicio_060/logs/tls.json) — Huellas sintéticas de certificados observados, no certificados reales.
- [config/renovaciones.json](ejercicio_060/config/renovaciones.json) — Cobertura temporal incluye inicio y excluye fin.

### Requisitos

- Endpoint es host/puerto.
- ordenar observaciones.
- detectar cambios de SHA-256 validado.
- unir con ventanas de renovación por endpoint.
- cambio dentro autorizado sigue visible.
- no validar criptografía del certificado.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Transiciones de huella y relación con renovación declarada. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Bytes, comparación de huellas y validación de formatos**: Comprobar igualdad respecto de una referencia sin confundirla con procedencia.
- **Zonas, intervalos, orden e incertidumbre**: Comparar instantes y fronteras temporales con una referencia explícita.

### Conceptos de ciberseguridad relacionados

Una dirección, puerto o nombre no identifica intención ni persona. Compara contra alcance e inventario explícitos y conserva el contexto de la observación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- hashlib y lectura binaria; justifica su necesidad y el límite de su garantía.
- datetime y timedelta; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **endpoint, huella anterior, huella nueva, ventana de renovación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué permitiría distinguir renovación de sustitución no autorizada?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 019](ejercicio_019.md), [ejercicio 030](ejercicio_030.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. api:443 cambia dentro de ventana → cambio previsto.
2. otro:443 cambia sin ventana → revisión.
3. Mismo hash repetido → sin transición.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Balanceo entre certificados legítimos puede alternar huellas. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Renovaciones y despliegues coordinados generan cambios normales. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Balanceo entre certificados legítimos puede alternar huellas. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [CIS Controls: contexto de inventario y defensa](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/hashlib.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Balanceo entre certificados legítimos puede alternar huellas.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En redes, este razonamiento ayuda a proteger **continuidad de servicios** mediante cambios de huella tls declarada. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Separar observaciones por nodo del balanceador. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
