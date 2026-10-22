---
id: HU-09
titulo: "HU-09 · Registrar signos vitales"
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-2, Signos-Vitales, historia-usuario, prioridad:alta, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** enfermera de triaje
> **quiero** registrar los signos vitales del paciente en cada toma
> **para** que exista evidencia clínica objetiva de su evolución y se detecten a tiempo los deterioros.

**Épica:** EP-02 · Admisión y registro clínico
**Prioridad (MoSCoW):** Must. Es el insumo del triaje y del diagnóstico asistido; sin signos vitales el sistema es solo un registro administrativo.
**Estimación:** 5 puntos. Siete campos con validación de rango, clasificación en normal/crítico, cálculo de IMC y alerta.
**Origen:** "RF-09 | Registrar Signos Vitales | La enfermera debe registrar temperatura, presión arterial, frecuencia cardíaca, frecuencia respiratoria y saturación de oxígeno."

## Criterios de aceptación

```gherkin
Característica: Registro de signos vitales

  Antecedentes:
    Dado que la enfermera "Ana Ruiz" tiene abierta la atención del paciente "María López"

  Escenario: Registro dentro de rangos normales
    Cuando registra temperatura 36.8 °C, presión 120/80 mmHg, frecuencia cardíaca 72 lpm,
    frecuencia respiratoria 16 rpm, saturación 98 %, peso 68 kg y talla 162 cm
    Entonces el sistema guarda la toma con fecha y hora 08:20
    Y la asocia al paciente y a la atención abierta
    Y la clasifica como "Normal"
    Y muestra el IMC calculado 25.9
    Y no genera ninguna alerta

  Escenario: Valor fisiológicamente imposible
    Cuando la enfermera registra temperatura 45 °C
    Entonces el sistema rechaza la toma
    Y muestra "Temperatura fuera del rango aceptable (34.0 – 42.0 °C)"

  Escenario: Valor crítico
    Cuando la enfermera registra saturación 88 %
    Entonces el sistema guarda la toma igualmente
    Y la clasifica como "Crítico"
    Y muestra una alerta visible "Saturación por debajo de 90 %"
    Y la deja disponible para el módulo de notificaciones

  Escenario: Presión diastólica mayor o igual que la sistólica
    Cuando la enfermera registra presión 80/120 mmHg
    Entonces el sistema rechaza la toma
    Y muestra "La presión diastólica debe ser menor que la sistólica"

  Escenario: Toma sin atención abierta
    Dado que el paciente "María López" no tiene una atención en curso
    Cuando la enfermera intenta registrar signos vitales
    Entonces el sistema lo impide
    Y muestra "El paciente no tiene una atención abierta"

  Escenario: Registro parcial permitido
    Cuando la enfermera registra solo temperatura y saturación
    Entonces el sistema guarda la toma con los dos valores
    Y marca los campos restantes como "No registrado"
```

**No funcionales**
- [ ] El registro se confirma en menos de 2 segundos (RNF-07).
- [ ] Los valores se muestran con una decimal y la unidad correspondiente.
- [ ] La toma no se puede alterar sin pasar por HU-11.

## Wireframe

![Mockup HU-09](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-09-registrar-signos-vitales.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Temperatura en grados Celsius.
2. Presión arterial sistólica y diastólica en mmHg.
3. Frecuencia cardíaca y respiratoria.
4. Clasificación de la toma: normal o crítica.
5. Umbrales que disparan la alerta clínica al guardar.
6. Peso y talla, con el IMC calculado por el sistema.

## Reglas de negocio

**Rangos aceptables** (fuera de ellos la toma se rechaza) y **umbrales críticos** (dentro de lo aceptable, pero generan alerta):

| Signo | Unidad | Aceptable | Normal | Crítico |
|---|---|---|---|---|
| Temperatura | °C | 34.0 – 42.0 | 36.0 – 37.5 | < 35.0 o > 39.5 |
| Presión sistólica | mmHg | 50 – 300 | 90 – 140 | < 90 o > 180 |
| Presión diastólica | mmHg | 30 – 180 | 60 – 90 | > 110 |
| Frecuencia cardíaca | lpm | 20 – 250 | 60 – 100 | < 50 o > 120 |
| Frecuencia respiratoria | rpm | 4 – 60 | 12 – 20 | < 10 o > 30 |
| Saturación O₂ | % | 50 – 100 | 95 – 100 | < 90 |
| Peso | kg | 0.5 – 300 | — | — |
| Talla | cm | 30 – 250 | — | — |

- **RN-1:** Solo se registra sobre una atención abierta; la toma se asocia a esa atención, no a un "turno".
- **RN-2:** Un valor fuera del rango aceptable se rechaza; un valor crítico se guarda y genera alerta.
- **RN-3:** La presión diastólica debe ser estrictamente menor que la sistólica.
- **RN-4:** El IMC se calcula con peso y talla; si falta uno, no se muestra.
- **RN-5:** Los campos son opcionales individualmente, pero la toma debe tener al menos un valor.
- **RN-6:** Los rangos son de adulto; pediatría queda fuera del MVP (supuesto S-6).

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Sí | Depende de que exista una atención, no de otra historia funcional. |
| **N**egociable | Sí | La disposición del formulario y el componente de alerta quedan abiertos; los rangos y unidades no. |
| **V**aliosa | Sí | Convierte una toma manual en un dato clínico comparable y alertable. |
| **E**stimable | Sí | Ocho campos, una tabla de rangos y una clasificación determinista. |
| **S**mall (pequeña) | Sí | 5 puntos: formulario con validación numérica y cálculo de IMC. |
| **T**esteable | Sí | Cada rango tiene valores de borde explícitos. |

## Dependencias y notas

- **Depende de:** HU-06 (paciente registrado con atención).
- **Notas para el equipo:**
  - El backlog original decía "asociación con turno"; **no existe entidad de turno**. Se asocia a la atención.
  - El backlog original decía "pulso"; se corrige a **frecuencia cardíaca** según RF-09.
  - El wireframe SVG existente es `docs/wireframes/signos-vitales.svg` (el original apuntaba a `registrar-signos-vitales.svg`, inexistente).
  - La alerta se persiste como marca de la toma; su envío corresponde a HU-18.
  - Si se quiere pediatría, es una historia aparte con rangos por edad.

## Definición de terminado

- [ ] Los 6 escenarios pasan como pruebas automatizadas
- [ ] Los valores de borde de la tabla RN-1 están cubiertos por pruebas (34.0, 42.0, 89, 90, 120, 121…)
- [ ] Interfaz validada contra el wireframe por el PO
