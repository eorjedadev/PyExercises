# Ejercicio 032 — Unión de clientes con sus pedidos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_031.md) · [Siguiente](ejercicio_033.md)

### Contexto

Un equipo comercial necesita un reporte que conserve pedidos con referencias rotas.

### Situación

El encargo es **unión de clientes con sus pedidos**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Cantidad e importe de pedidos por cliente, y listado separado de pedidos huérfanos**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Clientes con identificador único y nombre; pedidos con identificador único, cliente e importe no negativo.

### Resultado esperado

Cantidad e importe de pedidos por cliente, y listado separado de pedidos huérfanos.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- No descartar pedidos sin cliente conocido.
- Presentarlos como huérfanos.
- Incluir clientes sin pedidos con total cero.
- No modificar las entradas.

### Casos especiales y límites

Un pedido de importe cero sigue contando como pedido.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.
- **Conjuntos, pertenencia y operaciones entre grupos**. Tema para investigar: Investiga qué información de orden o multiplicidad se pierde al representar datos como conjunto.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.

### Variables y nombres

Identifica estas entidades: **clientes por identificador, pedidos relacionados, total por cliente, huérfanos**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo representarás una relación que no se puede resolver?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 017](ejercicio_017.md), [ejercicio 024](ejercicio_024.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Clientes A,B; pedidos P1 A100, P2 X50 → A:1/100, B:0/0, huérfano P2.
2. Sin pedidos → todos en cero.
3. Clientes duplicados → error de entrada.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Perder datos al asumir que todas las referencias existen.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Clientes A,B; pedidos P1 A100, P2 X50 → A:1/100, B:0/0, huérfano P2**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo representarás una relación que no se puede resolver?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Reportes empresariales combinan entidades relacionadas sin ocultar registros con referencias rotas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un informe de clientes cuyo importe supere un umbral.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
