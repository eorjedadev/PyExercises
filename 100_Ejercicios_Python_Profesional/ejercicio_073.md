# Ejercicio 073 — Asignación de envíos a vehículos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_072.md) · [Siguiente](ejercicio_074.md)

### Contexto

Una empresa quiere una política reproducible de carga sin prometer una optimización global.

### Situación

El encargo es **asignación de envíos a vehículos**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Asignaciones, capacidad final por vehículo y envíos no asignados**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Vehículos con id único y capacidad positiva en kg enteros; envíos ordenados con id único y peso positivo.

### Resultado esperado

Asignaciones, capacidad final por vehículo y envíos no asignados.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Para cada envío elegir vehículo con menor capacidad restante que aún permita cargarlo.
- Empate por id ascendente.
- No dividir envíos.
- No reconsiderar asignaciones anteriores.
- Registrar los que no caben.

### Casos especiales y límites

Una política válida no garantiza el mejor aprovechamiento posible para futuros envíos.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Comparación total, estabilidad y desempates reproducibles.
- Identidad de entidades y organización de datos relacionados.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Hacen reproducibles las prioridades y sus desempates.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **capacidad restante, peso del envío, vehículo seleccionado, envíos pendientes**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué compromisos impone mantener el orden de llegada?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 013](ejercicio_013.md), [ejercicio 031](ejercicio_031.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. V1:10,V2:6; envíos5,5 →primero V2, segundo V1.
2. Envío11 →no asignado.
3. Dos vehículos de6 →menor id para envío5.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Presentar esta política como solución óptima sin demostrarlo.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **V1:10,V2:6; envíos5,5 →primero V2, segundo V1**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué compromisos impone mantener el orden de llegada?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Asignación logística debe presentar políticas reproducibles sin prometer óptimos que no puede garantizar. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Comparar resultados al ordenar envíos por peso, dejando claro que es otra política.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
