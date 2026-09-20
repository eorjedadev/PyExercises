# Ejercicio 005 — Higiene de permisos declarados

[Índice](README.md#indice) · [Anterior](ejercicio_004.md) · [Siguiente](ejercicio_006.md)

### Escenario de seguridad

Administración exportó modos de permisos POSIX para una revisión sin tocar el equipo.

### Contexto profesional

Ámbito: **Sistemas**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Archivos de configuración Linux. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **higiene de permisos declarados**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Incumplimientos de política y registros imposibles**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 005](ejercicio_005/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/permisos.csv](ejercicio_005/datos/permisos.csv) — Exportación sintética POSIX; no consultar esas rutas en el equipo.

### Requisitos

- Modo exactamente tres dígitos octales.
- revisar escritura de otros en cualquier archivo y lectura de otros en clase secreto.
- es análisis del modo declarado, no ACL efectiva.
- no ejecutar chmod.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Incumplimientos de política y registros imposibles. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Cadenas, comparación y validación**: Conservar la entrada original y definir exactamente qué se normaliza.
- **Condiciones, tipos y precedencia de políticas**: Evitar que un valor ausente o una regla general oculten otra decisión.

### Conceptos de ciberseguridad relacionados

Un ajuste exportado no equivale siempre al control efectivo. Distingue modelo del ejercicio, semántica de plataforma y ejecución realmente observada.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **str, métodos de cadenas**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **if, operadores booleanos, funciones**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **modo declarado, clasificación del archivo, permiso observado, limitación**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué falta para deducir permisos efectivos?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?

### Casos de prueba

1. P02 secreto644 → lectura de otros.
2. P03 publico666 → escritura de otros.
3. P01 secreto600 → sin regla activada.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

ACL, propietario y directorios padre pueden cambiar el acceso real. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un archivo de ejemplo marcado secreto por error causa alerta de clasificación. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- ACL, propietario y directorios padre pueden cambiar el acceso real. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Métodos de Cadenas**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Condicionales**; busca ese título en el índice.
- [CIS Controls: contexto de configuración y auditoría](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/re.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **ACL, propietario y directorios padre pueden cambiar el acceso real.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En sistemas, este razonamiento ayuda a proteger **archivos de configuración linux** mediante higiene de permisos declarados. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Incorporar permisos de directorios padre como otra fuente. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
