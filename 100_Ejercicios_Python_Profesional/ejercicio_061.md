# Ejercicio 061 — Consumo de páginas de una API simulada

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_060.md) · [Siguiente](ejercicio_062.md)

---

## 1. Contexto y Propósito del Problema

### Contexto
Un equipo debe reunir resultados de un servicio que entrega páginas enlazadas.

### Situación Operativa
El encargo es **consumo de páginas de una api simulada**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo Principal
Producir este resultado a partir de las entradas indicadas: **Items reunidos, páginas visitadas y estado completo/incompleto**. La solución debe distinguir los resultados válidos de los rechazos previstos.

---

## 2. Especificación del Contrato (Entradas y Salidas)

### Datos de Entrada
Mapa en memoria token→página con items y siguiente token o None; token inicial; items con id y contenido.

### Resultado Esperado
Items reunidos, páginas visitadas y estado completo/incompleto.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de Negocio e Invariantes
- **Regla:** Sin red.
- **Regla:** Recorrer hasta None.
- **Regla:** Token inexistente o repetido detiene con diagnóstico.
- **Regla:** Items repetidos por id conservan primera aparición.
- **Regla:** Mantener orden recibido.
- **Regla:** Devolver resultado parcial marcado incompleto ante fallo.

### Casos Especiales y Límites de Frontera
Una página vacía puede tener una página siguiente.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

---

## 3. Guía de Nomenclatura y Variables Profesionales

Se recomienda definir nombres con alta carga semántica, respetando PEP 8 (`snake_case` para variables y funciones, `UPPER_SNAKE_CASE` para constantes de negocio):

| Variable / Identificador | Tipo Sugerido | Propósito y Semántica |
| :--- | :--- | :--- |
| `token_de_pagina` | `str` | Entidad de dominio: token de página. |
| `items_reunidos` | `int` | Entidad de dominio: items reunidos. |
| `paginas_visitadas` | `str` | Entidad de dominio: páginas visitadas. |
| `estado_de_completitud` | `str` | Entidad de dominio: estado de completitud. |

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
   - **Qué datos recibes:** Mapa en memoria token→página con items y siguiente token o None; token inicial; items con id y contenido.
   - **Tu acción lógica preliminar:** Revisa los datos de entrada antes de operar. Si recibes cadenas de texto, elimina espacios accidentales en los extremos y normaliza el formato si la regla lo exige (por ejemplo, mayúsculas/minúsculas). Si recibes colecciones o números, asegúrate de mantener la inmutabilidad de las entradas originales.

2. **Paso 2: Guardianes de Validación (*Fail-Fast*):**
   - Tu lógica debe interrogar los datos en orden estricto antes de realizar cualquier cálculo o transformación pesada:
     - *Condición de negocio:* Sin red.
     - *Condición de negocio:* Recorrer hasta None.
     - *Condición de negocio:* Token inexistente o repetido detiene con diagnóstico.
     - *Condición de negocio:* Items repetidos por id conservan primera aparición.
     - *Condición de negocio:* Mantener orden recibido.
     - *Condición de negocio:* Devolver resultado parcial marcado incompleto ante fallo.
   - **Decisión inmediata (*Fail-Fast*):** Si alguna de las condiciones de validez se incumple, detén la ejecución en ese preciso instante. Genera el motivo de rechazo claro y estructurado, evitando procesamientos innecesarios o estados corruptos.

3. **Paso 3: Núcleo de Transformación y Lógica de Dominio:**
   - Una vez superados los guardianes, tienes la certeza de que todos los datos son íntegros y cumplen las restricciones.
   - **El objetivo que debes resolver:** Producir este resultado a partir de las entradas indicadas: **Items reunidos, páginas visitadas y estado completo/incompleto**. La solución debe distinguir los resultados válidos de los rechazos previstos.
   - **Tu razonamiento operativo:** Aplica las operaciones, filtrados, acumulaciones o transformaciones requeridas por el negocio sobre los datos ya limpios y validados. Considera especialmente los límites de frontera: *Una página vacía puede tener una página siguiente.*.

4. **Paso 4: Empaquetado y Retorno del Resultado:**
   - Prepara la respuesta según el contrato de salida:
     - **En caso de éxito:** Retorna un estado afirmativo (`True`), junto con la estructura de datos procesada (Items reunidos, páginas visitadas y estado completo/incompleto.) y el indicador de error en `None`.
     - **En caso de rechazo:** Retorna un estado negativo (`False`), sin datos procesados (`None`), e incluye el mensaje o causa descriptiva del rechazo.

---

## 5. Esqueleto de Diseño Profesional (Sin Implementar)

> [!IMPORTANT]
> **Queda prohibido resolver el ejercicio aquí.** El siguiente bloque define el contrato formal, tipos y documentación para que implementes la lógica completa.

```python
from typing import Any, Dict, List, Optional, Tuple, Union

# Constantes de negocio recomendadas (ejemplo de configuración de límites)
# TODO: Define aquí tus constantes en UPPER_SNAKE_CASE con sus valores límite.

def ejecutar_ejercicio_061(
    token_de_pagina: str,
    items_reunidos: int,
    paginas_visitadas: str,
    estado_de_completitud: str
) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    Producir este resultado a partir de las entradas indicadas: **Items reunidos, páginas visitadas y estado completo/incompleto**. La solución debe distinguir los resultados válidos de los rechazos previstos.

    Args:
        token_de_pagina: Dato de entrada según contrato de negocio.
        items_reunidos: Dato de entrada según contrato de negocio.
        paginas_visitadas: Dato de entrada según contrato de negocio.
        estado_de_completitud: Dato de entrada según contrato de negocio.

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
| 1 | Caso 1 | `p1:[A], siguiente p2; p2:[A,B], None` | `A,B, completo.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 2 | Caso 2 | `p1 apunta a p1` | `incompleto por ciclo.` | Cumplimiento del contrato y reglas de negocio asociadas. |
| 3 | Caso 3 | `p1 apunta a ausente` | `parcial incompleto.` | Cumplimiento del contrato y reglas de negocio asociadas. |

---

## 7. Fundamentos de Python y Buenas Prácticas

### Fundamentos Clave
Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Identidad de entidades y organización de datos relacionados.
- Clasificación, propagación y recuperación de fallos.
- Organización del programa y dependencias sustituibles.

### ¿Por qué son útiles en este ejercicio?
- Relacionan identidades con atributos, estados o acumulados consultables.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.
- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.

### Errores Comunes que Debes Evitar
- Terminar al recibir una página sin items aunque tenga continuación.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Recomendaciones de Código Limpio (Clean Code / PEP 8)
- **Evita efectos secundarios (*side effects*):** No alteres colecciones recibidas como parámetros de entrada.
- **Tipado estricto:** Aprovecha las anotaciones de tipos para detectar discrepancias antes de la ejecución.
- **Manejo explícito de ausencia:** Distingue con claridad `None`, `0`, `""` y colecciones vacías `[]`/`{}`.

---

## 8. Consulta Técnica Recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).
- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

---

## 9. Preguntas de Autoevaluación y Reflexión Posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **p1:[A], siguiente p2; p2:[A,B], None →A,B, completo**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué condición indica fin y cuál indica un servicio inconsistente?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

---

## 10. Aplicación en el Mundo Real y Reto Adicional

### Aplicación Profesional
Clientes de servicios paginados deben distinguir final normal, resultados parciales y referencias inconsistentes. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto Adicional (Opcional)
Detectar si un id repetido trae contenido distinto.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
