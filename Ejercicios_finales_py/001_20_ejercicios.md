# Ejercicios Finales - Colección de Práctica Avanzada

> 500 ejercicios con sugerencias y ayuda para consolidar conocimientos.

---

## 001. Calculadora de fechas (Modelo de datos)

**Objetivo**: Implementar una clase `Date` que soporte operaciones aritméticas y representación legible.

```python
# Requisitos:
# - __init__(año, mes, día)
# - __add__(días) - sumar días
# - __sub__(other) - diferencia entre fechas
# - __repr__ - representación evaluable
# - __str__ - representación legible (dd/mm/aaaa)
```

**Sugerencia**: Usar `datetime.date ` como referencia de comportamiento. La clase debe ser inmutable.

---

## 002. Matriz dispersa (Secuencias)

**Objetivo**: Crear ` SparseMatrix` que solo almacene celdas no nulas.

```python
# Requisitos:
# - matrix[fila, col] - indexado dual
# - matrix[fila, col] = valor - set valor
# - __len__ - número total de celdas
# - memory usage < O(n*m) para matrices grandes
```

**Sugerencia**: Usar `dict ` interno con tuplas `(fila, col)` como clave. Implementar `__getitem__` y `__setitem__`.

---

## 003. Decorator de caché (Funciones)

**Objetivo**: Implementar `@cache ` sin usar ` functools.lru_cache`.

```python
# Requisitos:
# - Cachear resultados por argumentos
# - Thread-safe
# - Memory limit configurable
# - Cache.clear() para invalidar
```

**Sugerencia**: Usar `functools.wraps `, ` threading.Lock ` y LRU eviction manual.

---

## 004. Plugin system (POO)

**Objetivo**: Crear sistema de plugins usando ` Protocol` y registro automático.

```python
# Requisitos:
# - Protocol Plugin con validate(), process()
# - Registro automático con decorador
# - Ejecución por tipo de datos
```

**Sugerencia**: Usar `__init_subclass__` o entry points para registro automático.

---

## 005. Lista infinita (Iteradores)

**Objetivo**: Implementar ` InfiniteSequence` que genere números primos infinitamente.

```python
# Requisitos:
# - primes[:10] - slicing
# - primes[100] - indexado
# - lazy evaluation
# - __len__ opcional con error
```

**Sugerencia**: Usar generador interno con `yield` y caché para valores ya calculados.

---

## 006. WebSocket chat (Async)

**Objetivo**: Servidor de chat con websockets y broadcast.

```python
# Requisitos:
# - Conexión múltiple de clientes
# - Broadcast a todos
# - Salas de chat separadas
# - Manejo de desconexiones limpias
```

**Sugerencia**: Usar `asyncio.Queue ` por sala y ` asyncio.gather` para broadcast.

---

## 007. Test fixture factory (Testing)

**Objetivo**: Creador de fixtures para cualquier modelo SQLAlchemy.

```python
# Requisitos:
# - Factory genérica
# - Soporte para relationships
# - Faker para datos realistas
```

**Sugerencia**: Usar `pytest.fixture ` con ` request.cls` y introspección de columnas.

---

## 008. Repository genérico (Arquitectura)

**Objetivo**: Repository genérico con tipado correcto para cualquier modelo.

```python
# Requisitos:
# - Generic[ModelType]
# - get_by_id, list, create, update, delete
# - Filtros dinámicos
```

**Sugerencia**: Usar `TypeVar ` con bound a ` declarative_base ` y ` getattr`.

---

## 009. CLI con subcomandos (CLI)

**Objetivo**: CLI que gestione usuarios con subcomandos y persistencia.

```python
# Requisitos:
# - create-user, delete-user, list-users
# - JSON storage
# - Interactive prompts
```

**Sugerencia**: Usar `typer ` con ` Path ` argument y ` json` module.

---

## 010. Port scanner (Networking)

**Objetivo**: Scanner paralelo de puertos con asyncio.

```python
# Requisitos:
# - Escaneo de 1000+ puertos
# - Rate limiting
# - Service detection
# - JSON export
```

**Sugerencia**: Usar `asyncio.Semaphore `, ` asyncio.open_connection ` y ` socket.getservbyport`.

---

## 011. Correlation logger (Logging)

**Objetivo**: Logger con correlation ID automático para requests.

```python
# Requisitos:
# - ID único por request
# - Contexto automático
# - JSON output
```

**Sugerencia**: Usar `contextvars.ContextVar` para thread-safe correlation.

---

## 012. Rate limiter cache (Optimización)

**Objetivo**: Cache con rate limiting integrado.

```python
# Requisitos:
# - Límite de hits por ventana
# - Eviction automático
# - Stats de uso
```

**Sugerencia**: Combinar `sortedcontainers.SortedDict ` con sliding window.

---

## 013. State machine (Patrones)

**Objetivo**: Autómata para parsar protocolo binario.

**Sugerencia**: Usar `@dataclass ` para estados y ` match/case ` para transiciones.

---

## 014. Feature importance (ML)

**Objetivo**: Pipeline que calcule feature importance de XGBoost.

**Sugerencia**: Usar ` sklearn.model_selection.RandomizedSearchCV ` y ` sklearn.inspection.permutation_importance `.

---

## 015. Scanner web (Pentesting)

**Objetivo**: Scanner que detecte directorios ocultos.

**Sugerencia**: Usar ` asyncio ` para fuzz concurrente de wordlists comunes.

---

## 016. Editor con syntax highlight (GUI)

**Objetivo**: Editor simple con coloreado de keywords.

**Sugerencia**: Usar ` tkinter.Text ` con tags de color y regex para matching.

---

## 017. ThreadPool con timeout (Concurrencia)

**Objetivo**: Pool que cancele tasks después de timeout.

**Sugerencia**: Usar ` concurrent.futures.Future ` con ` add_done_callback `.

---

## 018. Type guard (Tipado)

**Objetivo**: Implementar ` is_str_list ` para narrowing.

**Sugerencia**: Usar ` TypeGuard ` de ` typing ` y ` Protocol ` para collections.

---

## 019. Query builder type-safe (Tipado)

**Objetivo**: Builder con method chaining type-checked.

**Sugerencia**: Usar `@overload` para diferentes etapas del builder.