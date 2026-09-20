# Ejercicio 089 — Vigencia de datos de varios proveedores

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_088.md) · [Siguiente](ejercicio_090.md)

### Contexto

Un reporte muestra la lectura más reciente disponible por sensor.

### Situación

El encargo es **vigencia de datos de varios proveedores**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Lectura elegida por sensor y sensores presentes sin datos vigentes**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lecturas con sensor, proveedor, instante UTC como entero y valor numérico finito; corte y antigüedad máxima no negativa.

### Resultado esperado

Lectura elegida por sensor y sensores presentes sin datos vigentes.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Excluir lecturas futuras y más antiguas que corte menos máximo.
- Límite antiguo incluido.
- Elegir mayor instante por sensor.
- Empate por proveedor ascendente.
- Mismos sensor/proveedor/instante repetidos invalidan entrada.

### Casos especiales y límites

No comparar tiempos como textos de formato variable.

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

Identifica estas entidades: **instante de observación, fecha de corte, edad máxima, lectura seleccionada**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo distinguirás ausencia de sensor de sensor con datos caducados?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 035](ejercicio_035.md), [ejercicio 067](ejercicio_067.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Corte100,máximo10; A en90 y95 →elige95.
2. A en89 →sin vigente.
3. A en100 →vigente.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar una lectura futura porque es la de mayor instante.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Corte100,máximo10; A en90 y95 →elige95**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo distinguirás ausencia de sensor de sensor con datos caducados?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Reportes multisistema deben seleccionar observaciones vigentes con reglas explícitas sobre antigüedad, futuro y desempate. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir prioridades de proveedor antes del desempate alfabético.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
