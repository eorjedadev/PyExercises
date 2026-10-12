# Ejercicio 006 — Duración de una visita técnica

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_005.md) · [Siguiente](ejercicio_007.md)

---

## 1. Contexto y Propósito del Problema

### Contexto
Un taller registra cuánto duró una visita que comenzó y terminó el mismo día.

### Situación Operativa
El encargo es **duración de una visita técnica**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo Principal
Producir este resultado a partir de las entradas indicadas: **Duración en minutos y presentación en horas y minutos**. La solución debe distinguir los resultados válidos de los rechazos previstos.

---

## 2. Especificación del Contrato (Entradas y Salidas)

### Datos de Entrada
Hora y minuto de inicio y de fin como cuatro enteros.

### Resultado Esperado
Duración en minutos y presentación en horas y minutos.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de Negocio e Invariantes
- **Regla:** Horas de 0 a 23.
- **Regla:** Minutos de 0 a 59.
- **Regla:** Fin no anterior a inicio.
- **Regla:** Duración cero permitida.
- **Regla:** No se cruzan días.

### Casos Especiales y Límites de Frontera
Un minuto fuera de rango no se corrige automáticamente.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

---

## 3. Guía de Nomenclatura y Variables Profesionales

Se recomienda definir nombres con alta carga semántica, respetando PEP 8 (`snake_case` para variables y funciones, `UPPER_SNAKE_CASE` para constantes de negocio):

| Variable / Identificador | Tipo Sugerido | Propósito y Semántica |
| :--- | :--- | :--- |
| `hora_de_inicio` | `str` | Entidad de dominio: hora de inicio. |
| `minuto_de_fin` | `str` | Entidad de dominio: minuto de fin. |
| `duracion_total` | `int` | Entidad de dominio: duración total. |
| `horas_completas` | `str` | Entidad de dominio: horas completas. |

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
   - **Qué datos recibes:** Hora y minuto de inicio y de fin como cuatro enteros.
   - **Tu acción lógica preliminar:** Revisa los datos de entrada antes de operar. Si recibes cadenas de texto, elimina espacios accidentales en los extremos y normaliza el formato si la regla lo exige (por ejemplo, mayúsculas/minúsculas). Si recibes colecciones o números, asegúrate de mantener la inmutabilidad de las entradas originales.

2. **Paso 2: Guardianes de Validación (*Fail-Fast*):**
   - Tu lógica debe interrogar los datos en orden estricto antes de realizar cualquier cálculo o transformación pesada:
     - *Condición de negocio:* Horas de 0 a 23.
     - *Condición de negocio:* Minutos de 0 a 59.
     - *Condición de negocio:* Fin no anterior a inicio.
     - *Condición de negocio:* Duración cero permitida.
     - *Condición de negocio:* No se cruzan días.
   - **Decisión inmediata (*Fail-Fast*):** Si alguna de las condiciones de validez se incumple, detén la ejecución en ese preciso instante. Genera el motivo de rechazo claro y estructurado, evitando procesamientos innecesarios o estados corruptos.

3. **Paso 3: Núcleo de Transformación y Lógica de Dominio:**
   - Una vez superados los guardianes, tienes la certeza de que todos los datos son íntegros y cumplen las restricciones.
   - **El objetivo que debes resolver:** Producir este resultado a partir de las entradas indicadas: **Duración en minutos y presentación en horas y minutos**. La solución debe distinguir los resultados válidos de los rechazos previstos.
   - **Tu razonamiento operativo:** Aplica las operaciones, filtrados, acumulaciones o transformaciones requeridas por el negocio sobre los datos ya limpios y validados. Considera especialmente los límites de frontera: *Un minuto fuera de rango no se corrige automáticamente.*.

4. **Paso 4: Empaquetado y Retorno del Resultado:**
   - Prepara la respuesta según el contrato de salida:
     - **En caso de éxito:** Retorna un estado afirmativo (`True`), junto con la estructura de datos procesada (Duración en minutos y presentación en horas y minutos.) y el indicador de error en `None`.
     - **En caso de rechazo:** Retorna un estado negativo (`False`), sin datos procesados (`None`), e incluye el mensaje o causa descriptiva del rechazo.

---

## 5. Esqueleto de Diseño Profesional (Sin Implementar)

> [!IMPORTANT]
> **Queda prohibido resolver el ejercicio aquí.** El siguiente bloque define el contrato formal, tipos y documentación para que implementes la lógica completa.

```python
from typing import Any, Dict, List, Optional, Tuple, Union

# Constantes de negocio recomendadas (ejemplo de configuración de límites)
# TODO: Define aquí tus constantes en UPPER_SNAKE_CASE con sus valores límite.

def procesar_duracion_de_una_visita_tecnica(
    hora_de_inicio: str,
    minuto_de_fin: str,
    horas_completas: str
) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    Producir este resultado a partir de las entradas indicadas: **Duración en minutos y presentación en horas y minutos**. La solución debe distinguir los resultados válidos de los rechazos previstos.

    Args:
        hora_de_inicio: Dato de entrada según contrato de negocio.
        minuto_de_fin: Dato de entrada según contrato de negocio.
        horas_completas: Dato de entrada según contrato de negocio.

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
| 1 | Caso 1 | `09:45 a 11:10` | `85 minutos, 1 h 25 min.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 2 | Caso 2 | `10:00 a 10:00` | `0.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 3 | Caso 3 | `23:50 a 00:10` | `rechazo.` | Cumplimiento del contrato y reglas de negocio asociadas. |

---

## 7. Fundamentos de Python y Buenas Prácticas

### Fundamentos Clave
- **Enteros, operadores aritméticos y formato de resultados**. Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.
- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.

### ¿Por qué son útiles en este ejercicio?
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.

### Errores Comunes que Debes Evitar
- Restar por separado horas y minutos sin considerar su relación.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Recomendaciones de Código Limpio (Clean Code / PEP 8)
- **Evita efectos secundarios (*side effects*):** No alteres colecciones recibidas como parámetros de entrada.
- **Tipado estricto:** Aprovecha las anotaciones de tipos para detectar discrepancias antes de la ejecución.
- **Manejo explícito de ausencia:** Distingue con claridad `None`, `0`, `""` y colecciones vacías `[]`/`{}`.

---

## 8. Consulta Técnica Recomendada

- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

---

## 9. Preguntas de Autoevaluación y Reflexión Posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **09:45 a 11:10 → 85 minutos, 1 h 25 min**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué representación permite comparar dos horas sin confundir sus partes?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

---

## 10. Aplicación en el Mundo Real y Reto Adicional

### Aplicación Profesional
Partes de trabajo convierten horas de entrada en duraciones comprobables con una unidad interna coherente. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto Adicional (Opcional)
Aceptar visitas que terminen al día siguiente con una marca explícita.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
