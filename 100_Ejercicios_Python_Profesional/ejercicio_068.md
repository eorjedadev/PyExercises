# Ejercicio 068 — Normalización Unicode de nombres de catálogo

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_067.md) · [Siguiente](ejercicio_069.md)

### Contexto

Un buscador necesita reconocer distintas representaciones del mismo texto.

### Situación

El encargo es **normalización unicode de nombres de catálogo**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Identificadores y nombres originales coincidentes**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Catálogo de id único y nombre; consulta de texto.

### Resultado esperado

Identificadores y nombres originales coincidentes.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Para comparar usar normalización NFC, recorte externo y comparación sin distinción de mayúsculas.
- Conservar tildes y espacios interiores.
- Búsqueda por igualdad normalizada.
- Devolver todas las coincidencias por id ascendente.

### Casos especiales y límites

Normalización Unicode no significa eliminar acentos.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Equivalencia de texto y conservación de su representación visible.
- Identidad textual, normalización y formatos admitidos.
- Comparación total, estabilidad y desempates reproducibles.

### ¿Por qué pueden ser útiles?

- Distingue caracteres visibles de su composición interna y de sus bytes.
- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Hacen reproducibles las prioridades y sus desempates.

### Variables y nombres

Identifica estas entidades: **nombre original, clave comparable, consulta normalizada, coincidencias**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué representación debe mostrarse y cuál sirve para comparar?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 010](ejercicio_010.md), [ejercicio 016](ejercicio_016.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Nombre 'café' y consulta con e seguida de acento combinante →coinciden.
2. CAFE no coincide con café.
3. Dos nombres equivalentes con ids distintos →ambos.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Reescribir los nombres visibles y perder su forma original.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 4. Texto Unicode frente a bytes](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-4-texto-unicode-frente-a-bytes).
- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Nombre 'café' y consulta con e seguida de acento combinante →coinciden**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué representación debe mostrarse y cuál sirve para comparar?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Buscadores internacionales separan texto mostrado y equivalencia de comparación sin eliminar información lingüística. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Agregar búsqueda por prefijo usando la misma equivalencia documentada.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
