# Ejercicio 051 — Indicadores tipados con vigencia

[Índice](README.md#indice) · [Anterior](ejercicio_050.md) · [Siguiente](ejercicio_052.md)

### Escenario de seguridad

Se cruza un feed ficticio de indicadores con observaciones locales.

### Contexto profesional

Ámbito: **Detección**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Eventos de proxy y DNS. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **indicadores tipados con vigencia**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Coincidencias vigentes y coincidencias caducadas separadas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 051](ejercicio_051/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/indicadores.json](ejercicio_051/datos/indicadores.json) — Indicadores ficticios. La confianza es declaración de la fuente, no conclusión del analista.
- [logs/observaciones.json](ejercicio_051/logs/observaciones.json) — Observaciones de fuentes sintéticas; tipo controla normalización.
- [config/parametros.json](ejercicio_051/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Tipos ip/domain/sha256.
- coincidencia exacta normalizada por tipo.
- dominios en minúsculas sin punto final.
- no permitir coincidencia de subcadena.
- indicador vigente si corte menor que expires_at.
- conservar emisor y confianza declarada sin convertirlos en certeza.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Coincidencias vigentes y coincidencias caducadas separadas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Cadenas, comparación y validación**: Conservar la entrada original y definir exactamente qué se normaliza.
- **Pertenencia, diferencia y conservación de identidad**: Comparar grupos sin confundir ausencia con un valor vacío.

### Conceptos de ciberseguridad relacionados

Separa indicador, hipótesis y conclusión. Mide cobertura y considera causas legítimas antes de asignar intención a un patrón.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- str, métodos de cadenas; justifica su necesidad y el límite de su garantía.
- set y dict cuando la identidad lo justifique; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **tipo de indicador, valor canónico, vigencia, evento coincidente**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué confianza aportan realmente procedencia y antigüedad?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 003](ejercicio_003.md), [ejercicio 006](ejercicio_006.md), [ejercicio 012](ejercicio_012.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. bad.example.test coincide consigo mismo.
2. notbad.example.test no coincide.
3. Indicador expirado en corte → caducado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un dominio puede cambiar de propietario. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un indicador de reputación desactualizado señala infraestructura ya legítima. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un dominio puede cambiar de propietario. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Métodos de Cadenas**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Conjuntos**; busca ese título en el índice.
- [CIS Controls: contexto de monitoreo defensivo](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/re.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Un dominio puede cambiar de propietario.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En detección, este razonamiento ayuda a proteger **eventos de proxy y dns** mediante indicadores tipados con vigencia. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir subdominios solo cuando el feed lo autorice explícitamente. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
