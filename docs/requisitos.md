# Requisitos — UrgencyAI

## 1. Requisitos Funcionales

### 1.1 Módulo de Autenticación y Gestión de Usuarios

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-01 | Inicio de Sesión | El sistema debe permitir a los usuarios autenticarse con email y contraseña. Al ser correctos, redirigir al dashboard correspondiente según su rol. | Alta | HU-01 | 1. El formulario contiene campos de email y contraseña. 2. El sistema valida que ambos campos estén llenos antes de enviar. 3. Si las credenciales son correctas, redirige al dashboard del rol del usuario. 4. Si las credenciales son incorrectas, muestra mensaje "Email o contraseña incorrectos". 5. El mensaje de error se limpia después de 5 segundos. |
| RF-02 | Cierre de Sesión por Inactividad | El sistema debe cerrar la sesión automáticamente tras 30 minutos de inactividad, mostrando un aviso 2 minutos antes. | Media | HU-02 | 1. Se detecta inactividad del usuario (mouse, teclado, scroll). 2. A los 28 minutos se muestra modal: "Tu sesión expirará en 2 minutos". 3. Si el usuario hace clic en "Continuar", se reinicia el contador. 4. Si no responde en 2 minutos, se cierra sesión y redirige al login. 5. El token JWT se invalida en el servidor. |
| RF-03 | Crear Usuario | El administrador debe poder crear usuarios con nombre completo, email, contraseña y rol del sistema. | Alta | HU-03 | 1. Formulario con campos: nombre, email, contraseña, rol (select). 2. Roles: Cajero, Médico, Enfermera, Farmacéutico, Administrador. 3. Contraseña mínimo 8 caracteres. 4. Email debe tener formato válido y no estar registrado. 5. Al guardar: "Usuario creado exitosamente". 6. El nuevo usuario aparece en la lista. |
| RF-04 | Editar Usuario | El administrador debe poder modificar nombre, email y rol de un usuario existente. La contraseña solo se cambia si se ingresa una nueva. | Media | HU-04 | 1. Formulario con datos actuales precargados. 2. Campos editables: nombre, email, rol. 3. Si contraseña está vacía, no se modifica. 4. Nueva contraseña válida con mínimo 8 caracteres. 5. Al guardar: "Usuario actualizado". 6. Cambios se reflejan inmediatamente. |
| RF-05 | Listar y Buscar Usuarios | El administrador debe ver todos los usuarios en tabla con opción de buscar, filtrar por rol y paginar. | Media | HU-05 | 1. Tabla: Nombre, Email, Rol, Estado, Acciones. 2. Búsqueda en tiempo real por nombre o email. 3. Filtro por rol (select). 4. Paginación de 10 por página. 5. Botones Editar y Eliminar/Desactivar por fila. |

### 1.2 Módulo de Gestión de Pacientes

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-06 | Registrar Paciente | El cajero debe registrar un paciente con datos personales, contacto y seguro médico. | Alta | HU-06 | 1. Formulario: Datos Personales, Contacto, Seguro. 2. Cédula obligatoria y numérica. 3. Fecha nacimiento formato DD/MM/YYYY. 4. Género: Masculino, Femenino, Otro (select). 5. Si paciente ya existe (misma cédula), se avisa. 6. Se genera número de expediente automático. 7. "Paciente registrado exitosamente". |
| RF-07 | Buscar Paciente | El cajero debe buscar pacientes por nombre, cédula o expediente y ver resultados en tabla. | Alta | HU-07 | 1. Búsqueda acepta nombre, cédula o expediente. 2. Búsqueda en tiempo real (sin botón). 3. Resultados: Nombre, Cédula, Expediente, Última Visita, Acciones. 4. Sin resultados: "No se encontraron pacientes". 5. Click en paciente muestra ficha completa. |
| RF-08 | Editar Paciente | El cajero debe modificar información de un paciente existente desde su ficha. | Media | HU-08 | 1. Formulario con datos actuales precargados. 2. Todos editables excepto expediente. 3. Cédula no se cambia si tiene registros asociados. 4. "Paciente actualizado". 5. Cambios reflejan en búsquedas posteriores. |

### 1.3 Módulo de Signos Vitales

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-09 | Registrar Signos Vitales | La enfermera debe registrar signos vitales: temperatura, presión arterial, saturación O2, frecuencia cardíaca y respiratoria. | Alta | HU-09 | 1. Formulario con campos numéricos para cada signo. 2. Temperatura en °C (rango 30-45). 3. Presión arterial: sistólica/diastólica en mmHg. 4. Saturación O2 en % (0-100). 5. FC en lpm (20-250). 6. FR en rpm (5-60). 7. Valores fuera de rango muestran advertencia. 8. Se asocia a paciente y fecha/hora actual. |
| RF-10 | Visualizar Historial Signos Vitales | La enfermera debe ver el historial de signos vitales en tabla cronológica con filtro por fechas. | Media | HU-10 | 1. Tabla: Fecha, Temperatura, Presión, Saturación O2, FC, FR, Enfermera. 2. Orden descendente (más reciente primero). 3. Filtro por rango de fechas. 4. Paginación de 15 por página. 5. Click en registro muestra detalle completo. |
| RF-11 | Editar Signos Vitales | La enfermera debe poder corregir signos vitales registrados por error, manteniendo registro de la edición. | Baja | HU-11 | 1. Formulario con valores actuales precargados. 2. Campo obligatorio "Motivo de corrección". 3. Se guarda fecha/hora de edición y enfermera. 4. Registro original en historial de auditoría. 5. "Signos vitales actualizados". |

### 1.4 Módulo de Farmacia

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-12 | Registrar Dosis Dispensada | El farmacéutico debe registrar cada dosis dispensada con medicamento, cantidad, vía de administración y observaciones. | Alta | HU-12 | 1. Formulario: paciente (select/búsqueda), medicamento (select), cantidad, vía admin, observaciones. 2. Stock se decrementa automáticamente. 3. Stock insuficiente bloquea el registro. 4. Se asocia fecha/hora y farmacéutico. 5. "Dosis registrada exitosamente". |
| RF-13 | Verificar Interacciones Medicamentosas | El sistema debe verificar automáticamente interacciones entre el medicamento a dispensar y los que el paciente ya toma. | Alta | HU-13 | 1. Al seleccionar medicamento, consulta medicamentos activos del paciente. 2. Si hay interacción, modal con: medicamentos, tipo, severidad. 3. Farmacéutico puede forzar con justificación. 4. Interacciones registradas en auditoría. 5. Sin interacciones: registro directo. |
| RF-14 | Gestionar Inventario | El farmacéutico debe administrar inventario: agregar, actualizar stock, definir stock mínimo y vencimiento. | Alta | HU-17 | 1. Tabla: Medicamento, Stock Actual, Stock Mínimo, Vencimiento, Estado. 2. Botón "Agregar Medicamento" con formulario completo. 3. Stock mínimo configurable por medicamento. 4. Vencidos se marcan automáticamente. 5. Opción de editar cada medicamento. |
| RF-15 | Alertas de Stock Bajo | El sistema debe activar alertas automáticas cuando stock cae debajo del mínimo configurable. | Alta | HU-18 | 1. Al decrementar stock, compara con mínimo. 2. Si stock < mínimo, genera alerta automática. 3. Alerta en panel de notificaciones. 4. Notificación push al navegador. 5. Alerta incluye: nombre, stock actual, stock mínimo. |
| RF-16 | Responder Alertas de Stock | El farmacéutico debe poder responder alertas con acciones: solicitar pedido, transferencia o resolver. | Media | HU-19 | 1. Panel de alertas activas con lista de medicamentos. 2. Botones: "Solicitar Pedido", "Transferir", "Resolver". 3. "Solicitar Pedido" registra solicitud con fecha y cantidad. 4. "Transferir" indica origen y cantidad. 5. "Resolver" marca alerta como atendida. 6. Historial de respuestas accesible. |

### 1.5 Módulo de Diagnóstico Asistido por IA

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-17 | Solicitar Diagnóstico IA | El médico debe ingresar síntomas, signos vitales y antecedentes para obtener sugerencia de diagnóstico por IA. | Alta | HU-14 | 1. Formulario: síntomas (texto libre), signos vitales (select), antecedentes (texto libre). 2. Botón "Obtener Sugerencia" envía datos al microservicio IA. 3. Spinner de carga mientras procesa. 4. Respuesta en máximo 5 segundos. 5. Error de conexión: "Servicio de IA no disponible". |
| RF-18 | Mostrar Diagnósticos Sugeridos | La IA debe generar al menos 3 diagnósticos con nivel de confianza porcentual, descripción y recomendaciones. | Alta | HU-14 | 1. Mínimo 3 diagnósticos en tarjetas. 2. Cada tarjeta: nombre, confianza (%), descripción breve. 3. Ordenados por confianza (mayor a menor). 4. Botones "Validar" y "Descartar" en cada una. 5. Aviso: "La decisión final es del médico". |
| RF-19 | Validar/Descartar Sugerencias IA | El médico debe poder validar (aceptar) o descartar (con motivo) cada sugerencia de IA. | Alta | HU-15 | 1. "Validar" cambia estado a "Validado por médico". 2. "Descartar" abre modal con motivo obligatorio. 3. Motivo de descarte es obligatorio. 4. Decisión registrada con fecha, hora y médico. 5. Diagnosticos validados en historial del paciente. |
| RF-20 | Aprendizaje del Modelo IA | El sistema debe registrar validaciones/descartes para retroalimentar el modelo de diagnóstico. | Baja | HU-15 | 1. Se almacena: inputs, output de IA, decisión del médico. 2. Tasa de acierto calculada automáticamente. 3. Métricas accesibles para administrador. 4. Datos usados exclusivamente para mejorar modelo. 5. Cumple política de privacidad. |

### 1.6 Módulo de Notificaciones

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-21 | Notificaciones en Tiempo Real | El sistema debe enviar notificaciones instantáneas vía WebSocket (alertas stock, signos críticos, asignación pacientes). | Alta | HU-16 | 1. Conexión WebSocket activa al login. 2. Notificaciones como toast/snackbar. 3. Sonido de alerta para eventos críticos (configurable). 4. Badge contador de no leídas. 5. Click en notificación navega al módulo. |
| RF-22 | Configurar Preferencias Notificación | Cada usuario debe configurar qué notificaciones recibe y por qué canal (en-app, sonido, email). | Baja | HU-20 | 1. Panel con tipos: stock, signos vitales, asignación, sistema. 2. Canales: En-app, Sonido, Email. 3. Toggle activar/desactivar cada combinación. 4. Cambios se guardan inmediatamente. 5. Configuración persiste entre sesiones. |

### 1.7 Módulo de Administración y Reportes

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-23 | Generar Reportes | El administrador debe generar reportes de atenciones, diagnósticos frecuentes y productividad por período. | Media | HU-21 | 1. Filtros: rango fechas, tipo reporte, área. 2. Tipos: Atenciones por día, Diagnósticos frecuentes, Productividad por médico. 3. Resultados en tabla y gráfico (barras/líneas). 4. Rango: mínimo 1 día, máximo 12 meses. 5. Datos en tiempo real al aplicar filtros. |
| RF-24 | Exportar Reportes | El sistema debe permitir exportar reportes en formato CSV o PDF. | Media | HU-21 | 1. Botones "Exportar CSV" y "Exportar PDF". 2. CSV incluye datos de la tabla mostrada. 3. PDF incluye gráfico + tabla + fecha generación. 4. Archivo se descarga automáticamente. 5. Nombre: reporte-[tipo]-[fecha-inicio]-[fecha-fin].[ext]. |
| RF-25 | Auditoría de Accesos | El administrador debe revisar registro de auditoría: usuario, fecha/hora, acción, IP y módulo. | Alta | HU-22 | 1. Tabla: Usuario, Fecha/Hora, Acción, Módulo, IP, Detalles. 2. Filtros: usuario, rango fechas, acción, módulo. 3. Acciones: login, logout, creación, edición, eliminación, exportación. 4. Registros no editables ni eliminables. 5. Paginación 50 por página. 6. Exportación CSV. |

### 1.8 Módulo de Monitoreo del Sistema

| ID | Requisito | Descripción | Prioridad | HU | Criterios de Aceptación |
|----|-----------|-------------|-----------|-----|--------------------------|
| RF-26 | Monitorear Estado del Sistema | El administrador debe ver en tiempo real: CPU, RAM, conexiones activas y uptime. | Baja | HU-23 | 1. Dashboard: CPU %, RAM %, Conexiones activas, Uptime. 2. Auto-refresh cada 10 segundos. 3. Gráfico de línea (últimas 24 horas). 4. Indicadores: verde (<70%), amarillo (70-90%), rojo (>90%). 5. Botón "Actualizar ahora". |
| RF-27 | Ejecutar Optimizaciones | El administrador debe ejecutar mantenimiento: limpiar caché, reiniciar servicios, optimizar BD. | Baja | HU-23 | 1. Botones: "Limpiar Caché", "Reiniciar Servicios", "Optimizar BD". 2. Cada acción requiere confirmación. 3. Se muestra progreso. 4. Resultado final: éxito/error. 5. Acciones registradas en auditoría. |
| RF-28 | Estado de Pacientes en Tiempo Real | El sistema debe mostrar estado de pacientes en sala: ubicación, estado clínico, tiempo de espera, responsable. | Alta | HU-24 | 1. Vista tablero (kanban/grid) agrupada por sala. 2. Tarjeta: paciente, sala, cama, estado (color), tiempo espera. 3. Estados: Rojo (crítico), Amarillo (estable), Verde (leve). 4. Filtro por sala y estado. 5. Datos en tiempo real via WebSocket. 6. Click en paciente muestra ficha. |

---

## 2. Requisitos No Funcionales

### 2.1 Seguridad

| ID | Requisito | Descripción | Prioridad | Criterios de Aceptación |
|----|-----------|-------------|-----------|--------------------------|
| RNF-01 | Hash de Contraseñas | Todas las contraseñas se almacenan hasheadas con bcrypt, mínimo 12 rondas de salt. | Alta | 1. Ninguna contraseña en texto plano. 2. Bcrypt con mínimo 12 rondas. 3. Hash generado antes de insertar en BD. 4. Comparación con bcrypt.compare(). |
| RNF-02 | Autenticación JWT | Autenticación mediante tokens JWT con expiración de 24 horas y refresco automático. | Alta | 1. Token JWT firmado con secreto seguro. 2. Expiración de 24 horas. 3. Token incluye: id, email, rol. 4. Cada petición valida token en header Authorization. 5. Token expirado retorna 401. |
| RNF-03 | Autorización por Roles | Cada endpoint debe verificar que el usuario tenga el rol necesario para acceder. | Alta | 1. Middleware de autorización en cada ruta. 2. Roles: admin, cajero, medico, enfermera, farmaceutico. 3. Sin rol adecuado retorna 403. 4. Rol extraído del token JWT. 5. Rutas públicas no requieren token. |
| RNF-04 | HTTPS Obligatorio | Todas las comunicaciones en producción deben ser sobre HTTPS con certificado válido. | Alta | 1. Certificado SSL/TLS válido. 2. Redirección automática HTTP → HTTPS. 3. Headers: HSTS, X-Content-Type-Options, X-Frame-Options. |
| RNF-05 | Registro de Auditoría | El sistema debe registrar acciones críticas: login, logout, creación, edición y eliminación. | Alta | 1. Tabla: usuario, acción, módulo, fecha/hora, IP, detalles. 2. Registro automático vía middleware. 3. Registros no modificables ni eliminables. 4. Retención mínima 1 año. |
| RNF-06 | Protección Inyección y XSS | El sistema debe estar protegido contra inyección SQL, XSS y ataques comunes de web. | Alta | 1. Queries parametrizadas. 2. Sanitización de inputs. 3. Content Security Policy (CSP). 4. Tokens CSRF en formularios. 5. Headers de seguridad configurados. |

### 2.2 Rendimiento

| ID | Requisito | Descripción | Prioridad | Criterios de Aceptación |
|----|-----------|-------------|-----------|--------------------------|
| RNF-07 | Tiempo Respuesta API | La API debe responder en menos de 200ms en operaciones CRUD estándar. | Alta | 1. 95% de peticiones CRUD en < 200ms. 2. Mediciones en carga normal. 3. Monitoreo continuo. 4. Alertas si se supera 500ms. |
| RNF-08 | Tiempo Respuesta IA | El servicio de diagnóstico IA debe retornar resultados en menos de 5 segundos. | Alta | 1. 90% de consultas IA en < 5 segundos. 2. Timeout a 10 segundos. 3. Excedido 10s: "Servicio no disponible". 4. Registro de cada superación de umbral. |
| RNF-09 | Concurrencia | El sistema debe soportar al menos 50 usuarios concurrentes sin degradación. | Media | 1. Prueba de carga con 50 usuarios simultáneos. 2. Tiempo respuesta no se duplica. 3. Sin errores de conexión agotada. 4. Logs de recursos durante prueba. |
| RNF-10 | Paginación | Los listados que superen 20 registros deben implementar paginación server-side. | Media | 1. Paginación server-side. 2. Tamaño configurable (mín 10, máx 100). 3. Indicador total registros y páginas. 4. Botones: Primera, Anterior, Siguiente, Última. |

### 2.3 Disponibilidad

| ID | Requisito | Descripción | Prioridad | Criterios de Aceptación |
|----|-----------|-------------|-----------|--------------------------|
| RNF-11 | Disponibilidad Sistema | Disponibilidad del 99% (máx 8.76 horas downtime no planificado/año). | Media | 1. Monitoreo de uptime con alertas. 2. Mantenimiento fuera de horario laboral. 3. Logs de cada incidente. 4. Recuperación objetivo: < 30 minutos. |
| RNF-12 | Backup Automático | Backup automático de la base de datos cada 6 horas en ubicación segura. | Alta | 1. Backup cada 6 horas. 2. Retención 30 días. 3. Almacenamiento separado del servidor. 4. Verificación de integridad. 5. Procedimiento documentado de restauración. |
| RNF-13 | Logs Centralizados | Los logs de error deben centralizarse para diagnóstico de fallos. | Media | 1. Formato: timestamp, nivel, módulo, mensaje, stack trace. 2. Niveles: ERROR, WARN, INFO, DEBUG. 3. Retención mínima 90 días. 4. Accesibles vía interfaz o CLI. 5. Alertas para errores CRITICAL. |

### 2.4 Usabilidad

| ID | Requisito | Descripción | Prioridad | Criterios de Aceptación |
|----|-----------|-------------|-----------|--------------------------|
| RNF-14 | Interfaz Responsiva | La interfaz web debe adaptarse a desktop, tablet y móvil. | Alta | 1. Breakpoints: mobile (<768px), tablet (768-1024px), desktop (>1024px). 2. Sidebar colapsable en mobile. 3. Tablas con scroll horizontal en mobile. 4. Formularios a pantalla completa en mobile. 5. Prueba en Chrome, Firefox, Safari, Edge. |
| RNF-15 | Curva de Aprendizaje | Un nuevo usuario debe poder realizar tareas básicas después de máximo 30 minutos sin entrenamiento. | Media | 1. Navegación intuitiva con sidebar visible. 2. Tooltips en botones principales. 3. Mensajes de ayuda contextual. 4. Prueba de usabilidad con 3 usuarios nuevos. |
| RNF-16 | Navegación Consistente | Todas las pantallas deben mantener sidebar fija y breadcrumbs de ubicación. | Media | 1. Sidebar fija a la izquierda. 2. Breadcrumb debajo del header. 3. Botón de regreso en formularios. 4. Logo y nombre siempre visibles. |
| RNF-17 | Mensajes de Error Claros | Los mensajes de error deben ser comprensibles, en español e indicar cómo resolver. | Media | 1. Mensajes en español. 2. Describen qué falló y cómo solucionarlo. 3. Códigos internos no expuestos. 4. Toast/snackbar para errores no críticos. 5. Página amigable para 404 y 500. |

### 2.5 Escalabilidad

| ID | Requisito | Descripción | Prioridad | Criterios de Aceptación |
|----|-----------|-------------|-----------|--------------------------|
| RNF-18 | Arquitectura Microservicios | Desacoplar frontend, backend API y servicio de IA en servicios independientes. | Alta | 1. Frontend, backend e IA separados. 2. Comunicación HTTP/REST. 3. Cada servicio desplegable independientemente. 4. Docker/Docker Compose para orquestación. |
| RNF-19 | Base de Datos Normalizada | PostgreSQL con diseño normalizado hasta 3FN. | Alta | 1. PostgreSQL como motor. 2. Diseño en 3FN. 3. Llaves primarias y foráneas definidas. 4. Índices en campos de búsqueda frecuente. 5. Migraciones versionadas. |
| RNF-20 | API Versionada | API REST versionada (v1/) para evolución sin romper clientes. | Baja | 1. Todas las rutas prefijadas con /api/v1/. 2. Documentación Swagger/OpenAPI. 3. Compatibilidad entre versiones. 4. Deprecation headers al descontinuar. |

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
