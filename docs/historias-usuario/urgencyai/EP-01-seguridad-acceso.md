---
id: EP-01
titulo: "EP-01 · Seguridad y control de acceso"
tipo: epica
etiquetas: [epica, prioridad:alta, Autenticación]
milestone: ""
---

# EP-01 · Seguridad y control de acceso

**Objetivo:** que solo el personal autorizado entre al sistema y que cada persona acceda únicamente a lo que su rol permite, en un entorno de estaciones de trabajo compartidas.

**Valor de negocio:** UrgencyAI maneja datos clínicos de pacientes. Sin control de acceso verificable no hay habilitación para uso real ni cumplimiento de privacidad, y en una sala de urgencias el equipo se comparte físicamente entre turnos.

**Métrica de éxito:** cero accesos con credenciales de otro usuario reportados en el piloto; 100 % de las sesiones finalizadas dentro de los 30 minutos posteriores al abandono de la estación.

## Historias

- [ ] HU-01 · Iniciar sesión — 3 pts — Must (#1)
- [ ] HU-02 · Cerrar sesión — 3 pts — Must (#2)
- [ ] HU-03 · Crear usuario — 3 pts — Must (#3)
- [ ] HU-04 · Editar usuario — 3 pts — Should (#4)
- [ ] HU-05 · Listar/buscar usuarios — 3 pts — Should (#5)

## Fuera de alcance de esta épica

- Recuperación de contraseña por correo (no está en los requisitos; requiere proveedor de correo).
- Autenticación de dos factores.
- Inicio de sesión único institucional (LDAP/SSO).

## Notas

El rol "usuario del sistema" del backlog original se conserva únicamente en HU-01, porque es el texto de la historia de inicio de sesión; el resto de las historias de esta épica nombran roles concretos o, cuando el valor es transversal, "miembro del personal", que es una categoría real y acotada.
