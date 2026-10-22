<div align="center">
  <img src="../../../Logos/logo_universidad.png" alt="Universidad Privada de Tacna" height="62">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="../../../Logos/logo_escuela_sistemas.jpeg" alt="Escuela Profesional de Ingeniería de Sistemas" height="62">
</div>

<p align="center">
  <strong>Universidad Privada de Tacna</strong><br>
  Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas
</p>

<h1 align="center">INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR</h1>

<p align="center">
  Banco de casos · <strong>Empresa 07</strong> · Educación superior tecnológica privada<br>
  <em>Organización ficticia. Cualquier parecido con una empresa real es coincidencia.</em>
</p>

---

## A. Ficha de la organización

| Campo | Contenido |
|---|---|
| **Razón social** | INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR |
| **Sector** | Educación superior tecnológica privada |
| **Domicilio fiscal** | Tacna |
| **RUC** | 20558XXXXX *(enmascarado; es una organización ficticia)* |
| **Años de operación** | 16 |
| **Personal en planilla** | 88 |
| **Personal adicional** | 112 docentes por horas |
| **Facturación / presupuesto anual** | S/ 19.7 millones |
| **Mercado o población atendida** | 3 240 estudiantes en 7 carreras |
| **Naturaleza** | Empresa privada. |
| **Entidades que la regulan o supervisan** | MINEDU · SUNEDU (para programas conducentes) · ANPD · SUNAT |

**Objetivo declarado para TI en el periodo.** Profesionalizar la administración de los sistemas académicos y asegurar la integridad de las actas.

## B. Estructura y gobierno

| | |
|---|---|
| **Personal de TI** | 3 personas |
| **Responsable de TI** | Coordinador de TI, reporta a Dirección General |
| **Comité de TI o de gobierno digital** | Existe en el papel; no se ha reunido en el último año. |
| **Política de seguridad de la información** | No existe. |
| **Presupuesto de TI del periodo** | S/ 356 000 · 1.81 % de la facturación |

> **Sin marco de gobierno digital obligatorio.** Al ser privada, las exigencias provienen de su regulador sectorial, de la Ley 29733 de protección de datos personales y de sus compromisos contractuales.

## C. Sistemas de información

| Sistema | Descripción | Dónde corre | Desde | ¿Tiene soporte vigente? |
|---|---|---|---|---|
| **Sistema académico** | Producto para institutos, matrícula, notas y certificados | Servidor propio | 2017 | Sí |
| **Aula virtual** | Moodle autoalojado | Servidor propio | 2020 | Administrado por un docente |
| **Cobranzas y tesorería** | Módulo del sistema académico | Mismo servidor | 2017 | Sí |
| **Correo y ofimática** | Suite en nube, licencias educativas | Nube | 2019 | Proveedor |
| **Biblioteca** | Software libre, instalado en 2018 | PC de biblioteca | 2018 | No |

**El problema que la organización reconoce.** El Moodle lo administra un docente de la carrera de computación, sin contrato de TI, sin respaldos programados y con acceso de administrador compartido con dos estudiantes practicantes.

## D. Procesos de negocio

| N.º | Proceso | ¿Qué sistema lo soporta? |
|---|---|---|
| 1 | Admisión y matrícula | Sistema académico |
| 2 | Programación académica y carga docente | Sistema académico |
| 3 | Registro de evaluaciones y actas | Sistema académico |
| 4 | Cobranza de pensiones | Cobranzas y tesorería |
| 5 | Titulación y certificación | Sistema académico |
| 6 | Bienestar y seguimiento estudiantil | Aula virtual |

## E. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado real |
|---|---|---|---|
| Plan estratégico o plan de negocio | Sí | 2023–2027 | Aprobado, pero no se ha revisado desde su aprobación. |
| Plan operativo anual | Sí | 2025 | Se formula cada año para efectos presupuestales. |
| Plan Estratégico de Tecnologías de la Información (PETI) | **No** | — | **Nunca se ha formulado.** |
| Plan de transformación digital | No | — | No se ha formulado. |
| Política de seguridad de la información | No | — | No existe. |
| Plan de continuidad del negocio | No | — | No existe. El BIA de `datos/bia.csv` es un borrador incompleto elaborado por un practicante. |
| Catálogo de servicios de TI | No | — | Sin responsable asignado. |

## F. Situación de TI — hechos verificables para el diagnóstico

Son los hechos que la organización admite y que pueden darse por ciertos. Todo lo demás se pregunta en la entrevista.

| Aspecto | Situación verificada |
|---|---|
| **Contraseñas** | Hay política escrita desde hace cuatro años, pero el sistema principal no la puede exigir técnicamente. |
| **Gestión de cambios** | Solo se documentan los cambios que salieron mal. |
| **Segundo factor de autenticación** | Solo en el correo corporativo. |
| **Contratos con proveedores de TI** | Los contratos existen pero ninguno define niveles de servicio medibles. |
| **Inventario de activos de TI** | No existe. |
| **Capacitación en seguridad** | Se envían correos de concientización que nadie confirma haber leído. |
| **Respaldos** | Existen respaldos programados, pero tres de los sistemas quedaron fuera del alcance sin que nadie lo advirtiera. |
| **Registro de incidentes** | No se registra. Se resuelve y se olvida. |

## G. El incidente del periodo

**Alteración de notas en el sistema académico**

Se detectaron 17 modificaciones de notas fuera del periodo de registro, hechas con la cuenta de un docente que estaba de licencia. El sistema no exige segundo factor y la contraseña era la fecha de nacimiento del docente.

## H. Riesgos que la organización ya conoce y no ha tratado

| N.º | Riesgo conocido | ¿Tratado? |
|---|---|---|
| 1 | Administración de un sistema crítico por personal sin responsabilidad formal | No |
| 2 | Sin autenticación reforzada en el sistema de notas | No |
| 3 | Datos de menores de edad en algunos programas, sin tratamiento diferenciado | No |

## I. Datos entregados

Los siete archivos de `datos/` corresponden al periodo del 1 de enero al 31 de diciembre de 2025. Fueron generados con la semilla de esta empresa. **No coinciden con los de ningún otro equipo**.

| Archivo | Qué contiene | Registros |
|---|---|---|
| `pagos.csv` | Población de pagos del periodo — comprobante, fecha, proveedor, concepto, monto, quién registró y quién aprobó | 6 013 |
| `proveedores.csv` | Maestro de proveedores con su contacto y documento de identidad | 60 |
| `empleados.csv` | Planilla del periodo, con fechas de ingreso y cese | 88 |
| `usuarios_erp.csv` | Usuarios del ERP con su perfil, último acceso y estado | 67 |
| `bia.csv` | Análisis de impacto al negocio por proceso, con RTO, RPO y fecha de la última prueba | 6 |
| `presupuesto_ti.csv` | Presupuesto de TI del periodo por partida, planificado contra ejecutado | 7 |
| `inversiones_cerradas.csv` | Tres inversiones cerradas con su beneficio declarado y si se midió | 3 |

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
