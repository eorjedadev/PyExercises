# Ejercicio 044 — Permisos efectivos en una matriz acotada

[Índice](README.md#indice) · [Anterior](ejercicio_043.md) · [Siguiente](ejercicio_045.md)

### Escenario de seguridad

Administración entrega grupos, membresías y reglas simplificadas para evaluar acceso.

### Contexto profesional

Ámbito: **Sistemas**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Recursos compartidos. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **permisos efectivos en una matriz acotada**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Decisión y reglas que participaron para cada solicitud**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 044](ejercicio_044/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/grupos.json](ejercicio_044/datos/grupos.json) — Membresías de un nivel; no hay grupos implícitos.
- [config/reglas.json](ejercicio_044/config/reglas.json) — Lenguaje simplificado con deny prevalente; no es ACL nativa de un sistema.
- [datos/solicitudes.json](ejercicio_044/datos/solicitudes.json) — Solicitudes contra reglas y grupos declarados.

### Requisitos

- Solo allow/deny de acción leer por usuario o grupo.
- deny coincidente prevalece.
- sin allow se deniega.
- grupos de un nivel sin anidación.
- esta política no emula ACL Windows ni POSIX.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Decisión y reglas que participaron para cada solicitud. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Pertenencia, diferencia y conservación de identidad**: Comparar grupos sin confundir ausencia con un valor vacío.
- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.

### Conceptos de ciberseguridad relacionados

Un ajuste exportado no equivale siempre al control efectivo. Distingue modelo del ejercicio, semántica de plataforma y ejecución realmente observada.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- set y dict cuando la identidad lo justifique; justifica su necesidad y el límite de su garantía.
- json, dict y excepciones específicas; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **sujeto, grupo, regla coincidente, permiso efectivo simulado**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Por qué no puedes trasladar esta precedencia directamente a cualquier sistema operativo?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 005](ejercicio_005.md), [ejercicio 031](ejercicio_031.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. ana en lectores con allow → permite.
2. beto con allow de grupo y deny personal → deniega.
3. cora sin regla → deniega.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un nombre de grupo no permite inferir sus miembros. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una denegación intencional por separación de funciones puede parecer error. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un nombre de grupo no permite inferir sus miembros. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Conjuntos**; busca ese título en el índice.
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [CIS Controls: contexto de configuración y auditoría](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/collections.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Un nombre de grupo no permite inferir sus miembros.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En sistemas, este razonamiento ayuda a proteger **recursos compartidos** mediante permisos efectivos en una matriz acotada. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Incorporar grupos anidados detectando ciclos. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
