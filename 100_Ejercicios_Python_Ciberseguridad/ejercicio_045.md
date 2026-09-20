# Ejercicio 045 — Deriva de configuración entre capturas

[Índice](README.md#indice) · [Anterior](ejercicio_044.md) · [Siguiente](ejercicio_046.md)

### Escenario de seguridad

Dos capturas deben compararse con un inventario de cambios autorizados.

### Contexto profesional

Ámbito: **DevSecOps**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Configuración de seguridad publicada. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **deriva de configuración entre capturas**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Diferencias redactadas y cobertura de autorización**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 045](ejercicio_045/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/antes.json](ejercicio_045/datos/antes.json) — Captura anterior; token es ficticio.
- [datos/despues.json](ejercicio_045/datos/despues.json) — Captura posterior; secretos siempre redactados en resultados.
- [config/aprobaciones.json](ejercicio_045/config/aprobaciones.json) — Rutas lógicas con punto; en estos datos las claves no contienen puntos. Solo approved verdadero cubre.

### Requisitos

- Comparar campos hoja por ruta lógica.
- distinguir añadido, retirado y cambiado.
- no imprimir valores de claves secret/token/password.
- autorización requiere ruta exacta y valor nuevo permitido, salvo secretos solo aprobación de cambio.
- no marcar cambio autorizado como invisible.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Diferencias redactadas y cobertura de autorización. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Estructuras anidadas, tipos y contratos de entrada**: Diferenciar documento legible de documento que satisface el esquema.
- **Propiedad de datos, copias y efectos**: Conservar fuentes sin cambios mientras se genera una vista derivada.

### Conceptos de ciberseguridad relacionados

La configuración declarada, su contexto de despliegue y su estado efectivo deben distinguirse. La revisión automatizada cubre un contrato específico.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- json, dict y excepciones específicas; justifica su necesidad y el límite de su garantía.
- Copias e interfaces que no exponen mutables internos; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **ruta de configuración, valor previo redactado, valor nuevo, aprobación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué diferencia existe entre cambio esperado y configuración segura?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 015](ejercicio_015.md), [ejercicio 019](ejercicio_019.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. debug false → true sin aprobación → revisión.
2. timeout30 → 60 aprobado → cambio autorizado.
3. token cambiado → valores redactados.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Igualdad de capturas no garantiza que no hubo cambios intermedios. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un despliegue aprobado produce deriva legítima. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Igualdad de capturas no garantiza que no hubo cambios intermedios. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON**; busca ese título en el índice.
- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md) — **Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos**; busca ese título en el índice.
- [CIS Controls: contexto de defensa de activos](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/json.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Igualdad de capturas no garantiza que no hubo cambios intermedios.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En devsecops, este razonamiento ayuda a proteger **configuración de seguridad publicada** mediante deriva de configuración entre capturas. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Comparar tres capturas para detectar cambios transitorios. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
