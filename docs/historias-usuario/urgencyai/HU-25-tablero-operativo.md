---
id: HU-25
titulo: "HU-25 · Ver tablero operativo del servicio"
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Dashboard, historia-usuario, prioridad:media, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** administrador del servicio de urgencias
> **quiero** ver de un vistazo cuántos pacientes hay en cada etapa y cuánto tiempo llevan esperando
> **para** reasignar personal antes de que la espera se desborde, en lugar de descubrirlo al final del turno.

**Épica:** EP-04 · Operación, seguimiento y cumplimiento
**Prioridad (MoSCoW):** Should. No bloquea la operación clínica, pero es lo que convierte los datos en decisiones.
**Estimación:** 5 puntos. Cuatro indicadores calculados, refresco automático y estado vacío.
**Origen:** "RF-28 | Estado Pacientes Tiempo Real" (visión agregada) y necesidad operativa del rol administrador.

## Criterios de aceptación

```gherkin
Característica: Tablero operativo del servicio

  Antecedentes:
    Dado que el administrador "Carlos Peña" está autenticado
    Y hoy se registraron 40 pacientes en admisión

  Escenario: Indicadores del día
    Cuando Carlos abre el tablero a las 11:00
    Entonces ve "En espera: 12", "En atención: 7", "Atendidos: 21"
    Y los tres valores suman los 40 pacientes del día
    Y ve el tiempo promedio de espera de los pacientes que siguen esperando

  Escenario: Cálculo del tiempo promedio de espera
    Dado que hay tres pacientes en espera con 10, 20 y 40 minutos de espera
    Cuando se calcula el promedio
    Entonces el tablero muestra "23 minutos"

  Escenario: Día sin actividad
    Dado que hoy no se registró ningún paciente
    Cuando Carlos abre el tablero
    Entonces los tres indicadores muestran 0
    Y aparece "Sin actividad registrada hoy"
    Y no se muestran gráficas vacías

  Escenario: Alertas activas
    Dado que existe una alerta de stock bajo sin atender
    Cuando Carlos abre el tablero
    Entonces la alerta aparece en la lista de alertas activas
    Y muestra el módulo de origen y la hora

  Escenario: Actualización automática
    Dado que el tablero está abierto
    Cuando transcurren 30 segundos
    Entonces los indicadores se actualizan sin recargar la página
    Y se muestra la hora de la última actualización
```

**No funcionales**
- [ ] El tablero se carga en menos de 2 segundos con 500 atenciones activas.
- [ ] El refresco automático no interrumpe la interacción del usuario.
- [ ] Los indicadores son legibles sin depender del color.

## Wireframe

![Mockup HU-25](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-25-tablero-operativo.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Hora de la última actualización y acción para refrescar los datos.
2. Contadores del día: en espera, en atención y atendidos.
3. Tiempo promedio de espera de quienes siguen esperando.
4. Pacientes en espera ordenados por triaje y hora de llegada.
5. Alertas activas del servicio.

## Reglas de negocio

- **RN-1:** "Hoy" va de las 00:00 a las 23:59 en hora local del servidor.
- **RN-2:** Los estados del paciente son excluyentes: `En espera`, `En atención`, `Atendido`, `Alta`.
- **RN-3:** El tiempo de espera de un paciente es la diferencia entre ahora y la hora de registro, solo para quienes están en `En espera`.
- **RN-4:** El promedio se calcula únicamente sobre los pacientes que siguen esperando; no incluye a los ya atendidos.
- **RN-5:** Las alertas activas son las no atendidas, de cualquier módulo, ordenadas por antigüedad.
- **RN-6:** El tablero no filtra ni permite segmentar en esta versión: es una foto del día.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Parcial | Consume datos de admisión (HU-06) y de la atención. Dependencia declarada. |
| **N**egociable | Sí | La disposición de las tarjetas y el intervalo de refresco son negociables; los cálculos no. |
| **V**aliosa | Sí | Permite reasignar personal con información, que es la decisión real del administrador. |
| **E**stimable | Sí | Cuatro indicadores con fórmulas explícitas y sin gráficas. |
| **S**mall (pequeña) | Sí | 5 puntos. Se excluyeron áreas y tendencias para mantenerla ahí. |
| **T**esteable | Sí | Los escenarios tienen cifras y resultados calculados. |

## Dependencias y notas

- **Depende de:** HU-06 (registro con estado) y del ciclo de atención que produce los estados `En atención` / `Atendido`.
- **Notas para el equipo:**
  - **Ocupación por área está fuera del alcance**: no existe entidad de áreas ni de camas (supuesto S-4).
  - **"Dados de alta" sale del tablero**: el alta no tiene historia que la produzca.
  - Las gráficas de tendencia diaria/semanal se retiraron: con un MVP de días no aportan y encarecen.
  - El wireframe SVG existente es `docs/wireframes/dashboard-admin.svg` (el original apuntaba a `dashboard-principal.svg`, inexistente).

## Definición de terminado

- [ ] Los 5 escenarios pasan como pruebas automatizadas
- [ ] Probada la coherencia: la suma de estados cuadra con las admisiones del día
- [ ] Interfaz validada contra el wireframe por el PO
