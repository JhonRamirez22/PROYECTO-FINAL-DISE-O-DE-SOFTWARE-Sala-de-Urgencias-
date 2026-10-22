---
id: HU-25
titulo: 'HU-25 "Ver Dashboard Principal"'
tipo: historia
etiquetas: [HU, Sprint-3, Dashboard, historia-usuario, prioridad:media, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** administrador del servicio de urgencias
**Quiero** ver de un vistazo cuántos pacientes hay en cada etapa y cuánto tiempo llevan esperando
**Para** reasignar personal antes de que la espera se desborde, en lugar de descubrirlo al final del turno

**Criterios de Aceptación:**
- Contadores del día: en espera, en atención y atendidos
- Tiempo promedio de espera calculado solo sobre quienes siguen esperando
- Pacientes en espera ordenados por nivel de triaje y hora de llegada
- Alertas activas no atendidas, de cualquier módulo, ordenadas por antigüedad
- Hora de la última actualización y refresco automático del tablero
- Estado vacío explícito cuando no hay actividad en el día
- "Hoy" va de las 00:00 a las 23:59 en hora local del servidor

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Depende de que existan atenciones y triaje, no de otras historias nuevas |
| **Negotiable** | Sí | Los indicadores mostrados pueden reducirse o ampliarse |
| **Valuable** | Sí | Convierte los datos del día en decisiones de dotación |
| **Estimable** | Sí | Cuatro indicadores con reglas de cálculo explícitas |
| **Small** | Sí | 5 puntos: cuatro consultas agregadas y refresco |
| **Testable** | Sí | Cada indicador tiene una fórmula y un estado vacío definidos |

**Score INVEST:** 6/6
**Riesgo principal:** Indicadores mal calculados inducen decisiones de personal equivocadas.
**Sugerencia:** Congelar las fórmulas con pruebas de cálculo antes de publicar el tablero.

---

## Wireframe Asociado

![Wireframe HU-25](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-25-tablero-operativo.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-25-tablero-operativo.svg)

**Leyenda del mockup:**

1. Hora de la última actualización y acción para refrescar los datos.
2. Contadores del día: en espera, en atención y atendidos.
3. Tiempo promedio de espera de quienes siguen esperando.
4. Pacientes en espera ordenados por triaje y hora de llegada.
5. Alertas activas del servicio.
