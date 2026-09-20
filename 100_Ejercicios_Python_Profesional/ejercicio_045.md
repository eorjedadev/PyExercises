# Ejercicio 045 — Fechas de vencimiento de préstamos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_044.md) · [Siguiente](ejercicio_046.md)

### Contexto

Una biblioteca calcula devoluciones con días naturales, no con reglas legales.

### Situación

El encargo es **fechas de vencimiento de préstamos**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Fecha de vencimiento y días de retraso por préstamo válido**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de préstamos con identificador, fecha de salida ISO YYYY-MM-DD y plazo entero positivo; fecha de corte explícita.

### Resultado esperado

Fecha de vencimiento y días de retraso por préstamo válido.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Vencimiento igual a salida más plazo.
- Vence ese día y hay retraso solo después.
- Corte anterior a salida invalida ese préstamo.
- Fechas imposibles se reportan por registro.

### Casos especiales y límites

El cambio de mes y los años bisiestos afectan el cálculo.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Fechas, intervalos y aritmética de calendario**. Tema para investigar: Investiga construcción y validación de fechas, diferencias y límites del intervalo; recibe el tiempo de referencia explícitamente.
- **Excepciones y resultados de validación**. Tema para investigar: Investiga qué fallos puedes recuperar, cuáles debes propagar y cómo conservar su causa.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Evitan interpretar meses y días como cantidades con longitud fija.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **fecha de salida, plazo, fecha de vencimiento, días de retraso**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Por qué una fecha de corte recibida como dato mejora las pruebas?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 006](ejercicio_006.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Salida2024-02-28, plazo2, corte2024-03-02 → vence03-01, retraso1.
2. Corte igual a vencimiento →0.
3. 2025-02-29 → fecha inválida.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Sumar al número del día sin respetar el calendario.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora** (buscar ese título dentro del documento).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Salida2024-02-28, plazo2, corte2024-03-02 → vence03-01, retraso1**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Por qué una fecha de corte recibida como dato mejora las pruebas?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Control de vencimientos usa calendarios reales y fechas de corte explícitas para reproducir reportes. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Excluir fines de semana del plazo y actualizar el contrato de vencimiento.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
