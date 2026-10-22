---
id: HU-27
titulo: "HU-27 · Consultar auditoría de accesos"
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Seguridad, historia-usuario, prioridad:media, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** administrador del servicio
> **quiero** revisar quién accedió a los datos de un paciente, cuándo y desde dónde
> **para** detectar usos indebidos y poder responder con evidencia si alguien reclama por un acceso indebido.

**Épica:** EP-04 · Operación, seguimiento y cumplimiento
**Prioridad (MoSCoW):** Should. No cambia la atención, pero es la garantía de trazabilidad sobre datos clínicos.
**Estimación:** 5 puntos. Registro append-only, consulta con filtros, alerta de acceso fuera de jornada y exportación.
**Origen:** "RF-25 | Auditoría de Accesos | El administrador puede consultar el registro de accesos y acciones sobre datos sensibles."

## Criterios de aceptación

```gherkin
Característica: Auditoría de accesos y acciones

  Antecedentes:
    Dado que el administrador "Carlos Peña" está autenticado

  Escenario: Consulta del registro con filtros
    Cuando filtra por usuario "Ana Ruiz", acción "consulta_ficha" y el 21/10/2026
    Entonces ve cada evento con usuario, fecha y hora, acción, módulo e IP
    Y los resultados están ordenados del más reciente al más antiguo
    Y puede paginar de 20 en 20

  Escenario: Acceso a ficha de paciente registrado
    Dado que la enfermera "Ana Ruiz" abre la ficha de "María López"
    Cuando se consulta la auditoría
    Entonces aparece el evento "consulta_ficha" con el identificador de la atención
    Y con la hora exacta del acceso

  Escenario: Acceso fuera de la jornada institucional
    Dado que la jornada institucional está configurada de 06:00 a 22:00
    Cuando un usuario inicia sesión a las 23:30
    Entonces el sistema genera una alerta de acceso fuera de jornada
    Y el acceso queda registrado igualmente

  Escenario: Exportación del registro
    Cuando Carlos exporta el rango del 01/10/2026 al 21/10/2026
    Entonces descarga "auditoria-20261001-20261021.csv"
    Y el archivo contiene todos los eventos del rango, sin truncar

  Escenario: El registro es inmutable
    Dado un evento de auditoría registrado
    Cuando cualquier usuario intenta editarlo o eliminarlo
    Entonces el sistema no ofrece ninguna acción de edición o borrado
    Y el registro permanece intacto
```

**No funcionales**
- [ ] El registro se escribe sin bloquear la operación auditada.
- [ ] La consulta de un día completo con 10 000 eventos responde en menos de 3 segundos.
- [ ] Cada evento incluye zona horaria explícita.
- [ ] El registro es append-only: no admite `UPDATE` ni `DELETE` desde la aplicación.

## Wireframe

![Mockup HU-27](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-27-auditoria-accesos.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Filtros por usuario, acción y rango de fechas.
2. Exportación del resultado filtrado.
3. Registro de eventos con fecha, usuario, acción, módulo e IP.
4. Eventos fuera de la jornada institucional resaltados.
5. Resumen de anomalías del período consultado.
6. El registro es inmutable: no se edita ni se borra.

## Reglas de negocio

- **RN-1:** Eventos mínimos auditados: `login`, `logout`, alta y edición de usuario, `consulta_ficha`, dispensación y cambio de configuración.
- **RN-2:** Cada evento registra: usuario, fecha y hora con zona horaria, acción, módulo afectado, identificador del recurso e IP.
- **RN-3:** La jornada institucional es un parámetro configurable; por defecto **06:00 – 22:00**.
- **RN-4:** El registro es **append-only**: la aplicación no puede modificarlo ni eliminarlo.
- **RN-5:** La retención mínima es de **1 año**; se propone como RNF-21 y no como regla de esta historia.
- **RN-6:** La exportación es CSV en UTF-8 y solo la puede ejecutar el rol Administrador.
- **RN-7:** Un acceso denegado también se registra: la ausencia de registro no debe confundirse con ausencia de intento.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Parcial | Requiere que existan login (HU-01) y consulta de ficha. Dependencia declarada. |
| **N**egociable | Sí | La interfaz de consulta y el formato del CSV quedan abiertos; el catálogo de eventos y la inmutabilidad no. |
| **V**aliosa | Sí | Es la evidencia que protege a la institución y al paciente. |
| **E**stimable | Sí | Un catálogo cerrado de eventos, una consulta con filtros y una exportación. |
| **S**mall (pequeña) | Sí | 5 puntos. La política de retención se sacó a un RNF. |
| **T**esteable | Sí | Eventos, filtros y ausencia de acciones de edición son verificables. |

## Dependencias y notas

- **Depende de:** HU-01 (autenticación) y de que exista la consulta de ficha de paciente.
- **Notas para el equipo:**
  - El backlog original incluía "retención de datos: 1 año mínimo" como criterio de aceptación. **No es observable por el usuario**: se traslada a RNF-21.
  - El backlog original hablaba de "accesos fuera de horario" sin modelo de turnos; aquí se resuelve con una **jornada institucional configurable**, que sí es implementable hoy.
  - El wireframe SVG existente es `docs/wireframes/auditoria-accesos.svg`.

## Definición de terminado

- [ ] Los 5 escenarios pasan como pruebas automatizadas
- [ ] Verificado a nivel de base de datos que el usuario de la aplicación no puede hacer `UPDATE` ni `DELETE` sobre la tabla de auditoría
- [ ] `RNF-21` (retención) propuesto en `docs/requisitos.md`
- [ ] Interfaz validada contra el wireframe por el PO
