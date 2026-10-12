## Ejercicio 048 — Consola de Diagnóstico de Red Local con Historial (`NetworkPingToolApp`)

> [Índice General](../README.md) · [← Ejercicio 047](../ejercicio_047/README.md) · [Ejercicio 049 →](../ejercicio_049/README.md)

### Contexto profesional
En áreas de soporte técnico y administración de redes, los ingenieros comprueban la conectividad básica con servidores, enrutadores e impresoras de red registrando el histórico de pruebas.

### Usuario objetivo
Técnico de soporte de redes o administrador de sistemas.

### Problema
Ejecutar comandos en la consola de comandos de texto dispersa los resultados y no permite archivar un histórico visual organizado de las pruebas realizadas.

### Objetivo
Desarrollar una aplicación de diagnóstico de conectividad local que reciba una dirección IP o nombre de host, ejecute una comprobación simulada de diagnóstico con tiempo de respuesta en ms, registre el resultado en una tabla principal y permita abrir una ventana secundaria con el histórico detallado de pruebas.

### Flujo principal
El técnico ingresa una IP o host (ej. `192.168.1.1` o `google.com`) y selecciona la cantidad de paquetes. Presiona 'Probar Conectividad'. La aplicación simula la prueba, calcula la latencia promedio y estado ('En línea' en verde o 'Sin respuesta' en rojo), y lo agrega a la tabla. Puede abrir una ventana secundaria de histórico o exportar la traza.

### Requisitos funcionales
- Entrada para Host / Dirección IP (con validación de formato básico).
- Selector de paquetes a enviar (1 a 5 paquetes).
- Simulación de prueba de diagnóstico con cálculo de latencia en milisegundos y porcentaje de pérdida.
- Visualización en `ttk.Treeview` con columnas: Host, Fecha/Hora, Latencia Promedio, Estado.
- Barra de menú con opciones para limpiar historial y exportar a texto.
- Ventana secundaria `Toplevel` con el log detallado de trazas técnicas.

### Requisitos de interfaz
- Formulario superior compacto con botón 'Probar Conectividad' destacado.
- `Treeview` de resultados con tags cromáticos según estado.
- Ventana secundaria de log con widget `Text` monoespaciado.

### Datos
- Prueba de red: host, timestamp, paquetes_enviados, paquetes_recibidos, latencia_ms, estado.

### Estado
- Historial acumulado de diagnósticos en memoria.
- Variable para host ingresado.

### Persistencia
Exportación opcional a archivo de texto plano (`filedialog.asksaveasfilename`).

### Validaciones
- Host o IP no puede estar vacío ni contener espacios en blanco.
- Validar formato de IP o nombre de dominio básico.

### Casos límite
- Intentar probar un host con caracteres inválidos.
- Historial vacío al intentar exportar.

### Manejo de errores
- Notificar con aviso visual si el formato del host ingresado es inválido.

### Fundamentos de Python relacionados
- Validación de direcciones IP con el módulo estándar `ipaddress` o regex.
- Simulación de valores aleatorios controlados (`random.uniform`) para latencias realistas.

### Conceptos Tkinter relacionados
- Ventanas de diagnóstico con menús y diálogos secundarios.
- Actualización de tablas y tags de colores.

### Herramientas para investigar
- Módulo `ipaddress` de la biblioteca estándar de Python.
- Manejo de ventanas secundarias de log en Tkinter.

### Diseño de interfaz
¿Cómo asegurarías que el botón de prueba comunique un estado activo mientras se procesa la simulación?

### Diseño de variables
Usa nombres como `host_entry`, `packet_count_combo`, `test_btn`, `history_tree`, `log_window`, `export_trace_btn`.

### Antes de programar
1. ¿Cómo se valida si una cadena es una dirección IP válida utilizando el módulo estándar `ipaddress`?
2. ¿Cómo se actualiza la interfaz para que muestre el nuevo diagnóstico en la primera fila de la tabla?

### Arquitectura
```
ejercicio_048/
├── app.py             # Formulario de prueba y tabla de resultados
├── log_window.py      # Ventana secundaria con traza técnica
└── ping_simulator.py  # Simulación de diagnóstico de red y validación de IPs
```

### Pruebas mínimas
1. Ingresar '192.168.1.1' y probar -> Debe registrar el diagnóstico en la tabla con latencia y estado 'En línea'.
2. Abrir la ventana de histórico -> Debe mostrar la traza técnica detallada del paquete.

### Pruebas de error
1. Ingresar '999.999.999.999' -> Debe rechazar la dirección indicando formato de host inválido.

### Experiencia de usuario
Los estados en línea deben verse en verde nítido y las caídas de conexión en rojo prominente.

### Explicación posterior
¿Cómo ayuda el módulo `ipaddress` de Python a robustecer la validación de entradas de red en una aplicación gráfica?

### Aplicación profesional
Herramientas de diagnóstico de soporte de campo, monitores de cabina de telecomunicaciones y consolas de mesa de ayuda.

### Reto adicional
Añade una opción en el menú para 'Comprobar Lista de Servidores Críticos' que ejecute el diagnóstico secuencial sobre 5 IPs predefinidas.

---
> [Índice General](../README.md) · [← Ejercicio 047](../ejercicio_047/README.md) · [Ejercicio 049 →](../ejercicio_049/README.md)
