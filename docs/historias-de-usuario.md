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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Módulo base, sin dependencias de otras HUs |
| **Negotiable** | ✅ | Detalles de seguridad (expiración, intentos) pueden ajustarse |
| **Valuable** | ✅ | Acceso seguro al sistema, valor fundamental |
| **Estimable** | ✅ | JWT + login son patrones estándar bien conocidos |
| **Small** | ✅ | Alcance acotado: formulario + token + redirección |
| **Testable** | ✅ | ACs claros: credenciales válidas/inválidas, bloq, redirección |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

#### HU-02 "Cerrar Sesión"
**Como** usuario autenticado
**Quiero** cerrar sesión de forma segura
**Para** proteger mi cuenta y los datos del sistema

**Criterios de Aceptación:**
- Botón visible en el navbar
- Invalida el token JWT
- Redirige al login
- Limpia datos de sesión del navegador

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Funcionalidad trivial, sin dependencias externas |
| **Negotiable** | ✅ | UI placement y comportamiento de limpieza pueden variar |
| **Valuable** | ✅ | Seguridad básica, protección de datos |
| **Estimable** | ✅ | Muy simple: invalidar token + redirect |
| **Small** | ✅ | Una de las HUs más pequeñas del proyecto |
| **Testable** | ✅ | Verificar token inválido, redirect, datos limpiados |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno
**Sugerencia:** Sin cambios necesarios

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-01 (auth) como base — documentar orden |
| **Negotiable** | ✅ | Formato de formulario y validaciones pueden ajustarse |
| **Valuable** | ✅ | Gestión de personal, esencial para operación |
| **Estimable** | ✅ | CRUD estándar con validaciones conocidas |
| **Small** | ✅ | Formulario + validaciones + persistencia |
| **Testable** | ✅ | Crear usuario válido, duplicado, campos obligatorios |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-01 — orden de sprint
**Sugerencia:** Ejecutar después de HU-01 en Sprint 1

---

#### HU-04 "Editar Usuario"
**Como** administrador
**Quiero** modificar datos y roles de usuarios existentes
**Para** mantener la información actualizada

**Criterios de Aceptación:**
- Editar nombre, email, rol, estado (activo/inactivo)
- No permitir editar email si ya existe otro usuario
- Historial de cambios registrado
- Confirmación antes de guardar

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-03 (usuarios existentes) |
| **Negotiable** | ✅ | Campos editables y reglas de negocio ajustables |
| **Valuable** | ✅ | Mantener datos actualizados del personal |
| **Estimable** | ✅ | CRUD edit con validaciones estándar |
| **Small** | ✅ | Formulario edición + audit trail |
| **Testable** | ✅ | Editar válido, email duplicado, confirmación |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-03
**Sugerencia:** Ejecutar después de HU-03

---

#### HU-05 "Listar/Buscar Usuarios"
**Como** administrador
**Quiero** ver y filtrar la lista de usuarios
**Para** gestionar el personal del sistema

**Criterios de Aceptación:**
- Tabla paginada (10 por página)
- Filtros: nombre, rol, estado
- Búsqueda por nombre o email
- Acciones: editar, desactivar

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-03 (datos de usuarios) |
| **Negotiable** | ✅ | Filtros y paginación pueden ajustarse |
| **Valuable** | ✅ | Visualización y gestión del personal |
| **Estimable** | ✅ | Tabla + filtros + paginación, patrón común |
| **Small** | ✅ | Componente de tabla con filtros |
| **Testable** | ✅ | Paginar, filtrar, buscar, acciones |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-03
**Sugerencia:** Ejecutar después de HU-03

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Núcleo del sistema, sin dependencias de otras HUs |
| **Negotiable** | ✅ | Campos del formulario ajustables según necesidad |
| **Valuable** | ✅ | Registro de pacientes, funcionalidad fundamental |
| **Estimable** | ✅ | Formulario + validación + cola de espera |
| **Small** | ✅ | Alcance claro y acotado |
| **Testable** | ✅ | Cédula única, edad auto, ticket generado |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

#### HU-07 "Buscar Paciente"
**Como** usuario del sistema
**Quiero** buscar pacientes por cédula o nombre
**Para** acceder rápidamente a su información

**Criterios de Aceptación:**
- Búsqueda por cédula (exacta) o nombre (parcial)
- Resultados en tiempo real (< 500ms)
- Muestra: nombre, cédula, edad, última visita
- Click en resultado abre perfil del paciente

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-06 (pacientes existentes) |
| **Negotiable** | ✅ | Tipo de búsqueda y campos mostrados ajustables |
| **Valuable** | ✅ | Acceso rápido a información del paciente |
| **Estimable** | ✅ | Búsqueda con índice, patrón estándar |
| **Small** | ✅ | Componente de búsqueda + resultados |
| **Testable** | ✅ | Cédula exacta, nombre parcial, < 500ms |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-06
**Sugerencia:** Ejecutar después de HU-06

---

#### HU-08 "Editar Datos del Paciente"
**Como** cajero o médico
**Quiero** actualizar información del paciente
**Para** mantener datos precisos

**Criterios de Aceptación:**
- Editar: teléfono, dirección, contacto de emergencia
- No editar: cédula (identificador único)
- Historial de modificaciones con timestamp
- Auditoría de quién hizo el cambio

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-06 (paciente registrado) |
| **Negotiable** | ✅ | Campos editables y reglas ajustables |
| **Valuable** | ✅ | Mantener datos del paciente actualizados |
| **Estimable** | ✅ | Edición de campos + audit trail |
| **Small** | ✅ | Formulario edición + historial |
| **Testable** | ✅ | Editar campos válidos, bloquear cédula, audit |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-06
**Sugerencia:** Ejecutar después de HU-06

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-06 (paciente) y HU-01 (auth/turno) |
| **Negotiable** | ✅ | Campos y rangos de alerta ajustables |
| **Valuable** | ✅ | Documentación clínica esencial |
| **Estimable** | ✅ | Formulario + validación + alertas |
| **Small** | ✅ | Un formulario con 7 campos y alertas |
| **Testable** | ✅ | Valores dentro/fuera de rango, asociación correcta |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-06
**Sugerencia:** Ejecutar después de HU-06 en Sprint 2

---

#### HU-10 "Visualizar Signos Vitales"
**Como** médico o enfermera
**Quiero** ver el historial de signos vitales del paciente
**Para** evaluar tendencias y evolución

**Criterios de Aceptación:**
- Gráfica de tendencia por cada signo vital
- Tabla cronológica con todos los registros
- Filtro por rango de fechas
- Comparación entre registros

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-09 (datos de signos vitales) |
| **Negotiable** | ✅ | Tipo de gráfica y filtros ajustables |
| **Valuable** | ✅ | Evaluación de tendencias, decisión clínica |
| **Estimable** | ✅ | Gráfica + tabla + filtro, patrones conocidos |
| **Small** | ✅ | Visualización de datos existentes |
| **Testable** | ✅ | Gráfica muestra datos, filtro funciona, comparación |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-09
**Sugerencia:** Ejecutar después de HU-09

---

#### HU-11 "Editar Signos Vitales"
**Como** enfermera
**Quiero** corregir registros de signos vitales erróneos
**Para** mantener la integridad de los datos clínicos

**Criterios de Aceptación:**
- Solo editable durante las primeras 2 horas
- Motivo de edición obligatorio
- Se preserva el registro original (audit trail)
- Notificación al médico si el paciente ya fue visto

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-09 (registros de signos vitales) |
| **Negotiable** | ✅ | Ventana de tiempo y reglas ajustables |
| **Valuable** | ✅ | Integridad de datos clínicos, corrección de errores |
| **Estimable** | ✅ | Edición condicional + audit trail + notificación |
| **Small** | ✅ | Lógica de edición con restricción temporal |
| **Testable** | ✅ | Editar dentro/fuera de 2h, motivo obligatorio, audit |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-09
**Sugerencia:** Ejecutar después de HU-09

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Módulo farmacia autónomo, sin dependencias de otras HUs |
| **Negotiable** | ✅ | Campos y reglas de alerta ajustables |
| **Valuable** | ✅ | Control de inventario, disponibilidad crítica |
| **Estimable** | ✅ | CRUD estándar + alertas + búsqueda |
| **Small** | ✅ | Módulo completo pero acotado |
| **Testable** | ✅ | CRUD, alertas stock bajo, búsqueda, vencimientos |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-12 (inventario de medicamentos) |
| **Negotiable** | ✅ | Campos y reglas de dispensación ajustables |
| **Valuable** | ✅ | Control de consumo, prevención de errores |
| **Estimable** | ✅ | Registro + validación stock + descuento |
| **Small** | ✅ | Flujo de registro de dosis |
| **Testable** | ✅ | Stock suficiente/insuficiente, descuento correcto |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-12
**Sugerencia:** Ejecutar después de HU-12

---

#### HU-14 "Verificar Interacciones"
**Como** farmacéutico o médico
**Quiero** que el sistema verifique interacciones medicamentosas
**Para** prevenir reacciones adversas

**Criterios de Aceptación:**
- Al prescribir/dispensar, verificar contra medicamentos activos del paciente
- Alerta visual + sonora por interacción grave
- Sugerencia de alternativa cuando sea posible
- Registro de interacciones detectadas

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-12 (medicamentos) y datos de paciente |
| **Negotiable** | ✅ | Base de datos de interacciones y reglas ajustables |
| **Valuable** | ✅ | Seguridad del paciente, prevención de reacciones adversas |
| **Estimable** | ⚠️ | Algoritmo de verificación requiere clarificación de reglas |
| **Small** | ✅ | Verificación + alerta + registro |
| **Testable** | ✅ | Interacción detectada, alerta activada, alternativa sugerida |

**Score INVEST:** 5/6
**Riesgo principal:** Complejidad del algoritmo de interacciones — clarificar reglas de negocio
**Sugerencia:** Definir fuente de datos de interacciones (API externa o base propia)

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-06 (paciente), HU-09 (signos vitales), integración IA |
| **Negotiable** | ✅ | Modelo IA, formato de respuesta ajustables |
| **Valuable** | ✅ | Alto valor: apoyo a decisión clínica con IA |
| **Estimable** | ⚠️ | Integración con modelo IA, tiempos de respuesta variables |
| **Small** | ⚠️ | **Split recomendado**: HU-15a (enviar datos) + HU-15b (recibir resultado IA) |
| **Testable** | ✅ | Envío de datos, respuesta con diagnósticos, tiempo < 10s |

**Score INVEST:** 4/6
**Riesgo principal:** Integración IA + tamaño potencialmente grande
**Sugerencia:** **Split**: HU-15a "Enviar datos a IA" (endpoint + validación) y HU-15b "Recibir diagnóstico IA" (respuesta + UI)

---

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-15 (diagnósticos IA generados) |
| **Negotiable** | ✅ | Formato de vista y opciones ajustables |
| **Valuable** | ✅ | Validación humana del diagnóstico IA |
| **Estimable** | ✅ | UI de revisión + feedback loop |
| **Small** | ✅ | Componente de revisión con opciones |
| **Testable** | ✅ | Aceptar, rechazar, modificar, comentario obligatorio |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-15 — flujo secuencial
**Sugerencia:** Ejecutar inmediatamente después de HU-15

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-09 (signos vitales) y HU-15 (IA para sugerencia) |
| **Negotiable** | ✅ | Escala de triaje y reglas ajustables |
| **Valuable** | ✅ | Priorización de atención, crítico para urgencias |
| **Estimable** | ✅ | Algoritmo de clasificación + override manual |
| **Small** | ✅ | Clasificación + UI de override |
| **Testable** | ✅ | Asignación por IA, override manual, reclasificación |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-09 y HU-15
**Sugerencia:** Ejecutar en Sprint 3 después de ambas dependencias

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Sistema de notificaciones independiente, WebSocket propio |
| **Negotiable** | ✅ | Canales y formato de notificación ajustables |
| **Valuable** | ✅ | Respuesta rápida a emergencias, vidas en juego |
| **Estimable** | ✅ | WebSocket + UI de panel, patrón conocido |
| **Small** | ✅ | Notificación en tiempo real + panel |
| **Testable** | ✅ | Notificación recibida, sonido, panel actualizado |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

#### HU-19 "Configurar Notificaciones"
**Como** usuario del sistema
**Quiero** configurar qué notificaciones recibo y cómo
**Para** personalizar mi experiencia

**Criterios de Aceptación:**
- Tipos: emergencias, asignaciones, recordatorios
- Canales: push, email, sonido
- Filtro por nivel de urgencia
- Horario de silencio configurable

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Configuración de usuario, sin dependencias de otras HUs |
| **Negotiable** | ✅ | Tipos de notificación y canales ajustables |
| **Valuable** | ✅ | Personalización de experiencia, reducir ruido |
| **Estimable** | ✅ | Formulario de configuración + persistencia |
| **Small** | ✅ | Configuración de preferencias |
| **Testable** | ✅ | Configurar tipos, canales, horario silencio |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-15 (sugerencia IA) y HU-16 (revisión) |
| **Negotiable** | ✅ | Formulario y reglas de validación ajustables |
| **Valuable** | ✅ | Cierre del loop de validación humana-IA |
| **Estimable** | ✅ | Formulario + registro + métricas |
| **Small** | ✅ | Componente de validación con feedback |
| **Testable** | ✅ | Aceptar, rechazar, modificar, métricas actualizadas |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-15 y HU-16 — cierre del loop
**Sugerencia:** Ejecutar después de ambas en Sprint 3

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Módulo de insumos independiente de medicamentos |
| **Negotiable** | ✅ | Tipos de insumos y reglas de alerta ajustables |
| **Valuable** | ✅ | Disponibilidad de insumos, operación continua |
| **Estimable** | ✅ | CRUD + alertas + reporte, patrones estándar |
| **Small** | ✅ | Módulo CRUD completo pero acotado |
| **Testable** | ✅ | CRUD, alertas stock bajo, consumo, reporte |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Sistema de alertas transversal, sin dependencias |
| **Negotiable** | ✅ | Tipos de emergencia y reglas ajustables |
| **Valuable** | ✅ | Movilización rápida, vidas en juego |
| **Estimable** | ✅ | Botón + notificación masiva + registro |
| **Small** | ✅ | Activación de alerta + notificación |
| **Testable** | ✅ | Botón visible, notificación enviada, registro creado |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

---

#### HU-23 "Responder a Alerta"
**Como** usuario notificado
**Quiero** confirmar recepción y llegada a emergencia
**Para** que el equipo sepa quién está respondiendo

**Criterios de Aceptación:**
- Botón "Respondiendo" con tiempo estimado
- Dashboard muestra quiénes están en camino
- Tiempo de respuesta promedio registrado
- Escalación si nadie responde en 5 min

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-22 (alerta activa para responder) |
| **Negotiable** | ✅ | Tiempos de escalamiento y formato ajustables |
| **Valuable** | ✅ | Coordinación de respuesta a emergencia |
| **Estimable** | ✅ | Botón + dashboard + temporizador |
| **Small** | ✅ | Respuesta a alerta existente |
| **Testable** | ✅ | Responder, dashboard actualizado, escalamiento |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-22
**Sugerencia:** Ejecutar después de HU-22

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Requiere HU-06 (paciente) y HU-17 (triaje) |
| **Negotiable** | ✅ | Estados y formato de vista ajustables |
| **Valuable** | ✅ | Transparencia para paciente/familiar |
| **Estimable** | ✅ | Vista de estado + código de seguimiento |
| **Small** | ✅ | Componente de consulta pública |
| **Testable** | ✅ | Código válido, estados correctos, sin datos sensibles |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia con HU-06 y HU-17
**Sugerencia:** Ejecutar después de ambas en Sprint 3

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Agrega datos de múltiples módulos (pacientes, triaje, alertas) |
| **Negotiable** | ✅ | Métricas y formato de gráficos ajustables |
| **Valuable** | ✅ | Visión operativa completa, toma de decisiones |
| **Estimable** | ⚠️ | Integración de datos de varios módulos compleja |
| **Small** | ⚠️ | **Split recomendado**: HU-25a (métricas core) + HU-25b (gráficos avanzados) |
| **Testable** | ✅ | Métricas calculadas correctamente, gráficos renderizados |

**Score INVEST:** 4/6
**Riesgo principal:** Agrega datos de múltiples módulos, potencialmente grande
**Sugerencia:** **Split**: HU-25a "Métricas del Dashboard" (KPIs numéricos) y HU-25b "Gráficos del Dashboard" (visualización)

---

#### HU-26 "Generar Reportes"
**Como** administrador
**Quiero** generar reportes de actividad
**Para** análisis y cumplimiento normativo

**Criterios de Aceptación:**
- Tipos: diario, semanal, mensual, por médico, por diagnóstico
- Exportar: PDF, Excel
- Filtros: rango fechas, departamento, médico
- Estadísticas: pacientes atendidos, diagnósticos más frecuentes, tiempos promedio

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ⚠️ | Depende de datos acumulados de otros módulos |
| **Negotiable** | ✅ | Tipos de reporte y filtros ajustables |
| **Valuable** | ✅ | Cumplimiento normativo, análisis operativo |
| **Estimable** | ⚠️ | Múltiples tipos de reporte + exportación PDF/Excel |
| **Small** | ⚠️ | **Split recomendado**: HU-26a (reportes básicos) + HU-26b (exportación avanzada) |
| **Testable** | ✅ | Generar cada tipo, exportar, filtros funcionan |

**Score INVEST:** 4/6
**Riesgo principal:** Múltiples tipos de reporte + exportación = alcance amplio
**Sugerencia:** **Split**: HU-26a "Generar Reportes" (consulta + vista) y HU-26b "Exportar Reportes" (PDF/Excel)

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Sistema de auditoría transversal, sin dependencias funcionales |
| **Negotiable** | ✅ | Reglas de alerta y retención ajustables |
| **Valuable** | ✅ | Seguridad, cumplimiento normativo, detección de anomalías |
| **Estimable** | ✅ | Logging + alertas + exportación |
| **Small** | ✅ | Módulo de auditoría con reglas claras |
| **Testable** | ✅ | Log generado, alertas activadas, exportación funcional |

**Score INVEST:** 6/6
**Riesgo principal:** Ninguno significativo
**Sugerencia:** Sin cambios necesarios

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

#### Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | ✅ | Requisito no funcional transversal |
| **Negotiable** | ✅ | Umbrales de tiempo ajustables |
| **Valuable** | ✅ | Rendimiento crítico en entorno de urgencias |
| **Estimable** | ⚠️ | Requiere profiling y optimización iterativa |
| **Small** | ⚠️ | **Candidata a migrar a RNF** — métricas globales, no funcional aislada |
| **Testable** | ⚠️ | Métricas de rendimiento requieren benchmarks y entorno de carga |

**Score INVEST:** 4/6
**Riesgo principal:** No-funcional, difícil de testear aislado, métricas dependen del estado del sistema
**Sugerencia:** **Migrar a `docs/requisitos.md` como RNF** — las métricas de rendimiento ya están cubiertas como requisitos no funcionales

---

## Resumen por Sprint

| Sprint | HUs | Descripción |
|--------|-----|-------------|
| **Sprint 1** | HU-01 a HU-08 | Autenticación, Usuarios, Pacientes |
| **Sprint 2** | HU-09 a HU-16 | Signos Vitales, Farmacología, IA Diagnóstico |
| **Sprint 3** | HU-17 a HU-28 | Triaje, Notificaciones, Alertas, Dashboard, Seguridad |

## Resumen INVEST

| Score | HUs | Acción |
|-------|-----|--------|
| **6/6** | HU-01, HU-02, HU-06, HU-12, HU-18, HU-19, HU-21, HU-22, HU-27 | Sin cambios |
| **5/6** | HU-03, HU-04, HU-05, HU-07, HU-08, HU-09, HU-10, HU-11, HU-13, HU-14, HU-16, HU-17, HU-20, HU-23, HU-24 | Documentar dependencia |
| **4/6** | HU-15, HU-25, HU-26, HU-28 | Split o migrar a RNF |