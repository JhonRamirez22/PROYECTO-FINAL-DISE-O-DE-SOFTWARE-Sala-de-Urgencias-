---
id: HU-26
titulo: 'HU-26 "Generar Reportes"'
tipo: historia
etiquetas: [HU, Sprint-3, Dashboard, historia-usuario, prioridad:media, sp:8]
milestone: ""
---

## Historia de Usuario

**Como** administrador del servicio
**Quiero** consultar el consolidado de atenciones de un período y descargarlo en un archivo reutilizable
**Para** sustentar decisiones de dotación y adjuntar las cifras al informe institucional sin transcribirlas y arriesgarme a equivocarme

**Criterios de Aceptación:**
- Rango de fechas con un máximo consultable de 366 días
- Totales del período: número de atenciones y tiempo promedio de atención
- Distribución por nivel de triaje con conteo y porcentaje sobre el total del período
- Los 10 diagnósticos más frecuentes, agrupados por texto normalizado
- Una atención cuenta como atendida cuando tiene diagnóstico definitivo registrado
- Un período sin atenciones devuelve el reporte en cero, no un error
- Un rango invertido o superior al máximo se rechaza con un mensaje claro
- Exportación en CSV codificado en UTF-8 con BOM y en PDF
- El nombre del archivo es reporte-atenciones-AAAAMMDD-AAAAMMDD.ext
- El contenido exportado es idéntico al mostrado en pantalla para el mismo período
- El PDF incluye título, período, fecha de generación y las tres secciones
- Ningún formato incluye datos personales de pacientes
- Sin un reporte generado previamente, la exportación no se habilita
- Solo el rol Administrador puede consultar y exportar

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Depende de atenciones, triaje y diagnósticos ya existentes |
| **Negotiable** | Sí | Los cortes del reporte son ajustables por la dirección y se descartó Excel |
| **Valuable** | Sí | Sin reporte no hay rendición de cuentas ni informe institucional |
| **Estimable** | Sí | Cinco agregaciones sobre un rango acotado y dos serializadores |
| **Small** | Parcial | 8 puntos: consulta con cinco agregaciones más exportación CSV y PDF |
| **Testable** | Sí | Rango invertido, período vacío, coherencia con los registros y ausencia de datos personales |

**Score INVEST:** 5/6
**Riesgo principal:** Reportes que no cuadran con los registros operativos o que filtran datos personales al exportar.
**Sugerencia:** Pruebas de coherencia contra la base de atenciones y verificación de ausencia de datos personales en ambos formatos antes de publicar.

---

## Wireframe Asociado

![Wireframe HU-26](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-26-generar-reportes.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-26-generar-reportes.svg)

**Leyenda del mockup:**

1. Rango de fechas del reporte; máximo 366 días.
2. "Generar reporte" aplica el rango y recalcula todas las secciones.
3. Totales del período: atenciones y tiempo promedio.
4. Distribución por nivel de triaje con conteo y porcentaje sobre el total.
5. Diagnósticos más frecuentes agrupados por texto normalizado.
6. Fecha y hora de generación del reporte.
7. "Exportar CSV" (UTF-8 con BOM) y "Exportar PDF"; solo el rol Administrador.
8. Nombre del archivo reporte-atenciones-AAAAMMDD-AAAAMMDD.ext; ningún formato incluye datos personales.
