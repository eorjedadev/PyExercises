# Ejercicio 033 — Resolución de alias de productos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_032.md) · [Siguiente](ejercicio_034.md)

### Contexto

Un catálogo histórico mantiene alias que pueden apuntar a otros alias.

### Situación

El encargo es **resolución de alias de productos**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Código final o diagnóstico con cadena recorrida**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Conjunto de códigos finales, mapa de alias a destino y código consultado.

### Resultado esperado

Código final o diagnóstico con cadena recorrida.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Códigos finales y alias disjuntos.
- Seguir referencias hasta código final.
- Informar destino inexistente o ciclo.
- No imponer un máximo arbitrario de saltos.
- No alterar el mapa.

### Casos especiales y límites

Una autorreferencia también es un ciclo.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Conjuntos, pertenencia y operaciones entre grupos**. Tema para investigar: Investiga qué información de orden o multiplicidad se pierde al representar datos como conjunto.
- **Bucles, acumuladores y control de flujo**. Tema para investigar: Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.

### Variables y nombres

Identifica estas entidades: **alias actual, destinos visitados, código final, cadena de referencias**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué evidencia distingue un recorrido largo de uno que nunca terminará?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 024](ejercicio_024.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Final Z; A→B, B→Z; consulta A → Z.
2. A→B, B→A → ciclo.
3. A→X sin X → destino inexistente.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Suponer que todos los alias apuntan directamente a un producto.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Final Z; A→B, B→Z; consulta A → Z**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué evidencia distingue un recorrido largo de uno que nunca terminará?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Resolución de alias y configuraciones enlazadas necesita detectar tanto destinos inexistentes como referencias circulares. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Resolver una lista de consultas y agrupar las que terminan en el mismo código.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
