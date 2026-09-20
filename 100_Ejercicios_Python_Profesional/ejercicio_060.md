# Ejercicio 060 — Evaluación de calidad de un conjunto de datos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_059.md) · [Siguiente](ejercicio_061.md)

### Contexto

Una analista necesita un diagnóstico antes de utilizar un archivo de personas.

### Situación

El encargo es **evaluación de calidad de un conjunto de datos**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Total de filas, válidas y errores por categoría y fila**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

CSV con cabecera id,edad,ciudad; edad como entero de 0 a120; id y ciudad recortados no vacíos.

### Resultado esperado

Total de filas, válidas y errores por categoría y fila.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Reportar todas las infracciones por fila.
- Marcar id duplicado en cada aparición posterior, aunque la anterior tenga otros errores.
- No corregir datos.
- Filas sin infracciones cuentan válidas.
- Id vacío no se incorpora al registro de identidades vistas.

### Casos especiales y límites

Una fila puede aportar más de un error al informe.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Intercambio tabular y módulo csv**. Tema para investigar: Ubica csv en el diccionario y explora reader, writer y DictReader con la ayuda local del módulo; diferencia registro CSV y línea física.
- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Preserva campos que pueden incluir delimitadores o comillas sin confundirlos con columnas adicionales.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **fila examinada, identidad vista, infracciones, filas válidas**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Por qué la suma de errores puede superar el número de filas rechazadas?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 012](ejercicio_012.md), [ejercicio 042](ejercicio_042.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A,20,Lima y A,200,'' →segunda con duplicado, edad y ciudad.
2. Fila sin id →error id.
3. Archivo solo cabecera →cero filas.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Interrumpir la revisión de una fila tras su primer error.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Imports Importantes por Área](../Diccionario_Python.md#imports-importantes-por-%C3%A1rea).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A,20,Lima y A,200,'' →segunda con duplicado, edad y ciudad**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Por qué la suma de errores puede superar el número de filas rechazadas?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Control de calidad de datos hace visibles varias infracciones por registro antes de autorizar su utilización. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir umbrales de aceptación del archivo basados en porcentaje de filas válidas.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
