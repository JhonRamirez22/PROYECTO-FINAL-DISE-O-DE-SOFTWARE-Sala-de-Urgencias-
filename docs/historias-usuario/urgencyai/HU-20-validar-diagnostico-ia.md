---
id: HU-20
titulo: 'HU-20 "Validar Diagnóstico IA"'
tipo: historia
etiquetas: [HU, Sprint-3, Validación-IA, historia-usuario, prioridad:media, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** médico
**Quiero** validar o rechazar el diagnóstico sugerido por IA
**Para** asegurar la calidad del diagnóstico

**Criterios de Aceptación:**
- Formulario de validación: aceptar/rechazar/modificar
- Comentario clínico obligatorio
- El diagnóstico final queda registrado
- Métricas de precisión de IA se actualizan
- Auditoría completa de la decisión

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-15 (sugerencia IA) y HU-16 (revisión) |
| **Negotiable** | Sí | Formulario y reglas de validación ajustables |
| **Valuable** | Sí | Cierre del loop de validación humana-IA |
| **Estimable** | Sí | Formulario + registro + métricas |
| **Small** | Sí | Componente de validación con feedback |
| **Testable** | Sí | Aceptar, rechazar, modificar, métricas actualizadas |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-15 y HU-16 — cierre del loop
**Sugerencia:** Ejecutar después de ambas en Sprint 3

---

## Wireframe Asociado

![Wireframe HU-20](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-20-validar-diagnostico-ia.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-20-validar-diagnostico-ia.svg)

**Leyenda del mockup:**

1. Formulario de validación: aceptar, rechazar o modificar.
2. Precisión histórica del modelo, visible antes de decidir.
3. Validaciones registradas y casos revisados en el mes.
4. "Registrar validación" firma la decisión con nombre, rol y hora.
