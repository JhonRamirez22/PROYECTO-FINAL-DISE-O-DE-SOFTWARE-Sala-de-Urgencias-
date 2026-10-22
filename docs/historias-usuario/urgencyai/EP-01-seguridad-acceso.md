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

- [ ] HU-02 · Cerrar sesión de forma segura — 3 pts — Must
- [ ] HU-03 · Crear usuario del sistema — 3 pts — Must

## Fuera de alcance de esta épica

- Recuperación de contraseña por correo (no está en los requisitos; requiere proveedor de correo).
- Autenticación de dos factores.
- Inicio de sesión único institucional (LDAP/SSO).

## Notas

El rol "usuario del sistema" utilizado en el backlog original desaparece: las dos historias nombran roles concretos o, cuando el valor es transversal, "miembro del personal", que es una categoría real y acotada.
