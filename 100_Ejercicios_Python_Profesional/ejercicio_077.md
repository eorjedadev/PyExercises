# Ejercicio 077 — Corrección de una fuga entre presupuestos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_076.md) · [Siguiente](ejercicio_078.md)

### Contexto

Una revisión detecta que cambios en una cotización podrían alterar otra por referencias compartidas.

### Situación

El encargo es **corrección de una fuga entre presupuestos**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Diagnóstico con líneas relevantes de tu código, corrección si procede y pruebas de independencia**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Tu implementación del ejercicio56 y un escenario con dos presupuestos construidos desde la misma lista de partidas.

### Resultado esperado

Diagnóstico con líneas relevantes de tu código, corrección si procede y pruebas de independencia.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Leer primero el recorrido de los datos.
- Si ya hay aislamiento, demostrarlo.
- Proteger ambos presupuestos frente a cambios externos y cambios en vistas devueltas.
- Documentar qué se copia o se hace inmutable.

### Casos especiales y límites

Copiar el contenedor externo no garantiza aislar elementos anidados.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Propiedad de los datos y modificaciones compartidas.
- Encapsulación de estado y protección de invariantes.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Explican por qué una modificación puede aparecer en otra parte del programa.
- Pueden reunir estado y operaciones cuando esa unión protege reglas del dominio.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **fuente compartida, copia propia, vista pública, presupuesto independiente**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿En qué frontera de tu código se adquiere la propiedad de los datos?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 056](ejercicio_056.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Dos presupuestos con partida2×150 →ambos300.
2. Modificar fuente a2×200 →ambos300.
3. Agregar partida solo al primero →segundo sigue300.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Añadir copias en todas partes sin identificar el origen del alias.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-6-referencias-mutabilidad-y-ciclo-de-vida-de-objetos).
- [Universidad_Python.md — Programación Orientada a Objetos](../Universidad_Python.md#programaci%C3%B3n-orientada-a-objetos).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Dos presupuestos con partida2×150 →ambos300**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿En qué frontera de tu código se adquiere la propiedad de los datos?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Revisiones de código rastrean referencias compartidas para corregir cambios que afectan objetos aparentemente independientes. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir revisiones compartiendo únicamente componentes demostrablemente inmutables.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
