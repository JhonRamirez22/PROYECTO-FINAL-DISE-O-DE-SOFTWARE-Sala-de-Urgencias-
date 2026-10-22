---
id: HU-26b
titulo: 'HU-26b "Exportar Reporte de Atenciones"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Dashboard, historia-usuario, prioridad:baja, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** administrador del servicio
**Quiero** descargar el reporte que acabo de consultar en un archivo reutilizable
**Para** adjuntarlo al informe institucional sin volver a transcribir las cifras y arriesgarme a equivocarme

**Criterios de Aceptación:**
- Exportación en CSV codificado en UTF-8 con BOM y en PDF
- El nombre del archivo es reporte-atenciones-AAAAMMDD-AAAAMMDD.ext
- El contenido exportado es idéntico al mostrado en pantalla para el mismo período
- El PDF incluye título, período, fecha de generación y las tres secciones
- Ningún formato incluye datos personales de pacientes
- Sin un reporte generado previamente, la exportación no se habilita
- Solo el rol Administrador puede exportar

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Requiere el reporte en pantalla (HU-26a) |
| **Negotiable** | Sí | Se descartó Excel; los dos formatos restantes son fijos |
| **Valuable** | Sí | Evita transcribir cifras a mano en el informe institucional |
| **Estimable** | Sí | Dos formatos sobre datos que ya están calculados |
| **Small** | Sí | 3 puntos: dos serializadores y el control de permisos |
| **Testable** | Sí | El contenido debe coincidir con el de pantalla, byte a byte en CSV |

**Score INVEST:** 6/6
**Riesgo principal:** Exportar datos personales por error en alguno de los formatos.
**Sugerencia:** Pruebas que verifiquen la ausencia de datos personales en ambos archivos.

---

## Wireframe Asociado

![Wireframe HU-26b](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-26b-exportar-reporte.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-26b-exportar-reporte.svg)

**Leyenda del mockup:**

1. Exportación en CSV, codificada en UTF-8 con BOM.
2. Exportación en PDF con título, período y fecha de generación.
3. Contenido del archivo: resumen, triaje y diagnósticos.
4. Los archivos no incluyen datos personales de pacientes.
