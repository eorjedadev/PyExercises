## Ejercicio 067 — Verificador Masivo de Hashes Criptográficos en Disco (`BulkHashVerifierApp`)

> [Índice General](../README.md) · [← Ejercicio 066](../ejercicio_066/README.md) · [Ejercicio 068 →](../ejercicio_068/README.md)

### Contexto profesional
En laboratorios de informática forense y auditorías de seguridad informática, los peritos verifican la integridad de lotes de evidencias digitales calculando y comparando hashes criptográficos SHA-256.

### Usuario objetivo
Perito en informática forense o auditor de ciberseguridad.

### Problema
Calcular funciones hash criptográficas sobre archivos de gran tamaño (imágenes de disco, bases de datos) congela la interfaz y puede provocar errores de falta de memoria si se leen completos con `.read()`.

### Objetivo
Desarrollar una aplicación de verificación de integridad criptográfica con `threading`, que calcule hashes SHA-256 leyendo archivos en bloques de 64 KB en segundo plano, compare los hashes contra un archivo de manifiesto esperado (`checksums.sha256`) y reporte el estado de cada archivo (Íntegro en verde / Modificado en rojo) con una barra de progreso.

### Flujo principal
El perito carga un archivo de manifiesto de hashes o selecciona un lote de archivos locales. Presiona 'Verificar Integridad'. Un hilo secundario calcula el hash SHA-256 de cada archivo leyendo en bloques. Conforme procesa cada archivo, actualiza la barra de progreso general y marca en la tabla si el hash coincide exactamente con el valor esperado o si el archivo fue alterado.

### Requisitos funcionales
- Carga de archivos locales mediante `filedialog`.
- Cálculo de hash SHA-256 en hilo de fondo leyendo en chunks de 64 KB (`hashlib.sha256()`).
- Comparación automática contra un hash esperado ingresado por el usuario o cargado desde un archivo de texto.
- Visualización en `ttk.Treeview`: Archivo, Tamaño, Hash Calculado, Hash Esperado, Dictamen ('Íntegro', 'Alterado', 'No Encontrado').
- Barra de progreso determinada que avance archivo por archivo.
- Exportación del informe de auditoría forense a un archivo de texto.

### Requisitos de interfaz
- Treeview amplio con columnas monoespaciadas para los hashes hexadecimales de 64 caracteres.
- Tags de colores: Verde para archivos íntegros, Rojo para archivos alterados o corruptos.
- Panel inferior con el dictamen global de la evidencia (ej. '10 de 10 archivos íntegros').

### Datos
- Ficha forense: archivo, tamano_bytes, hash_calculado, hash_esperado, integro (bool).

### Estado
- Lista de archivos en verificación.
- Progreso porcentual y cola de comunicación.

### Persistencia
Exportación del informe de integridad a archivo TXT en disco.

### Validaciones
- Verificar que los archivos existan y sean legibles antes de intentar procesarlos.
- Hashes esperados deben normalizarse a minúsculas para comparaciones fiables.

### Casos límite
- Archivos de tamaño cero (hash de archivo vacío).
- Archivos gigantescos de varios gigabytes (deben procesarse en streaming sin sobrecargar la RAM).
- Archivos bloqueados por permisos de administrador.

### Manejo de errores
- Capturar `PermissionError` y `FileNotFoundError` registrando el estado del archivo como 'Error de Lectura' sin detener la verificación de los demás.

### Fundamentos de Python relacionados
- Módulo estándar `hashlib` (`hashlib.sha256`).
- Lectura de archivos binarios por bloques con bucle `while chunk := f.read(65536):`.
- Comparación segura de cadenas de hash.

### Conceptos Tkinter relacionados
- Tablas con tipografías monoespaciadas para valores hash extensos.
- Actualización de estados por cola en tareas de procesamiento intensivo de CPU.

### Herramientas para investigar
- Módulo `hashlib` de la biblioteca estándar de Python.
- Lectura eficiente en bloques binarios con el operador morsa (`:=`).

### Diseño de interfaz
¿Cómo asegurarías que la columna del hash SHA-256 (64 caracteres) sea completamente legible sin recortar los extremos de la cadena?

### Diseño de variables
Usa nombres como `hash_tree`, `load_manifest_btn`, `verify_btn`, `progress_bar`, `audit_status_label`, `hash_queue`, `hasher_thread`.

### Antes de programar
1. ¿Por qué es fundamental leer archivos en bloques de bytes (ej. 64 KB) con `hashlib.update(chunk)` en lugar de leer todo el archivo en memoria con `hashlib.sha256(f.read())`?
2. ¿Cómo se normalizan los hashes a minúsculas para evitar falsos positivos de discordancia por mayúsculas?

### Arquitectura
```
ejercicio_067/
├── app.py           # Vistas de auditoría y tabla de hashes
├── hash_worker.py   # Hilo de cálculo criptográfico en chunks binarios
└── manifest_parser.py # Lectura y parseo de archivos checksums estándar
```

### Pruebas mínimas
1. Procesar un archivo con su hash exacto -> Comprobar que calcule el SHA-256 idéntico a la utilidad `sha256sum` y marque 'Íntegro' en verde.
2. Modificar un solo byte del archivo -> Verificar que el dictamen cambie de inmediato a 'Alterado' en rojo.

### Pruebas de error
1. Incluir en la lista un archivo inexistente -> Debe marcar 'No Encontrado' sin colapsar el proceso.

### Experiencia de usuario
Los hashes deben mostrarse con fuente monoespaciada para facilitar la comparación visual entre el calculado y el esperado.

### Explicación posterior
¿Cómo garantiza el patrón de lectura en bloques (chunking) que la aplicación pueda calcular hashes de archivos de varios gigabytes consumiendo una cantidad mínima y constante de memoria RAM?

### Aplicación profesional
Auditorías de evidencia forense digital, verificación de instaladores descargados y comprobación de integridad en copias de seguridad.

### Reto adicional
Añade un selector de algoritmo criptográfico (`Combobox`) para permitir alternar entre SHA-256, SHA-512 y MD5.

---
> [Índice General](../README.md) · [← Ejercicio 066](../ejercicio_066/README.md) · [Ejercicio 068 →](../ejercicio_068/README.md)
