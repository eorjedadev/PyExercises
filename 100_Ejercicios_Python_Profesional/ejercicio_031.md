# Ejercicio 031 — Presupuesto de compras por departamento

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_030.md) · [Siguiente](ejercicio_032.md)

### Contexto

Administración recibe solicitudes que compiten por presupuestos independientes.

### Situación

El encargo es **presupuesto de compras por departamento**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Decisiones con motivo y presupuesto restante de cada departamento**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Presupuesto inicial por departamento y solicitudes ordenadas con identificador, departamento e importe positivo en céntimos.

### Resultado esperado

Decisiones con motivo y presupuesto restante de cada departamento.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Identificadores de solicitud únicos.
- Aceptar si el departamento existe y dispone de saldo.
- No transferir presupuesto entre departamentos.
- Continuar después de rechazos.

### Casos especiales y límites

Un departamento agotado no impide procesar otros.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.
- **Bucles, acumuladores y control de flujo**. Tema para investigar: Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.

### Variables y nombres

Identifica estas entidades: **presupuesto asignado, departamento solicitante, gasto aprobado, remanente**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué debe permanecer invariable después de un rechazo?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 019](ejercicio_019.md), [ejercicio 023](ejercicio_023.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. TI:1000, RH:500; TI700, TI400, RH500 → acepta, rechaza, acepta; TI300, RH0.
2. Departamento desconocido → rechazo.
3. Sin solicitudes → mismos presupuestos.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Validar contra la suma global y gastar fondos de otra área.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **TI:1000, RH:500; TI700, TI400, RH500 → acepta, rechaza, acepta; TI300, RH0**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué debe permanecer invariable después de un rechazo?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Control de presupuestos protege límites independientes y permite continuar con solicitudes de otras áreas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Incorporar cancelación de una solicitud aprobada una sola vez.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
