## Ejercicio 080 — Editor y Marcador Visual de Zonas en Planos (`ImageRegionMarkerApp`)

> [Índice General](../README.md) · [← Ejercicio 079](../ejercicio_079/README.md) · [Ejercicio 081 →](../ejercicio_081/README.md)

### Contexto profesional
En sistemas de control de calidad visual en manufactura y supervisión de seguridad en almacenes, los inspectores marcan zonas de interés o áreas restringidas directamente sobre planos o fotografías de inspección.

### Usuario objetivo
Inspector de calidad o auditor de seguridad industrial.

### Problema
Describir defectos o zonas peligrosas con texto sin señalar su coordenada visual exacta en la imagen genera confusiones en auditorías de campo.

### Objetivo
Desarrollar una aplicación de etiquetado y marcado visual de zonas sobre imágenes con `Canvas`, que cargue una imagen local con `PhotoImage`, permita al usuario dibujar cuadros delimitadores (bounding boxes) con el ratón arrastrando un rectángulo sobre el lienzo, liste las zonas creadas en una tabla lateral con su nombre y coordenadas, y permita exportar el conjunto de anotaciones a un archivo `zonas.json`.

### Flujo principal
El inspector abre una imagen o plano con 'Cargar Imagen'. La imagen se despliega en el `Canvas`. El inspector hace clic y arrastra sobre la imagen para definir un recuadro. Al soltar, se dibuja un rectángulo semitransparente o coloreado con una etiqueta numérica y se solicita un nombre para la zona (ej. 'Zona de Alto Voltaje', 'Fisura en Soldadura'). La zona se añade a la tabla lateral. El usuario puede seleccionar una zona de la tabla para resaltarla en la imagen o eliminarla.

### Requisitos funcionales
- Carga de imagen en formato compatible (`.png`, `.gif` nativos de `tk.PhotoImage`) mediante `filedialog`.
- Despliegue de la imagen en un widget `Canvas` adaptado a las dimensiones del archivo.
- Dibujo interactivo de rectángulos delimitadores mediante eventos `<Button-1>` (inicio de esquina), `<B1-Motion>` (estiramiento del cuadro con línea punteada de previsualización) y `<ButtonRelease-1>` (fijación del cuadro definitivo).
- Solicitud de nombre o categoría de la zona creada mediante diálogo rápido.
- Tabla lateral (`ttk.Treeview`) que liste: ID, Nombre de la Zona, Coordenadas `(x1, y1, x2, y2)`.
- Selección bidireccional: hacer clic en una fila de la tabla resalta el rectángulo correspondiente en el `Canvas` con un color más vivo.
- Exportación del conjunto de anotaciones a un archivo estructurado `zonas.json`.

### Requisitos de interfaz
- Panel izquierdo: `Canvas` amplio con barras de desplazamiento bidireccionales.
- Panel derecho: Tabla de zonas marcadas y botones 'Eliminar Zona', 'Exportar Anotaciones'.
- Barra de estado inferior con las coordenadas del ratón en tiempo real al moverse sobre la imagen.

### Datos
- Anotación de zona: id, etiqueta, x1, y1, x2, y2, color.

### Estado
- Imagen cargada en memoria y referencia `image` activa para evitar recolección de basura.
- Lista de rectángulos creados en el Canvas.
- Coordenadas de inicio de arrastre.

### Persistencia
Archivo JSON (`datos/zonas.json`).

### Validaciones
- No permitir registrar zonas con ancho o alto menor a 10 píxeles (evitar clics accidentales).
- Imagen cargada obligatoria antes de permitir dibujar sobre el Canvas.

### Casos límite
- Arrastrar el rectángulo de derecha a izquierda o de abajo hacia arriba (normalizar coordenadas para que $x_1 < x_2$ e $y_1 < y_2$).
- Archivos de imagen muy grandes (debe habilitarse el scroll del Canvas con `scrollregion`).

### Manejo de errores
- Mantener una referencia permanente a la instancia de `PhotoImage` en un atributo de clase para evitar que el recolector de basura de Python elimine la imagen de la pantalla.

### Fundamentos de Python relacionados
- Normalización de coordenadas rectangulares: `x1, x2 = min(x_a, x_b), max(x_a, x_b)`.
- Serialización de metadatos espaciales en JSON.

### Conceptos Tkinter relacionados
- Carga de imágenes con `tk.PhotoImage` y persistencia de referencias.
- Dibujo de rectángulos elásticos (rubber-banding) en `Canvas`.
- Coordenadas reales del Canvas frente a coordenadas de ventana usando `canvas.canvasx(event.x)`.

### Herramientas para investigar
- Problema común de Garbage Collection con `PhotoImage` en Tkinter.
- Métodos `canvas.canvasx()` y `canvas.canvasy()` para soporte de scroll en lienzos.

### Diseño de interfaz
¿Cómo asegurarías que el rectángulo elástico de previsualización mientras el usuario arrastra no deje rastros visuales sucios en el lienzo?

### Diseño de variables
Usa nombres como `image_canvas`, `photo_reference`, `start_x`, `start_y`, `temp_rect_id`, `zones_tree`, `export_json_btn`.

### Antes de programar
1. ¿Por qué las imágenes cargadas con `tk.PhotoImage` desaparecen de la ventana si no se guarda una referencia explícita a la variable en `self.mi_imagen = foto`?
2. ¿Por qué es obligatorio usar `canvas.canvasx(event.x)` en lugar de `event.x` directo cuando el Canvas tiene barras de desplazamiento activas?

### Arquitectura
```
ejercicio_080/
├── app.py             # Interfaz con Canvas y tabla lateral de zonas
├── marker_tool.py     # Manejo del dibujo interactivo de bounding boxes
├── json_exporter.py   # Serialización de coordenadas espaciales en JSON
└── datos/
    └── muestra_plano.png # Imagen de prueba para marcado
```

### Pruebas mínimas
1. Cargar la imagen de prueba -> Comprobar que se despliegue en el Canvas.
2. Arrastrar un cuadro sobre un área del plano -> Debe fijar el rectángulo, pedir nombre y agregarlo a la tabla lateral con sus coordenadas exactas.
3. Exportar a JSON -> Comprobar que el archivo contenga las coordenadas normalizadas.

### Pruebas de error
1. Hacer un clic sin arrastrar (menos de 5 píxeles) -> Debe ignorarse sin crear una zona nula.

### Experiencia de usuario
El cursor sobre el Canvas debe cambiar a cruz de precisión (`cursor='crosshair'`) para facilitar el encuadre exacto.

### Explicación posterior
¿Por qué ocurre la recolección de basura con `PhotoImage` en Tkinter y cómo se resuelve de forma definitiva en la arquitectura de la clase?

### Aplicación profesional
Herramientas de anotación de imágenes para visión artificial y machine learning, auditorías de planos arquitectónicos y marcaje de áreas de peligro en plantas industriales.

### Reto adicional
Añade una opción para que el usuario pueda cambiar el color del borde del recuadro (Rojo para Peligro, Verde para Seguro, Amarillo para Precaución).

---
> [Índice General](../README.md) · [← Ejercicio 079](../ejercicio_079/README.md) · [Ejercicio 081 →](../ejercicio_081/README.md)
