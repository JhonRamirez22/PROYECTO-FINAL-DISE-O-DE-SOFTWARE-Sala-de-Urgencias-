# Requisitos — UrgencyAI

## 1. Requisitos Funcionales

Organizados por módulo del sistema. Cada requisito referencia la Historia de Usuario (HU) correspondiente.

### 1.1 Módulo de Autenticación y Gestión de Usuarios

| ID | Requisito | HU |
|----|-----------|-----|
| RF-01 | El sistema debe permitir inicio de sesión con email y contraseña | HU-01 |
| RF-02 | El sistema debe cerrar sesión automáticamente tras inactividad de 30 minutos | HU-02 |
| RF-03 | El administrador debe poder crear usuarios con nombre, email, contraseña y rol | HU-03 |
| RF-04 | El administrador debe poder editar datos y rol de usuarios existentes | HU-04 |
| RF-05 | El administrador debe poder listar, buscar y filtrar usuarios por rol o estado | HU-05 |

### 1.2 Módulo de Gestión de Pacientes

| ID | Requisito | HU |
|----|-----------|-----|
| RF-06 | El cajero debe poder registrar un paciente con datos personales, contacto y seguro | HU-06 |
| RF-07 | El cajero debe poder buscar pacientes por nombre, cédula o número de expediente | HU-07 |
| RF-08 | El cajero debe poder editar información de pacientes existentes | HU-08 |

### 1.3 Módulo de Signos Vitales

| ID | Requisito | HU |
|----|-----------|-----|
| RF-09 | La enfermera debe poder registrar signos vitales: temperatura, presión arterial, saturación de oxígeno, frecuencia cardíaca, frecuencia respiratoria | HU-09 |
| RF-10 | La enfermera debe poder visualizar el historial de signos vitales de un paciente | HU-10 |
| RF-11 | La enfermera debe poder editar signos vitales registrados en caso de error | HU-11 |

### 1.4 Módulo de Farmacia

| ID | Requisito | HU |
|----|-----------|-----|
| RF-12 | El farmacéutico debe poder registrar dosis dispensadas a un paciente con medicamento, cantidad y observaciones | HU-12 |
| RF-13 | El sistema debe verificar automáticamente interacciones medicamentosas al dispensar | HU-13 |
| RF-14 | El farmacéutico debe poder gestionar el inventario de medicamentos (stock mínimo, stock actual, vencimiento) | HU-17 |
| RF-15 | El sistema debe activar alertas automáticas cuando el stock de un medicamento baja del mínimo configurable | HU-18 |
| RF-16 | El farmacéutico debe poder responder a alertas de stock con acciones (pedido, transferencia, resolución) | HU-19 |

### 1.5 Módulo de Diagnóstico Asistido por IA

| ID | Requisito | HU |
|----|-----------|-----|
| RF-17 | El médico debe poder ingresar síntomas, signos vitales y antecedentes para obtener un diagnóstico sugerido por IA | HU-14 |
| RF-18 | La IA debe generar al menos 3 diagnósticos sugeridos con nivel de confianza | HU-14 |
| RF-19 | El médico debe poder revisar y validar o descartar las sugerencias de IA | HU-15 |
| RF-20 | El sistema debe registrar la validación del médico para mejorar el modelo de IA | HU-15 |

### 1.6 Módulo de Notificaciones

| ID | Requisito | HU |
|----|-----------|-----|
| RF-21 | El sistema debe enviar notificaciones en tiempo real (WebSocket) al navegador | HU-16 |
| RF-22 | El usuario debe poder configurar qué tipos de notificaciones recibe y por qué canal | HU-20 |

### 1.7 Módulo de Administración y Reportes

| ID | Requisito | HU |
|----|-----------|-----|
| RF-23 | El administrador debe poder generar reportes de atenciones, diagnósticos y productividad | HU-21 |
| RF-24 | El sistema debe poder exportar reportes en formato CSV o PDF | HU-21 |
| RF-25 | El administrador debe poder auditar accesos: quién, cuándo, qué acción, desde qué IP | HU-22 |

### 1.8 Módulo de Monitoreo del Sistema

| ID | Requisito | HU |
|----|-----------|-----|
| RF-26 | El administrador debe poder monitorear estado del sistema (CPU, RAM, conexiones activas) | HU-23 |
| RF-27 | El administrador debe poder ejecutar optimizaciones (limpiar caché, reiniciar servicios) | HU-23 |
| RF-28 | El sistema debe mostrar estado de pacientes en tiempo real (sala, cama, estado) | HU-24 |

---

## 2. Requisitos No Funcionales

### 2.1 Seguridad

| ID | Requisito |
|----|-----------|
| RNF-01 | Contraseñas almacenadas con hash bcrypt (mínimo 12 rondas) |
| RNF-02 | Autenticación mediante JWT con expiración de 24 horas |
| RNF-03 | Autorización basada en roles: cada endpoint verifica el rol del usuario |
| RNF-04 | HTTPS obligatorio en producción |
| RNF-05 | Registro de auditoría para acciones críticas (login, creación, eliminación) |
| RNF-06 | Protección contra inyección SQL y XSS |

### 2.2 Rendimiento

| ID | Requisito |
|----|-----------|
| RNF-07 | Tiempo de respuesta de la API menor a 200ms en operaciones CRUD |
| RNF-08 | Tiempo de respuesta del servicio de IA menor a 5 segundos para diagnósticos |
| RNF-09 | Soporte para al menos 50 usuarios concurrentes sin degradación |
| RNF-10 | Paginación obligatoria en listados que superen 20 registros |

### 2.3 Disponibilidad

| ID | Requisito |
|----|-----------|
| RNF-11 | Disponibilidad del sistema del 99% (máximo 8.76 horas de downtime al año) |
| RNF-12 | Backup automático de la base de datos cada 6 horas |
| RNF-13 | Logs de error centralizados para diagnóstico de fallos |

### 2.4 Usabilidad

| ID | Requisito |
|----|-----------|
| RNF-14 | Interfaz responsiva (desktop, tablet, móvil) |
| RNF-15 | Tiempo máximo de aprendizaje para un nuevo usuario: 30 minutos |
| RNF-16 | Navegación consistente con sidebar y breadcrumbs |
| RNF-17 | Mensajes de error comprensibles y en español |

### 2.5 Escalabilidad

| ID | Requisito |
|----|-----------|
| RNF-18 | Arquitectura de microservicios para desacoplar frontend, backend y servicio de IA |
| RNF-19 | Base de datos relacional (PostgreSQL) con diseño normalizado (3FN) |
| RNF-20 | API RESTful versionada (v1/) para permitir evolución sin romper clientes |

---

## 3. Restricciones y Supuestos

### 3.1 Restricciones

- El proyecto se desarrolla como Proyecto Final de Diseño de Software
- El equipo es un solo desarrollador (desarrollo individual)
- El plazo de entrega es el semestre académico vigente
- Se debe utilizar tecnología open source (sin licencias comerciales)
- El servicio de IA puede utilizar una API externa (OpenAI) con límites de uso

### 3.2 Supuestos

- Los usuarios tienen acceso a un navegador web actualizado (Chrome, Firefox, Edge)
- La sala de urgencias tiene conectividad a internet estable
- Los datos de prueba serán proporcionados por el desarrollador (no datos reales de pacientes)
- El sistema se desplegará en un entorno de producción accesible vía URL pública

---

## 4. Matriz de Trazabilidad

Relación entre Requisitos Funcionales y Historias de Usuario:

| HU | Requisito(s) |
|----|-------------|
| HU-01 | RF-01 |
| HU-02 | RF-02 |
| HU-03 | RF-03 |
| HU-04 | RF-04 |
| HU-05 | RF-05 |
| HU-06 | RF-06 |
| HU-07 | RF-07 |
| HU-08 | RF-08 |
| HU-09 | RF-09 |
| HU-10 | RF-10 |
| HU-11 | RF-11 |
| HU-12 | RF-12 |
| HU-13 | RF-13 |
| HU-14 | RF-17, RF-18 |
| HU-15 | RF-19, RF-20 |
| HU-16 | RF-21 |
| HU-17 | RF-14 |
| HU-18 | RF-15 |
| HU-19 | RF-16 |
| HU-20 | RF-22 |
| HU-21 | RF-23, RF-24 |
| HU-22 | RF-25 |
| HU-23 | RF-26, RF-27 |
| HU-24 | RF-28 |
| HU-25 | — |
| HU-26 | — |
| HU-27 | — |
| HU-28 | — |
