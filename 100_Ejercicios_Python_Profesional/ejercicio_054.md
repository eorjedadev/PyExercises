# Ejercicio 054 — Reconstrucción de existencias desde eventos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_053.md) · [Siguiente](ejercicio_055.md)

### Contexto

Auditoría reconstruye el estado de un almacén sin confiar en un resumen guardado.

### Situación

El encargo es **reconstrucción de existencias desde eventos**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Inventario reconstruido, duplicados ignorados y eventual punto de detención**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Inventario inicial con cantidades enteras no negativas y eventos ordenados con id de evento, código, tipo entrada/salida y cantidad en unidades enteras positivas; se permiten reenvíos.

### Resultado esperado

Inventario reconstruido, duplicados ignorados y eventual punto de detención.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Identificadores repetidos con contenido idéntico se ignoran.
- Mismo id con contenido distinto es conflicto.
- Salida sin stock, código desconocido, tipo inválido o cantidad no positiva detienen la reconstrucción antes del evento.
- Devolver último estado válido y posición del problema.

### Casos especiales y límites

Repetir la misma notificación no debe duplicar sus efectos.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Modelado de estados, transiciones y efectos**. Tema para investigar: Relaciona condicionales, datos y funciones con invariantes; separa intento, validación y confirmación sin asumir una arquitectura única.
- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **identidad del evento, contenido original, estado reconstruido, punto de corte**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué información permite distinguir reenvío de contradicción?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 019](ejercicio_019.md), [ejercicio 050](ejercicio_050.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A0; E1 entrada3 repetido igual, E2 salida1 →A2 y un duplicado.
2. E1 entrada3 luego E1 entrada4 →conflicto.
3. Salida1 desde A0 →detención sin cambio.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Deduplicar solo por contenido y fusionar eventos distintos.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A0; E1 entrada3 repetido igual, E2 salida1 →A2 y un duplicado**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué información permite distinguir reenvío de contradicción?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Consumidores de eventos reconstruyen estados verificables y distinguen reenvíos de contradicciones. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Persistir un punto de control para continuar desde un prefijo ya validado.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
