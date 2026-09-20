# Ejercicio 053 — Importación con aceptación total

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_052.md) · [Siguiente](ejercicio_054.md)

### Contexto

Una tienda necesita aplicar un lote de ajustes solo si todos son posibles.

### Situación

El encargo es **importación con aceptación total**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Nuevo inventario completo o errores con inventario original intacto**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Mapa de existencias y lista ordenada de ajustes código/delta entero distinto de cero.

### Resultado esperado

Nuevo inventario completo o errores con inventario original intacto.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Códigos deben existir.
- Evaluar stock acumulado en orden y nunca permitir negativo.
- Si falla una línea, rechazar todo el lote.
- No modificar el mapa recibido.
- Devolver resultado independiente.

### Casos especiales y límites

Una copia superficial puede ser insuficiente si luego agregas estructuras anidadas.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Referencias, mutabilidad y propiedad de los datos**. Tema para investigar: Comprende alias, copias superficiales, elementos anidados e inmutabilidad antes de decidir qué compartir.
- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Explican por qué una modificación puede aparecer en otra parte del programa.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **inventario original, estado propuesto, ajuste inválido, lote aprobado**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué significa todo o nada cuando una regla depende de movimientos anteriores?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 023](ejercicio_023.md), [ejercicio 037](ejercicio_037.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A2; ajustes -1,+3 →A4.
2. A2; ajustes -3,+3 →rechazo aunque saldo final sería2.
3. Lote vacío →inventario equivalente sin compartir mutables.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Dejar aplicados los ajustes previos a la primera falla.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-6-referencias-mutabilidad-y-ciclo-de-vida-de-objetos).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A2; ajustes -1,+3 →A4**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué significa todo o nada cuando una regla depende de movimientos anteriores?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Importaciones de ajustes protegen el estado previo cuando una operación tardía invalida todo el lote. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir metadatos anidados y comprobar que el origen sigue intacto.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
