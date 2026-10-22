---
id: HU-07
titulo: 'HU-07 "Buscar Paciente"'
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-1, Gestión-Pacientes, historia-usuario, prioridad:alta, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** usuario del sistema
**Quiero** buscar pacientes por cédula o nombre
**Para** acceder rápidamente a su información

**Criterios de Aceptación:**
- Búsqueda por cédula (exacta) o nombre (parcial)
- Resultados en tiempo real (< 500ms)
- Muestra: nombre, cédula, edad, última visita
- Click en resultado abre perfil del paciente

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-06 (pacientes existentes) |
| **Negotiable** | Sí | Tipo de búsqueda y campos mostrados ajustables |
| **Valuable** | Sí | Acceso rápido a información del paciente |
| **Estimable** | Sí | Búsqueda con índice, patrón estándar |
| **Small** | Sí | Componente de búsqueda + resultados |
| **Testable** | Sí | Cédula exacta, nombre parcial, < 500ms |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-06
**Sugerencia:** Ejecutar después de HU-06

---

## Wireframe Asociado

![Wireframe HU-07](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-07-buscar-paciente.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-07-buscar-paciente.svg)

**Leyenda del mockup:**

1. Búsqueda por cédula exacta o nombre parcial, con respuesta en menos de 500 ms.
2. Resultados con nombre, cédula, edad y última visita.
3. Un clic sobre el resultado abre el perfil del paciente.
4. Estado vacío cuando no hay coincidencias.
