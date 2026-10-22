---
id: HU-12
titulo: 'HU-12 "Gestionar Medicamentos"'
tipo: historia
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:alta, sp:8]
milestone: ""
---

## Historia de Usuario

**Como** farmacéutico
**Quiero** mantener el catálogo de medicamentos y el inventario por lotes del servicio
**Para** que todo el personal prescriba y dispense sobre la misma lista validada, sin duplicados, sin vencidos y sin quedarme sin stock en medio de una urgencia

**Criterios de Aceptación:**
- Alta con nombre, concentración, forma farmacéutica, principio activo y categoría
- Nombre, concentración y forma farmacéutica identifican el medicamento; no se admiten duplicados
- Nombre y concentración son inmutables tras el alta; un error se corrige desactivando y creando uno nuevo
- Búsqueda por nombre o principio activo
- No se elimina ningún medicamento: se desactiva con motivo obligatorio
- No se puede desactivar un medicamento con stock mayor que cero
- Los medicamentos inactivos no se ofrecen al dispensar, pero permanecen en el histórico
- La categoría pertenece a un catálogo cerrado: Analgésico, Antibiótico, Antiinflamatorio, Antihipertensivo u Otro
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
| **Independent** | Parcial | El catálogo es autónomo; la salida por lotes la consume HU-13 |
| **Negotiable** | Sí | La identidad del medicamento, el umbral por defecto y la política de alertas son ajustables |
| **Valuable** | Sí | Sin catálogo no hay dispensación, verificación de interacciones ni control de vencidos |
| **Estimable** | Sí | Dos bloques acotados: catálogo con unicidad y desactivación, e inventario con FEFO y umbral |
| **Small** | Parcial | 8 puntos: alta, búsqueda, desactivación lógica, lotes, FEFO y alertas en una sola historia |
| **Testable** | Sí | Duplicado, desactivación con stock, lote vencido, orden FEFO y stock negativo son deterministas |

**Score INVEST:** 5/6
**Riesgo principal:** Un catálogo mal curado y los ajustes manuales de inventario se propagan a toda la farmacia.
**Sugerencia:** Revisión de un segundo farmacéutico antes de publicar un medicamento nuevo, motivo obligatorio en cada ajuste y conciliación mensual del inventario.

---

## Wireframe Asociado

![Wireframe HU-12](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-12-gestionar-medicamentos.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-12-gestionar-medicamentos.svg)

**Leyenda del mockup:**

1. "Nuevo medicamento" da de alta el ítem; nombre y concentración quedan bloqueados después.
2. Búsqueda por nombre o principio activo.
3. Los inactivos no se ofrecen al dispensar y no se eliminan: solo se desactivan con motivo.
4. Stock total (excluye lotes vencidos) y stock mínimo configurable por medicamento.
5. Lotes ordenados por vencimiento: se dispensa primero el que vence antes (FEFO).
6. Un lote vencido no se dispensa aunque conserve unidades.
7. "Recibir lote" y "Ajustar inventario" exigen motivo y quedan auditados con autor y fecha.
8. Alertas de stock bajo: se emiten al cruzar el mínimo y se silencian hasta superarlo.
