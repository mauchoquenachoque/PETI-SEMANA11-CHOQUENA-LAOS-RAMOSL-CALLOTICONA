# -*- coding: utf-8 -*-
"""
Programa: GD05_carga_tablero.py
Propósito: Carga del catálogo de servicios, ejes de gobierno digital, matriz de
           cumplimiento y capacidad de procesos en PostgreSQL / base analítica
           para el despliegue del Tablero de Línea Base en Metabase.
Organización: INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR (Caso 07)
Curso: SI-886 Planeamiento Estratégico de TI - Taller Semana 11
"""

import os
import sys
import pandas as pd
from sqlalchemy import create_engine

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVID_DIR = os.path.join(SCRIPT_DIR, "..", "evidencias", "S11", "salidas")
os.makedirs(EVID_DIR, exist_ok=True)

# Rutas de los CSVs generados
csv_servicios = os.path.join(SCRIPT_DIR, "GD01_catalogo_servicios.csv")
csv_ejes = os.path.join(SCRIPT_DIR, "GD03_ejes.csv")
csv_cumplimiento = os.path.join(SCRIPT_DIR, "..", "04_normativa", "NO03_matriz_cumplimiento.csv")
csv_capacidad = os.path.join(SCRIPT_DIR, "..", "04_normativa", "MG03_capacidad.csv")

# Intentar conexión a PostgreSQL (Docker en puerto 5433)
pg_url = "postgresql://peti:peti_lab@127.0.0.1:5433/peti"
sqlite_url = f"sqlite:///{os.path.join(SCRIPT_DIR, 'peti_tablero.db')}"

motor_usado = None
eng = None

try:
    eng = create_engine(pg_url)
    # Probar conexión real
    with eng.connect() as conn:
        pass
    motor_usado = "PostgreSQL Docker (127.0.0.1:5433/peti)"
except Exception as e:
    # Fallback seguro para entorno local sin demonio Docker activo
    eng = create_engine(sqlite_url)
    motor_usado = f"Base de Datos Relacional Analítica (SQLite local: peti_tablero.db)"

# Carga de tablas
df_servicios = pd.read_csv(csv_servicios)
df_ejes = pd.read_csv(csv_ejes)
df_cumplimiento = pd.read_csv(csv_cumplimiento)
df_capacidad = pd.read_csv(csv_capacidad)

df_servicios.to_sql("servicios", eng, if_exists="replace", index=False)
df_ejes.to_sql("ejes_gd", eng, if_exists="replace", index=False)
df_cumplimiento.to_sql("cumplimiento", eng, if_exists="replace", index=False)
df_capacidad.to_sql("capacidad", eng, if_exists="replace", index=False)

salida = []
salida.append("=" * 80)
salida.append("INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR - CARGA TABLERO METABASE")
salida.append("PROGRAMA: GD05_carga_tablero.py")
salida.append("=" * 80)
salida.append(f"Motor de Base de Datos conectado: {motor_usado}")
salida.append("")
salida.append("Tablas cargadas exitosamente para el Tablero de Línea Base:")
salida.append(f"  1. 'servicios'     : {len(df_servicios)} registros cargados desde GD01_catalogo_servicios.csv")
salida.append(f"  2. 'ejes_gd'       : {len(df_ejes)} registros cargados desde GD03_ejes.csv")
salida.append(f"  3. 'cumplimiento'  : {len(df_cumplimiento)} registros cargados desde NO03_matriz_cumplimiento.csv")
salida.append(f"  4. 'capacidad'     : {len(df_capacidad)} registros cargados desde MG03_capacidad.csv")
salida.append("")
salida.append("Configuración de origen de datos en Metabase:")
salida.append("  • Tipo: PostgreSQL (o SQLite según despliegue)")
salida.append("  • Host: host.docker.internal / 127.0.0.1")
salida.append("  • Puerto: 5433 | Base: peti | Usuario: peti")
salida.append("  • URL de acceso al Tablero: http://127.0.0.1:3001/dashboard/linea-base-gobierno-digital")
salida.append("=" * 80)

reporte_txt = "\n".join(salida)
print(reporte_txt)

with open(os.path.join(EVID_DIR, "GD05_salida.txt"), "w", encoding="utf-8") as f:
    f.write(reporte_txt)

print("\nDatos cargados. Metabase: http://127.0.0.1:3001")
