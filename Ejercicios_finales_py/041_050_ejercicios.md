# Ejercicios Finales - Parte 3 (del 41 al 50)

---

## 041. Binary protocol encoder

**Objetivo**: Implementar encoder/decoder para protocolo binario con header.

```python
# Protocolo: [2 bytes type][4 bytes length][payload]
# Soporta: INTEGER, STRING, LIST
```

**Sugerencia**: Usar `struct.pack('!HI', type, len)` para header.

---

## 042. Rate limiter con Redis

**Objetivo**: Implementar token bucket rate limiter distribuido.

**Sugerencia**: Usar Redis ` INCR ` y ` EXPIRE ` con Lua script atómico.

---

## 043. Memory mapped file processor

**Objetivo**: Procesar archivo grande usando mmap.

**Sugerencia**: Usar ` mmap.mmap ` para acceder sin cargar en memoria.

---

## 044. Priority task queue

**Objetivo**: Queue con prioridad que procese tareas urgentes primero.

**Sugerencia**: Usar ` heapq ` con tuplas `(priority, counter, task)`.

---

## 045. Circuit breaker pattern

**Objetivo**: Circuit breaker que falle rápido después de errores.

**Sugerencia**: Estados: CLOSED, OPEN, HALF_OPEN con timeout.

---

## 046. Event bus con handlers

**Objetivo**: Bus de eventos donde múltiples handlers puedan suscribirse.

**Sugerencia**: Usar ` weakref.WeakSet ` para evitar memory leaks.

---

## 047. Data validator con Protocol

**Objetivo**: Validador que funcione con cualquier tipo usando Protocol.

**Sugerencia**: Protocol ` Validatable ` con método ` validate() -> bool `.

---

## 048. Configurable logger

**Objetivo**: Logger que lea configuración de archivo TOML.

**Sugerencia**: Usar ` tomllib ` y ` logging.config.dictConfig `.

---

## 049. Benchmark framework

**Objetivo**: Framework para comparar rendimiento de funciones.

**Sugerencia**: Usar ` statistics ` para análisis y ` matplotlib ` para gráficos.

---

## 050. Plugin decorator system

**Objetivo**: Decorador que registre plugins automáticamente.

**Sugerencia**: Usar ` globals()` o entry points para registro.