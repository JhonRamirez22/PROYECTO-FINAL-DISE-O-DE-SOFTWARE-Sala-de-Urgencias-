---
id: HU-15
titulo: 'HU-15 "Solicitar Diagnóstico IA"'
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, IA-Diagnóstico, historia-usuario, prioridad:media, sp:8]
milestone: ""
---

## Historia de Usuario

**Como** médico de urgencias
**Quiero** obtener una lista breve de diagnósticos diferenciales a partir de los síntomas y signos vitales del paciente
**Para** contrastarla con mi criterio antes de decidir, sobre todo en cuadros que no me resultan evidentes

**Criterios de Aceptación:**
- Entrada: síntomas descritos por el médico y signos vitales de la atención, con contexto anonimizado
- No se envían nombre, cédula, teléfono ni dirección al proveedor del modelo
- La respuesta válida contiene entre 3 y 5 diagnósticos, cada uno con nombre, confianza y recomendación
- El tiempo máximo de espera es de 5 segundos
- Una respuesta que no cumple el contrato se descarta completa y nunca se muestra parcialmente
- La sugerencia no se guarda como diagnóstico del paciente, solo como sugerencia asociada a la atención
- Se exige al menos una toma de signos vitales y síntomas descritos para solicitar
- Cada llamada se audita con proveedor, modelo, versión y latencia, sin registrar el contenido clínico

---

## Análisis INVEST

| Criterio | Cumple | Justificación |
|----------|:------:|---------------|
| **Independent** | Sí | Requiere signos vitales (HU-09) y un proveedor externo |
| **Negotiable** | Sí | El proveedor y el modelo son intercambiables |
| **Valuable** | Sí | Aporta valor diferencial, aunque el servicio funciona sin ella |
| **Estimable** | Parcial | El contrato de respuesta está definido; la latencia del proveedor no |
| **Small** | Sí | 8 puntos: integración, contrato, anonimización y trazabilidad |
| **Testable** | Sí | Los escenarios cubren éxito, fallo y contrato inválido |

**Score INVEST:** 5/6
**Riesgo principal:** Dependencia de un proveedor externo en disponibilidad y latencia.
**Sugerencia:** Implementar primero contra un proveedor simulado y dejar una bandera para desactivar la función.

---

## Wireframe Asociado

![Wireframe HU-15](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-15-diagnostico-ia.svg)

[Ver wireframe en tamaño completo](https://github.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/blob/main/docs/historias-usuario/urgencyai/wireframes/HU-15-diagnostico-ia.svg)

**Leyenda del mockup:**

1. Síntomas reportados por el médico; entrada principal de la sugerencia.
2. Resumen exacto de los datos clínicos que se envían al modelo.
3. "Solicitar diagnóstico asistido" envía la solicitud y espera la respuesta.
4. Aviso permanente de que la salida no constituye diagnóstico.
5. Entre 3 y 5 diagnósticos con nivel de confianza y recomendación.
