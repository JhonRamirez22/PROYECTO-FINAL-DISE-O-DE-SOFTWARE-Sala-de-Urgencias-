---
id: HU-06
titulo: "HU-06 · Registrar paciente en admisión"
tipo: historia
epica: EP-02
etiquetas: [HU, Sprint-1, Gestión-Pacientes, historia-usuario, prioridad:alta, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** cajero de admisión
> **quiero** registrar a la persona que llega a urgencias
> **para** que entre a la cola de atención con un identificador que permita seguirla durante toda su estancia.

**Épica:** EP-02 · Admisión y registro clínico
**Prioridad (MoSCoW):** Must. Es la puerta de entrada del sistema: sin admisión no hay cola, ni triaje, ni historia clínica.
**Estimación:** 5 puntos. Un formulario con siete campos, tres caminos de identificación (nuevo, existente, sin documento) y generación de ticket.
**Origen:** "RF-06 | Registrar Paciente | El cajero debe registrar un paciente con datos personales, contacto y seguro médico."

## Criterios de aceptación

```gherkin
Característica: Admisión de pacientes en urgencias

  Antecedentes:
    Dado que el cajero "Diego Salas" está autenticado en admisión

  Escenario: Registro de un paciente nuevo
    Cuando registra a "María López" con cédula 10293847, fecha de nacimiento 14/03/1985,
    teléfono 3105551234, seguro médico "Sura" y contacto de emergencia "Jorge López 3105559999"
    Entonces el sistema crea la ficha del paciente
    Y muestra el ticket "T-20261022-014"
    Y deja al paciente en estado "En espera" con la hora de registro 08:14
    Y muestra la edad calculada "41 años"

  Escenario: Cédula ya registrada
    Dado que existe un paciente con cédula 10293847
    Cuando el cajero intenta registrarlo de nuevo
    Entonces el sistema no crea una ficha duplicada
    Y muestra la ficha existente con nombre y edad
    Y ofrece la opción "Iniciar nueva atención"
    Y al confirmarla genera un ticket nuevo para la misma ficha

  Escenario: Paciente sin documento
    Cuando el cajero marca "Paciente sin documento" y registra el resto de los datos
    Entonces el sistema asigna el identificador temporal "SD-20261022-003"
    Y crea la ficha en estado "En espera"
    Y deja constancia de que la identificación está pendiente

  Escenario: Datos obligatorios faltantes
    Cuando el cajero envía el formulario sin contacto de emergencia
    Entonces el sistema no crea la ficha
    Y muestra "El contacto de emergencia es obligatorio" junto al campo

  Escenario: Fecha de nacimiento inválida
    Cuando el cajero ingresa la fecha de nacimiento 01/01/2030
    Entonces el sistema rechaza el registro
    Y muestra "La fecha de nacimiento no puede ser futura"

  Escenario: Paciente menor de edad
    Cuando el cajero registra a un paciente de 9 años
    Entonces el sistema exige el nombre del acompañante responsable
    Y no permite continuar sin ese dato
```

**No funcionales**
- [ ] El registro completo se confirma en menos de 2 segundos (RNF-07).
- [ ] El ticket es legible en voz alta y no contiene caracteres ambiguos.
- [ ] Los datos personales no aparecen en la URL ni en los registros del servidor.

## Wireframe

![Mockup HU-06](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-06-registrar-paciente.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Registro sin documento; habilita una identificación temporal.
2. Nombre completo del paciente.
3. Cédula; si ya existe se reutiliza la ficha y no se duplica el paciente.
4. Fecha de nacimiento y edad calculada, base de los rangos clínicos.
5. Teléfono y dirección, ambos opcionales.
6. Seguro médico.
7. Contacto de emergencia.
8. Ticket generado con formato T-AAAAMMDD-NNN y consecutivo diario.

## Reglas de negocio

- **RN-1:** La cédula es única. Se normaliza quitando puntos y espacios antes de comparar.
- **RN-2:** Si la cédula ya existe, **no se duplica la ficha**: se reutiliza y se abre una nueva atención.
- **RN-3:** El ticket tiene el formato `T-AAAAMMDD-NNN`, con consecutivo diario que reinicia en 001 a las 00:00.
- **RN-4:** Se almacena la fecha de nacimiento; la edad se calcula en cada consulta.
- **RN-5:** El seguro médico es obligatorio (RF-06).
- **RN-6:** Paciente sin documento: identificador `SD-AAAAMMDD-NNN` y marca de identificación pendiente.
- **RN-7:** Estado inicial "En espera"; la hora de registro la asigna el sistema.
- **RN-8:** Menor de 18 años exige acompañante responsable.
- **RN-9:** No se admiten fechas de nacimiento futuras ni edades superiores a 120 años.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Sí | No depende de ninguna otra historia funcional; solo de que el cajero esté autenticado. |
| **N**egociable | Sí | La disposición del formulario y el formato impreso del ticket quedan abiertos; los campos obligatorios y el formato del ticket no. |
| **V**aliosa | Sí | Sin admisión el paciente no existe para el sistema y no puede ser atendido. |
| **E**stimable | Sí | Entidad concreta, tres caminos de identificación y una regla de unicidad. |
| **S**mall (pequeña) | Sí | 5 puntos: un formulario con validaciones y generación de consecutivo. |
| **T**esteable | Sí | Ticket concreto, estados, mensajes exactos y edad calculada. |

## Dependencias y notas

- **Depende de:** HU-01 (autenticación del cajero).
- **Notas para el equipo:**
  - **HU-06 bloquea HU-07, HU-08, HU-09, HU-15 y HU-24.** Debe cerrarse primero.
  - La "cola de espera" se reduce a un **estado del paciente**; administrar la cola (llamar, reordenar) es una épica pendiente y no se incluye aquí.
  - El wireframe SVG existente es `docs/wireframes/registro-paciente.svg` (el original apuntaba a `registrar-paciente.svg`, inexistente).
  - La generación del consecutivo diario requiere control de concurrencia: dos cajeros registrando a la vez no deben obtener el mismo número.

## Definición de terminado

- [ ] Los 6 escenarios pasan como pruebas automatizadas
- [ ] Probada la concurrencia de dos registros simultáneos sin ticket repetido
- [ ] Interfaz validada contra el wireframe por el PO
