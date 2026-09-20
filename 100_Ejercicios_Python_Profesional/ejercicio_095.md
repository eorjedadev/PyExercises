# Ejercicio 095 — Duración efectiva de atención de incidencias

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_094.md) · [Siguiente](ejercicio_096.md)

### Contexto

Soporte mide trabajo activo sin contar pausas de espera de información.

### Situación

El encargo es **duración efectiva de atención de incidencias**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Minutos activos, pausados desde primera pausa hasta reanudación/cierre y tiempo total desde inicio hasta cierre**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Eventos ordenados con minuto entero no decreciente y acción iniciar, pausar, reanudar o cerrar; estado inicial pendiente.

### Resultado esperado

Minutos activos, pausados desde primera pausa hasta reanudación/cierre y tiempo total desde inicio hasta cierre.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Pendiente admite iniciar→activa.
- Activa admite pausar→pausada o cerrar→cerrada.
- Pausada admite reanudar→activa o cerrar→cerrada.
- Cerrada es final.
- Secuencia inválida rechaza cálculo completo.
- Última acción debe cerrar.

### Casos especiales y límites

Dos eventos al mismo instante pueden ser válidos y no añaden duración.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Unidades, exactitud y conservación de cantidades.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **instante de transición, estado vigente, minutos activos, minutos pausados**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué igualdad relaciona el tiempo activo, pausado y total?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 006](ejercicio_006.md), [ejercicio 050](ejercicio_050.md), [ejercicio 086](ejercicio_086.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Iniciar0,pausar10,reanudar20,cerrar25 →activos15,pausados10,total25.
2. Iniciar0,cerrar0 →todos0.
3. Cerrar sin iniciar →error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Contar como activo todo el intervalo entre inicio y cierre.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Iniciar0,pausar10,reanudar20,cerrar25 →activos15,pausados10,total25**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué igualdad relaciona el tiempo activo, pausado y total?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Medición de atención distingue tiempo activo y pausado según eventos de transición comprobables. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir un corte de consulta para incidencias aún no cerradas.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
