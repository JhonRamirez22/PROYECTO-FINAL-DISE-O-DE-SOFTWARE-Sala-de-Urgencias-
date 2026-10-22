---
id: HU-12a
titulo: 'HU-12a "Gestionar Catálogo de Medicamentos"'
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:alta, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** farmacéutico
**Quiero** mantener el catálogo de medicamentos que maneja el servicio
**Para** que todo el personal prescriba y dispense sobre la misma lista validada, sin nombres duplicados ni presentaciones ambiguas

**Criterios de Aceptación:**
- Alta con nombre, concentración, forma farmacéutica, principio activo y categoría
- Nombre, concentración y forma farmacéutica identifican el medicamento; no se admiten duplicados
- Nombre y concentración son inmutables tras el alta; un error se corrige desactivando y creando uno nuevo
- Búsqueda por nombre o principio activo
- No se elimina ningún medicamento: se desactiva con motivo obligatorio
- No se puede desactivar un medicamento con stock mayor que cero
- Los medicamentos inactivos no se ofrecen al dispensar, pero permanecen en el histórico
- La categoría pertenece a un catálogo cerrado: Analgésico, Antibiótico, Antiinflamatorio, Antihipertensivo u Otro

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Solo requiere el catálogo de categorías, que es fijo |
| **Negotiable** | Sí | La composición de la identidad del medicamento puede revisarse |
| **Valuable** | Sí | Sin catálogo no hay dispensación ni verificación de interacciones |
| **Estimable** | Sí | CRUD con regla de unicidad, desactivación lógica y búsqueda |
| **Small** | Sí | 3 puntos: formulario, listado y desactivación |
| **Testable** | Sí | Duplicado, desactivación con stock y búsqueda son verificables |

**Score INVEST:** 6/6
**Riesgo principal:** Un catálogo mal curado propaga errores a toda la farmacia.
**Sugerencia:** Exigir revisión de un segundo farmacéutico antes de publicar un medicamento nuevo.

---

## Wireframe Asociado

![Wireframe HU-12a](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-12a-catalogo-medicamentos.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-12a-catalogo-medicamentos.svg)

**Leyenda del mockup:**

1. Alta de un medicamento nuevo en el catálogo.
2. Búsqueda por nombre o principio activo.
3. Cada fila muestra stock y estado; los medicamentos inactivos no se dispensan.
4. Nombre y concentración se bloquean después del alta.
5. "Desactivar" retira el medicamento del catálogo sin borrar el historial.
