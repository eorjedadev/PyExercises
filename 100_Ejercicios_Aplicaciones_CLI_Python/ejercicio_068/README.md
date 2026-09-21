## Ejercicio 068 — Escáner de Puertos y Captura de Banners de Red (`port-peek`)

> [← Ejercicio 067](../ejercicio_067/README.md) · [Índice General](../README.md) · [Ejercicio 069 →](../ejercicio_069/README.md)

### Contexto profesional
Los administradores de sistemas y auditores de seguridad necesitan escanear rápidamente direcciones IP y rangos de red locales para inventariar puertos abiertos (SSH 22, HTTP 80, HTTPS 443, PostgreSQL 5432, MySQL 3306), capturar los banners de servicio devueltos para identificar versiones de software y detectar servicios no autorizados.

### Problema
Construir una CLI que realice escaneos de puertos TCP rápidos y no bloqueantes usando concurrencia (`ThreadPoolExecutor` o sockets asíncronos), soporte rangos de puertos (ej. `1-1024` o `80,443,5432`), capture el banner de bienvenida del servicio si está disponible, aplique timeouts configurables y exporte los resultados en tabla, JSON o base de datos.

### Usuario objetivo
Administradores de red, auditores de seguridad (SecOps) y DevOps.

### Objetivo
Crear un escáner de puertos TCP concurrente con captura de banners, control de timeouts y salida estructurada.

### Ejemplo conceptual de uso
```bash
# Escanear puertos comunes en un host con captura de banners
python port_peek.py 192.168.1.1 --ports common --banner

# Escanear rango de puertos 1-1000 con 50 hilos concurrentes y timeout de 500ms
python port_peek.py 10.0.0.50 --ports 1-1000 --threads 50 --timeout 0.5 --format json
```

### Requisitos funcionales
- Resolver nombre de host a dirección IP IPv4/IPv6.
- Especificación de puertos: lista separada por comas (`80,443,5432`), rangos (`1-1024`), puerto individual (`22`) o perfiles predefinidos (`--ports common`, `--ports database`, `--ports web`).
- Conexión TCP no bloqueante con timeout configurable por puerto.
- Captura de banners (Banner Grabbing): si el puerto está abierto y se usa `--banner`, enviar un saludo inicial o esperar respuesta para capturar la versión del software (ej. `SSH-2.0-OpenSSH_8.9p1`, `HTTP/1.1 200 OK Server: nginx`).
- Concurrencia configurable mediante `--threads N` (default 20).
- Subcomando o flag para persistir el historial de puertos abiertos en PostgreSQL o SQLite opcional.

### Requisitos de CLI
- Argumento posicional: host o IP objetivo.
- Opción `-p / --ports <PUERTOS>` (default `common`).
- Opción `-t / --threads <N>` (default 20).
- Opción `--timeout <SEG>` (default 1.0).
- Flag `-b / --banner`.
- Opción `--format [table|json|csv]`.
- Exit code 0 si el escaneo concluyó exitosamente, 1 si no se encontraron puertos abiertos, 2 en errores.

### Entradas
- Host/IP objetivo y rangos de puertos.

### Salidas
- Tabla de puertos abiertos, servicio estimado y banner capturado en STDOUT.

### Persistencia
Registro opcional de escaneos en PostgreSQL/SQLite.

### Validaciones
- Validar formato de IP o resolución DNS del hostname.
- Validar que los puertos estén en el rango 1 a 65535.

### Casos límite
- Hosts protegidos por firewall que descartan paquetes silenciosamente (DROP en lugar de REJECT; respetar timeout sin colapsar la velocidad global).
- Puertos que requieren el envío de un payload previo para responder con banner (ej. HTTP requiere `HEAD / HTTP/1.0\r\n\r\n`).
- Escaneo de localhost vs hosts remotos.

### Manejo de errores
- `socket.gaierror` en errores de resolución DNS.
- `socket.timeout` y `ConnectionRefusedError`.

### Fundamentos de Python relacionados
- Módulo estándar `socket` (`socket.socket`, `connect_ex`, `settimeout`).
- Concurrencia con `concurrent.futures.ThreadPoolExecutor`.
- Mapeo de puertos conocidos a nombres de servicio con `socket.getservbyport` o diccionario interno.

### Conceptos CLI relacionados
- Escaneo de red concurrente de alto rendimiento.
- Formateo de inventarios de servicios descubiertos.

### Herramientas o módulos para investigar
- `socket`.
- `concurrent.futures`.
- `ipaddress`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para escanear un bloque de red CIDR completo (ej. `192.168.1.0/24`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para mostrar únicamente los puertos abiertos omitiendo los cerrados (`--open-only`)?

### Diseño de variables
`target_host_ip`, `target_ports_list`, `thread_pool_executor`, `open_ports_results_list`, `captured_service_banner`.

### Antes de programar
1. ¿Por qué `socket.connect_ex((ip, port))` es más limpio que `socket.connect()` para escaneo de puertos (porque devuelve un código de error numérico `0` si tiene éxito en lugar de lanzar una excepción)?
2. ¿Cómo estructurar el worker concurrente para capturar el banner con timeout corto de 1 segundo sin retrasar el escaneo?

### Arquitectura
Motor de escaneo (`scanner_core.py`), extractor de banners (`banner_grabber.py`), catálogo de servicios (`services_db.py`) y CLI.

### Pruebas mínimas
1. Escanear localhost en puertos conocidos (ej. puerto de un servidor local activo) y verificar que reporte el puerto como `OPEN`.
2. Probar con `--banner` y verificar la captura del texto de bienvenida.

### Pruebas de error
1. Pasar un hostname que no existe `host-invalido-xyz.test` -> Exit code 2 con error de DNS.

### Experiencia de usuario
Tabla clara en terminal con columnas: `PUERTO`, `ESTADO`, `SERVICIO ESTIMADO` y `BANNER / VERSIÓN` con colores llamativos.

### Explicación posterior
Explica la diferencia entre escaneo TCP Connect completo (Three-way handshake SYN-SYN/ACK-ACK) y escaneo TCP SYN stealth (half-open scan).

### Aplicación profesional
Auditorías de superficie de ataque, verificación de reglas de firewall y diagnóstico rápido de infraestructura de red.

### Reto adicional
Implementar detección de servicios TLS/SSL en puertos no estándar intentando automáticamente un handshake TLS si la conexión de texto plano falla.

---
> [← Ejercicio 067](../ejercicio_067/README.md) · [Índice General](../README.md) · [Ejercicio 069 →](../ejercicio_069/README.md)
