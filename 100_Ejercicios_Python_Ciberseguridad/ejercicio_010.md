# Ejercicio 010 — Conteo de decisiones de firewall

[Índice](README.md#indice) · [Anterior](ejercicio_009.md) · [Siguiente](ejercicio_011.md)

### Escenario de seguridad

El SOC recibe eventos permitidos y bloqueados de una frontera simulada.

### Contexto profesional

Ámbito: **Redes**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Visibilidad de controles de acceso de red. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **conteo de decisiones de firewall**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Resumen y trazabilidad a filas, incluidos registros descartados**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 010](ejercicio_010/README.md). Su README describe formatos, campos y procedencia sintética.

- [logs/firewall.csv](ejercicio_010/logs/firewall.csv) — Puertos destino y decisión declarada. No contiene paquetes ni obliga a transmitir tráfico.

### Requisitos

- Estados allow/deny.
- contar por acción y destino/puerto.
- puertos 1–65535.
- excluir filas inválidas con motivo.
- no convertir un bloqueo aislado en incidente.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Resumen y trazabilidad a filas, incluidos registros descartados. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Registros tabulares, conversión y trazabilidad**: Respetar delimitadores y campos citados sin perder la línea de origen.
- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.

### Conceptos de ciberseguridad relacionados

Una dirección, puerto o nombre no identifica intención ni persona. Compara contra alcance e inventario explícitos y conserva el contexto de la observación.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

- **csv y conversiones verificadas**. Investiga su contrato, las entradas que rechaza y qué información conserva.
- **dict, list, collections**. Investiga su contrato, las entradas que rechaza y qué información conserva.

### Diseño de variables

Identifica estas entidades: **acción del control, destino, puerto, registros aceptados**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué diferencia hay entre decisión registrada y tráfico efectivamente entregado?
- ¿Qué activo proteges, qué registros recibes y qué comportamiento considera normal este contrato?
- ¿Qué dato necesitas validar antes de contarlo o compararlo?
- ¿Qué ejemplo de frontera comprobarás a mano antes de programar?

### Casos de prueba

1. FW1 y FW2 deny al mismo destino443 → conteo2.
2. FW3 allow → conteo allow separado.
3. FW7 acción pass → inválido.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Ausencia de allow puede deberse a pérdida de registros. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un cliente mal configurado genera bloqueos repetidos sin ataque. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Ausencia de allow puede deberse a pérdida de registros. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Diccionario_Python.md](../Diccionario_Python.md) — **Imports Importantes por Área**; busca ese título en el índice.
- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [CIS Controls: contexto de inventario y defensa](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/csv.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Ausencia de allow puede deberse a pérdida de registros.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En redes, este razonamiento ayuda a proteger **visibilidad de controles de acceso de red** mediante conteo de decisiones de firewall. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Agregar porcentaje de deny indicando el denominador válido. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
