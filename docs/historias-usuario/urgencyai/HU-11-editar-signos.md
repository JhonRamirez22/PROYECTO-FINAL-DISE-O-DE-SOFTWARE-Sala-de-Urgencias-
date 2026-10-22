---
id: HU-11
titulo: 'HU-11 "Editar Signos Vitales"'
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-2, Signos-Vitales, historia-usuario, prioridad:media, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** enfermera
**Quiero** corregir registros de signos vitales erróneos
**Para** mantener la integridad de los datos clínicos

**Criterios de Aceptación:**
- Solo editable durante las primeras 2 horas
- Motivo de edición obligatorio
- Se preserva el registro original (audit trail)
- Notificación al médico si el paciente ya fue visto

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-09 (registros de signos vitales) |
| **Negotiable** | Sí | Ventana de tiempo y reglas ajustables |
| **Valuable** | Sí | Integridad de datos clínicos, corrección de errores |
| **Estimable** | Sí | Edición condicional + audit trail + notificación |
| **Small** | Sí | Lógica de edición con restricción temporal |
| **Testable** | Sí | Editar dentro/fuera de 2h, motivo obligatorio, audit |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-09
**Sugerencia:** Ejecutar después de HU-09

---

## Wireframe Asociado

![Wireframe HU-11](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-11-editar-signos.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-11-editar-signos.svg)

**Leyenda del mockup:**

1. Plazo de 2 horas para corregir; pasado el plazo el registro se bloquea.
2. Valores originales, que se conservan en la auditoría.
3. Valores corregidos.
4. Aviso al médico que ya evaluó al paciente.
