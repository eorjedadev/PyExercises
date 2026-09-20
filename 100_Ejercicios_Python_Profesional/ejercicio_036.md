# Ejercicio 036 — Agenda de reservas sin solapamientos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_035.md) · [Siguiente](ejercicio_037.md)

### Contexto

Un centro presta salas durante intervalos dentro de una jornada.

### Situación

El encargo es **agenda de reservas sin solapamientos**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Aceptación de la solicitud o reservas que chocan con ella**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Reservas existentes con sala e inicio/fin en minutos de 0 a 1440; una solicitud nueva.

### Resultado esperado

Aceptación de la solicitud o reservas que chocan con ella.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Inicio menor que fin.
- Intervalos incluyen inicio y excluyen fin.
- Solo compiten reservas de igual sala.
- Existentes válidas y sin conflictos.
- No modificar entradas.

### Casos especiales y límites

Un intervalo que contiene totalmente otro también se solapa.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Listas, tuplas, índices y recorridos**. Tema para investigar: Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.
- **Condicionales, booleanos y operadores de comparación**. Tema para investigar: Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.

### Variables y nombres

Identifica estas entidades: **sala solicitada, inicio incluido, fin excluido, reservas conflictivas**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo explicarías con un dibujo la diferencia entre tocarse y solaparse?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 006](ejercicio_006.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Sala A 60–120; solicitar A120–180 → aceptada.
2. Solicitar A119–130 → conflicto.
3. Solicitar B60–120 → aceptada.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Detectar solo extremos interiores y omitir intervalos que contienen a otros.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Sala A 60–120; solicitar A120–180 → aceptada**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo explicarías con un dibujo la diferencia entre tocarse y solaparse?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Agendas y recursos compartidos requieren contratos inequívocos sobre extremos de intervalos y conflictos. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Procesar varias solicitudes en orden y conservar las aceptadas.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
