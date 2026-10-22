---
id: HU-24
titulo: "HU-24 · Consultar estado de atención"
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Asistencia-Paciente, historia-usuario, prioridad:media, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** familiar de un paciente que está siendo atendido
> **quiero** consultar en qué etapa va su atención con un código que me entregaron en admisión
> **para** saber si ya entró, cuánto falta y si debo acercarme, sin interrumpir al personal en cada momento.

**Épica:** EP-04 · Operación, seguimiento y cumplimiento
**Prioridad (MoSCoW):** Should. Mejora la experiencia y descongestiona el mostrador, pero el servicio funciona sin ella.
**Estimación:** 5 puntos. Vista pública, generación de código no enumerable, control de intentos y cálculo de tiempo estimado.
**Origen:** "RF-28 | Estado Pacientes Tiempo Real | El paciente o familiar puede consultar el estado de la atención."

## Criterios de aceptación

```gherkin
Característica: Consulta pública del estado de atención

  Antecedentes:
    Dado que en admisión se entregó el código "7K3M9QRT" al familiar de "María López"

  Escenario: Consulta con código válido
    Cuando el familiar ingresa el código "7K3M9QRT"
    Entonces el sistema muestra "En espera"
    Y muestra el nivel de triaje "Naranja (II)"
    Y muestra "2 personas antes que usted"
    Y muestra "Tiempo estimado: 25 minutos"
    Y no muestra el nombre completo, la cédula ni el diagnóstico

  Escenario: Código inexistente
    Cuando el familiar ingresa el código "ZZZZZZZZ"
    Entonces el sistema muestra "Código no válido o vencido"
    Y responde en el mismo tiempo que con un código válido

  Escenario: Exceso de intentos desde una misma conexión
    Dado que se realizaron 5 consultas fallidas en el último minuto desde la misma conexión
    Cuando se intenta una sexta consulta
    Entonces el sistema bloquea la consulta durante 15 minutos
    Y muestra "Demasiados intentos. Intenta más tarde."

  Escenario: Paciente dado de alta
    Dado que la atención de María finalizó con estado "Alta"
    Cuando el familiar consulta el código
    Entonces el sistema muestra "Atención finalizada"
    Y no muestra tiempo estimado
    Y el código deja de ser válido a los 7 días del alta

  Escenario: Intento de acceso a datos clínicos
    Cuando se inspecciona la respuesta de la consulta pública
    Entonces no aparece el nombre completo, la cédula, el diagnóstico,
    los signos vitales ni los medicamentos del paciente
```

**No funcionales**
- [ ] La página carga en menos de 2 segundos en un móvil con 3G.
- [ ] Es usable en pantalla de 360 px de ancho.
- [ ] No requiere autenticación y no expone identificadores internos del paciente en la URL.

## Wireframe

![Mockup HU-24](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-24-consultar-estado-atencion.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Código de seguimiento de 8 caracteres entregado en admisión.
2. Estado actual de la atención.
3. Nivel de triaje asignado.
4. Tiempo estimado de espera.
5. Hora de la última actualización del estado.
6. Aviso de privacidad: no se muestran datos clínicos ni personales.

## Reglas de negocio

- **RN-1:** El código tiene **8 caracteres** en alfabeto Crockford Base32 sin `0`, `O`, `1`, `I`, `L`, para que pueda dictarse por teléfono sin ambigüedad. Se genera aleatoriamente, no se deriva de datos del paciente.
- **RN-2:** Campos visibles: estado, nivel de triaje (nombre y número), personas por delante, tiempo estimado y hora de actualización. **Nunca**: nombre completo, cédula, diagnóstico, signos vitales ni medicamentos.
- **RN-3:** Código inexistente y código vencido producen **el mismo mensaje** y el mismo tiempo de respuesta, para no permitir enumeración.
- **RN-4:** Máximo 5 consultas por minuto por conexión; superado el límite, bloqueo de 15 minutos.
- **RN-5:** El código sigue válido hasta **7 días después del alta**; luego expira.
- **RN-6:** El tiempo estimado se calcula como *personas por delante × tiempo promedio de atención de las últimas 24 horas*. Si no hay datos suficientes, se muestra "No disponible".
- **RN-7:** La consulta **no requiere autenticación** (supuesto S-3) y no registra datos del consultante más allá de la IP para el control de intentos.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Parcial | Requiere paciente (HU-06) y triaje (HU-17). Aporta valor completo cuando ambas existen. |
| **N**egociable | Sí | La presentación y el formato del código quedan abiertos; la lista blanca de campos y el límite de intentos no. |
| **V**aliosa | Sí | Reduce interrupciones al personal y da certidumbre a la familia, que es el dolor real del proceso. |
| **E**stimable | Sí | Una vista pública, un cálculo y un control de intentos. |
| **S**mall (pequeña) | Sí | 5 puntos: sin autenticación y con una sola pantalla. |
| **T**esteable | Sí | La ausencia de campos sensibles es verificable inspeccionando la respuesta. |

## Dependencias y notas

- **Depende de:** HU-06 (paciente con ticket) y HU-17 (nivel de triaje).
- **Notas para el equipo:**
  - El backlog original decía "paciente **o** familiar", que no es un rol del sistema. Aquí el actor es el familiar y el acceso es público.
  - El estado "Alta" **no tiene historia que lo produzca**: es una dependencia abierta del backlog. Mientras no exista, la consulta nunca mostrará ese estado.
  - El wireframe SVG existente es `docs/wireframes/consultar-estado.svg`.
  - Esta es la única superficie sin autenticación del sistema: debe pasar revisión de seguridad antes de publicarse.

## Definición de terminado

- [ ] Los 5 escenarios pasan como pruebas automatizadas
- [ ] Revisión de seguridad del endpoint público aprobada
- [ ] Verificado que la respuesta JSON no contiene campos clínicos ni personales
- [ ] Interfaz validada contra el wireframe por el PO
