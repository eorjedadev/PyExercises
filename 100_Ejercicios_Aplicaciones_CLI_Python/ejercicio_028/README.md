## Ejercicio 028 — Conversor de Divisas con Caché Local de Tasas (`unit-calc`)

> [← Ejercicio 027](../ejercicio_027/README.md) · [Índice General](../README.md) · [Ejercicio 029 →](../ejercicio_029/README.md)

### Contexto profesional
En sistemas de facturación internacional, análisis financiero y plataformas de comercio electrónico, los analistas y desarrolladores necesitan convertir montos entre múltiples divisas (USD, EUR, GBP, JPY, COP, MXN) consultando tasas de cambio actualizadas y manteniendo una caché local fuera de línea para operar sin conexión a internet.

### Problema
Construir una CLI para conversión de divisas que permita convertir montos entre monedas, actualizar la tabla de tasas de cambio desde una API pública o archivo mock, mantener una caché local con expiración temporal (TTL) y operar en modo offline.

### Usuario objetivo
Desarrolladores, analistas financieros y operadores de comercio electrónico.

### Objetivo
Implementar un conversor financiero con subcomandos, caché de datos con expiración, manejo de red resiliente y modo offline.

### Ejemplo conceptual de uso
```bash
# Convertir 150 USD a EUR y COP
python unit_calc.py convert 150 USD --to EUR,COP

# Actualizar tasas de cambio manualmente
python unit_calc.py rates update

# Listar todas las tasas de cambio almacenadas en caché y su antigüedad
python unit_calc.py rates list
```

### Requisitos funcionales
- Subcomando `convert <MONTO> <DIVISA_ORIGEN> --to <DIVISAS_DESTINO>`: realiza la conversión matemática $Monto_{dest} = Monto_{orig} \times (Tasa_{dest} / Tasa_{orig})$.
- Subcomando `rates update`: descarga las últimas tasas de cambio y las guarda en la caché local (`rates_cache.json`).
- Subcomando `rates list`: muestra las tasas vigentes, divisa base y fecha de última sincronización.
- Verificación automática de TTL (Time-To-Live, default 24 horas): si la caché caducó, intentar actualizar; si no hay conexión, advertir y usar las tasas en caché.
- Flag `--offline`: prohíbe cualquier petición de red y utiliza exclusivamente los datos locales.

### Requisitos de CLI
- Subcomandos: `convert` y `rates` (con subcomandos anidados `update`, `list`, `set-base`).
- Opciones de `convert`: `--to <LISTA>`, `--precision <N>` (decimales, default 2).
- Flag `--offline`.
- Exit code 0 en éxito, 1 si la divisa no existe o no hay datos disponibles, 2 en errores.

### Entradas
- Montos numéricos, códigos de moneda ISO 4217 (3 letras).
- Opciones de destino y flags de red.

### Salidas
- Tabla de conversión con tasa aplicada y monto resultante en STDOUT.

### Persistencia
Archivo JSON local con tasas y timestamp (`rates_cache.json`).

### Validaciones
- Validar que el monto sea un número positivo.
- Validar que los códigos de divisa tengan 3 letras y existan en la tabla de tasas.

### Casos límite
- Ejecución en máquina sin conexión a internet y sin archivo de caché previo (debe fallar con mensaje claro).
- Conversión entre la misma divisa (ej. USD a USD -> factor 1.0 directo).
- Tasas de divisas con valores muy pequeños (ej. criptomonedas o monedas con alta inflación; respetar precisión decimal).

### Manejo de errores
- `urllib.error.URLError` o errores de timeout de red.
- `KeyError` por divisa no reconocida.

### Fundamentos de Python relacionados
- Módulo `decimal` (`Decimal`) para cálculos financieros precisos (evitar problemas de redondeo de punto flotante).
- Módulo `datetime` para cálculo de antigüedad de caché.
- Módulos `json` y `urllib.request`.
- Subparsers jerárquicos de dos niveles en `argparse`.

### Conceptos CLI relacionados
- Gestión de caché local con invalidación por tiempo (TTL).
- Diseño de modo offline para herramientas resilientes.

### Herramientas o módulos para investigar
- `decimal.Decimal`.
- `urllib.request`.
- `json` y `datetime`.
- `argparse`.

### Diseño de comandos
¿Cómo estructurarías los subparsers para soportar `unit_calc.py rates update` de forma limpia?

### Diseño de argumentos
¿Cómo permitirías configurar una API Key externa si se usa un proveedor comercial de tasas de cambio (`--api-key` o variable de entorno `EXCHANGE_API_KEY`)?

### Diseño de variables
`source_currency`, `target_currencies`, `input_amount_decimal`, `rates_dictionary`, `cache_timestamp`, `is_cache_stale`.

### Antes de programar
1. ¿Por qué nunca se deben hacer cálculos de dinero con el tipo `float` de Python y es obligatorio usar `decimal.Decimal`?
2. ¿Cómo calcular la conversión indirecta si todas las tasas están expresadas respecto a una moneda base (ej. USD)?

### Arquitectura
Estructura:
```
ejercicio_028/
├── unit_calc.py
├── cache_manager.py
├── converter_service.py
└── fixtures/
    └── mock_rates.json
```

### Pruebas mínimas
1. Con un mock de tasas (USD=1.0, EUR=0.9, COP=4000.0), convertir 100 USD a EUR y verificar que dé exactamente 90.00 EUR.
2. Probar `--precision 4` y verificar los 4 decimales.

### Pruebas de error
1. Intentar convertir a una moneda inexistente `XYZ` -> Exit code 1.

### Experiencia de usuario
Presentar los resultados en una tabla clara que muestre: `MONTO ORIGEN`, `DIVISA ORIGEN`, `TASA`, `MONTO DESTINO`, `DIVISA DESTINO` y advertencia en amarillo si las tasas tienen más de 24 horas de antigüedad.

### Explicación posterior
Explica el fenómeno de imprecisión binaria de punto flotante IEEE 754 (ej. `0.1 + 0.2 != 0.3`) y por qué `Decimal` es indispensable en finanzas.

### Aplicación profesional
Cálculo de tarifas internacionales en plataformas de pago (Stripe, PayPal) y motores de tarificación multi-país.

### Reto adicional
Permitir agregar divisas o tasas personalizadas manualmente mediante el comando `rates add-custom BTC 65000.0 --base USD`.

---
> [← Ejercicio 027](../ejercicio_027/README.md) · [Índice General](../README.md) · [Ejercicio 029 →](../ejercicio_029/README.md)
