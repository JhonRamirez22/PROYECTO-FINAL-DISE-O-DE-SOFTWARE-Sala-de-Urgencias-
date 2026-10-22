---
id: HU-24
titulo: 'HU-24 "Consultar Estado de Paciente"'
tipo: historia
epica: EP-04
etiquetas: [HU, Sprint-3, Asistencia-Paciente, historia-usuario, prioridad:media, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** familiar de un paciente que está siendo atendido
**Quiero** consultar en qué etapa va su atención con un código que me entregaron en admisión
**Para** saber si ya entró, cuánto falta y si debo acercarme, sin interrumpir al personal en cada momento

**Criterios de Aceptación:**
- Consulta con un código de 8 caracteres en alfabeto Crockford Base32, sin 0, O, 1, I ni L
- Muestra estado, nivel de triaje, personas por delante, tiempo estimado y hora de actualización
- Nunca muestra nombre, cédula, diagnóstico ni ningún otro dato clínico o personal
- Código inexistente y código vencido producen el mismo mensaje y el mismo tiempo de respuesta
- Máximo 5 consultas por minuto por conexión; superado el límite, bloqueo de 15 minutos
- El código sigue válido hasta 7 días después del alta del paciente
- Tiempo estimado = personas por delante × tiempo promedio de atención de las últimas 24 horas
- La consulta no requiere autenticación

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Requiere que exista la atención, no otras historias nuevas |
| **Negotiable** | Sí | La longitud del código y el formato del mensaje son ajustables |
| **Valuable** | Sí | Descongestiona el mostrador sin exponer datos clínicos |
| **Estimable** | Sí | Código no enumerable, control de intentos y tiempo estimado |
| **Small** | Sí | 5 puntos: vista pública, código, límite de intentos y cálculo |
| **Testable** | Sí | Código inválido, exceso de intentos y alta son verificables |

**Score INVEST:** 6/6
**Riesgo principal:** El código de seguimiento puede filtrarse a terceros.
**Sugerencia:** Lista blanca de campos visibles y ningún dato personal en la vista.

---

## Wireframe Asociado

![Wireframe HU-24](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-24-consultar-estado-atencion.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-24-consultar-estado-atencion.svg)

**Leyenda del mockup:**

1. Código de seguimiento de 8 caracteres entregado en admisión.
2. Estado actual de la atención.
3. Nivel de triaje asignado.
4. Tiempo estimado de espera.
5. Hora de la última actualización del estado.
6. Aviso de privacidad: no se muestran datos clínicos ni personales.
