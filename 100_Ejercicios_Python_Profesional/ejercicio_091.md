# Ejercicio 091 — Evolución compatible de un resultado público

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_090.md) · [Siguiente](ejercicio_092.md)

### Contexto

Otros programas consumen tu clasificador de tareas y necesitan una nueva salida sin romper la anterior.

### Situación

El encargo es **evolución compatible de un resultado público**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Dos interfaces documentadas y pruebas de compatibilidad**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Solución del ejercicio25; cliente v1 espera solo tareas ordenadas; cliente v2 pide también duración total por prioridad.

### Resultado esperado

Dos interfaces documentadas y pruebas de compatibilidad.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Mantener contrato v1.
- V2 devuelve tareas y totales de alta/normal/baja, incluidos ceros.
- Ambos comparten reglas de orden.
- Versión desconocida se rechaza.
- No duplicar políticas de clasificación.

### Casos especiales y límites

Un campo añadido puede romper a un consumidor que esperaba una lista.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Organización del programa y dependencias sustituibles.
- Contratos, parámetros explícitos y responsabilidades comprobables.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **versión de contrato, resultado histórico, resumen nuevo, adaptación**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Dónde debe existir la decisión de versión sin contaminar las reglas comunes?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 025](ejercicio_025.md), [ejercicio 076](ejercicio_076.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A alta5,B normal3 →v1 A,B; v2 mismos y totales5,3,0.
2. Vacío →v1 vacío, v2 totales0.
3. v3 →error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Cambiar el tipo de retorno original sin avisar a sus consumidores.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A alta5,B normal3 →v1 A,B; v2 mismos y totales5,3,0**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Dónde debe existir la decisión de versión sin contaminar las reglas comunes?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Evolución de interfaces exige conservar contratos históricos mientras se incorporan nuevas representaciones. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Marcar v1 como obsoleta en documentación sin eliminar su funcionamiento.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
