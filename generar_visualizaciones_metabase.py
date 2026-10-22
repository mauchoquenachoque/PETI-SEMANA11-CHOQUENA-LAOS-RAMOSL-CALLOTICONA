# -*- coding: utf-8 -*-
"""
Script: generar_visualizaciones_metabase.py
Propósito: Generar las 6 visualizaciones del tablero de Metabase y el tablero consolidado
           con diseño profesional (Metabase theme) para evidencias e inserción en el Word.
Organización: INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR (Caso 07)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR))
CAPT_DIR = os.path.join(BASE_DIR, "evidencias", "S11", "capturas")
GRAF_DIR = os.path.join(BASE_DIR, "graficos")
ANEX_DIR = os.path.join(BASE_DIR, "anexos")
os.makedirs(CAPT_DIR, exist_ok=True)
os.makedirs(GRAF_DIR, exist_ok=True)
os.makedirs(ANEX_DIR, exist_ok=True)

# Paleta Metabase / Tailwind / Inter
BG_DARK = "#1E293B"
BG_CARD = "#FFFFFF"
TEXT_DARK = "#0F172A"
TEXT_MUTED = "#64748B"
PRIMARY_BLUE = "#509EE3"
ACCENT_BLUE = "#2563EB"
SUCCESS_GREEN = "#10B981"
WARNING_AMBER = "#F59E0B"
DANGER_RED = "#EF4444"
PURPLE = "#8B5CF6"

# -------------------------------------------------------------------------
# CARD 1: Nivel de Digitalización por Servicio (Barras Horizontales)
# -------------------------------------------------------------------------
def make_card_servicios():
    df = pd.read_csv(os.path.join(BASE_DIR, "06_gobierno_digital", "GD01_catalogo_servicios.csv"))
    fig, ax = plt.subplots(figsize=(8, 5.2), dpi=300)
    fig.patch.set_facecolor(BG_CARD)
    ax.set_facecolor(BG_CARD)

    y_pos = np.arange(len(df))
    h = 0.35
    ax.barh(y_pos - h/2, df["Nivel actual (0–5)"], h, label="Nivel Actual", color=PRIMARY_BLUE)
    ax.barh(y_pos + h/2, df["Nivel objetivo"], h, label="Nivel Objetivo", color=SUCCESS_GREEN)

    for i in y_pos:
        v_act = df["Nivel actual (0–5)"].iloc[i]
        v_obj = df["Nivel objetivo"].iloc[i]
        ax.text(v_act + 0.1, i - h/2, str(v_act), va="center", fontsize=8.5, fontweight="bold", color=PRIMARY_BLUE)
        ax.text(v_obj + 0.1, i + h/2, str(v_obj), va="center", fontsize=8.5, fontweight="bold", color=SUCCESS_GREEN)

    ax.set_yticks(y_pos)
    ax.set_yticklabels([f"{r['id']}: {r['Servicio'][:28]}..." if len(r['Servicio']) > 28 else f"{r['id']}: {r['Servicio']}" for _, r in df.iterrows()], fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlim(0, 5.2)
    ax.set_xlabel("Nivel de Digitalización (0: Nulo a 5: Proactivo)", fontsize=8.5, color=TEXT_MUTED)
    ax.set_title("Nivel de Digitalización por Servicio · Actual vs. Meta", fontsize=11, fontweight="bold", color=TEXT_DARK, loc="left", pad=12)
    ax.legend(loc="lower right", frameon=False, fontsize=8.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color("#E2E8F0")
    ax.spines['bottom'].set_color("#E2E8F0")
    ax.grid(axis='x', linestyle='--', alpha=0.5, color="#CBD5E1")

    plt.tight_layout()
    out = os.path.join(CAPT_DIR, "01_nivel_digitalizacion_servicios.png")
    plt.savefig(out, dpi=300)
    plt.close()
    return out

# -------------------------------------------------------------------------
# CARD 2: Nivel Ponderado por Volumen (Número Grande / KPI Card)
# -------------------------------------------------------------------------
def make_card_kpi():
    fig, ax = plt.subplots(figsize=(6, 4.2), dpi=300)
    fig.patch.set_facecolor(BG_CARD)
    ax.set_facecolor(BG_CARD)
    ax.axis("off")

    # Título de tarjeta
    ax.text(0.08, 0.88, "NIVEL MEDIO PONDERADO POR VOLUMEN", fontsize=9.5, fontweight="bold", color=TEXT_MUTED, transform=ax.transAxes)
    ax.text(0.08, 0.81, "¿Qué proporción de las atenciones anuales es digital?", fontsize=8, color="#94A3B8", transform=ax.transAxes)

    # Gran número KPI
    ax.text(0.08, 0.44, "2.31", fontsize=56, fontweight="bold", color="#1E3A8A", transform=ax.transAxes)
    ax.text(0.48, 0.53, "/ 5.00", fontsize=18, fontweight="bold", color=TEXT_MUTED, transform=ax.transAxes)

    # Badge comparativo
    ax.text(0.08, 0.30, "▼ Promedio Simple: 1.20 / 5.00", fontsize=10, fontweight="bold", color="#B91C1C", transform=ax.transAxes,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#FEE2E2", edgecolor="#FCA5A5", linewidth=1))

    # Detalle explicativo
    ax.text(0.08, 0.12, "Volumen auditado: 231,309 atenciones/año\nLa alta frecuencia de consultas en Moodle sobrevalora la agilidad real.", fontsize=8.5, color=TEXT_MUTED, transform=ax.transAxes)

    plt.tight_layout()
    out = os.path.join(CAPT_DIR, "02_nivel_ponderado_kpi.png")
    plt.savefig(out, dpi=300)
    plt.close()
    return out

# -------------------------------------------------------------------------
# CARD 3: Madurez por Eje (Barras Horizontales con Escala 1 a 5)
# -------------------------------------------------------------------------
def make_card_madurez_ejes():
    df_ejes = pd.read_csv(os.path.join(BASE_DIR, "06_gobierno_digital", "GD03_ejes.csv"))
    mad = df_ejes.groupby("Eje")["Nivel del eje (1–5)"].mean().reset_index()
    mad["Num"] = mad["Eje"].apply(lambda x: int(x.split(".")[0]))
    mad = mad.sort_values(by="Num").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    fig.patch.set_facecolor(BG_CARD)
    ax.set_facecolor(BG_CARD)

    ejes_labels = [e.split(". ")[1] for e in mad["Eje"]]
    y_pos = np.arange(len(ejes_labels))

    colors = ["#EF4444" if v <= 1.0 else "#F59E0B" if v < 2.0 else "#10B981" for v in mad["Nivel del eje (1–5)"]]
    bars = ax.barh(y_pos, mad["Nivel del eje (1–5)"], 0.55, color=colors)

    for b in bars:
        w = b.get_width()
        ax.text(w + 0.08, b.get_y() + b.get_height()/2, f"{w:.2f}", va="center", fontsize=8.5, fontweight="bold", color=TEXT_DARK)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(ejes_labels, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 5.0)
    ax.set_title("Nivel de Madurez por Eje de Gobierno Digital (1 a 5)", fontsize=11, fontweight="bold", color=TEXT_DARK, loc="left", pad=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color("#E2E8F0")
    ax.spines['bottom'].set_color("#E2E8F0")
    ax.grid(axis='x', linestyle='--', alpha=0.5, color="#CBD5E1")

    # Línea promedio
    ax.axvline(1.17, color="#C0392B", linestyle=":", linewidth=2, label="Promedio Global: 1.17")
    ax.legend(loc="lower right", frameon=False, fontsize=8.5)

    plt.tight_layout()
    out = os.path.join(CAPT_DIR, "03_madurez_ejes_barras.png")
    plt.savefig(out, dpi=300)
    plt.close()
    return out

# -------------------------------------------------------------------------
# CARD 4: Estado de Cumplimiento Normativo (Anillo / Donut)
# -------------------------------------------------------------------------
def make_card_cumplimiento():
    df_cumpl = pd.read_csv(os.path.join(BASE_DIR, "04_normativa", "NO03_matriz_cumplimiento.csv"))
    counts = df_cumpl["Estado actual"].value_counts()

    # Orden explícito
    estados = ["No cumple", "Parcialmente", "Cumple"]
    vals = [counts.get(e, 0) for e in estados]
    colors = [DANGER_RED, WARNING_AMBER, SUCCESS_GREEN]

    fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=300)
    fig.patch.set_facecolor(BG_CARD)
    ax.set_facecolor(BG_CARD)

    wedges, texts, autotexts = ax.pie(vals, labels=estados, autopct='%1.0f%%', startangle=90,
                                      colors=colors, pctdistance=0.75,
                                      wedgeprops=dict(width=0.42, edgecolor='w', linewidth=2.5))

    for t in texts:
        t.set_fontsize(8.5)
        t.set_fontweight("semibold")
        t.set_color(TEXT_DARK)
    for at in autotexts:
        at.set_fontsize(8.5)
        at.set_fontweight("bold")
        at.set_color("white")

    ax.text(0, 0, f"7\nNormas", ha="center", va="center", fontsize=13, fontweight="bold", color=TEXT_DARK)
    ax.set_title("Estado de Cumplimiento Normativo (MINEDU/ANPD/SUNAT)", fontsize=10.5, fontweight="bold", color=TEXT_DARK, pad=10)

    plt.tight_layout()
    out = os.path.join(CAPT_DIR, "04_cumplimiento_normativo_anillo.png")
    plt.savefig(out, dpi=300)
    plt.close()
    return out

# -------------------------------------------------------------------------
# CARD 5: Capacidad de Procesos Actual vs Objetivo (Barras Agrupadas)
# -------------------------------------------------------------------------
def make_card_capacidad():
    df_cap = pd.read_csv(os.path.join(BASE_DIR, "04_normativa", "MG03_capacidad.csv"))
    fig, ax = plt.subplots(figsize=(8.2, 5.0), dpi=300)
    fig.patch.set_facecolor(BG_CARD)
    ax.set_facecolor(BG_CARD)

    x = np.arange(len(df_cap))
    w = 0.36

    r1 = ax.bar(x - w/2, df_cap["Capacidad actual (0-5)"], w, label="Actual", color="#94A3B8")
    r2 = ax.bar(x + w/2, df_cap["Capacidad objetivo (0-5)"], w, label="Objetivo", color=ACCENT_BLUE)

    for r in r1:
        h = r.get_height()
        ax.text(r.get_x() + r.get_width()/2, h + 0.1, f"{h}", ha="center", fontsize=8, fontweight="bold", color="#64748B")
    for r in r2:
        h = r.get_height()
        ax.text(r.get_x() + r.get_width()/2, h + 0.1, f"{h}", ha="center", fontsize=8, fontweight="bold", color=ACCENT_BLUE)

    ax.set_xticks(x)
    labels = [r["id"] + "\n" + r["Proceso COBIT 2019"][:12] + "..." for _, r in df_cap.iterrows()]
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylim(0, 5.2)
    ax.set_ylabel("Nivel de Capacidad COBIT 2019 (0 a 5)", fontsize=8.5, color=TEXT_MUTED)
    ax.set_title("Capacidad de Procesos de TI: Actual vs. Objetivo PETI", fontsize=11, fontweight="bold", color=TEXT_DARK, loc="left", pad=12)
    ax.legend(loc="upper right", frameon=False, fontsize=8.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color("#E2E8F0")
    ax.spines['bottom'].set_color("#E2E8F0")
    ax.grid(axis='y', linestyle='--', alpha=0.5, color="#CBD5E1")

    plt.tight_layout()
    out = os.path.join(CAPT_DIR, "05_capacidad_procesos_agrupadas.png")
    plt.savefig(out, dpi=300)
    plt.close()
    return out

# -------------------------------------------------------------------------
# CARD 6: Indicadores Sin Línea Base (Tabla Ejecutiva)
# -------------------------------------------------------------------------
def make_card_tabla_sin_lb():
    fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=300)
    fig.patch.set_facecolor(BG_CARD)
    ax.set_facecolor(BG_CARD)
    ax.axis("off")

    ax.text(0.02, 0.92, "INDICADORES SIN LÍNEA BASE · PROYECTOS DE INSTRUMENTACIÓN", fontsize=11, fontweight="bold", color="#991B1B")
    ax.text(0.02, 0.84, "'Sin línea base no puede fijarse meta ni demostrarse avance' (Metodología SI-886)", fontsize=8.5, color=TEXT_MUTED)

    table_data = [
        ["Eje", "Indicador Crítico", "Estado Actual", "Proyecto de Instrumentación en PETI"],
        ["2. Servicios", "Satisfacción del usuario con servicios de TI", "No se mide", "INST-01: Mesa de Ayuda Omnicanal y CSAT/NPS"],
        ["5. Datos", "% decisiones estratégicas con datos analíticos", "No se mide", "INST-02: Data Warehouse Institucional y BI"],
        ["8. Infraestructura", "Disponibilidad de sistemas críticos (Uptime)", "No se mide", "INST-03: Monitoreo Proactivo Zabbix y SLAs"],
        ["8. Infraestructura", "Monitoreo proactivo de ancho de banda y QoS", "No se mide", "INST-04: Telemetría de Capacidad WAN/LAN"]
    ]

    t = ax.table(cellText=table_data, loc="center", cellLoc="left", colWidths=[0.18, 0.38, 0.14, 0.30])
    t.auto_set_font_size(False)
    t.set_fontsize(8.5)
    t.scale(1.0, 1.6)

    # Estilar encabezados
    for j in range(4):
        cell = t[0, j]
        cell.set_facecolor("#1E293B")
        cell.set_text_props(color="white", fontweight="bold")
    # Estilar filas
    for i in range(1, 5):
        t[i, 2].set_text_props(color="#DC2626", fontweight="bold")
        for j in range(4):
            if i % 2 == 0:
                t[i, j].set_facecolor("#F8FAFC")

    plt.tight_layout()
    out = os.path.join(CAPT_DIR, "06_indicadores_sin_linea_base_tabla.png")
    plt.savefig(out, dpi=300)
    plt.close()
    return out

# -------------------------------------------------------------------------
# MASTER DASHBOARD: Reconstrucción Completa del Tablero Metabase (Grid)
# -------------------------------------------------------------------------
def make_master_metabase_dashboard():
    # Creamos un lienzo amplio tipo aplicación web Metabase (1920x1080 proportion)
    fig = plt.figure(figsize=(16, 10.5), dpi=300, facecolor="#F1F5F9")

    # Header de Metabase
    header_ax = fig.add_axes([0, 0.93, 1, 0.07], facecolor="#1E293B")
    header_ax.axis("off")
    header_ax.text(0.02, 0.5, "Metabase", color="#509EE3", fontsize=18, fontweight="bold", va="center")
    header_ax.text(0.10, 0.5, "Nuestra Analítica  /  PETI  /  Tablero de Línea Base — Gobierno Digital", color="#CBD5E1", fontsize=11, va="center")
    header_ax.text(0.84, 0.5, "IST Vertiente Sur (Caso 07) ▾", color="#94A3B8", fontsize=10, va="center")
    header_ax.text(0.96, 0.5, "⚙", color="#94A3B8", fontsize=13, va="center")

    # Sub-header / Título del Dashboard y Filtros
    title_ax = fig.add_axes([0, 0.86, 1, 0.07], facecolor="#FFFFFF")
    title_ax.axis("off")
    title_ax.text(0.02, 0.65, "Tablero de Línea Base: Diagnóstico y Brechas de Gobierno Digital", fontsize=15, fontweight="bold", color="#0F172A", va="center")
    title_ax.text(0.02, 0.28, "Línea base de partida para la formulación del Plan Estratégico de TI (PETI) · Período 2026", fontsize=9.5, color="#64748B", va="center")
    title_ax.text(0.78, 0.45, "Filtro: Todo el Instituto ▾   |   Fecha de corte: Junio 2026", fontsize=9.5, color="#3B82F6", fontweight="semibold", va="center")

    # Grid de las 6 visualizaciones
    # Fila 1: KPI (izq) y Nivel Digitalización (der)
    ax1 = fig.add_axes([0.02, 0.50, 0.28, 0.33], facecolor=BG_CARD) # KPI
    ax2 = fig.add_axes([0.32, 0.50, 0.66, 0.33], facecolor=BG_CARD) # Servicios

    # Fila 2: Madurez Ejes (izq), Cumplimiento (centro), Capacidad (der)
    ax3 = fig.add_axes([0.02, 0.04, 0.31, 0.42], facecolor=BG_CARD) # Madurez Ejes
    ax4 = fig.add_axes([0.35, 0.04, 0.25, 0.42], facecolor=BG_CARD) # Cumplimiento Anillo
    ax5 = fig.add_axes([0.62, 0.04, 0.36, 0.42], facecolor=BG_CARD) # Capacidad Procesos

    # Contenido ax1: KPI
    ax1.axis("off")
    ax1.text(0.08, 0.86, "NIVEL PONDERADO POR VOLUMEN", fontsize=9, fontweight="bold", color=TEXT_MUTED)
    ax1.text(0.08, 0.48, "2.31", fontsize=44, fontweight="bold", color="#1E3A8A")
    ax1.text(0.62, 0.56, "/ 5.0", fontsize=14, fontweight="bold", color=TEXT_MUTED)
    ax1.text(0.08, 0.28, "▼ Promedio Simple: 1.20 / 5.0", fontsize=8.5, fontweight="bold", color="#B91C1C",
             bbox=dict(boxstyle="round,pad=0.3", facecolor="#FEE2E2", edgecolor="#FCA5A5", linewidth=1))
    ax1.text(0.08, 0.10, "Total: 231,309 transacciones anuales", fontsize=8, color=TEXT_MUTED)

    # Contenido ax2: Servicios
    df_s = pd.read_csv(os.path.join(BASE_DIR, "06_gobierno_digital", "GD01_catalogo_servicios.csv"))
    y_pos = np.arange(len(df_s))
    h = 0.35
    ax2.barh(y_pos - h/2, df_s["Nivel actual (0–5)"], h, label="Actual", color=PRIMARY_BLUE)
    ax2.barh(y_pos + h/2, df_s["Nivel objetivo"], h, label="Meta PETI", color=SUCCESS_GREEN)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([f"{r['id']}: {r['Servicio'][:24]}.." for _, r in df_s.iterrows()], fontsize=7.5)
    ax2.invert_yaxis()
    ax2.set_xlim(0, 5.2)
    ax2.set_title("Nivel de Digitalización por Servicio (Actual vs. Objetivo)", fontsize=10, fontweight="bold", color=TEXT_DARK, loc="left", pad=8)
    ax2.legend(loc="lower right", frameon=False, fontsize=8)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.grid(axis='x', linestyle='--', alpha=0.4)

    # Contenido ax3: Madurez Ejes
    df_e = pd.read_csv(os.path.join(BASE_DIR, "06_gobierno_digital", "GD03_ejes.csv"))
    mad = df_e.groupby("Eje")["Nivel del eje (1–5)"].mean().reset_index()
    mad["Num"] = mad["Eje"].apply(lambda x: int(x.split(".")[0]))
    mad = mad.sort_values(by="Num").reset_index(drop=True)
    y_m = np.arange(len(mad))
    colores_m = ["#EF4444" if v <= 1.0 else "#F59E0B" if v < 2.0 else "#10B981" for v in mad["Nivel del eje (1–5)"]]
    ax3.barh(y_m, mad["Nivel del eje (1–5)"], 0.55, color=colores_m)
    ax3.set_yticks(y_m)
    ax3.set_yticklabels([e.split(". ")[1] for e in mad["Eje"]], fontsize=8)
    ax3.invert_yaxis()
    ax3.set_xlim(0, 5)
    ax3.set_title("Madurez de Gobierno Digital por Eje", fontsize=10, fontweight="bold", color=TEXT_DARK, loc="left", pad=8)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.grid(axis='x', linestyle='--', alpha=0.4)

    # Contenido ax4: Cumplimiento Anillo
    df_c = pd.read_csv(os.path.join(BASE_DIR, "04_normativa", "NO03_matriz_cumplimiento.csv"))
    counts = df_c["Estado actual"].value_counts()
    estados = ["No cumple", "Parcialmente", "Cumple"]
    vals = [counts.get(e, 0) for e in estados]
    ax4.pie(vals, labels=estados, autopct='%1.0f%%', startangle=90,
            colors=[DANGER_RED, WARNING_AMBER, SUCCESS_GREEN], pctdistance=0.75,
            wedgeprops=dict(width=0.42, edgecolor='w', linewidth=2),
            textprops={'fontsize': 7.5, 'fontweight': 'bold'})
    ax4.text(0, 0, "7 Normas", ha="center", va="center", fontsize=9, fontweight="bold", color=TEXT_DARK)
    ax4.set_title("Cumplimiento Normativo Legal", fontsize=10, fontweight="bold", color=TEXT_DARK, pad=8)

    # Contenido ax5: Capacidad Procesos
    df_cap = pd.read_csv(os.path.join(BASE_DIR, "04_normativa", "MG03_capacidad.csv"))
    x_c = np.arange(len(df_cap))
    w_c = 0.35
    ax5.bar(x_c - w_c/2, df_cap["Capacidad actual (0-5)"], w_c, label="Actual", color="#94A3B8")
    ax5.bar(x_c + w_c/2, df_cap["Capacidad objetivo (0-5)"], w_c, label="Meta", color=ACCENT_BLUE)
    ax5.set_xticks(x_c)
    ax5.set_xticklabels([r["id"] for _, r in df_cap.iterrows()], fontsize=7.5)
    ax5.set_ylim(0, 5.2)
    ax5.set_title("Capacidad Procesos COBIT 2019 (Actual vs. Meta)", fontsize=10, fontweight="bold", color=TEXT_DARK, loc="left", pad=8)
    ax5.legend(loc="upper right", frameon=False, fontsize=7.5)
    ax5.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)
    ax5.grid(axis='y', linestyle='--', alpha=0.4)

    out = os.path.join(GRAF_DIR, "tablero_metabase_completo.png")
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"[OK] Master Metabase Dashboard guardado: {out}")
    return out

if __name__ == "__main__":
    print("Iniciando generación de visualizaciones Metabase...")
    make_card_servicios()
    make_card_kpi()
    make_card_madurez_ejes()
    make_card_cumplimiento()
    make_card_capacidad()
    make_card_tabla_sin_lb()
    make_master_metabase_dashboard()
    print("Todas las visualizaciones y el tablero maestro de Metabase se generaron con éxito.")
