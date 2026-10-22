---
id: HU-26a
titulo: "HU-26a · Consultar reporte de atenciones"
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Dashboard, historia-usuario, prioridad:media, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** administrador del servicio
> **quiero** consultar en pantalla el consolidado de atenciones de un período
> **para** sustentar decisiones de dotación y demostrar el volumen asistencial ante la dirección del hospital.

**Épica:** EP-04 · Operación, seguimiento y cumplimiento
**Prioridad (MoSCoW):** Should. Sin reporte no hay rendición de cuentas, pero no afecta la atención del paciente.
**Estimación:** 5 puntos. Cinco agregaciones sobre un rango de fechas con filtros y validaciones.
**Origen:** "RF-23 | Generar Reportes | El administrador puede generar reportes por rango de fechas, médico, diagnóstico y estadísticas de atención."

## Criterios de aceptación

```gherkin
Característica: Reporte de atenciones por período

  Antecedentes:
    Dado que el administrador "Carlos Peña" está autenticado

  Escenario: Consulta de un período con datos
    Cuando genera el reporte del 01/10/2026 al 21/10/2026
    Entonces ve el total de atenciones "312"
    Y la distribución por nivel de triaje (I a V) con sus porcentajes
    Y los 10 diagnósticos más frecuentes con su conteo
    Y el tiempo promedio de atención en minutos
    Y la fecha y hora de generación del reporte

  Escenario: Período sin atenciones
    Cuando genera el reporte del 01/01/2026 al 03/01/2026
    Entonces el sistema muestra "No hay atenciones registradas en este período"
    Y no muestra tablas vacías ni divisiones por cero

  Escenario: Rango de fechas invertido
    Cuando ingresa fecha inicial 21/10/2026 y fecha final 01/10/2026
    Entonces el sistema rechaza la consulta
    Y muestra "La fecha inicial debe ser anterior a la fecha final"

  Escenario: Rango superior al máximo permitido
    Cuando solicita un rango de 400 días
    Entonces el sistema rechaza la consulta
    Y muestra "El período máximo es de 366 días"

  Escenario: Coherencia con los registros
    Dado un período con 312 atenciones registradas
    Cuando el reporte muestra el total
    Entonces ese total coincide con el número de atenciones del período
    Y la suma de la distribución por triaje también suma 312
```

**No funcionales**
- [ ] El reporte se genera en menos de 3 segundos con 5000 atenciones en el rango.
- [ ] Los porcentajes se muestran con un decimal y suman 100 %.
- [ ] Las fechas se muestran en formato DD/MM/AAAA y hora local.

## Wireframe

![Mockup HU-26a](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-26a-reporte-atenciones.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Rango de fechas del reporte; máximo 366 días.
2. “Generar reporte” aplica el rango seleccionado.
3. Totales del período: atenciones y tiempo promedio.
4. Distribución por nivel de triaje con conteo y porcentaje.
5. Diagnósticos más frecuentes del período.
6. Fecha y hora de generación del reporte.

## Reglas de negocio

- **RN-1:** El rango máximo consultable es de **366 días**.
- **RN-2:** Una atención cuenta como "atendida" cuando tiene diagnóstico definitivo registrado.
- **RN-3:** Los diagnósticos frecuentes se agrupan por texto normalizado y se listan los 10 primeros.
- **RN-4:** El tiempo promedio de atención se calcula entre el inicio y el cierre de la atención, en minutos.
- **RN-5:** El reporte es de solo lectura: no se guarda ni se versiona.
- **RN-6:** No se filtra por médico ni por departamento (supuesto S-5): no existen esas entidades.
- **RN-7:** Los porcentajes se calculan sobre el total de atenciones del período.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Sí | Consume datos históricos; no requiere otra historia en curso. |
| **N**egociable | Sí | La disposición visual y el orden de las secciones quedan abiertos; las agregaciones no. |
| **V**aliosa | Sí | Es el insumo de la rendición de cuentas institucional. |
| **E**stimable | Sí | Cinco agregaciones con reglas explícitas y un rango acotado. |
| **S**mall (pequeña) | Sí | 5 puntos. La exportación se separó en HU-26b. |
| **T**esteable | Sí | Cifras, sumas y mensajes concretos. |

## Dependencias y notas

- **Depende de:** HU-06 (atenciones registradas), HU-09 y del registro de diagnósticos (HU-16/HU-20).
- **Notas para el equipo:**
  - Esta historia es la mitad consultiva del "HU-26 Generar Reportes" original; la exportación está en **HU-26b**. Reemplaza a la issue #26, que se cierra al publicarse esta división.
  - Se retiraron los tipos "diario, semanal, mensual": son el mismo reporte con distinto rango.
  - Se retiró "por médico" y "departamento" porque no existen esas entidades (supuesto S-5).
  - El wireframe SVG existente es `docs/wireframes/generar-reportes.svg`.

## Definición de terminado

- [ ] Los 5 escenarios pasan como pruebas automatizadas
- [ ] Verificada la coherencia entre el total y la suma por triaje con datos reales
- [ ] Interfaz validada contra el wireframe por el PO
