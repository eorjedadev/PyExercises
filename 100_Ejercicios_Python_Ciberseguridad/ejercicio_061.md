# Ejercicio 061 — Accesos después de una baja de cuenta

[Índice](README.md#indice) · [Anterior](ejercicio_060.md) · [Siguiente](ejercicio_062.md)

### Escenario de seguridad

Se correlacionan accesos con cambios de estado del directorio.

### Contexto profesional

Ámbito: **Autenticación**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Cuentas deshabilitadas. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **accesos después de una baja de cuenta**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Accesos incompatibles con el estado y eventos de soporte**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 061](ejercicio_061/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/usuarios.json](ejercicio_061/datos/usuarios.json) — Usuarios conocidos, inicialmente habilitados.
- [logs/cambios.json](ejercicio_061/logs/cambios.json) — Cambios de identidad observados, no decisiones que deba ejecutar el alumno.
- [logs/auth.json](ejercicio_061/logs/auth.json) — Eventos de autenticación, no uso de sesión preexistente.

### Requisitos

- Por cuenta estado inicial habilitada.
- aplicar disable/enable según tiempo.
- empate cambios antes de acceso.
- éxito mientras deshabilitada se revisa.
- usuarios no inventariados → sin contexto.
- no asumir que todos los sistemas comparten directorio.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Accesos incompatibles con el estado y eventos de soporte. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Zonas, intervalos, orden e incertidumbre.
- Transiciones, invariantes y funciones con efectos delimitados.

### Conceptos de ciberseguridad relacionados

Distingue identidad declarada, autenticación, sesión y autorización. Un fallo repetido es una observación; una intrusión requiere más respaldo.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **cuenta, estado temporal, acceso exitoso, fuente de identidad**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿La baja revoca sesiones o solo impide autenticaciones nuevas?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 012](ejercicio_012.md), [ejercicio 048](ejercicio_048.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. Disable ana10:00, éxito10:01 → revisión.
2. Enable10:02, éxito10:03 → no activa regla.
3. Cuenta desconocida → sin contexto.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Tiempo desalineado puede invertir el orden aparente. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una aplicación con sesiones existentes puede registrar actividad tras baja. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Tiempo desalineado puede invertir el orden aparente. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Programación Orientada a Objetos**; busca ese título en el índice.
- [OWASP: autenticación](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Tiempo desalineado puede invertir el orden aparente.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En autenticación, este razonamiento ayuda a proteger **cuentas deshabilitadas** mediante accesos después de una baja de cuenta. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir sesiones y distinguir autenticación de uso de sesión. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
