---
id: HU-06
titulo: 'HU-06 "Registrar Paciente"'
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-1, Gestión-Pacientes, historia-usuario, prioridad:alta, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** cajero de admisión
**Quiero** registrar a la persona que llega a urgencias
**Para** que entre a la cola de atención con un identificador que permita seguirla durante toda su estancia

**Criterios de Aceptación:**
- Registro con cédula, nombre completo, fecha de nacimiento, seguro médico y contacto de emergencia
- La cédula es única: si ya existe, se reutiliza la ficha y se abre una nueva atención sin duplicar al paciente
- Paciente sin documento recibe un identificador temporal SD-AAAAMMDD-NNN con marca de identificación pendiente
- Ticket generado con formato T-AAAAMMDD-NNN y consecutivo diario que reinicia a las 00:00
- La edad se calcula desde la fecha de nacimiento en cada consulta
- Se rechazan fechas de nacimiento futuras y edades superiores a 120 años
- Paciente menor de 18 años exige acompañante responsable
- El estado inicial es "En espera" y la hora de registro la asigna el sistema

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Es la puerta de entrada del sistema; no depende de otras historias |
| **Negotiable** | Sí | Los campos opcionales y el formato del ticket pueden negociarse |
| **Valuable** | Sí | Sin admisión no hay cola, ni triaje, ni historia clínica |
| **Estimable** | Sí | Siete campos, tres caminos de identificación y ticket diario |
| **Small** | Sí | 5 puntos: formulario, detección de duplicados y generación de ticket |
| **Testable** | Sí | Cédula duplicada, fecha inválida y menor de edad son casos concretos |

**Score INVEST:** 6/6
**Riesgo principal:** Los pacientes sin documento tienden a generar fichas duplicadas.
**Sugerencia:** Marcar la identificación pendiente y conciliar al momento del alta.

---

## Wireframe Asociado

![Wireframe HU-06](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-06-registrar-paciente.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-06-registrar-paciente.svg)

**Leyenda del mockup:**

1. Registro sin documento; habilita una identificación temporal.
2. Nombre completo del paciente.
3. Cédula; si ya existe se reutiliza la ficha y no se duplica el paciente.
4. Fecha de nacimiento y edad calculada, base de los rangos clínicos.
5. Teléfono y dirección, ambos opcionales.
6. Seguro médico.
7. Contacto de emergencia.
8. Ticket generado con formato T-AAAAMMDD-NNN y consecutivo diario.
