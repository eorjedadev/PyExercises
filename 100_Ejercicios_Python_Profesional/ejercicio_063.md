# Ejercicio 063 — Límite de solicitudes por ventana temporal

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_062.md) · [Siguiente](ejercicio_064.md)

### Contexto

Un servicio simulado decide si acepta llamadas de cada cliente.

### Situación

El encargo es **límite de solicitudes por ventana temporal**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Decisión por evento y número de aceptadas vigentes tras cada decisión**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Eventos ordenados por segundo no decreciente con cliente; límite L positivo y ventana W positiva.

### Resultado esperado

Decisión por evento y número de aceptadas vigentes tras cada decisión.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- En tiempo t cuentan aceptadas del mismo cliente en intervalo (t-W,t].
- Rechazar si aceptar superaría L.
- Rechazadas no consumen cupo.
- Eventos del mismo segundo se procesan en orden de entrada.

### Casos especiales y límites

El evento exactamente en t-W ya no cuenta.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Identidad de entidades y organización de datos relacionados.
- Orden, posiciones y conservación de relaciones.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.

### Variables y nombres

Identifica estas entidades: **cliente, instante recibido, aceptadas vigentes, cupo disponible**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Por qué importa la definición de los extremos de la ventana?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 035](ejercicio_035.md), [ejercicio 061](ejercicio_061.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. L2,W10; A en0,5,9,10 →acepta,acepta,rechaza,acepta.
2. B en9 no comparte cupo con A.
3. L1; A0,A0 →acepta,rechaza.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Incluir rechazos en el consumo o mantener eventos ya vencidos.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **L2,W10; A en0,5,9,10 →acepta,acepta,rechaza,acepta**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Por qué importa la definición de los extremos de la ventana?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Simulación de cuotas por cliente exige una definición precisa de qué operaciones consumen capacidad temporal. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir un límite distinto por cliente.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
