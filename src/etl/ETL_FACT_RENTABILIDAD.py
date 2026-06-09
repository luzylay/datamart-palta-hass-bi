"""
ETL PARA FACT_RENTABILIDAD - VERSIÓN DBF (CORREGIDO)
Carga desde archivos DBF a FACT_RENTABILIDAD
CORREGIDO: Actualización de FK_Finanzas sin condición FK_Ubicacion
"""

import pandas as pd
from sqlalchemy import create_engine, text
import os
import re
from dbfread import DBF

# ==================================================
# CONFIGURACIÓN
# ==================================================

POSTGRES_USUARIO = "postgres"
POSTGRES_CONTRASEÑA = "LLLR123"
POSTGRES_HOST = "localhost"
POSTGRES_PUERTO = "5432"
POSTGRES_DB = "Palta_Hass_DM"

# Ruta de la carpeta con los archivos DBF
CARPETA_DATOS = r"C:\Users\Loayza\Downloads\PROYECTO_PALTA_HASS\DATOS_ORIGINALES"

# ==================================================
# CONEXIÓN A POSTGRESQL
# ==================================================

url_conexion = f"postgresql://{POSTGRES_USUARIO}:{POSTGRES_CONTRASEÑA}@{POSTGRES_HOST}:{POSTGRES_PUERTO}/{POSTGRES_DB}"
engine = create_engine(url_conexion)

print("=" * 80)
print("📊 CARGANDO FACT_RENTABILIDAD DESDE ARCHIVOS DBF")
print("=" * 80)

# ==================================================
# 1. CARGAR MAPEOS DE DIMENSIONES
# ==================================================

print("\n📂 Cargando dimensiones para mapeo...")

# DIM_TIEMPO
df_tiempo = pd.read_sql('SELECT "ID_Tiempo", "Fecha" FROM "DIM_TIEMPO"', engine)
df_tiempo['Fecha'] = pd.to_datetime(df_tiempo['Fecha']).dt.date
map_fecha = dict(zip(df_tiempo['Fecha'], df_tiempo['ID_Tiempo']))
print(f"   ✅ DIM_TIEMPO: {len(map_fecha)} registros")

# DIM_UBICACION
df_ubicacion = pd.read_sql('SELECT "ID_Ubicacion", "Pais_Nombre" FROM "DIM_UBICACION"', engine)
map_pais = dict(zip(df_ubicacion['Pais_Nombre'], df_ubicacion['ID_Ubicacion']))
print(f"   ✅ DIM_UBICACION: {len(map_pais)} registros")

# DIM_EXPORTADOR
df_exportador = pd.read_sql('SELECT "ID_Exportador", "RUC" FROM "DIM_EXPORTADOR"', engine)
map_ruc = dict(zip(df_exportador['RUC'], df_exportador['ID_Exportador']))
print(f"   ✅ DIM_EXPORTADOR: {len(map_ruc)} registros")

# DIM_ADUANA
df_aduana = pd.read_sql('SELECT "ID_Aduana", "Nombre_Aduana" FROM "DIM_ADUANA"', engine)
map_aduana = dict(zip(df_aduana['Nombre_Aduana'], df_aduana['ID_Aduana']))
print(f"   ✅ DIM_ADUANA: {len(map_aduana)} registros")

# DIM_PRODUCTO
df_producto = pd.read_sql('SELECT "ID_Producto" FROM "DIM_PRODUCTO" LIMIT 1', engine)
id_producto = df_producto.iloc[0]['ID_Producto'] if len(df_producto) > 0 else 1
print(f"   ✅ DIM_PRODUCTO: ID = {id_producto}")

# DIM_VARIEDAD_CALIDAD
df_calidad = pd.read_sql('SELECT "ID_Variedad_Calidad" FROM "DIM_VARIEDAD_CALIDAD" LIMIT 1', engine)
id_calidad = df_calidad.iloc[0]['ID_Variedad_Calidad'] if len(df_calidad) > 0 else 1
print(f"   ✅ DIM_VARIEDAD_CALIDAD: ID = {id_calidad}")

df_calidad_completa = pd.read_sql('SELECT * FROM "DIM_VARIEDAD_CALIDAD"', engine)
mapa_calidad = {
    (
        str(row['Variedad']).strip(),
        str(row['Categoria_Calidad']).strip(),
        str(row['Metodo_Produccion']).strip()
    ): int(row['ID_Variedad_Calidad'])
    for _, row in df_calidad_completa.iterrows()
}

# DIM_COSTO (prioriza Logístico)
df_costo = pd.read_sql('''
    SELECT "ID_Costo", "Tipo_Costo", "Subcategoria"
    FROM "DIM_COSTO"
    WHERE "Es_Vigente" = TRUE
    ORDER BY
        CASE WHEN "Tipo_Costo" = 'Logístico' THEN 0 ELSE 1 END,
        "ID_Costo"
    LIMIT 1
''', engine)
id_costo = df_costo.iloc[0]['ID_Costo'] if len(df_costo) > 0 else 1
print(f"   ✅ DIM_COSTO: ID = {id_costo}")

# ==================================================
# 2. BUSCAR ARCHIVOS DBF
# ==================================================

print(f"\n📂 Buscando archivos DBF en: {CARPETA_DATOS}")

if not os.path.exists(CARPETA_DATOS):
    print(f"   ❌ Carpeta no encontrada: {CARPETA_DATOS}")
    exit()

archivos_dbf = [f for f in os.listdir(CARPETA_DATOS) if f.upper().endswith('.DBF')]
print(f"   📄 Archivos DBF encontrados: {len(archivos_dbf)}")

for f in archivos_dbf:
    print(f"      - {f}")

if len(archivos_dbf) == 0:
    print("   ❌ No se encontraron archivos DBF")
    exit()

# ==================================================
# 3. FUNCIONES DE LIMPIEZA
# ==================================================

def limpiar_texto(texto):
    if pd.isna(texto):
        return ""
    return ''.join([c for c in str(texto) if ord(c) < 128]).strip()

def es_palta_hass(texto):
    if pd.isna(texto):
        return False
    texto = str(texto).upper()
    patrones_hass = [r'\bHASS?\b', r'\bHAS\b', r'PALTA.*HASS', r'AGUACATE.*HASS', r'AVOCADO.*HASS']
    patrones_excluir = [r'PULPA', r'CONGELADO', r'CONGELADA', r'TROZOS', r'TAJADAS', 
                        r'PROCESAMIENTO', r'MUESTRA', r'ACEITE', r'PURÉ', r'PROCESADO', 
                        r'HARINA', r'DESHIDRATADA', r'TRITURADA', r'IQF']
    es_hass = any(re.search(p, texto) for p in patrones_hass)
    es_excluido = any(re.search(p, texto) for p in patrones_excluir)
    return es_hass and not es_excluido

def extraer_atributos_descripcion(texto):
    """Extrae variedad, calidad y método de producción usando Regex."""
    if pd.isna(texto):
        texto = ""
    texto = str(texto).upper()

    variedad = "HASS" if re.search(r'\bHASS?\b', texto) else "NO_DEFINIDO"

    if re.search(r'CAT\s*\.?\s*1', texto):
        calidad = "CAT 1"
    elif re.search(r'CAT\s*\.?\s*2', texto):
        calidad = "CAT 2"
    else:
        calidad = "NO_ESPECIFICA"

    metodo = "ORGANICO" if re.search(r'ORGANIC[OA]', texto) else "CONVENCIONAL"

    return variedad, calidad, metodo

def mapear_calidad(texto):
    variedad, calidad, metodo = extraer_atributos_descripcion(texto)
    return mapa_calidad.get((variedad, calidad, metodo), id_calidad)

def generar_clave_unica(row):
    """Genera clave única usando todos los diferenciadores disponibles."""
    campos = [
        str(row.get('NRO_DOCU', '')).strip(),
        str(row.get('FECHA', '')).strip(),
        str(row.get('ITEM', '1')).strip(),
        str(row.get('CNAN', '')).strip(),
        str(row.get('CPAIS', '')).strip(),
        str(row.get('EXPORTADOR', '')).strip()[:50],
        str(row.get('CADUANA', '')).strip(),
        str(row.get('VIA_TRANSP', '')).strip(),
        str(row.get('PUER_EMBAR', '')).strip(),
    ]
    return '|'.join(campos)

# ==================================================
# 4. PROCESAR CADA ARCHIVO DBF
# ==================================================

hechos_final = []
claves_vistas = set()
estadisticas = {
    'total': 0, 
    'sin_fecha': 0, 
    'sin_pais': 0, 
    'hass': 0,
    'ok': 0,
    'duplicados': 0
}

for archivo in archivos_dbf:
    ruta = os.path.join(CARPETA_DATOS, archivo)
    print(f"\n📄 Procesando: {archivo}")
    
    try:
        # Leer DBF
        tabla = DBF(ruta, encoding='latin-1', ignore_missing_memofile=True)
        df = pd.DataFrame(iter(tabla))
        
        # Limpiar nombres de columnas
        df.columns = [col.upper() for col in df.columns]
        
        # Agregar ITEM si no existe
        if 'ITEM' not in df.columns:
            columnas_orden = [
                'NRO_DOCU',
                'FECHA',
                'CNAN',
                'FOB_DOLPOL',
                'PESO_NETO',
                'CPAIS',
                'EXPORTADOR',
                'CADUANA',
                'VIA_TRANSP',
                'PUER_EMBAR',
            ]
            columnas_orden = [col for col in columnas_orden if col in df.columns]
            df = df.sort_values(columnas_orden)
            df['ITEM'] = df.groupby(['NRO_DOCU', 'FECHA']).cumcount() + 1
        else:
            df['ITEM'] = pd.to_numeric(df['ITEM'], errors='coerce').fillna(1).astype(int)
        
        # Eliminar duplicados por clave única
        df['CLAVE_UNICA'] = df.apply(generar_clave_unica, axis=1)
        duplicados_antes = len(df)
        df = df[~df['CLAVE_UNICA'].isin(claves_vistas)]
        claves_vistas.update(df['CLAVE_UNICA'].tolist())
        estadisticas['duplicados'] += (duplicados_antes - len(df))
        
        # Filtrar por palta Hass
        df['ES_HASS'] = False
        if 'DESC_ADIC' in df.columns:
            df['ES_HASS'] = df['ES_HASS'] | df['DESC_ADIC'].astype(str).apply(es_palta_hass)
        if 'DESC_COM' in df.columns:
            df['ES_HASS'] = df['ES_HASS'] | df['DESC_COM'].astype(str).apply(es_palta_hass)
        
        df_hass = df[df['ES_HASS'] == True]
        estadisticas['hass'] += len(df_hass)
        
        if len(df_hass) == 0:
            print(f"   ⚠️ No se encontraron registros de palta Hass")
            continue
        
        # Limpiar datos nulos
        df_hass = df_hass.dropna(subset=['FOB_DOLPOL', 'PESO_NETO', 'FECHA', 'PAIS_DESC'])
        df_hass = df_hass[(df_hass['FOB_DOLPOL'] > 0) & (df_hass['PESO_NETO'] > 0)]
        
        # Procesar fecha
        df_hass['FECHA_STR'] = df_hass['FECHA'].astype(str).str.strip()
        df_hass['FECHA_DT'] = pd.to_datetime(df_hass['FECHA_STR'], format='%Y%m%d', errors='coerce')
        df_hass = df_hass.dropna(subset=['FECHA_DT'])
        df_hass = df_hass[(df_hass['FECHA_DT'].dt.year >= 2016) & (df_hass['FECHA_DT'].dt.year <= 2024)]
        df_hass['FECHA_DATE'] = df_hass['FECHA_DT'].dt.date
        
        # Limpiar textos
        df_hass['PAIS_DESC'] = df_hass['PAIS_DESC'].apply(limpiar_texto)
        if 'DESC_ADIC' in df_hass.columns:
            df_hass['DESC_ADIC'] = df_hass['DESC_ADIC'].apply(limpiar_texto)
        if 'NRO_DOCU' in df_hass.columns:
            df_hass['NRO_DOCU'] = df_hass['NRO_DOCU'].apply(limpiar_texto)
        if 'ADUA_DESC' in df_hass.columns:
            df_hass['ADUA_DESC'] = df_hass['ADUA_DESC'].apply(limpiar_texto)
        
        # Mapear dimensiones
        df_hass['FK_Tiempo'] = df_hass['FECHA_DATE'].map(map_fecha)
        df_hass['FK_Ubicacion'] = df_hass['PAIS_DESC'].map(map_pais)
        df_hass['FK_Producto'] = id_producto
        if 'DESC_ADIC' in df_hass.columns:
            df_hass['FK_Variedad_Calidad'] = df_hass['DESC_ADIC'].apply(mapear_calidad)
        else:
            df_hass['FK_Variedad_Calidad'] = id_calidad
        
        # Exportador
        if 'NRO_DOCU' in df_hass.columns:
            df_hass['FK_Exportador'] = df_hass['NRO_DOCU'].map(map_ruc).fillna(1).astype(int)
        else:
            df_hass['FK_Exportador'] = 1
        
        # Aduana
        if 'ADUA_DESC' in df_hass.columns:
            df_hass['FK_Aduana'] = df_hass['ADUA_DESC'].map(map_aduana).fillna(1).astype(int)
        else:
            df_hass['FK_Aduana'] = 1
        
        # Finanzas (se deja NULL temporalmente, se actualizará después)
        df_hass['FK_Finanzas'] = None
        
        # Costo
        df_hass['FK_Costo'] = id_costo
        
        # Eliminar registros sin FK válidos
        df_hass_validos = df_hass.dropna(subset=['FK_Tiempo', 'FK_Ubicacion'])
        
        # Agregar a la lista final
        for _, row in df_hass_validos.iterrows():
            hechos_final.append({
                'FK_Tiempo': int(row['FK_Tiempo']),
                'FK_Ubicacion': int(row['FK_Ubicacion']),
                'FK_Producto': int(row['FK_Producto']),
                'FK_Variedad_Calidad': int(row['FK_Variedad_Calidad']),
                'FK_Exportador': int(row['FK_Exportador']),
                'FK_Aduana': int(row['FK_Aduana']),
                'FK_Finanzas': None,
                'FK_Costo': int(id_costo),
                'Valor_FOB': float(row['FOB_DOLPOL']),
                'Volumen_Exportado': float(row['PESO_NETO'])
                , 'NRO_DOCU': str(row.get('NRO_DOCU', '')).strip()
            })
            estadisticas['ok'] += 1
        
        estadisticas['total'] += len(df_hass_validos)
        print(f"   ✅ Registros válidos: {len(df_hass_validos):,}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")

# ==================================================
# 5. RESUMEN DE ESTADÍSTICAS
# ==================================================

print("\n" + "=" * 80)
print("📊 ESTADÍSTICAS DE PROCESAMIENTO")
print("=" * 80)
print(f"   Total registros de palta Hass encontrados: {estadisticas['hass']:,}")
print(f"   Registros duplicados eliminados: {estadisticas['duplicados']:,}")
print(f"   Registros OK para insertar: {estadisticas['ok']:,}")

# ==================================================
# 6. CARGAR A POSTGRESQL
# ==================================================

print(f"\n💾 Cargando {len(hechos_final):,} registros a FACT_RENTABILIDAD...")

if len(hechos_final) > 0:
    with engine.connect() as conn:
        conn.execute(text('ALTER TABLE "FACT_RENTABILIDAD" ADD COLUMN IF NOT EXISTS "NRO_DOCU" VARCHAR(20)'))
        conn.commit()
    print("   ✅ Columna NRO_DOCU verificada en FACT_RENTABILIDAD")

    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "FACT_RENTABILIDAD" RESTART IDENTITY CASCADE'))
        conn.commit()
    print("   ✅ Tabla limpiada")
    
    # Convertir a DataFrame y cargar
    df_final = pd.DataFrame(hechos_final)
    
    # Cargar en batches
    batch_size = 5000
    for i in range(0, len(df_final), batch_size):
        batch = df_final.iloc[i:i+batch_size]
        batch.to_sql('FACT_RENTABILIDAD', engine, if_exists='append', index=False)
        print(f"   ✅ Batch {i//batch_size + 1}: {len(batch):,} registros")

# ==================================================
# 7. ACTUALIZAR FK_FINANZAS (CORREGIDO - SIN CONDICIÓN FK_UBICACION)
# ==================================================

print("\n" + "=" * 80)
print("🔗 ACTUALIZANDO FK_FINANZAS")
print("=" * 80)

with engine.connect() as conn:
    # CORRECCIÓN: Se eliminó la condición AND fin."FK_Ubicacion" = f."FK_Ubicacion"
    result = conn.execute(text('''
        UPDATE "FACT_RENTABILIDAD" f
        SET "FK_Finanzas" = fin."ID_Finanzas"
        FROM "DIM_FINANZAS" fin
        WHERE fin."Fecha_Referencia" = (
            SELECT t."Fecha" 
            FROM "DIM_TIEMPO" t 
            WHERE t."ID_Tiempo" = f."FK_Tiempo"
        )
    '''))
    conn.commit()
    print(f"   ✅ Registros actualizados: {result.rowcount}")

# ==================================================
# 8. VERIFICACIÓN FINAL
# ==================================================

print("\n" + "=" * 80)
print("✅ VERIFICACIÓN FINAL")
print("=" * 80)

verificacion = pd.read_sql('SELECT COUNT(*) as total FROM "FACT_RENTABILIDAD"', engine)
print(f"📊 Total registros en FACT_RENTABILIDAD: {verificacion['total'][0]:,}")

if verificacion['total'][0] > 0:
    # Verificar FK_Finanzas
    fk_check = pd.read_sql('''
        SELECT 
            COUNT(*) as total,
            COUNT("FK_Finanzas") as con_finanzas,
            COUNT(*) - COUNT("FK_Finanzas") as sin_finanzas
        FROM "FACT_RENTABILIDAD"
    ''', engine)
    print(f"   ✅ Registros con FK_Finanzas: {fk_check['con_finanzas'][0]:,} de {fk_check['total'][0]:,}")
    
    # Mostrar muestra
    muestra = pd.read_sql('''
        SELECT 
            f."Valor_FOB", 
            f."Volumen_Exportado", 
            t."Año", 
            u."Pais_Nombre",
            fin."Tipo_Cambio_USD_PEN"
        FROM "FACT_RENTABILIDAD" f
        JOIN "DIM_TIEMPO" t ON f."FK_Tiempo" = t."ID_Tiempo"
        JOIN "DIM_UBICACION" u ON f."FK_Ubicacion" = u."ID_Ubicacion"
        LEFT JOIN "DIM_FINANZAS" fin ON f."FK_Finanzas" = fin."ID_Finanzas"
        LIMIT 5
    ''', engine)
    
    print("\n📋 Muestra de datos cargados:")
    print(muestra.to_string(index=False))

print("\n" + "=" * 80)
print("🎉 ¡DATA MART COMPLETADO EXITOSAMENTE!")
print("=" * 80)