## Ejercicio 093 — Aplicación Empaquetable con PyInstaller y Gestión de Recursos (`DistributableToolApp`)

> [Índice General](../README.md) · [← Ejercicio 092](../ejercicio_092/README.md) · [Ejercicio 094 →](../ejercicio_094/README.md)

### Contexto profesional
En el ciclo final de ingeniería de software, los desarrolladores deben distribuir su aplicación de escritorio a usuarios finales que no tienen Python instalado en sus equipos, empaquetando código, iconos, imágenes y bases de datos en un ejecutable autónomo.

### Usuario objetivo
Ingeniero de release de software o desarrollador de aplicaciones de escritorio.

### Problema
Hardcodear rutas relativas como `'assets/logo.png'` provoca que la aplicación colapse con `FileNotFoundError` una vez empaquetada con PyInstaller debido a la forma en que los recursos se extraen en la carpeta temporal de ejecución.

### Objetivo
Desarrollar una aplicación de escritorio completa con iconos, imágenes y base de datos local que implemente formalmente el patrón de resolución de rutas de recursos para PyInstaller (`sys._MEIPASS`), acompañada de un archivo de especificaciones `.spec` configurado y documentación técnica de empaquetado y distribución multiplataforma.

### Flujo principal
El desarrollador estructura la aplicación con carpetas `assets/` (icono de ventana `.ico`, logo `.png`) y `datos/` (base de datos SQLite de plantilla). Implementa una función utilitaria robusta `resource_path(relative_path)` que detecta si la aplicación se ejecuta como script estándar de Python o congelada dentro de un bundle de PyInstaller. Prueba la app en modo desarrollo y genera el ejecutable independiente.

### Requisitos funcionales
- Función utilitaria de resolución de rutas `resource_path(relative_path)` que verifique si `sys._MEIPASS` está presente.
- Aplicación funcional que cargue un icono de ventana propio (`root.iconbitmap` o `root.iconphoto`), una imagen de cabecera con `PhotoImage` y conecte con una base de datos SQLite embebida.
- Archivo de especificación de PyInstaller (`app.spec`) documentado con listas `datas=[...]` para incluir las carpetas de recursos.
- Estructura limpia de proyecto compatible con estándares PEP 621.
- Guía paso a paso de comandos de compilación para modo consola oculta (`--noconsole` / `--windowed`) y archivo único (`--onefile`).

### Requisitos de interfaz
- Ventana profesional con icono propio en la barra de título de la ventana y en la barra de tareas del sistema operativo.
- Imagen o logo visible en la cabecera.
- Panel que muestre en tiempo real: 'Modo de Ejecución: Desarrollo (Script Python)' o 'Modo de Ejecución: Empaquetado (PyInstaller Frozen)' junto con la ruta base de recursos detectada.

### Datos
- Recursos de la app: icono `.ico` o `.png`, imagen de logo, base de datos SQLite inicial.

### Estado
- Estado de congelamiento de la aplicación (`getattr(sys, 'frozen', False)`).

### Persistencia
Base de datos SQLite local persistida fuera del directorio temporal de PyInstaller.

### Validaciones
- Verificar que la base de datos persistente no se cree dentro de la carpeta temporal `_MEIPASS` (donde se borraría al cerrar el ejecutable).

### Casos límite
- Ejecución en sistemas Windows frente a sistemas Linux (manejo de extensiones `.ico` vs `.png`).
- Antivirus corporativos que marcan ejecutables de PyInstaller como falsos positivos.

### Manejo de errores
- Manejar la ausencia de recursos visuales cargando un estado por defecto si un archivo de imagen no está presente.

### Fundamentos de Python relacionados
- Variable especial `sys._MEIPASS` inyectada por el bootloader de PyInstaller.
- Módulo `pathlib.Path` y `sys.frozen`.
- Comprensión de entornos virtuales y dependencias mínimas.

### Conceptos Tkinter relacionados
- Configuración de iconos de ventana multiplataforma con `root.iconphoto()` e `iconbitmap()`.
- Carga segura de recursos gráficos.

### Herramientas para investigar
- Documentación oficial de PyInstaller (sección 'Bundling data files with a spec file').
- Mecanismo de extracción de PyInstaller en modo `--onefile`.

### Diseño de interfaz
¿Cómo asegurarías que la interfaz informe claramente en qué modo se encuentra ejecutándose para facilitar la depuración antes y después del empaquetado?

### Diseño de variables
Usa nombres como `resource_resolver`, `is_frozen_app`, `bundle_dir_path`, `app_logo_image`, `runtime_mode_label`.

### Antes de programar
1. ¿Por qué una base de datos SQLite NUNCA debe guardarse en la ruta retornada por `sys._MEIPASS` en una aplicación empaquetada con `--onefile`?
2. ¿Cómo se diseña la función `resource_path()` para que funcione de forma transparente tanto con `python main.py` como en el `.exe` compilado?

### Arquitectura
```
ejercicio_093/
├── app.py             # Ventana principal y visualización de modo de ejecución
├── path_utils.py      # Función resource_path compatible con PyInstaller (_MEIPASS)
├── app.spec           # Archivo de especificaciones de empaquetado de PyInstaller
├── assets/
│   ├── app_icon.png   # Icono de la aplicación
│   └── logo.png       # Logo de cabecera
└── datos/
    └── plantilla.db   # Base de datos inicial
```

### Pruebas mínimas
1. Ejecutar `python app.py` en modo script -> Debe mostrar 'Modo: Desarrollo' y cargar el logo e icono correctamente.
2. Simular `sys.frozen = True` -> La función `resource_path` debe resolver las rutas apuntando a la carpeta de bundle temporal.

### Pruebas de error
1. Intentar cargar un recurso con ruta relativa cruda sin `resource_path()` -> Demostrar por qué fallaría en un ejecutable congelado.

### Experiencia de usuario
La aplicación debe sentirse como un software comercial terminado, con identidad visual propia en la barra de tareas y en la ventana.

### Explicación posterior
¿Cómo funciona el ciclo de vida del directorio temporal `sys._MEIPASS` al ejecutar un binario congelado con PyInstaller y por qué requiere una función de resolución de rutas dedicada?

### Aplicación profesional
Distribución comercial de aplicaciones de escritorio a clientes corporativos, herramientas de soporte técnico portátiles en memorias USB y entregables de software llave en mano.

### Reto adicional
Añade una rutina que detecte la carpeta de datos de usuario estándar del sistema operativo (`%APPDATA%` en Windows o `~/.local/share` en Linux) para almacenar allí la base de datos persistente del usuario.

---
> [Índice General](../README.md) · [← Ejercicio 092](../ejercicio_092/README.md) · [Ejercicio 094 →](../ejercicio_094/README.md)
