---
id: HU-22
titulo: 'HU-22 "Activar Alerta de Emergencia"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Alertas]
milestone: ""
---

## Historia de Usuario

**Como** médico o enfermera
**Quiero** activar una alerta de código rojo
**Para** movilizar recursos rápidamente

**Criterios de Aceptación:**
- Botón de emergencia visible siempre
- Al activar: notifica a todo el personal
- Incluye: ubicación, tipo de emergencia
- Temporizador de respuesta
- Registro completo del evento

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Sistema de alertas transversal, sin dependencias |
| **Negotiable** | Sí | Tipos de emergencia y reglas ajustables |
| **Valuable** | Sí | Movilización rápida, vidas en juego |
| **Estimable** | Sí | Botón + notificación masiva + registro |
| **Small** | Sí | Activación de alerta + notificación |
| **Testable** | Sí | Botón visible, notificación enviada, registro creado |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

## Wireframe Asociado

![Wireframe HU-22](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-22-activar-alerta.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-22-activar-alerta.svg)

**Leyenda del mockup:**

1. Botón siempre visible, presente en todas las pantallas.
2. Tipo de emergencia y ubicación.
3. Tiempo de respuesta contado desde la activación.
4. Registro del evento, inmutable una vez cerrado.
