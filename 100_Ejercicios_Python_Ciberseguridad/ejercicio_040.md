# Ejercicio 040 — Exportación de reportes sin fórmulas activas

[Índice](README.md#indice) · [Anterior](ejercicio_039.md) · [Siguiente](ejercicio_041.md)

### Escenario de seguridad

Campos ajenos podrían ser interpretados como fórmulas al abrir un CSV.

### Contexto profesional

Ámbito: **Desarrollo seguro**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Hoja de cálculo usada por analistas. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **exportación de reportes sin fórmulas activas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **CSV de vista protegida y conteo de campos transformados**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 040](ejercicio_040/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/campos.json](ejercicio_040/datos/campos.json) — Campos textuales para exportar una columna campo; los números de teléfono son ficticios.

### Requisitos

- Para campos textuales cuyo primer carácter tras ignorar espacio/tab/CR/LF sea =,+,-,@, anteponer apóstrofo al texto completo.
- usar serialización CSV correcta.
- preservar original solo en evidencia, no en vista compartida.
- política depende del consumidor.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

CSV de vista protegida y conteo de campos transformados. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Registros tabulares, conversión y trazabilidad**: Respetar delimitadores y campos citados sin perder la línea de origen.
- **Cadenas, comparación y validación**: Conservar la entrada original y definir exactamente qué se normaliza.

### Conceptos de ciberseguridad relacionados

Toda entrada externa requiere un contrato. Validar, codificar según contexto y minimizar datos de salida son responsabilidades diferentes.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- csv y conversiones verificadas; justifica su necesidad y el límite de su garantía.
- str, métodos de cadenas; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **campo original, prefijo significativo, campo exportado, transformación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cómo verificarías la interpretación en el consumidor autorizado?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 007](ejercicio_007.md), [ejercicio 033](ejercicio_033.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. =SUM(1,2) → texto prefijado.
2. Espacios seguidos de @x → prefijado.
3. Ana → sin cambio.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

El tratamiento del apóstrofo depende del programa que abre el CSV. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un número de teléfono que empieza con + puede activar la política. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- El tratamiento del apóstrofo depende del programa que abre el CSV. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports Importantes por Área**; busca ese título en el índice.
- [Diccionario_Python.md](../Diccionario_Python.md) — **Métodos de Cadenas**; busca ese título en el índice.
- [OWASP: logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/csv.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **El tratamiento del apóstrofo depende del programa que abre el CSV.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En desarrollo seguro, este razonamiento ayuda a proteger **hoja de cálculo usada por analistas** mediante exportación de reportes sin fórmulas activas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Crear una salida JSON alternativa que no pretenda ser una hoja de cálculo. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
