# Ejercicio 071 — Dependencias entre tareas de entrega

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_070.md) · [Siguiente](ejercicio_072.md)

### Contexto

Una coordinadora necesita un orden posible para tareas con prerrequisitos.

### Situación

El encargo es **dependencias entre tareas de entrega**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Orden completo o prefijo más diagnóstico de bloqueo**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Mapa de tarea a conjunto de tareas requeridas; identificadores no vacíos.

### Resultado esperado

Orden completo o prefijo más diagnóstico de bloqueo.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Una tarea se ejecuta una vez, después de todos sus requisitos.
- Elegir lexicográficamente la menor entre las disponibles en cada decisión.
- Dependencia inexistente invalida entrada.
- Si no se pueden completar todas, devolver prefijo ejecutable y tareas bloqueadas sin afirmar que todas forman un ciclo.

### Casos especiales y límites

Una tarea dependiente de un ciclo puede estar bloqueada sin pertenecer al ciclo.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Pertenencia, unicidad y equivalencia entre grupos.
- Identidad de entidades y organización de datos relacionados.
- Comparación total, estabilidad y desempates reproducibles.

### ¿Por qué pueden ser útiles?

- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Hacen reproducibles las prioridades y sus desempates.

### Variables y nombres

Identifica estas entidades: **requisitos por tarea, tareas completadas, tareas disponibles, bloqueos**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo distinguirías falta de datos de imposibilidad de completar un plan?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 033](ejercicio_033.md), [ejercicio 034](ejercicio_034.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A sin requisitos, B requiere A →A,B.
2. A requiere B y B requiere A →bloqueadas A,B.
3. A requiere X inexistente →error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Etiquetar como miembros del ciclo a todos los elementos bloqueados.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A sin requisitos, B requiere A →A,B**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo distinguirías falta de datos de imposibilidad de completar un plan?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Planificación de entregas necesita reconocer requisitos ausentes, ciclos y tareas bloqueadas indirectamente. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Separar tareas cíclicas de tareas que solo dependen de ellas.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
