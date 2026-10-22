---
id: HU-23
titulo: 'HU-23 "Responder a Alerta"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Alertas]
milestone: ""
---

## Historia de Usuario

**Como** usuario notificado
**Quiero** confirmar recepción y llegada a emergencia
**Para** que el equipo sepa quién está respondiendo

**Criterios de Aceptación:**
- Botón "Respondiendo" con tiempo estimado
- Dashboard muestra quiénes están en camino
- Tiempo de respuesta promedio registrado
- Escalación si nadie responde en 5 min

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-22 (alerta activa para responder) |
| **Negotiable** | Sí | Tiempos de escalamiento y formato ajustables |
| **Valuable** | Sí | Coordinación de respuesta a emergencia |
| **Estimable** | Sí | Botón + dashboard + temporizador |
| **Small** | Sí | Respuesta a alerta existente |
| **Testable** | Sí | Responder, dashboard actualizado, escalamiento |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-22
**Sugerencia:** Ejecutar después de HU-22

---

## Wireframe Asociado

![Wireframe HU-23](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-23-responder-alerta.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-23-responder-alerta.svg)

**Leyenda del mockup:**

1. Alerta activa con tiempo transcurrido y estado de respuesta.
2. "Respondiendo" y tiempo estimado de llegada.
3. Quién está respondiendo, con su tiempo estimado.
4. Escalación automática si nadie responde en 5 minutos.
