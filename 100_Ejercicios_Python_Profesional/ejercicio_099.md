# Ejercicio 099 — Cola de trabajo con reintentos diferidos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_098.md) · [Siguiente](ejercicio_100.md)

---

## 1. Contexto y Propósito del Problema

### Contexto
Una automatización procesa trabajos pendientes sin bloquearse por un fallo transitorio.

### Situación Operativa
El encargo es **cola de trabajo con reintentos diferidos**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo Principal
Producir este resultado a partir de las entradas indicadas: **Historial con tiempos, resultado final por trabajo y número de intentos; sin esperas reales**. La solución debe distinguir los resultados válidos de los rechazos previstos.

---

## 2. Especificación del Contrato (Entradas y Salidas)

### Datos de Entrada
Trabajos con id único y secuencia de resultados simulados éxito/temporal/permanente; reloj inicial0; máximo3 intentos.

### Resultado Esperado
Historial con tiempos, resultado final por trabajo y número de intentos; sin esperas reales.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de Negocio e Invariantes
- **Regla:** Un intento por decisión.
- **Regla:** Elegir menor instante de elegibilidad y luego id.
- **Regla:** Primer temporal pospone2 segundos, segundo4.
- **Regla:** Tercer temporal agota.
- **Regla:** Éxito/permanente finalizan.
- **Regla:** Avanzar reloj simulado si no hay elegibles.
- **Regla:** Resultado faltante produce error de simulación para ese trabajo.

### Casos Especiales y Límites de Frontera
Un trabajo pospuesto no debe impedir atender a otro ya elegible.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

---

## 3. Guía de Nomenclatura y Variables Profesionales

Se recomienda definir nombres con alta carga semántica, respetando PEP 8 (`snake_case` para variables y funciones, `UPPER_SNAKE_CASE` para constantes de negocio):

| Variable / Identificador | Tipo Sugerido | Propósito y Semántica |
| :--- | :--- | :--- |
| `instante_elegible` | `str` | Entidad de dominio: instante elegible. |
| `intento_consumido` | `int` | Entidad de dominio: intento consumido. |
| `resultado_transitorio` | `str` | Entidad de dominio: resultado transitorio. |
| `trabajo_finalizado` | `str` | Entidad de dominio: trabajo finalizado. |

---

## 4. Guía del Instructor y Razonamiento Lógico (Paso a Paso sin Código)

Para resolver este ejercicio con calidad profesional, sigue este razonamiento mental estructurado. No comiences escribiendo código directamente; primero comprende el flujo de decisiones y traslada estos pasos lógicos a tu solución.

```mermaid
graph TD
    A[1. Recepción y Saneamiento] --> B[2. Guardianes de Validación Fail-Fast]
    B -->|Incumple Regla / Dato Inválido| E[Retorno Inmediato de Rechazo]
    B -->|Datos Íntegros y Válidos| C[3. Procesamiento Central y Lógica de Negocio]
    C --> D[4. Empaquetado y Retorno del Resultado]
```

### 🧠 ¿Cómo debe razonar tu mente paso a paso?

1. **Paso 1: Recepción y Limpieza de Entradas (Saneamiento):**
   - **Qué datos recibes:** Trabajos con id único y secuencia de resultados simulados éxito/temporal/permanente; reloj inicial0; máximo3 intentos.
   - **Tu acción lógica preliminar:** Revisa los datos de entrada antes de operar. Si recibes cadenas de texto, elimina espacios accidentales en los extremos y normaliza el formato si la regla lo exige (por ejemplo, mayúsculas/minúsculas). Si recibes colecciones o números, asegúrate de mantener la inmutabilidad de las entradas originales.

2. **Paso 2: Guardianes de Validación (*Fail-Fast*):**
   - Tu lógica debe interrogar los datos en orden estricto antes de realizar cualquier cálculo o transformación pesada:
     - *Condición de negocio:* Un intento por decisión.
     - *Condición de negocio:* Elegir menor instante de elegibilidad y luego id.
     - *Condición de negocio:* Primer temporal pospone2 segundos, segundo4.
     - *Condición de negocio:* Tercer temporal agota.
     - *Condición de negocio:* Éxito/permanente finalizan.
     - *Condición de negocio:* Avanzar reloj simulado si no hay elegibles.
     - *Condición de negocio:* Resultado faltante produce error de simulación para ese trabajo.
   - **Decisión inmediata (*Fail-Fast*):** Si alguna de las condiciones de validez se incumple, detén la ejecución en ese preciso instante. Genera el motivo de rechazo claro y estructurado, evitando procesamientos innecesarios o estados corruptos.

3. **Paso 3: Núcleo de Transformación y Lógica de Dominio:**
   - Una vez superados los guardianes, tienes la certeza de que todos los datos son íntegros y cumplen las restricciones.
   - **El objetivo que debes resolver:** Producir este resultado a partir de las entradas indicadas: **Historial con tiempos, resultado final por trabajo y número de intentos; sin esperas reales**. La solución debe distinguir los resultados válidos de los rechazos previstos.
   - **Tu razonamiento operativo:** Aplica las operaciones, filtrados, acumulaciones o transformaciones requeridas por el negocio sobre los datos ya limpios y validados. Considera especialmente los límites de frontera: *Un trabajo pospuesto no debe impedir atender a otro ya elegible.*.

4. **Paso 4: Empaquetado y Retorno del Resultado:**
   - Prepara la respuesta según el contrato de salida:
     - **En caso de éxito:** Retorna un estado afirmativo (`True`), junto con la estructura de datos procesada (Historial con tiempos, resultado final por trabajo y número de intentos; sin esperas reales.) y el indicador de error en `None`.
     - **En caso de rechazo:** Retorna un estado negativo (`False`), sin datos procesados (`None`), e incluye el mensaje o causa descriptiva del rechazo.

---

## 5. Esqueleto de Diseño Profesional (Sin Implementar)

> [!IMPORTANT]
> **Queda prohibido resolver el ejercicio aquí.** El siguiente bloque define el contrato formal, tipos y documentación para que implementes la lógica completa.

```python
from typing import Any, Dict, List, Optional, Tuple, Union

# Constantes de negocio recomendadas (ejemplo de configuración de límites)
# TODO: Define aquí tus constantes en UPPER_SNAKE_CASE con sus valores límite.

def ejecutar_ejercicio_099(
    instante_elegible: str,
    intento_consumido: int,
    trabajo_finalizado: str
) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    Producir este resultado a partir de las entradas indicadas: **Historial con tiempos, resultado final por trabajo y número de intentos; sin esperas reales**. La solución debe distinguir los resultados válidos de los rechazos previstos.

    Args:
        instante_elegible: Dato de entrada según contrato de negocio.
        intento_consumido: Dato de entrada según contrato de negocio.
        trabajo_finalizado: Dato de entrada según contrato de negocio.

    Returns:
        Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
            - bool: True si la operación fue exitosa y válida; False si fue rechazada.
            - Optional[Dict[str, Any]]: Datos resultantes estructurados, o None en caso de fallo.
            - Optional[str]: Mensaje / causa de rechazo en caso de error, o None en caso de éxito.
    """
    # TODO: El profesional debe implementar la normalización, validaciones y cálculo aquí.
    raise NotImplementedError("Implementación pendiente por el desarrollador.")
```

---

## 6. Matriz de Casos de Prueba (*Test Cases*)

Diseña tus pruebas unitarias (`unittest` o aserciones estructuradas) cubriendo todos estos escenarios:

| ID | Escenario | Entrada | Salida Esperada | Criterio de Aceptación Evaluado |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Caso 1 | `A:temporal,éxito` | `intentos en0 y2.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 2 | Caso 2 | `A:temporal,temporal,temporal` | `0,2,6 y agotado.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 3 | Caso 3 | `B:permanente` | `un intento.` | Cumplimiento del contrato y reglas de negocio asociadas. |

---

## 7. Fundamentos de Python y Buenas Prácticas

### Fundamentos Clave
Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Comparación total, estabilidad y desempates reproducibles.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué son útiles en este ejercicio?
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Hacen reproducibles las prioridades y sus desempates.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Errores Comunes que Debes Evitar
- Dormir el proceso entero cuando solo un trabajo espera.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Recomendaciones de Código Limpio (Clean Code / PEP 8)
- **Evita efectos secundarios (*side effects*):** No alteres colecciones recibidas como parámetros de entrada.
- **Tipado estricto:** Aprovecha las anotaciones de tipos para detectar discrepancias antes de la ejecución.
- **Manejo explícito de ausencia:** Distingue con claridad `None`, `0`, `""` y colecciones vacías `[]`/`{}`.

---

## 8. Consulta Técnica Recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

---

## 9. Preguntas de Autoevaluación y Reflexión Posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A:temporal,éxito →intentos en0 y2**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia hay entre orden de entrada, prioridad de ejecución y estado final?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

---

## 10. Aplicación en el Mundo Real y Reto Adicional

### Aplicación Profesional
Procesadores de trabajo diferido combinan elegibilidad temporal, límites de intentos y atención de otras tareas disponibles. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto Adicional (Opcional)
Permitir cancelar un trabajo pendiente antes de su próximo intento.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
