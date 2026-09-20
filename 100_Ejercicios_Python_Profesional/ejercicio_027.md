# Ejercicio 027 — Detección de rachas de retrasos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_026.md) · [Siguiente](ejercicio_028.md)

### Contexto

Una coordinadora busca secuencias de entregas tardías de un mismo equipo.

### Situación

El encargo es **detección de rachas de retrasos**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Longitud y límites de la racha; sin retrasos, longitud 0 y límites ausentes**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista cronológica de días de retraso enteros no negativos.

### Resultado esperado

Longitud y límites de la racha; sin retrasos, longitud 0 y límites ausentes.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Valor 0 interrumpe la racha.
- Valor positivo cuenta como una entrega tardía.
- Devolver racha más larga y posiciones inicial y final desde 1.
- En empate elegir primera.

### Casos especiales y límites

La mejor racha puede terminar en el último registro.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Bucles, acumuladores y control de flujo**. Tema para investigar: Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.
- **Listas, tuplas, índices y recorridos**. Tema para investigar: Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.
- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **racha actual, mejor racha, inicio de racha, posición de entrega**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué distingue la duración del retraso de la longitud de una racha?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 009](ejercicio_009.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. 0,2,1,0,3 → longitud 2, posiciones 2 a 3.
2. 1,1,0,2,2 → primera racha.
3. 0,0 o vacío → longitud 0.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Sumar días de retraso cuando se cuentan entregas consecutivas.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).
- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **0,2,1,0,3 → longitud 2, posiciones 2 a 3**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué distingue la duración del retraso de la longitud de una racha?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Seguimiento de calidad identifica recurrencias consecutivas sin confundirlas con la magnitud de cada incidente. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Informar todas las rachas que superen un umbral.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
