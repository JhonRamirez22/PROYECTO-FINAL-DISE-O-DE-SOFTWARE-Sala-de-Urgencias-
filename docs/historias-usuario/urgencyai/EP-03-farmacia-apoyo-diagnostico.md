---
id: EP-03
titulo: "EP-03 · Farmacia y apoyo a la decisión clínica"
tipo: epica
etiquetas: [epica, prioridad:media, Farmacología]
milestone: ""
---

# EP-03 · Farmacia y apoyo a la decisión clínica

**Objetivo:** que la farmacia opere con inventario confiable y que el médico reciba apoyo automatizado sin comprometer la seguridad del paciente.

**Valor de negocio:** dos riesgos clínicos concretos se atacan aquí: dispensar un medicamento vencido o sin stock, y dispensar una combinación peligrosa. El diagnóstico asistido por IA es valor incremental, no un requisito de operación.

**Métrica de éxito:** cero dispensaciones de lotes vencidos; 100 % de las interacciones contraindicadas bloqueadas; el tiempo de respuesta de la IA por debajo de 5 segundos en el percentil 95.

## Historias

- [ ] HU-12a · Gestionar catálogo de medicamentos — 3 pts — Must (#34)
- [ ] HU-12b · Controlar lotes y vencimientos — 5 pts — Should (#35)
- [ ] HU-13 · Registrar dosis — 5 pts — Must (#13)
- [ ] HU-14 · Verificar interacciones — 5 pts — Should (#14)
- [ ] HU-15 · Solicitar diagnóstico IA — 8 pts — Should (#15)
- [ ] HU-16 · Revisar sugerencia IA — 3 pts — Should (#16)
- [ ] HU-20 · Validar diagnóstico IA — 3 pts — Should (#20)

## Fuera de alcance de esta épica

- Prescripción médica como entidad propia (ausencia detectada en la auditoría; bloquea parcialmente a HU-14).
- Integración con una API externa de interacciones (supuesto S-2).
- Aprendizaje automático del modelo a partir de las validaciones del médico.

## Notas

HU-15 va al final del release a propósito. Es la historia de mayor incertidumbre técnica y el sistema es plenamente utilizable sin ella.
