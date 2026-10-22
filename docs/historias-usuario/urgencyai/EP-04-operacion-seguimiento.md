---
id: EP-04
titulo: "EP-04 · Operación, seguimiento y cumplimiento"
tipo: epica
etiquetas: [epica, prioridad:media, Dashboard]
milestone: ""
---

# EP-04 · Operación, seguimiento y cumplimiento

**Objetivo:** dar visibilidad del estado del servicio al administrador, al paciente y a la auditoría, sin exponer datos clínicos a quien no debe verlos.

**Valor de negocio:** cierra el ciclo. El administrador decide con datos, el familiar deja de preguntar en mostrador y la institución puede demostrar quién accedió a qué. Es lo que convierte un registro clínico en un sistema operable y auditable.

**Métrica de éxito:** el tablero responde en menos de 2 segundos con 500 atenciones activas; cero datos clínicos expuestos en la vista pública; 100 % de los accesos a ficha de paciente trazados.

## Historias

- [ ] HU-24 · Consultar estado de atención — 5 pts — Should
- [ ] HU-25 · Ver tablero operativo del servicio — 5 pts — Should
- [ ] HU-26a · Consultar reporte de atenciones — 5 pts — Should
- [ ] HU-26b · Exportar reporte de atenciones — 3 pts — Should
- [ ] HU-27 · Consultar auditoría de accesos — 5 pts — Should

## Fuera de alcance de esta épica

- Ocupación por área (requiere modelar áreas y camas; supuesto S-4).
- Reportes por médico o por departamento (supuesto S-5).
- Cuadro de mando en tiempo real con WebSocket: el refresco es por sondeo.

## Notas

HU-24 es la única historia del backlog con acceso sin autenticación. Su contrato de privacidad —qué se ve y qué no— está en las reglas de negocio y debe revisarse con cuidado antes de publicar la historia.
