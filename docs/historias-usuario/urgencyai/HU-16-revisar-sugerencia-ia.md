---
id: HU-16
titulo: 'HU-16 "Revisar Sugerencia IA"'
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, IA-Diagnóstico, historia-usuario, prioridad:media, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** médico
**Quiero** revisar y evaluar las sugerencias de IA
**Para** tomar una decisión informada

**Criterios de Aceptación:**
- Vista detallada de cada diagnóstico sugerido
- Opción de aceptar, rechazar o modificar
- Comentario obligatorio al rechazar
- Justificación clínica registrada
- La IA aprende de las decisiones del médico

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-15 (diagnósticos IA generados) |
| **Negotiable** | Sí | Formato de vista y opciones ajustables |
| **Valuable** | Sí | Validación humana del diagnóstico IA |
| **Estimable** | Sí | UI de revisión + feedback loop |
| **Small** | Sí | Componente de revisión con opciones |
| **Testable** | Sí | Aceptar, rechazar, modificar, comentario obligatorio |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-15 — flujo secuencial
**Sugerencia:** Ejecutar inmediatamente después de HU-15

---

## Wireframe Asociado

![Wireframe HU-16](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-16-revisar-sugerencia-ia.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-16-revisar-sugerencia-ia.svg)

**Leyenda del mockup:**

1. Sugerencias de la IA con nivel de confianza y severidad.
2. Acción del médico: aceptar, rechazar o modificar.
3. Comentario clínico obligatorio al rechazar.
4. "Registrar decisión" alimenta las métricas del modelo.
