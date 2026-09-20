# Ejercicio 034 — Selección de candidaturas por requisitos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_033.md) · [Siguiente](ejercicio_035.md)

### Contexto

Un programa de formación filtra candidaturas con criterios publicados.

### Situación

El encargo es **selección de candidaturas por requisitos**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Aptas con puntaje y rechazadas con competencias obligatorias faltantes**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Candidatos con identificador único y conjunto de competencias; conjunto de competencias obligatorias y deseables.

### Resultado esperado

Aptas con puntaje y rechazadas con competencias obligatorias faltantes.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Una candidatura es apta si contiene todas las obligatorias.
- Puntaje igual al número de deseables presentes.
- Competencias exactas.
- Ordenar aptas por puntaje descendente e identificador ascendente.

### Casos especiales y límites

Una competencia puede aparecer en ambas categorías y cuenta como deseable una vez.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Conjuntos, pertenencia y operaciones entre grupos**. Tema para investigar: Investiga qué información de orden o multiplicidad se pierde al representar datos como conjunto.
- **Ordenación, claves de comparación y estabilidad**. Tema para investigar: Investiga orden total, criterios compuestos y diferencia entre ordenar una copia y modificar la colección original.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.
- Hacen reproducibles las prioridades y sus desempates.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **competencias obligatorias, competencias acreditadas, faltantes, puntaje**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué diferencia hay entre requisito excluyente y criterio de ordenación?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 018](ejercicio_018.md), [ejercicio 025](ejercicio_025.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Obligatoria Python, deseable SQL; A con ambas → apta 1.
2. B solo SQL → rechazada, falta Python.
3. Sin obligatorias → todas aptas.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar el puntaje para compensar un requisito obligatorio ausente.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).
- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Obligatoria Python, deseable SQL; A con ambas → apta 1**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia hay entre requisito excluyente y criterio de ordenación?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Procesos de selección distinguen requisitos excluyentes de criterios que solo mejoran la posición relativa. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir grupos de requisitos donde baste una competencia de cada grupo.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
