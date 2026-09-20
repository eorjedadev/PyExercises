# Ejercicio 025 — Clasificación estable de tareas

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_024.md) · [Siguiente](ejercicio_026.md)

### Contexto

Una supervisora necesita una cola de tareas con prioridades y desempates predecibles.

### Situación

El encargo es **clasificación estable de tareas**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Lista ordenada y duración total**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de tareas con identificador único, prioridad alta/normal/baja y minutos estimados positivos.

### Resultado esperado

Lista ordenada y duración total.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Ordenar alta antes que normal antes que baja.
- A igual prioridad, menor duración primero.
- A igual duración conservar orden de entrada.
- Rechazar todo si un registro es inválido.

### Casos especiales y límites

Los identificadores no determinan el desempate final.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Ordenación, claves de comparación y estabilidad**. Investiga orden total, criterios compuestos y diferencia entre ordenar una copia y modificar la colección original.
- **Diccionarios, registros y colecciones anidadas**. Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

### ¿Por qué pueden ser útiles?

- Hacen reproducibles las prioridades y sus desempates.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **prioridad declarada, duración estimada, posición original, cola ordenada**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué significa que el orden sea estable en este caso?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

Recupera razonamiento de [ejercicio 011](ejercicio_011.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A normal 10, B alta 20, C alta 5 → C,B,A.
2. A alta 5, B alta 5 → A,B.
3. Lista vacía → vacía y duración 0.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Depender del orden alfabético de los nombres de prioridad.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A normal 10, B alta 20, C alta 5 → C,B,A**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué significa que el orden sea estable en este caso?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Colas operativas necesitan prioridades y desempates previsibles para explicar el orden de trabajo. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir fecha de entrega como criterio entre prioridad y duración.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
