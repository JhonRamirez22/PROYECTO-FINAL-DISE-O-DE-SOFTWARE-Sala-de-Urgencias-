---
id: HU-03
titulo: 'HU-03 "Crear Usuario"'
tipo: historia
etiquetas: [HU, Sprint-1, Gestión-Usuarios, historia-usuario, prioridad:alta, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** administrador del servicio
**Quiero** dar de alta a un miembro del personal asignándole un rol
**Para** que acceda únicamente a las funciones que su cargo permite y quede responsabilidad nominal sobre lo que hace

**Criterios de Aceptación:**
- Formulario con nombre completo, correo electrónico, rol y contraseña temporal
- El correo es único sin distinguir mayúsculas; si ya existe, el alta se rechaza
- El rol es obligatorio y debe ser Administrador, Cajero, Médico, Enfermera o Farmacéutico
- Contraseña temporal de 12 caracteres, visible una sola vez y con cambio obligatorio en el primer ingreso
- Política de contraseña: mínimo 8 caracteres con mayúscula, minúscula y dígito
- Los usuarios no se eliminan: se desactivan
- Debe existir siempre al menos un usuario Administrador activo
- El alta queda registrada en auditoría con autor, fecha y rol asignado

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Solo necesita que exista el rol Administrador; no depende de otras historias |
| **Negotiable** | Sí | El mecanismo de entrega de la contraseña temporal puede ajustarse |
| **Valuable** | Sí | Sin alta de usuarios nadie más puede operar el sistema |
| **Estimable** | Sí | Seis validaciones, generación de contraseña y registro de auditoría |
| **Small** | Sí | 3 puntos: un formulario, sus validaciones y un registro |
| **Testable** | Sí | Correo duplicado, rol faltante y contraseña débil son verificables |

**Score INVEST:** 6/6
**Riesgo principal:** La contraseña temporal circula por canales informales.
**Sugerencia:** Mostrarla una sola vez y forzar el cambio en el primer ingreso.

---

## Wireframe Asociado

![Wireframe HU-03](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-03-crear-usuario.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-03-crear-usuario.svg)

**Leyenda del mockup:**

1. Nombre completo; se usa para identificar al usuario en la auditoría.
2. Correo electrónico; identificador de inicio de sesión, debe ser único.
3. Rol; determina los permisos y es obligatorio.
4. Contraseña temporal generada por el sistema o definida manualmente.
5. La contraseña temporal se muestra una sola vez y no es recuperable.
6. "Crear usuario" valida el formulario completo antes de persistir.
