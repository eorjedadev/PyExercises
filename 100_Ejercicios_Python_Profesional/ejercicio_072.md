# Ejercicio 072 — Planificador de ejecución por rondas

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_071.md) · [Siguiente](ejercicio_073.md)

### Contexto

Un equipo simula cómo ejecutar tareas dependientes con varios puestos disponibles.

### Situación

El encargo es **planificador de ejecución por rondas**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Tareas por ronda y número de rondas; entrada inválida se rechaza**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Tareas de duración exacta una ronda, dependencias válidas sin ciclos y capacidad positiva de puestos.

### Resultado esperado

Tareas por ronda y número de rondas; entrada inválida se rechaza.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Cada ronda inicia hasta capacidad de tareas disponibles, por id ascendente.
- Solo cuentan dependencias terminadas en rondas anteriores.
- No rellenar un puesto con una tarea liberada dentro de la misma ronda.

### Casos especiales y límites

Elegibilidad al inicio de ronda es distinta de elegibilidad durante una iteración interna.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Identidad de entidades y organización de datos relacionados.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **capacidad de ejecución, tareas disponibles al inicio, ronda, finalizadas**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué define la frontera entre una ronda y la siguiente?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 029](ejercicio_029.md), [ejercicio 071](ejercicio_071.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A,B libres; C depende A; capacidad2 →ronda1 A,B, ronda2 C.
2. Capacidad1 →A,B,C según disponibilidad y orden.
3. Sin tareas →0 rondas.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Permitir que una tarea y su requisito se ejecuten simultáneamente.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A,B libres; C depende A; capacidad2 →ronda1 A,B, ronda2 C**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué define la frontera entre una ronda y la siguiente?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Simuladores de ejecución por lotes distinguen disponibilidad al inicio de una ronda y tareas liberadas después. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir duraciones de varias rondas conservando dependencias.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
