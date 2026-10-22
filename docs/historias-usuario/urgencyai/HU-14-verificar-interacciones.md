---
id: HU-14
titulo: "HU-14 · Verificar interacciones medicamentosas"
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:media, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** farmacéutico
> **quiero** que el sistema contraste el medicamento que voy a dispensar con los que el paciente ya tiene activos
> **para** no provocar una reacción adversa que era evitable.

**Épica:** EP-03 · Farmacia y apoyo a la decisión clínica
**Prioridad (MoSCoW):** Should. El sistema opera sin esto, pero es la salvaguarda clínica de la dispensación.
**Estimación:** 5 puntos. Catálogo de pares con severidad, tres comportamientos distintos y registro de la decisión.
**Origen:** "RF-13 | Verificar Interacciones | El farmacéutico o médico debe verificar interacciones medicamentosas antes de dispensar."

## Criterios de aceptación

```gherkin
Característica: Verificación de interacciones medicamentosas

  Antecedentes:
    Dado que el paciente "María López" tiene una atención abierta

  Escenario: Interacción contraindicada
    Dado que María tiene dispensada "Warfarina 5 mg"
    Y el catálogo registra la interacción "Warfarina + Aspirina" como contraindicada
    Cuando el farmacéutico intenta dispensar "Aspirina 100 mg"
    Entonces el sistema bloquea la dispensación
    Y muestra "Interacción contraindicada: Warfarina + Aspirina"
    Y no permite continuar

  Escenario: Interacción grave con justificación
    Dado que María tiene dispensada "Ibuprofeno 400 mg"
    Y el catálogo registra "Ibuprofeno + Enalapril" como grave
    Cuando el farmacéutico intenta dispensar "Enalapril 10 mg"
    Entonces el sistema muestra una confirmación obligatoria
    Y exige una justificación de al menos 20 caracteres
    Y solo dispensa si se confirma
    Y registra la justificación con autor y fecha

  Escenario: Interacción moderada
    Dado que el catálogo registra "Omeprazol + Clopidogrel" como moderada
    Cuando el farmacéutico intenta dispensar "Clopidogrel 75 mg"
    Entonces el sistema muestra una advertencia informativa
    Y permite continuar sin justificación
    Y registra que la advertencia fue mostrada

  Escenario: Sin interacción registrada
    Dado que María no tiene medicamentos activos
    Cuando el farmacéutico dispensa "Paracetamol 500 mg"
    Entonces el sistema no muestra ninguna alerta
    Y registra la verificación con la versión del catálogo utilizada
```

**No funcionales**
- [ ] La verificación añade menos de 300 ms a la dispensación con un catálogo de 5000 pares.
- [ ] El texto de la alerta identifica los dos medicamentos y la severidad.
- [ ] La advertencia es visible sin depender del color (texto y símbolo, no solo rojo).

## Wireframe

![Mockup HU-14](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-14-verificar-interacciones.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Par de medicamentos en conflicto, con su nivel de severidad.
2. Con severidad contraindicada la dispensación queda bloqueada.
3. Con severidad grave se exige justificación clínica de al menos 20 caracteres.
4. “Dispensar igual” se habilita solo con la justificación registrada.

## Reglas de negocio

- **RN-1:** La fuente es un **catálogo local versionado** de pares de principios activos con severidad: `contraindicada`, `grave`, `moderada` (supuesto S-2).
- **RN-2:** El par es no ordenado: "A + B" y "B + A" son la misma interacción.
- **RN-3:** "Medicamentos activos" son los dispensados en la atención abierta y no suspendidos.
- **RN-4:** Contraindicada **bloquea**; grave exige justificación de 20 caracteres o más; moderada solo informa.
- **RN-5:** Toda verificación —con o sin hallazgo— se registra con la versión del catálogo utilizada.
- **RN-6:** La ausencia de una interacción en el catálogo **no garantiza inocuidad clínica**; la pantalla lo advierte siempre al pie.
- **RN-7:** La verificación ocurre en la dispensación, no en la prescripción (supuesto S-7).

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Parcial | Requiere el catálogo de medicamentos (HU-12a) y el flujo de dispensación (HU-13). Dependencia declarada. |
| **N**egociable | Sí | La presentación de la alerta y el origen futuro del catálogo quedan abiertos; las severidades y sus efectos no. |
| **V**aliosa | Sí | Previene reacciones adversas evitables, que es un objetivo clínico de primer orden. |
| **E**stimable | Sí | Con la fuente resuelta (catálogo local) el alcance es una consulta y tres comportamientos. |
| **S**mall (pequeña) | Sí | 5 puntos: tabla de pares, consulta y tres modales. |
| **T**esteable | Sí | Cada severidad tiene un comportamiento observable y distinto. |

## Dependencias y notas

- **Depende de:** HU-12a (catálogo) y HU-13 · Registrar dispensación.
- **Notas para el equipo:**
  - El backlog original decía "sugerencia de alternativa **cuando sea posible**", que no es verificable. Aquí las alternativas son solo informativas y quedan fuera de los criterios de aceptación.
  - El backlog original decía "farmacéutico **o médico**": se acota a farmacéutico porque la verificación ocurre en la dispensación.
  - **RF-16** (responder alertas de stock) sigue sin historia; no se mezcla con esta.
  - La carga inicial del catálogo es un archivo semilla versionado en el repositorio.

## Definición de terminado

- [ ] Los 4 escenarios pasan como pruebas automatizadas
- [ ] Probado que el par se detecta en ambos órdenes (A+B y B+A)
- [ ] Interfaz validada contra el wireframe por el PO
