# Ejercicio 072 — Planificador de ejecución por rondas

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_071.md) · [Siguiente](ejercicio_073.md)

---

## 1. Contexto y Propósito del Problema

### Contexto
Un equipo simula cómo ejecutar tareas dependientes con varios puestos disponibles.

### Situación Operativa
El encargo es **planificador de ejecución por rondas**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo Principal
Producir este resultado a partir de las entradas indicadas: **Tareas por ronda y número de rondas; entrada inválida se rechaza**. La solución debe distinguir los resultados válidos de los rechazos previstos.

---

## 2. Especificación del Contrato (Entradas y Salidas)

### Datos de Entrada
Tareas de duración exacta una ronda, dependencias válidas sin ciclos y capacidad positiva de puestos.

### Resultado Esperado
Tareas por ronda y número de rondas; entrada inválida se rechaza.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de Negocio e Invariantes
- **Regla:** Cada ronda inicia hasta capacidad de tareas disponibles, por id ascendente.
- **Regla:** Solo cuentan dependencias terminadas en rondas anteriores.
- **Regla:** No rellenar un puesto con una tarea liberada dentro de la misma ronda.

### Casos Especiales y Límites de Frontera
Elegibilidad al inicio de ronda es distinta de elegibilidad durante una iteración interna.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

---

## 3. Guía de Nomenclatura y Variables Profesionales

Se recomienda definir nombres con alta carga semántica, respetando PEP 8 (`snake_case` para variables y funciones, `UPPER_SNAKE_CASE` para constantes de negocio):

| Variable / Identificador | Tipo Sugerido | Propósito y Semántica |
| :--- | :--- | :--- |
| `capacidad_de_ejecucion` | `int` | Entidad de dominio: capacidad de ejecución. |
| `tareas_disponibles_al_inicio` | `str` | Entidad de dominio: tareas disponibles al inicio. |
| `ronda` | `str` | Entidad de dominio: ronda. |
| `finalizadas` | `str` | Entidad de dominio: finalizadas. |

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
   - **Qué datos recibes:** Tareas de duración exacta una ronda, dependencias válidas sin ciclos y capacidad positiva de puestos.
   - **Tu acción lógica preliminar:** Revisa los datos de entrada antes de operar. Si recibes cadenas de texto, elimina espacios accidentales en los extremos y normaliza el formato si la regla lo exige (por ejemplo, mayúsculas/minúsculas). Si recibes colecciones o números, asegúrate de mantener la inmutabilidad de las entradas originales.

2. **Paso 2: Guardianes de Validación (*Fail-Fast*):**
   - Tu lógica debe interrogar los datos en orden estricto antes de realizar cualquier cálculo o transformación pesada:
     - *Condición de negocio:* Cada ronda inicia hasta capacidad de tareas disponibles, por id ascendente.
     - *Condición de negocio:* Solo cuentan dependencias terminadas en rondas anteriores.
     - *Condición de negocio:* No rellenar un puesto con una tarea liberada dentro de la misma ronda.
   - **Decisión inmediata (*Fail-Fast*):** Si alguna de las condiciones de validez se incumple, detén la ejecución en ese preciso instante. Genera el motivo de rechazo claro y estructurado, evitando procesamientos innecesarios o estados corruptos.

3. **Paso 3: Núcleo de Transformación y Lógica de Dominio:**
   - Una vez superados los guardianes, tienes la certeza de que todos los datos son íntegros y cumplen las restricciones.
   - **El objetivo que debes resolver:** Producir este resultado a partir de las entradas indicadas: **Tareas por ronda y número de rondas; entrada inválida se rechaza**. La solución debe distinguir los resultados válidos de los rechazos previstos.
   - **Tu razonamiento operativo:** Aplica las operaciones, filtrados, acumulaciones o transformaciones requeridas por el negocio sobre los datos ya limpios y validados. Considera especialmente los límites de frontera: *Elegibilidad al inicio de ronda es distinta de elegibilidad durante una iteración interna.*.

4. **Paso 4: Empaquetado y Retorno del Resultado:**
   - Prepara la respuesta según el contrato de salida:
     - **En caso de éxito:** Retorna un estado afirmativo (`True`), junto con la estructura de datos procesada (Tareas por ronda y número de rondas; entrada inválida se rechaza.) y el indicador de error en `None`.
     - **En caso de rechazo:** Retorna un estado negativo (`False`), sin datos procesados (`None`), e incluye el mensaje o causa descriptiva del rechazo.

---

## 5. Esqueleto de Diseño Profesional (Sin Implementar)

> [!IMPORTANT]
> **Queda prohibido resolver el ejercicio aquí.** El siguiente bloque define el contrato formal, tipos y documentación para que implementes la lógica completa.

```python
from typing import Any, Dict, List, Optional, Tuple, Union

# Constantes de negocio recomendadas (ejemplo de configuración de límites)
# TODO: Define aquí tus constantes en UPPER_SNAKE_CASE con sus valores límite.

def ejecutar_ejercicio_072(
    capacidad_de_ejecucion: int,
    tareas_disponibles_al_inicio: str,
    ronda: str,
    finalizadas: str
) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    Producir este resultado a partir de las entradas indicadas: **Tareas por ronda y número de rondas; entrada inválida se rechaza**. La solución debe distinguir los resultados válidos de los rechazos previstos.

    Args:
        capacidad_de_ejecucion: Dato de entrada según contrato de negocio.
        tareas_disponibles_al_inicio: Dato de entrada según contrato de negocio.
        ronda: Dato de entrada según contrato de negocio.
        finalizadas: Dato de entrada según contrato de negocio.

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
| 1 | Caso 1 | `A,B libres; C depende A; capacidad2` | `ronda1 A,B, ronda2 C.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 2 | Caso 2 | `Capacidad1` | `A,B,C según disponibilidad y orden.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 3 | Caso 3 | `Sin tareas` | `0 rondas.` | Cumplimiento del contrato y reglas de negocio asociadas. |

---

## 7. Fundamentos de Python y Buenas Prácticas

### Fundamentos Clave
Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Identidad de entidades y organización de datos relacionados.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué son útiles en este ejercicio?
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Errores Comunes que Debes Evitar
- Permitir que una tarea y su requisito se ejecuten simultáneamente.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Recomendaciones de Código Limpio (Clean Code / PEP 8)
- **Evita efectos secundarios (*side effects*):** No alteres colecciones recibidas como parámetros de entrada.
- **Tipado estricto:** Aprovecha las anotaciones de tipos para detectar discrepancias antes de la ejecución.
- **Manejo explícito de ausencia:** Distingue con claridad `None`, `0`, `""` y colecciones vacías `[]`/`{}`.

---

## 8. Consulta Técnica Recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

---

## 9. Preguntas de Autoevaluación y Reflexión Posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A,B libres; C depende A; capacidad2 →ronda1 A,B, ronda2 C**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué define la frontera entre una ronda y la siguiente?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

---

## 10. Aplicación en el Mundo Real y Reto Adicional

### Aplicación Profesional
Simuladores de ejecución por lotes distinguen disponibilidad al inicio de una ronda y tareas liberadas después. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto Adicional (Opcional)
Añadir duraciones de varias rondas conservando dependencias.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
