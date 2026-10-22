---
id: HU-03
titulo: "HU-03 · Crear usuario del sistema"
tipo: historia
epica: EP-01
etiquetas: [HU, Sprint-1, Gestión-Usuarios, historia-usuario, prioridad:alta, sp:3]
milestone: ""
---
## Historia de usuario

> **Como** administrador del servicio
> **quiero** dar de alta a un miembro del personal asignándole un rol
> **para** que acceda únicamente a las funciones que su cargo permite y quede responsabilidad nominal sobre lo que hace.

**Épica:** EP-01 · Seguridad y control de acceso
**Prioridad (MoSCoW):** Must. Sin alta de usuarios no hay sistema operativo: nadie podría iniciar sesión salvo el administrador inicial.
**Estimación:** 3 puntos. Formulario con seis validaciones, generación de contraseña temporal y registro de auditoría.
**Origen:** "RF-03 | Crear Usuario | El administrador debe poder crear usuarios con nombre completo, email, contraseña y rol del sistema."

## Criterios de aceptación

```gherkin
Característica: Alta de usuarios del sistema

  Antecedentes:
    Dado que el administrador "Carlos Peña" está autenticado

  Escenario: Alta exitosa con contraseña temporal
    Cuando registra a "Lucía Márquez" con email "lucia.marquez@hospital.org" y rol "Enfermera"
    Entonces el sistema crea el usuario en estado activo
    Y muestra una contraseña temporal de 12 caracteres una única vez
    Y exige cambiarla en el primer inicio de sesión
    Y registra el alta en la auditoría con el autor

  Escenario: Email ya registrado
    Dado que existe un usuario con el email "lucia.marquez@hospital.org"
    Cuando el administrador intenta crear otro usuario con ese mismo email en mayúsculas
    Entonces el sistema rechaza la creación
    Y muestra el mensaje "Ya existe un usuario con ese correo electrónico"
    Y conserva los datos ya ingresados en el formulario

  Esquema del escenario: Contraseña que no cumple la política
    Cuando el administrador registra la contraseña <password>
    Entonces el sistema la rechaza
    Y muestra el criterio incumplido en el mensaje
    Ejemplos:
      | password     | criterio incumplido      |
      | "abc12"      | mínimo 8 caracteres      |
      | "abcdefgh"   | al menos una mayúscula   |
      | "ABCDEFGH"   | al menos una minúscula   |
      | "Abcdefgh"   | al menos un dígito       |

  Escenario: Rol no seleccionado
    Cuando el administrador envía el formulario sin elegir rol
    Entonces el sistema no crea el usuario
    Y muestra "Debes seleccionar un rol" junto al campo de rol

  Escenario: Primer inicio de sesión con contraseña temporal
    Dado un usuario recién creado con contraseña temporal
    Cuando inicia sesión por primera vez
    Entonces el sistema exige cambiar la contraseña antes de continuar
    Y no permite acceder a ninguna otra función hasta completar el cambio
```

**No funcionales**
- [ ] La contraseña temporal se genera con al menos 72 bits de entropía.
- [ ] La contraseña nunca se muestra en la auditoría ni en los registros del servidor.
- [ ] El formulario es operable solo con teclado y los errores aparecen junto al campo.

## Wireframe

![Mockup HU-03](https://raw.githubusercontent.com/JhonRamirez22/PROYECTO-FINAL-DISE-O-DE-SOFTWARE-Sala-de-Urgencias-/refs/heads/main/docs/historias-usuario/urgencyai/wireframes/HU-03-crear-usuario.svg)

*Mockup de baja fidelidad. Los números remiten a la leyenda.*

**Leyenda del mockup:**

1. Nombre completo; se usa para identificar al usuario en la auditoría.
2. Correo electrónico; identificador de inicio de sesión, debe ser único.
3. Rol; determina los permisos y es obligatorio.
4. Contraseña temporal generada por el sistema o definida manualmente.
5. La contraseña temporal se muestra una sola vez y no es recuperable.
6. “Crear usuario” valida el formulario completo antes de persistir.

## Reglas de negocio

- **RN-1:** Política de contraseña: mínimo 8 caracteres, al menos una mayúscula, una minúscula y un dígito; no puede ser igual al correo ni figurar entre las 100 contraseñas más comunes.
- **RN-2:** El correo es único sin distinguir mayúsculas de minúsculas.
- **RN-3:** La contraseña temporal es de 12 caracteres, se muestra una sola vez y obliga cambio en el primer ingreso.
- **RN-4:** El rol es obligatorio y debe ser uno de: Administrador, Cajero, Médico, Enfermera, Farmacéutico.
- **RN-5:** Los usuarios no se eliminan, se desactivan (coherente con HU-05).
- **RN-6:** Toda alta queda registrada en auditoría con autor, fecha y rol asignado.
- **RN-7:** Debe existir siempre al menos un usuario Administrador activo.

## Evaluación INVEST

| Criterio | Cumple | Justificación |
|---|---|---|
| **I**ndependiente | Sí | Necesita autenticación para que el administrador entre, pero entrega valor completo por sí sola. |
| **N**egociable | Sí | El formato del alta (formulario, importación CSV) y el canal de entrega de la contraseña quedan abiertos; la política de contraseña no. |
| **V**aliosa | Sí | Habilita que el resto del personal use el sistema con permisos correctos. |
| **E**stimable | Sí | Una entidad, seis validaciones y un evento de auditoría. |
| **S**mall (pequeña) | Sí | 3 puntos: un formulario con reglas claras. |
| **T**esteable | Sí | Cada validación tiene mensaje exacto y resultado binario. |

## Dependencias y notas

- **Depende de:** HU-01 (inicio de sesión del administrador).
- **Notas para el equipo:**
  - El backlog original decía "contraseña mínimo 8 caracteres con complejidad" sin definir complejidad; aquí está definida en RN-1.
  - El wireframe SVG existente es `docs/wireframes/crear-usuario.svg`.
  - Si más adelante se integra correo institucional, el canal de entrega de la contraseña temporal puede cambiar sin tocar los criterios.

## Definición de terminado

- [ ] Los escenarios pasan como pruebas automatizadas, incluido el esquema con sus 4 ejemplos
- [ ] La contraseña temporal no aparece en logs ni en la auditoría
- [ ] Interfaz validada contra el wireframe por el PO
