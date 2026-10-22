---
id: EP-02
titulo: "EP-02 · Admisión y registro clínico"
tipo: epica
etiquetas: [epica, prioridad:alta, Gestión-Pacientes]
milestone: ""
---

# EP-02 · Admisión y registro clínico

**Objetivo:** que todo paciente que entra a urgencias quede identificado y con un registro objetivo de su estado clínico desde el primer contacto.

**Valor de negocio:** es el núcleo operativo del servicio. Sin admisión no hay cola, sin signos vitales no hay triaje, sin triaje no hay priorización. Todo lo demás del sistema cuelga de estas dos historias.

**Métrica de éxito:** 100 % de los pacientes atendidos con registro de admisión completo; primera toma de signos vitales registrada en menos de 5 minutos desde el ingreso.

## Historias

- [ ] HU-06 · Registrar paciente — 5 pts — Must (#6)
- [ ] HU-07 · Buscar paciente — 3 pts — Must (#7)
- [ ] HU-08 · Editar datos del paciente — 3 pts — Should (#8)
- [ ] HU-09 · Registrar signos vitales — 5 pts — Must (#9)
- [ ] HU-10 · Visualizar signos vitales — 5 pts — Must (#10)
- [ ] HU-11 · Editar signos vitales — 3 pts — Should (#11)
- [ ] HU-17 · Clasificar por triaje — 5 pts — Must (#17)

## Fuera de alcance de esta épica

- Gestión de la cola de espera (asignación de turnos de atención, llamado, reordenamiento). Hoy la cola solo se crea; administrarla es una épica pendiente.
- Rangos clínicos pediátricos (supuesto S-6).
- Historia clínica completa, antecedentes y alergias.

## Notas

HU-06 es el punto único de fallo del backlog: de ella dependen HU-07, HU-08, HU-09, HU-15 y HU-24. Debe cerrarse en el primer sprint, antes que cualquier otra historia de esta lista.
