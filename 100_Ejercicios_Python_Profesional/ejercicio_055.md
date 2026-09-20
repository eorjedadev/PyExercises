# Ejercicio 055 — Reserva de ejemplares como objeto

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_054.md) · [Siguiente](ejercicio_056.md)

### Contexto

Una biblioteca quiere que las reglas de un ejemplar permanezcan juntas al reutilizarlas.

### Situación

El encargo es **reserva de ejemplares como objeto**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Estado y titular después de cada operación, con motivos de rechazo**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Ejemplar con identificador, estado disponible inicial y operaciones reservar usuario, retirar usuario, devolver usuario.

### Resultado esperado

Estado y titular después de cada operación, con motivos de rechazo.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Usar una clase que proteja transiciones.
- Disponible→reservado→prestado→disponible.
- Retirar solo por quien reservó.
- Devolver solo por quien tiene el préstamo.
- Usuarios no vacíos.
- Rechazos conservan estado.

### Casos especiales y límites

Dos ejemplares distintos no deben compartir su titular.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Clases, instancias, composición e invariantes**. Tema para investigar: Compara atributos de instancia y de clase, vistas públicas y métodos; justifica si la clase protege algo o solo añade ceremonia.
- **Modelado de estados, transiciones y efectos**. Tema para investigar: Relaciona condicionales, datos y funciones con invariantes; separa intento, validación y confirmación sin asumir una arquitectura única.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Pueden reunir estado y operaciones cuando esa unión protege reglas del dominio.
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **identificador del ejemplar, titular actual, estado, operación solicitada**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué invariantes justifican una clase en lugar de un recipiente de datos?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 023](ejercicio_023.md), [ejercicio 050](ejercicio_050.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Reservar Ana, retirar Ana, devolver Ana →disponible sin titular.
2. Retirar sin reserva →rechazo.
3. Reservado por Ana, retirar Beto →sin cambio.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Permitir que el código externo cambie el estado saltándose las reglas.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Programación Orientada a Objetos](../Universidad_Python.md#programaci%C3%B3n-orientada-a-objetos).
- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Reservar Ana, retirar Ana, devolver Ana →disponible sin titular**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué invariantes justifican una clase en lugar de un recipiente de datos?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Objetos de dominio protegen transiciones y evitan que estados imposibles aparezcan por modificación externa. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Incorporar cancelación de reserva por su titular.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
