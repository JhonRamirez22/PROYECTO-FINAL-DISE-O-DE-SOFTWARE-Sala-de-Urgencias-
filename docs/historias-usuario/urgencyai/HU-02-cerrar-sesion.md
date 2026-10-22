---
id: HU-02
titulo: 'HU-02 "Cerrar Sesión"'
tipo: historia
etiquetas: [HU, Sprint-1, Autenticación, historia-usuario, prioridad:alta, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** miembro del personal que comparte estaciones de trabajo en urgencias
**Quiero** que mi sesión termine al abandonarla o tras un periodo de inactividad
**Para** que nadie pueda usar mi acceso para consultar o modificar datos clínicos

**Criterios de Aceptación:**
- Cierre manual desde el menú de usuario, con revocación del token en el servidor
- Aviso a los 28 minutos de inactividad, con las opciones "Continuar" y "Cerrar sesión"
- Cierre automático a los 30 minutos si no se responde el aviso
- Expiración absoluta a las 8 horas desde el inicio de sesión, aunque haya actividad
- Tras el cierre, el botón "atrás" del navegador no repone contenido autenticado
- Todo cierre se registra en auditoría con usuario, hora y motivo (manual, inactividad, expiración)

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Solo requiere que exista el inicio de sesión (HU-01); aporta valor por sí sola |
| **Negotiable** | Sí | El canal del aviso queda abierto; la regla de 30 y 28 minutos no |
| **Valuable** | Sí | Protege datos clínicos en estaciones compartidas entre turnos |
| **Estimable** | Sí | Dos caminos de salida, temporizadores explícitos y eventos de auditoría definidos |
| **Small** | Sí | 3 puntos: un temporizador, una revocación de token y un modal |
| **Testable** | Sí | Cada escenario tiene tiempo, estado y mensaje verificables |

**Score INVEST:** 6/6
**Riesgo principal:** Un temporizador solo en el cliente es eludible.
**Sugerencia:** Implementar el cierre también en el servidor y probar la revocación contra la API.

---

## Wireframe Asociado

![Wireframe HU-02](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-02-cerrar-sesion.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-02-cerrar-sesion.svg)

**Leyenda del mockup:**

1. El menú de usuario es el único punto de salida manual de la sesión.
2. La acción "Cerrar sesión" revoca el token y devuelve al inicio de sesión.
3. Aviso a los 28 minutos de inactividad; la pantalla de fondo queda bloqueada.
4. Responder reinicia el contador; no responder cierra la sesión a los 30 minutos.
