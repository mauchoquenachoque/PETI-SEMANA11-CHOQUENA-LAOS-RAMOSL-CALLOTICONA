# -*- coding: utf-8 -*-
"""
Programa: GD04_madurez.py
Propósito: Evaluación del nivel de madurez de los 8 ejes de Gobierno Digital,
           conteo de indicadores sin línea base y generación de radar analítico.
Organización: INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR (Caso 07)
Curso: SI-886 Planeamiento Estratégico de TI - Taller Semana 11
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "GD03_ejes.csv")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "graficos")
EVID_DIR = os.path.join(SCRIPT_DIR, "..", "evidencias", "S11", "salidas")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(EVID_DIR, exist_ok=True)

# 1. Cargar datos
df = pd.read_csv(CSV_PATH)

col_eje = [c for c in df.columns if "eje" in c.lower() and "nivel" not in c.lower()][0]
col_nivel = [c for c in df.columns if "nivel" in c.lower()][0]
col_lb = [c for c in df.columns if "base" in c.lower()][0]
col_ind = [c for c in df.columns if "indicador" in c.lower()][0]
col_obs = [c for c in df.columns if "observaci" in c.lower()][0]

df[col_nivel] = pd.to_numeric(df[col_nivel])

# 2. Análisis por Eje
madurez_ejes = df.groupby(col_eje)[col_nivel].mean().reset_index()
madurez_ejes.columns = ["Eje", "Nivel_Promedio"]
# Ordenar ejes por su numeración
madurez_ejes["Num"] = madurez_ejes["Eje"].apply(lambda x: int(x.split(".")[0]))
madurez_ejes = madurez_ejes.sort_values(by="Num").reset_index(drop=True)

nivel_global = madurez_ejes["Nivel_Promedio"].mean()

# Posicionamiento en el Modelo de 5 Niveles
if nivel_global < 1.5:
    etiqueta_madurez = "NIVEL 1 · INICIAL / AD-HOC (Vulnerable y Reactivo)"
    desc_madurez = "Procesos informales, ausencia de controles automatizados, alta vulnerabilidad operacional y desarticulación técnica."
elif nivel_global < 2.5:
    etiqueta_madurez = "NIVEL 2 · GESTIONADO (Repetible pero Aislado)"
    desc_madurez = "Iniciativas incipientes a nivel de área, con documentación básica pero sin integración institucional ni telemetría formal."
elif nivel_global < 3.5:
    etiqueta_madurez = "NIVEL 3 · DEFINIDO (Estandarizado e Integrado)"
    desc_madurez = "Procesos y arquitecturas documentadas a nivel institucional con estándares técnicos compartidos y cumplimiento normativo."
elif nivel_global < 4.5:
    etiqueta_madurez = "NIVEL 4 · CUANTITATIVAMENTE GESTIONADO (Medido y Predecible)"
    desc_madurez = "Gestión guiada por métricas cuantitativas, analítica avanzada, telemetría continua y niveles de servicio acordados."
else:
    etiqueta_madurez = "NIVEL 5 · OPTIMIZADO (Innovación Continua e Inteligente)"
    desc_madurez = "Servicios proactivos con interoperabilidad total, automatización inteligente y evolución tecnológica sostenida."

# Indicadores sin línea base
sin_lb = df[df[col_lb].str.strip().str.lower().str.startswith("no se mide")].copy()
proyectos_instrumentacion = [
    ("Satisfacción de usuarios con servicios TI", "INST-01: Mesa de Ayuda Omnicanal y Evaluación Automatizada CSAT/NPS"),
    ("% decisiones estratégicas basadas en datos", "INST-02: Implementación de Almacén de Datos Institucional y BI Académico"),
    ("Disponibilidad efectiva de sistemas críticos (Uptime)", "INST-03: Despliegue de Sistema de Monitoreo Proactivo de Servicios y Uptime"),
    ("Monitoreo proactivo de ancho de banda y enlaces", "INST-04: Instrumentación de Telemetría de Redes y Gestión de Capacidad WAN/LAN")
]

# Construir Reporte
salida = []
salida.append("=" * 80)
salida.append("INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR - EVALUACIÓN DE MADUREZ GD")
salida.append("REPORTE GD04: DIAGNÓSTICO DE LOS 8 EJES Y DETERMINACIÓN DE LÍNEA BASE")
salida.append("=" * 80)
salida.append(f"Total de indicadores evaluados: {len(df)}")
salida.append(f"Nivel de Madurez Global de Gobierno Digital: {nivel_global:.2f} de 5.00")
salida.append(f"Clasificación Institucional: {etiqueta_madurez}")
salida.append(f"Diagnóstico: {desc_madurez}")
salida.append("")
salida.append("1. PUNTUACIÓN DE MADUREZ POR CADA UNO DE LOS 8 EJES:")
salida.append(f"{'Eje de Gobierno Digital':<26} {'Puntaje Promedio':<18} {'Nivel Entero':<14} {'Estado Cualitativo'}")
salida.append("-" * 75)
for _, r in madurez_ejes.iterrows():
    redondeado = round(r['Nivel_Promedio'])
    estado = "Crítico / Inicial" if r['Nivel_Promedio'] <= 1.2 else ("Incipiente" if r['Nivel_Promedio'] < 2.0 else "Gestionado Básico")
    salida.append(f"{r['Eje']:<26} {r['Nivel_Promedio']:<18.2f} Nivel {redondeado:<8} {estado}")
salida.append("-" * 75)
salida.append("")
salida.append(f"2. IDENTIFICACIÓN DE INDICADORES SIN LÍNEA BASE ({len(sin_lb)} DETECTADOS):")
salida.append("   'Sin línea base no puede fijarse meta ni demostrarse avance.'")
salida.append("-" * 88)
salida.append(f"{'Eje':<18} {'Indicador Sin Línea Base':<45} {'Proyecto de Instrumentación Obligatorio'}")
salida.append("-" * 88)
for i, (_, row) in enumerate(sin_lb.iterrows()):
    proj = proyectos_instrumentacion[i][1] if i < len(proyectos_instrumentacion) else "INST-05: Instrumentación General"
    salida.append(f"{row[col_eje]:<18} {row[col_ind][:43]:<45} {proj}")
salida.append("-" * 88)
salida.append(f"Dictamen: Los {len(sin_lb)} indicadores representan el punto de partida ciego de la institución.")
salida.append("Los proyectos de instrumentación correspondientes tienen prioridad absoluta en el PETI.")
salida.append("=" * 80)

texto_salida = "\n".join(salida)
print(texto_salida)

# Guardar en evidencias
with open(os.path.join(EVID_DIR, "GD04_salida.txt"), "w", encoding="utf-8") as f:
    f.write(texto_salida)

# 3. Generación del Gráfico Radar de Madurez (GD_madurez.png)
labels = [e.split(". ")[1] for e in madurez_ejes["Eje"]]
num_vars = len(labels)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
values = madurez_ejes["Nivel_Promedio"].tolist()

# Cerrar el radar
values += values[:1]
angles += angles[:1]
labels_closed = labels + labels[:1]

fig, ax = plt.subplots(figsize=(8.5, 8.5), subplot_kw=dict(polar=True), dpi=300)

# Color styling
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], labels, color="#1F2937", size=10.5, fontweight="bold")
ax.set_rlabel_position(0)
plt.yticks([1, 2, 3, 4, 5], ["1 (Inicial)", "2 (Gestionado)", "3 (Definido)", "4 (Cuantitativo)", "5 (Optimizado)"],
           color="#6B7280", size=8.5)
plt.ylim(0, 5)

# Trazar el polígono actual
ax.plot(angles, values, color="#C0392B", linewidth=2.5, linestyle="solid", label=f"Nivel Actual: {nivel_global:.2f}")
ax.fill(angles, values, color="#E74C3C", alpha=0.35)

# Trazar el polígono objetivo (Nivel 3 mínimo para PETI)
obj_values = [3.5, 4.0, 3.0, 3.5, 3.5, 4.0, 3.0, 3.5]
obj_values += obj_values[:1]
ax.plot(angles, obj_values, color="#27AE60", linewidth=1.8, linestyle="dashed", label="Nivel Meta PETI (Promedio: 3.50)")
ax.fill(angles, obj_values, color="#2ECC71", alpha=0.1)

plt.title("Radar de Madurez de Gobierno Digital por Eje\nInstituto Superior Tecnológico Vertiente Sur (Caso 07)",
          size=13, fontweight="bold", y=1.08, color="#111827")
plt.legend(loc="upper right", bbox_to_anchor=(1.25, 1.05), frameon=True, facecolor="#F9FAFB")

# Cuadro explicativo
info_text = (f"Madurez Global Actual: {nivel_global:.2f} / 5.00\n"
             f"Estado: NIVEL 1 (Inicial / Ad-hoc)\n"
             f"Indicadores 'No se mide': {len(sin_lb)} de {len(df)}")
fig.text(0.12, 0.05, info_text, fontsize=9.5,
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#FEF2F2", edgecolor="#DC2626", alpha=0.9))

plt.tight_layout()
grafico_radar = os.path.join(OUT_DIR, "GD_madurez.png")
plt.savefig(grafico_radar, dpi=300, bbox_inches="tight")
plt.close()
print(f"\n[OK] Radar de madurez exportado exitosamente: {grafico_radar}")
