# Ejercicio 010 — Depuración de etiquetas de catálogo

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_009.md) · [Siguiente](ejercicio_011.md)

### Contexto

Un catálogo recibe etiquetas escritas con espacios y mayúsculas inconsistentes.

### Situación

El encargo es **depuración de etiquetas de catálogo**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Lista depurada y cantidades de vacías y duplicadas descartadas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de textos; cada texto es una etiqueta completa.

### Resultado esperado

Lista depurada y cantidades de vacías y duplicadas descartadas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Recortar extremos y pasar a minúsculas.
- Descartar vacías.
- Conservar una sola aparición por etiqueta normalizada.
- Respetar el orden de primera aparición.

### Casos especiales y límites

Los espacios interiores forman parte de la etiqueta.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Cadenas, métodos de texto y comparaciones**. Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Listas, tuplas, índices y recorridos**. Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.
- **Conjuntos, pertenencia y operaciones entre grupos**. Investiga qué información de orden o multiplicidad se pierde al representar datos como conjunto.

### ¿Por qué pueden ser útiles?

- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.

### Variables y nombres

Identifica estas entidades: **etiqueta original, etiqueta normalizada, descartes, etiquetas publicables**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué significa que dos etiquetas sean iguales en este contrato?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. Python, ' python ', '', Datos → python, datos; 1 vacía y 1 duplicada.
2. 'a b' y 'a  b' → distintas.
3. Lista vacía → lista vacía.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar una colección sin orden como si garantizara el orden exigido.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Python, ' python ', '', Datos → python, datos; 1 vacía y 1 duplicada**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué significa que dos etiquetas sean iguales en este contrato?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Catálogos y buscadores necesitan una definición explícita de equivalencia que no destruya el orden requerido. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Unificar también secuencias de espacios interiores.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
