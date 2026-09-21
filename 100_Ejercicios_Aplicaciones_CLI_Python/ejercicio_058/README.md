## Ejercicio 058 — Monitor y Alerta de Expiración de Certificados SSL/TLS (`cert-watch`)

> [← Ejercicio 057](../ejercicio_057/README.md) · [Índice General](../README.md) · [Ejercicio 059 →](../ejercicio_059/README.md)

### Contexto profesional
La expiración accidental de certificados SSL/TLS en sitios web y APIs corporativas provoca caídas críticas de servicio, alertas de seguridad en navegadores y pérdida de confianza de los clientes. Los equipos de infraestructura necesitan verificar continuamente las fechas de vencimiento de sus dominios y la cadena de confianza completa.

### Problema
Construir una CLI que verifique certificados SSL/TLS de una lista de dominios o direcciones IP (soportando puertos personalizados y Server Name Indication / SNI), calcule los días restantes de validez, compruebe la autoridad emisora (Issuer CA), evalúe la cadena de confianza y emita alertas tempranas y reportes en terminal o base de datos.

### Usuario objetivo
Ingenieros de seguridad, SREs y administradores de sistemas.

### Objetivo
Crear un monitor de certificados TLS con sockets seguros nativos, cálculo de vigencia, soporte SNI y códigos de salida para alertamiento.

### Ejemplo conceptual de uso
```bash
# Verificar certificado de un dominio individual
python cert_watch.py check google.com

# Auditar lista de dominios desde un archivo alertando si vencen en menos de 15 días
python cert_watch.py scan --file domains.txt --warning-days 30 --critical-days 15

# Salida estructurada en JSON para ingesta en sistemas de monitoreo
python cert_watch.py check api.ejemplo.com:8443 --format json
```

### Requisitos funcionales
- Realizar apretón de manos TLS (TLS handshake) con soporte de SNI (`server_hostname`).
- Extraer metadatos del certificado: Nombre común (CN), Nombres alternativos del sujeto (SANs), Emisor (Issuer CA), Algoritmo de firma, Versión TLS negociada, Fecha de inicio de validez (`notBefore`) y Fecha de expiración (`notAfter`).
- Calcular días y horas restantes de vigencia a partir del momento actual.
- Niveles de alerta configurables: `OK` (> warning days), `WARNING` (<= warning days), `CRITICAL` (<= critical days o expirado).
- Subcomando `scan`: procesa múltiples dominios en paralelo.
- Persistencia opcional de auditoría en PostgreSQL o SQLite opcional.

### Requisitos de CLI
- Subcomandos: `check`, `scan`.
- Opción `--warning-days <N>` (default 30).
- Opción `--critical-days <N>` (default 14).
- Opción `--timeout <SEG>` (default 5.0).
- Opción `--format [table|json|csv]`.
- Exit code 0 si todos los certificados están OK, 1 si hay certificados en WARNING, 2 si hay certificados en CRITICAL/expirados o errores de conexión.

### Entradas
- Dominios, puertos (ej. `midominio.com:443`) o archivo de texto con lista de dominios.

### Salidas
- Fichas técnicas, tablas de auditoría y JSON en STDOUT.

### Persistencia
PostgreSQL o SQLite opcional para registro histórico de estados de certificados.

### Validaciones
- Validar formato de nombres de dominio y números de puerto (1-65535).
- Validar que `--critical-days` sea menor que `--warning-days`.

### Casos límite
- Certificados autofirmados o con cadena de confianza rota (ofrecer flag `--allow-untrusted` para inspeccionar el certificado sin verificar la CA).
- Certificados ya expirados (calcular días de retraso en negativo).
- Servidores que requieren autenticación mTLS de cliente.

### Manejo de errores
- `ssl.SSLCertVerificationError`.
- `socket.timeout` y `socket.gaierror` (errores de DNS o conexión rechazada).

### Fundamentos de Python relacionados
- Módulo estándar `ssl` (`ssl.create_default_context`, `SSLContext.wrap_socket`).
- Módulo estándar `socket`.
- Módulo `datetime` para análisis de fechas ASN.1/RFC 5280.
- Concurrencia con `ThreadPoolExecutor` para escaneos masivos.

### Conceptos CLI relacionados
- Manejo de protocolos criptográficos y sockets de red en terminal.
- Calibración de umbrales de alerta y códigos de retorno.

### Herramientas o módulos para investigar
- `ssl`.
- `socket`.
- `datetime`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para inspeccionar los certificados de un archivo local en disco (`.crt` o `.pem`) además de conexiones de red?

### Diseño de argumentos
¿Cómo nombrarías la opción para verificar si el nombre del host consultado coincide con los SANs del certificado (`--verify-hostname`)?

### Diseño de variables
`tls_ssl_context`, `tls_wrapped_socket`, `certificate_dict`, `expiration_datetime_utc`, `remaining_days_int`, `alert_status_enum`.

### Antes de programar
1. ¿Por qué es fundamental pasar el parámetro `server_hostname` al envolver el socket con TLS para soportar SNI en servidores que alojan múltiples dominios en la misma IP?
2. ¿Cómo parsear el formato de fecha estándar de certificados TLS (`%b %d %H:%M:%S %Y %Z`, ej. `May 15 12:00:00 2026 GMT`) a un objeto `datetime` con zona horaria UTC?

### Arquitectura
Cliente TLS (`tls_client.py`), parser de certificados (`cert_parser.py`), evaluador de alertas (`alert_engine.py`) y CLI.

### Pruebas mínimas
1. Consultar un dominio público con certificado válido y verificar que reporte el emisor y días restantes > 0.
2. Probar `--critical-days 9999` y verificar que retorne exit code 2 por umbral forzado.

### Pruebas de error
1. Consultar un host con puerto cerrado -> Exit code 2 con error de conexión claro.

### Experiencia de usuario
Tabla visual clara con colores: Verde para > 30 días, Amarillo para 15-30 días, Rojo brillante para < 15 días o expirados.

### Explicación posterior
Explica la estructura de una cadena de certificados (Certificado de Hoja -> Certificado Intermedio -> Certificado Raíz) y la función de las listas de revocación (CRL/OCSP).

### Aplicación profesional
Monitoreo preventivo en pipelines de CI/CD, tareas de cron en operaciones y tableros de seguridad.

### Reto adicional
Detectar y alertar sobre el uso de protocolos TLS obsoletos e inseguros (TLS 1.0 y TLS 1.1) durante el handshake.

---
> [← Ejercicio 057](../ejercicio_057/README.md) · [Índice General](../README.md) · [Ejercicio 059 →](../ejercicio_059/README.md)
