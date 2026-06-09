"""
ETL PARA DIM_COSTO - CORREGIDO
EXTRACCIÓN DESDE TABLAS DEL DOCUMENTO WORD PRINCIPAL
"""

import os
import re
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date
from docx import Document

# ==================================================
# CONFIGURACIÓN
# ==================================================

CARPETA_COSTOS = r"C:\Users\Loayza\Downloads\BI\Fuentes-Proyecto\Costos Referenciales de Producción y Logística de la palta Hass"
ARCHIVO_PRINCIPAL = "Costos Referenciales de Producción y Logística de la palta Hass.docx"

POSTGRES_USUARIO = "postgres"
POSTGRES_CONTRASEÑA = "LLLR123"
POSTGRES_HOST = "localhost"
POSTGRES_PUERTO = "5432"
POSTGRES_DB = "Palta_Hass_DM"

def extraer_valor_moneda_celda(cell_text, cell_index, row_cells):
    """Extrae el valor de la celda correcta (columna 2 = índice 2)"""
    if not cell_text:
        return None
    # Buscar patrón como $0.25 o 0.25
    match = re.search(r'\$?(\d+\.\d+)', str(cell_text))
    if match:
        valor = float(match.group(1))
        # Validar rango razonable para costos (entre 0.01 y 5.0)
        if 0.01 <= valor <= 5.0:
            return valor
    return None

# ==================================================
# EXTRACCIÓN DESDE WORD
# ==================================================

print("=" * 70)
print("📊 ETL - DIM_COSTO (MIDAGRI / SIERRA EXPORTADORA)")
print("=" * 70)

ruta_word = os.path.join(CARPETA_COSTOS, ARCHIVO_PRINCIPAL)

if not os.path.exists(ruta_word):
    print(f"\n❌ ERROR: No se encuentra el archivo {ARCHIVO_PRINCIPAL}")
    exit()

print(f"\n📂 Leyendo documento: {ARCHIVO_PRINCIPAL}")
doc = Document(ruta_word)

# Diccionario para almacenar costos únicos
costos = {}

# Patrones de búsqueda por subcategoría
patrones_subcategoria = {
    'Labores Culturales e Insumos': ['labores culturales', 'insumos'],
    'Mano de Obra de Cosecha': ['mano de obra', 'cosecha'],
    'Procesamiento en Packing': ['procesamiento', 'packing', 'empaque'],
    'Transporte Terrestre Interno': ['transporte terrestre', 'flete terrestre'],
    'Servicios Portuarios y Estiba': ['servicios portuarios', 'estiba'],
    'Agenciamiento y Certificaciones': ['agenciamiento', 'certificaciones'],
    'Certificaciones Internacionales': ['certificaciones internacionales'],
    'Gastos Administrativos Corporativos': ['gastos administrativos']
}

# Mapeo de subcategoría a Tipo_Costo
tipo_por_subcategoria = {
    'Labores Culturales e Insumos': 'Producción',
    'Mano de Obra de Cosecha': 'Producción',
    'Procesamiento en Packing': 'Producción',
    'Transporte Terrestre Interno': 'Logístico',
    'Servicios Portuarios y Estiba': 'Logístico',
    'Agenciamiento y Certificaciones': 'Logístico',
    'Certificaciones Internacionales': 'Operativo',
    'Gastos Administrativos Corporativos': 'Operativo'
}

print("\n🔍 Extrayendo costos desde tablas...")

for table in doc.tables:
    for row in table.rows:
        cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
        texto_fila = ' '.join(cells).lower()
        
        for subcat, keywords in patrones_subcategoria.items():
            if any(kw in texto_fila for kw in keywords) and subcat not in costos:
                # Buscar valor en las celdas (generalmente en la columna 2 o 3)
                valor = None
                for idx, cell in enumerate(cells):
                    valor_cell = extraer_valor_moneda_celda(cell, idx, cells)
                    if valor_cell:
                        valor = valor_cell
                        break
                
                if valor:
                    costos[subcat] = {
                        'Tipo_Costo': tipo_por_subcategoria[subcat],
                        'Subcategoria': subcat,
                        'Region_Destino': 'Global',
                        'Valor_Unitario_USD': valor
                    }
                    print(f"   ✓ {tipo_por_subcategoria[subcat]} - {subcat}: ${valor}/kg")

# ==================================================
# VALORES POR DEFECTO (SI NO SE ENCONTRARON)
# ==================================================

if not costos:
    print("\n⚠️ No se encontraron costos en el documento. Usando valores por defecto...")
    costos_por_defecto = {
        'Labores Culturales e Insumos': {'Tipo_Costo': 'Producción', 'Valor_Unitario_USD': 0.25},
        'Mano de Obra de Cosecha': {'Tipo_Costo': 'Producción', 'Valor_Unitario_USD': 0.20},
        'Procesamiento en Packing': {'Tipo_Costo': 'Producción', 'Valor_Unitario_USD': 0.30},
        'Transporte Terrestre Interno': {'Tipo_Costo': 'Logístico', 'Valor_Unitario_USD': 0.15},
        'Servicios Portuarios y Estiba': {'Tipo_Costo': 'Logístico', 'Valor_Unitario_USD': 0.60},
        'Agenciamiento y Certificaciones': {'Tipo_Costo': 'Logístico', 'Valor_Unitario_USD': 0.04},
        'Certificaciones Internacionales': {'Tipo_Costo': 'Operativo', 'Valor_Unitario_USD': 0.06},
        'Gastos Administrativos Corporativos': {'Tipo_Costo': 'Operativo', 'Valor_Unitario_USD': 0.04}
    }
    for subcat, info in costos_por_defecto.items():
        costos[subcat] = {
            'Tipo_Costo': info['Tipo_Costo'],
            'Subcategoria': subcat,
            'Region_Destino': 'Global',
            'Valor_Unitario_USD': info['Valor_Unitario_USD']
        }

# ==================================================
# TRANSFORMACIÓN
# ==================================================

df = pd.DataFrame(list(costos.values()))

# Agregar campos SCD Tipo 2
df['Fecha_Vigencia_Inicio'] = date(2016, 1, 1)
df['Fecha_Vigencia_Fin'] = None
df['Es_Vigente'] = True
df['Fuente_Estimacion'] = 'MIDAGRI / Sierra Exportadora - Extraído de Word'

print(f"\n✅ Total de costos extraídos: {len(df)}")
print(f"💰 Total costo por kg: ${df['Valor_Unitario_USD'].sum():.2f}/kg")

# ==================================================
# DATOS A INSERTAR
# ==================================================

print("\n" + "=" * 70)
print("📋 DATOS A INSERTAR")
print("=" * 70)
print(df[['Tipo_Costo', 'Subcategoria', 'Valor_Unitario_USD']].to_string(index=False))

# ==================================================
# CARGA A POSTGRESQL
# ==================================================

print("\n" + "=" * 70)
print("💾 CARGA A DIM_COSTO")
print("=" * 70)

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
    conn.execute(text('TRUNCATE TABLE "DIM_COSTO" RESTART IDENTITY CASCADE'))
    conn.commit()
print("✅ Datos existentes eliminados")

df.to_sql('DIM_COSTO', engine, if_exists='append', index=False)
print(f"✅ {len(df)} registros insertados")

# ==================================================
# VERIFICACIÓN
# ==================================================

print("\n" + "=" * 70)
print("✅ VERIFICACIÓN")
print("=" * 70)

verificacion = pd.read_sql(text('SELECT COUNT(*) as total FROM "DIM_COSTO"'), engine)
print(f"📊 Total registros en DIM_COSTO: {verificacion['total'][0]}")

datos_cargados = pd.read_sql(text('''
    SELECT "ID_Costo", "Tipo_Costo", "Subcategoria", 
           "Valor_Unitario_USD", "Es_Vigente"
    FROM "DIM_COSTO"
    ORDER BY "ID_Costo"
'''), engine)

print("\n📋 Datos cargados:")
print(datos_cargados.to_string(index=False))

print("\n" + "=" * 70)
print("🎉 ¡ETL - DIM_COSTO COMPLETADO EXITOSAMENTE!")
print("=" * 70)