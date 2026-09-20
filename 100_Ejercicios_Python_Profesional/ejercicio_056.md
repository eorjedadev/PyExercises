# Ejercicio 056 — Presupuesto compuesto por partidas

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_055.md) · [Siguiente](ejercicio_057.md)

### Contexto

Una oficina conserva una cotización aunque luego cambien las partidas originales.

### Situación

El encargo es **presupuesto compuesto por partidas**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Partidas del presupuesto, subtotales y total consistente**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Partidas con concepto, unidades positivas y precio entero no negativo en céntimos.

### Resultado esperado

Partidas del presupuesto, subtotales y total consistente.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Crear una representación de presupuesto que posea sus propias partidas.
- Total derivado del contenido.
- Agregar solo partidas válidas.
- Editar una lista externa después de crear el presupuesto no debe alterarlo.
- No exigir herencia.

### Casos especiales y límites

Exponer directamente una lista interna también puede romper el aislamiento.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Clases, instancias, composición e invariantes**. Tema para investigar: Compara atributos de instancia y de clase, vistas públicas y métodos; justifica si la clase protege algo o solo añade ceremonia.
- **Referencias, mutabilidad y propiedad de los datos**. Tema para investigar: Comprende alias, copias superficiales, elementos anidados e inmutabilidad antes de decidir qué compartir.
- **Enteros, operadores aritméticos y formato de resultados**. Tema para investigar: Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Pueden reunir estado y operaciones cuando esa unión protege reglas del dominio.
- Explican por qué una modificación puede aparecer en otra parte del programa.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.

### Variables y nombres

Identifica estas entidades: **partida original, partida incorporada, subtotal, presupuesto**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué información debe ser una copia y qué información puede compartirse?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 001](ejercicio_001.md), [ejercicio 053](ejercicio_053.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Dos unidades a150 →300.
2. Cambiar luego el precio del registro original a200 →presupuesto permanece300.
3. Unidades0 →rechazo sin cambio.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Guardar referencias mutables externas sin un contrato de propiedad.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Programación Orientada a Objetos](../Universidad_Python.md#programaci%C3%B3n-orientada-a-objetos).
- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-6-referencias-mutabilidad-y-ciclo-de-vida-de-objetos).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Dos unidades a150 →300**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué información debe ser una copia y qué información puede compartirse?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Cotizaciones y revisiones documentales necesitan propiedad clara de sus datos para conservar lo ya aprobado. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir crear una revisión del presupuesto conservando el anterior.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
