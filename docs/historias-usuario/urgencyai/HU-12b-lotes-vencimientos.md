---
id: HU-12b
titulo: 'HU-12b "Controlar Lotes y Vencimientos"'
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:media, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** farmacéutico
**Quiero** que el inventario se lleve por lotes con su fecha de vencimiento y que avise cuando un medicamento esté por agotarse
**Para** no dispensar medicamentos vencidos ni quedarme sin existencias en medio de una urgencia

**Criterios de Aceptación:**
- Recepción de lotes con cantidad, fecha de vencimiento y proveedor
- Salida FEFO: se dispensa primero el lote que vence antes
- Un lote vencido no se dispensa aunque conserve unidades
- Stock mínimo configurable por medicamento; por defecto 10 unidades
- La alerta de stock bajo se emite al cruzar el umbral hacia abajo y se silencia hasta superarlo
- El stock nunca puede ser negativo; la validación es transaccional
- Todo ajuste manual exige motivo y queda auditado con autor y fecha
- El stock mostrado excluye los lotes vencidos

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Requiere el catálogo (HU-12a) y la dispensación (HU-13) |
| **Negotiable** | Sí | El umbral por defecto y la política de alertas son ajustables |
| **Valuable** | Sí | Evita dispensar vencidos y quedarse sin stock en una urgencia |
| **Estimable** | Sí | Recepción de lotes, salida FEFO, umbral y alerta |
| **Small** | Sí | 5 puntos: lotes, FEFO, umbral y ajustes auditados |
| **Testable** | Sí | Lote vencido, orden FEFO y stock negativo son casos deterministas |

**Score INVEST:** 6/6
**Riesgo principal:** Ajustes manuales de inventario sin control.
**Sugerencia:** Motivo obligatorio y auditoría de cada ajuste, con revisión mensual.

---

## Wireframe Asociado

![Wireframe HU-12b](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-12b-lotes-vencimientos.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-12b-lotes-vencimientos.svg)

**Leyenda del mockup:**

1. Stock total de lotes no vencidos y stock mínimo configurable.
2. Lotes ordenados por vencimiento: el que vence antes sale primero (FEFO).
3. Un lote vencido no se dispensa aunque conserve unidades.
4. "Recibir lote" y "Ajustar inventario" registran usuario, hora y motivo.
5. Alertas generadas cuando el stock cae por debajo del mínimo.
