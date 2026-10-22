---
id: HU-05
titulo: 'HU-05 "Listar/Buscar Usuarios"'
tipo: historia
epica: EP-01
etiquetas: [HU, Sprint-1, Gestión-Usuarios, historia-usuario, prioridad:media, sp:3]
milestone: ""
---

## Historia de Usuario

**Como** administrador
**Quiero** ver y filtrar la lista de usuarios
**Para** gestionar el personal del sistema

**Criterios de Aceptación:**
- Tabla paginada (10 por página)
- Filtros: nombre, rol, estado
- Búsqueda por nombre o email
- Acciones: editar, desactivar

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Parcial | Requiere HU-03 (datos de usuarios) |
| **Negotiable** | Sí | Filtros y paginación pueden ajustarse |
| **Valuable** | Sí | Visualización y gestión del personal |
| **Estimable** | Sí | Tabla + filtros + paginación, patrón común |
| **Small** | Sí | Componente de tabla con filtros |
| **Testable** | Sí | Paginar, filtrar, buscar, acciones |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-03
**Sugerencia:** Ejecutar después de HU-03

---

## Wireframe Asociado

![Wireframe HU-05](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-05-listar-usuarios.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-05-listar-usuarios.svg)

**Leyenda del mockup:**

1. Búsqueda por nombre o correo y filtros por rol y estado.
2. Tabla paginada de 10 usuarios por página.
3. Acciones por fila: editar y desactivar o activar.
4. Paginación; conserva los filtros aplicados.
