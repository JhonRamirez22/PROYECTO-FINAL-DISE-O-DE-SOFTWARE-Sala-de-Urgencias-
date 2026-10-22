---
id: HU-13
titulo: 'HU-13 "Registrar Dosis"'
tipo: historia
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:alta, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** farmacéutico
**Quiero** registrar la dosis dispensada a un paciente
**Para** controlar el consumo y evitar errores

**Criterios de Aceptación:**
- Selección de medicamento del inventario
- Cantidad, vía de administración, frecuencia
- Validación de stock disponible
- Descuento automático del inventario
- Asociación con prescripción médica

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-12 (inventario de medicamentos) |
| **Negotiable** | Sí | Campos y reglas de dispensación ajustables |
| **Valuable** | Sí | Control de consumo, prevención de errores |
| **Estimable** | Sí | Registro + validación stock + descuento |
| **Small** | Sí | Flujo de registro de dosis |
| **Testable** | Sí | Stock suficiente/insuficiente, descuento correcto |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-12
**Sugerencia:** Ejecutar después de HU-12

---

## Wireframe Asociado

![Wireframe HU-13](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-13-registrar-dosis.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-13-registrar-dosis.svg)

**Leyenda del mockup:**

1. Medicamento del catálogo; solo se ofrecen los activos.
2. Cantidad, vía y frecuencia de la dosis.
3. Prescripción asociada a la dosis.
4. Inventario: stock actual y stock tras la dispensación.
5. "Confirmar dosis" descuenta el stock del lote que vence antes.
6. Stock insuficiente: la dispensación se bloquea.
