## Ejercicio 043 — Visor de Reportes con Ventana Secundaria de Previsualización (`ReportPreviewerApp`)

> [Índice General](../README.md) · [← Ejercicio 042](../ejercicio_042/README.md) · [Ejercicio 044 →](../ejercicio_044/README.md)

### Contexto profesional
En departamentos de administración y finanzas, los usuarios generan reportes de cierre de mes y necesitan previsualizarlos en una ventana secundaria de formato limpio antes de exportar o imprimir.

### Usuario objetivo
Analista contable o asistente administrativo.

### Problema
Exportar archivos directamente sin previsualización genera archivos huérfanos con errores en el desglose de datos que deben borrarse manualmente.

### Objetivo
Desarrollar una aplicación generadora de reportes donde el usuario configure los parámetros (Mes, Sucursal, Tipo de Reporte) y presione 'Vista Previa', abriendo una ventana secundaria `Toplevel` no modal con el reporte formateado en un widget `Text` monoespaciado, con opciones de guardado a archivo de texto o cerrado.

### Flujo principal
El usuario elige en la ventana principal la sucursal y el mes. Presiona 'Generar Vista Previa'. Se abre una ventana secundaria que muestra el reporte perfectamente alineado con encabezados, tabla y firmas simuladas. Desde la ventana de vista previa, puede presionar 'Exportar a TXT' para guardar el reporte en disco o cerrarla para ajustar parámetros.

### Requisitos funcionales
- Parámetros de generación en ventana principal: Sucursal (`Combobox`), Periodo/Mes (`Combobox`), Nivel de Detalle (`Radiobutton`: Resumido / Detallado).
- Generación de informe en texto formateado con columnas tabulares alineadas y líneas divisorias (`---`, `===`).
- Ventana secundaria `Toplevel` de previsualización que contenga un widget `Text` de solo lectura (`state='disabled'`) con tipografía monoespaciada (Courier o Consolas).
- Botón dentro de la ventana de vista previa para exportar el texto a archivo `.txt` mediante `filedialog.asksaveasfilename`.
- Capacidad de mantener abierta la vista previa mientras se ajustan parámetros en la principal.

### Requisitos de interfaz
- Ventana principal compacta para selección de parámetros.
- Ventana de previsualización amplia con proporciones similares a una hoja de reporte vertical.
- Tipografía monoespaciada para garantizar alineación perfecta de columnas de texto.

### Datos
- Datos de reporte simulados: ventas por departamento, gastos, utilidad neta.

### Estado
- Parámetros seleccionados en memoria.
- Texto del reporte generado.

### Persistencia
Exportación a archivo TXT en disco (`filedialog.asksaveasfilename`).

### Validaciones
- Verificar que se haya seleccionado sucursal y periodo antes de generar el reporte.

### Casos límite
- Abrir múltiples ventanas de vista previa simultáneas (gestionar si se reutiliza una ventana existente o se abren independientes).
- Cancelar el diálogo de exportación a archivo.

### Manejo de errores
- Manejar la escritura en disco de forma segura notificando éxito o error.

### Fundamentos de Python relacionados
- Formateo de cadenas con alineación fija (`f'{concepto:<30} {monto:>12,.2f}'`).
- Manejo de archivos de texto con context managers.

### Conceptos Tkinter relacionados
- Ventanas secundarias no modales con `Toplevel`.
- Widget `Text` en modo de solo lectura (`state='disabled'`) y cómo habilitarlo temporalmente para insertar texto.
- Uso de fuentes monoespaciadas (`font=('Consolas', 10)`).

### Herramientas para investigar
- Especificadores de alineación y ancho en f-strings de Python (`<`, `>`, `^`).
- Fuentes estándar multiplataforma en Tkinter.

### Diseño de interfaz
¿Por qué es obligatorio utilizar una fuente monoespaciada para reportes tabulares en texto plano y cómo se garantiza su visualización en Windows y Linux?

### Diseño de variables
Usa nombres como `branch_combo`, `period_combo`, `preview_btn`, `preview_window`, `report_text_widget`, `export_txt_btn`.

### Antes de programar
1. ¿Cómo se inserta texto en un widget `Text` que está en `state='disabled'` sin provocar error de Tkinter?
2. ¿Cómo se formatean columnas de texto para que queden perfectamente alineadas usando f-strings de Python?

### Arquitectura
```
ejercicio_043/
├── app.py             # Ventana principal de parámetros
├── preview_window.py  # Ventana Toplevel de previsualización y exportación
└── report_builder.py  # Motor de generación de reportes en texto plano formateado
```

### Pruebas mínimas
1. Seleccionar 'Sucursal Norte' y presionar 'Vista Previa' -> La ventana secundaria debe abrirse con el reporte alineado.
2. Presionar 'Exportar a TXT' en la vista previa -> Debe permitir guardar el archivo y confirmar éxito.

### Pruebas de error
1. Intentar editar el texto dentro de la ventana de vista previa -> Debe estar bloqueado para edición (solo lectura).

### Experiencia de usuario
La ventana de vista previa debe tener un tamaño generoso y barras de desplazamiento vertical y horizontal para inspeccionar reportes extensos.

### Explicación posterior
¿Cómo se manipula la propiedad `state` de un widget `Text` para permitir actualizaciones por código impidiendo la modificación por parte del usuario?

### Aplicación profesional
Generadores de minutas de reunión, estados de cuenta para clientes y reportes de inventario en almacenes.

### Reto adicional
Añade en la ventana de previsualización un selector de tamaño de fuente que permita agrandar o achicar el texto para facilitar la lectura.

---
> [Índice General](../README.md) · [← Ejercicio 042](../ejercicio_042/README.md) · [Ejercicio 044 →](../ejercicio_044/README.md)
