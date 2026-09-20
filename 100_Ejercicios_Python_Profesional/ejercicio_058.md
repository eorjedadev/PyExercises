# Ejercicio 058 — Plazos de atención con calendario

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_057.md) · [Siguiente](ejercicio_059.md)

### Contexto

Un equipo mide vencimientos únicamente en fechas laborables según un calendario recibido.

### Situación

El encargo es **plazos de atención con calendario**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Fecha de vencimiento y fechas contabilizadas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Fecha de alta ISO, plazo positivo en días laborables y conjunto de festivos ISO.

### Resultado esperado

Fecha de vencimiento y fechas contabilizadas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Contar a partir del día siguiente al alta.
- Laborables de lunes a viernes salvo festivos.
- Alta puede caer en festivo.
- Festivos duplicados no cambian resultado.
- No usar calendario externo.

### Casos especiales y límites

Un festivo en sábado no debe descontarse dos veces.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Fechas, intervalos y aritmética de calendario**. Tema para investigar: Investiga construcción y validación de fechas, diferencias y límites del intervalo; recibe el tiempo de referencia explícitamente.
- **Conjuntos, pertenencia y operaciones entre grupos**. Tema para investigar: Investiga qué información de orden o multiplicidad se pierde al representar datos como conjunto.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Evitan interpretar meses y días como cantidades con longitud fija.
- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **fecha de alta, días hábiles requeridos, festivos, vencimiento**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué datos hacen que el calendario sea reproducible?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 045](ejercicio_045.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Alta2025-01-03 viernes, plazo1, sin festivos →2025-01-06.
2. Festivo2025-01-06 →2025-01-07.
3. Plazo0 →rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Contar el día de alta aunque el contrato lo excluye.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora** (buscar ese título dentro del documento).
- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Alta2025-01-03 viernes, plazo1, sin festivos →2025-01-06**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué datos hacen que el calendario sea reproducible?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Acuerdos internos de atención pueden usar calendarios configurables sin depender de un reloj o servicio externo. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir una semana laboral configurable.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
