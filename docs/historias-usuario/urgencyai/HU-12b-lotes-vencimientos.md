---
id: HU-12b
titulo: "HU-12b · Controlar lotes, vencimientos y stock"
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:media, sp:5]
milestone: ""
---
## Historia de usuario

> **Como** farmacéutico
> **quiero** que el inventario se lleve por lotes con su fecha de vencimiento y que avise cuando un medicamento esté por agotarse
> **para** no dispensar medicamentos vencidos ni quedarme sin existencias en medio de una urgencia.

**Épica:** EP-03 · Farmacia y apoyo a la decisión clínica
**Prioridad (MoSCoW):** Should. El catálogo ya funciona sin esto, pero la seguridad de la dispensación depende del control de lotes.
**Estimación:** 5 puntos. Recepción de lotes, salida FEFO, umbral configurable, alerta y bloqueo de vencidos.
**Origen:** "RF-14 | Gestionar Inventario" (parte de lotes y stock) y "RF-15 | Alertas de Stock Bajo".

## Criterios de aceptación

```gherkin
Característica: Control de lotes, vencimientos y stock

  Antecedentes:
    Dado que el farmacéutico "Rosa Vega" está autenticada

  Escenario: Recepción de un lote
    Cuando registra el lote "L-2026-118" de "Paracetamol 500 mg Tableta"
    con 200 unidades y vencimiento 30/06/2028
    Entonces el sistema suma 200 unidades al stock del medicamento
    Y deja el lote disponible para dispensación

  Escenario: Dispensación con salida FEFO
    Dado que existen dos lotes disponibles:
      | lote       | vencimiento | unidades |
      | L-2026-118 | 30/06/2028  | 50       |
      | L-2026-071 | 31/01/2027  | 20       |
    Cuando se dispensan 30 unidades
    Entonces el sistema descuenta las 20 unidades del lote "L-2026-071"
    Y las 10 restantes del lote "L-2026-118"

  Escenario: Lote vencido
    Dado el lote "L-2025-004" con vencimiento 31/12/2025
    Cuando el farmacéutico intenta dispensar de ese lote
    Entonces el sistema lo impide
    Y muestra "El lote está vencido. Selecciona otro lote disponible"

  Escenario: Alerta de stock bajo
    Dado "Ibuprofeno 400 mg" con stock mínimo 10 y stock actual 11
    Cuando una dispensación deja el stock en 9
    Entonces el sistema genera una alerta de stock bajo
    Y la muestra en el panel de farmacia
    Y no repite la alerta hasta que el stock vuelva a superar el mínimo

  Escenario: Stock insuficiente
    Dado un stock total de 5 unidades
    Cuando se intenta dispensar 8
    Entonces el sistema rechaza la operación
    Y muestra el stock disponible real

  Escenario: Ajuste por inventario físico
    Dado un stock registrado de 42 unidades y un conteo físico de 40
    Cuando Rosa registra el ajuste con el motivo "Conteo físico mensual"
    Entonces el sistema registra una diferencia de -2
    Y conserva el autor, la fecha y el motivo del ajuste
```

**No funcionales**
- [ ] El stock nunca puede quedar negativo: la validación es atómica.
- [ ] Dos dispensaciones simultáneas del mismo lote no pueden descontar más unidades de las disponibles.
- [ ] La alerta de stock bajo se muestra en menos de 1 segundo tras la dispensación.

## Wireframe

![Mockup HU-12b](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-12b-lotes-vencimientos.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Stock total de lotes no vencidos y stock mínimo configurable.
2. Lotes ordenados por vencimiento: el que vence antes sale primero (FEFO).
3. Un lote vencido no se dispensa aunque conserve unidades.
4. “Recibir lote” y “Ajustar inventario” registran usuario, hora y motivo.
5. Alertas generadas cuando el stock cae por debajo del mínimo.

## Reglas de negocio

- **RN-1:** Todo movimiento de inventario ocurre sobre un lote; no hay stock "suelto".
- **RN-2:** La salida es **FEFO** (*first expired, first out*): se dispensa primero el lote que vence antes.
- **RN-3:** Un lote con fecha de vencimiento anterior a hoy no es dispensable.
- **RN-4:** El stock mínimo es configurable por medicamento; si no se define, vale 10.
- **RN-5:** La alerta de stock bajo se emite al cruzar el umbral hacia abajo y se silencia hasta que el stock lo supere de nuevo.
- **RN-6:** El stock nunca puede ser negativo; la validación es transaccional.
- **RN-7:** Todo ajuste manual exige motivo y queda auditado con autor y fecha.
- **RN-8:** El stock total que se muestra excluye los lotes vencidos.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Parcial | Requiere el catálogo de HU-12a. Aporta valor por sí sola una vez que existe el medicamento. |
| **N**egociable | Sí | La interfaz de recepción de lotes y el formato de la alerta quedan abiertos; FEFO y el bloqueo de vencidos no. |
| **V**aliosa | Sí | Evita dos errores clínicos reales: dispensar vencido y quedarse sin stock. |
| **E**stimable | Sí | Reglas de salida deterministas y una alerta con umbral explícito. |
| **S**mall (pequeña) | Sí | 5 puntos, en el límite: si aparece la trazabilidad por proveedor, se separa. |
| **T**esteable | Sí | El escenario FEFO tiene lotes, fechas y cantidades exactas. |

## Dependencias y notas

- **Depende de:** HU-12a (catálogo de medicamentos).
- **Notas para el equipo:**
  - Esta historia es la segunda mitad del "HU-12" original.
  - La **respuesta** a las alertas de stock (pedido, transferencia, resolución) es RF-16 y **no tiene historia**: queda como pendiente del backlog.
  - El wireframe SVG existente es `docs/wireframes/farmacia.svg`.

## Definición de terminado

- [ ] Los 6 escenarios pasan como pruebas automatizadas
- [ ] Probada la concurrencia de dos dispensaciones simultáneas sobre el mismo lote
- [ ] Interfaz validada contra el wireframe por el PO
