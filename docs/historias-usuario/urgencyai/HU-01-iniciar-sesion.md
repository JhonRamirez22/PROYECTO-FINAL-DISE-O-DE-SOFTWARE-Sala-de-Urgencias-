---
id: HU-01
titulo: 'HU-01 "Iniciar Sesión"'
tipo: historia
epica: EP-01
etiquetas: [HU, Sprint-1, Autenticación]
milestone: ""
---

## Historia de Usuario

**Como** usuario del sistema
**Quiero** iniciar sesión con mis credenciales
**Para** acceder a las funcionalidades según mi rol

**Criterios de Aceptación:**
- Login con email y contraseña
- Token JWT expira en 8 horas
- Bloqueo tras 3 intentos fallidos
- Redirección según rol (Admin→Dashboard, Médico→Pacientes, etc.)

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Módulo base, sin dependencias de otras HUs |
| **Negotiable** | Sí | Detalles de seguridad (expiración, intentos) pueden ajustarse |
| **Valuable** | Sí | Acceso seguro al sistema, valor fundamental |
| **Estimable** | Sí | JWT + login son patrones estándar bien conocidos |
| **Small** | Sí | Alcance acotado: formulario + token + redirección |
| **Testable** | Sí | ACs claros: credenciales válidas/inválidas, bloq, redirección |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

## Wireframe Asociado

![Wireframe HU-01](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-01-iniciar-sesion.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-01-iniciar-sesion.svg)

**Leyenda del mockup:**

1. Correo electrónico; identificador de inicio de sesión.
2. Contraseña; se valida contra el hash almacenado.
3. "Iniciar sesión"; redirige según el rol del usuario.
4. Mensaje tras el tercer intento fallido; la cuenta se bloquea 15 minutos.
