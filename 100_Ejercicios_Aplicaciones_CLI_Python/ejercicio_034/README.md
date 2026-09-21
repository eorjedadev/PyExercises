## Ejercicio 034 — Gestor de Alias y Conexiones SSH Config (`ssh-manager`)

> [← Ejercicio 033](../ejercicio_033/README.md) · [Índice General](../README.md) · [Ejercicio 035 →](../ejercicio_035/README.md)

### Contexto profesional
Los administradores de sistemas y DevOps se conectan a decenas de servidores a través de SSH. Mantener el archivo `~/.ssh/config` manualmente con bloques `Host`, `HostName`, `User`, `Port`, `IdentityFile` y configuraciones de salto (`ProxyJump`) se vuelve propenso a errores de formato y duplicación de alias.

### Problema
Construir una CLI que administre el archivo de configuración SSH local, permitiendo añadir hosts, listar conexiones existentes en una tabla limpia, probar conectividad TCP rápida hacia el puerto SSH (`test`), eliminar alias y respaldar el archivo automáticamente antes de cada modificación.

### Usuario objetivo
Administradores de sistemas, ingenieros de redes y desarrolladores backend.

### Objetivo
Crear un gestor y auditor de configuración SSH con backup automático, validación de llaves privadas y pruebas de conectividad.

### Ejemplo conceptual de uso
```bash
# Agregar un nuevo servidor al SSH config
python ssh_manager.py add prod-web1 --host 198.51.100.10 --user ubuntu --key ~/.ssh/prod.pem --port 2222

# Listar todos los servidores configurados
python ssh_manager.py list

# Probar conectividad TCP al puerto SSH de un alias
python ssh_manager.py test prod-web1
```

### Requisitos funcionales
- Parsear y escribir respetando la sintaxis del archivo `~/.ssh/config`.
- Subcomando `add <ALIAS>`: añade un bloque `Host` con opciones: `--host` (HostName), `--user`, `--port` (default 22), `--key` (IdentityFile) y `--proxy` (ProxyJump).
- Subcomando `list`: tabla formateada con alias, dirección IP/hostname, usuario, puerto y llave.
- Subcomando `remove <ALIAS>`: elimina el bloque del host seleccionado.
- Subcomando `test <ALIAS>`: realiza una conexión de socket TCP rápida (timeout 3s) al host y puerto configurados para verificar que el servicio SSH esté alcanzable.
- Realizar un respaldo automático con timestamp (`~/.ssh/config.bak.<TIMESTAMP>`) antes de cualquier modificación destructiva.

### Requisitos de CLI
- Subcomandos: `add`, `list`, `remove`, `test`, `backup`.
- Opción `--config-file <RUTA>` para usar un archivo SSH alternativo.
- Exit code 0 en éxito, 1 si el host no existe o la prueba de conexión falla, 2 en errores.

### Entradas
- Datos de conexión de servidores y nombres de alias.

### Salidas
- Tabla de hosts, confirmaciones de edición y estado de pruebas de red en STDOUT.

### Persistencia
Lectura y modificación del archivo `~/.ssh/config` con backups en disco.

### Validaciones
- Validar que el alias no esté duplicado en `add`.
- Validar que el puerto sea un número entre 1 y 65535.
- Si se especifica una llave privada (`--key`), validar que el archivo exista y tenga permisos seguros.

### Casos límite
- Archivo `~/.ssh/config` que contiene directivas globales o comodines (`Host *`).
- Bloques con comentarios manuales (deben preservarse en la medida de lo posible).
- Archivo `.ssh` o carpeta inexistente (crear con permisos `0700` y `0600` en Unix).

### Manejo de errores
- `PermissionError` al intentar leer/escribir en `~/.ssh`.
- Errores de socket en `test` (`socket.timeout`, `ConnectionRefusedError`).

### Fundamentos de Python relacionados
- Módulo `socket` (`socket.create_connection`) para comprobaciones TCP de red.
- `pathlib.Path` y `shutil.copy2` para copias de seguridad.
- Parsing y manipulación de texto con bloques estructurados.

### Conceptos CLI relacionados
- Gestión segura de archivos sensibles de configuración del usuario.
- Diagnóstico de red integrado en herramientas de gestión de infraestructura.

### Herramientas o módulos para investigar
- `socket`.
- `pathlib`.
- `shutil`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para exportar la lista de servidores a un inventario compatible con Ansible (`--export-ansible`)?

### Diseño de argumentos
¿Cómo permitirías definir variables de reenvío de puertos (Port Forwarding con `-L` o `-R`)?

### Diseño de variables
`ssh_config_path`, `host_entries_list`, `target_alias`, `socket_connection_timeout`, `backup_timestamp_path`.

### Antes de programar
1. ¿Cómo estructurar el parser para agrupar las propiedades bajo su directiva `Host` correspondiente?
2. ¿Por qué es crítico verificar que la carpeta `~/.ssh` tenga permisos estrictos en sistemas Linux/macOS?

### Arquitectura
Parser de SSH (`ssh_config_parser.py`), probador de red (`network_tester.py`) y CLI.

### Pruebas mínimas
1. Agregar un host a un archivo de configuración temporal, listar y verificar que aparezca en la tabla.
2. Ejecutar `remove` y verificar que el bloque sea eliminado limpiamente del archivo.

### Pruebas de error
1. Intentar hacer `test` hacia un host con puerto cerrado -> Exit code 1 informando conexión rechazada/timeout.

### Experiencia de usuario
Tabla clara con colores, confirmaciones explícitas de backups creados y alertas si la llave privada especificada no existe en disco.

### Explicación posterior
Explica la directiva `ProxyJump` de OpenSSH y cómo permite acceder a servidores en redes privadas (bastion/jump host).

### Aplicación profesional
Administración de flotas de servidores, gestión de accesos para equipos de soporte y simplificación de flujos SSH.

### Reto adicional
Implementar un subcomando `connect <ALIAS>` que invoque directamente el binario `ssh` nativo del sistema operativo con el alias seleccionado usando `subprocess.call`.

---
> [← Ejercicio 033](../ejercicio_033/README.md) · [Índice General](../README.md) · [Ejercicio 035 →](../ejercicio_035/README.md)
