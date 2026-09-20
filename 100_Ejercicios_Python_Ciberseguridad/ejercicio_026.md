# Ejercicio 026 — Autenticidad de mensajes con HMAC

[Índice](README.md#indice) · [Anterior](ejercicio_025.md) · [Siguiente](ejercicio_027.md)

### Escenario de seguridad

Se entregan mensajes inertes y etiquetas de autenticación creadas con una clave ficticia.

### Contexto profesional

Ámbito: **Criptografía aplicada**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Mensajes entre componentes de laboratorio. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **autenticidad de mensajes con hmac**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Estado de verificación por mensaje, errores de formato y límites de atribución**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 026](ejercicio_026/README.md). Su README describe formatos, campos y procedencia sintética.

- [config/clave_lab.bin](ejercicio_026/config/clave_lab.bin) — Clave pública de práctica; no reutilizar como secreto real ni incrustar su valor en código.
- [datos/m1.bin](ejercicio_026/datos/m1.bin) — Mensaje inerte; autenticar bytes exactos, incluido LF final.
- [datos/m2.bin](ejercicio_026/datos/m2.bin) — Variante de contenido que conserva etiqueta de otro mensaje.
- [datos/etiquetas.json](ejercicio_026/datos/etiquetas.json) — Rutas relativas a datos; etiquetas como hex ASCII. H3 tiene formato intencionalmente inválido.

### Requisitos

- Verificar HMAC-SHA256 sobre bytes exactos, sin reserializar JSON.
- clave se recibe del archivo de laboratorio y no se incrusta en el programa.
- comparación adecuada para etiquetas.
- no confundir HMAC con firma de identidad pública ni cifrado.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Estado de verificación por mensaje, errores de formato y límites de atribución. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Contratos de APIs criptográficas y manejo de errores**: Usar primitivas mantenidas con entradas bien definidas, sin diseñar criptografía propia.
- **Representación binaria, codificación y límites de tamaño**: Medir y conservar los bytes que sustentan una comprobación.

### Conceptos de ciberseguridad relacionados

Codificación, hash, HMAC, firma y cifrado ofrecen propiedades distintas. La clave, el formato exacto y el modelo de confianza forman parte del contrato.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Investiga hmac, compare_digest y el contrato de bytes. La clave se recibe como recurso externo de laboratorio.

### Diseño de variables

Identifica estas entidades: **mensaje exacto, etiqueta recibida, clave de laboratorio, verificación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué puede falsificar cualquiera que conozca la clave compartida?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 006](ejercicio_006.md), [ejercicio 009](ejercicio_009.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. m1.bin con etiqueta original → verifica.
2. m2.bin alterado con etiqueta de m1 → no verifica.
3. etiqueta de longitud incorrecta → formato inválido.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Cambiar un salto de línea cambia los bytes autenticados. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una conversión de codificación accidental también rompe la autenticación. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Cambiar un salto de línea cambia los bytes autenticados. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Bytes, Unicode y Codificación**; busca ese título en el índice.
- [OWASP: almacenamiento criptográfico](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial pertinente](https://docs.python.org/3/library/hmac.html) — consulta el contrato y las excepciones, no copies una solución.
- [Python: HMAC y comparación de etiquetas](https://docs.python.org/3/library/hmac.html).

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Cambiar un salto de línea cambia los bytes autenticados.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En criptografía aplicada, este razonamiento ayuda a proteger **mensajes entre componentes de laboratorio** mediante autenticidad de mensajes con hmac. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir identificador de clave para una rotación controlada. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
