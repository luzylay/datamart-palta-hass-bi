"""
SCRIPT CORREGIDO - VERIFICACIÓN DE DIM_FINANZAS
Con sintaxis correcta para SQLAlchemy 2.0
"""

import pandas as pd
from sqlalchemy import create_engine, text

# ==================================================
# CONFIGURACIÓN
# ==================================================

POSTGRES_USUARIO = "postgres"
POSTGRES_CONTRASEÑA = "LLLR123"
POSTGRES_HOST = "localhost"
POSTGRES_PUERTO = "5432"
POSTGRES_DB = "Palta_Hass_DM"

# ==================================================
# CONEXIÓN
# ==================================================

print("=" * 70)
print("📊 VERIFICACIÓN DE DIM_FINANZAS - BCRP (TIPO DE CAMBIO)")
print("=" * 70)

url_conexion = f"postgresql://{POSTGRES_USUARIO}:{POSTGRES_CONTRASEÑA}@{POSTGRES_HOST}:{POSTGRES_PUERTO}/{POSTGRES_DB}"
engine = create_engine(url_conexion)

print("\n🔌 Conectando a PostgreSQL...")
try:
    with engine.connect() as conn:
        # Usar text() para SQL puro
        result = conn.execute(text("SELECT 1"))
        print("✅ Conexión exitosa")
except Exception as e:
    print(f"❌ Error de conexión: {e}")
    exit()

# ==================================================
# VERIFICACIÓN
# ==================================================

print("\n" + "=" * 70)
print("✅ VERIFICACIÓN DE DATOS")
print("=" * 70)

# Total de registros
verificacion = pd.read_sql(text('SELECT COUNT(*) as total FROM "DIM_FINANZAS"'), engine)
print(f"📊 Total registros en DIM_FINANZAS: {verificacion['total'][0]:,}")

# Muestra de datos (primeros 10)
if verificacion['total'][0] > 0:
    muestra = pd.read_sql(text('''
        SELECT "ID_Finanzas", "Fecha_Referencia", "Tipo_Cambio_USD_PEN" 
        FROM "DIM_FINANZAS" 
        ORDER BY "Fecha_Referencia" 
        LIMIT 10
    '''), engine)
    print("\n📋 Muestra de datos cargados (primeros 10 días):")
    print(muestra.to_string(index=False))
    
    # Resumen por año
    resumen = pd.read_sql(text('''
        SELECT 
            EXTRACT(YEAR FROM "Fecha_Referencia") as año,
            COUNT(*) as días,
            ROUND(MIN("Tipo_Cambio_USD_PEN")::numeric, 3) as tc_min,
            ROUND(MAX("Tipo_Cambio_USD_PEN")::numeric, 3) as tc_max,
            ROUND(AVG("Tipo_Cambio_USD_PEN")::numeric, 3) as tc_promedio
        FROM "DIM_FINANZAS"
        GROUP BY EXTRACT(YEAR FROM "Fecha_Referencia")
        ORDER BY año
    '''), engine)
    
    print("\n📈 Resumen por año:")
    print(resumen.to_string(index=False))
else:
    print("\n⚠️ No hay datos en DIM_FINANZAS")

print("\n" + "=" * 70)
print("🎉 ¡VERIFICACIÓN COMPLETADA!")
print("=" * 70)