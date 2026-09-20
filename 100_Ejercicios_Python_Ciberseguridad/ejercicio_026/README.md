# Recursos del ejercicio 026

[Volver al enunciado](../ejercicio_026.md) · [Convenciones](../README.md#contratos-comunes)

## Procedencia y alcance

Todos los datos son sintéticos y se distribuyen para este laboratorio. No son capturas de usuarios ni sistemas reales. Los vectores públicos criptográficos se identifican expresamente. Una declaración de sensor o ticket es evidencia del escenario, no una certificación independiente de veracidad.

## Archivos y formatos

### [config/clave_lab.bin](config/clave_lab.bin)

Clave pública de práctica; no reutilizar como secreto real ni incrustar su valor en código.

Contenido binario inerte; 33 bytes. No decodificar antes de una comprobación de integridad.

### [datos/m1.bin](datos/m1.bin)

Mensaje inerte; autenticar bytes exactos, incluido LF final.

Contenido binario inerte; 32 bytes. No decodificar antes de una comprobación de integridad.

### [datos/m2.bin](datos/m2.bin)

Variante de contenido que conserva etiqueta de otro mensaje.

Contenido binario inerte; 32 bytes. No decodificar antes de una comprobación de integridad.

### [datos/etiquetas.json](datos/etiquetas.json)

Rutas relativas a datos; etiquetas como hex ASCII. H3 tiene formato intencionalmente inválido.

JSON: lista de registros; campos observados: hmac_sha256, id, ruta.

## Contrato de lectura

- Usa las claves y columnas entregadas. Los nombres describen el campo de origen; elige tus propios nombres internos sin cambiar significado.
- Identificadores y nombres de entidad son texto; puertos, bytes, cantidades, offsets y segundos relativos son enteros. CSV los representa como texto que debes convertir y validar. Los booleanos JSON son booleanos, no textos ni enteros. Los ids numéricos de SQLite son la excepción explícita.
- ts, start, end, inicio, fin, expires_at y otras fechas son instantes ISO8601 con zona cuando el contrato no declare segundos relativos. Un campo sin zona puede ser un caso defectuoso intencional.
- id identifica un registro; event_id, origin, source, collector o boot_id pueden formar identidad compuesta si lo exige el enunciado. La posición física permite distinguir repeticiones.
- null, campo ausente, cadena vacía, cero y falso no son intercambiables. Las claves que faltan pueden representar incertidumbre o una infracción según el contrato; no rellenarlas por intuición.
- Unidades: bytes enteros; segundos para reloj relativo, diferencias y márgenes; distancias en km cuando existan. MiB representa 1048576 bytes. Los intervalos siguen los extremos definidos en el ejercicio.
- Las rutas dentro de registros son datos. Solo abre archivos que el enunciado indique expresamente dentro del paquete; no abras rutas /etc, /tmp, C:/... ni URLs copiadas de un log.

## Preparar pruebas

Conserva estos archivos como origen y trabaja con copias en tu propia carpeta de práctica. Los casos mínimos pueden seleccionar un subconjunto o cambiar una frontera en una copia; los originales no se editan. No hay una salida completa de referencia ni implementaciones.
