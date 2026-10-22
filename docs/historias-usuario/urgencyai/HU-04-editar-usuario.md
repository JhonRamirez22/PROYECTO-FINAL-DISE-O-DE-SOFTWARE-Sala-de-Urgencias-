---
id: HU-04
titulo: 'HU-04 "Editar Usuario"'
tipo: historia
epica: EP-01
etiquetas: [HU, Sprint-1, Gestión-Usuarios, historia-usuario, prioridad:media, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** administrador
**Quiero** modificar datos y roles de usuarios existentes
**Para** mantener la información actualizada

**Criterios de Aceptación:**
- Editar nombre, email, rol, estado (activo/inactivo)
- No permitir editar email si ya existe otro usuario
- Historial de cambios registrado
- Confirmación antes de guardar

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-03 (usuarios existentes) |
| **Negotiable** | Sí | Campos editables y reglas de negocio ajustables |
| **Valuable** | Sí | Mantener datos actualizados del personal |
| **Estimable** | Sí | CRUD edit con validaciones estándar |
| **Small** | Sí | Formulario edición + audit trail |
| **Testable** | Sí | Editar válido, email duplicado, confirmación |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-03
**Sugerencia:** Ejecutar después de HU-03

---

## Wireframe Asociado

![Wireframe HU-04](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-04-editar-usuario.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-04-editar-usuario.svg)

**Leyenda del mockup:**

1. Nombre completo; se refleja en la auditoría.
2. Correo electrónico; no puede coincidir con otro usuario.
3. Rol; determina los permisos del usuario.
4. Estado activo o inactivo; desactivar no borra el historial.
5. Historial de cambios con fecha, usuario y valor anterior.
6. Confirmación antes de guardar; el resto de la pantalla queda bloqueado.
