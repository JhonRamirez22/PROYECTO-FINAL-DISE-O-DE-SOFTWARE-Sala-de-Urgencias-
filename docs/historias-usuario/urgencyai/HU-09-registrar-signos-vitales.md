---
id: HU-09
titulo: 'HU-09 "Registrar Signos Vitales"'
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-2, Signos-Vitales, historia-usuario, prioridad:alta, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** enfermera de triaje
**Quiero** registrar los signos vitales del paciente en cada toma
**Para** que exista evidencia clínica objetiva de su evolución y se detecten a tiempo los deterioros

**Criterios de Aceptación:**
- Registro de temperatura, presión arterial sistólica y diastólica, frecuencia cardíaca y respiratoria
- Peso y talla opcionales, con el IMC calculado por el sistema cuando existen ambos
- Solo se registra sobre una atención abierta
- Un valor fuera del rango fisiológico se rechaza; un valor crítico se guarda y genera alerta
- La presión diastólica debe ser estrictamente menor que la sistólica
- Los campos son opcionales individualmente, pero la toma exige al menos un valor
- La toma se clasifica como normal o crítica al guardar
- Los rangos aplicados son de adulto; pediatría queda fuera del alcance

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Requiere una atención abierta (HU-06), no otras historias |
| **Negotiable** | Sí | Los rangos exactos son parámetros clínicos ajustables |
| **Valuable** | Sí | Es el insumo del triaje y del diagnóstico asistido |
| **Estimable** | Sí | Siete campos con rangos, clasificación e IMC |
| **Small** | Sí | 5 puntos: formulario, validación de rangos y alerta |
| **Testable** | Sí | Cada rango y cada rechazo producen un resultado verificable |

**Score INVEST:** 6/6
**Riesgo principal:** Aplicar rangos de adulto a pacientes pediátricos.
**Sugerencia:** Dejar los rangos como parámetro y excluir pediatría del MVP de forma explícita.

---

## Wireframe Asociado

![Wireframe HU-09](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-09-registrar-signos-vitales.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-09-registrar-signos-vitales.svg)

**Leyenda del mockup:**

1. Temperatura en grados Celsius.
2. Presión arterial sistólica y diastólica en mmHg.
3. Frecuencia cardíaca y respiratoria.
4. Clasificación de la toma: normal o crítica.
5. Umbrales que disparan la alerta clínica al guardar.
6. Peso y talla, con el IMC calculado por el sistema.
