---
id: HU-19
titulo: 'HU-19 "Configurar Notificaciones"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Notificaciones, historia-usuario, prioridad:media, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** usuario del sistema
**Quiero** configurar qué notificaciones recibo y cómo
**Para** personalizar mi experiencia

**Criterios de Aceptación:**
- Tipos: emergencias, asignaciones, recordatorios
- Canales: push, email, sonido
- Filtro por nivel de urgencia
- Horario de silencio configurable

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Configuración de usuario, sin dependencias de otras HUs |
| **Negotiable** | Sí | Tipos de notificación y canales ajustables |
| **Valuable** | Sí | Personalización de experiencia, reducir ruido |
| **Estimable** | Sí | Formulario de configuración + persistencia |
| **Small** | Sí | Configuración de preferencias |
| **Testable** | Sí | Configurar tipos, canales, horario silencio |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

## Wireframe Asociado

![Wireframe HU-19](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-19-configurar-notificaciones.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-19-configurar-notificaciones.svg)

**Leyenda del mockup:**

1. Matriz de tipos de notificación por canal.
2. Filtro por nivel de urgencia.
3. Horario de silencio; las emergencias siguen sonando.
