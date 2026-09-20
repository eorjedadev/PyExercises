# Ejercicio 029 — Asignación circular de responsables

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_028.md) · [Siguiente](ejercicio_030.md)

### Contexto

Un equipo reparte tickets nuevos de manera continua entre sus integrantes.

### Situación

El encargo es **asignación circular de responsables**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Asignación de cada ticket y siguiente posición**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista ordenada de integrantes únicos, lista de tickets únicos y posición inicial desde 0.

### Resultado esperado

Asignación de cada ticket y siguiente posición.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Con tickets debe existir al menos un integrante.
- Posición válida dentro de integrantes.
- Asignar por turnos circulares.
- Devolver también posición para el siguiente lote.
- Sin integrantes y sin tickets, posición ausente.

### Casos especiales y límites

Un lote nuevo no debe reiniciar por accidente el turno.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Listas, tuplas, índices y recorridos**. Tema para investigar: Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.
- **Enteros, operadores aritméticos y formato de resultados**. Tema para investigar: Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **integrantes disponibles, tickets pendientes, posición inicial, siguiente turno**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué dato permite continuar el reparto entre llamadas?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 014](ejercicio_014.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Ana,Beto; T1,T2,T3; inicio 0 → Ana,Beto,Ana; siguiente 1.
2. Mismos integrantes sin tickets e inicio 1 → siguiente 1.
3. Tickets sin integrantes → error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Asignar siempre el primer ticket a la primera persona.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Ana,Beto; T1,T2,T3; inicio 0 → Ana,Beto,Ana; siguiente 1**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué dato permite continuar el reparto entre llamadas?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Distribución de trabajo entre equipos necesita continuidad entre lotes para no favorecer siempre al mismo integrante. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Excluir temporalmente integrantes ausentes antes del reparto.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
