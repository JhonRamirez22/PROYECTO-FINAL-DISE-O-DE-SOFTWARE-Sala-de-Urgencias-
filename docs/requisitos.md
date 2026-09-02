# Requisitos — UrgencyAI

## 1. Requisitos Funcionales

### 1.1 Módulo de Autenticación y Gestión de Usuarios

---

#### RF-01 — Inicio de Sesión

- **Descripción:** El sistema debe permitir a los usuarios autenticarse con email y contraseña. Al ser correctos, redirigir al dashboard correspondiente según su rol.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-01
- **Criterios de Aceptación:**
  1. El formulario contiene campos de email y contraseña
  2. El sistema valida que ambos campos estén llenos antes de enviar
  3. Si las credenciales son correctas, redirige al dashboard del rol del usuario
  4. Si las credenciales son incorrectas, muestra mensaje de error "Email o contraseña incorrectos"
  5. Se muestra el mensaje de error por máximo 5 segundos y luego se limpia

---

#### RF-02 — Cierre de Sesión por Inactividad

- **Descripción:** El sistema debe cerrar la sesión del usuario automáticamente tras 30 minutos de inactividad (sin movimiento del mouse ni teclado), mostrando un aviso 2 minutos antes.
- **Prioridad:** Media
- **Historia de Usuario:** HU-02
- **Criterios de Aceptación:**
  1. Se detecta inactividad del usuario (mouse, teclado, scroll)
  2. A los 28 minutos se muestra un modal: "Tu sesión expirará en 2 minutos"
  3. Si el usuario hace clic en "Continuar", se reinicia el contador
  4. Si el usuario no responde en 2 minutos, se cierra la sesión y redirige al login
  5. El token JWT se invalida en el servidor

---

#### RF-03 — Crear Usuario

- **Descripción:** El administrador debe poder crear nuevos usuarios ingresando nombre completo, email, contraseña y seleccionando un rol del sistema.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-03
- **Criterios de Aceptación:**
  1. El formulario tiene campos: nombre, email, contraseña, rol (select)
  2. Los roles disponibles son: Cajero, Médico, Enfermera, Farmacéutico, Administrador
  3. La contraseña debe tener mínimo 8 caracteres
  4. El email debe tener formato válido y no estar registrado
  5. Al guardar, se muestra confirmación "Usuario creado exitosamente"
  6. El nuevo usuario aparece en la lista de usuarios

---

#### RF-04 — Editar Usuario

- **Descripción:** El administrador debe poder modificar el nombre, email y rol de un usuario existente. La contraseña solo se cambia si se ingresa una nueva.
- **Prioridad:** Media
- **Historia de Usuario:** HU-04
- **Criterios de Aceptación:**
  1. El formulario se carga con los datos actuales del usuario
  2. El administrador puede modificar nombre, email y rol
  3. Si se deja el campo de contraseña vacío, no se modifica
  4. Si se ingresa una nueva contraseña, se valida mínimo 8 caracteres
  5. Al guardar, se muestra confirmación "Usuario actualizado"
  6. Los cambios se reflejan inmediatamente en la lista

---

#### RF-05 — Listar y Buscar Usuarios

- **Descripción:** El administrador debe poder ver todos los usuarios en una tabla con opción de buscar por nombre/email, filtrar por rol y paginar resultados.
- **Prioridad:** Media
- **Historia de Usuario:** HU-05
- **Criterios de Aceptación:**
  1. Se muestra tabla con columnas: Nombre, Email, Rol, Estado, Acciones
  2. Barra de búsqueda filtra en tiempo real por nombre o email
  3. Filtro por rol (select): Todos, Cajero, Médico, Enfermera, Farmacéutico, Administrador
  4. Paginación de 10 usuarios por página
  5. Cada fila tiene botones de Editar y Eliminar/Desactivar

---

### 1.2 Módulo de Gestión de Pacientes

---

#### RF-06 — Registrar Paciente

- **Descripción:** El cajero debe poder registrar un nuevo paciente ingresando datos personales (nombre, cédula, fecha de nacimiento, género), datos de contacto (teléfono, dirección) y datos del seguro médico.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-06
- **Criterios de Aceptación:**
  1. Formulario con secciones: Datos Personales, Contacto, Seguro
  2. Cédula es obligatoria y debe ser numérica
  3. Fecha de nacimiento en formato DD/MM/YYYY
  4. Género: Masculino, Femernino, Otro (select)
  5. Si el paciente ya existe (misma cédula), se muestra aviso
  6. Al guardar, se genera número de expediente automático
  7. Se muestra confirmación "Paciente registrado exitosamente"

---

#### RF-07 — Buscar Paciente

- **Descripción:** El cajero debe poder buscar pacientes existentes por nombre, cédula o número de expediente, y ver los resultados en una tabla.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-07
- **Criterios de Aceptación:**
  1. Barra de búsqueda acepta nombre, cédula o expediente
  2. Búsqueda en tiemporeal (sin botón "Buscar")
  3. Resultados en tabla: Nombre, Cédula, Expediente, Última Visita, Acciones
  4. Si no hay resultados, se muestra "No se encontraron pacientes"
  5. Click en un paciente muestra su ficha completa

---

#### RF-08 — Editar Paciente

- **Descripción:** El cajero debe poder modificar la información de un paciente existente desde su ficha.
- **Prioridad:** Media
- **Historia de Usuario:** HU-08
- **Criterios de Aceptación:**
  1. El formulario se carga con los datos actuales del paciente
  2. Todos los campos son editables excepto el número de expediente
  3. La cédula no se puede cambiar si ya tiene registros asociados
  4. Al guardar, se muestra "Paciente actualizado"
  5. Los cambios se reflejan en búsquedas posteriores

---

### 1.3 Módulo de Signos Vitales

---

#### RF-09 — Registrar Signos Vitales

- **Descripción:** La enfermera debe poder registrar los signos vitales de un paciente: temperatura corporal, presión arterial (sistolica/diastólica), saturación de oxígeno, frecuencia cardíaca y frecuencia respiratoria.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-09
- **Criterios de Aceptación:**
  1. Formulario con campos numéricos para cada signo vital
  2. Temperatura en °C (rango 30-45)
  3. Presión arterial: sistólica/diastólica en mmHg
  4. Saturación O2 en % (rango 0-100)
  5. Frecuencia cardíaca en lpm (rango 20-250)
  6. Frecuencia respiratoria en rpm (rango 5-60)
  7. Valores fuera de rango muestran advertencia visual
  8. Se asocia automáticamente al paciente y fecha/hora actual

---

#### RF-10 — Visualizar Historial de Signos Vitales

- **Descripción:** La enfermera debe poder ver el historial de signos vitales de un paciente en una tabla cronológica con opción de filtrar por rango de fechas.
- **Prioridad:** Media
- **Historia de Usuario:** HU-10
- **Criterios de Aceptación:**
  1. Tabla con columnas: Fecha, Temperatura, Presión, Saturación O2, FC, FR, Enfermera
  2. Orden cronológico descendente (más reciente primero)
  3. Filtro por rango de fechas (fecha inicio - fecha fin)
  4. Paginación de 15 registros por página
  5. Click en un registro muestra detalle completo

---

#### RF-11 — Editar Signos Vitales

- **Descripción:** La enfermera debe poder corregir signos vitales registrados por error, manteniendo un registro de la edición.
- **Prioridad:** Baja
- **Historia de Usuario:** HU-11
- **Criterios de Aceptación:**
  1. Formulario con los valores actuales precargados
  2. Campo obligatorio "Motivo de corrección"
  3. Se guarda la fecha/hora de la edición y la enfermera que editó
  4. El registro original se mantiene en historial de auditoría
  5. Se muestra "Signos vitales actualizados"

---

### 1.4 Módulo de Farmacia

---

#### RF-12 — Registrar Dosis Dispensada

- **Descripción:** El farmacéutico debe poder registrar cada dosis dispensada a un paciente, indicando medicamento, cantidad, vía de administración y observaciones.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-12
- **Criterios de Aceptación:**
  1. Formulario: paciente (select/búsqueda), medicamento (select), cantidad, vía admin, observaciones
  2. El stock del medicamento se decrementa automáticamente
  3. Si el stock es insuficiente, se muestra advertencia y bloquea el registro
  4. Se asocia fecha/hora y farmacéutico actual
  5. Se muestra "Dosis registrada exitosamente"

---

#### RF-13 — Verificar Interacciones Medicamentosas

- **Descripción:** El sistema debe verificar automáticamente si existen interacciones medicamentosas entre el medicamento a dispensar y los que el paciente ya está tomando, mostrando advertencias si las hay.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-13
- **Criterios de Aceptación:**
  1. Al seleccionar un medicamento, el sistema consulta los medicamentos activos del paciente
  2. Si hay interacción conocida, se muestra modal de advertencia con: medicamentos involucrados, tipo de interacción, nivel de severidad
  3. El farmacéutico puede forzar el registro con justificación
  4. Las interacciones se registran en auditoría
  5. Si no hay interacciones, se permite el registro directo

---

#### RF-14 — Gestionar Inventario

- **Descripción:** El farmacéutico debe poder administrar el inventario de medicamentos: agregar nuevos, actualizar stock, definir stock mínimo y registrar fecha de vencimiento.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-17
- **Criterios de Aceptación:**
  1. Tabla de inventario: Medicamento, Stock Actual, Stock Mínimo, Vencimiento, Estado
  2. Botón "Agregar Medicamento" con formulario (nombre, concentración, forma, stock, mínimo, vencimiento)
  3. Stock mínimo es configurable por medicamento
  4. Medicamentos vencidos se marcan automáticamente como "Vencido"
  5. Opción de editar stock y datos de cada medicamento

---

#### RF-15 — Alertas de Stock Bajo

- **Descripción:** El sistema debe activar alertas automáticas cuando el stock actual de un medicamento cae por debajo del stock mínimo configurado.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-18
- **Criterios de Aceptación:**
  1. Al decrementar stock, el sistema compara con stock mínimo
  2. Si stock < mínimo, se genera alerta automática
  3. La alerta aparece en el panel de notificaciones del farmacéutico
  4. Se envía notificación push al navegador
  5. La alerta incluye: nombre del medicamento, stock actual, stock mínimo

---

#### RF-16 — Responder a Alertas de Stock

- **Descripción:** El farmacéutico debe poder responder a las alertas de stock bajo con acciones: solicitar pedido, transferencia de otra sala, o marcar como resuelta.
- **Prioridad:** Media
- **Historia de Usuario:** HU-19
- **Criterios de Aceptación:**
  1. Panel de alertas activas con lista de medicamentos bajo mínimos
  2. Cada alerta tiene botones: "Solicitar Pedido", "Transferir", "Resolver"
  3. "Solicitar Pedido" registra la solicitud con fecha y cantidad
  4. "Transferir" permite indicar origen y cantidad
  5. "Resolver" marca la alerta como atendida con observaciones
  6. Historial de respuestas accesible

---

### 1.5 Módulo de Diagnóstico Asistido por IA

---

#### RF-17 — Solicitar Diagnóstico IA

- **Descripción:** El médico debe poder ingresar síntomas, signos vitales del paciente y antecedentes para obtener una sugerencia de diagnóstico generada por inteligencia artificial.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-14
- **Criterios de Aceptación:**
  1. Formulario con campos: síntomas (texto libre), signos vitales (select de registros recientes), antecedentes (texto libre)
  2. Botón "Obtener Sugerencia" envía los datos al microservicio de IA
  3. Se muestra spinner de carga mientras la IA procesa
  4. La respuesta llega en máximo 5 segundos
  5. Si hay error de conexión, se muestra "Servicio de IA no disponible"

---

#### RF-18 — Mostrar Diagnósticos Sugeridos

- **Descripción:** La IA debe generar al menos 3 diagnósticos sugeridos, cada uno con nivel de confianza porcentual, descripción breve y recomendaciones.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-14
- **Criterios de Aceptación:**
  1. Se muestran mínimo 3 diagnósticos en tarjetas
  2. Cada tarjeta muestra: nombre del diagnóstico, nivel de confianza (%), descripción breve
  3. Diagnósticos ordenados por nivel de confianza (mayor a menor)
  4. Cada tarjeta tiene botón "Validar" y "Descartar"
  5. Se muestra aviso: "Este es un apoyo diagnóstico. La decisión final es del médico"

---

#### RF-19 — Validar o Descartar Sugerencias IA

- **Descripción:** El médico debe poder revisar cada sugerencia de la IA y tomar una decisión: validar (aceptar como diagnóstico presuntivo) o descartar (rechazar con motivo).
- **Prioridad:** Alta
- **Historia de Usuario:** HU-15
- **Criterios de Aceptación:**
  1. Botón "Validar" cambia estado del diagnóstico a "Validado por médico"
  2. Botón "Descartar" abre modal solicitando motivo del descarte
  3. El motivo de descarte es obligatorio
  4. La decisión se registra con fecha, hora y médico
  5. Los diagnósticos validados aparecen en el historial del paciente

---

#### RF-20 — Aprendizaje del Modelo IA

- **Descripción:** El sistema debe registrar las validaciones y descartes del médico para retroalimentar y mejorar el modelo de diagnóstico de IA.
- **Prioridad:** Baja
- **Historia de Usuario:** HU-15
- **Criterios de Aceptación:**
  1. Cada validación/descarte se almacena con: inputs (síntomas, signos), output de IA, decisión del médico
  2. Se calcula tasa de acierto del modelo (validaciones / total sugerencias)
  3. Métricas accesibles para el administrador
  4. Los datos se usan exclusivamente para mejorar el modelo
  5. Se cumple con política de privacidad de datos

---

### 1.6 Módulo de Notificaciones

---

#### RF-21 — Notificaciones en Tiempo Real

- **Descripción:** El sistema debe enviar notificaciones instantáneas a los usuarios a través de WebSocket cuando ocurran eventos relevantes (alertas de stock, signos vitales críticos, asignación de pacientes).
- **Prioridad:** Alta
- **Historia de Usuario:** HU-16
- **Criterios de Aceptación:**
  1. Conexión WebSocket activa al iniciar sesión
  2. Notificaciones aparecen como toast/snackbar en pantalla
  3. Sonido de alerta para eventos críticos (configurable)
  4. Badge contador de notificaciones no leídas
  5. Click en notificación navega al módulo relevante

---

#### RF-22 — Configurar Preferencias de Notificación

- **Descripción:** Cada usuario debe poder configurar qué tipos de notificaciones recibe y por qué canal (en-app, sonido, email).
- **Prioridad:** Baja
- **Historia de Usuario:** HU-20
- **Criterios de Aceptación:**
  1. Panel de configuración con tipos de notificación (stock, signos vitales, asignación, sistema)
  2. Para cada tipo, opciones de canal: En-app, Sonido, Email
  3. Toggle para activar/desactivar cada combinación
  4. Los cambios se guardan inmediatamente
  5. Configuración persiste entre sesiones

---

### 1.7 Módulo de Administración y Reportes

---

#### RF-23 — Generar Reportes

- **Descripción:** El administrador debe poder generar reportes de atenciones médicas, diagnósticos más frecuentes y productividad por período.
- **Prioridad:** Media
- **Historia de Usuario:** HU-21
- **Criterios de Aceptación:**
  1. Panel de reportes con filtros: rango de fechas, tipo de reporte, área
  2. Tipos de reporte: Atenciones por día, Diagnósticos frecuentes, Productividad por médico
  3. Resultados se muestran en tabla y gráfico (barras o líneas)
  4. Rango de fechas mínimo: 1 día, máximo: 12 meses
  5. Datos se calculan en tiempo real al aplicar filtros

---

#### RF-24 — Exportar Reportes

- **Descripción:** El sistema debe permitir exportar los reportes generados en formato CSV o PDF.
- **Prioridad:** Media
- **Historia de Usuario:** HU-21
- **Criterios de Aceptación:**
  1. Botones "Exportar CSV" y "Exportar PDF" en el panel de reportes
  2. CSV incluye todos los datos de la tabla mostrada
  3. PDF incluye gráfico + tabla + fecha de generación
  4. El archivo se descarga automáticamente
  5. Nombre del archivo: reporte-[tipo]-[fecha-inicio]-[fecha-fin].[ext]

---

#### RF-25 — Auditoría de Accesos

- **Descripción:** El administrador debe poder revisar un registro de auditoría que muestre qué usuario realizó qué acción, en qué fecha/hora, desde qué IP y en qué módulo.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-22
- **Criterios de Aceptación:**
  1. Tabla de auditoría: Usuario, Fecha/Hora, Acción, Módulo, IP, Detalles
  2. Filtros: usuario, rango de fechas, tipo de acción, módulo
  3. Acciones registradas: login, logout, creación, edición, eliminación, exportación
  4. Los registros de auditoría no se pueden editar ni eliminar
  5. Paginación de 50 registros por página
  6. Exportación de auditoría en CSV

---

### 1.8 Módulo de Monitoreo del Sistema

---

#### RF-26 — Monitorear Estado del Sistema

- **Descripción:** El administrador debe poder ver en tiempo real el estado del sistema: uso de CPU, memoria RAM, conexiones activas y tiempo de actividad.
- **Prioridad:** Baja
- **Historia de Usuario:** HU-23
- **Criterios de Aceptación:**
  1. Dashboard con métricas: CPU %, RAM %, Conexiones activas, Uptime
  2. Datos se actualizan cada 10 segundos (auto-refresh)
  3. Gráfico de línea con tendencia de las últimas 24 horas
  4. Indicadores visuales: verde (<70%), amarillo (70-90%), rojo (>90%)
  5. Botón "Actualizar ahora" para refresh manual

---

#### RF-27 — Ejecutar Optimizaciones

- **Descripción:** El administrador debe poder ejecutar acciones de mantenimiento: limpiar caché, reiniciar servicios y optimizar base de datos.
- **Prioridad:** Baja
- **Historia de Usuario:** HU-23
- **Criterios de Aceptación:**
  1. Panel con botones: "Limpiar Caché", "Reiniciar Servicios", "Optimizar BD"
  2. Cada acción requiere confirmación antes de ejecutarse
  3. Se muestra progreso de la operación
  4. Al finalizar, se muestra resultado (éxito/error)
  5. Las acciones se registran en auditoría

---

#### RF-28 — Estado de Pacientes en Tiempo Real

- **Descripción:** El sistema debe mostrar el estado actual de todos los pacientes en sala: ubicación (sala, cama), estado clínico, tiempo de espera y responsable asignado.
- **Prioridad:** Alta
- **Historia de Usuario:** HU-24
- **Criterios de Aceptación:**
  1. Vista tipo tablero (kanban o grid) con pacientes agrupados por sala
  2. Cada tarjeta muestra: paciente, sala, cama, estado (color), tiempo de espera
  3. Estados con colores: Rojo (crítico), Amarillo (estable), Verde (leve)
  4. Filtro por sala y por estado
  5. Datos se actualizan en tiempo real via WebSocket
  6. Click en paciente muestra ficha detallada

---

## 2. Requisitos No Funcionales

### 2.1 Seguridad

---

#### RNF-01 — Hash de Contraseñas

- **Descripción:** Todas las contraseñas deben almacenarse hasheadas con bcrypt using un mínimo de 12 rondas de salt.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Ninguna contraseña se almacena en texto plano
  2. Se utiliza bcrypt con mínimo 12 rondas
  3. El hash se genera antes de insertar en la base de datos
  4. Al comparar, se usa bcrypt.compare() no igualdad directa

---

#### RNF-02 — Autenticación JWT

- **Descripción:** La autenticación se realiza mediante tokens JWT con expiración de 24 horas y refresco automático.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Token JWT firmado con secreto seguro
  2. Expiración de 24 horas
  3. Token incluye: id usuario, email, rol
  4. Cada petición API valida el token en header Authorization
  5. Token expirado retorna 401 Unauthorized

---

#### RNF-03 — Autorización por Roles

- **Descripción:** Cada endpoint de la API debe verificar que el usuario autenticado tenga el rol necesario para acceder.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Middleware de autorización en cada ruta protegida
  2. Roles: admin, cajero, medico, enfermera, farmaceutico
  3. Endpoint sin rol adecuado retorna 403 Forbidden
  4. El rol se extrae del token JWT
  5. Rutas públicas (login) no requieren token

---

#### RNF-04 — HTTPS Obligatorio

- **Descripción:** Todas las comunicaciones en producción deben realizar se sobre HTTPS con certificado válido.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Certificado SSL/TLS válido (no auto-firmado)
  2. Redirección automática HTTP → HTTPS
  3. Headers de seguridad: HSTS, X-Content-Type-Options, X-Frame-Options

---

#### RNF-05 — Registro de Auditoría

- **Descripción:** El sistema debe registrar todas las acciones críticas: login, logout, creación, edición y eliminación de registros.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Tabla de auditoría con: usuario, acción, módulo, fecha/hora, IP, detalles
  2. Se registra automáticamente vía middleware
  3. Los registros no se pueden modificar ni eliminar
  4. Retención mínima de 1 año

---

#### RNF-06 — Protección contra Inyección y XSS

- **Descripción:** El sistema debe estar protegido contra inyección SQL, Cross-Site Scripting (XSS) y otros ataques comunes de web.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Queries parametrizadas (no concatenación de strings en SQL)
  2. Sanitización de inputs del usuario
  3. Content Security Policy (CSP) habilitado
  4. Tokens CSRF en formularios
  5. Headers de seguridad configurados

---

### 2.2 Rendimiento

---

#### RNF-07 — Tiempo de Respuesta API

- **Descripción:** La API debe responder en menos de 200 milisegundos en operaciones CRUD estándar (create, read, update, delete).
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. 95% de las peticiones CRUD responden en < 200ms
  2. Mediciones en condiciones normales de carga
  3. Monitoreo continuo de tiempo de respuesta
  4. Alertas si se supera el umbral de 500ms

---

#### RNF-08 — Tiempo de Respuesta IA

- **Descripción:** El servicio de diagnóstico por IA debe retornar resultados en menos de 5 segundos.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. 90% de las consultas de IA responden en < 5 segundos
  2. Timeout configurado a 10 segundos
  3. Si excede 10 segundos, se muestra "Servicio no disponible, intente de nuevo"
  4. Se registra cada vez que se supera el umbral

---

#### RNF-09 — Concurrencia

- **Descripción:** El sistema debe soportar al menos 50 usuarios concurrentes sin degradación significativa del rendimiento.
- **Prioridad:** Media
- **Criterios de Aceptación:**
  1. Prueba de carga con 50 usuarios simultáneos
  2. Tiempo de respuesta no se duplica con carga completa
  3. Sin errores de conexión agotada
  4. Logs de uso de recursos durante la prueba

---

#### RNF-10 — Paginación

- **Descripción:** Todos los listados que superen 20 registros deben implementar paginación del lado del servidor.
- **Prioridad:** Media
- **Criterios de Aceptación:**
  1. Paginación server-side (no cargar todos los registros)
  2. Tamaño de página configurable (mínimo 10, máximo 100)
  3. Indicador de total de registros y páginas
  4. Botones: Primera, Anterior, Siguiente, Última

---

### 2.3 Disponibilidad

---

#### RNF-11 — Disponibilidad del Sistema

- **Descripción:** El sistema debe mantener una disponibilidad del 99%, equivalente a máximo 8.76 horas de downtime no planificado al año.
- **Prioridad:** Media
- **Criterios de Aceptación:**
  1. Monitoreo de uptime con alertas
  2. Mantenimiento planificado fuera de horario laboral
  3. Logs de cada incidente de indisponibilidad
  4. Tiempo de recuperación objetivo: < 30 minutos

---

#### RNF-12 — Backup Automático

- **Descripción:** La base de datos debe realizarse backup automáticamente cada 6 horas, almacenando los respaldos en ubicación segura.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Backup automático cada 6 horas
  2. Retención de backups por 30 días
  3. Almacenamiento en ubicación separada del servidor principal
  4. Verificación de integridad del backup
  5. Procedimiento documentado de restauración

---

#### RNF-13 — Logs Centralizados

- **Descripción:** Los logs de error del sistema deben centralizarse para facilitar el diagnóstico de fallos.
- **Prioridad:** Media
- **Criterios de Aceptación:**
  1. Logs con formato: timestamp, nivel, módulo, mensaje, stack trace
  2. Niveles: ERROR, WARN, INFO, DEBUG
  3. Retención mínima de 90 días
  4. Accesibles vía interfaz o CLI
  5. Alertas automáticas para errores CRITICAL

---

### 2.4 Usabilidad

---

#### RNF-14 — Interfaz Responsiva

- **Descripción:** La interfaz web debe adaptarse a diferentes tamaños de pantalla: desktop, tablet y móvil.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Diseño responsive con breakpoints: mobile (<768px), tablet (768-1024px), desktop (>1024px)
  2. Sidebar colapsable en mobile
  3. Tablas con scroll horizontal en mobile
  4. Formularios adaptados a pantalla completa en mobile
  5. Prueba en Chrome, Firefox, Safari, Edge

---

#### RNF-15 — Curva de Aprendizaje

- **Descripción:** Un nuevo usuario debe poder realizar las tareas básicas (login, registro de paciente, consulta) después de máximo 30 minutos de uso sin entrenamiento formal.
- **Prioridad:** Media
- **Criterios de Aceptación:**
  1. Navegación intuitiva con sidebar claramente visible
  2. Tooltips en botones principales
  3. Mensajes de ayuda contextual
  4. Prueba de usabilidad con 3 usuarios nuevos

---

#### RNF-16 — Navegación Consistente

- **Descripción:** Todas las pantallas deben mantener una navegación consistente con sidebar fija y breadcrumbs que indiquen la ubicación actual.
- **Prioridad:** Media
- **Criterios de Aceptación:**
  1. Sidebar fija a la izquierda en todas las pantallas
  2. Breadcrumb debajo del header mostrando ruta actual
  3. Botón de regreso en formularios
  4. Logo y nombre del sistema siempre visibles

---

#### RNF-17 — Mensajes de Error Claros

- **Descripción:** Todos los mensajes de error del sistema deben ser comprensibles, en español, e indicar al usuario qué hacer para resolver el problema.
- **Prioridad:** Media
- **Criterios de Aceptación:**
  1. Mensajes en español
  2. Describen qué falló y cómo solucionarlo
  3. Códigos de error internos no expuestos al usuario
  4. Toast/snackbar para errores no críticos
  5. Página de error amigable para errores 404 y 500

---

### 2.5 Escalabilidad

---

#### RNF-18 — Arquitectura de Microservicios

- **Descripción:** El sistema debe implementar arquitectura de microservicios desacoplando frontend, backend API y servicio de IA en servicios independientes.
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. Frontend, backend e IA son servicios separados
  2. Comunicación vía HTTP/REST entre servicios
  3. Cada servicio se puede desplegar independientemente
  4. Docker/Docker Compose para orquestación

---

#### RNF-19 — Base de Datos Normalizada

- **Descripción:** La base de datos debe ser relacional (PostgreSQL) con diseño normalizado hasta la tercera forma normal (3FN).
- **Prioridad:** Alta
- **Criterios de Aceptación:**
  1. PostgreSQL como motor de base de datos
  2. Diseño en 3FN (sin redundancia de datos)
  3. Llaves primarias y foráneas definidas
  4. Índices en campos de búsqueda frecuente
  5. Migraciones versionadas

---

#### RNF-20 — API Versionada

- **Descripción:** La API REST debe estar versionada (v1/) para permitir evolución sin romper clientes existentes.
- **Prioridad:** Baja
- **Criterios de Aceptación:**
  1. Todas las rutas prefijadas con /api/v1/
  2. Documentación de la API (Swagger/OpenAPI)
  3. Endpoints versionados mantienen compatibilidad
  4. Deprecation headers cuando una versión se descontinúa

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
