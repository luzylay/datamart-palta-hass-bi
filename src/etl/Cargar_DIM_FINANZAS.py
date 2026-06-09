"""
SCRIPT CORREGIDO - CARGA DIM_FINANZAS (CON NOMBRES DE COLUMNAS ENTRE COMILLAS DOBLES)
"""

import pandas as pd
from sqlalchemy import create_engine, text
import os

# ==================================================
# CONFIGURACIÓN
# ==================================================

ARCHIVO_BCRP = r"C:\Users\Loayza\Downloads\BI\Fuentes-Proyecto\histórico del Tipo de Cambio (USDPEN) del 2016 al 2024\TC_BCRP_USD_PEN_2016_2024.xlsx"

POSTGRES_USUARIO = "postgres"
POSTGRES_CONTRASEÑA = "LLLR123"
POSTGRES_HOST = "localhost"
POSTGRES_PUERTO = "5432"
POSTGRES_DB = "Palta_Hass_DM"

# ==================================================
# CARGA PRINCIPAL
# ==================================================

print("=" * 70)
print("📊 CARGA DE DIM_FINANZAS - BCRP (TIPO DE CAMBIO)")
print("=" * 70)

if not os.path.exists(ARCHIVO_BCRP):
    print(f"\n❌ ERROR: Archivo no encontrado")
    exit()

print(f"\n✅ Archivo encontrado")

# Leer hoja DIM_FINANZAS_TC
print("\n📂 Leyendo hoja: 'DIM_FINANZAS_TC'")
df = pd.read_excel(ARCHIVO_BCRP, sheet_name='DIM_FINANZAS_TC', header=1)
print(f"✅ Hoja leída: {len(df):,} filas")

# Limpieza básica
df = df.dropna(subset=['FECHA', 'TC_USD_PEN'])
df['FECHA'] = pd.to_datetime(df['FECHA'])
df = df[(df['FECHA'].dt.year >= 2016) & (df['FECHA'].dt.year <= 2024)]

print(f"📅 Registros después de limpieza: {len(df):,}")
print(f"📅 Rango: {df['FECHA'].min().date()} a {df['FECHA'].max().date()}")

# Preparar DataFrame final
df_final = pd.DataFrame()
df_final['Fecha_Referencia'] = df['FECHA']
df_final['Tipo_Cambio_USD_PEN'] = df['TC_USD_PEN']
df_final['FK_Ubicacion'] = None
df_final['Arancel_Porcentaje'] = None
df_final['Acuerdo_TLC'] = None
df_final['Fuente_BCRP'] = 'BCRP - Serie PD04638PD'
df_final['Fuente_MINCETUR'] = None

# Conectar a PostgreSQL
url_conexion = f"postgresql://{POSTGRES_USUARIO}:{POSTGRES_CONTRASEÑA}@{POSTGRES_HOST}:{POSTGRES_PUERTO}/{POSTGRES_DB}"
engine = create_engine(url_conexion)

# ==================================================
# LIMPIAR DATOS EXISTENTES
# ==================================================

print("\n🔌 Conectando a PostgreSQL...")
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Conexión exitosa")
except Exception as e:
    print(f"❌ Error de conexión: {e}")
    exit()

print("\n💾 Limpiando datos existentes...")
with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_FINANZAS" RESTART IDENTITY CASCADE'))
    conn.commit()
print("✅ Datos existentes eliminados")

# ==================================================
# CARGAR NUEVOS DATOS
# ==================================================

print("\n💾 Cargando nuevos datos...")
df_final.to_sql('DIM_FINANZAS', engine, if_exists='append', index=False)
print(f"✅ {len(df_final):,} registros insertados")

# ==================================================
# VERIFICACIÓN (TODAS LAS COLUMNAS CON COMILLAS DOBLES)
# ==================================================

print("\n" + "=" * 70)
print("✅ VERIFICACIÓN FINAL")
print("=" * 70)

# Total de registros
verificacion = pd.read_sql('SELECT COUNT(*) as total FROM "DIM_FINANZAS"', engine)
print(f"📊 Total registros en DIM_FINANZAS: {verificacion['total'][0]:,}")

# Mostrar muestra (con comillas dobles en columnas)
muestra = pd.read_sql('''
    SELECT 
        "Fecha_Referencia", 
        "Tipo_Cambio_USD_PEN" 
    FROM "DIM_FINANZAS" 
    ORDER BY "Fecha_Referencia"
    LIMIT 10
''', engine)
print("\n📋 Muestra de datos (primeros 10 días):")
print(muestra.to_string(index=False))

# Resumen por año (con comillas dobles en columnas y alias sin comillas)
resumen = pd.read_sql('''
    SELECT 
        EXTRACT(YEAR FROM "Fecha_Referencia") as año,
        COUNT(*) as días,
        ROUND(MIN("Tipo_Cambio_USD_PEN")::numeric, 3) as tc_min,
        ROUND(MAX("Tipo_Cambio_USD_PEN")::numeric, 3) as tc_max,
        ROUND(AVG("Tipo_Cambio_USD_PEN")::numeric, 3) as tc_promedio
    FROM "DIM_FINANZAS"
    GROUP BY EXTRACT(YEAR FROM "Fecha_Referencia")
    ORDER BY año
''', engine)

print("\n📈 Resumen por año:")
print(resumen.to_string(index=False))

print("\n" + "=" * 70)
print("🎉 ¡DIM_FINANZAS CARGADA EXITOSAMENTE!")
print("=" * 70)