# Ejercicio 075 — Reglas de clasificación configurables

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_074.md) · [Siguiente](ejercicio_076.md)

### Contexto

Una herramienta clasifica registros usando reglas que cambian sin reescribir el flujo general.

### Situación

El encargo es **reglas de clasificación configurables**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Etiqueta por registro y regla aplicada o marca de predeterminada**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Registros de id único, categoría y cantidad; lista ordenada de reglas con campo, operador, valor y etiqueta; etiqueta predeterminada.

### Resultado esperado

Etiqueta por registro y regla aplicada o marca de predeterminada.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Campos categoría/cantidad.
- Operadores igual para ambos y mayor_o_igual solo para cantidad.
- Primera regla que coincide gana.
- Configuración inválida aborta antes de procesar.
- No ejecutar texto como código.

### Casos especiales y límites

El orden de reglas forma parte del contrato público.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Organización del programa y dependencias sustituibles.
- Contratos, parámetros explícitos y responsabilidades comprobables.
- Identidad de entidades y organización de datos relacionados.

### ¿Por qué pueden ser útiles?

- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Relacionan identidades con atributos, estados o acumulados consultables.

### Variables y nombres

Identifica estas entidades: **regla declarada, operador admitido, condición evaluada, etiqueta final**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué variabilidad conviene expresar como datos y cuál requiere código nuevo?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 011](ejercicio_011.md), [ejercicio 047](ejercicio_047.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Regla cantidad>=10 etiqueta grande; cantidad10 →grande.
2. Ninguna coincide →predeterminada.
3. Operador desconocido →configuración rechazada.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar evaluación arbitraria de expresiones para un lenguaje acotado.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Regla cantidad>=10 etiqueta grande; cantidad10 →grande**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué variabilidad conviene expresar como datos y cuál requiere código nuevo?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Clasificadores configurables separan políticas declaradas, validación de configuración y evaluación de registros. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir una regla compuesta por todas las condiciones de una lista.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
