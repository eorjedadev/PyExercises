# Ejercicio 041 — Cruce de dependencias con avisos ficticios

[Índice](README.md#indice) · [Anterior](ejercicio_040.md) · [Siguiente](ejercicio_042.md)

### Escenario de seguridad

Una lista de paquetes debe cruzarse con un feed pequeño sin consultar vulnerabilidades reales.

### Contexto profesional

Ámbito: **DevSecOps**. El trabajo consiste en convertir evidencia y una política explícita en resultados revisables por otra persona del equipo.

### Activo protegido

Componentes de una aplicación. Identifica qué propiedad de confidencialidad, integridad, disponibilidad o trazabilidad está en juego y por qué.

### Situación

El encargo es **cruce de dependencias con avisos ficticios**. Se han incluido observaciones normales, desviaciones de contrato o información insuficiente según el caso. No asumas que un nombre de archivo o id revela su clasificación.

### Objetivo

Construir y justificar una herramienta de Python que produzca: **Componentes potencialmente afectados y avisos coincidentes, no prueba de explotabilidad**. La conclusión de seguridad debe respetar el alcance de las fuentes.

### Evidencias disponibles

Todos los recursos se entregan en [el paquete 041](ejercicio_041/README.md). Su README describe formatos, campos y procedencia sintética.

- [datos/dependencias.json](ejercicio_041/datos/dependencias.json) — Nombres y versiones ficticios; no representan avisos de paquetes reales.
- [datos/avisos.json](ejercicio_041/datos/avisos.json) — Feed ficticio cerrado; no son CVE ni reglas de versión universales.

### Requisitos

- Identidad ecosistema/nombre exacta.
- versiones de 3 enteros no negativos.
- aviso aplica en intervalo mínimo incluido, máximo excluido.
- no usar rangos semver generales.
- estado desconocido si formato no admitido.
- avisos identificados LAB-ADV, no CVE reales.
- formato de versión: tres grupos de dígitos ASCII separados por puntos, sin signos ni sufijos.
- se permiten ceros iniciales.

Conserva evidencia original y aplica las [convenciones de entrada, errores y resultados](README.md#contratos-comunes). Elige tu interfaz de salida y documenta su esquema; no requiere menús ni servicios salvo indicación explícita.

### Resultado esperado

Componentes potencialmente afectados y avisos coincidentes, no prueba de explotabilidad. Incluye referencia de origen, datos rechazados o no evaluables y la versión de las reglas empleadas. Ordena por id cuando no exista otro orden exigido; el texto de los mensajes es libre.

### Fundamentos de Python relacionados

- **Identidad, agregación y relaciones entre registros**: Distinguir conteos, entidades únicas y vínculos respaldados por claves.
- **Cadenas, comparación y validación**: Conservar la entrada original y definir exactamente qué se normaliza.

### Conceptos de ciberseguridad relacionados

La configuración declarada, su contexto de despliegue y su estado efectivo deben distinguirse. La revisión automatizada cubre un contrato específico.

En este ejercicio debes separar **dato → evento → observación → indicador → hipótesis → evidencia → conclusión**. Un dato respalda una observación; su procedencia y calidad determinan qué puede usarse como evidencia. No es una escalera automática hacia la certeza.

### Herramientas o módulos que investigar

Estas son alternativas de estudio, no una arquitectura obligatoria:

- dict, list, collections; justifica su necesidad y el límite de su garantía.
- str, métodos de cadenas; justifica su necesidad y el límite de su garantía.

### Diseño de variables

Identifica estas entidades: **identidad de componente, versión instalada, intervalo del aviso, alcance**. Propón nombres de variables, colecciones, contadores, funciones, parámetros, constantes y resultados intermedios que realmente necesites. No inventes entidades para completar una lista.

Expresa unidad, alcance y estado cuando eviten ambigüedad. Distingue observado, esperado, candidato y confirmado. Evita nombres como data1, lista1, temp o valor; explica un nombre que descartaste.

### Antes de programar

- ¿Qué falta antes de afirmar que el servicio es explotable?
- ¿Qué relaciones e intervalos exige el contrato y qué coincidencias podrían ser accidentales?
- ¿Qué responsabilidad puedes probar sin archivos, reloj real ni interfaz de usuario?
- Recupera razonamiento de [ejercicio 011](ejercicio_011.md), [ejercicio 019](ejercicio_019.md). Explica una similitud y una diferencia antes de reutilizar código.

### Casos de prueba

1. libalpha1.2.0 en[1.0.0,1.3.0) → afectado.
2. 1.3.0 → fuera.
3. 1.2.0-beta → no evaluable.

Son escenarios de aceptación, no una solución ni una clasificación completa del dataset. Cuando un caso requiera alterar un dato, crea una copia de prueba. Añade un caso normal, uno de frontera y uno que contradiga tu hipótesis; registra la expectativa antes de ejecutar.

### Casos límite

Inventario puede omitir dependencias transitivas. Comprueba también ausencia de datos y fronteras de tamaño, tiempo o identidad que afecten a las reglas. No confundas un resultado vacío con un análisis completo.

### Falsos positivos

Un paquete afectado puede no usar la función vulnerable. Explica qué información aumentaría o reduciría tu confianza. En ejercicios de validación, distingue una entrada legítima rechazada por política de una detección errónea de actividad maliciosa.

### Errores comunes

- Inventario puede omitir dependencias transitivas. Ignorar esta limitación permite conclusiones que la evidencia no respalda.
- Tratar un dato desconocido como falso, cero o benigno.
- Ocultar rechazos, perder procedencia o incluir datos sensibles innecesarios en el reporte.

### Consulta recomendada

- [Universidad_Python.md](../Universidad_Python.md) — **Diccionarios**; busca ese título en el índice.
- [Diccionario_Python.md](../Diccionario_Python.md) — **Métodos de Cadenas**; busca ese título en el índice.
- [CIS Controls: contexto de defensa de activos](https://www.cisecurity.org/controls/v8) — contexto; no reemplaza las reglas del laboratorio.
- [Documentación oficial de la herramienta](https://docs.python.org/3/library/collections.html) — consulta el contrato y las excepciones, no copies una solución.

### Explicación posterior

- Explica el problema, los datos recibidos y su recorrido hasta el resultado; muestra una referencia concreta a la evidencia.
- ¿Por qué elegiste esas representaciones, funciones y nombres? ¿Qué validaciones y errores controla tu implementación?
- Lee un fragmento de tu propio código sin ejecutarlo y predice un caso límite; contrasta después la predicción.
- ¿Qué parte es reutilizable, qué limitaciones conserva y cómo modificarías la política sin perder trazabilidad?
- ¿Qué falso positivo no puede resolver tu programa por sí solo?

### Interpretación de resultados

Presenta una conclusión técnica breve con **Hallazgo, Evidencia, Interpretación, Nivel de confianza, Información faltante y Recomendación**. Cada afirmación factual debe citar archivo e id o línea. La confianza se justifica por afirmación, no con una puntuación arbitraria.

Contrasta tu resultado con esta limitación: **Inventario puede omitir dependencias transitivas.** Indica qué puedes afirmar, qué sigue siendo hipótesis y qué comprobación defensiva tendría sentido después. Si la evidencia no alcanza, «no determinado» es un resultado válido.

### Aplicación profesional

En devsecops, este razonamiento ayuda a proteger **componentes de una aplicación** mediante cruce de dependencias con avisos ficticios. Describe qué adaptación exigiría una fuente real y qué garantía no puedes trasladar desde el dataset sintético.

### Reto adicional

Añadir estado de uso de una función afectada desde evidencia separada. Es opcional: escribe qué contrato cambia, qué pruebas deben seguir pasando y qué nuevas hipótesis aparecen.
