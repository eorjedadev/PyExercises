# Recursos del ejercicio 100

[Volver al enunciado](../ejercicio_100.md) · [Convenciones](../README.md#contratos-comunes)

## Procedencia y alcance

Todos los datos son sintéticos y se distribuyen para este laboratorio. No son capturas de usuarios ni sistemas reales. Los vectores públicos criptográficos se identifican expresamente. Una declaración de sensor o ticket es evidencia del escenario, no una certificación independiente de veracidad.

## Archivos y formatos

### [logs/auth.json](logs/auth.json)

Copia independiente para recuperar el contrato anterior. Caso de ana con errores y éxito, más actividad de otras cuentas.

JSON: lista de registros; campos observados: cuenta, destino, id, origen, resultado, ts.

### [logs/roles.json](logs/roles.json)

Copia independiente para recuperar el contrato anterior. Cambio P1 de ana y P2 de beto; no indican si hubo sesión interactiva real.

JSON: lista de registros; campos observados: actor, id, new_role, ts, user.

### [datos/tickets.json](datos/tickets.json)

Copia independiente para recuperar el contrato anterior. Solo existe autorización aportada para beto; no inventar otra para ana.

JSON: lista de registros; campos observados: approved, approver, end, id, role, start, user.

### [datos/cobertura.json](datos/cobertura.json)

Copia independiente para recuperar el contrato anterior. Ausencia explícita de fuente endpoint en el expediente recibido.

JSON: objeto; claves de primer nivel: auth, roles, endpoint.

### [logs/firewall.json](logs/firewall.json)

Conexión N1 corrobora tiempo y par de A4; no identifica persona ni contenido.

JSON: lista de registros; campos observados: action, destination, id, origin, port, protocol, ts.

### [datos/inventario.json](datos/inventario.json)

Propietarios para dirigir preguntas; no autorizan automáticamente actividad.

JSON: lista de registros; campos observados: id, owner, role.

### [datos/encargo.json](datos/encargo.json)

Encargo acotado y carencias conocidas; otras hipótesis pueden necesitar fuentes adicionales.

JSON: objeto; claves de primer nivel: scope, period, question, missing.

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
