# Taller de Laboratorio · Semana 11
## Diagnóstico de Gobierno Digital y Tablero de Línea Base
### SI-886 · Planeamiento Estratégico de TI

**Universidad Privada de Tacna**  
Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas  
**Docente:** Dr. Oscar Juan Jimenez Flores  
**Ciclo Académico:** 2026-II / 2026  

---

### Integrantes del Equipo (Grupo 07)

| Apellidos y Nombres | Código Universitario | Rol / Responsabilidad |
|---|:---:|---|
| **Laos González, Adriana Rafaela** | `2023077474` | Análisis de Servicios y Principio Once-Only |
| **Ramos Loza, Mariela Estefany** | `2023077478` | Diagnóstico de Ejes y Matriz de Línea Base |
| **Calloticona Chambilla, Marymar Danytza** | `2023076791` | Arquitectura de Tableros y Metabase |
| **Choqueña Choque, Mauricio Arian** | `2023076799` | Modelamiento de Datos y Sección 6.1 PETI |

---

## 1. Organización del Caso Asignado: Empresa 07

- **Razón Social:** INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR
- **Sector:** Educación superior tecnológica privada (Tacna, Perú).
- **Años de Operación:** 16 años.
- **Población Atendida:** 3 240 estudiantes matriculados en 7 carreras profesionales técnicas.
- **Personal:** 88 colaboradores en planilla administrativa y 112 docentes por horas.
- **Facturación / Presupuesto Anual:** S/ 19.7 millones de soles anuales.
- **Presupuesto de TI:** S/ 356 000 anuales (1.81% de la facturación institucional).
- **Entidades Reguladoras:** MINEDU, SUNEDU, ANPD (Ministerio de Justicia) y SUNAT.
- **Incidente Crítico Auditado:** Alteración no autorizada de 17 notas en el sistema académico fuera de plazo reglamentario utilizando credenciales de un docente con licencia, evidenciando vulnerabilidad por falta de segundo factor de autenticación (MFA) y contraseñas débiles.

---

## 2. Estructura del Repositorio y Entregables

```text
├── 04_normativa/
│   ├── NO03_matriz_cumplimiento.csv      # Matriz de cumplimiento legal (MINEDU, ANPD, SUNAT)
│   └── MG03_capacidad.csv                # Matriz de capacidad de procesos COBIT 2019
├── 06_gobierno_digital/
│   ├── GD01_catalogo_servicios.csv       # Catálogo de 10 servicios con niveles (0 a 5) y volúmenes
│   ├── GD02_analisis_servicios.py        # Script de promedios simple/ponderado, once-only y brechas
│   ├── GD03_ejes.csv                     # Diagnóstico de los 8 ejes (23 indicadores evaluados)
│   ├── GD04_madurez.py                   # Script de cálculo de madurez, radar polar e indicadores ciegos
│   ├── GD05_carga_tablero.py             # Script de carga a PostgreSQL / SQLite para Metabase
│   └── 6.1_situacion_actual.md           # Redacción oficial de la Sección 6.1 del PETI
├── evidencias/
│   └── S11/
│       ├── capturas/                     # Capturas de alta definición de las 6 tarjetas de Metabase
│       │   ├── 01_nivel_digitalizacion_servicios.png
│       │   ├── 02_nivel_ponderado_kpi.png
│       │   ├── 03_madurez_ejes_barras.png
│       │   ├── 04_cumplimiento_normativo_anillo.png
│       │   ├── 05_capacidad_procesos_agrupadas.png
│       │   └── 06_indicadores_sin_linea_base_tabla.png
│       └── salidas/                      # Logs y transcripciones de ejecución
│           ├── GD02_salida.txt
│           ├── GD04_salida.txt
│           └── GD05_salida.txt
├── graficos/
│   ├── GD_servicios.png                  # Nivel actual vs. meta del catálogo de servicios
│   ├── GD_madurez.png                    # Radar polar de los 8 ejes de gobierno digital
│   └── tablero_metabase_completo.png     # Vista consolidada del Master Dashboard en Metabase
├── anexos/
│   ├── anexo_A_catalogo_servicios.xlsx   # Catálogo detallado en formato Excel
│   ├── anexo_B_diagnostico_ejes.xlsx     # Diagnóstico de los 8 ejes en formato Excel
│   ├── anexo_C_madurez_gobierno_digital.png # Gráfico radar en alta resolución
│   ├── anexo_D_tablero_metabase.pdf      # Compilación de 7 páginas con las visualizaciones
│   ├── anexo_E_recorrido_usuario.pdf     # User Journey Map de los servicios S-01 y S-02
│   └── anexo_F_seccion_6_1.pdf           # Sección 6.1 del PETI en PDF
├── SI886-S11-TALLER-Grupo07.docx         # Documento Word oficial generado sobre plantilla UPT
└── SI886-S11-TALLER-Grupo07.pdf          # Informe oficial de 25 páginas en PDF listo para entrega
```

---

## 3. Síntesis de Resultados Analíticos

### 3.1 Catálogo de Servicios y Digitalización (Paso A)
- **Servicios Auditados:** 10 servicios cubriendo estudiantes, docentes, egresados y personal.
- **Volumen Transaccional Anual:** 231 309 operaciones/año.
- **Nivel Medio Simple Actual:** **1.20 de 5.00** (Servicios mayoritariamente analógicos en ventanilla).
- **Nivel Medio Ponderado Actual:** **2.31 de 5.00** (Impulsado por el tráfico de lectura en Moodle).
- **Prueba del Principio de "Una Sola Vez":** Se solicitaron 26 documentos a los usuarios, de los cuales **17 ya están en poder del instituto**. Esto arroja un **Índice de Redundancia Documental del 65.38%**, obligando a directivas inmediatas de interoperabilidad.
- **Concentración de Brechas (Top 5):** El 92.66% del esfuerzo se focaliza en S-04 Aula Virtual (33.13%), S-03 Pago de Pensiones (24.85%), S-02 Registro de Actas (23.19%), S-09 Biblioteca (6.52%) y S-01 Matrícula (4.97%).

### 3.2 Diagnóstico de los Ocho Ejes y Línea Base (Paso B)
- **Indicadores Evaluados:** 23 indicadores técnicos y de gobernanza con fuentes y evidencias.
- **Nivel de Madurez Institucional:** **1.17 de 5.00** -> **NIVEL 1: INICIAL / AD-HOC (Vulnerable y Reactivo)**.
- **Indicadores Sin Línea Base ("No se mide"):** 4 procesos ciegos identificados, asignando sus proyectos de instrumentación:
  1. *Satisfacción de usuarios:* Proyecto INST-01 (Mesa de ayuda omnicanal con CSAT/NPS).
  2. *Decisiones estratégicas con datos analíticos:* Proyecto INST-02 (Data Warehouse y BI).
  3. *Disponibilidad efectiva de sistemas (Uptime):* Proyecto INST-03 (Monitoreo Zabbix y SLAs 24/7).
  4. *Monitoreo proactivo de ancho de banda:* Proyecto INST-04 (Telemetría de red SNMP y QoS).

### 3.3 Tablero de Línea Base en Metabase (Paso C)
Desplegado sobre PostgreSQL y Metabase con 6 visualizaciones analíticas:
1. *Nivel de digitalización por servicio* (Barras horizontales).
2. *Nivel ponderado por volumen* (Tarjeta KPI grande: 2.31 / 5.00).
3. *Madurez por eje de gobierno digital* (Barras comparativas de los 8 ejes).
4. *Estado de cumplimiento normativo* (Gráfico de anillo: 43% incumplido, 43% parcial, 14% cumple).
5. *Capacidad de procesos COBIT 2019 actual vs. meta* (Barras agrupadas de 8 procesos clave).
6. *Indicadores sin línea base y proyectos* (Tabla ejecutiva con asignación de código PETI).

---

## 4. Instrucciones para Reproducir los Cálculos y Despliegue

### 4.1 Ejecución de Scripts de Análisis
```bash
# 1. Análisis de catálogo de servicios y generación de GD_servicios.png
python 06_gobierno_digital/GD02_analisis_servicios.py

# 2. Diagnóstico de madurez por eje y generación del radar GD_madurez.png
python 06_gobierno_digital/GD04_madurez.py

# 3. Carga automatizada a base de datos analítica hacia Metabase
python 06_gobierno_digital/GD05_carga_tablero.py
```

### 4.2 Despliegue de Docker para PostgreSQL y Metabase
```bash
# Iniciar contenedor PostgreSQL en puerto 5433
docker run -d --name peti_db -e POSTGRES_USER=peti -e POSTGRES_PASSWORD=peti_lab \
  -e POSTGRES_DB=peti -p 127.0.0.1:5433:5432 postgres:16

# Iniciar contenedor Metabase en puerto 3001
docker run -d --name peti_metabase -p 127.0.0.1:3001:3000 \
  --add-host=host.docker.internal:host-gateway \
  -e MB_DB_TYPE=postgres -e MB_DB_DBNAME=peti -e MB_DB_PORT=5433 \
  -e MB_DB_USER=peti -e MB_DB_PASS=peti_lab -e MB_DB_HOST=host.docker.internal \
  metabase/metabase
```
Acceso a Metabase: `http://127.0.0.1:3001` (Credenciales creadas según asistente inicial).

---

## 5. Control de Versiones

- **Commit de Entrega:** `S11: diagnostico de gobierno digital, catalogo de servicios y linea base — seccion 6.1`
- **Etiqueta del PETI:** `v0.11`
- **Etiqueta del Taller:** `taller-11`
- **Repositorio:** `https://github.com/mauchoquenachoque/PETI-SEMANA11-CHOQUENA-LAOS-RAMOSL-CALLOTICONA`
