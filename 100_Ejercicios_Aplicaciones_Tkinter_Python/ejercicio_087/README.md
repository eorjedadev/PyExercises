## Ejercicio 087 — Sistema de Autenticación Local con Bitácora Técnica (`SecureAuthAuditApp`)

> [Índice General](../README.md) · [← Ejercicio 086](../ejercicio_086/README.md) · [Ejercicio 088 →](../ejercicio_088/README.md)

### Contexto profesional
En estaciones de trabajo compartidas de instituciones de salud o auditoría fiscal, las aplicaciones locales requieren autenticación de operadores con hashing seguro de contraseñas y un registro de auditoría estricto de accesos exitosos y fallidos.

### Usuario objetivo
Operador de sistema o auditor de seguridad informática.

### Problema
Guardar contraseñas en texto plano o no registrar intentos de acceso fallidos expone el sistema a ataques de fuerza bruta y viola normativas de protección de datos.

### Objetivo
Construir una pantalla de autenticación local profesional con `Toplevel`, hashing criptográfico de contraseñas mediante `hashlib.scrypt` (o `hashlib.sha256` con sal aleatoria), bloqueo temporal de cuenta tras 3 intentos fallidos consecutivos y registro de bitácora técnica estructurada con el módulo estándar `logging` hacia un archivo rotativo `auditoria_acceso.log`.

### Flujo principal
El usuario inicia la aplicación. Se presenta la ventana modal de login. Ingresa su nombre de usuario y contraseña (con caracteres ocultos con asteriscos `*`). La aplicación recupera la sal y el hash almacenados, calcula el hash de la entrada y los compara de forma segura (`hmac.compare_digest`). Si coincide, la modal se cierra, se registra el éxito en el log y se abre la ventana principal. Si falla 3 veces seguidas, la cuenta se bloquea por 60 segundos y se estampa una alerta crítica en la bitácora.

### Requisitos funcionales
- Sistema de autenticación con usuarios de prueba almacenados con sal (`salt`) y hash seguro.
- Hashing mediante `hashlib.scrypt` o `hashlib.pbkdf2_hmac`.
- Comparación segura contra ataques de temporización utilizando `hmac.compare_digest`.
- Contador de intentos fallidos: al llegar a 3 fallos consecutivos, bloquear el login por 60 segundos mediante un temporizador regresivo con `.after()`.
- Bitácora técnica estructurada utilizando el módulo estándar `logging` con marcas de tiempo, nivel (`INFO`, `WARNING`, `CRITICAL`), usuario y resultado del intento.
- Ventana modal de login con campos de usuario y contraseña con máscara (`show='*'`).
- Ventana principal que solo se hace visible si la autenticación fue exitosa.

### Requisitos de interfaz
- Ventana modal de login sobria, centrada y sin bordes superfluos.
- Campo de contraseña con botón para alternar visibilidad (mostrar/ocultar contraseña).
- Banner de cuenta bloqueada con temporizador regresivo visible en caso de sobrepasar intentos.

### Datos
- Credencial: usuario, salt_hex, hash_hex, intentos_fallidos, bloqueado_hasta.
- Log: timestamp, nivel, mensaje, ip/host.

### Estado
- Contador de intentos fallidos en memoria.
- Estado de bloqueo temporal.
- Usuario autenticado activo.

### Persistencia
Archivo de bitácora técnica rotativo (`logs/auditoria_acceso.log`) y archivo de usuarios estructurado.

### Validaciones
- Usuario y contraseña obligatorios.
- No permitir intentos de login mientras el bloqueo temporal esté activo.

### Casos límite
- Intentar forzar el login cerrando la ventana modal con la 'X' (la aplicación completa debe abortar sin abrir la ventana principal).
- Usuario inexistente (debe procesar el tiempo de hash para evitar ataques de enumeración por temporización).

### Manejo de errores
- Capturar fallos de autenticación registrando en nivel `WARNING` y bloqueos en nivel `CRITICAL` en la bitácora técnica.

### Fundamentos de Python relacionados
- Módulo estándar `logging` (`getLogger`, `FileHandler`, `Formatter`).
- Módulo estándar `hashlib` y función `hmac.compare_digest`.
- Generación de sales criptográficas con `secrets.token_bytes()`.

### Conceptos Tkinter relacionados
- Control de flujo de inicio de aplicación donde la ventana principal permanece oculta (`withdraw()`) hasta que la modal de login retorne éxito.
- Temporizadores con `after()` para el bloqueo regresivo.

### Herramientas para investigar
- Módulo `logging` de Python y rotación básica de logs.
- Función `hmac.compare_digest()` para prevenir ataques de temporización.

### Diseño de interfaz
¿Cómo asegurarías que la ventana principal permanezca completamente oculta y no visible en la barra de tareas hasta que el login sea exitoso?

### Diseño de variables
Usa nombres como `login_dialog`, `user_entry`, `pass_entry`, `auth_service`, `failed_attempts_counter`, `lockout_timer_label`, `audit_logger`.

### Antes de programar
1. ¿Por qué se debe ocultar la ventana principal con `root.withdraw()` al arrancar antes de abrir la modal de autenticación?
2. ¿Por qué es fundamental usar `hmac.compare_digest()` en lugar de `hash_a == hash_b` para contrastar hashes criptográficos?

### Arquitectura
```
ejercicio_087/
├── app.py             # Flujo de inicio, ventana principal y control modal
├── login_dialog.py    # Ventana modal de login con campos enmascarados
├── auth_service.py    # Lógica de hashing seguro, salting y control de bloqueos
├── audit_logger.py    # Configuración de bitácora estructurada con logging
└── logs/
    └── auditoria_acceso.log # Archivo de log técnico generado
```

### Pruebas mínimas
1. Ingresar credenciales correctas -> La modal debe cerrarse, abrirse la ventana principal y registrarse `'Login exitoso para usuario: operador1'` en `auditoria_acceso.log`.
2. Verificar que el log tenga formato estructurado con fecha, nivel e información.

### Pruebas de error
1. Fallar la contraseña 3 veces consecutivas -> La interfaz debe bloquearse por 60 segundos, deshabilitar el botón y registrar evento `CRITICAL` en el log.

### Experiencia de usuario
El campo de contraseña debe tener la tecla `Enter` enlazada para enviar el formulario rápidamente sin requerir hacer clic en el botón.

### Explicación posterior
¿Cómo coordina `root.withdraw()` y `root.deiconify()` el flujo seguro de pantallas de autenticación previa en Tkinter?

### Aplicación profesional
Estaciones de trabajo médicas (sistemas hospitalarios), terminales de caja registradora seguras y consolas administrativas de soporte.

### Reto adicional
Añade en la ventana principal un visor de bitácora técnica exclusivo para administradores que lea y muestre las últimas 20 líneas de `auditoria_acceso.log`.

---
> [Índice General](../README.md) · [← Ejercicio 086](../ejercicio_086/README.md) · [Ejercicio 088 →](../ejercicio_088/README.md)
