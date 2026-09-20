# Ejercicio 085 — Priorización contextual de avisos de dependencias

[Índice](README.md#indice) · [Anterior](ejercicio_084.md) · [Siguiente](ejercicio_086.md)

### Escenario de seguridad

Una lista de avisos ficticios requiere priorización operativa basada en evidencia local.

### Contexto profesional

Ámbito: **DevSecOps**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Servicios que contienen componentes señalados. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **priorización contextual de avisos de dependencias**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Cola con razones y tareas para completar contexto**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 085](ejercicio_085/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/dependencias.json](ejercicio_085/datos/dependencias.json) — Copia independiente para recuperar el contrato anterior. Nombres y versiones ficticios; no representan avisos de paquetes reales.
- [datos/avisos.json](ejercicio_085/datos/avisos.json) — Copia independiente para recuperar el contrato anterior. Feed ficticio cerrado; no son CVE ni reglas de versión universales.
- [datos/contexto.json](ejercicio_085/datos/contexto.json) — Unión por component_id con id del inventario. P5 carece de contexto; no completar con falso.

### Requisitos

- Primero evaluar afectación según41.
- prioridad alta si afectado, expuesto y función afectada utilizada.
- normal si afectado y ambos datos conocidos pero no ambos verdaderos.
- faltantes → pendiente de contexto, no baja.
- no usar puntuación inventada como probabilidad.
- componentes no afectados se clasifican fuera del aviso, no en prioridad normal.
- versión no evaluable conserva ese estado.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Cola con razones y tareas para completar contexto. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

Relaciona por tu cuenta estos fundamentos con el problema:

- Identidad, agregación y relaciones entre registros.
- Selección, correlación y comunicación de resultados.

### Conceptos de ciberseguridad relacionados

La configuración declarada, su contexto de despliegue y su estado efectivo deben distinguirse. La revisión automatizada cubre un contrato específico.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Elige primero tus herramientas: ¿qué estructura representa identidades y procedencia?, ¿qué módulo investigarías para los formatos presentes?, ¿qué dependencia podrías sustituir durante las pruebas? Justifica al menos una alternativa descartada. Las referencias son biblioteca de consulta, no una lista de imports obligatorios.

### Diseño de variables

Identifica estas entidades: **componente afectado, exposición declarada, función usada, dato faltante**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué cambio de evidencia alteraría la prioridad?
- Define hipótesis rivales, contratos, invariantes y criterios de evidencia suficiente. Justifica qué fuente analizarás y cuál dejarás fuera.
- Recupera razonamiento de [ejercicio 041](ejercicio_041.md), [ejercicio 054](ejercicio_054.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. P1 afectado, expuesto y utilizado → alta.
2. P6 afectado, interno y no utilizado → normal.
3. P7 uso desconocido → pendiente de contexto.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

La utilización declarada puede no cubrir todas las rutas del software. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un paquete vulnerable instalado puede no ser alcanzable por entradas no confiables. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- La utilización declarada puede no cubrir todas las rutas del software. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Funciones**; busca ese título en el índice.
- [CIS Controls: contexto de defensa de activos](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **La utilización declarada puede no cubrir todas las rutas del software.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En devsecops, este razonamiento ayuda a proteger **servicios que contienen componentes señalados** mediante priorización contextual de avisos de dependencias. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Incluir fecha de última verificación del contexto. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
