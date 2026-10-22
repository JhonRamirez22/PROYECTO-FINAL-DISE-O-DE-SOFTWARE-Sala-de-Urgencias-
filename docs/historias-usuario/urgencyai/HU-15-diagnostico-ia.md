---
id: HU-15
titulo: "HU-15 · Obtener diagnóstico asistido por IA"
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, IA-Diagnóstico, historia-usuario, prioridad:media, sp:8]
milestone: ""
---
## Historia de usuario

> **Como** médico de urgencias
> **quiero** obtener una lista breve de diagnósticos diferenciales a partir de los síntomas y signos vitales del paciente
> **para** contrastarla con mi criterio antes de decidir, sobre todo en cuadros que no me resultan evidentes.

**Épica:** EP-03 · Farmacia y apoyo a la decisión clínica
**Prioridad (MoSCoW):** Should. Aporta valor diferencial, pero el servicio funciona sin ella: es la última historia del release.
**Estimación:** 8 puntos. Integración con un proveedor externo, contrato de respuesta, anonimización, manejo de fallos y registro de trazabilidad.
**Origen:** "RF-17 | Solicitar Diagnóstico IA | El médico solicita análisis de IA con síntomas y signos vitales del paciente." y "RF-18 | Mostrar Diagnósticos | Se muestran diagnósticos diferenciales con nivel de confianza."

## Criterios de aceptación

```gherkin
Característica: Diagnóstico asistido por IA

  Antecedentes:
    Dado que el médico "Andrés Rojas" tiene abierta la atención de "María López"

  Escenario: Solicitud exitosa
    Dado que María tiene registrados síntomas "fiebre 39 °C, tos seca, disnea"
    Y signos vitales con temperatura 39.1 °C, frecuencia cardíaca 112 lpm y saturación 91 %
    Cuando el médico solicita el diagnóstico asistido
    Entonces el sistema devuelve 4 diagnósticos diferenciales
    Y cada uno muestra nombre, nivel de confianza y recomendación
    Y la respuesta llega en menos de 5 segundos
    Y el resultado se marca como "Sugerencia de IA — no constituye diagnóstico"

  Escenario: Datos clínicos insuficientes
    Dado un paciente sin signos vitales registrados
    Cuando el médico solicita el diagnóstico asistido
    Entonces el sistema no envía la solicitud
    Y muestra "Faltan signos vitales para generar una sugerencia"
    Y enumera los datos mínimos requeridos

  Escenario: Falla del proveedor de IA
    Dado que el proveedor responde con error o no responde en 5 segundos
    Cuando el médico solicita el diagnóstico
    Entonces el sistema muestra "No fue posible obtener la sugerencia. Intenta de nuevo."
    Y ofrece "Reintentar"
    Y registra el incidente con la latencia y el código de error
    Y no bloquea la atención del paciente

  Escenario: Respuesta que no cumple el contrato
    Dado que el proveedor devuelve un diagnóstico sin nivel de confianza
    Cuando el sistema valida la respuesta
    Entonces la descarta por completo
    Y muestra el mismo mensaje de fallo
    Y registra el incidente como "respuesta inválida"

  Escenario: Anonimización de datos enviados
    Cuando el médico solicita el diagnóstico de "María López", cédula 10293847
    Entonces la solicitud enviada al proveedor no contiene nombre ni cédula
    Y solo incluye edad, sexo, síntomas y signos vitales
```

**No funcionales**
- [ ] El percentil 95 de latencia es inferior a 5 segundos (RNF-08).
- [ ] Ningún dato identificativo del paciente abandona el servidor (nombre, cédula, teléfono, dirección).
- [ ] Si el proveedor está caído, la pantalla responde en menos de 1 segundo con el mensaje de error.
- [ ] Se registra proveedor, modelo, versión y latencia de cada llamada, sin contenido clínico.

## Wireframe

![Mockup HU-15](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-15-diagnostico-ia.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Síntomas reportados por el médico; entrada principal de la sugerencia.
2. Resumen exacto de los datos clínicos que se envían al modelo.
3. “Solicitar diagnóstico asistido” envía la solicitud y espera la respuesta.
4. Aviso permanente de que la salida no constituye diagnóstico.
5. Entre 3 y 5 diagnósticos con nivel de confianza y recomendación.

## Reglas de negocio

- **RN-1:** La entrada es **síntomas + signos vitales de la atención** y el contexto anonimizado (edad, sexo). No se envían nombre, cédula, teléfono ni dirección.
- **RN-2:** La respuesta válida contiene entre **3 y 5** diagnósticos, cada uno con nombre, confianza de 0 a 100 y recomendación.
- **RN-3:** El tiempo máximo de espera es **5 segundos** (RNF-08), no los 10 del backlog original.
- **RN-4:** Una respuesta que no cumple el contrato se descarta completa; nunca se muestra parcialmente.
- **RN-5:** La sugerencia **no** se guarda como diagnóstico del paciente; solo como sugerencia asociada a la atención.
- **RN-6:** Datos mínimos para solicitar: al menos una toma de signos vitales y síntomas descritos.
- **RN-7:** Cada llamada se audita con proveedor, modelo, versión y latencia; el contenido clínico no se registra en el log.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Parcial | Requiere paciente (HU-06) y signos vitales (HU-09). Aporta valor por sí sola una vez que existen. |
| **N**egociable | Sí | El proveedor concreto y el modelo quedan abiertos; el contrato de respuesta y el límite de 5 s no. |
| **V**aliosa | Sí | Apoyo a la decisión en cuadros difíciles, que es el valor diferencial del producto. |
| **E**stimable | Sí | Con el contrato de respuesta y el timeout definidos, el alcance es acotado. |
| **S**mall (pequeña) | Sí | 8 puntos: en el límite superior, pero una sola integración. |
| **T**esteable | Sí | Número de diagnósticos, latencia, mensajes y contenido del payload son verificables. |

## Dependencias y notas

- **Depende de:** HU-06 (paciente) y HU-09 (signos vitales).
- **Notas para el equipo:**
  - El backlog original enviaba "historial y alergias": **ninguno de los dos existe** en el sistema. Se eliminaron del alcance.
  - El backlog original pedía "exámenes complementarios"; aquí se reduce a una recomendación textual por diagnóstico.
  - El backlog original sugería dividir en "enviar" y "recibir". **No se dividió** porque sería una división por capas, no por valor (ver `references/invest.md`, SPIDR).
  - La anonimización es un requisito de privacidad, no un detalle: si el proveedor es externo, no puede recibir PII.
  - El wireframe SVG existente es `docs/wireframes/diagnostico-ia.svg`.

## Definición de terminado

- [ ] Los 5 escenarios pasan como pruebas automatizadas, con proveedor simulado
- [ ] Verificado por inspección del payload que no viaja ningún dato identificativo
- [ ] Probado el comportamiento con el proveedor caído
- [ ] Interfaz validada contra el wireframe por el PO
