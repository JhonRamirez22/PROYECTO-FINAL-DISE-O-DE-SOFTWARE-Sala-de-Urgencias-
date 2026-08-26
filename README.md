# UrgencyAI - Sistema de Gestión de Sala de Urgencias con IA

Plataforma inteligente para la gestión integral de salas de urgencias que integra inteligencia artificial para apoyar el diagnóstico médico, optimizar el triaje y mejorar la eficiencia operativa.

---

## Roles del Sistema

| Rol | Descripción |
|-----|-------------|
| **Administrador** | Gestiona usuarios, configuración y reportes del sistema |
| **Cajero** | Registra pacientes y gestiona admisiones |
| **Médico** | Diagnostica, prescribe y valida tratamientos |
| **Enfermera** | Registra y monitorea signos vitales |
| **Farmacéutico** | Gestiona inventario y dispensa medicamentos |

---

## Stack Tecnológico

- **Frontend:** React / Next.js
- **Backend:** Node.js / Express
- **Base de Datos:** PostgreSQL
- **IA:** Python (FastAPI) + OpenAI API
- **Autenticación:** JWT + bcrypt
- **Monitoreo:** WebSocket para alertas en tiempo real

---

## Documentación del Proyecto

| Documento | Descripción |
|-----------|-------------|
| [Diseño Thinking](docs/dise%C3%B1o-thinking.md) | Proceso de diseño: Empatizar, Definir, Idear — personas, pain points, pregunta de diseño |
| [Requisitos](docs/requisitos.md) | Requisitos funcionales (27 RF) y no funcionales (20 RNF) con trazabilidad a HUs |
| [Historias de Usuario](docs/historias-de-usuario.md) | 28 HU completas con aceptación, organizadas por sprint |
| [Wireframes](docs/wireframes/) | 28 wireframes SVG de las pantallas principales |

---

## Estructura del Repositorio

```
├── docs/
│   ├── diseño-thinking.md      # Proceso de diseño thinking
│   ├── requisitos.md            # Requisitos funcionales y no funcionales
│   ├── historias-de-usuario.md  # 28 historias de usuario
│   └── wireframes/              # 28 wireframes SVG
├── backend/                     # API REST (Node.js + Express)
├── frontend/                    # Interfaz web (React / Next.js)
├── ai-service/                  # Microservicio de IA (Python + FastAPI)
└── database/                    # Scripts SQL y migraciones
```

---

## Historias de Usuario

28 HU organizadas en 3 sprints:

| Sprint | HU | Módulo |
|--------|-----|--------|
| Sprint 1 | HU-01 a HU-11 | Autenticación, Gestión de Pacientes, Signos Vitales |
| Sprint 2 | HU-12 a HU-20 | Farmacia, Diagnóstico IA, Notificaciones |
| Sprint 3 | HU-21 a HU-28 | Reportes, Auditoría, Monitoreo |

Ver [docs/historias-de-usuario.md](docs/historias-de-usuario.md) para el detalle completo.

---

## Wireframes

28 wireframes SVG de las pantallas principales del sistema.

Ver carpeta [docs/wireframes/](docs/wireframes/).

---

## Equipo

- **Jhon Ramirez** - Desarrollador Full Stack
