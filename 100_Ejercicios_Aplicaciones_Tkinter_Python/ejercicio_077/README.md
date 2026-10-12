## Ejercicio 077 — Tablero de Dibujo y Firma Digital de Conformidad (`SignaturePadApp`)

> [Índice General](../README.md) · [← Ejercicio 076](../ejercicio_076/README.md) · [Ejercicio 078 →](../ejercicio_078/README.md)

### Contexto profesional
En servicios de paquetería, notarías y recepciones de mercancía en almacén, los clientes firman digitalmente la recepción de productos o contratos de conformidad sobre tabletas o pantallas táctiles.

### Usuario objetivo
Receptor de mercancía, cliente de entrega o auditor de almacén.

### Problema
La falta de un componente de firma digital local obliga a imprimir hojas de remisión físicas que luego deben escanearse y archivarse en papel.

### Objetivo
Desarrollar un componente de pad de firma digital interactivo en `Canvas` que capture el trazo continuo del ratón a mano alzada, permita limpiar el lienzo, valide que el recuadro no esté vacío antes de aceptar, y guarde los puntos vectoriales del trazo en un archivo `firma.json`.

### Flujo principal
El cliente dibuja su firma sobre el recuadro del lienzo con el ratón o lápiz óptico. El trazo se dibuja de forma fluida y continua. Si el cliente comete un error, presiona 'Limpiar Firma' para reiniciar el lienzo. Al presionar 'Aceptar y Guardar Firma', la aplicación valida que la firma contenga una cantidad mínima de trazos reales (no esté en blanco o tenga solo un punto accidental) y guarda las coordenadas en disco.

### Requisitos funcionales
- Widget `Canvas` estilizado como recuadro de firma bancaria con línea guía punteada inferior.
- Captura de trazo suave a mano alzada mediante eventos `<Button-1>`, `<B1-Motion>` y `<ButtonRelease-1>` dibujando segmentos con `canvas.create_line` con acabado redondeado (`capstyle='round'`, `smooth=True`).
- Registro secuencial de coordenadas vectoriales de cada trazo en una lista de polilíneas.
- Botón 'Limpiar Firma' que borre el lienzo y restablezca la lista de trazos.
- Validación estricta de 'Firma válida': verificar que existan al menos 20 puntos de trazo registrados.
- Guardado de las coordenadas vectoriales de la firma en formato `firma.json`.
- Indicador de estado que comunique 'Firma registrada con éxito' o 'Por favor, firme dentro del recuadro'.

### Requisitos de interfaz
- Recuadro de firma delimitado por borde visible con fondo blanco nítido.
- Botones de acción inferiores: 'Limpiar', 'Validar', 'Guardar Firma'.
- Barra de estado clara que confirme si la firma ha sido aceptada.

### Datos
- Trazo vectorial: lista de trazos, donde cada trazo es una lista de puntos `[(x1, y1), (x2, y2), ...]`.
- Metadatos: fecha, hora, total_puntos.

### Estado
- Lista de trazos de la firma actual en memoria.
- Coordenada anterior del cursor $(x_{ant}, y_{ant})$ durante el arrastre.

### Persistencia
Archivo JSON (`datos/firma.json`).

### Validaciones
- No permitir guardar si el Canvas está en blanco o tiene un solo clic accidental (menos de 20 puntos de trazo).
- Trazos contenidos dentro de los límites del lienzo.

### Casos límite
- El usuario dibuja fuera del marco del Canvas (el trazo debe cortarse limpiamente en el borde).
- Dibujar múltiples trazos separados (levantando el ratón y volviendo a trazar).

### Manejo de errores
- Notificar con advertencia visual si se intenta guardar una firma vacía o insuficiente.

### Fundamentos de Python relacionados
- Serialización de listas de coordenadas en formato JSON estructurado.
- Algoritmos básicos de interpolación y distancia euclidiana entre puntos.

### Conceptos Tkinter relacionados
- Parámetros de estilo de línea en `create_line`: `width=2`, `capstyle=tk.ROUND`, `smooth=True`.
- Mecánica de seguimiento de trazos continuos entre evento y evento de ratón.

### Herramientas para investigar
- Opciones de línea en `tkinter.Canvas` (`capstyle`, `joinstyle`, `smooth`).
- Serialización de coordenadas vectoriales en Python.

### Diseño de interfaz
¿Cómo diseñarías el lienzo para que imite la apariencia de una tableta de firma digital profesional (con línea punteada para firmar y aviso 'Firme aquí')?

### Diseño de variables
Usa nombres como `signature_canvas`, `clear_sig_btn`, `save_sig_btn`, `sig_status_label`, `current_stroke_points`, `all_strokes_list`.

### Antes de programar
1. ¿Cómo se dibuja un trazo continuo uniendo las coordenadas del evento anterior $(x_{prev}, y_{prev})$ con las actuales $(x_{curr}, y_{curr})$ en cada evento `<B1-Motion>`?
2. ¿Cómo se determina que una firma es válida comprobando la longitud y cantidad de segmentos trazados?

### Arquitectura
```
ejercicio_077/
├── app.py             # Formulario de recepción y panel de firma
├── signature_pad.py   # Componente de lienzo de firma y eventos de ratón
├── vector_storage.py  # Exportación y carga de trazos en firma.json
└── datos/
    └── firma.json     # Archivo de persistencia de coordenadas vectoriales
```

### Pruebas mínimas
1. Dibujar una firma completa a mano alzada y presionar 'Guardar' -> Debe confirmar éxito y guardar las coordenadas en `firma.json`.
2. Presionar 'Limpiar' -> El lienzo debe quedar en blanco y el archivo no debe guardarse.

### Pruebas de error
1. Hacer un solo clic (un punto de 1 píxel) y presionar Guardar -> Debe advertir 'La firma es demasiado corta o está en blanco'.

### Experiencia de usuario
El trazo debe responder de forma inmediata al movimiento del ratón con un grosor uniforme y sin discontinuidades visuales.

### Explicación posterior
¿Cómo se capturan y serializan trazos vectoriales a mano alzada utilizando eventos de arrastre de ratón en el widget `Canvas`?

### Aplicación profesional
Recepción de entregas de mensajería (Proof of Delivery - POD), contratos de alquiler de vehículos y consentimiento informado médico en clínica.

### Reto adicional
Añade una función para reconstruir y redibujar automáticamente en el lienzo una firma guardada previamente a partir de su archivo `firma.json`.

---
> [Índice General](../README.md) · [← Ejercicio 076](../ejercicio_076/README.md) · [Ejercicio 078 →](../ejercicio_078/README.md)
