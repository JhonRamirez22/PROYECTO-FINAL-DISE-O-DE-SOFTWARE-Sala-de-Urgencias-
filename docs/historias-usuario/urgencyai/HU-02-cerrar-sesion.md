---
id: HU-02
titulo: "HU-02 · Cerrar sesión de forma segura"
tipo: historia
epica: EP-01
etiquetas: [HU, Sprint-1, Autenticación, historia-usuario, prioridad:alta, sp:3]
milestone: ""
---
## Historia de usuario

> **Como** miembro del personal que comparte estaciones de trabajo en urgencias
> **quiero** que mi sesión termine al abandonarla o tras un periodo de inactividad
> **para** que nadie pueda usar mi acceso para consultar o modificar datos clínicos.

**Épica:** EP-01 · Seguridad y control de acceso
**Prioridad (MoSCoW):** Must. Las estaciones de urgencias se comparten entre turnos; sin cierre de sesión, el control de acceso de HU-01 es decorativo.
**Estimación:** 3 puntos. Dos caminos de salida, temporizadores en cliente y servidor, revocación de token y registro de auditoría.
**Origen:** "RF-02 | Cierre de Sesión por Inactividad | El sistema debe cerrar la sesión automáticamente tras 30 minutos de inactividad, mostrando un aviso 2 minutos antes." y RNF-02 (autenticación por tokens).

## Criterios de aceptación

```gherkin
Característica: Cierre de sesión

  Antecedentes:
    Dado que la enfermera "Ana Ruiz" inició sesión a las 07:00 en la estación 3

  Escenario: Cierre manual desde el menú de usuario
    Cuando Ana selecciona "Cerrar sesión" en el menú de usuario
    Entonces el sistema termina la sesión
    Y la redirige a la pantalla de inicio de sesión
    Y registra en la auditoría el evento "logout" con motivo "manual"

  Escenario: Aviso previo al cierre por inactividad
    Dado que Ana no ha interactuado con el sistema durante 28 minutos
    Cuando se alcanza el minuto 28 de inactividad
    Entonces el sistema muestra el aviso "Tu sesión se cerrará en 2 minutos"
    Y ofrece las opciones "Continuar" y "Cerrar sesión"

  Escenario: Cierre automático por inactividad
    Dado que el aviso de inactividad está visible
    Cuando transcurren 2 minutos sin que Ana seleccione "Continuar"
    Entonces el sistema cierra la sesión automáticamente
    Y registra el evento con motivo "inactividad"

  Escenario: Continuidad de la sesión
    Dado que el aviso de inactividad está visible
    Cuando Ana selecciona "Continuar"
    Entonces el aviso desaparece
    Y el contador de inactividad se reinicia en 30 minutos

  Escenario: Sesión cerrada no reutilizable
    Dado que la sesión de Ana fue cerrada
    Cuando se intenta reutilizar el acceso anterior desde el historial del navegador
    Entonces el sistema rechaza la petición
    Y redirige al inicio de sesión
    Y no muestra ningún dato clínico en pantalla

  Escenario: Expiración absoluta
    Dado que Ana inició sesión a las 07:00 y ha estado activa de forma continua
    Cuando se cumplen 8 horas desde el inicio de sesión
    Entonces el sistema cierra la sesión
    Y registra el evento con motivo "expiracion"
```

**No funcionales**
- [ ] El cierre por inactividad se dispara con una desviación máxima de 10 segundos respecto de los 30 minutos.
- [ ] El cierre manual completa la redirección en menos de 1 segundo en una conexión de 3G.
- [ ] El token revocado deja de ser aceptado por la API en menos de 5 segundos.

## Wireframe

![Mockup HU-02](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-02-cerrar-sesion.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. El menú de usuario es el único punto de salida manual de la sesión.
2. La acción “Cerrar sesión” revoca el token y devuelve al inicio de sesión.
3. Aviso a los 28 minutos de inactividad; la pantalla de fondo queda bloqueada.
4. Responder reinicia el contador; no responder cierra la sesión a los 30 minutos.

## Reglas de negocio

- **RN-1:** Se considera inactividad la ausencia de teclado, puntero y peticiones autenticadas durante **30 minutos**.
- **RN-2:** El aviso aparece a los **28 minutos** de inactividad y permanece visible 2 minutos.
- **RN-3:** Existe además una **expiración absoluta de 8 horas** desde el inicio de sesión, aunque haya actividad (supuesto S-1, alineado con RF-02 y no con RNF-02).
- **RN-4:** Al cerrar sesión se revoca el token de refresco en el servidor; el token de acceso deja de aceptarse.
- **RN-5:** El estado en el cliente se descarta: el botón "atrás" no repone contenido autenticado.
- **RN-6:** Todo cierre se registra en auditoría con usuario, hora y motivo (`manual`, `inactividad`, `expiracion`).

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Sí | Solo requiere que exista inicio de sesión (HU-01). Aporta valor por sí sola: con HU-01 ya se puede entrar, con HU-02 ya se puede salir. |
| **N**egociable | Sí | El canal del aviso (modal, barra inferior) y el mecanismo de revocación quedan abiertos al equipo; la regla de 30/28 minutos no. |
| **V**aliosa | Sí | Protege datos clínicos en estaciones compartidas, que es el escenario real de urgencias. |
| **E**stimable | Sí | Dos caminos, temporizadores explícitos y una lista de eventos de auditoría. |
| **S**mall (pequeña) | Sí | 3 puntos: un temporizador, una revocación y un modal. |
| **T**esteable | Sí | Cada escenario tiene tiempo, estado y mensaje verificables. |

## Dependencias y notas

- **Depende de:** HU-01 (inicio de sesión, que debe existir).
- **Notas para el equipo:**
  - Este cambio obliga a **corregir RNF-02** en `docs/requisitos.md`: de 24 horas a 8 horas.
  - El cierre por inactividad debe implementarse también en el servidor: un temporizador solo en cliente es eludible.
  - El wireframe SVG existente es `docs/wireframes/cerrar-sesion.svg` (el backlog original apuntaba a `logout.svg`, que no existe).

## Definición de terminado

- [ ] Los 6 escenarios pasan como pruebas automatizadas
- [ ] La revocación de token está verificada contra la API, no solo simulado en el cliente
- [ ] `RNF-02` actualizado en `docs/requisitos.md`
- [ ] Interfaz validada contra el wireframe por el PO
