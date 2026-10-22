---
id: HU-21
titulo: 'HU-21 "Gestionar Insumos Médicos"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Insumos]
milestone: ""
---

## Historia de Usuario

**Como** administrador
**Quiero** controlar el inventario de insumos no medicamentos
**Para** garantizar disponibilidad operativa

**Criterios de Aceptación:**
- CRUD: guantes, jeringas, gasas, etc.
- Stock mínimo configurable
- Alertas de reabastecimiento
- Registro de consumo por turno
- Reporte de consumo mensual

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Módulo de insumos independiente de medicamentos |
| **Negotiable** | Sí | Tipos de insumos y reglas de alerta ajustables |
| **Valuable** | Sí | Disponibilidad de insumos, operación continua |
| **Estimable** | Sí | CRUD + alertas + reporte, patrones estándar |
| **Small** | Sí | Módulo CRUD completo pero acotado |
| **Testable** | Sí | CRUD, alertas stock bajo, consumo, reporte |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

## Wireframe Asociado

![Wireframe HU-21](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-21-gestionar-insumos.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-21-gestionar-insumos.svg)

**Leyenda del mockup:**

1. Búsqueda y filtro por categoría.
2. Tabla de insumos con stock, mínimo y estado.
3. Alerta de reabastecimiento cuando el stock cae bajo el mínimo.
4. Consumo del turno y reporte mensual exportable.
