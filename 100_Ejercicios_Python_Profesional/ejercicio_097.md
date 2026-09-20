# Ejercicio 097 — Editor con deshacer y rehacer

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_096.md) · [Siguiente](ejercicio_098.md)

### Contexto

Una herramienta interna permite corregir una lista de etiquetas sin perder el historial reciente.

### Situación

El encargo es **editor con deshacer y rehacer**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Lista y disponibilidad de deshacer/rehacer después de cada comando**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista inicial y comandos agregar texto, quitar último, deshacer, rehacer; texto no vacío.

### Resultado esperado

Lista y disponibilidad de deshacer/rehacer después de cada comando.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Agregar/quitar exitosos crean cambios.
- Quitar en vacío se rechaza.
- Deshacer revierte último cambio vigente.
- Rehacer restaura último deshecho.
- Edición nueva tras deshacer elimina la posibilidad de rehacer.
- Comandos rechazados no cambian historial.

### Casos especiales y límites

Las versiones históricas no deben cambiar cuando se modifica la lista actual.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Propiedad de los datos y modificaciones compartidas.
- Invariantes y operaciones dependientes del estado vigente.
- Encapsulación de estado y protección de invariantes.

### ¿Por qué pueden ser útiles?

- Explican por qué una modificación puede aparecer en otra parte del programa.
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Pueden reunir estado y operaciones cuando esa unión protege reglas del dominio.

### Variables y nombres

Identifica estas entidades: **estado visible, cambio confirmado, historial deshecho, historial rehacible**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué significa crear una nueva rama de edición después de retroceder?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 053](ejercicio_053.md), [ejercicio 077](ejercicio_077.md), [ejercicio 087](ejercicio_087.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Agregar A,agregar B,deshacer →A; rehacer →A,B.
2. Deshacer y agregar C →rehacer no disponible.
3. Quitar en vacío →rechazo sin historial nuevo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Conservar un rehacer perteneciente a una rama que ya fue reemplazada.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-6-referencias-mutabilidad-y-ciclo-de-vida-de-objetos).
- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Programación Orientada a Objetos](../Universidad_Python.md#programaci%C3%B3n-orientada-a-objetos).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Agregar A,agregar B,deshacer →A; rehacer →A,B**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué significa crear una nueva rama de edición después de retroceder?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Editores internos manejan historial, reversión y nuevas ramas sin permitir cambios retroactivos en versiones guardadas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Limitar historial a los últimos diez cambios y documentar el efecto.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
