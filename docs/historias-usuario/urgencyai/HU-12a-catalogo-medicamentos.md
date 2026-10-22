---
id: HU-12a
titulo: "HU-12a · Gestionar catálogo de medicamentos"
tipo: historia
epica: EP-03
etiquetas: [HU, Sprint-2, Farmacología, historia-usuario, prioridad:alta, sp:3]
milestone: ""
---
## Historia de usuario

> **Como** farmacéutico
> **quiero** mantener el catálogo de medicamentos que maneja el servicio
> **para** que todo el personal prescriba y dispense sobre la misma lista validada, sin nombres duplicados ni presentaciones ambiguas.

**Épica:** EP-03 · Farmacia y apoyo a la decisión clínica
**Prioridad (MoSCoW):** Must. Sin catálogo no se puede dispensar, ni verificar interacciones, ni llevar inventario.
**Estimación:** 3 puntos. CRUD con regla de unicidad, desactivación lógica y búsqueda.
**Origen:** "RF-14 | Gestionar Inventario | El farmacéutico debe poder administrar el inventario de medicamentos con nombre, principio activo, concentración, stock y categoría." (parte de catálogo)

## Criterios de aceptación

```gherkin
Característica: Catálogo de medicamentos

  Antecedentes:
    Dado que el farmacéutico "Rosa Vega" está autenticada

  Escenario: Alta de un medicamento
    Cuando registra "Paracetamol", principio activo "Acetaminofén",
    concentración "500 mg", forma "Tableta" y categoría "Analgésico"
    Entonces el sistema lo crea en estado activo
    Y lo deja disponible para dispensación
    Y no permite editar después su nombre ni su concentración

  Escenario: Medicamento duplicado
    Dado que existe "Paracetamol 500 mg Tableta"
    Cuando Rosa intenta crear "paracetamol 500 mg tableta"
    Entonces el sistema rechaza el alta
    Y muestra "Ya existe un medicamento con ese nombre, concentración y forma"

  Escenario: Búsqueda por principio activo
    Dado que existe "Paracetamol" con principio activo "Acetaminofén"
    Cuando Rosa busca "acetaminofen"
    Entonces el sistema devuelve "Paracetamol 500 mg Tableta"
    Y la búsqueda ignora mayúsculas y tildes

  Escenario: Desactivación de un medicamento con stock
    Dado un medicamento activo con stock 120 unidades
    Cuando Rosa intenta desactivarlo
    Entonces el sistema lo impide
    Y muestra "No se puede desactivar un medicamento con stock disponible"

  Escenario: Desactivación de un medicamento sin stock
    Dado un medicamento activo con stock 0
    Cuando Rosa lo desactiva indicando el motivo "Descontinuado por el proveedor"
    Entonces el sistema lo marca como inactivo
    Y deja de aparecer en las búsquedas de dispensación
    Y conserva su historial
```

**No funcionales**
- [ ] La búsqueda devuelve resultados en menos de 200 ms con 2000 medicamentos (RNF-07).
- [ ] El listado pagina del lado del servidor a partir de 20 registros (RNF-10).
- [ ] Los medicamentos inactivos no aparecen en el buscador de dispensación, pero sí en el histórico.

## Wireframe

![Mockup HU-12a](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-12a-catalogo-medicamentos.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Alta de un medicamento nuevo en el catálogo.
2. Búsqueda por nombre o principio activo.
3. Cada fila muestra stock y estado; los medicamentos inactivos no se dispensan.
4. Nombre y concentración se bloquean después del alta.
5. “Desactivar” retira el medicamento del catálogo sin borrar el historial.

## Reglas de negocio

- **RN-1:** La identidad del medicamento es la combinación **nombre + concentración + forma farmacéutica**, sin distinguir mayúsculas ni tildes.
- **RN-2:** Nombre y concentración son inmutables tras el alta; un error se corrige desactivando y creando uno nuevo.
- **RN-3:** No se elimina ningún medicamento: se desactiva con motivo obligatorio.
- **RN-4:** No se puede desactivar un medicamento con stock mayor que cero.
- **RN-5:** Los medicamentos inactivos no se ofrecen al dispensar, pero permanecen en el histórico.
- **RN-6:** La categoría pertenece a un catálogo cerrado (Analgésico, Antibiótico, Antiinflamatorio, Antihipertensivo, Otro).

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Sí | No depende de ninguna otra historia; aporta valor por sí sola al normalizar el catálogo. |
| **N**egociable | Sí | El diseño de la tabla y el formulario quedan abiertos; las reglas de unicidad e inmutabilidad no. |
| **V**aliosa | Sí | Evita duplicados y presentaciones ambiguas, que son la causa habitual de errores de dispensación. |
| **E**stimable | Sí | Una entidad, una regla de unicidad y un borrado lógico. |
| **S**mall (pequeña) | Sí | 3 puntos. La parte de lotes y stock se separó en HU-12b. |
| **T**esteable | Sí | Mensajes exactos y estados verificables. |

## Dependencias y notas

- **Depende de:** nada.
- **Notas para el equipo:**
  - Esta historia es la mitad de lo que el backlog original llamaba "HU-12 Gestionar Medicamentos" (que mezclaba catálogo, lotes, stock y búsqueda en un solo ítem).
  - El inventario y los vencimientos van en **HU-12b**.
  - El wireframe SVG existente es `docs/wireframes/farmacia.svg` (el original apuntaba a `gestionar-medicamentos.svg`, inexistente).

## Definición de terminado

- [ ] Los 5 escenarios pasan como pruebas automatizadas
- [ ] La normalización de tildes y mayúsculas está probada
- [ ] Interfaz validada contra el wireframe por el PO
