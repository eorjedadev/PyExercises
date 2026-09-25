# Ejercicios Finales - Parte 1 (001-020): Fundamentos Core, Modelo de Datos, POO y Concurrencia

> Colección de práctica profesional avanzada (Ejercicios 001 al 020).

---

## 001. Calculadora de fechas (Modelo de datos) (Modelo de Datos y POO)

### Contexto y Escenario
En sistemas de gestión financiera, facturación o reservas hoteleras, es fundamental modelar fechas de manera inmutable, precisa y con soporte completo para operadores aritméticos nativos de Python.

### Objetivo
Construir una clase `Date` personalizada e inmutable que implemente el protocolo del modelo de datos de Python (`__init__`, `__repr__`, `__str__`, `__add__`, `__sub__`, `__eq__`, `__lt__`), permitiendo aritmética de fechas y serialización.

### Misión Concreta y Operaciones Mínimas
- Implementar constructor con validación de año, mes (1-12) y días según mes (incluyendo años bisiestos).
- Sobrecargar operador `__add__(dias: int)` para sumar días y retornar una nueva instancia `Date`.
- Sobrecargar operador `__sub__(other: Union[Date, int])`: Si se resta otra fecha retorna la diferencia entera en días; si se resta un entero retorna una nueva `Date`.
- Implementar `__repr__()` para representación evaluable (`Date(2026, 9, 22)`) y `__str__()` para formato legible (`22/09/2026`).
- Garantizar ordenamiento total implementando `__eq__` y `__lt__`.

### Reglas de Dominio y Validación
- La clase `Date` debe ser estrictamente inmutable tras su instanciación.
- No permitir años menores a 1 ni fechas inexistentes (ej. 29 de febrero en año no bisiesto).
- Si se intenta operar con tipos no soportados, retornar `NotImplemented` o elevar `TypeError`.

### Piezas y Herramientas a Integrar
- `typing.Union`, `typing.Self`
- Métodos mágicos del modelo de datos de Python
- Algoritmo de año bisiesto: `(año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)`

### Orientación del Profesor
1. Valida primero los límites del calendario antes de almacenar los valores de los atributos.

2. Asegúrate de que ninguna operación aritmética modifique `self`; retorna siempre una nueva instancia.

3. Separa la lógica de cómputo del formato de salida visual.

### Lógica a Cuidar y Errores a Vigilar
- `ValueError` al intentar instanciar fechas inválidas como `Date(2026, 2, 29)`.
- `TypeError` al sumar tipos incompatibles.
- Modificar el objeto original en lugar de generar una nueva instancia.

### Batería de Pruebas Mínimas
- **Suma básica**: `Date(2026, 9, 22) + 10` -> `Date(2026, 10, 2)`.
- **Diferencia de fechas**: `Date(2026, 10, 2) - Date(2026, 9, 22)` -> `10`.
- **Bisiesto válido**: `Date(2024, 2, 28) + 1` -> `Date(2024, 2, 29)`.
- **Fecha inválida**: `Date(2023, 2, 29)` -> Eleva `ValueError`.

### Reto Extra
Añadir soporte para parsing desde formato ISO 8601 (`Date.from_iso('2026-09-22')`) y método para obtener el día de la semana.

---
## 002. Matriz dispersa (Secuencias y Optimización) (Estructuras de Datos y Secuencias)

### Contexto y Escenario
En problemas de grafos, álgebra lineal y sistemas de recomendación, las matrices gigantes contienen en su mayoría ceros. Almacenar todas las celdas agota la memoria rápidamente.

### Objetivo
Implementar la clase `SparseMatrix` que almacene en memoria únicamente las celdas con valores no nulos mediante un diccionario de coordenadas `(fila, columna)`, implementando el protocolo de indexación dual.

### Misión Concreta y Operaciones Mínimas
- Implementar constructor `SparseMatrix(filas: int, columnas: int, default: float = 0.0)`.
- Implementar `__getitem__(key: tuple[int, int])` para acceder mediante `matrix[f, c]`.
- Implementar `__setitem__(key: tuple[int, int], value: float)`: almacenar solo si el valor difiere del valor por defecto; si se asigna cero, eliminar la entrada del diccionario interno.
- Implementar `__len__()` que retorne el total de celdas lógicas (`filas * columnas`).
- Implementar método `non_zero_count()` para conocer la cantidad real de celdas almacenadas.

### Reglas de Dominio y Validación
- El uso de memoria debe ser O(k), donde k es la cantidad de elementos no nulos.
- Las coordenadas fuera de rango deben elevar `IndexError`.
- La consulta de celdas no asignadas debe retornar el valor por defecto en tiempo O(1).

### Piezas y Herramientas a Integrar
- `dict` interno con claves tupla `(int, int)`
- Métodos mágicos `__getitem__`, `__setitem__`, `__len__`, `__repr__`

### Orientación del Profesor
1. Usa una tupla `(fila, columna)` como clave en un diccionario estándar de Python.

2. En `__setitem__`, si el valor recibido es igual a cero o al valor por defecto, haz un `dict.pop(key, None)` para liberar la memoria.

3. Valida que `0 <= fila < filas` y `0 <= columna < columnas` antes de operar.

### Lógica a Cuidar y Errores a Vigilar
- `IndexError` al consultar índices negativos o fuera de dimensión.
- Fuga de memoria al almacenar ceros explícitamente en el diccionario.

### Batería de Pruebas Mínimas
- **Asignación y consulta**: `m[10, 20] = 5.5` -> `m[10, 20] == 5.5`.
- **Valor por defecto**: `m[1, 1] == 0.0`.
- **Liberación de celda**: `m[10, 20] = 0.0` -> `(10, 20)` desaparece del diccionario interno.
- **Límites**: `m[100, 100]` en matriz 10x10 -> Eleva `IndexError`.

### Reto Extra
Implementar la suma de dos matrices dispersas (`__add__`) y la transposición (`transpose()`).

---
## 003. Decorator de caché LRU manual (Funciones y Concurrencia) (Funciones de Alto Orden y Decoradores)

### Contexto y Escenario
El almacenamiento en caché de funciones costosas o consultas I/O requiere controlar el límite de memoria mediante políticas de desalojo LRU (Least Recently Used) y garantizar seguridad en multihilo.

### Objetivo
Construir un decorador `@lru_cache_custom(maxsize=128)` sin utilizar `functools.lru_cache`, que soporte argumentos posicionales y nombrados, desalojo LRU y métodos de inspección `cache_info()` y `cache_clear()`.

### Misión Concreta y Operaciones Mínimas
- Diseñar la envoltura con `functools.wraps` para conservar la firma y docstrings originales.
- Serializar de forma unívoca argumentos `*args` y `**kwargs` para conformar la clave de caché.
- Implementar estructura de ordenamiento de acceso (utilizando `collections.OrderedDict` o lista doblemente enlazada con `dict`).
- Integrar sincronización mediante `threading.RLock` para garantizar seguridad en entornos con múltiples hilos.
- Adjuntar a la función decorada los métodos `.cache_info()` (hits, misses, currsize, maxsize) y `.cache_clear()`.

### Reglas de Dominio y Validación
- Cuando el tamaño alcance `maxsize`, el siguiente miss debe desalojar el elemento menos recientemente utilizado en tiempo O(1).
- Los argumentos mutables no hashables deben manejarse de forma segura o elevar `TypeError` explícito.

### Piezas y Herramientas a Integrar
- `collections.OrderedDict`
- `threading.RLock`
- `functools.wraps`

### Orientación del Profesor
1. En cada hit de caché, mueve la clave al final del `OrderedDict` mediante `.move_to_end(key)`.

2. Protege tanto la lectura como la mutación del diccionario dentro del bloque `with lock:`.

### Lógica a Cuidar y Errores a Vigilar
- Condiciones de carrera al modificar la caché simultáneamente desde varios hilos.
- Contadores de `hits`/`misses` desincronizados.

### Batería de Pruebas Mínimas
- **Caché hit**: Dos llamadas consecutivas con mismos argumentos ejecutan la función una sola vez.
- **Desalojo LRU**: Con `maxsize=2`, al insertar una 3ra clave se expulsa la primera accedida.
- **Limpieza**: `.cache_clear()` vacía la estructura y resetea contadores.

### Reto Extra
Agregar soporte opcional para TTL (Time-To-Live) con expiración automática de entradas tras N segundos.

---
## 004. Plugin system (POO) (Fundamentos Avanzados de Python)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Plugin system (POO)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Crear sistema de plugins usando ` Protocol` y registro automático.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Plugin system (POO)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `__init_subclass__` o entry points para registro automático.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `__init_subclass__` o entry points para registro automático.

### Orientación del Profesor
1. Comienza descomponiendo `Plugin system (POO)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Plugin system (POO)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Plugin system (POO)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 005. Lista infinita (Iteradores) (Fundamentos Avanzados de Python)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Lista infinita (Iteradores)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Implementar ` InfiniteSequence` que genere números primos infinitamente.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Lista infinita (Iteradores)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar generador interno con `yield` y caché para valores ya calculados.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar generador interno con `yield` y caché para valores ya calculados.

### Orientación del Profesor
1. Comienza descomponiendo `Lista infinita (Iteradores)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Lista infinita (Iteradores)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Lista infinita (Iteradores)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 006. WebSocket chat (Async) (Asincronía y Concurrencia con Asyncio)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `WebSocket chat (Async)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Servidor de chat con websockets y broadcast.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `WebSocket chat (Async)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `asyncio.Queue ` por sala y ` asyncio.gather` para broadcast.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `asyncio.Queue ` por sala y ` asyncio.gather` para broadcast.

### Orientación del Profesor
1. Comienza descomponiendo `WebSocket chat (Async)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `WebSocket chat (Async)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `WebSocket chat (Async)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 007. Test fixture factory (Testing) (Testing Automatizado y Calidad de Software)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Test fixture factory (Testing)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Creador de fixtures para cualquier modelo SQLAlchemy.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Test fixture factory (Testing)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `pytest.fixture ` con ` request.cls` y introspección de columnas.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `pytest.fixture ` con ` request.cls` y introspección de columnas.

### Orientación del Profesor
1. Comienza descomponiendo `Test fixture factory (Testing)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Test fixture factory (Testing)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Test fixture factory (Testing)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 008. Repository genérico (Arquitectura) (Fundamentos Avanzados de Python)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Repository genérico (Arquitectura)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Repository genérico con tipado correcto para cualquier modelo.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Repository genérico (Arquitectura)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `TypeVar ` con bound a ` declarative_base ` y ` getattr`.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `TypeVar ` con bound a ` declarative_base ` y ` getattr`.

### Orientación del Profesor
1. Comienza descomponiendo `Repository genérico (Arquitectura)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Repository genérico (Arquitectura)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Repository genérico (Arquitectura)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 009. CLI con subcomandos (CLI) (Herramientas de Línea de Comandos (CLI))

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `CLI con subcomandos (CLI)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
CLI que gestione usuarios con subcomandos y persistencia.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `CLI con subcomandos (CLI)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `typer ` con ` Path ` argument y ` json` module.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `typer ` con ` Path ` argument y ` json` module.

### Orientación del Profesor
1. Comienza descomponiendo `CLI con subcomandos (CLI)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `CLI con subcomandos (CLI)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `CLI con subcomandos (CLI)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 010. Port scanner (Networking) (Redes y Programación de Sockets)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Port scanner (Networking)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Scanner paralelo de puertos con asyncio.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Port scanner (Networking)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `asyncio.Semaphore `, ` asyncio.open_connection ` y ` socket.getservbyport`.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `asyncio.Semaphore `, ` asyncio.open_connection ` y ` socket.getservbyport`.

### Orientación del Profesor
1. Comienza descomponiendo `Port scanner (Networking)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Port scanner (Networking)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Port scanner (Networking)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 011. Correlation logger (Logging) (Observabilidad, Métricas y Logging Estructurado)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Correlation logger (Logging)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Logger con correlation ID automático para requests.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Correlation logger (Logging)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `contextvars.ContextVar` para thread-safe correlation.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `contextvars.ContextVar` para thread-safe correlation.

### Orientación del Profesor
1. Comienza descomponiendo `Correlation logger (Logging)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Correlation logger (Logging)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Correlation logger (Logging)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 012. Rate limiter cache (Optimización) (Funciones de Alto Orden y Decoradores)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Rate limiter cache (Optimización)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Cache con rate limiting integrado.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Rate limiter cache (Optimización)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Combinar `sortedcontainers.SortedDict ` con sliding window.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Combinar `sortedcontainers.SortedDict ` con sliding window.

### Orientación del Profesor
1. Comienza descomponiendo `Rate limiter cache (Optimización)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Rate limiter cache (Optimización)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Rate limiter cache (Optimización)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 013. State machine (Patrones) (Patrones de Diseño de Software (GoF))

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `State machine (Patrones)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Autómata para parsar protocolo binario.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `State machine (Patrones)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `@dataclass ` para estados y ` match/case ` para transiciones.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `@dataclass ` para estados y ` match/case ` para transiciones.

### Orientación del Profesor
1. Comienza descomponiendo `State machine (Patrones)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `State machine (Patrones)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `State machine (Patrones)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 014. Feature importance (ML) (Redes y Programación de Sockets)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Feature importance (ML)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Pipeline que calcule feature importance de XGBoost.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Feature importance (ML)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar ` sklearn.model_selection.RandomizedSearchCV ` y ` sklearn.inspection.permutation_importance `.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar ` sklearn.model_selection.RandomizedSearchCV ` y ` sklearn.inspection.permutation_importance `.

### Orientación del Profesor
1. Comienza descomponiendo `Feature importance (ML)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Feature importance (ML)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Feature importance (ML)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 015. Scanner web (Pentesting) (Testing Automatizado y Calidad de Software)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Scanner web (Pentesting)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Scanner que detecte directorios ocultos.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Scanner web (Pentesting)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar ` asyncio ` para fuzz concurrente de wordlists comunes.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar ` asyncio ` para fuzz concurrente de wordlists comunes.

### Orientación del Profesor
1. Comienza descomponiendo `Scanner web (Pentesting)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Scanner web (Pentesting)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Scanner web (Pentesting)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 016. Editor con syntax highlight (GUI) (Interfaces Gráficas de Usuario (GUI))

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Editor con syntax highlight (GUI)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Editor simple con coloreado de keywords.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Editor con syntax highlight (GUI)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar ` tkinter.Text ` con tags de color y regex para matching.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar ` tkinter.Text ` con tags de color y regex para matching.

### Orientación del Profesor
1. Comienza descomponiendo `Editor con syntax highlight (GUI)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Editor con syntax highlight (GUI)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Editor con syntax highlight (GUI)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 017. ThreadPool con timeout (Concurrencia) (Fundamentos Avanzados de Python)

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `ThreadPool con timeout (Concurrencia)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Pool que cancele tasks después de timeout.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `ThreadPool con timeout (Concurrencia)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar ` concurrent.futures.Future ` con ` add_done_callback `.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar ` concurrent.futures.Future ` con ` add_done_callback `.

### Orientación del Profesor
1. Comienza descomponiendo `ThreadPool con timeout (Concurrencia)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `ThreadPool con timeout (Concurrencia)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `ThreadPool con timeout (Concurrencia)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 018. Type guard (Tipado) (Tipado Estático y Sistema de Tipos (PEP 484/544/647))

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Type guard (Tipado)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Implementar ` is_str_list ` para narrowing.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Type guard (Tipado)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar ` TypeGuard ` de ` typing ` y ` Protocol ` para collections.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar ` TypeGuard ` de ` typing ` y ` Protocol ` para collections.

### Orientación del Profesor
1. Comienza descomponiendo `Type guard (Tipado)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Type guard (Tipado)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Type guard (Tipado)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 019. Query builder type-safe (Tipado) (Tipado Estático y Sistema de Tipos (PEP 484/544/647))

### Contexto y Escenario
En entornos de producción y arquitecturas empresariales de Python, la solución `Query builder type-safe (Tipado)` es indispensable para garantizar robustez, mantenibilidad y alto rendimiento. Este ejercicio requiere modelar una arquitectura modular, separando la lógica de negocio de los efectos secundarios y la infraestructura.

### Objetivo
Builder con method chaining type-checked.. La implementación debe estructurarse mediante contratos claros, validación exhaustiva y manejo robusto de excepciones.

### Misión Concreta y Operaciones Mínimas
- Diseñar e implementar la estructura principal para `Query builder type-safe (Tipado)` con interfaces tipadas y modularidad.
- Implementar los métodos de procesamiento, transformación o gestión de ciclo de vida requeridos.
- Proveer mecanismos limpios de inicialización, ejecución y liberación de recursos.
- Validar rigurosamente los parámetros de entrada y gestionar estados anómalos o de error.
- Aprovechar la técnica clave: Usar `@overload` para diferentes etapas del builder.

### Reglas de Dominio y Validación
- No tolerar estados inconsistentes ni mutaciones inesperadas sobre estructuras compartidas.
- Garantizar tipado explícito en todas las firmas públicas mediante type hints (PEP 484/544/586).
- El código debe ser determinista, seguro ante concurrencia (thread-safe o async-safe según corresponda) y no filtrar recursos.
- Separar de forma estricta la lógica de cómputo/dominio de la entrada/salida y presentación.

### Piezas y Herramientas a Integrar
- Módulos clave: typing, functools, contextvars, dataclasses.
- Estructuras de datos óptimas para complejidad temporal O(1) o O(log n) según el caso.
- Manejo de excepciones específico para cada condición de fallo prevista.
- Herramientas sugeridas: Usar `@overload` para diferentes etapas del builder.

### Orientación del Profesor
1. Comienza descomponiendo `Query builder type-safe (Tipado)` en sus responsabilidades esenciales: define interfaces, contratos de datos y flujos de ejecución.

2. Diseña primero los casos de fallo y validaciones antes de escribir la ruta de ejecución principal.

3. Asegura la liberación ordenada de recursos utilizando manejadores de contexto (`with` o `async with`) cuando existan conexiones, locks o descriptores de archivos.

4. Evita el acoplamiento directo entre componentes; favorece la inyección de dependencias y el uso de protocolos abstractos.

### Lógica a Cuidar y Errores a Vigilar
- `TypeError` o `ValueError` ante entradas con formato o tipos incorrectos.
- Fugas de memoria (memory leaks) por referencias circulares o no liberación de descriptores de archivos/sockets.
- Condiciones de carrera (race conditions) o interbloqueos (deadlocks) en entornos concurrentes.
- Excepciones no capturadas que puedan abortar el hilo o proceso principal.

### Batería de Pruebas Mínimas
- **Caso Nominal**: Ejecución con parámetros válidos verificando que el resultado cumpla con la especificación de `Query builder type-safe (Tipado)`.
- **Caso de Borde**: Ejecución con entradas vacías, límites superiores/inferiores o colecciones de tamaño cero.
- **Caso de Error Controlado**: Enviar datos inválidos o desconexiones forzadas y validar que se eleven las excepciones esperadas sin corromper el estado.

### Reto Extra
Extender `Query builder type-safe (Tipado)` incorporando telemetría/métricas (tiempos de respuesta, contadores de fallos), soporte asíncrono no bloqueante con `asyncio` o persistencia desacoplada si aplica.

---
## 020. Pipeline de streaming de datos sin carga en memoria (Secuencias) (Estructuras de Datos y Secuencias)

### Contexto y Escenario
Al procesar archivos de texto o logs de gigabytes o terabytes, cargar todo el archivo en memoria produce errores `MemoryError`. La solución estándar consiste en encadenar generadores lazy.

### Objetivo
Construir un pipeline compuesto por generadores encadenados que lea un archivo línea por línea, filtre líneas vacías, transforme el texto a mayúsculas, tokenice y calcule frecuencias de palabras con consumo constante de memoria O(1).

### Misión Concreta y Operaciones Mínimas
- Generador `read_lines(file_path)`: Lee de forma perezosa el archivo sin usar `.readlines()`.
- Generador `filter_empty_and_comments(lines)`: Omite líneas en blanco o que inicien con `#`.
- Generador `transform_uppercase(lines)`: Convierte el flujo de texto a mayúsculas.
- Generador `tokenize_words(lines)`: Extrae palabras individuales mediante expresiones regulares.
- Función `aggregate_frequencies(tokens, top_n=10)`: Acumula frecuencias y retorna el top de palabras más comunes.

### Reglas de Dominio y Validación
- El uso de memoria RAM debe mantenerse en O(1) independientemente del tamaño del archivo de entrada.
- Manejar correctamente el cierre de descriptores de archivos mediante context managers (`with`).

### Piezas y Herramientas a Integrar
- `yield` y `yield from`
- `collections.Counter`
- `re.finditer`
- `pathlib.Path`

### Orientación del Profesor
1. Encadena los generadores pasando la salida de uno como argumento iterador del siguiente.

2. No conviertas ningún paso intermedio a lista (`list(generator)`); mantén la evaluación perezosa hasta la agregación final.

### Lógica a Cuidar y Errores a Vigilar
- Usar `.read()` o `.readlines()` dentro de `read_lines()` cargando todo el archivo.
- No cerrar el archivo si el consumidor se interrumpe prematuramente.

### Batería de Pruebas Mínimas
- **Procesamiento correcto**: Verifica que líneas comentadas no aparezcan en el conteo.
- **Eficiencia de memoria**: Validar con archivo sintético de 500 MB que el proceso no supere 25 MB de RAM.

### Reto Extra
Implementar un generador de batching (`chunked(tokens, size=1000)`) para procesar datos en lotes.

---
