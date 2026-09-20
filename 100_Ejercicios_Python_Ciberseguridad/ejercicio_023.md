# Ejercicio 023 — Modelo de bloqueo y recuperación

[Índice](README.md#indice) · [Anterior](ejercicio_022.md) · [Siguiente](ejercicio_024.md)

### Escenario de seguridad

Desarrollo necesita simular una política antes de implementarla en el portal.

### Contexto profesional

Ámbito: **Autenticación**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Disponibilidad y resistencia de cuentas. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **modelo de bloqueo y recuperación**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Decisiones y estado después de cada evento; no efectuar autenticación real**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 023](ejercicio_023/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/intentos.json](ejercicio_023/datos/intentos.json) — Reloj de segundos relativo al inicio; no esperar ni autenticar realmente.

### Requisitos

- Por cuenta,3 fallos desde último éxito bloquean 60 segundos.
- durante bloqueo rechazar intentos sin contar ni alargar.
- en instante de fin desbloquear y contador0.
- éxito fuera reinicia.
- reloj sintético ordenado.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Decisiones y estado después de cada evento; no efectuar autenticación real. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Transiciones, invariantes y funciones con efectos delimitados**: Explicar qué puede cambiar al aceptar o rechazar una operación.
- **Pruebas de contrato, regresión y fallos simulados**: Contrastar observaciones esperadas sin reproducir el algoritmo como oráculo.

### Conceptos de ciberseguridad relacionados

Distingue identidad declarada, autenticación, sesión y autorización. Un fallo repetido es una observación; una intrusión requiere más respaldo.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **Funciones; clases solo si protegen invariantes**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **unittest y sustitución de dependencias en pruebas**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **contador consecutivo, bloqueo hasta, instante actual, decisión**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué coste tiene esta defensa para usuarios reales?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?
- Recupera razonamiento de [ejercicio 002](ejercicio_002.md), [ejercicio 012](ejercicio_012.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Fallos en 0,1,2 → bloqueo hasta 62.
2. Intento en 61 → bloqueado.
3. Intento ok en 62 → aceptado.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Una política de bloqueo puede facilitar denegación de servicio a usuarios. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Errores legítimos también disparan un bloqueo por política. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Una política de bloqueo puede facilitar denegación de servicio a usuarios. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Programación Orientada a Objetos**; busca ese título en el índice.
- [INTENSIVO DE PYTHON (Eric Matthes).md](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md) — **11. Probar el código**; busca ese título en el índice.
- [OWASP: autenticación](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/unittest.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Una política de bloqueo puede facilitar denegación de servicio a usuarios.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En autenticación, este razonamiento ayuda a proteger **disponibilidad y resistencia de cuentas** mediante modelo de bloqueo y recuperación. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Separar bloqueo de cuenta de limitación por origen. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
