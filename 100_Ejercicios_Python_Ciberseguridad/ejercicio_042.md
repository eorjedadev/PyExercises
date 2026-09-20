# Ejercicio 042 — Secretos recibidos por configuración externa

[Índice](README.md#indice) · [Anterior](ejercicio_041.md) · [Siguiente](ejercicio_043.md)

### Escenario de seguridad

La herramienta debe exigir configuración secreta sin incrustarla ni registrarla.

### Contexto profesional

Ámbito: **Desarrollo seguro**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Credenciales de una herramienta defensiva. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **secretos recibidos por configuración externa**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Configuración pública validada y disponibilidad de secreto, nunca el secreto**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 042](ejercicio_042/README.md). Su README describe formatos, campos y procedencia sintética.

- [config/entornos_simulados.json](ejercicio_042/config/entornos_simulados.json) — Mapas simulados, no leer ni volcar os.environ real.

### Requisitos

- Trabajar con mapa simulado de variables de entorno.
- API_TOKEN obligatorio, no vacío ni espacios.
- no reflejar valor en errores.
- LOG_LEVEL permitido INFO/WARN/ERROR.
- no emitir mapa completo.
- no leer variables reales de la máquina.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Configuración pública validada y disponibilidad de secreto, nunca el secreto. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.
- **Excepciones, resultados parciales y diagnóstico**: Separar rechazo de datos, fallo operativo y resultado completo.

### Conceptos de ciberseguridad relacionados

Toda entrada externa requiere un contrato. Validar, codificar según contexto y minimizar datos de salida son responsabilidades diferentes.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- json, dict y excepciones específicas; justifica su necesidad y el límite de su garantía.
- Excepciones específicas y contratos de retorno; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **nombre de variable, secreto recibido, error público, nivel de registro**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué salida permite depurar sin revelar un secreto?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 007](ejercicio_007.md), [ejercicio 015](ejercicio_015.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Token ficticio presente y INFO → lista para uso.
2. Token ausente → error por nombre de campo.
3. LOG_LEVEL desconocido → error sin volcado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Presencia no acredita que el secreto sea válido o tenga permisos mínimos. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una rotación aún no propagada puede causar configuración incompleta. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Presencia no acredita que el secreto sea válido o tenga permisos mínimos. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Manejo de Errores y Excepciones**; busca ese título en el índice.
- [OWASP: logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/json.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Presencia no acredita que el secreto sea válido o tenga permisos mínimos.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En desarrollo seguro, este razonamiento ayuda a proteger **credenciales de una herramienta defensiva** mediante secretos recibidos por configuración externa. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Modelar rotación con identificador de versión sin copiar el valor. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
