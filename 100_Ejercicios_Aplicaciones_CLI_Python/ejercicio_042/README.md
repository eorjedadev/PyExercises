## Ejercicio 042 — Bóveda Cifrada de Credenciales y Tokens API (`vault-cli`)

> [← Ejercicio 041](../ejercicio_041/README.md) · [Índice General](../README.md) · [Ejercicio 043 →](../ejercicio_043/README.md)

### Contexto profesional
Los desarrolladores y operadores manejan secretos sensibles (API keys de Stripe, tokens de AWS, contraseñas de bases de datos) que no deben almacenarse en texto plano en archivos `.env` ni en repositorios de Git.

### Problema
Construir una CLI que actúe como bóveda segura de credenciales, solicitando una contraseña maestra interactiva (mediante `getpass` para no mostrar caracteres en pantalla), derivando una llave de cifrado con PBKDF2/Argon2, cifrando y descifrando secretos con AES-GCM o Fernet y persistiendo los datos cifrados en una base de datos relacional (PostgreSQL o SQLite local).

### Usuario objetivo
Desarrolladores, ingenieros de seguridad y DevOps.

### Objetivo
Crear una bóveda de contraseñas con derivación criptográfica de llaves, cifrado simétrico robusto, autenticación segura y persistencia relacional.

### Ejemplo conceptual de uso
```bash
# Inicializar una nueva bóveda con contraseña maestra
python vault_cli.py init

# Guardar un secreto (solicitará la clave maestra de forma oculta)
python vault_cli.py set "AWS_SECRET_ACCESS_KEY" "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" --service "AWS"

# Obtener el secreto descifrado
python vault_cli.py get "AWS_SECRET_ACCESS_KEY"
```

### Requisitos funcionales
- Subcomando `init`: inicializa la bóveda generando una sal criptográfica (`salt`), solicitando la contraseña maestra dos veces y creando la tabla relacional de credenciales.
- Subcomando `set <CLAVE> [VALOR]`: almacena un secreto cifrado con el nombre de clave, categoría/servicio y descripción. Si no se pasa el valor como argumento, solicitarlo de forma oculta.
- Subcomando `get <CLAVE>`: solicita la contraseña maestra, deriva la llave, descifra el secreto y lo emite en STDOUT.
- Subcomando `list`: lista las claves almacenadas, servicios y fechas de modificación (sin mostrar los secretos en texto claro).
- Subcomando `delete <CLAVE>`: elimina un secreto previa confirmación.
- Subcomando `rotate-master-key`: descifra todos los secretos con la contraseña anterior y los recifra con una nueva contraseña maestra en una única transacción atómica.

### Requisitos de CLI
- Subcomandos: `init`, `set`, `get`, `list`, `delete`, `rotate-master-key`.
- Opciones de persistencia: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite local opcional en `~/.vault.db`).
- Flag `--env-export`: emite en formato `export CLAVE=VALOR` para inyección rápida en el shell.
- Exit code 0 en éxito, 1 si la contraseña maestra es incorrecta o la clave no existe, 2 en errores.

### Entradas
- Contraseñas maestras seguras (vía `getpass`), nombres de secreto y valores confidenciales.

### Salidas
- Secretos descifrados, tablas informativas o errores en STDERR.

### Persistencia
Tabla relacional cifrada en PostgreSQL o SQLite conteniendo: `key_name`, `encrypted_payload_bytes`, `nonce_or_iv`, `service`, `updated_at`, `salt_hash`.

### Validaciones
- Comprobar que la contraseña maestra ingresada descifre correctamente un testigo de validación (`canary`). Si la derivación falla, abortar inmediatamente con exit code 1.
- No permitir nombres de clave vacíos ni duplicados.

### Casos límite
- Intento de descifrado con contraseña incorrecta (debe rechazar sin exponer trazas de error criptográfico que ayuden a un atacante).
- Valores de secretos muy largos (certificados SSL completos de varios KB).
- Modificación concurrente de la base de datos.

### Manejo de errores
- Fallo de autenticación / contraseña incorrecta.
- Errores de integridad de datos alterados (tampering detectado en el tag de autenticación GCM).

### Fundamentos de Python relacionados
- Módulo `getpass` (`getpass.getpass()`) para captura segura en terminal sin eco.
- Módulos de criptografía estándar (`hashlib.pbkdf2_hmac`, `secrets`) o librería `cryptography` (`Fernet`, `AESGCM`).
- Conexiones y transacciones en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Captura segura de entradas interactivas confidenciales en terminal.
- Gestión de ciclo de vida de secretos y rotación atómica de llaves maestras.

### Herramientas o módulos para investigar
- `getpass`.
- `hashlib` y `secrets`.
- Librería `cryptography` (o implementación de cifrado).
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `export-all` para generar un archivo de backup cifrado portable?

### Diseño de argumentos
¿Cómo permitirías pasar la contraseña maestra mediante variable de entorno `VAULT_MASTER_KEY` para scripts de automatización no interactivos?

### Diseño de variables
`master_password_str`, `derived_crypto_key`, `cipher_engine`, `encrypted_blob`, `canary_verification_token`.

### Antes de programar
1. ¿Por qué nunca se debe derivar una clave de cifrado sin usar una sal criptográfica (`salt`) de al menos 16 bytes y al menos 100,000 iteraciones de PBKDF2?
2. ¿Cómo diseñar la rotación de clave maestra para que si falla a mitad del proceso se realice un `ROLLBACK` total sin perder ningún secreto?

### Arquitectura
Motor criptográfico (`crypto.py`), repositorio de persistencia (`vault_repository.py`) y CLI (`vault_cli.py`).

### Pruebas mínimas
1. Inicializar bóveda con contraseña de prueba, guardar un secreto `API_KEY=12345` y recuperarlo con `get` verificando el valor exacto.
2. Probar `list` y verificar que el valor secreto no aparezca en ningún lugar de la tabla.

### Pruebas de error
1. Intentar recuperar el secreto ingresando una contraseña maestra incorrecta -> Exit code 1 con mensaje de acceso denegado.

### Experiencia de usuario
La contraseña maestra debe solicitarse limpiamente con prompt `Contraseña Maestra: ` sin imprimir asteriscos ni caracteres.

### Explicación posterior
Explica la diferencia entre cifrado autenticado (AEAD como AES-GCM) y cifrado sin autenticación (como AES-CBC), y por qué el cifrado autenticado previene ataques de manipulación de bits (bit-flipping).

### Aplicación profesional
Gestión de credenciales para scripts de despliegue, herramientas similares a HashiCorp Vault en entornos locales o pequeños equipos.

### Reto adicional
Implementar bloqueo automático de intentos fallidos (ej. bloquear durante 30 segundos tras 3 contraseñas maestras consecutivas incorrectas).

---
> [← Ejercicio 041](../ejercicio_041/README.md) · [Índice General](../README.md) · [Ejercicio 043 →](../ejercicio_043/README.md)
