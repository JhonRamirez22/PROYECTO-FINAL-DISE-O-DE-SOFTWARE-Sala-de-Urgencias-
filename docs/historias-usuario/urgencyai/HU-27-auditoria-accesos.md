---
id: HU-27
titulo: 'HU-27 "Auditoría de Accesos"'
tipo: historia
etiquetas: [HU, Sprint-3, Seguridad, historia-usuario, prioridad:media, sp:5]
milestone: ""
---

## Historia de Usuario

**Como** administrador del servicio
**Quiero** revisar quién accedió a los datos de un paciente, cuándo y desde dónde
**Para** detectar usos indebidos y poder responder con evidencia si alguien reclama por un acceso indebido

**Criterios de Aceptación:**
- Filtros por usuario, acción y rango de fechas
- Cada evento registra usuario, fecha y hora con zona horaria, acción, módulo, recurso afectado e IP
- Accesos fuera de la jornada institucional resaltados; por defecto 06:00 a 22:00, configurable
- Los accesos denegados también se registran
- El registro es append-only: la aplicación no puede modificarlo ni eliminarlo
- Exportación en CSV UTF-8 disponible solo para el rol Administrador
- Retención mínima de un año

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Depende de que existan eventos que auditar |
| **Negotiable** | Sí | La jornada institucional es un parámetro configurable |
| **Valuable** | Sí | Es la garantía de trazabilidad sobre datos clínicos |
| **Estimable** | Sí | Registro append-only, filtros, alerta y exportación |
| **Small** | Sí | 5 puntos: escritura, consulta con filtros y exportación |
| **Testable** | Sí | Inmutabilidad, filtros y exportación son verificables |

**Score INVEST:** 6/6
**Riesgo principal:** El volumen de eventos degrada la consulta con filtros amplios.
**Sugerencia:** Índices por fecha y usuario, y paginación obligatoria en la vista.

---

## Wireframe Asociado

![Wireframe HU-27](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-27-auditoria-accesos.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-27-auditoria-accesos.svg)

**Leyenda del mockup:**

1. Filtros por usuario, acción y rango de fechas.
2. Exportación del resultado filtrado.
3. Registro de eventos con fecha, usuario, acción, módulo e IP.
4. Eventos fuera de la jornada institucional resaltados.
5. Resumen de anomalías del período consultado.
6. El registro es inmutable: no se edita ni se borra.
