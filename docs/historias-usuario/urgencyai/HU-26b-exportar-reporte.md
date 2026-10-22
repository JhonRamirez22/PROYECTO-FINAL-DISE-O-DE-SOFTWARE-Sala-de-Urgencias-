---
id: HU-26b
titulo: "HU-26b · Exportar reporte de atenciones"
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Dashboard, historia-usuario, prioridad:baja, sp:3]
milestone: ""
---
## Historia de usuario

> **Como** administrador del servicio
> **quiero** descargar el reporte que acabo de consultar en un archivo reutilizable
> **para** adjuntarlo al informe institucional sin volver a transcribir las cifras y arriesgarme a equivocarme.

**Épica:** EP-04 · Operación, seguimiento y cumplimiento
**Prioridad (MoSCoW):** Should. Es la razón práctica por la que existe el reporte: sin exportación, las cifras se copian a mano.
**Estimación:** 3 puntos. Dos formatos de salida sobre datos que ya están calculados.
**Origen:** "RF-24 | Exportar Reportes | Los reportes pueden exportarse en CSV o PDF." (alineado; el backlog original decía Excel)

## Criterios de aceptación

```gherkin
Característica: Exportación del reporte de atenciones

  Antecedentes:
    Dado que el administrador generó el reporte del 01/10/2026 al 21/10/2026

  Escenario: Exportación en CSV
    Cuando selecciona "Exportar CSV"
    Entonces se descarga "reporte-atenciones-20261001-20261021.csv"
    Y el archivo contiene una fila de encabezados
    Y contiene una fila por cada sección del reporte
    Y los valores coinciden exactamente con los mostrados en pantalla

  Escenario: Exportación en PDF
    Cuando selecciona "Exportar PDF"
    Entonces se descarga "reporte-atenciones-20261001-20261021.pdf"
    Y el documento incluye el título, el período, la fecha de generación y las tres secciones
    Y no incluye datos personales de pacientes

  Escenario: Exportación de un período sin datos
    Dado un período sin atenciones
    Cuando selecciona "Exportar CSV"
    Entonces el archivo contiene solo la fila de encabezados
    Y la pantalla advierte "El archivo no contiene atenciones"

  Escenario: Exportación sin reporte generado
    Cuando el administrador intenta exportar sin haber generado el reporte
    Entonces el sistema deshabilita los botones de exportación
    Y muestra "Genera el reporte antes de exportar"

  Escenario: Usuario sin permisos
    Dado un usuario con rol "Enfermera"
    Cuando intenta acceder a la exportación de reportes
    Entonces el sistema le deniega el acceso
```

**No funcionales**
- [ ] El archivo se genera en menos de 5 segundos con 5000 atenciones.
- [ ] El CSV se codifica en UTF-8 con BOM para que Excel abra bien las tildes.
- [ ] El PDF no supera 2 MB en un rango de 366 días.

## Wireframe

![Mockup HU-26b](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-26b-exportar-reporte.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Exportación en CSV, codificada en UTF-8 con BOM.
2. Exportación en PDF con título, período y fecha de generación.
3. Contenido del archivo: resumen, triaje y diagnósticos.
4. Los archivos no incluyen datos personales de pacientes.

## Reglas de negocio

- **RN-1:** Formatos soportados: **CSV y PDF**. Se descarta Excel (supuesto S-8, alineado con RF-24).
- **RN-2:** El nombre del archivo es `reporte-atenciones-AAAAMMDD-AAAAMMDD.<ext>`.
- **RN-3:** El contenido exportado debe ser idéntico al mostrado en pantalla para el mismo período.
- **RN-4:** El CSV usa UTF-8 con BOM y separador coma.
- **RN-5:** El PDF incluye título, período, fecha de generación y las tres secciones.
- **RN-6:** Ningún formato incluye datos personales de pacientes.
- **RN-7:** Solo el rol Administrador puede exportar.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Parcial | Requiere el reporte en pantalla (HU-26a). Dependencia declarada y natural. |
| **N**egociable | Sí | La librería de PDF y el diseño del documento quedan abiertos; los formatos y el contenido no. |
| **V**aliosa | Sí | Elimina la transcripción manual, que es la fuente real de errores en informes. |
| **E**stimable | Sí | Dos serializadores sobre datos ya calculados. |
| **S**mall (pequeña) | Sí | 3 puntos. |
| **T**esteable | Sí | Nombre de archivo, contenido y permisos son verificables. |

## Dependencias y notas

- **Depende de:** HU-26a (reporte en pantalla).
- **Notas para el equipo:**
  - El backlog original decía "PDF, Excel"; RF-24 dice "CSV o PDF". Se alinea con el requisito.
  - Si más adelante se pide Excel, es un tercer serializador sin cambios en el resto.

## Definición de terminado

- [ ] Los 5 escenarios pasan como pruebas automatizadas
- [ ] Verificado que el CSV se abre correctamente en Excel con tildes
- [ ] Verificado que el PDF no contiene datos personales
