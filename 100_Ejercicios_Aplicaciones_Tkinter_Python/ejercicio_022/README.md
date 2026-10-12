## Ejercicio 022 — Inspección y Control de Calidad de Lotes (`QualityInspectionApp`)

> [Índice General](../README.md) · [← Ejercicio 021](../ejercicio_021/README.md) · [Ejercicio 023 →](../ejercicio_023/README.md)

### Contexto profesional
En líneas de envasado y manufactura de alimentos, los inspectores de control de calidad evalúan muestras de lotes de producción para dictaminar si el lote es liberado o retenido.

### Usuario objetivo
Inspector de calidad o analista de aseguramiento de calidad (QA).

### Problema
El cálculo incorrecto de los porcentajes de defectos en libretas de campo genera la liberación indebida de lotes no conformes o retrasos en auditorías.

### Objetivo
Desarrollar una aplicación de dictamen de lotes industriales donde se registre el tamaño del lote, tamaño de la muestra inspeccionada y conteo de defectos por tipo (Críticos, Mayores, Menores), calculando el índice de defectos y bloqueando la edición tras emitir el dictamen.

### Flujo principal
El inspector ingresa código de lote, tamaño de muestra y cantidad de defectos detectados. El sistema calcula el porcentaje ponderado de defectos. Si los defectos críticos son mayores a 0 o el porcentaje total supera el 2.5%, el dictamen es 'LOTE RECHAZADO' (rojo); en caso contrario, 'LOTE APROBADO' (verde). Al dictaminar, el formulario se bloquea para evitar manipulaciones.

### Requisitos funcionales
- Entradas: Código de Lote, Tamaño del Lote, Tamaño de Muestra inspeccionada.
- Contadores de defectos: Críticos, Mayores y Menores.
- Cálculo automático de Porcentaje de Defectos sobre la muestra.
- Regla de aceptación: 0 defectos críticos y tasa ponderada <= 2.5%.
- Dictamen formal: 'Aprobado para Distribución' o 'Retenido por Calidad'.
- Botón para dictaminar que bloquee todos los campos en modo solo lectura (`state='disabled'`).
- Botón de 'Nueva Inspección' con confirmación para reiniciar.

### Requisitos de interfaz
- Banner de dictamen grande y coloreado en la parte inferior.
- Campos de defectos organizados en columnas claras.
- Botón de dictamen prominente.

### Datos
- Ficha de inspección: lote, tamaño, muestra, defectos por tipo, tasa resultante, veredicto final.

### Estado
- Estado del dictamen: 'PENDIENTE', 'APROBADO', 'RECHAZADO'.
- Estado de bloqueo de los campos de entrada.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Tamaño de muestra debe ser mayor a 0 y menor o igual al tamaño del lote.
- La suma de defectos no puede superar el tamaño de la muestra.

### Casos límite
- Tamaño de muestra igual a 0 (evitar división por cero).
- Defectos negativos (no permitidos).

### Manejo de errores
- Prevenir divisiones por cero validando que la muestra sea estrictamente mayor a cero.

### Fundamentos de Python relacionados
- Fórmulas de tasas porcentuales y ponderadas.
- Recorrido y bloqueo masivo de widgets mediante listas o jerarquía de contenedores.

### Conceptos Tkinter relacionados
- Iteración sobre widgets hijos de un contenedor (`frame.winfo_children()`) para modificar su estado en lote.
- Bloqueo y desbloqueo de formularios.

### Herramientas para investigar
- Método `.winfo_children()` en contenedores de Tkinter.
- Estándares militares de muestreo de calidad (AQL simple).

### Diseño de interfaz
¿Cómo diseñarías el panel para que el dictamen final sea completamente visible y no pueda confundirse con un estado de edición activo?

### Diseño de variables
Usa nombres como `lot_code_entry`, `sample_size_entry`, `critical_defects_entry`, `verdict_banner_label`, `finalize_btn`.

### Antes de programar
1. ¿Cómo se bloquean todos los campos de entrada de un `Frame` usando `winfo_children()` sin tener que escribir `entry.config(state='disabled')` para cada uno?
2. ¿Cuál es el criterio para considerar un lote como rechazado?

### Arquitectura
```
ejercicio_022/
├── app.py           # Formulario de inspección y bloqueo de controles
└── quality_core.py  # Reglas de dictamen AQL y cálculo de defectos
```

### Pruebas mínimas
1. Muestra 100, Defectos Críticos 0, Mayores 1 -> Tasa 1.0%, dictamen debe ser 'LOTE APROBADO' en verde.
2. Presionar 'Finalizar Dictamen' -> Todos los campos deben quedar inhabilitados para edición.

### Pruebas de error
1. Muestra 100, Defectos Críticos 1 -> Dictamen debe ser 'LOTE RECHAZADO' en rojo inmediatamente a pesar de tener 1 solo defecto.

### Experiencia de usuario
El bloqueo del formulario debe ser visualmente claro (campos atenuados) para evitar que el usuario intente escribir sobre un dictamen cerrado.

### Explicación posterior
¿Cómo optimiza `winfo_children()` el mantenimiento de formularios extensos cuando se requiere bloquear o limpiar grupos enteros de componentes?

### Aplicación profesional
Sistemas de control de piso de planta en industrias farmacéuticas, automotrices y alimentarias.

### Reto adicional
Añade un campo de firma digital con el nombre del inspector responsable antes de permitir el bloqueo definitivo del dictamen.

---
> [Índice General](../README.md) · [← Ejercicio 021](../ejercicio_021/README.md) · [Ejercicio 023 →](../ejercicio_023/README.md)
