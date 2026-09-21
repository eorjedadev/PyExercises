## Ejercicio 018 — Redactor y Enmascarador de Secretos en Logs (`log-redact`)

> [← Ejercicio 017](../ejercicio_017/README.md) · [Índice General](../README.md) · [Ejercicio 019 →](../ejercicio_019/README.md)

### Contexto profesional
Para cumplir con regulaciones como GDPR, PCI-DSS y SOC2, las organizaciones deben evitar que información confidencial (números de tarjeta de crédito, tokens JWT, llaves privadas RSA, passwords en URLs) quede expuesta en texto claro en archivos de log compartidos o servicios centralizados.

### Problema
Construir una CLI de alto rendimiento que analice flujos de texto o archivos de log, detecte patrones de datos sensibles mediante expresiones regulares y reglas configurables, y los reemplace por máscaras seguras (ej. `[REDACTED-JWT]`, `****-****-****-1234`).

### Usuario objetivo
Ingenieros de seguridad (SecOps), DevOps y desarrolladores.

### Objetivo
Crear un motor de sanitización de texto con reglas regex predefinidas, archivo de configuración personalizable y procesamiento en streaming.

### Ejemplo conceptual de uso
```bash
# Sanitizar un archivo de logs usando reglas predeterminadas
python log_redact.py production.log -o production_clean.log

# Procesar flujo continuo con reglas personalizadas en YAML/JSON
cat live_stream.log | python log_redact.py --rules security_rules.json
```

### Requisitos funcionales
- Reglas integradas por defecto para detectar: Tarjetas de crédito (con validación de algoritmo Luhn), Tokens JWT (`eyJ...`), Llaves privadas PEM (`-----BEGIN...`), Contraseñas en query strings (`password=...`), Direcciones de correo electrónico (opcional).
- Soportar archivo de reglas externo (`--rules <FILE>`) en JSON para definir nuevos patrones y etiquetas de reemplazo.
- Modo de máscara completa (`[REDACTED]`) o máscara parcial (`****-****-****-5678` para tarjetas).
- Estadísticas de redacción al finalizar el procesamiento (emitidas a STDERR para no ensuciar STDOUT).

### Requisitos de CLI
- Argumento posicional opcional: archivo de log (lee STDIN si se omite).
- Opción `-r / --rules <FILE>`: reglas personalizadas.
- Opción `-o / --output <FILE>`: archivo de salida.
- Flag `--stats`: muestra recuento de patrones enmascarados en STDERR.
- Exit code 0 en éxito, 1 si el archivo de reglas es inválido, 2 en errores de archivo.

### Entradas
- Archivo de log o flujo STDIN.
- Archivo de reglas opcional.

### Salidas
- Flujo sanitizado en STDOUT o archivo.
- Resumen estadístico en STDERR.

### Persistencia
Escritura de archivo sanitizado si se especifica `-o`.

### Validaciones
- Validar la sintaxis de las expresiones regulares cargadas desde el archivo de reglas.
- Comprobar que el archivo de reglas tenga la estructura esperada.

### Casos límite
- Tarjetas de crédito separadas por espacios, guiones o continuas.
- Tokens extremadamente largos que abarcan múltiples fragmentos.
- Falsos positivos en identificadores numéricos que parecen tarjetas pero no pasan el algoritmo Luhn.

### Manejo de errores
- `re.error` en reglas personalizadas.
- Errores de lectura de configuración.

### Fundamentos de Python relacionados
- Módulo `re`.
- Implementación del algoritmo Luhn en Python para filtrado de tarjetas.
- Módulo `json` o parser simple de reglas.
- Uso de `sys.stderr` para telemetría independiente.

### Conceptos CLI relacionados
- Separación de canal de datos (STDOUT) y canal de métricas/diagnóstico (STDERR).
- Configuración desacoplada en archivos externos.

### Herramientas o módulos para investigar
- `re`.
- `json`.
- `sys.stderr` y `argparse`.

### Diseño de comandos
¿Cómo diseñarías un subcomando `test-rules` para verificar si un conjunto de reglas coincide contra cadenas de prueba sin procesar un archivo completo?

### Diseño de argumentos
¿Cómo nombrarías la opción para ignorar una regla específica integrada (ej. `--disable-rule email`)?

### Diseño de variables
`redaction_rules`, `compiled_patterns`, `masked_stream`, `redaction_counters`, `luhn_checksum`.

### Antes de programar
1. ¿Por qué validar el checksum de Luhn en números de 16 dígitos evita arruinar logs enmascarando números de serie que no son tarjetas de crédito?
2. ¿Cómo estructurar los reemplazos para que el orden de aplicación no rompa patrones anidados?

### Arquitectura
Motor de reglas (`rules_engine.py`), validador Luhn (`luhn.py`) y CLI (`log_redact.py`).

### Pruebas mínimas
1. Procesar un log con un token JWT y una tarjeta de crédito falsa válida y comprobar que ambos se enmascaren.
2. Ejecutar con `--stats` y verificar que el conteo en STDERR sea exacto.

### Pruebas de error
1. Pasar un archivo de reglas JSON con sintaxis rota -> Exit code 1.

### Experiencia de usuario
La salida de datos en STDOUT debe ser 100% limpia para redirecciones, y el reporte en STDERR debe ser claro y conciso.

### Explicación posterior
Explica la importancia de evitar fugas de PII (Personally Identifiable Information) en logs centralizados.

### Aplicación profesional
Pre-procesador en agentes de recolección de logs (Fluentd, Logstash, Vector) antes de indexar en Datadog o Splunk.

### Reto adicional
Implementar preservación determinista de identidad mediante HMAC-SHA256 truncado (ej. `USER-ID: <HASH>`) para permitir correlacionar eventos del mismo usuario sin revelar su identidad real.

---
> [← Ejercicio 017](../ejercicio_017/README.md) · [Índice General](../README.md) · [Ejercicio 019 →](../ejercicio_019/README.md)
