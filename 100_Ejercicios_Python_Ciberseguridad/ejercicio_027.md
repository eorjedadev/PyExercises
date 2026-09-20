# Ejercicio 027 — Emisión y consumo de tokens de laboratorio

[Índice](README.md#indice) · [Anterior](ejercicio_026.md) · [Siguiente](ejercicio_028.md)

### Escenario de seguridad

Desarrollo necesita modelar tokens de un solo uso sin contraseñas reales.

### Contexto profesional

Ámbito: **Autenticación**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Recuperación de acceso simulada. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **emisión y consumo de tokens de laboratorio**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Simulación de emisión/consumo y pruebas de estados sin publicar secretos en reporte**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 027](ejercicio_027/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/escenarios.json](ejercicio_027/datos/escenarios.json) — Guiones de prueba independientes: cada escenario emite su propio token durante la implementación. No se proporcionan tokens.
- [config/parametros.json](ejercicio_027/config/parametros.json) — Parámetros explícitos del laboratorio; no son recomendaciones universales.

### Requisitos

- Generar tokens con fuente criptográfica y 32 bytes aleatorios.
- almacenar solo huella y metadatos.
- vence en 120 segundos desde emisión, extremo excluido.
- consumo correcto una sola vez.
- no escribir token en logs ni usar datos suministrados como aleatoriedad.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Simulación de emisión/consumo y pruebas de estados sin publicar secretos en reporte. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Transiciones, invariantes y funciones con efectos delimitados**: Explicar qué puede cambiar al aceptar o rechazar una operación.
- **Contratos de APIs criptográficas y manejo de errores**: Usar primitivas mantenidas con entradas bien definidas, sin diseñar criptografía propia.

### Conceptos de ciberseguridad relacionados

Distingue identidad declarada, autenticación, sesión y autorización. Un fallo repetido es una observación; una intrusión requiere más respaldo.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Investiga secrets y gestión del estado. Debes justificar la fuente de aleatoriedad; no demostrar entropía contando colisiones en una muestra.

### Diseño de variables

Identifica estas entidades: **huella de token, expiración, instante simulado, estado de consumo**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cómo probarás estados sin esperar ni fijar tokens reales en el código?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 007](ejercicio_007.md), [ejercicio 012](ejercicio_012.md), [ejercicio 023](ejercicio_023.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Emitir en 0, consumir en 119 → acepta.
2. Consumir en 120 → expirado.
3. Consumir dos veces → segundo rechazado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

La longitud observada no demuestra entropía de la fuente. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Repetición por usuario puede ser doble clic, no uso hostil. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- La longitud observada no demuestra entropía de la fuente. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Programación Orientada a Objetos**; busca ese título en el índice.
- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [OWASP: autenticación](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://docs.python.org/3/library/secrets.html) — consulta el contrato y las excepciones, no copies una solución.
- [Python: secrets](https://docs.python.org/3/library/secrets.html).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **La longitud observada no demuestra entropía de la fuente.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En autenticación, este razonamiento ayuda a proteger **recuperación de acceso simulada** mediante emisión y consumo de tokens de laboratorio. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Revocar tokens anteriores cuando se emita uno nuevo. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
