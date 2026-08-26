# Historias de Usuario - UrgencyAI

## Sprint 1: Fundamentos (Semanas 1-3)

### Epic: Autenticación y Seguridad

#### HU-01 "Iniciar Sesión"
**Como** usuario del sistema
**Quiero** iniciar sesión con mis credenciales
**Para** acceder a las funcionalidades según mi rol

**Criterios de Aceptación:**
- Login con email y contraseña
- Token JWT expira en 8 horas
- Bloqueo tras 3 intentos fallidos
- Redirección según rol (Admin→Dashboard, Médico→Pacientes, etc.)

#### HU-02 "Cerrar Sesión"
**Como** usuario autenticado
**Quiero** cerrar sesión de forma segura
**Para** proteger mi cuenta y los datos del sistema

**Criterios de Aceptación:**
- Botón visible en el navbar
- Invalida el token JWT
- Redirige al login
- Limpia datos de sesión del navegador

---

### Epic: Gestión de Usuarios

#### HU-03 "Crear Usuario"
**Como** administrador
**Quiero** crear nuevos usuarios con roles específicos
**Para** que el personal pueda acceder al sistema

**Criterios de Aceptación:**
- Formulario con nombre, email, contraseña, rol
- Roles válidos: Admin, Cajero, Médico, Enfermera, Farmacéutico
- Contraseña mínimo 8 caracteres con complejidad
- Email único en el sistema
- Confirmación antes de crear

#### HU-04 "Editar Usuario"
**Como** administrador
**Quiero** modificar datos y roles de usuarios existentes
**Para** mantener la información actualizada

**Criterios de Aceptación:**
- Editar nombre, email, rol, estado (activo/inactivo)
- No permitir editar email si ya existe otro usuario
- Historial de cambios registrado
- Confirmación antes de guardar

#### HU-05 "Listar/Buscar Usuarios"
**Como** administrador
**Quiero** ver y filtrar la lista de usuarios
**Para** gestionar el personal del sistema

**Criterios de Aceptación:**
- Tabla paginada (10 por página)
- Filtros: nombre, rol, estado
- Búsqueda por nombre o email
- Acciones: editar, desactivar

---

### Epic: Gestión de Pacientes

#### HU-06 "Registrar Paciente"
**Como** cajero
**Quiero** registrar un nuevo paciente con sus datos
**Para** que pueda ser atendido en urgencias

**Criterios de Aceptación:**
- Formulario: nombre, cédula, fecha nacimiento, género, teléfono, dirección, contacto de emergencia
- Cédula única en el sistema
- Fecha de nacimiento calcula edad automáticamente
- Paciente se asigna a cola de espera
- Confirmación con número de ticket

#### HU-07 "Buscar Paciente"
**Como** usuario del sistema
**Quiero** buscar pacientes por cédula o nombre
**Para** acceder rápidamente a su información

**Criterios de Aceptación:**
- Búsqueda por cédula (exacta) o nombre (parcial)
- Resultados en tiempo real (< 500ms)
- Muestra: nombre, cédula, edad, última visita
- Click en resultado abre perfil del paciente

#### HU-08 "Editar Datos del Paciente"
**Como** cajero o médico
**Quiero** actualizar información del paciente
**Para** mantener datos precisos

**Criterios de Aceptación:**
- Editar: teléfono, dirección, contacto de emergencia
- No editar: cédula (identificador único)
- Historial de modificaciones con timestamp
- Auditoría de quién hizo el cambio

---

## Sprint 2: Funcionalidades Core (Semanas 4-6)

### Epic: Signos Vitales

#### HU-09 "Registrar Signos Vitales"
**Como** enfermera
**Quiero** registrar signos vitales de un paciente
**Para** documentar su estado clínico

**Criterios de Aceptación:**
- Campos: temperatura, presión arterial, pulso, frecuencia respiratoria, saturación O2, peso, talla
- Alertas automáticas si valores fuera de rango
- Asociación automática con paciente y turno
- Formulario validado con rangos clínicos

#### HU-10 "Visualizar Signos Vitales"
**Como** médico o enfermera
**Quiero** ver el historial de signos vitales del paciente
**Para** evaluar tendencias y evolución

**Criterios de Aceptación:**
- Gráfica de tendencia por cada signo vital
- Tabla cronológica con todos los registros
- Filtro por rango de fechas
- Comparación entre registros

#### HU-11 "Editar Signos Vitales"
**Como** enfermera
**Quiero** corregir registros de signos vitales erróneos
**Para** mantener la integridad de los datos clínicos

**Criterios de Aceptación:**
- Solo editable durante las primeras 2 horas
- Motivo de edición obligatorio
- Se preserva el registro original (audit trail)
- Notificación al médico si el paciente ya fue visto

---

### Epic: Farmacología

#### HU-12 "Gestionar Medicamentos"
**Como** farmacéutico
**Quiero** administrar el inventario de medicamentos
**Para** garantizar disponibilidad en urgencias

**Criterios de Aceptación:**
- CRUD completo: nombre, principio activo, concentración, stock, categoría
- Alertas de stock bajo (configurable por medicamento)
- Registro de lotes y fechas de vencimiento
- Búsqueda por nombre o principio activo

#### HU-13 "Registrar Dosis"
**Como** farmacéutico
**Quiero** registrar la dosis dispensada a un paciente
**Para** controlar el consumo y evitar errores

**Criterios de Aceptación:**
- Selección de medicamento del inventario
- Cantidad, vía de administración, frecuencia
- Validación de stock disponible
- Descuento automático del inventario
- Asociación con prescripción médica

#### HU-14 "Verificar Interacciones"
**Como** farmacéutico o médico
**Quiero** que el sistema verifique interacciones medicamentosas
**Para** prevenir reacciones adversas

**Criterios de Aceptación:**
- Al prescribir/dispensar, verificar contra medicamentos activos del paciente
- Alerta visual + sonora por interacción grave
- Sugerencia de alternativa cuando sea posible
- Registro de interacciones detectadas

---

### Epic: Diagnóstico con IA

#### HU-15 "Solicitar Diagnóstico IA"
**Como** médico
**Quiero** enviar datos del paciente al sistema de IA para obtener un diagnóstico sugerido
**Para** apoyar mi decisión clínica

**Criterios de Aceptación:**
- Envía: síntomas, signos vitales, historial, alergias
- IA responde con diagnósticos diferenciales (máx. 5)
- Cada diagnóstico con nivel de confianza (%)
- Sugerencia de exámenes complementarios
- Tiempo de respuesta < 10 segundos

#### HU-16 "Revisar Sugerencia IA"
**Como** médico
**Quiero** revisar y evaluar las sugerencias de IA
**Para** tomar una decisión informada

**Criterios de Aceptación:**
- Vista detallada de cada diagnóstico sugerido
- Opción de aceptar, rechazar o modificar
- Comentario obligatorio al rechazar
- Justificación clínica registrada
- La IA aprende de las decisiones del médico

---

## Sprint 3: Funcionalidades Avanzadas (Semanas 7-9)

### Epic: Triaje

#### HU-17 "Clasificar por Triaje"
**Como** enfermera
**Quiero** clasificar pacientes por nivel de urgencia
**Para** priorizar la atención según gravedad

**Criterios de Aceptación:**
- Escala de triaje: Rojo (I), Naranja (II), Amarillo (III), Verde (IV), Azul (V)
- Basado en signos vitales + síntomas reportados
- Asignación automática sugerida por IA
- Override manual con justificación
- Reclasificación automática si signos vitales cambian

---

### Epic: Notificaciones

#### HU-18 "Recibir Notificación de Emergencia"
**Como** médico o enfermera
**Quiero** recibir alertas en tiempo real de pacientes críticos
**Para** responder rápidamente a emergencias

**Criterios de Aceptación:**
- Notificación push + sonido para pacientes Rojo/Naranja
- Aparece en panel de notificaciones
- Incluye: paciente, nivel, signos vitales clave
- Marcar como leída/atendida
- Historial de notificaciones

#### HU-19 "Configurar Notificaciones"
**Como** usuario del sistema
**Quiero** configurar qué notificaciones recibo y cómo
**Para** personalizar mi experiencia

**Criterios de Aceptación:**
- Tipos: emergencias, asignaciones, recordatorios
- Canales: push, email, sonido
- Filtro por nivel de urgencia
- Horario de silencio configurable

---

### Epic: Validación Humana

#### HU-20 "Validar Diagnóstico IA"
**Como** médico
**Quiero** validar o rechazar el diagnóstico sugerido por IA
**Para** asegurar la calidad del diagnóstico

**Criterios de Aceptación:**
- Formulario de validación: aceptar/rechazar/modificar
- Comentario clínico obligatorio
- El diagnóstico final queda registrado
- Métricas de precisión de IA se actualizan
- Auditoría completa de la decisión

---

### Epic: Gestión de Insumos

#### HU-21 "Gestionar Insumos Médicos"
**Como** administrador
**Quiero** controlar el inventario de insumos no medicamentos
**Para** garantizar disponibilidad operativa

**Criterios de Aceptación:**
- CRUD: guantes, jeringas, gasas, etc.
- Stock mínimo configurable
- Alertas de reabastecimiento
- Registro de consumo por turno
- Reporte de consumo mensual

---

### Epic: Alertas de Emergencia

#### HU-22 "Activar Alerta de Emergencia"
**Como** médico o enfermera
**Quiero** activar una alerta de código rojo
**Para** movilizar recursos rápidamente

**Criterios de Aceptación:**
- Botón de emergencia visible siempre
- Al activar: notifica a todo el personal
- Incluye: ubicación, tipo de emergencia
- Temporizador de respuesta
- Registro completo del evento

#### HU-23 "Responder a Alerta"
**Como** usuario notificado
**Quiero** confirmar recepción y arrival a emergencia
**Para** que el equipo sepa quién está respondiendo

**Criterios de Aceptación:**
- Botón "Respondiendo" con tiempo estimado
- Dashboard muestra quiénes están en camino
- Tiempo de respuesta promedio registrado
- Escalación si nadie responde en 5 min

---

### Epic: Asistencia al Paciente

#### HU-24 "Consultar Estado de Paciente"
**Como** paciente o familiar
**Quiero** ver el estado de atención del paciente
**Para** saber cuándo será atendido

**Criterios de Aceptación:**
- Código de seguimiento único
- Estado: Esperando → En triaje → En atención → Diagnosticando → Farmacia → Alta
- Tiempo estimado de espera
- Nivel de triaje asignado
- Sin información clínica sensible

---

### Epic: Dashboard y Reportes

#### HU-25 "Ver Dashboard Principal"
**Como** administrador
**Quiero** ver un dashboard con métricas en tiempo real
**Para** tomar decisiones operativas

**Criterios de Aceptación:**
- Pacientes en espera, en atención, dados de alta
- Tiempo promedio de espera
- Ocupación por área
- Alertas activas
- Gráficos de tendencia diaria/semanal

#### HU-26 "Generar Reportes"
**Como** administrador
**Quiero** generar reportes de actividad
**Para** análisis y cumplimiento normativo

**Criterios de Aceptación:**
- Tipos: diario, semanal, mensual, por médico, por diagnóstico
- Exportar: PDF, Excel
- Filtros: rango fechas, departamento, médico
- Estadísticas: pacientes atendidos, diagnósticos más frecuentes, tiempos promedio

---

### Epic: Seguridad

#### HU-27 "Auditoría de Accesos"
**Como** administrador
**Quiero** revisar el registro de accesos al sistema
**Para** detectar actividades sospechosas

**Criterios de Aceptación:**
- Log de cada login/logout con IP y timestamp
- Registro de acceso a datos sensibles del paciente
- Alertas por accesos fuera de horario
- Exportación del log de auditoría
- Retención de datos: 1 año mínimo

---

### Epic: UI/UX y Performance

#### HU-28 "Optimizar Rendimiento"
**Como** usuario del sistema
**Quiero** que el sistema responda rápidamente
**Para** no perder tiempo en momentos críticos

**Criterios de Aceptación:**
- Tiempo de carga inicial < 3 segundos
- Búsquedas < 500ms
- Notificaciones en tiempo real < 1 segundo
- Optimización de consultas SQL
- Cache para datos estáticos
- Responsive design para tablets

---

## Resumen por Sprint

| Sprint | HUs | Descripción |
|--------|-----|-------------|
| **Sprint 1** | HU-01 a HU-08 | Autenticación, Usuarios, Pacientes |
| **Sprint 2** | HU-09 a HU-16 | Signos Vitales, Farmacología, IA Diagnóstico |
| **Sprint 3** | HU-17 a HU-28 | Triaje, Notificaciones, Alertas, Dashboard, Seguridad |
