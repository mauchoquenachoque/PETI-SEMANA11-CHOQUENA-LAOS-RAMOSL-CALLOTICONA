[Semana 11](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Semana 11

## Diagnóstico de gobierno digital y tablero de línea base

**SI-886 - Planeamiento Estratégico de TI** - Sesión 2 en laboratorio - **Taller grupal** · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S11-TALLER-Grupo<N>.pdf` |
| **Modalidad** | **Taller grupal.** Un informe por equipo, con los códigos de todos los integrantes. El repositorio y el PETI son del equipo |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La sección **5. Resultados y evidencias** de la plantilla se llena con la lista de comprobación 3.2 de esta guía, una fila por resultado, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 11» |
| **Cuándo vence** | Según lo programado en el aula virtual |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- Levantar el **catálogo de servicios** de la organización con su nivel de digitalización.
- Evaluar los **ocho ejes** del gobierno digital con evidencia.
- Establecer la **línea base** de cada indicador, o declarar explícitamente que no se mide.
- Determinar el **nivel de madurez de gobierno digital** de la organización.
- Aplicar la prueba del **principio de una sola vez** al catálogo de servicios.
- Construir el **tablero de línea base** en Metabase.
- Redactar la **Sección 6.1** del PETI (Plan Estratégico de Tecnologías de Información).

**Tecnología que aplica el estudiante en este taller**

| Tecnología | Qué hace con ella | Dónde queda la evidencia |
|---|---|---|
| **Docker** (PostgreSQL + Metabase) | Despliega una base de datos y una herramienta de inteligencia de negocios en local | Contenedores activos |
| **pandas** + **SQLAlchemy** | Carga el catálogo, los ejes, la matriz de cumplimiento y la capacidad como tablas en PostgreSQL | Salida de `GD05_carga_tablero.py` |
| **Metabase** | Construye al menos seis visualizaciones sobre esas tablas: el tablero de línea base | Capturas del tablero |
| **pandas** y **matplotlib** | Calcula el nivel ponderado por volumen, la prueba de «una sola vez» y la madurez por eje | `GD_servicios.png`, `GD_madurez.png` |

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **[`RECURSOS-TALLER/`](RECURSOS-TALLER/)** | Documentos del caso de su organización y programas de este taller, listos para copiar. El [README](RECURSOS-TALLER/README.md) de la carpeta explica cada archivo |
| **RSGD 005-2018-PCM/SEGDI**, Anexo I | https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf |
| **D. S. 029-2021-PCM** y **D. S. 085-2023-PCM** | Componentes del gobierno digital y objetivos de la política |
| **Estándares de Interoperabilidad de la PIDE** | https://www.peru.gob.pe/normas/docs/Estandares_Interoperabilidad_PIDE_SEGDI.pdf |
| **Metabase** (Docker) | https://www.metabase.com/ |
| **PostgreSQL** (Docker) | Base del tablero |
| **Python 3.11+** con `pandas`, `matplotlib` | Cálculo de indicadores |
| Secciones Sección 4.1, Sección 4.3 y Sección 5 del PETI | Insumos del diagnóstico |

### 1.3. Seguridad

1. El catálogo de servicios y sus volúmenes son información **Confidencial** de la organización.
2. El tablero se despliega **en local** (`127.0.0.1`) con datos agregados; no se cargan datos personales de usuarios.
3. Los indicadores de seguridad digital revelan debilidades. Se reportan por nivel, sin detalle técnico explotable.
4. Si se observa el recorrido de un usuario real, se obtiene su **consentimiento** y no se registran sus datos personales.

---

## 2. Procedimiento o Metodología

> **Recursos de este taller.** Están en [`RECURSOS-TALLER/`](RECURSOS-TALLER/) y su [README](RECURSOS-TALLER/README.md) explica cada archivo. Su equipo usa la subcarpeta de su organización, `RECURSOS-TALLER/EMPRESA-<NN>-<nombre>/`. Trae `FICHA.md`, `mesa-de-servicio-y-sla.md` y `cuestionario-diagnostico.md`. La mesa de servicio lista los servicios que TI reconoce, sus canales, sus niveles declarados y el registro de atenciones; con eso y con los procesos de la sección D de la ficha se levanta el catálogo del Paso A. El cuestionario es el instrumento con el que la organización mide hoy la percepción de sus servicios: sirve en el Paso B para decidir qué indicadores tienen una línea base utilizable y cuáles no (sección 6.1.5). Los volúmenes anuales que falten se piden en la entrevista simulada con el docente.
>
> **Las tablas de ejemplo de esta guía**, y los datos que traen los programas, están resueltas sobre Distribuidora Andina del Sur S.A.C., el caso de respaldo del curso descrito en [`ANEXO-CASO-SIMULADO.md`](../ANEXO-CASO-SIMULADO.md). Muestran el formato y el nivel de detalle que se espera. Las cifras de su informe salen de su organización, no de estas tablas.

> **Cómo leer los pasos.** Cada paso nombra el archivo que el equipo crea, con su ruta dentro del repositorio del PETI, por ejemplo `06_gobierno_digital/GD01_catalogo_servicios.csv`. La carpeta es la de la sección del plan, dentro de la estructura de carpetas del repositorio; el nombre es el que usan los programas y la lista de comprobación. La tabla o la plantilla que sigue a la ruta es **el contenido de ese archivo**. Ese mismo archivo, versionado en GitHub, es la evidencia que se enlaza en el informe.

### Paso A — Catálogo de servicios y su nivel de digitalización

**Archivo que se crea en el repositorio:** `06_gobierno_digital/GD01_catalogo_servicios.csv`:

| id | Servicio | Usuario destinatario | Volumen anual | **Nivel actual (0–5)** | Canales | Tiempo de atención | Documentos solicitados | **De ellos, ya en poder de la organización** | Sistemas que lo soportan | ¿Trata datos personales? | Nivel objetivo | Justificación del objetivo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-01 | Registro de pedido | Cliente (bodega) | 74 400 | **1** | Teléfono, vendedor, portal (4 %) | 15 min | 0 | 0 | Portal, ERP | Sí | **4** | Es el servicio de mayor volumen; la visión exige 80 % digital |
| S-02 | Consulta de estado de pedido | Cliente | 22 000 | **0** | Teléfono al vendedor | 5 min | 0 | 0 | Ninguno | No | **4** | Elimina 22 000 llamadas anuales |
| S-03 | Solicitud de línea de crédito | Cliente | 320 | **2** | Formulario en papel | 5 días | 4 | **2** (RUC y ficha ya registrados) | ERP | Sí | **3** | Requiere evaluación humana |
| S-04 | Reclamo o devolución | Cliente | 180 | **1** | Teléfono, correo | 48 h | 2 | 1 | Correo | Sí | **4** | Trazabilidad exigida por el diagnóstico |
| S-05 | Descarga de comprobante | Cliente | 74 400 | **2** | Correo bajo pedido | 24 h | 0 | 0 | ERP | Sí | **4** | Autoservicio inmediato |
| S-06 | Solicitud de vacaciones | Trabajador | 130 | **0** | Papel | 3 días | 1 | **1** | Ninguno | Sí | **4** | Interno, esfuerzo bajo |
| S-07 | Consulta de boleta de pago | Trabajador | 768 | **2** | Impresa | Mensual | 0 | 0 | Planilla | Sí, sensibles | **4** | Reduce carga administrativa |

**Programa [`GD02_analisis_servicios.py`](RECURSOS-TALLER/GD02_analisis_servicios.py).** Lee `GD01_catalogo_servicios.csv`, en la misma carpeta. Produce el análisis en pantalla y `graficos/GD_servicios.png`. Se copia a `06_gobierno_digital/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-11/RECURSOS-TALLER/GD02_analisis_servicios.py 06_gobierno_digital/
cd 06_gobierno_digital && python3 GD02_analisis_servicios.py
```

### Paso B — Diagnóstico de los ocho ejes con línea base

**Archivo que se crea en el repositorio:** `06_gobierno_digital/GD03_ejes.csv`:

| Eje | Indicador | **Línea base** | Fuente y fecha del dato | Evidencia | Nivel del eje (1–5) | Observación |
|---|---|---|---|---|---|---|
| 1. Gobernanza | ¿Existe comité de TI o de gobierno digital? | **No** | Entrevista y revisión de actas, a la fecha de corte | Sin actas | 1 | — |
| 1. Gobernanza | ¿Existe plan de TI vigente? | **No** | Documental | — | 1 | Este PETI será el primero |
| 2. Servicios | Nivel medio ponderado de digitalización | **1,2 de 5** | `GD02` | Catálogo | 2 | — |
| 2. Servicios | % de transacciones por canal digital | **4 %** | Registro del portal, a la fecha de corte | Reporte | 1 | — |
| 3. Interoperabilidad | N.º de integraciones activas | **1** (ERP↔WMS por archivo plano) | Sección 5.2.3 | Modelo de arquitectura | 1 | — |
| 3. Interoperabilidad | Documentos solicitados que ya poseemos | **3 de 7** | `GD02` | Catálogo | 2 | — |
| 4. Seguridad digital | ¿Existe SGSI (Sistema de Gestión de Seguridad de la Información)? | **No** | Sección 4.1, Sección 4.3 | Matriz de cumplimiento | 1 | Obligación normativa pendiente |
| 4. Seguridad digital | Incidentes registrados en 12 meses | **3** | Registro | — | 1 | **Cifra anormalmente baja.** No se registran |
| 4. Seguridad digital | % de sistemas con restauración probada | **0 %** | Entrevista; sin prueba de restauración en más de dos años | — | 1 | — |
| 5. Datos | Entidades con dueño designado | **0 de 6** | Sección 5.2.2 | Estructura de información | 1 | — |
| 5. Datos | % de decisiones con dato verificable | **No se mide** | — | — | 1 | **Primer proyecto: empezar a medir** |
| 6. Identidad digital | ¿Identidad única de usuario? | **No** | Inventario de accesos | — | 1 | Cuentas por sistema, sin correspondencia |
| 6. Identidad digital | ¿Segundo factor de autenticación? | **No** | — | — | 1 | — |
| 7. Talento | % de personal capacitado en TI en 12 meses | **8 %** | RR. HH., último ejercicio | Registro de capacitación | 2 | — |
| 7. Talento | Perfil cultural dominante | **Jerarquía (42)** | Sección 2.4 | Diagnóstico CVF | — | Condiciona la implantación |
| 8. Infraestructura | Disponibilidad de servicios críticos | **No se mide** | — | — | 1 | **Primer proyecto: instrumentar** |
| 8. Infraestructura | % de equipos dentro de soporte | **66 %** | Inventario | — | 2 | Servidor del ERP fuera de soporte |

**Programa [`GD04_madurez.py`](RECURSOS-TALLER/GD04_madurez.py).** Lee `GD03_ejes.csv`, en la misma carpeta. Produce el nivel de madurez en pantalla y `graficos/GD_madurez.png`. Se copia a `06_gobierno_digital/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-11/RECURSOS-TALLER/GD04_madurez.py 06_gobierno_digital/
cd 06_gobierno_digital && python3 GD04_madurez.py
```

### Paso C — Tablero de línea base en Metabase

```bash
docker run -d --name peti_db -e POSTGRES_USER=peti -e POSTGRES_PASSWORD=peti_lab \
  -e POSTGRES_DB=peti -p 127.0.0.1:5433:5432 postgres:16

docker run -d --name peti_metabase -p 127.0.0.1:3001:3000 \
  --add-host=host.docker.internal:host-gateway \
  -e MB_DB_TYPE=postgres -e MB_DB_DBNAME=peti -e MB_DB_PORT=5433 \
  -e MB_DB_USER=peti -e MB_DB_PASS=peti_lab -e MB_DB_HOST=host.docker.internal \
  metabase/metabase
```

> El puerto es **5433** en los dos contenedores, porque es el que PostgreSQL publica en la máquina. `--add-host` hace que `host.docker.internal` funcione también en Linux. Metabase tarda uno o dos minutos en arrancar; luego, en **Admin → Databases**, se agrega la misma base `peti` (host `host.docker.internal`, puerto `5433`) como fuente de datos para construir las visualizaciones.

```python
# 06_gobierno_digital/GD05_carga_tablero.py
import pandas as pd
from sqlalchemy import create_engine

eng = create_engine("postgresql://peti:peti_lab@127.0.0.1:5433/peti")
pd.read_csv("GD01_catalogo_servicios.csv").to_sql("servicios", eng, if_exists="replace", index=False)
pd.read_csv("GD03_ejes.csv").to_sql("ejes_gd", eng, if_exists="replace", index=False)
pd.read_csv("../04_normativa/NO03_matriz_cumplimiento.csv").to_sql("cumplimiento", eng, if_exists="replace", index=False)
pd.read_csv("../04_normativa/MG03_capacidad.csv").to_sql("capacidad", eng, if_exists="replace", index=False)
print("Datos cargados. Metabase: http://127.0.0.1:3001")
```

**Tableros mínimos a construir en Metabase.**

| Tablero | Visualización | Pregunta que responde |
|---|---|---|
| Nivel de digitalización por servicio | Barras horizontales | ¿Qué servicios están más atrasados? |
| Nivel ponderado por volumen | Número grande | ¿Qué proporción de las atenciones es realmente digital? |
| Madurez por eje | Radar o barras | ¿Dónde está la mayor brecha de gobierno digital? |
| Estado de cumplimiento normativo | Anillo | ¿Cuántas obligaciones se incumplen? |
| Capacidad de procesos actual vs. objetivo | Barras agrupadas | ¿Qué procesos exigen mayor esfuerzo? |
| **Indicadores sin línea base** | Tabla | ¿Qué necesitamos empezar a medir? |

> **Este tablero es el punto de partida de la sección 10 Supervisión.** Los mismos indicadores, con sus metas de sección 6.2, se monitorearán durante la ejecución del plan.

### Paso D — Redactar la Sección 6.1

```markdown
## 6.1 Situación actual del gobierno digital

### 6.1.1 Marco conceptual y alcance
Los seis componentes del gobierno digital aplicados a la organización, con su
equivalencia si es privada.

### 6.1.2 Catálogo de servicios y su nivel de digitalización
Tabla del catálogo · **nivel medio simple y ponderado por volumen**.

### 6.1.3 Aplicación del principio de una sola vez
Documentos solicitados que la organización ya posee y su proporción.

### 6.1.4 Diagnóstico por eje
Los ocho ejes con indicador, línea base, fuente y nivel.

### 6.1.5 Indicadores sin línea base
Listado y proyectos de instrumentación asociados.
**Sin línea base no puede fijarse meta ni demostrarse avance.**

### 6.1.6 Nivel de madurez del gobierno digital
Nivel obtenido, radar y posicionamiento en el modelo de cinco niveles.

### 6.1.7 Síntesis · las brechas de mayor impacto
Servicios de mayor brecha ponderada por volumen y ejes de menor nivel.
**Esta síntesis es el insumo directo de los objetivos (Sección 6.2).**
```

### Paso E — Validar y corregir

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Recorrer dos servicios de principio a fin y comprobar que el nivel declarado es el real.
2. Verificar que cada eje evaluado trae la evidencia que sostiene su puntaje.
3. Comprobar que el principio de «una sola vez» se evaluó sobre documentos concretos.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso F — Registrar la evidencia y cerrar

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S11: diagnostico de gobierno digital, catalogo de servicios y linea base — seccion 6.1"
git tag -a v0.11 -m "PETI v0.11 — situacion actual del gobierno digital"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Programas y archivos CSV del taller | La carpeta de la sección del PETI que el taller indica (esta semana, `06_gobierno_digital/`), en la rama del taller fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | La misma carpeta de la sección, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `evidencias/S11/` | URL del archivo |
> | Salida de comandos | `evidencias/S11/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-11` sobre el commit entregado:
>
> ```bash
> git tag -a taller-11 -m "Taller 11 · SI886"
> git push origin taller-11
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-11`
>
> Esta etiqueta convive con la de versión del PETI que crea el último paso del procedimiento (`v0.11`): `taller-11` marca el commit que se entrega a calificar y `v0.11` marca el estado del documento. Pueden apuntar al mismo commit.
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **El catálogo con niveles** | Cada servicio con su nivel comprobado, no declarado | Catálogo de servicios |
| **Los ocho ejes con evidencia** | Cada puntaje con la prueba que lo sostiene | Tablero de línea base |
| **La línea base del plan** | Las cifras de partida contra las que se medirá el avance | `GD03_ejes.csv` y sección 6.1.4 |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | Catálogo con **≥ 7 servicios**, cada uno con volumen anual y nivel de digitalización | `GD01_catalogo_servicios.csv` |
| 2 | **Nivel medio ponderado por volumen** calculado y contrastado con el promedio simple | Salida de `GD02_analisis_servicios.py` |
| 3 | Prueba del **principio de una sola vez**. Documentos redundantes contados | Salida del script |
| 4 | Brecha por servicio ponderada por volumen, con los 5 de mayor impacto | Salida del script |
| 5 | Gráfico del catálogo con nivel actual y objetivo | `GD_servicios.png` |
| 6 | Los **ocho ejes** evaluados, con al menos dos indicadores cada uno | `GD03_ejes.csv` |
| 7 | **Línea base declarada** en cada indicador, o «no se mide» explícito | Misma tabla |
| 8 | **Indicadores sin línea base identificados y contados**, con su proyecto de instrumentación | Salida de `GD04_madurez.py` |
| 9 | Nivel de madurez de gobierno digital calculado y posicionado en el modelo | Salida del script |
| 10 | Radar de madurez por eje | `GD_madurez.png` |
| 11 | Tablero en Metabase con **al menos 6 visualizaciones** | Capturas |
| 12 | Sección 6.1 redactada, con la síntesis de brechas de mayor impacto | `6.1_situacion_actual.md` |
| 13 | Etiqueta `v0.11` en Git | `git tag` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **El catálogo con niveles** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **Los ocho ejes con evidencia** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La línea base del plan** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

## 4. Conclusiones

1. El nivel de digitalización ponderado por volumen es el indicador que importa. El promedio simple sobrevalora el avance cuando los servicios de mayor volumen son los menos digitalizados, que es el caso más frecuente.
2. Un indicador sin línea base no puede sostener una meta ni demostrar avance; el primer proyecto asociado a esos indicadores no es mejorarlos sino empezar a medirlos.
3. Gobierno digital no es cantidad de sistemas sino capacidad del usuario de completar el servicio sin cambiar de canal; medir sistemas en lugar de servicios produce un diagnóstico que no refleja la experiencia real.

## 5. Referencias Bibliográficas

- Decreto Legislativo 1412, Ley de Gobierno Digital. https://www.gob.pe/institucion/pcm/colecciones/147-normativa-sobre-gobierno-digital
- Decreto Supremo 029-2021-PCM, Reglamento de la Ley de Gobierno Digital. https://www.gob.pe/13326-reglamento-de-la-ley-de-gobierno-digital
- Decreto Supremo 085-2023-PCM, Política Nacional de Transformación Digital al 2030. https://busquedas.elperuano.pe/dispositivo/NL/2200457-5
- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI, Anexo I — Lineamientos del PGD (Plan de Gobierno Digital). https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- Estándares de Interoperabilidad de la PIDE. https://www.peru.gob.pe/normas/docs/Estandares_Interoperabilidad_PIDE_SEGDI.pdf
- Presidencia del Consejo de Ministros. *Transformación digital en el Perú*. https://www.gob.pe/transformaciondigital
- OCDE. *Digital Government Policy Framework*. https://www.oecd.org/governance/digital-government/
- Rodríguez Bermúdez, J. R. (2015). *Usos estratégicos de las TIC*. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57677
- Metabase. *Metabase Documentation*. https://www.metabase.com/docs/latest/

## 6. Anexos

- `anexo_A_catalogo_servicios.xlsx`
- `anexo_B_diagnostico_ejes.xlsx`
- `anexo_C_madurez_gobierno_digital.png`
- `anexo_D_tablero_metabase.pdf` — capturas de las visualizaciones
- `anexo_E_recorrido_usuario.pdf` — el de la dinámica de aula
- `anexo_F_seccion_6_1.pdf`

---

---

[Semana 11](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
