# Ejercicio 030 — Comparación de inventarios declarados

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_029.md) · [Siguiente](ejercicio_031.md)

### Contexto

Auditoría compara las cantidades declaradas por dos sistemas.

### Situación

El encargo es **comparación de inventarios declarados**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Diferencias con ambos valores cuando existan y clase de discrepancia**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Dos mapas de código a cantidad entera no negativa.

### Resultado esperado

Diferencias con ambos valores cuando existan y clase de discrepancia.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- La ausencia de código es distinta de cantidad cero.
- Informar solo diferencias.
- Distinguir solo en origen, solo en destino y cantidad distinta.
- Ordenar por código.

### Casos especiales y límites

No rellenar ausencias con cero antes de clasificar.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Conjuntos, pertenencia y operaciones entre grupos**. Tema para investigar: Investiga qué información de orden o multiplicidad se pierde al representar datos como conjunto.
- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **inventario de origen, inventario de destino, código ausente, discrepancia**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué información desaparece al sustituir una ausencia por cero?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 018](ejercicio_018.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Origen A:0,B:2; destino B:3,C:0 → A solo origen, B diferencia, C solo destino.
2. Mapas idénticos → sin diferencias.
3. Cantidad negativa → entrada inválida.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar un valor por defecto que oculte códigos inexistentes.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Origen A:0,B:2; destino B:3,C:0 → A solo origen, B diferencia, C solo destino**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué información desaparece al sustituir una ausencia por cero?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Auditorías entre sistemas conservan la diferencia entre una entidad ausente y una entidad con valor cero. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un resumen de unidades de diferencia solo para códigos compartidos.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
