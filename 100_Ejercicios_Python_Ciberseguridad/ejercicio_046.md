# Ejercicio 046 — Auditoría portable de modos POSIX y ACL exportadas

[Índice](README.md#indice) · [Anterior](ejercicio_045.md) · [Siguiente](ejercicio_047.md)

### Escenario de seguridad

El equipo necesita un reporte comparable sin aplicar semánticas del sistema anfitrión.

### Contexto profesional

Ámbito: **Sistemas**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Permisos de recursos de Windows y Linux. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **auditoría portable de modos posix y acl exportadas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Hallazgos por plataforma y lista de limitaciones no evaluadas**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 046](ejercicio_046/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/permisos.json](ejercicio_046/datos/permisos.json) — Exportaciones simplificadas; plataformas comparadas por controles acotados, no por permisos efectivos completos.

### Requisitos

- POSIX: revisar escritura de otros.
- Windows simplificado: revisar allow Write para Everyone salvo deny Write para Everyone en mismo recurso.
- evaluar modelos separados.
- no deducir acceso real por herencia o pertenencia no incluidas.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Hallazgos por plataforma y lista de limitaciones no evaluadas. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.
- **Condiciones, tipos y precedencia de políticas**: Evitar que un valor ausente o una regla general oculten otra decisión.

### Conceptos de ciberseguridad relacionados

Un ajuste exportado no equivale siempre al control efectivo. Distingue modelo del ejercicio, semántica de plataforma y ejecución realmente observada.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- json, dict y excepciones específicas; justifica su necesidad y el límite de su garantía.
- if, operadores booleanos, funciones; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **modelo de permisos, recurso, entrada declarada, alcance del modelo**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué información adicional necesitarías en cada plataforma?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 005](ejercicio_005.md), [ejercicio 044](ejercicio_044.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Linux666 → escritura de otros.
2. Windows allow Everyone Write sin deny → revisión.
3. Windows deny equivalente → no concede en modelo.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

No convertir máscara octal en una ACL Windows. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Carpetas temporales compartidas pueden permitir escritura por diseño. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- No convertir máscara octal en una ACL Windows. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Condicionales**; busca ese título en el índice.
- [CIS Controls: contexto de configuración y auditoría](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/json.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **No convertir máscara octal en una ACL Windows.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En sistemas, este razonamiento ayuda a proteger **permisos de recursos de windows y linux** mediante auditoría portable de modos posix y acl exportadas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir un campo de herencia y mantener los casos no evaluables. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
