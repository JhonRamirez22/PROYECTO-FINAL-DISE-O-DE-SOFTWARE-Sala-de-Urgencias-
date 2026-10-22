---
id: HU-26a
titulo: 'HU-26a "Consultar Reporte de Atenciones"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Dashboard, historia-usuario, prioridad:media, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** administrador del servicio
**Quiero** consultar en pantalla el consolidado de atenciones de un período
**Para** sustentar decisiones de dotación y demostrar el volumen asistencial ante la dirección del hospital

**Criterios de Aceptación:**
- Rango de fechas con un máximo consultable de 366 días
- Totales del período: número de atenciones y tiempo promedio de atención
- Distribución por nivel de triaje con conteo y porcentaje sobre el total del período
- Los 10 diagnósticos más frecuentes, agrupados por texto normalizado
- Una atención cuenta como atendida cuando tiene diagnóstico definitivo registrado
- Un período sin atenciones devuelve el reporte en cero, no un error
- Un rango invertido o superior al máximo se rechaza con un mensaje claro
- El reporte es de solo lectura: no se guarda ni se versiona

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Depende de atenciones, triaje y diagnósticos ya existentes |
| **Negotiable** | Sí | Los cortes del reporte son ajustables por la dirección |
| **Valuable** | Sí | Sin reporte no hay rendición de cuentas del servicio |
| **Estimable** | Sí | Cinco agregaciones sobre un rango acotado |
| **Small** | Sí | 5 puntos: filtros, cinco agregaciones y validaciones |
| **Testable** | Sí | Rango invertido, período vacío y coherencia con los registros |

**Score INVEST:** 6/6
**Riesgo principal:** Reportes que no cuadran con los registros operativos.
**Sugerencia:** Pruebas de coherencia que comparen el reporte contra la base de atenciones.

---

## Wireframe Asociado

![Wireframe HU-26a](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-26a-reporte-atenciones.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-26a-reporte-atenciones.svg)

**Leyenda del mockup:**

1. Rango de fechas del reporte; máximo 366 días.
2. "Generar reporte" aplica el rango seleccionado.
3. Totales del período: atenciones y tiempo promedio.
4. Distribución por nivel de triaje con conteo y porcentaje.
5. Diagnósticos más frecuentes del período.
6. Fecha y hora de generación del reporte.
