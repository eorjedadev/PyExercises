# Ejercicio 078 — Pruebas de propiedades de un reparto

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_077.md) · [Siguiente](ejercicio_079.md)

### Contexto

Un equipo quiere comprobar el reparto de céntimos más allá de tres ejemplos conocidos.

### Situación

El encargo es **pruebas de propiedades de un reparto**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Suite reproducible y explicación de qué defecto detectaría cada propiedad**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Tu solución del ejercicio7 y combinaciones de totales de 0 a200 y tamaños de grupo de1 a20.

### Resultado esperado

Suite reproducible y explicación de qué defecto detectaría cada propiedad.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Automatizar comprobaciones de conservación del total, no negatividad, diferencia máxima de1 y preferencia por primeras posiciones.
- Comprobar por separado grupo vacío.
- No copiar el algoritmo de producción para calcular el esperado.

### Casos especiales y límites

Una propiedad aislada puede ser satisfecha por una solución incorrecta.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Evidencia automatizada y detección de regresiones.
- Unidades, exactitud y conservación de cantidades.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **casos generados, propiedad comprobada, contraejemplo, diagnóstico**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué error podría pasar desapercibido si solo compruebas que la suma coincide?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 007](ejercicio_007.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Total1 y tres personas →1,0,0.
2. Total200 y20 personas →diez cada una.
3. Grupo vacío →rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Construir una segunda implementación idéntica como oráculo de pruebas.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Total1 y tres personas →1,0,0**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué error podría pasar desapercibido si solo compruebas que la suma coincide?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Pruebas de propiedades complementan ejemplos concretos con invariantes que cubren familias de entradas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Introducir temporalmente un defecto en tu copia de trabajo y demostrar qué prueba lo detecta.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
