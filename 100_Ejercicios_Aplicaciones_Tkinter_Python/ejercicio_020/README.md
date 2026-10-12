## Ejercicio 020 — Solicitud de Reembolso de Gastos de Viaje (`ExpenseClaimApp`)

> [Índice General](../README.md) · [← Ejercicio 019](../ejercicio_019/README.md) · [Ejercicio 021 →](../ejercicio_021/README.md)

### Contexto profesional
En corporativos multinacionales, los consultores y auditores deben presentar solicitudes de reembolso de viáticos adjuntando comprobantes fiscales digitales para su aprobación contable.

### Usuario objetivo
Consultor o empleado que rinde gastos de viaje.

### Problema
Las rendiciones de gastos enviadas sin comprobante adjunto o con importes mal categorizados generan devoluciones continuas por parte de contabilidad.

### Objetivo
Construir un formulario de rendición de gastos con selección de categoría, fecha del gasto, importe con moneda, selector de archivo de comprobante mediante `filedialog` y validación de comprobante adjunto obligatorio.

### Flujo principal
El empleado ingresa el concepto del gasto, monto, categoría (Vuelos, Hotel, Taxis, Comidas) y hace clic en 'Adjuntar Comprobante'. Se abre el explorador del sistema de archivos para elegir un archivo `.pdf`, `.png` o `.jpg`. El sistema valida que el archivo exista, muestra la ruta seleccionada y permite enviar la solicitud tras confirmar.

### Requisitos funcionales
- Campos para: Concepto del Gasto, Categoría (`Combobox`), Fecha del Gasto, Monto.
- Botón 'Adjuntar Comprobante' que invoque `filedialog.askopenfilename` con filtros de extensiones de archivo (`.pdf`, `.png`, `.jpg`).
- Etiqueta que muestre el nombre del archivo seleccionado o 'Ningún archivo adjunto'.
- Validación de que el comprobante sea obligatorio antes de enviar el reembolso.
- Confirmación y agregado a una lista de rendiciones en memoria.

### Requisitos de interfaz
- Formulario ordenado con campo de archivo adjunto visualmente claro.
- Botón de exploración con icono o texto claro de selección.
- Lista o panel inferior que acumule el total de gastos rendidos durante la sesión.

### Datos
- Ficha de gasto: concepto, categoría, fecha, monto (float), ruta del archivo adjunto (`pathlib.Path`).

### Estado
- Ruta del archivo adjunto seleccionado en memoria.
- Acumulado de gastos rendidos en la sesión.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Monto debe ser mayor a 0.
- Debe haberse seleccionado un archivo adjunto existente y con extensión permitida.
- Concepto debe tener al menos 5 caracteres.

### Casos límite
- El usuario abre el diálogo de archivos y cancela la selección (no debe sobreescribir un archivo previamente seleccionado ni provocar error).
- Archivos con nombres extremadamente largos (debe truncarse la visualización para no deformar la ventana).

### Manejo de errores
- Manejar la cancelación del diálogo `filedialog` sin alterar el estado previo.

### Fundamentos de Python relacionados
- Módulo `pathlib.Path` para inspección de rutas y extensiones de archivos.
- Manejo de cadenas para truncar nombres de archivo largos.

### Conceptos Tkinter relacionados
- Módulo `filedialog` (`filedialog.askopenfilename(filetypes=[...])`).
- Acoplamiento de selección de archivos a variables de la interfaz.

### Herramientas para investigar
- Función `filedialog.askopenfilename` y su parámetro `filetypes`.
- Métodos de `pathlib.Path` (`.name`, `.exists()`, `.suffix`).

### Diseño de interfaz
¿Cómo asegurarías que la ruta del archivo adjunto no rompa el ancho de la ventana si es muy extensa?

### Diseño de variables
Usa nombres como `expense_desc_entry`, `category_combo`, `amount_entry`, `attached_file_path`, `file_display_label`, `submit_expense_btn`.

### Antes de programar
1. ¿Qué retorna `askopenfilename` si el usuario hace clic en 'Cancelar'?
2. ¿Por qué es mejor mostrar solo `archivo.name` en la etiqueta de la interfaz en lugar de la ruta absoluta completa?

### Arquitectura
```
ejercicio_020/
├── app.py           # Formulario gráfico y explorador de archivos
└── expense_model.py # Entidad de gasto y validaciones de archivos adjuntos
```

### Pruebas mínimas
1. Llenar campos, adjuntar un archivo `.pdf` y enviar -> Debe confirmar el registro y sumar el monto al total del viaje.
2. Presionar 'Adjuntar' y cancelar -> Debe conservar el estado anterior sin fallos.

### Pruebas de error
1. Intentar enviar sin adjuntar archivo -> Debe indicar que el comprobante fiscal es estrictamente obligatorio.

### Experiencia de usuario
El nombre del archivo adjunto debe aparecer con un indicador visual de confirmación (ej. icono de documento o texto verde).

### Explicación posterior
¿Cómo gestiona `filedialog.askopenfilename` la cancelación por parte del usuario y cómo se debe manejar en el código?

### Aplicación profesional
Portales de rendición de viáticos en empresas multinacionales, sistemas contables y mesas de compras.

### Reto adicional
Añade una validación del tamaño máximo del archivo adjunto (máximo 5 MB) utilizando `os.path.getsize` antes de aceptar la selección.

---
> [Índice General](../README.md) · [← Ejercicio 019](../ejercicio_019/README.md) · [Ejercicio 021 →](../ejercicio_021/README.md)
