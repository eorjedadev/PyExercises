## Ejercicio 016 — Registro de Incidentes de Soporte Nivel 1 (`HelpdeskIncidentApp`)

> [Índice General](../README.md) · [← Ejercicio 015](../ejercicio_015/README.md) · [Ejercicio 017 →](../ejercicio_017/README.md)

### Contexto profesional
En centros de operaciones de red (NOC) y mesas de ayuda de TI, los operadores reciben llamadas de usuarios y deben categorizar y documentar incidentes rápidamente.

### Usuario objetivo
Analista de mesa de ayuda (Service Desk Nivel 1).

### Problema
La falta de tipificación de la severidad y la ausencia de descripciones claras de pasos para reproducir causan retrasos al escalar incidentes a ingenieros de nivel 2 y 3.

### Objetivo
Desarrollar una aplicación de captura de tickets de soporte con niveles de severidad (Baja, Media, Alta, Crítica), área de descripción detallada con contador de caracteres mínimos, validaciones condicionales y confirmación visual.

### Flujo principal
El analista ingresa el nombre del usuario afectado, selecciona el servicio impactado y la severidad. Si la severidad es 'Crítica', el sistema exige obligatoriamente un teléfono de contacto directo. Al redactar la descripción (mínimo 30 caracteres), se valida el ticket y se genera un número de folio único simulado.

### Requisitos funcionales
- Captura de: Usuario Afectado, Servicio Impactado (`Combobox`), Nivel de Severidad (`Radiobutton` o `Combobox`).
- Campo de Teléfono que se vuelve obligatorio y visualmente resaltado si la severidad es 'Crítica'.
- Área `Text` para descripción del incidente con validación de longitud mínima (30 caracteres).
- Generación de folio único con formato `INC-YYYYMMDD-XXXX`.
- Reseteo del formulario tras registrar el ticket exitosamente.

### Requisitos de interfaz
- Formulario estructurado con etiquetas consistentes.
- Contenedor visual para el área de descripción con scrollbar.
- Alerta visual en color rojo si se selecciona severidad 'Crítica'.
- Cuadro de diálogo modal que confirme el registro y muestre el folio generado.

### Datos
- Ficha de ticket: folio, usuario, servicio, severidad, teléfono, descripción y timestamp.

### Estado
- Severidad actualmente seleccionada.
- Conteo de caracteres en el área de descripción.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Usuario afectado no debe estar vacío.
- Si la severidad es 'Crítica', el teléfono es obligatorio y debe contener al menos 8 dígitos.
- La descripción debe tener al menos 30 caracteres.

### Casos límite
- El operador cambia la severidad de 'Crítica' a 'Baja' (el campo de teléfono debe dejar de ser obligatorio).
- Descripción con solo espacios en blanco.

### Manejo de errores
- Mostrar con claridad en la interfaz qué requisito falta cumplir antes de enviar.

### Fundamentos de Python relacionados
- Módulo `uuid` o `random` para generación de identificadores únicos.
- Validación condicional con estructuras `if/elif/else` complejas.

### Conceptos Tkinter relacionados
- Cambio dinámico de propiedades de widgets (`entry.config(bg=...)`, `label.config(text=...)`).
- Widget `Text` para entradas multilínea largas.
- Diálogo modal con `messagebox.showinfo`.

### Herramientas para investigar
- Generación de folios con `datetime.now().strftime` y `random.randint`.
- Eventos de selección en `Combobox`.

### Diseño de interfaz
¿Cómo indicarías de forma clara al operador que el campo de teléfono se volvió obligatorio tras cambiar la severidad a 'Crítica'?

### Diseño de variables
Usa nombres como `affected_user_entry`, `service_combo`, `severity_var`, `phone_entry`, `desc_text`, `submit_ticket_btn`.

### Antes de programar
1. ¿Cómo conectas un callback que observe el cambio de severidad para alterar el estado visual del campo de teléfono?
2. ¿Cómo validas que el texto de un widget `Text` tenga al menos 30 caracteres reales ignorando espacios?

### Arquitectura
```
ejercicio_016/
├── app.py            # Formulario de soporte y lógica visual
└── ticket_service.py # Generación de folios y validación de reglas de negocio
```

### Pruebas mínimas
1. Llenar ticket con severidad 'Media' y descripción de 35 caracteres -> Debe registrar y entregar folio `INC-...`.
2. Seleccionar severidad 'Crítica' -> Debe exigir teléfono y no permitir guardar si está vacío.

### Pruebas de error
1. Intentar enviar con descripción de 10 caracteres -> Debe indicar que la descripción es demasiado corta.

### Experiencia de usuario
El formulario debe permitir tabular naturalmente entre campos con la tecla `Tab` en orden lógico.

### Explicación posterior
¿Cómo manejaste la reactividad condicional del campo de teléfono según la severidad seleccionada?

### Aplicación profesional
Sistemas de Service Desk interno, consolas de registro de averías en telecomunicaciones y plataformas de ticketing.

### Reto adicional
Añade un contador en tiempo real debajo de la descripción que muestre 'X / 30 caracteres requeridos' y cambie a color verde al alcanzar el mínimo.

---
> [Índice General](../README.md) · [← Ejercicio 015](../ejercicio_015/README.md) · [Ejercicio 017 →](../ejercicio_017/README.md)
