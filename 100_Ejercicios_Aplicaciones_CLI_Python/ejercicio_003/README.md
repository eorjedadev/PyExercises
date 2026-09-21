## Ejercicio 003 — Calculadora de Subredes y Validador CIDR (`ip-calc`)

> [← Ejercicio 002](../ejercicio_002/README.md) · [Índice General](../README.md) · [Ejercicio 004 →](../ejercicio_004/README.md)

### Contexto profesional
Los administradores de redes y arquitectos de infraestructura cloud (AWS VPCs, Azure VNets) necesitan calcular rápidamente rangos de direcciones IP, máscaras de red, direcciones de broadcast y cantidad de hosts útiles antes de desplegar recursos.

### Problema
Se requiere una CLI que reciba una dirección IPv4 en notación CIDR (ej. `192.168.1.0/24`) y entregue el desglose técnico completo de la subred, validando además si una IP secundaria pertenece a dicho rango.

### Usuario objetivo
Ingenieros de redes, administradores de sistemas y DevOps.

### Objetivo
Crear una herramienta de análisis de direccionamiento IPv4 con validación estricta, cálculo binario/decimal y verificación de pertenencia.

### Ejemplo conceptual de uso
```bash
# Análisis general de subred
python ip_calc.py 10.0.4.0/22

# Comprobar si una IP pertenece a la subred
python ip_calc.py 10.0.4.0/22 --contains 10.0.6.50
```

### Requisitos funcionales
- Parsear y validar la notación CIDR.
- Calcular: Máscara de red en formato decimal con puntos, máscara wildcard, dirección de red, dirección de broadcast, primer host útil, último host útil y número total de hosts utilizables.
- Indicar si la IP corresponde a un rango privado (RFC 1918), público, loopback o multicast.
- Si se pasa `--contains <IP>`, evaluar si dicha IP está dentro del rango y devolver mensaje explicativo.

### Requisitos de CLI
- Argumento posicional: notación CIDR (`IPv4/Máscara`).
- Opción opcional: `--contains <IP>` para prueba de pertenencia.
- Exit code 0 en éxito (o si la IP está contenida).
- Exit code 1 si la IP evaluada con `--contains` NO pertenece a la red.
- Exit code 2 si la sintaxis CIDR o IP es inválida.

### Entradas
- Cadena con bloque CIDR.
- Cadena opcional con dirección IP a verificar.

### Salidas
- Tabla formateada en terminal con todas las métricas de red.
- En modo `--contains`: mensaje claro de confirmación o rechazo.

### Persistencia
Sin persistencia.

### Validaciones
- Octetos IPv4 válidos (0 a 255).
- Longitud de prefijo CIDR válida (0 a 32).
- Validación de formato con expresiones regulares o módulo especializado.

### Casos límite
- Prefijos especiales: `/31` (enlaces punto a punto RFC 3021) y `/32` (host individual).
- Prefijo `/0` (la totalidad de internet IPv4).
- IPs con ceros a la izquierda en los octetos.

### Manejo de errores
- `ValueError`: Notación inválida en octeto o máscara.
- STDERR con explicación del error de formato.

### Fundamentos de Python relacionados
- Módulo de la biblioteca estándar `ipaddress` (`ipaddress.IPv4Network`, `ipaddress.IPv4Address`).
- Operaciones a nivel de bits (bitwise AND, OR, XOR, shifts) si se implementa lógica nativa.
- Formateo de cadenas con f-strings.

### Conceptos CLI relacionados
- Uso de exit codes como valor booleano para scripts (0 = True, 1 = False).
- Formateo tabular alineado para visualización en terminal.

### Herramientas o módulos para investigar
- Módulo `ipaddress`.
- Módulo `argparse`.

### Diseño de comandos
¿Debería existir un comando para calcular la intersección o solapamiento entre dos redes (`--overlaps`)?

### Diseño de argumentos
¿Cómo llamarías a un flag para mostrar la salida en formato JSON (`--json`) para consumo de scripts?

### Diseño de variables
`network_cidr`, `network_object`, `netmask_str`, `broadcast_str`, `usable_hosts_count`, `target_ip`.

### Antes de programar
1. ¿Cuántos hosts útiles tiene una subred /24? ¿Por qué se restan 2 direcciones en redes convencionales?
2. ¿Cómo responde `ipaddress.IPv4Network` cuando se le pasa un host con máscara (ej. `192.168.1.50/24`) sin el parámetro `strict=False`?

### Arquitectura
Archivo único estructurado en funciones de cálculo y función `main()`.

### Pruebas mínimas
1. `python ip_calc.py 192.168.1.0/24` -> Debe reportar máscara `255.255.255.0`, 254 hosts útiles, Broadcast `192.168.1.255`.
2. `python ip_calc.py 10.0.0.0/8 --contains 10.254.1.1` -> Debe retornar exit code 0.

### Pruebas de error
1. `python ip_calc.py 192.168.1.300/24` -> Exit code 2 con error descriptivo.
2. `python ip_calc.py 192.168.1.0/35` -> Exit code 2.

### Experiencia de usuario
Diseñar una salida limpia con bordes ASCII o encabezados claros que destaque inmediatamente el rango útil.

### Explicación posterior
Explica la diferencia entre una red estricta y una dirección de interfaz con máscara de subred.

### Aplicación profesional
Automatización en aprovisionamiento de infraestructura con Terraform, Ansible y validación de reglas de firewall.

### Reto adicional
Agregar soporte automático para direcciones IPv6 y prefijos `/64` a `/128`.

---
> [← Ejercicio 002](../ejercicio_002/README.md) · [Índice General](../README.md) · [Ejercicio 004 →](../ejercicio_004/README.md)
