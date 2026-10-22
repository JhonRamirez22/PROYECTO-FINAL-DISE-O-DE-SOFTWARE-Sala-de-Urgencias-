---
id: HU-18
titulo: 'HU-18 "Recibir Notificación de Emergencia"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Notificaciones]
milestone: ""
---

## Historia de Usuario

**Como** médico o enfermera
**Quiero** recibir alertas en tiempo real de pacientes críticos
**Para** responder rápidamente a emergencias

**Criterios de Aceptación:**
- Notificación push + sonido para pacientes Rojo/Naranja
- Aparece en panel de notificaciones
- Incluye: paciente, nivel, signos vitales clave
- Marcar como leída/atendida
- Historial de notificaciones

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Sistema de notificaciones independiente, WebSocket propio |
| **Negotiable** | Sí | Canales y formato de notificación ajustables |
| **Valuable** | Sí | Respuesta rápida a emergencias, vidas en juego |
| **Estimable** | Sí | WebSocket + UI de panel, patrón conocido |
| **Small** | Sí | Notificación en tiempo real + panel |
| **Testable** | Sí | Notificación recibida, sonido, panel actualizado |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

## Wireframe Asociado

![Wireframe HU-18](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-18-recibir-notificacion.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-18-recibir-notificacion.svg)

**Leyenda del mockup:**

1. Notificación emergente; llega con sonido si el nivel es Rojo o Naranja.
2. Lista de notificaciones con nivel y hora.
3. Acciones "Atender" y "Leída".
4. Estado de lectura de cada notificación.
