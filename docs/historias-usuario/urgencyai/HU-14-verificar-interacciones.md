---
id: HU-14
titulo: 'HU-14 "Verificar Interacciones"'
tipo: historia
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:media, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** farmacéutico
**Quiero** que el sistema contraste el medicamento que voy a dispensar con los que el paciente ya tiene activos
**Para** no provocar una reacción adversa que era evitable

**Criterios de Aceptación:**
- Contraste del medicamento a dispensar contra los medicamentos activos del paciente
- Severidad contraindicada: la dispensación queda bloqueada
- Severidad grave: exige justificación clínica de al menos 20 caracteres
- Severidad moderada: solo informa y permite continuar
- El par es no ordenado: "A + B" y "B + A" son la misma interacción
- Toda verificación se registra con la versión del catálogo utilizada, haya o no hallazgo
- La pantalla advierte siempre que la ausencia de interacción no garantiza inocuidad clínica

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Requiere catálogo (HU-12) y dispensación (HU-13) |
| **Negotiable** | Sí | El catálogo de pares y sus severidades son datos, no código |
| **Valuable** | Sí | Es la salvaguarda clínica de la dispensación |
| **Estimable** | Sí | Tres comportamientos definidos y un registro de decisión |
| **Small** | Sí | 5 puntos: consulta de pares, tres reglas y auditoría |
| **Testable** | Sí | Cada severidad produce una acción distinta y observable |

**Score INVEST:** 6/6
**Riesgo principal:** El catálogo local queda desactualizado frente a la evidencia clínica.
**Sugerencia:** Versionarlo y someterlo a revisión periódica del comité de farmacia.

---

## Wireframe Asociado

![Wireframe HU-14](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-14-verificar-interacciones.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-14-verificar-interacciones.svg)

**Leyenda del mockup:**

1. Par de medicamentos en conflicto, con su nivel de severidad.
2. Con severidad contraindicada la dispensación queda bloqueada.
3. Con severidad grave se exige justificación clínica de al menos 20 caracteres.
4. "Dispensar igual" se habilita solo con la justificación registrada.
