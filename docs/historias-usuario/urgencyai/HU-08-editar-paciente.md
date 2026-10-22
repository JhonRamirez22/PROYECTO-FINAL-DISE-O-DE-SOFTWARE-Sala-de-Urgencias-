---
id: HU-08
titulo: 'HU-08 "Editar Datos del Paciente"'
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-1, Gestión-Pacientes, historia-usuario, prioridad:media, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** cajero o médico
**Quiero** actualizar información del paciente
**Para** mantener datos precisos

**Criterios de Aceptación:**
- Editar: teléfono, dirección, contacto de emergencia
- No editar: cédula (identificador único)
- Historial de modificaciones con timestamp
- Auditoría de quién hizo el cambio

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-06 (paciente registrado) |
| **Negotiable** | Sí | Campos editables y reglas ajustables |
| **Valuable** | Sí | Mantener datos del paciente actualizados |
| **Estimable** | Sí | Edición de campos + audit trail |
| **Small** | Sí | Formulario edición + historial |
| **Testable** | Sí | Editar campos válidos, bloquear cédula, audit |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-06
**Sugerencia:** Ejecutar después de HU-06

---

## Wireframe Asociado

![Wireframe HU-08](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-08-editar-paciente.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-08-editar-paciente.svg)

**Leyenda del mockup:**

1. Cédula no editable: es el identificador único del paciente.
2. Teléfono.
3. Dirección.
4. Contacto de emergencia.
5. Historial de modificaciones con fecha, usuario y campos afectados.
