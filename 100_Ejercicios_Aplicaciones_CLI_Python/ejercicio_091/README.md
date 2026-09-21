## Ejercicio 091 — Recolector de Evidencias Forenses para Respuesta a Incidentes (`incident-collector`)

> [← Ejercicio 090](../ejercicio_090/README.md) · [Índice General](../README.md) · [Ejercicio 092 →](../ejercicio_092/README.md)

### Contexto profesional
Ante la sospecha de una intrusión o compromiso de seguridad en un servidor de producción (Security Incident Response), los analistas de seguridad deben recopilar evidencias volátiles y no volátiles del sistema (procesos en ejecución, conexiones de red activas, puertos abiertos, sockets crudos, sesiones de usuario, logs recientes, hashes de archivos del sistema) de forma ordenada y preservando la cadena de custodia sin alterar la evidencia.

### Problema
Construir una CLI forense que recolecte artefactos críticos del sistema operativo, calcule hashes SHA256 de cada evidencia capturada, empaquete todo en un archivo comprimido `.tar.gz` firmado, genere un manifiesto de cadena de custodia inmutable y registre el incidente en una base de datos centralizada (PostgreSQL o SQLite opcional).

### Usuario objetivo
Equipos de respuesta a incidentes (CSIRT / SOC), analistas forenses y administradores de sistemas.

### Objetivo
Desarrollar un recolector de evidencias forenses volátiles y estáticas con firma de integridad criptográfica, cadena de custodia y empaquetado seguro.

### Ejemplo conceptual de uso
```bash
# Recopilar evidencia forense completa del sistema ante un incidente
python incident_collector.py collect --case-id "INC-2026-042" --investigator "mario.forensics" --out-dir /secure/evidence

# Verificar la integridad y cadena de custodia de un paquete de evidencia
python incident_collector.py verify /secure/evidence/INC-2026-042_evidence.tar.gz
```

### Requisitos funcionales
- Subcomando `collect`: recopila sistemáticamente artefactos del sistema siguiendo el orden de volatilidad de RFC 3227:
  1. Memoria y procesos: lista de procesos con PID, PPID, usuario, línea de comandos completa, sockets abiertos (`/proc` o `ps`).
  2. Red: conexiones de red activas (`ESTABLISHED`, `LISTEN`, `TIME_WAIT`), tablas de enrutamiento y caché ARP.
  3. Usuarios y sesiones: usuarios conectados actualmente (`who`, `w`), historial de logins (`last`) y llaves SSH autorizadas.
  4. Archivos del sistema: hashes SHA256 de binarios críticos en `/bin`, `/usr/bin`, `/sbin` y tareas de cron programadas.
  5. Logs del sistema: copia de los últimos N megabytes de `/var/log/syslog`, `/var/log/auth.log` o visor de eventos.
- Generar manifiesto de cadena de custodia `manifest.json`: timestamp UTC exacto, caso de investigación, nombre del analista, versión de la herramienta y tabla con hash SHA256 de cada archivo recolectado.
- Empaquetar todo en un archivo comprimido `CASE_ID_evidence.tar.gz` y calcular el hash SHA256 del tarball final.
- Subcomando `verify <TARBALL>`: descomprime en memoria y verifica que ningún archivo haya sido manipulado comparando contra el manifiesto interno.
- Persistencia de metadatos del caso en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `collect`, `verify`, `report`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--case-id <ID>` (obligatorio en `collect`).
- Opción `--investigator <NOMBRE>`.
- Opción `--out-dir <RUTA>` (default `./evidence`).
- Exit code 0 en éxito, 1 si falla la verificación de integridad de la evidencia, 2 en errores.

### Entradas
- Parámetros de caso forense e inspección del sistema operativo.

### Salidas
- Paquete de evidencia firmado en disco y resumen de recolección en STDOUT.

### Persistencia
Creación de archivos `.tar.gz` en disco y guardado de auditoría en PostgreSQL / SQLite.

### Validaciones
- El identificador de caso debe tener formato alfanumérico estricto.
- Comprobar que el directorio de salida tenga suficiente espacio en disco.

### Casos límite
- Procesos ocultos o con nombres falsificados (recolectar directamente desde `/proc` cuando esté disponible).
- Archivos de log bloqueados en escritura.
- Ejecución en entornos multiplataforma (adaptar comandos y fuentes de datos según Linux o Windows).

### Manejo de errores
- `PermissionError` (recolectar todo lo que los privilegios actuales permitan y registrar los artefactos que no pudieron leerse en el informe de excepciones).

### Fundamentos de Python relacionados
- Módulos estándar `tarfile`, `gzip`, `hashlib`.
- Invocación segura de comandos del sistema con `subprocess.run` y lectura de `/proc`.
- Manejo de fechas UTC precisas con `datetime`.
- Persistencia relacional en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Metodología forense digital y preservación de cadena de custodia (Order of Volatility RFC 3227).
- Integridad criptográfica inmutable en herramientas de seguridad.

### Herramientas o módulos para investigar
- `tarfile`.
- `hashlib`.
- `subprocess` y `platform`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para calcular hashes de memoria RAM física si se cuenta con privilegios de root (`--dump-ram`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para cifrar el archivo de evidencia resultante con la llave pública PGP/GPG del equipo de seguridad (`--gpg-recipient security@empresa.com`)?

### Diseño de variables
`forensic_case_identifier`, `investigator_full_name`, `evidence_artifacts_manifest_dict`, `tarball_archive_writer`, `evidence_package_sha256_hash`.

### Antes de programar
1. ¿Por qué el principio de orden de volatilidad (RFC 3227) exige recolectar primero la memoria RAM y conexiones de red antes de recolectar logs de disco?
2. ¿Cómo construir el archivo `tar.gz` en memoria o en disco asegurando que los timestamps de los archivos empaquetados no alteren la reproducibilidad del hash?

### Arquitectura
Recolector de artefactos volátiles (`volatile_collector.py`), recolector de disco (`disk_collector.py`), empaquetador y firmador (`evidence_packager.py`), verificador (`verifier.py`) y CLI.

### Pruebas mínimas
1. Ejecutar `collect --case-id TEST-001`, verificar que se cree el tarball y que dentro contenga los archivos de procesos, red, usuarios y el `manifest.json`.
2. Ejecutar `verify` sobre el tarball generado y comprobar que valide la integridad de todos los archivos.

### Pruebas de error
1. Modificar un byte dentro del tarball y ejecutar `verify` -> Exit code 1 alertando de manipulación de evidencia.

### Experiencia de usuario
Resumen de auditoría forense en terminal: `[✓] Procesos del sistema capturados (142 procesos)`, `[✓] Conexiones de red activas (28 sockets)`, `[✓] Hashes de binarios verificados`, `[✓] Paquete de evidencia generado: INC-042.tar.gz (SHA256: a3f5...)`.

### Explicación posterior
Explica la importancia de la cadena de custodia (Chain of Custody) para que la evidencia digital sea admisible en procesos judiciales o auditorías regulatorias.

### Aplicación profesional
Equipos de respuesta a incidentes de seguridad (IR), análisis forense post-compromiso y respuesta a ransomware.

### Reto adicional
Implementar captura de memoria RAM volátil mediante integración con herramientas nativas del kernel (`/dev/fmem` o `LiME`).

---
> [← Ejercicio 090](../ejercicio_090/README.md) · [Índice General](../README.md) · [Ejercicio 092 →](../ejercicio_092/README.md)
