# -*- coding: utf-8 -*-
"""
Programa: GD02_analisis_servicios.py
Propósito: Análisis del catálogo de servicios, niveles de digitalización,
           principio de una sola vez y brechas ponderadas de TI.
Organización: INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR (Caso 07)
Curso: SI-886 Planeamiento Estratégico de TI - Taller Semana 11
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Rutas de entrada y salida
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "GD01_catalogo_servicios.csv")
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "graficos")
EVID_DIR = os.path.join(SCRIPT_DIR, "..", "evidencias", "S11", "salidas")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(EVID_DIR, exist_ok=True)

# 1. Carga de datos
df = pd.read_csv(CSV_PATH)

# Asegurar nombres de columnas
col_actual = [c for c in df.columns if "actual" in c.lower()][0]
col_obj = [c for c in df.columns if "objetivo" in c.lower() and "just" not in c.lower()][0]
col_vol = [c for c in df.columns if "volumen" in c.lower()][0]
col_docs_tot = [c for c in df.columns if "documentos solicitados" in c.lower()][0]
col_docs_org = [c for c in df.columns if "poder de la" in c.lower()][0]

df[col_actual] = pd.to_numeric(df[col_actual])
df[col_obj] = pd.to_numeric(df[col_obj])
df[col_vol] = pd.to_numeric(df[col_vol])
df[col_docs_tot] = pd.to_numeric(df[col_docs_tot])
df[col_docs_org] = pd.to_numeric(df[col_docs_org])

# 2. Cálculos Estadísticos
total_servicios = len(df)
volumen_total = df[col_vol].sum()
promedio_simple = df[col_actual].mean()
promedio_ponderado = (df[col_actual] * df[col_vol]).sum() / volumen_total

promedio_objetivo_simple = df[col_obj].mean()
promedio_objetivo_ponderado = (df[col_obj] * df[col_vol]).sum() / volumen_total

# Principio de una sola vez
total_docs_pedidos = df[col_docs_tot].sum()
total_docs_redundantes = df[col_docs_org].sum()
pct_redundancia = (total_docs_redundantes / total_docs_pedidos) * 100 if total_docs_pedidos > 0 else 0

# Brechas por servicio
df["brecha_unitaria"] = df[col_obj] - df[col_actual]
df["brecha_ponderada"] = df["brecha_unitaria"] * df[col_vol]
df["pct_brecha_total"] = (df["brecha_ponderada"] / df["brecha_ponderada"].sum()) * 100

top5_brechas = df.sort_values(by="brecha_ponderada", ascending=False).head(5)

# Formateo de salida en consola y archivo de evidencia
salida = []
salida.append("=" * 80)
salida.append("INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR - AUDITORÍA DE GOBIERNO DIGITAL")
salida.append("REPORTE GD02: ANÁLISIS DEL CATÁLOGO DE SERVICIOS Y NIVELES DE DIGITALIZACIÓN")
salida.append("=" * 80)
salida.append(f"Total de servicios catalogados: {total_servicios}")
salida.append(f"Volumen transaccional anual auditado: {volumen_total:,.0f} atenciones/año")
salida.append("")
salida.append("1. DIAGNÓSTICO DE DIGITALIZACIÓN (NIVEL 0 A 5):")
salida.append(f"   • Nivel medio simple actual:       {promedio_simple:.2f} de 5.00")
salida.append(f"   • Nivel medio ponderado actual:    {promedio_ponderado:.2f} de 5.00")
salida.append(f"   • Nivel medio simple objetivo:     {promedio_objetivo_simple:.2f} de 5.00")
salida.append(f"   • Nivel medio ponderado objetivo:  {promedio_objetivo_ponderado:.2f} de 5.00")
salida.append(f"   --> Brecha de digitalización global ponderada: {promedio_objetivo_ponderado - promedio_ponderado:.2f} puntos")
salida.append("")
salida.append("2. PRUEBA DEL PRINCIPIO DE UNA SOLA VEZ (ONCE-ONLY PRINCIPLE):")
salida.append(f"   • Total de documentos solicitados a usuarios:        {total_docs_pedidos}")
salida.append(f"   • Documentos solicitados que YA POSEE la institución: {total_docs_redundantes}")
salida.append(f"   • Índice de redundancia documental institucional:    {pct_redundancia:.2f} %")
salida.append("   --> Dictamen: INEFICIENCIA CRÍTICA. Casi 2 de cada 3 requisitos exigidos")
salida.append("       ya constan en los registros académicos, contables o legajos del instituto.")
salida.append("")
salida.append("3. RANKING DE SERVICIOS POR BRECHA PONDERADA (TOP 5 DE MAYOR IMPACTO):")
salida.append(f"{'ID':<6} {'Servicio':<38} {'Volumen':<10} {'Act':<5} {'Obj':<5} {'Brecha Pond':<14} {'% Impacto'}")
salida.append("-" * 88)
for _, r in top5_brechas.iterrows():
    salida.append(f"{r['id']:<6} {r['Servicio'][:36]:<38} {r[col_vol]:<10,d} {r[col_actual]:<5.0f} {r[col_obj]:<5.0f} {r['brecha_ponderada']:<14,d} {r['pct_brecha_total']:<6.2f}%")
salida.append("-" * 88)
salida.append(f"Top 5 concentra el {top5_brechas['pct_brecha_total'].sum():.2f}% del esfuerzo de transformación digital.")
salida.append("=" * 80)

texto_reporte = "\n".join(salida)
print(texto_reporte)

# Guardar salida en evidencia
with open(os.path.join(EVID_DIR, "GD02_salida.txt"), "w", encoding="utf-8") as f:
    f.write(texto_reporte)

# 3. Generación de Gráfico de Visualización (GD_servicios.png)
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)

y = np.arange(len(df))
height = 0.38

# Barras horizontales
rects1 = ax.barh(y - height/2, df[col_actual], height, label="Nivel Actual (0 a 5)", color="#1F4E79", edgecolor="none")
rects2 = ax.barh(y + height/2, df[col_obj], height, label="Nivel Objetivo (PETI)", color="#2CA02C", edgecolor="none")

# Etiquetas de valores
for r in rects1:
    w = r.get_width()
    ax.text(w + 0.08, r.get_y() + r.get_height()/2, f"{w:.0f}", ha="left", va="center", fontsize=9, fontweight="bold", color="#1F4E79")

for r in rects2:
    w = r.get_width()
    ax.text(w + 0.08, r.get_y() + r.get_height()/2, f"{w:.0f}", ha="left", va="center", fontsize=9, fontweight="bold", color="#2CA02C")

ax.set_yticks(y)
ax.set_yticklabels([f"{r['id']}: {r['Servicio']}" for _, r in df.iterrows()], fontsize=9.5)
ax.invert_yaxis()  # primer servicio arriba
ax.set_xlabel("Nivel de Digitalización (0: Informativo/Nulo, 1: Básico, 2: Interactivo, 3: Transaccional, 4: Integrado, 5: Proactivo)", fontsize=9, fontweight="semibold")
ax.set_xlim(0, 5.5)
ax.set_title("Catálogo de Servicios: Nivel de Digitalización Actual vs. Objetivo\nInstituto Superior Tecnológico Vertiente Sur (Caso 07)", fontsize=12, fontweight="bold", pad=15)
ax.legend(loc="lower right", frameon=True, facecolor="#F8F9FA", edgecolor="#D1D5DB")

# Anotación del ponderado
txt_box = (f"Promedio Simple Actual: {promedio_simple:.2f} / 5.0\n"
           f"Promedio Ponderado Actual: {promedio_ponderado:.2f} / 5.0\n"
           f"Redundancia Documental: {pct_redundancia:.1f}%")
ax.text(0.98, 0.22, txt_box, transform=ax.transAxes, fontsize=9,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEF3C7', edgecolor='#F59E0B', alpha=0.9))

plt.tight_layout()
grafico_path = os.path.join(OUT_DIR, "GD_servicios.png")
plt.savefig(grafico_path, dpi=300)
plt.close()
print(f"\n[OK] Gráfico exportado exitosamente: {grafico_path}")
