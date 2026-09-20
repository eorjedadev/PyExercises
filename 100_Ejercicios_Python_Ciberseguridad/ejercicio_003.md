# Ejercicio 003 — Validación de direcciones de origen

[Índice](README.md#indice) · [Anterior](ejercicio_002.md) · [Siguiente](ejercicio_004.md)

### Escenario de seguridad

Un sensor exporta direcciones mezcladas con valores malformados.

### Contexto profesional

Ámbito: **Redes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Calidad de los registros de red. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **validación de direcciones de origen**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Direcciones válidas con versión y red coincidente, más rechazos**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 003](ejercicio_003/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/origenes.json](ejercicio_003/datos/origenes.json) — Direcciones textuales, no destinos que deban contactarse.
- [config/redes.json](ejercicio_003/config/redes.json) — Redes inventariadas explícitas; direcciones de documentación.

### Requisitos

- Solo texto IPv4 o IPv6 sin puerto ni zona porcentual.
- producir representación canónica.
- clasificar pertenencia exclusivamente a CIDR suministrados.
- no consultar Internet ni usar is_private como sinónimo de red corporativa.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Direcciones válidas con versión y red coincidente, más rechazos. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Representación y comparación de direcciones y redes**: Distinguir validez, versión y pertenencia a una red explícita.
- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.

### Conceptos de ciberseguridad relacionados

Una dirección, puerto o nombre no identifica intención ni persona. Compara contra alcance e inventario explícitos y conserva el contexto de la observación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **ipaddress**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **dict, list, collections**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **origen textual, dirección canónica, versión IP, red inventariada**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué diferencia hay entre dirección válida y origen autorizado?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?

### Casos de prueba

1. 192.0.2.10 → red lab-v4.
2. 2001:db8::10 → lab-v6.
3. 999.1.1.1 y 192.0.2.1:443 → inválidas.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Dos escrituras IPv6 pueden representar una sola dirección. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Una IP fuera del inventario puede ser un equipo legítimo aún no registrado. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Dos escrituras IPv6 pueden representar una sola dirección. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports para Ciberseguridad y Hacking Ético**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [CIS Controls: contexto de inventario y defensa](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/ipaddress.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Dos escrituras IPv6 pueden representar una sola dirección.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En redes, este razonamiento ayuda a proteger **calidad de los registros de red** mediante validación de direcciones de origen. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Contar direcciones únicas tras normalizar. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
