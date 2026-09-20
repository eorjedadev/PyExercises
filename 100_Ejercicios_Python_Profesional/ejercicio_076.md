# Ejercicio 076 — Refactorización de un reporte sin cambios visibles

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_075.md) · [Siguiente](ejercicio_077.md)

### Contexto

Tu solución del ejercicio 37 ya se utiliza y necesita separar cálculo y presentación.

### Situación

El encargo es **refactorización de un reporte sin cambios visibles**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Implementación reorganizada, contrato escrito y evidencia comparativa anterior/posterior**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Implementación propia del ejercicio37, sus pruebas y una muestra con varios proyectos y siete días.

### Resultado esperado

Implementación reorganizada, contrato escrito y evidencia comparativa anterior/posterior.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Conservar entradas admitidas, rechazos, orden y resultados.
- Separar el cálculo de la salida visible.
- Mantener el punto de entrada anterior como adaptación.
- No incorporar nuevas reglas de negocio.

### Casos especiales y límites

Un formato externo que ya se documentó también es comportamiento observable.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Organización del programa y dependencias sustituibles.
- Evidencia automatizada y detección de regresiones.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **entrada pública, resultado de cálculo, presentación, contrato conservado**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué acoplamiento concreto eliminarás y cómo demostrarás equivalencia?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 037](ejercicio_037.md), [ejercicio 051](ejercicio_051.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A día1 30 y A día1 15 →45 antes y después.
2. Día8 →mismo rechazo.
3. Sin registros →mismo reporte vacío.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Aprovechar la refactorización para cambiar reglas sin reconocerlo.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A día1 30 y A día1 15 →45 antes y después**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué acoplamiento concreto eliminarás y cómo demostrarás equivalencia?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Mantenimiento de reportes requiere reorganizar responsabilidades sin cambiar el comportamiento de consumidores existentes. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un segundo formato de salida usando el mismo cálculo.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
