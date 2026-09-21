## Ejercicio 096 — Divisor y Reconstructor de Secretos con Esquema Shamir (`secret-splitter`)

> [← Ejercicio 095](../ejercicio_095/README.md) · [Índice General](../README.md) · [Ejercicio 097 →](../ejercicio_097/README.md)

### Contexto profesional
Para proteger claves maestras de cifrado de almacenamiento, llaves privadas de autoridades de certificación raíz (Root CA) o credenciales de desbloqueo de infraestructura de alta seguridad, ninguna persona individual debe poseer la clave completa. Se utiliza el esquema criptográfico de compartición de secretos de Shamir (Shamir's Secret Sharing - SSS), donde un secreto se divide en $N$ fragmentos (shards) y se requiere un umbral mínimo de $K$ fragmentos ($K \le N$) para reconstruir el secreto original.

### Problema
Construir una CLI criptográfica que implemente el esquema de Shamir sobre campos de Galois ($GF(2^8)$ / polinomios en aritmética modular), permitiendo dividir un secreto de texto o archivo en $N$ partes con un umbral de reconstrucción $K$, exportar los fragmentos en formato seguro con checksum y reconstruir el secreto exacto a partir de cualquier combinación de al menos $K$ fragmentos.

### Usuario objetivo
Oficiales de seguridad, ingenieros criptográficos y administradores de infraestructura crítica.

### Objetivo
Implementar el esquema criptográfico de Shamir (Shamir's Secret Sharing) en aritmética de campos finitos con interfaz de división, reconstrucción e inspección de fragmentos.

### Ejemplo conceptual de uso
```bash
# Dividir una llave maestra en 5 partes requiriendo 3 para reconstruir (umbral 3 de 5)
python secret_splitter.py split "MI_LLAVE_MAESTRA_SUPER_SECRETA" --shares 5 --threshold 3 -o ./shards

# Reconstruir el secreto combinando 3 fragmentos cualesquiera
python secret_splitter.py combine ./shards/shard_1.txt ./shards/shard_3.txt ./shards/shard_5.txt

# Inspeccionar metadatos de un fragmento sin revelar el secreto
python secret_splitter.py inspect ./shards/shard_2.txt
```

### Requisitos funcionales
- Subcomando `split <SECRETO>`: divide una cadena o archivo de entrada en $N$ fragmentos (`--shares N`) con un umbral $K$ (`--threshold K`):
  - Generar polinomios aleatorios de grado $K-1$ donde el término independiente ($a_0$) es el byte del secreto.
  - Evaluar el polinomio en $N$ puntos distintos para generar cada fragmento $(x, y)$.
  - Codificar cada fragmento con metadatos (ID de fragmento, índice $x$, umbral $K$, checksum SHA256 truncado y datos en Base64/Hexadecimal).
- Subcomando `combine <SHARD_FILES...>`: lee al menos $K$ archivos de fragmentos, valida sus checksums y que pertenezcan a la misma sesión de división, ejecuta la interpolación de Lagrange en $x=0$ para recuperar el secreto y lo emite en STDOUT.
- Subcomando `inspect <SHARD_FILE>`: muestra el índice $x$, el umbral requerido $K$ y la validez del checksum del fragmento sin revelar datos confidenciales.
- Garantía criptográfica: cualquier subconjunto de $K-1$ fragmentos no revela absolutamente ninguna información sobre el secreto original (Information-Theoretic Security).

### Requisitos de CLI
- Subcomandos: `split`, `combine`, `inspect`.
- Opciones de `split`: `-n / --shares <N>` (default 5), `-k / --threshold <K>` (default 3), `-o / --out-dir <RUTA>`.
- Exit code 0 en éxito, 1 si se proporcionan menos de $K$ fragmentos o hay fragmentos corruptos en `combine`, 2 en errores de sintaxis.

### Entradas
- Secretos en texto/archivo o rutas de archivos de fragmentos.

### Salidas
- Fragmentos generados en disco o secreto reconstruido en STDOUT.

### Persistencia
Escritura y lectura de archivos de fragmentos (`shard_X.txt`) en el sistema de archivos.

### Validaciones
- El umbral $K$ debe ser menor o igual a la cantidad total de partes $N$ ($2 \le K \le N$).
- En `combine`, verificar que todos los fragmentos pertenezcan al mismo identificador de secreto y no haya índices $x$ duplicados.

### Casos límite
- Intentar reconstruir con exactamente $K-1$ fragmentos (debe rechazar por falta de fragmentos antes de intentar interpolar).
- Fragmentos que contienen datos alterados (el checksum del fragmento debe fallar).
- Secretos de longitud variable (cifrar byte a byte o usar cifrado simétrico combinado con Shamir para la llave).

### Manejo de errores
- Error de umbral insuficiente en `combine`.
- Fragmentos incompatibles entre sí.

### Fundamentos de Python relacionados
- Criptografía teórica y aritmética modular / campos de Galois $GF(256)$ o aritmética de polinomios con números primos grandes.
- Interpolación polinómica de Lagrange: $L(0) = \sum_{j} y_j \prod_{m \ne j} \frac{-x_m}{x_j - x_m}$.
- Generación de números aleatorios criptográficamente seguros con módulo `secrets`.
- Módulos `hashlib` y `base64`.

### Conceptos CLI relacionados
- Implementación de esquemas de compartición de secretos (Secret Sharing Schemes) en terminal.
- Gestión de ceremonias criptográficas de custodia distribuida.

### Herramientas o módulos para investigar
- `secrets`.
- `hashlib` y `base64`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `verify-shard <SHARD_FILE>` para comprobar que el archivo no esté corrupto sin requerir los demás fragmentos?

### Diseño de argumentos
¿Cómo nombrarías la opción para ingresar el secreto de forma oculta en la terminal mediante `getpass` (`--secret-prompt`)?

### Diseño de variables
`secret_raw_bytes`, `polynomial_coefficients_list`, `threshold_k_integer`, `shares_n_integer`, `lagrange_interpolated_secret`.

### Antes de programar
1. ¿Cómo funciona la interpolación de Lagrange para reconstruir el secreto evaluando el polinomio en $x=0$ a partir de $K$ puntos $(x_i, y_i)$?
2. ¿Por qué usar un campo finito (como aritmética modular con un número primo grande $P > 255$ o $GF(2^8)$) evita la fuga de información que ocurriría con polinomios sobre números reales?

### Arquitectura
Motor de Shamir (`shamir_core.py`), interpolador de Lagrange (`lagrange.py`), codificador de fragmentos (`shard_codec.py`) y CLI.

### Pruebas mínimas
1. Dividir un secreto con $N=5$ y $K=3$. Combinar las partes 1, 2 y 4 y verificar que el secreto reconstruido sea 100% idéntico al original.
2. Intentar combinar con solo las partes 1 y 2 y verificar que rechace con exit code 1 por umbral insuficiente.

### Pruebas de error
1. Pasar $K=5$ y $N=3$ (umbral mayor que partes totales) -> Exit code 2 con error de validación.

### Experiencia de usuario
En `split`, mostrar resumen de fragmentos generados y advertencias de seguridad. En `combine`, emitir únicamente el secreto recuperado para facilitar pipes.

### Explicación posterior
Explica la diferencia entre seguridad computacional (que depende de la dificultad de romper un algoritmo) y seguridad teórica de la información (donde los fragmentos insuficientes no contienen información matemática del secreto).

### Aplicación profesional
Ceremonias de generación de llaves de Root CA, custodia compartida de llaves de billeteras institucionales y recuperación ante desastres de credenciales maestras.

### Reto adicional
Implementar un esquema de compartición de secretos verificable (Verifiable Secret Sharing - Feldman VSS) donde cada fragmento incluya un testigo criptográfico para verificar si un custodio entrega un fragmento falso.

---
> [← Ejercicio 095](../ejercicio_095/README.md) · [Índice General](../README.md) · [Ejercicio 097 →](../ejercicio_097/README.md)
