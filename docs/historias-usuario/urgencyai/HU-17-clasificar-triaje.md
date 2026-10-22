---
id: HU-17
titulo: 'HU-17 "Clasificar por Triaje"'
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-3, Triaje, historia-usuario, prioridad:alta, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** enfermera
**Quiero** clasificar pacientes por nivel de urgencia
**Para** priorizar la atención según gravedad

**Criterios de Aceptación:**
- Escala de triaje: Rojo (I), Naranja (II), Amarillo (III), Verde (IV), Azul (V)
- Basado en signos vitales + síntomas reportados
- Asignación automática sugerida por IA
- Override manual con justificación
- Reclasificación automática si signos vitales cambian

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-09 (signos vitales) y HU-15 (IA para sugerencia) |
| **Negotiable** | Sí | Escala de triaje y reglas ajustables |
| **Valuable** | Sí | Priorización de atención, crítico para urgencias |
| **Estimable** | Sí | Algoritmo de clasificación + override manual |
| **Small** | Sí | Clasificación + UI de override |
| **Testable** | Sí | Asignación por IA, override manual, reclasificación |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-09 y HU-15
**Sugerencia:** Ejecutar en Sprint 3 después de ambas dependencias

---

## Wireframe Asociado

![Wireframe HU-17](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-17-clasificar-triaje.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-17-clasificar-triaje.svg)

**Leyenda del mockup:**

1. Escala de triaje de cinco niveles; el sugerido se resalta.
2. Sugerencia de la IA, que no se aplica sin confirmación del personal.
3. Override manual con justificación obligatoria.
4. Reclasificación automática cuando los signos vitales cambian de rango.
