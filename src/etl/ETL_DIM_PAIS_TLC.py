"""
ETL PARA DIM_PAIS_TLC
EXTRACCIÓN AUTOMÁTICA DESDE ARCHIVOS MARKDOWN DE RCR (MINCETUR)
SOLO INSERTA COLUMNAS QUE EXISTEN EN LA TABLA
"""

import os
import re
import pandas as pd
from sqlalchemy import create_engine, text
from collections import Counter

# ==================================================
# CONFIGURACIÓN
# ==================================================

CARPETA_MARKDOWN = r"C:\Users\Loayza\Downloads\BI\Fuentes-Proyecto\Reporte de Comercio Regional de Huancavelica y busques info de TLCs para palta\markdown_files"

POSTGRES_USUARIO = "postgres"
POSTGRES_CONTRASEÑA = "LLLR123"
POSTGRES_HOST = "localhost"
POSTGRES_PUERTO = "5432"
POSTGRES_DB = "Palta_Hass_DM"

# ==================================================
# BASE DE CONOCIMIENTO DE TLCs
# ==================================================

TLC_DATABASE = {
    'China': {'acuerdo': 'TLC Perú-China (2010)', 'arancel': 0, 'categoria': 'Premium'},
    'Estados Unidos': {'acuerdo': 'APC Perú-EE.UU. (2009)', 'arancel': 0, 'categoria': 'Premium'},
    'Unión Europea': {'acuerdo': 'Acuerdo Comercial Perú-UE (2013)', 'arancel': 0, 'categoria': 'Premium'},
    'Suiza': {'acuerdo': 'TLC Perú-EFTA (2011)', 'arancel': 0, 'categoria': 'Premium'},
    'Canadá': {'acuerdo': 'TLC Perú-Canadá (2009)', 'arancel': 0, 'categoria': 'Premium'},
    'Japón': {'acuerdo': 'TLC Perú-Japón (2012)', 'arancel': 0, 'categoria': 'Premium'},
    'Corea del Sur': {'acuerdo': 'TLC Perú-Corea (2011)', 'arancel': 0, 'categoria': 'Premium'},
    'Reino Unido': {'acuerdo': 'TLC Perú-Reino Unido (2021)', 'arancel': 0, 'categoria': 'Premium'},
    'Hong Kong': {'acuerdo': 'TLC Perú-Hong Kong (2013)', 'arancel': 0, 'categoria': 'Premium'},
    'Ecuador': {'acuerdo': 'Comunidad Andina (CAN)', 'arancel': 0, 'categoria': 'Premium'},
    'Colombia': {'acuerdo': 'Comunidad Andina (CAN)', 'arancel': 0, 'categoria': 'Premium'},
    'Bolivia': {'acuerdo': 'Comunidad Andina (CAN)', 'arancel': 0, 'categoria': 'Premium'},
    'Brasil': {'acuerdo': 'ACE Nº 58 - MERCOSUR', 'arancel': 8.0, 'categoria': 'Estándar'},
    'India': {'acuerdo': 'Sin TLC', 'arancel': 30.0, 'categoria': 'Estándar'},
    'Rusia': {'acuerdo': 'Sin TLC', 'arancel': 15.0, 'categoria': 'Estándar'},
    'México': {'acuerdo': 'Sin TLC', 'arancel': 5.0, 'categoria': 'Estándar'},
    'Chile': {'acuerdo': 'Sin TLC', 'arancel': 6.0, 'categoria': 'Estándar'},
    'Vietnam': {'acuerdo': 'Sin TLC', 'arancel': 10.0, 'categoria': 'Estándar'},
    'Malasia': {'acuerdo': 'Sin TLC', 'arancel': 5.0, 'categoria': 'Estándar'},
    'Filipinas': {'acuerdo': 'Sin TLC', 'arancel': 5.0, 'categoria': 'Estándar'},
}

def extraer_paises(texto):
    paises_buscar = {
        'China', 'Estados Unidos', 'Unión Europea', 'UE', 'Suiza', 'Canadá', 'Japón',
        'Corea del Sur', 'Reino Unido', 'Hong Kong', 'Brasil', 'India', 'Rusia',
        'México', 'Chile', 'Vietnam', 'Malasia', 'Filipinas', 'Ecuador', 'Colombia', 'Bolivia'
    }
    paises_encontrados = []
    for pais in paises_buscar:
        if re.search(r'\b' + re.escape(pais) + r'\b', texto, re.IGNORECASE):
            paises_encontrados.append(pais)
    return paises_encontrados

def obtener_info_pais(pais_nombre):
    nombre = 'Estados Unidos' if pais_nombre in ['EE.UU.', 'EEUU', 'USA'] else pais_nombre
    nombre = 'Unión Europea' if pais_nombre == 'UE' else nombre
    return TLC_DATABASE.get(nombre, {'acuerdo': 'Sin información', 'arancel': 10.0, 'categoria': 'Estándar'})

# ==================================================
# EXTRACCIÓN
# ==================================================

print("=" * 70)
print("📊 ETL - DIM_PAIS_TLC (EXTRACCIÓN DESDE RCR MARKDOWN)")
print("=" * 70)

archivos_md = [f for f in os.listdir(CARPETA_MARKDOWN) if f.endswith('.md')]
print(f"\n📄 Archivos encontrados: {len(archivos_md)}")

frecuencia_paises = Counter()
for archivo in archivos_md:
    with open(os.path.join(CARPETA_MARKDOWN, archivo), 'r', encoding='utf-8') as f:
        for pais in extraer_paises(f.read()):
            frecuencia_paises[pais] += 1

# ==================================================
# CONSTRUIR DATAFRAME (SOLO COLUMNAS QUE EXISTEN)
# ==================================================

print("\n📋 Construyendo registros para DIM_PAIS_TLC...")

data = []
paises_procesados = set()
for pais, freq in frecuencia_paises.most_common():
    if pais not in paises_procesados:
        info = obtener_info_pais(pais)
        data.append({
            'FK_Ubicacion': None,
            'Acuerdo_TLC': info['acuerdo'],
            'Arancel_Aplicable': info['arancel'],
            'Categoria_Mercado': info['categoria']
        })
        paises_procesados.add(pais)

df = pd.DataFrame(data)
print(f"\n✅ Registros únicos a insertar: {len(df)}")

# ==================================================
# CARGA A POSTGRESQL
# ==================================================

url_conexion = f"postgresql://{POSTGRES_USUARIO}:{POSTGRES_CONTRASEÑA}@{POSTGRES_HOST}:{POSTGRES_PUERTO}/{POSTGRES_DB}"
engine = create_engine(url_conexion)

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Conexión exitosa")
except Exception as e:
    print(f"❌ Error: {e}")
    exit()

with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_PAIS_TLC" RESTART IDENTITY CASCADE'))
    conn.commit()
print("✅ Datos existentes eliminados")

df.to_sql('DIM_PAIS_TLC', engine, if_exists='append', index=False)
print(f"✅ {len(df)} registros insertados")

# ==================================================
# VERIFICACIÓN
# ==================================================

verificacion = pd.read_sql(text('SELECT COUNT(*) as total FROM "DIM_PAIS_TLC"'), engine)
print(f"\n📊 Total registros: {verificacion['total'][0]}")

print("\n📋 Datos cargados:")
print(pd.read_sql(text('''
    SELECT "ID_Pais_TLC", "Acuerdo_TLC", "Arancel_Aplicable", "Categoria_Mercado"
    FROM "DIM_PAIS_TLC"
'''), engine).to_string(index=False))

print("\n" + "=" * 70)
print("🎉 ¡ETL COMPLETADO!")
print("📌 FK_Ubicacion se actualizará después de poblar DIM_UBICACION")
print("=" * 70)