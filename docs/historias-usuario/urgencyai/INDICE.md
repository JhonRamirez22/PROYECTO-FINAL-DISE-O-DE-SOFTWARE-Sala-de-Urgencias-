# Backlog reescrito — UrgencyAI

**Sistema:** UrgencyAI · gestión de sala de urgencias
**Repositorio destino:** `JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-`
**Alcance de esta entrega:** reescritura de las 11 historias marcadas como rojas en la auditoría del backlog y unificación de las **29 historias** en un mismo formato, cada una con su mockup anotado.
**Resultado:** 11 historias originales → **13 reescritas** (2 divisiones por INVEST) + **16 historias que ya existían** sin reescribir + 4 épicas = **29 historias**.
**Puntos totales de las 13 reescritas:** 60.

---

## 1. Roles del sistema

| Rol | Quién es | Qué obtiene del sistema |
|---|---|---|
| **Administrador** | Jefatura del servicio | Control del personal, tablero operativo, reportes y auditoría |
| **Cajero** | Admisión | Registrar y ubicar al paciente que llega |
| **Enfermera** | Triaje y toma de signos | Clasificar y documentar el estado clínico |
| **Médico** | Atención médica | Apoyo diagnóstico y decisión clínica |
| **Farmacéutico** | Farmacia | Dispensación segura y control de inventario |
| **Paciente / familiar** | Acompañante | Seguimiento del estado de atención **sin autenticación** |

> El rol "usuario del sistema" desaparece del backlog: toda historia tiene un rol concreto.

---

## 2. Supuestos de diseño

Estas decisiones no estaban resueltas en el repositorio. Se toman como ingeniero de software y se registran aquí para que puedan revertirse con conocimiento de causa.

| ID | Decisión | Motivo | Impacto documental |
|---|---|---|---|
| **S-1** | La sesión expira a las **8 horas absolutas** y se cierra a los **30 minutos de inactividad**. | RNF-02 dice 24 h y HU-01 decía 8 h; además RF-02 exige 30 min de inactividad. En una sala de urgencias con estaciones compartidas, 24 h es un riesgo. La inactividad es el control real; las 8 h son el techo. | **Actualizar RNF-02** de 24 h a 8 h. |
| **S-2** | Las interacciones medicamentosas se verifican contra un **catálogo local versionado** (par de principios activos + severidad). | Depender de una API externa en el MVP agrega costo, licencia y una incógnita que impide estimar. El catálogo local se carga desde un archivo semilla y es sustituible después. | Nueva tabla `interacciones`; el RF-13 debe decir "catálogo del sistema". |
| **S-3** | HU-24 es una consulta **pública sin autenticación**, con código de 8 caracteres, lista blanca de campos visibles y límite de intentos. | El paciente no es un rol autenticado. Sin lista blanca ni límite, la historia es un agujero de privacidad. | Nuevo RNF de privacidad para la vista pública. |
| **S-4** | **No se modelan áreas/salas** en el MVP: la ocupación por área sale del tablero. | No existe la entidad y arrastra una historia completa que nadie ha pedido. El tablero conserva lo que sí se puede calcular. | Ajustar RF si menciona áreas. |
| **S-5** | Los reportes **no filtran por médico ni por departamento**; filtran por rango de fechas y nivel de triaje. | No existe asignación paciente→médico ni catálogo de departamentos. Se evita un reporte que no se puede calcular. | Ajustar RF-23. |
| **S-6** | Los rangos clínicos de HU-09 son los de **adulto**; pediatría queda fuera del MVP. | Los rangos pediátricos dependen de edad y peso y duplican el alcance. | Restricción explícita en el RF-09. |
| **S-7** | HU-14 verifica interacciones **en la dispensación** (HU-13), no en la prescripción. | No existe historia de prescripción; anclar la verificación a la dispensación la hace implementable hoy. | Renombrar RF-13 a "verificar al dispensar". |
| **S-8** | La exportación es **CSV y PDF**. Se descarta Excel. | RF-24 dice CSV o PDF; HU-26 decía Excel. Se alinea con el requisito. | HU-26b. |

### Sobre los identificadores

Se conserva el número original para mantener la trazabilidad con `docs/requisitos.md`. Cuando una historia se divide por INVEST, las partes se nombran con letra: **HU-12a / HU-12b** y **HU-26a / HU-26b**. No se renumeran las demás.

---

## 3. Épicas

| Épica | Nombre | Historias | Puntos | Issue |
|---|---|---|---:|---|
| **EP-01** | Seguridad y control de acceso | HU-02, HU-03 | 6 | #30 |
| **EP-02** | Admisión y registro clínico | HU-06, HU-09 | 10 | #31 |
| **EP-03** | Farmacia y apoyo a la decisión clínica | HU-12a, HU-12b, HU-14, HU-15 | 21 | #32 |
| **EP-04** | Operación, seguimiento y cumplimiento | HU-24, HU-25, HU-26a, HU-26b, HU-27 | 23 | #33 |

---

## 4. Historias reescritas

| ID | Título | Épica | Prioridad | SP | Sprint | Depende de | Issue |
|---|---|---|---|---:|---|---|---|
| **HU-02** | Cerrar sesión de forma segura | EP-01 | Must | 3 | 1 | HU-01 | #2 |
| **HU-03** | Crear usuario del sistema | EP-01 | Must | 3 | 1 | HU-01 | #3 |
| **HU-06** | Registrar paciente en admisión | EP-02 | Must | 5 | 1 | HU-01 | #6 |
| **HU-09** | Registrar signos vitales | EP-02 | Must | 5 | 2 | HU-06 | #9 |
| **HU-12a** | Gestionar catálogo de medicamentos | EP-03 | Must | 3 | 2 | — | #34 |
| **HU-12b** | Controlar lotes, vencimientos y stock | EP-03 | Should | 5 | 2 | HU-12a | #35 |
| **HU-14** | Verificar interacciones medicamentosas | EP-03 | Should | 5 | 2 | HU-12a, HU-13 | #14 |
| **HU-15** | Obtener diagnóstico asistido por IA | EP-03 | Should | 8 | 2 | HU-06, HU-09 | #15 |
| **HU-24** | Consultar estado de atención | EP-04 | Should | 5 | 3 | HU-06, HU-17 | #24 |
| **HU-25** | Ver tablero operativo del servicio | EP-04 | Should | 5 | 3 | HU-06, HU-09 | #25 |
| **HU-26a** | Consultar reporte de atenciones | EP-04 | Should | 5 | 3 | HU-06, HU-09 | #36 |
| **HU-26b** | Exportar reporte de atenciones | EP-04 | Should | 3 | 3 | HU-26a | #37 |
| **HU-27** | Consultar auditoría de accesos | EP-04 | Should | 5 | 3 | HU-01 | #27 |

**Total: 60 puntos.**

Las **16 historias restantes** — HU-01, HU-04, HU-05, HU-07, HU-08, HU-10, HU-11, HU-13, HU-16, HU-17, HU-18, HU-19, HU-20, HU-21, HU-22 y HU-23 — conservan su redacción original. Se les unificó el formato y se les reemplazó el mockup por uno del mismo estilo anotado; no se reescribió su contenido.

---

## 5. Orden de release

**MVP (Must) — 19 puntos, 5 historias:**
HU-02 → HU-03 → HU-06 → HU-09 → HU-12a

Con estas cinco el servicio funciona de punta a punta: el personal entra, admisión registra al paciente, enfermería documenta su estado y farmacia tiene catálogo. Es demoable.

**Segunda ola (Should) — 41 puntos, 8 historias:**
HU-12b → HU-14 → HU-26a → HU-26b → HU-25 → HU-24 → HU-27 → HU-15

La IA va al final a propósito: es la historia de mayor riesgo técnico y menor valor incremental — el sistema sirve sin ella.

---

## 6. Mockups

Cada una de las 29 historias incluye un mockup de baja fidelidad en SVG, monocromático y anotado con números. Los archivos viven en `docs/historias-usuario/urgencyai/wireframes/` y la leyenda numerada de cada uno está al pie de su historia en `docs/historias-usuario/urgencyai/` y en la issue correspondiente:

| Historia | Archivo |
|---|---|
| HU-01 | `wireframes/HU-01-iniciar-sesion.svg` |
| HU-02 | `wireframes/HU-02-cerrar-sesion.svg` |
| HU-03 | `wireframes/HU-03-crear-usuario.svg` |
| HU-04 | `wireframes/HU-04-editar-usuario.svg` |
| HU-05 | `wireframes/HU-05-listar-usuarios.svg` |
| HU-06 | `wireframes/HU-06-registrar-paciente.svg` |
| HU-07 | `wireframes/HU-07-buscar-paciente.svg` |
| HU-08 | `wireframes/HU-08-editar-paciente.svg` |
| HU-09 | `wireframes/HU-09-registrar-signos-vitales.svg` |
| HU-10 | `wireframes/HU-10-visualizar-signos.svg` |
| HU-11 | `wireframes/HU-11-editar-signos.svg` |
| HU-12a | `wireframes/HU-12a-catalogo-medicamentos.svg` |
| HU-12b | `wireframes/HU-12b-lotes-vencimientos.svg` |
| HU-13 | `wireframes/HU-13-registrar-dosis.svg` |
| HU-14 | `wireframes/HU-14-verificar-interacciones.svg` |
| HU-15 | `wireframes/HU-15-diagnostico-ia.svg` |
| HU-16 | `wireframes/HU-16-revisar-sugerencia-ia.svg` |
| HU-17 | `wireframes/HU-17-clasificar-triaje.svg` |
| HU-18 | `wireframes/HU-18-recibir-notificacion.svg` |
| HU-19 | `wireframes/HU-19-configurar-notificaciones.svg` |
| HU-20 | `wireframes/HU-20-validar-diagnostico-ia.svg` |
| HU-21 | `wireframes/HU-21-gestionar-insumos.svg` |
| HU-22 | `wireframes/HU-22-activar-alerta.svg` |
| HU-23 | `wireframes/HU-23-responder-alerta.svg` |
| HU-24 | `wireframes/HU-24-consultar-estado-atencion.svg` |
| HU-25 | `wireframes/HU-25-tablero-operativo.svg` |
| HU-26a | `wireframes/HU-26a-reporte-atenciones.svg` |
| HU-26b | `wireframes/HU-26b-exportar-reporte.svg` |
| HU-27 | `wireframes/HU-27-auditoria-accesos.svg` |

Los mockups son de baja fidelidad a propósito: muestran jerarquía, campos, estados y acciones, no la identidad visual del producto.

**Antes de publicar las issues:** las historias enlazan el mockup con una URL absoluta a `raw.githubusercontent.com`. Los archivos deben estar commiteados y empujados a `main` en la ruta `docs/historias-usuario/urgencyai/wireframes/`; de lo contrario la imagen aparece rota en la issue. Las rutas relativas no sirven en las issues de GitHub.

---

## 7. Qué cambió respecto del backlog original

| Problema detectado en la auditoría | Cómo se resolvió |
|---|---|
| HU-02 cubría logout manual e ignoraba RF-02 | Una sola historia con dos caminos (manual e inactividad) y 5 escenarios |
| HU-03 "complejidad" indefinida | Política de contraseña concreta + contraseña temporal con cambio obligatorio |
| HU-06 sin seguro médico, sin caso de cédula duplicada | RF-06 completo + reutilización de ficha + paciente sin documento |
| HU-09 sin rangos clínicos, "pulso" en vez de FC | Tabla de rangos aceptables y críticos; se corrige el campo |
| HU-09 dependía de "turno" (inexistente) | Se asocia a la **atención abierta**, que sí existe |
| HU-12 era un módulo de 4 funcionalidades | Se divide en catálogo (12a) y lotes/stock (12b), con FEFO |
| HU-14 decía "cuando sea posible" | Catálogo local con 4 severidades y comportamiento por severidad |
| HU-15 enviaba alergias e historial inexistentes; 10 s vs RNF-08 | Solo síntomas + signos vitales; 5 s; anonimización de PII |
| HU-24 con actor fuera del modelo y sin límites | Consulta pública con código, lista blanca y rate limit |
| HU-25 con áreas y altas inexistentes | Métricas calculables; ocupación por área fuera del MVP |
| HU-26 con Excel, "por médico" y "departamento" | Se divide en consulta (26a) y exportación CSV/PDF (26b) |
| HU-27 con retención y horarios sin modelo | Jornada institucional configurable; retención pasa a RNF |

---

## 8. Pendientes que este documento no cubre

- **HU-28** sigue sin issue: debe convertirse en RNF o publicarse.
- **Prescripción médica y alta del paciente** siguen sin historia. Son las dos ausencias más graves del backlog y bloquean parcialmente a HU-14 y HU-24.
- **Los 20 RNF no tienen issues**: se recomienda una épica técnica aparte o excluirlos formalmente del alcance.
- **Milestones**: el repositorio no tiene ninguno creado. Antes de publicar, crear `Sprint 1`, `Sprint 2` y `Sprint 3`, o dejar el campo vacío.
- **README y `docs/`** deben actualizarse con esta nueva redacción para que la fuente de verdad no se vuelva a partir.
