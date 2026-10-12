## Ejercicio 021 — Formulario de Registro para Pruebas Clínicas (`ClinicalTrialFormApp`)

> [Índice General](../README.md) · [← Ejercicio 020](../ejercicio_020/README.md) · [Ejercicio 022 →](../ejercicio_022/README.md)

### Contexto profesional
En centros de investigación biomédica y farmacéutica, los investigadores deben registrar a los voluntarios que participarán en ensayos clínicos bajo estrictos protocolos éticos.

### Usuario objetivo
Coordinador de investigación clínica o enfermero de protocolo.

### Problema
El ingreso de participantes que no cumplen criterios de edad o que no han firmado formalmente el consentimiento informado invalida las auditorías de comités de ética.

### Objetivo
Desarrollar un formulario riguroso para registro de voluntarios de ensayos clínicos, con validaciones estrictas de rango de edad (18 a 65 años), grupo sanguíneo, antecedentes de alergias y casilla obligatoria de consentimiento informado.

### Flujo principal
El coordinador ingresa código del participante, edad, peso, estatura, grupo sanguíneo y alergias conocidas. Para que el botón de envío se active, es estrictamente obligatorio que la casilla 'El voluntario ha firmado el Consentimiento Informado' esté marcada. Si la edad está fuera de rango, el sistema bloquea el registro con una advertencia médica.

### Requisitos funcionales
- Código de participante anónimo (formato `VOL-\d{5}`).
- Edad en años (entero entre 18 y 65).
- Peso (kg) y Estatura (cm) para cálculo automático del IMC (Índice de Masa Corporal).
- Grupo sanguíneo (`Combobox`: A+, A-, B+, B-, AB+, AB-, O+, O-).
- Casilla de verificación obligatoria de Consentimiento Informado.
- Bloqueo estricto del botón de registro hasta que todos los criterios se cumplan.

### Requisitos de interfaz
- Diseño sobrio y clínico.
- Resalte del IMC calculado automáticamente conforme se digita peso y estatura.
- Checkbox de consentimiento destacado en recuadro independiente.

### Datos
- Ficha de voluntario: código, edad, peso, estatura, imc, grupo sanguíneo, alergias, consentimiento firmado.

### Estado
- Variables de control de Tkinter.
- IMC calculado en tiempo real.
- Estado del botón de envío.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Edad estrictamente entre 18 y 65 años.
- Estatura entre 120 y 220 cm; peso entre 40 y 200 kg.
- Casilla de consentimiento informada marcada como verdadera.

### Casos límite
- Modificar peso y estatura sin haber llenado código.
- Intentar desmarcar el consentimiento tras haber presionado registrar.

### Manejo de errores
- Notificar con advertencias claras cualquier incumplimiento de los criterios éticos o médicos.

### Fundamentos de Python relacionados
- Fórmula de IMC: $\text{IMC} = \frac{\text{peso (kg)}}{(\text{estatura (m)})^2}$.
- Clasificación de rangos biométricos mediante condicionales.

### Conceptos Tkinter relacionados
- Widget `ttk.Checkbutton` acoplado a la habilitación de un botón (`state='normal'` vs `state='disabled'`).
- Enlace reactivo para cálculo de IMC al perder el foco o teclear.

### Herramientas para investigar
- Fórmula de Quetelet (IMC).
- Parámetro `state` en botones de Tkinter.

### Diseño de interfaz
¿Cómo asegurarías que el recuadro del consentimiento informado tenga una jerarquía visual destacada sobre el resto del formulario?

### Diseño de variables
Usa nombres como `volunteer_code_entry`, `age_entry`, `weight_entry`, `height_entry`, `bmi_display_label`, `consent_checkbox_var`.

### Antes de programar
1. ¿Cómo se habilita o deshabilita dinámicamente un botón en Tkinter según el valor de un `BooleanVar`?
2. ¿Por qué es crítico convertir la estatura de centímetros a metros antes de elevarla al cuadrado?

### Arquitectura
```
ejercicio_021/
├── app.py           # Formulario clínico y estados de interfaz
└── clinical_core.py # Validaciones de criterios de inclusión y cálculo de IMC
```

### Pruebas mínimas
1. Ingresar peso 70 kg, estatura 175 cm -> Comprobar que el IMC calculado sea ~22.86 (Normopeso).
2. Marcar consentimiento informado -> Comprobar que el botón 'Registrar Voluntario' pase de deshabilitado a habilitado.

### Pruebas de error
1. Ingresar edad 17 años -> Debe impedir el registro indicando que el voluntario no cumple la edad mínima legal.

### Experiencia de usuario
El IMC debe calcularse de manera reactiva en cuanto el usuario termine de ingresar estatura y peso.

### Explicación posterior
¿Cómo garantiza el patrón de inhabilitar el botón de acción principal que el usuario no envíe formularios incompletos?

### Aplicación profesional
Sistemas de captura electrónica de datos (EDC) en ensayos clínicos farmacéuticos y registros hospitalarios.

### Reto adicional
Añade una etiqueta que clasifique el IMC en su categoría clínica estándar (Bajo peso, Normal, Sobrepeso, Obesidad) con código cromático.

---
> [Índice General](../README.md) · [← Ejercicio 020](../ejercicio_020/README.md) · [Ejercicio 022 →](../ejercicio_022/README.md)
