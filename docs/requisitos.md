# Requisitos — UrgencyAI

## 1. Requisitos Funcionales

### 1.1 Módulo de Autenticación y Gestión de Usuarios

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-01 | Inicio de Sesión | El sistema debe permitir a los usuarios autenticarse con email y contraseña. Al ser correctos, redirigir al dashboard correspondiente según su rol. |
| RF-02 | Cierre de Sesión por Inactividad | El sistema debe cerrar la sesión automáticamente tras 30 minutos de inactividad, mostrando un aviso 2 minutos antes. |
| RF-03 | Crear Usuario | El administrador debe poder crear usuarios con nombre completo, email, contraseña y rol del sistema. |
| RF-04 | Editar Usuario | El administrador debe poder modificar nombre, email y rol de un usuario existente. La contraseña solo se cambia si se ingresa una nueva. |
| RF-05 | Listar y Buscar Usuarios | El administrador debe ver todos los usuarios en tabla con opción de buscar, filtrar por rol y paginar. |

### 1.2 Módulo de Gestión de Pacientes

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-06 | Registrar Paciente | El cajero debe registrar un paciente con datos personales, contacto y seguro médico. |
| RF-07 | Buscar Paciente | El cajero debe buscar pacientes por nombre, cédula o expediente y ver resultados en tabla. |
| RF-08 | Editar Paciente | El cajero debe modificar información de un paciente existente desde su ficha. |

### 1.3 Módulo de Signos Vitales

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-09 | Registrar Signos Vitales | La enfermera debe registrar signos vitales: temperatura, presión arterial, saturación O2, frecuencia cardíaca y respiratoria. |
| RF-10 | Visualizar Historial Signos Vitales | La enfermera debe ver el historial de signos vitales en tabla cronológica con filtro por fechas. |
| RF-11 | Editar Signos Vitales | La enfermera debe poder corregir signos vitales registrados por error, manteniendo registro de la edición. |

### 1.4 Módulo de Farmacia

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-12 | Registrar Dosis Dispensada | El farmacéutico debe registrar cada dosis dispensada con medicamento, cantidad, vía de administración y observaciones. |
| RF-13 | Verificar Interacciones Medicamentosas | El sistema debe verificar automáticamente interacciones entre el medicamento a dispensar y los que el paciente ya toma. |
| RF-14 | Gestionar Inventario | El farmacéutico debe administrar inventario: agregar, actualizar stock, definir stock mínimo y vencimiento. |
| RF-15 | Alertas de Stock Bajo | El sistema debe activar alertas automáticas cuando stock cae debajo del mínimo configurable. |
| RF-16 | Responder Alertas de Stock | El farmacéutico debe poder responder alertas con acciones: solicitar pedido, transferencia o resolver. |

### 1.5 Módulo de Diagnóstico Asistido por IA

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-17 | Solicitar Diagnóstico IA | El médico debe ingresar síntomas, signos vitales y antecedentes para obtener sugerencia de diagnóstico por IA. |
| RF-18 | Mostrar Diagnósticos Sugeridos | La IA debe generar al menos 3 diagnósticos con nivel de confianza porcentual, descripción y recomendaciones. |
| RF-19 | Validar/Descartar Sugerencias IA | El médico debe poder validar (aceptar) o descartar (con motivo) cada sugerencia de IA. |
| RF-20 | Aprendizaje del Modelo IA | El sistema debe registrar validaciones/descartes para retroalimentar el modelo de diagnóstico. |

### 1.6 Módulo de Notificaciones

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-21 | Notificaciones en Tiempo Real | El sistema debe enviar notificaciones instantáneas vía WebSocket (alertas stock, signos críticos, asignación pacientes). |
| RF-22 | Configurar Preferencias Notificación | Cada usuario debe configurar qué notificaciones recibe y por qué canal (en-app, sonido, email). |

### 1.7 Módulo de Administración y Reportes

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-23 | Generar Reportes | El administrador debe generar reportes de atenciones, diagnósticos frecuentes y productividad por período. |
| RF-24 | Exportar Reportes | El sistema debe permitir exportar reportes en formato CSV o PDF. |
| RF-25 | Auditoría de Accesos | El administrador debe revisar registro de auditoría: usuario, fecha/hora, acción, IP y módulo. |

### 1.8 Módulo de Monitoreo del Sistema

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RF-26 | Monitorear Estado del Sistema | El administrador debe ver en tiempo real: CPU, RAM, conexiones activas y uptime. |
| RF-27 | Ejecutar Optimizaciones | El administrador debe ejecutar mantenimiento: limpiar caché, reiniciar servicios, optimizar BD. |
| RF-28 | Estado de Pacientes en Tiempo Real | El sistema debe mostrar estado de pacientes en sala: ubicación, estado clínico, tiempo de espera, responsable. |

---

## 2. Requisitos No Funcionales

### 2.1 Seguridad

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-01 | Hash de Contraseñas | Todas las contraseñas se almacenan hasheadas con bcrypt, mínimo 12 rondas de salt. |
| RNF-02 | Autenticación JWT | Autenticación mediante tokens JWT con expiración de 24 horas y refresco automático. |
| RNF-03 | Autorización por Roles | Cada endpoint debe verificar que el usuario tenga el rol necesario para acceder. |
| RNF-04 | HTTPS Obligatorio | Todas las comunicaciones en producción deben ser sobre HTTPS con certificado válido. |
| RNF-05 | Registro de Auditoría | El sistema debe registrar acciones críticas: login, logout, creación, edición y eliminación. |
| RNF-06 | Protección Inyección y XSS | El sistema debe estar protegido contra inyección SQL, XSS y ataques comunes de web. |

### 2.2 Rendimiento

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-07 | Tiempo Respuesta API | La API debe responder en menos de 200ms en operaciones CRUD estándar. |
| RNF-08 | Tiempo Respuesta IA | El servicio de diagnóstico IA debe retornar resultados en menos de 5 segundos. |
| RNF-09 | Concurrencia | El sistema debe soportar al menos 50 usuarios concurrentes sin degradación. |
| RNF-10 | Paginación | Los listados que superen 20 registros deben implementar paginación server-side. |

### 2.3 Disponibilidad

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-11 | Disponibilidad Sistema | Disponibilidad del 99% (máx 8.76 horas downtime no planificado/año). |
| RNF-12 | Backup Automático | Backup automático de la base de datos cada 6 horas en ubicación segura. |
| RNF-13 | Logs Centralizados | Los logs de error deben centralizarse para diagnóstico de fallos. |

### 2.4 Usabilidad

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-14 | Interfaz Responsiva | La interfaz web debe adaptarse a desktop, tablet y móvil. |
| RNF-15 | Curva de Aprendizaje | Un nuevo usuario debe poder realizar tareas básicas después de máximo 30 minutos sin entrenamiento. |
| RNF-16 | Navegación Consistente | Todas las pantallas deben mantener sidebar fija y breadcrumbs de ubicación. |
| RNF-17 | Mensajes de Error Claros | Los mensajes de error deben ser comprensibles, en español e indicar cómo resolver. |

### 2.5 Escalabilidad

| ID | Requisito | Descripción |
|----|-----------|-------------|
| RNF-18 | Arquitectura Microservicios | Desacoplar frontend, backend API y servicio de IA en servicios independientes. |
| RNF-19 | Base de Datos Normalizada | PostgreSQL con diseño normalizado hasta 3FN. |
| RNF-20 | API Versionada | API REST versionada (v1/) para evolución sin romper clientes. |

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
