# Ejercicio 007 — Redacción de secretos en eventos

[Índice](README.md#indice) · [Anterior](ejercicio_006.md) · [Siguiente](ejercicio_008.md)

### Escenario de seguridad

Un JSON de diagnósticos contiene datos que no deben aparecer en la salida pública.

### Contexto profesional

Ámbito: **Desarrollo seguro**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Logs que se compartirán con soporte. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **redacción de secretos en eventos**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Copia redactada y contador de campos retirados**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 007](ejercicio_007/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/eventos.json](ejercicio_007/logs/eventos.json) — Valores exclusivamente ficticios. La clasificación viene de claves, no de patrones de sus valores.

### Requisitos

- Recorrer objetos y listas.
- reemplazar valores de claves password, token, api_key sin distinguir mayúsculas por [REDACTADO].
- conservar forma y demás datos.
- no modificar origen ni mostrar valores retirados.
- no asegurar detección de secretos en texto libre.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Copia redactada y contador de campos retirados. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.
- **Propiedad de datos, copias y efectos**: Conservar fuentes sin cambios mientras se genera una vista derivada.

### Conceptos de ciberseguridad relacionados

Toda entrada externa requiere un contrato. Validar, codificar según contexto y minimizar datos de salida son responsabilidades diferentes.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **json, dict y excepciones específicas**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **Copias e interfaces que no exponen mutables internos**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **campo sensible, ruta lógica, copia redactada, cantidad retirada**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Cómo comprobarás que el reporte no vuelve a filtrar lo retirado?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?

### Casos de prueba

1. password de E1 → marcador.
2. TOKEN anidado de E2 → marcador.
3. monkey de E3 → se conserva.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Un secreto incrustado en un mensaje libre queda fuera de esta política. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una clave token puede almacenar una etiqueta no sensible pero se retira por política. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Un secreto incrustado en un mensaje libre queda fuera de esta política. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md) — **Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos**; busca ese título en el índice.
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

Contrasta tu resultado con esta limitación: **Un secreto incrustado en un mensaje libre queda fuera de esta política.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En desarrollo seguro, este razonamiento ayuda a proteger **logs que se compartirán con soporte** mediante redacción de secretos en eventos. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir detección de una marca ficticia en texto libre sin imprimirla. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
