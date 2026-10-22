---
id: HU-10
titulo: 'HU-10 "Visualizar Signos Vitales"'
tipo: historia
etiquetas: [HU, Sprint-2, Signos-Vitales, historia-usuario, prioridad:alta, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** médico o enfermera
**Quiero** ver el historial de signos vitales del paciente
**Para** evaluar tendencias y evolución

**Criterios de Aceptación:**
- Gráfica de tendencia por cada signo vital
- Tabla cronológica con todos los registros
- Filtro por rango de fechas
- Comparación entre registros

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-09 (datos de signos vitales) |
| **Negotiable** | Sí | Tipo de gráfica y filtros ajustables |
| **Valuable** | Sí | Evaluación de tendencias, decisión clínica |
| **Estimable** | Sí | Gráfica + tabla + filtro, patrones conocidos |
| **Small** | Sí | Visualización de datos existentes |
| **Testable** | Sí | Gráfica muestra datos, filtro funciona, comparación |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-09
**Sugerencia:** Ejecutar después de HU-09

---

## Wireframe Asociado

![Wireframe HU-10](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-10-visualizar-signos.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-10-visualizar-signos.svg)

**Leyenda del mockup:**

1. Cabecera del paciente con el triaje vigente.
2. Rango de fechas y pestañas por signo vital.
3. Gráfica de tendencia del signo seleccionado.
4. Tabla de registros del mismo rango, con quién registró cada toma.
