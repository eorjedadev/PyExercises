## Ejercicio 012 — Panel de Verificación de Requisitos de Hardware (`SysCheckUI`)

> [Índice General](../README.md) · [← Ejercicio 011](../ejercicio_011/README.md) · [Ejercicio 013 →](../ejercicio_013/README.md)

### Contexto profesional
En departamentos de TI corporativos, los técnicos necesitan validar rápidamente si un equipo cumple los requisitos mínimos antes de instalar una suite de software pesada.

### Usuario objetivo
Técnico de soporte de TI o instalador de software corporativo.

### Problema
Los usuarios intentan instalar software en máquinas que no cumplen requisitos de arquitectura, versión de SO o memoria, generando tickets de soporte innecesarios.

### Objetivo
Desarrollar un panel gráfico que inspeccione automáticamente el sistema operativo, arquitectura de CPU y versión de Python, comparándolos contra requisitos mínimos predefinidos y mostrando un dictamen visual (Apto / No Apto).

### Flujo principal
El técnico abre la aplicación. El programa detecta automáticamente las propiedades del sistema operativo y las muestra. El técnico puede presionar 'Auditar Compatibilidad' y el sistema marca con iconos o colores cada ítem (SO, 64-bit, Python >= 3.10) y emite un veredicto general.

### Requisitos funcionales
- Inspección automática de: Sistema Operativo (`platform.system()`), Versión (`platform.release()`), Arquitectura (`platform.architecture()`), Versión de Python (`sys.version_info`).
- Comparación contra una política configurable de requisitos mínimos.
- Mostrar estado individual de cada componente (Cumple en verde / No cumple en rojo).
- Veredicto global: 'Equipo Apto para Instalación' o 'Equipo No Compatible'.
- Botón para copiar el informe de auditoría al portapapeles.

### Requisitos de interfaz
- Tabla o lista estructurada de requisitos vs valores detectados.
- Indicadores cromáticos claros de estado.
- Botón de exportación o copia de diagnóstico.

### Datos
- Diccionario con especificaciones detectadas y diccionario con requisitos mínimos de la política.

### Estado
- Estado de evaluación de cada regla.
- Dictamen global booleano.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Verificar que las versiones se comparen numéricamente y no como cadenas simples (ej. Python 3.10 > 3.9).

### Casos límite
- Ejecución en sistemas no Windows (Linux, macOS) donde los nombres de versiones varían.
- Arquitecturas poco comunes.

### Manejo de errores
- Manejar posibles excepciones al consultar variables del sistema operativo de forma controlada.

### Fundamentos de Python relacionados
- Módulos estándar `platform` y `sys`.
- Comparación de tuplas de versiones (`sys.version_info >= (3, 10)`).
- Formateo de diccionarios en informes de texto.

### Conceptos Tkinter relacionados
- Uso de colores dinámicos en etiquetas (`foreground='green'`, `foreground='red'`).
- Organización modular con `ttk.LabelFrame`.
- Copia de diagnósticos al portapapeles.

### Herramientas para investigar
- Módulo `platform` de la biblioteca estándar.
- Variable `sys.version_info`.

### Diseño de interfaz
¿Cómo diseñarías el panel para que el veredicto general sea lo primero que llame la atención sin saturar la pantalla?

### Diseño de variables
Usa nombres como `os_status_label`, `arch_status_label`, `py_status_label`, `verdict_banner`, `copy_report_btn`.

### Antes de programar
1. ¿Por qué comparar `'3.10' >= '3.9'` como texto daría un resultado falso y cómo se soluciona usando tuplas numéricas?
2. ¿Cómo detectas si el sistema operativo es Windows, Linux o macOS de forma agnóstica?

### Arquitectura
```
ejercicio_012/
├── app.py           # Presentación visual e indicadores
└── sys_inspector.py # Consulta del sistema y lógica de auditoría
```

### Pruebas mínimas
1. Ejecutar en un entorno compatible -> Comprobar que todos los checks salgan en verde y el veredicto sea 'Apto'.
2. Presionar 'Copiar Diagnóstico' -> Validar que el portapapeles contenga el texto estructurado del informe.

### Pruebas de error
1. Simular una política con requisito de Python 3.99 -> Verificar que marque el requisito de Python en rojo y el veredicto global sea 'No Apto'.

### Experiencia de usuario
El veredicto final debe presentarse como un banner prominente con fondo coloreado y texto en negrita.

### Explicación posterior
¿Cómo garantiza la comparación de tuplas en Python una evaluación correcta de versiones de software frente a cadenas de texto?

### Aplicación profesional
Prerrequisitos de instaladores de software, asistentes de onboarding para desarrolladores y herramientas de diagnóstico de helpdesk.

### Reto adicional
Añade la detección del espacio disponible en el disco principal utilizando el módulo `shutil.disk_usage` y valida si cuenta con al menos 10 GB libres.

---
> [Índice General](../README.md) · [← Ejercicio 011](../ejercicio_011/README.md) · [Ejercicio 013 →](../ejercicio_013/README.md)
