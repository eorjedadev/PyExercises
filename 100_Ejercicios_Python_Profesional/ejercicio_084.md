# Ejercicio 084 — Consistencia de un índice de búsqueda

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_083.md) · [Siguiente](ejercicio_085.md)

### Contexto

Una aplicación mantiene un catálogo y una vista por categorías para acelerar consultas.

### Situación

El encargo es **consistencia de un índice de búsqueda**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Resultado de operaciones e informe de discrepancias y reparación**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Catálogo id→registro con categoría y nombre; índice categoría→ids; operaciones agregar, mover y eliminar.

### Resultado esperado

Resultado de operaciones e informe de discrepancias y reparación.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- El catálogo es autoridad.
- Índice debe contener cada id exactamente en su categoría.
- Categorías vacías se retiran.
- Operación inválida no cambia ninguna estructura.
- Incluir revisión que detecte y repare índice corrupto desde catálogo.
- Solo se aplican cambios cuando el índice inicial es coherente.
- Revisar y reparar están disponibles aunque esté corrupto.

### Casos especiales y límites

Una estructura derivada no debe convertirse en una segunda autoridad contradictoria.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Identidad de entidades y organización de datos relacionados.
- Invariantes y operaciones dependientes del estado vigente.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **catálogo autoritativo, índice derivado, pertenencia esperada, discrepancia**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué invariante conecta las dos representaciones del mismo dato?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 017](ejercicio_017.md), [ejercicio 024](ejercicio_024.md), [ejercicio 030](ejercicio_030.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Agregar A en libros →índice libros:A.
2. Mover A a juegos →sin libros, juegos:A.
3. Índice contiene X inexistente →revisión lo detecta y elimina al reparar.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Actualizar catálogo y olvidar retirar una referencia antigua del índice.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Agregar A en libros →índice libros:A**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué invariante conecta las dos representaciones del mismo dato?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Índices y vistas derivadas requieren una fuente de autoridad y mecanismos de detección y reparación de inconsistencias. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Reconstruir el índice en una nueva estructura y comparar antes de sustituir.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
