# Diseño Thinking — UrgencyAI

## 1. Empatizar

### 1.1 Personas

#### Dr. Carlos Méndez — Médico de Urgencias
- **Edad:** 38 años
- **Experiencia:** 12 años en urgencias
- **Frustraciones:** Diagnósticos apresurados por falta de tiempo, pérdida de historial clínico, hardcopy de recetas que se pierden, exceso de papeleo que le quita tiempo con pacientes
- **Necesidades:** Herramienta que le ayude a diagnosticar más rápido, acceso al historial del paciente en segundos, alertas de interacciones medicamentosas
- **Cotidianidad:** Atiende 30-40 pacientes por turno, trabaja en 12-hour shifts, a veces sin break

#### Lic. María Torres — Cajera / Admisión
- **Edad:** 28 años
- **Experiencia:** 3 años en admisión hospitalaria
- **Frustraciones:** Colas enormes para registrar pacientes, errores al escribir datos a mano, no saber si el paciente ya tiene historial previo
- **Necesidades:** Registro rápido, búsqueda de pacientes existentes, interfaz simple que no requiera entrenamiento extenso
- **Cotidianidad:** Registra 60-80 pacientes por turno, maneja fila constante

#### Enf. Laura García — Enfermera de Piso
- **Edad:** 32 años
- **Experiencia:** 8 años en enfermería
- **Frustraciones:** Anota signos vitales en papel que luego tiene que copiar a la computadora, no recibe alertas cuando un paciente empeora, pierde tiempo buscando informes
- **Necesidades:** Registro rápido de signos vitales, notificaciones automáticas de pacientes críticos, dashboard de estado de salas
- **Cotidianidad:** Monitorea 6-8 pacientes simultáneamente, rotación cada 8 horas

#### Farm. Andrés Rojas — Farmacéutico
- **Edad:** 35 años
- **Experiencia:** 6 años en farmacia hospitalaria
- **Frustraciones:** No sabe cuándo el stock está bajo hasta que se agota, recetas manuscritas difíciles de leer, interacciones medicamentosas no detectadas
- **Necesidades:** Alertas de stock, digitalización de recetas, verificación automática de interacciones
- **Cotidianidad:** Dispensa 100+ medicamentos por turno, revisa inventario semanalmente

#### Admin. Roberto Sánchez — Administrador
- **Edad:** 45 años
- **Experiencia:** 15 años en gestión hospitalaria
- **Frustraciones:** No tiene datos en tiempo real para tomar decisiones, reportes que tardan días en generarse, no puede auditar quién accedió a qué
-   **Necesidades:** Dashboards con métricas, reportes automáticos, auditoría de accesos, gestión de usuarios
- **Cotidianidad:** Supervisa 3 áreas, revisa reportes mensuales, gestiona turnos de 20+ personas

---

### 1.2 Pain Points por Rol

| Rol | Pain Points |
|-----|-------------|
| **Cajero** | Lento proceso de registro, búsqueda manual de pacientes, formularios repetitivos |
| **Médico** | Sin apoyo para diagnóstico, historial clínico en papel, recetas manuscritas |
| **Enfermera** | Registro manual de signos vitales, sin alertas de pacientes críticos, comunicación tardía |
| **Farmacéutico** | Sin control de stock, interacciones no detectadas, recetas ilegibles |
| **Administrador** | Sin métricas en tiempo real, auditoría inexistente, reportes manuales |

---

### 1.3 Contexto del Problema

Las salas de urgencias enfrentan una sobrecarga constante que genera:

- **Errores humanos** — en diagnóstico, prescripción y registro de datos
- **Demoras innecesarias** — por procesos manuales y comunicación fragmentada
- **Pérdida de información** — historiales en papel, recetas extraviadas
- **Falta de visibilidad** — el administrador no sabe qué está pasando en tiempo real
- **Riesgos para pacientes** — interacciones medicamentosas no detectadas, signos vitales no monitoreados

---

## 2. Definir

### 2.1 Pregunta Principal de Diseño

> **¿Cómo podemos reducir el tiempo de atención y los errores médicos en salas de urgencias, integrando inteligencia artificial como herramienta de apoyo al profesional de salud?**

### 2.2 Usuarios Objetivo

- Personal médico (médicos, enfermeras, farmacéuticos) que necesita herramientas de apoyo rápido
- Personal administrativo (cajeros, administradores) que necesita gestión eficiente
- Pacientes que se benefician de una atención más rápida y segura

### 2.3 Alcance del Sistema

| Componente | Descripción |
|------------|-------------|
| **Frontend** | Interfaz web responsiva para los 5 roles |
| **Backend** | API RESTful con autenticación JWT por rol |
| **Servicio de IA** | Microservicio Python para diagnóstico asistido |
| **Base de datos** | PostgreSQL para persistencia de datos |
| **Tiempo real** | WebSocket para alertas y notificaciones |

### 2.4 Hipótesis

- Si los médicos reciben sugerencias de diagnóstico basadas en síntomas y signos vitales, entonces el tiempo de diagnóstico se reduce en un 40%
- Si el sistema alerta automáticamente sobre stock bajo, entonces se evitan desabastecimientos críticos
- Si las enfermeras registran signos vitales digitalmente, entonces se elimina el retrabajo de transcripción

---

## 3. Idear

### 3.1 Soluciones Propuestas

#### Módulo de Diagnóstico Asistido por IA
- El médico ingresa síntomas, signos vitales y antecedentes
- La IA genera 3 diagnósticos sugeridos con nivel de confianza
- El médico valida o descarta las sugerencias
- El sistema aprende de las validaciones para mejorar

#### Sistema de Triage Inteligente
- Clasificación automática de pacientes por severidad (rojo/amarillo/verde)
- Asignación de prioridad basada en signos vitales
- Reasignación automática si un paciente empeora

#### Control de Inventario con Alertas
- Registro de medicamentos con stock mínimo configurable
- Alertas automáticas por email/push cuando el stock baja
- Historial de movimientos (entradas, salidas, vencimientos)

#### Dashboard de Monitoreo en Tiempo Real
- Vista del administrador con métricas en vivo
- Estado de salas y camas disponibles
- Reportes automáticos de productividad

### 3.2 Justificación de la IA

| Función | Beneficio |
|---------|-----------|
| Diagnóstico sugerido | Reduce carga cognitiva del médico, segunda opinión instantánea |
| Detección de interacciones | Evita errores de prescripción, mejora seguridad del paciente |
| Clasificación de triage | Estandariza la priorización, reduce subjetividad |

### 3.3 Valor Diferenciador

A diferencia de sistemas de gestión tradicionales, UrgencyAI integra IA como **herramienta de apoyo** (no reemplazo) al criterio médico, manteniendo siempre al profesional como decisor final. Esto garantiza:

- Seguridad: el médico siempre valida
- Transparencia: el sistema explica por qué sugiere cada diagnóstico
- Mejora continua: cada validación alimenta el modelo
