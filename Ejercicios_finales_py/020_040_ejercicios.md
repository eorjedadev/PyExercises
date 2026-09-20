# Ejercicios Finales - Parte 2

---

## 020. Pipeline de datos

**Objetivo**: Pipeline que lea, filtre, transforme y cuente palabras.

```python
# Requisitos:
# - read_file() - lazy
# - filter_empty_lines()
# - to_uppercase()
# - count_words()
# - Memory efficient - no cargar todo en memoria
```

**Sugerencia**: Usar generadores encadenados con `yield from `.

---

## 021. Property-based testing

**Objetivo**: Tests con Hypothesis para una función de hash.

**Sugerencia**: Usar `@given(st.text(), st.integers())` y ` assume()` para precondiciones.

---

## 022. Memory profiler

**Objetivo**: Wrapper que mida uso de memoria antes/después de función.

**Sugerencia**: Usar ` tracemalloc ` o ` psutil.Process().memory_info()`.

---

## 023. WebSocket room manager

**Objetivo**: Manager que asigne usuarios a salas y broadcast selectivo.

**Sugerencia**: Usar ` WeakSet` para cleanup automático de clientes desconectados.

---

## 024. Context manager thread-safe

**Objetivo**: Context manager que adquiera locks automáticamente.

```python
# Uso esperado:
# with ThreadSafeResource() as resource:
#     resource.modify()
```

**Sugerencia**: Usar `threading.RLock ` en `__enter__`.

---

## 025. Test parametrization avanzado

**Objetivo**: Test parametrizado que genere casos desde archivo.

**Sugerencia**: Usar ` pytest_generate_tests ` hook o indirect parametrization.

---

## 026. Repository con soft deletes

**Objetivo**: Repository que implemente borrado suave con filtros automáticos.

**Sugerencia**: Usar ` with_loader_cbs ` y filtro global en ` get_queryset `.

---

## 027. CLI con autocompletado

**Objetivo**: CLI que autocomplete desde histórico o opciones.

**Sugerencia**: Usar ` prompt_toolkit ` con ` Completer ` custom.

---

## 028. Socket server concurrente

**Objetivo**: Servidor que maneje 1000+ conexiones concurrentes.

**Sugerencia**: Usar ` selectors ` o ` asyncio.start_server `.

---

## 029. Structured logs con contexto

**Objetivo**: Logger que agregue contexto automáticamente (user_id, request_id).

**Sugerencia**: Usar ` structlog.contextvars.merge_contextdict `.

---

## 030. LRU cache con TTL

**Objetivo**: Cache que expiración por tiempo además de tamaño.

**Sugerencia**: Usar ` sortedcontainers.SortedDict ` con timestamps.

---

## 031. Command pattern con undo

**Objetivo**: Sistema de comandos con historial y undo/redo.

**Sugerencia**: Usar ` deque ` con maxlen para historial y stack para undo.

---

## 032. Pipeline ML reproducible

**Objetivo**: Pipeline con hash de datos y versionado de features.

**Sugerencia**: Usar ` joblib.hash ` y ` dvc ` para tracking.

---

## 033. SQLi detector avanzado

**Objetivo**: Detector que identifique técnicas de bypass modernas.

**Sugerencia**: Usar ` sqlparse ` para parsing y árbol de detección.

---

## 034. Editor con multiple buffers

**Objetivo**: Editor con pestañas y buffer manager.

**Sugerencia**: Usar ` ttk.Notebook ` y ` Text ` widgets por documento.

---

## 035. Shared memory array

**Objetivo**: Array compartido entre procesos con locking.

**Sugerencia**: Usar ` multiprocessing.shared_memory.ShareableList `.

---

## 036. Typed config loader

**Objetivo**: Loader que valide config con TypedDict.

**Sugerencia**: Usar ` tomllib ` (Python 3.11+) o ` toml ` con validación.

---

## 037. Event-driven processor

**Objetivo**: Processor que publique eventos y múltiples handlers.

**Sugerencia**: Usar ` weakref.WeakMethod ` para cleanup automático.

---

## 038. Model explainer

**Objetivo**: Explainer que muestre feature importance y decision path.

**Sugerencia**: Usar ` sklearn.inspection.decision_path ` y ` matplotlib `.

---

## 039. Port knocking scanner

**Objetivo**: Scanner que detecte secuencias de puertos abiertos.

**Sugerencia**: Usar ` asyncio.Lock ` para coordinar secuencias.

---

## 040. Drag-drop interface

**Objetivo**: Interface que permita reorderar items con drag-drop.

**Sugerencia**: Usar `<ButtonPress>` y `<B1-Motion>` events de Tkinter.

---