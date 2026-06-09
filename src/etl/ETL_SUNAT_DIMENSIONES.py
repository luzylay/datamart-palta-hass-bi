"""
ETL CORREGIDO PARA DIMENSIONES DESDE SUNAT (DBF)
CON MANEJO ADECUADO DE DUPLICADOS Y FILTROS
"""

import os
import re
import pandas as pd
from dbfread import DBF
from sqlalchemy import create_engine, text
from datetime import datetime
from collections import defaultdict

# ==================================================
# CONFIGURACIÓN
# ==================================================

CARPETA_DATOS = r"C:\Users\Loayza\Downloads\PROYECTO_PALTA_HASS\DATOS_ORIGINALES"

POSTGRES_USUARIO = "postgres"
POSTGRES_CONTRASEÑA = "LLLR123"
POSTGRES_HOST = "localhost"
POSTGRES_PUERTO = "5432"
POSTGRES_DB = "Palta_Hass_DM"

# ==================================================
# FUNCIONES DE LIMPIEZA Y VALIDACIÓN
# ==================================================

def limpiar_texto(texto):
    """Limpia texto para evitar errores de codificación"""
    if pd.isna(texto):
        return ""
    texto = str(texto)
    # Eliminar caracteres no ASCII
    texto = ''.join([c for c in texto if ord(c) < 128])
    return texto.strip()

def es_palta_hass(texto):
    """Determina si un registro es palta Hass con criterios amplios"""
    if pd.isna(texto):
        return False
    texto = str(texto).upper()
    
    # Patrones positivos (incluye variantes comunes)
    patrones_hass = [
        r'\bHASS?\b',           # HASS o HAS
        r'\bHAS\b',             # HAS (error común de tipeo)
        r'PALTA.*HASS',         # PALTA HASS
        r'AGUACATE.*HASS',      # AGUACATE HASS
        r'AVOCADO.*HASS',       # AVOCADO HASS
    ]
    
    # Patrones negativos (excluir productos procesados o no comerciales)
    patrones_excluir = [
        r'PULPA',               # Pulpa (producto procesado)
        r'CONGELADO',           # Congelado (procesado)
        r'TROZOS',              # Trozos (procesado)
        r'PROCESAMIENTO',       # Procesado
        r'MUESTRA',             # Muestras sin valor comercial
        r'ACEITE',              # Aceite (derivado)
        r'PURÉ',                # Puré (procesado)
        r'PROCESADO',           # Procesado
        r'HARINA',              # Harina (derivado)
    ]
    
    es_hass = any(re.search(p, texto) for p in patrones_hass)
    es_excluido = any(re.search(p, texto) for p in patrones_excluir)
    
    return es_hass and not es_excluido

def generar_clave_unica(row):
    """Genera clave única usando todos los diferenciadores disponibles."""
    nro_docu = str(row.get('NRO_DOCU', '')).strip()
    fecha = str(row.get('FECHA', '')).strip()
    item = str(row.get('ITEM', '1')).strip()
    cnan = str(row.get('CNAN', '')).strip()
    cpais = str(row.get('CPAIS', '')).strip()
    exportador = str(row.get('EXPORTADOR', '')).strip()[:50]
    caduana = str(row.get('CADUANA', '')).strip()
    via_transp = str(row.get('VIA_TRANSP', '')).strip()
    puer_embar = str(row.get('PUER_EMBAR', '')).strip()
    return f"{nro_docu}|{fecha}|{item}|{cnan}|{cpais}|{exportador}|{caduana}|{via_transp}|{puer_embar}"

def extraer_atributos_descripcion(texto):
    """Extrae variedad, calidad y método de producción usando Regex"""
    if pd.isna(texto):
        texto = ""
    texto = str(texto).upper()
    
    # Variedad (solo HASS)
    variedad = "HASS" if re.search(r'\bHASS?\b', texto) else "NO_DEFINIDO"
    
    # Calidad (CAT 1, CAT 2, etc.)
    if re.search(r'CAT\s*\.?\s*1', texto):
        calidad = "CAT 1"
    elif re.search(r'CAT\s*\.?\s*2', texto):
        calidad = "CAT 2"
    else:
        calidad = "NO_ESPECIFICA"
    
    # Método de producción
    metodo = "ORGANICO" if re.search(r'ORGANIC[OA]', texto) else "CONVENCIONAL"
    
    return variedad, calidad, metodo

# ==================================================
# EXTRACCIÓN DE DBF
# ==================================================

print("=" * 80)
print("📊 ETL CORREGIDO - DIMENSIONES DESDE SUNAT (DBF)")
print("=" * 80)

# Buscar archivos DBF
archivos_dbf = [f for f in os.listdir(CARPETA_DATOS) if f.upper().endswith('.DBF')]
print(f"\n📂 Archivos DBF encontrados: {len(archivos_dbf)}")
for f in archivos_dbf:
    print(f"   - {f}")

# Diccionarios para valores únicos
fechas_unicas = set()
paises_unicos = set()
exportadores_unicos = set()
aduanas_unicas = set()
atributos_unicos = set()

# Listas para estadísticas
stats = {
    'total_leidos': 0,
    'filtro_hass': 0,
    'filtro_nulos': 0,
    'filtro_positivos': 0,
    'duplicados_eliminados': 0,
    'finales': 0,
    'registros_con_item': 0,
    'registros_sin_item': 0
}

hechos = []
claves_vistas = set()

print("\n🔍 Procesando archivos DBF...")

for archivo in archivos_dbf:
    ruta = os.path.join(CARPETA_DATOS, archivo)
    print(f"\n   📄 {archivo}")
    
    try:
        # Leer DBF
        tabla = DBF(ruta, encoding='latin-1', ignore_missing_memofile=True)
        df = pd.DataFrame(iter(tabla))
        stats['total_leidos'] += len(df)
        print(f"      Registros leídos: {len(df):,}")
        
        # Renombrar columnas a mayúsculas para consistencia
        df.columns = [col.upper() for col in df.columns]
        
        # ==========================================
        # MANEJO DE CAMPO ITEM (para duplicados)
        # ==========================================
        tiene_item = 'ITEM' in df.columns
        if tiene_item:
            stats['registros_con_item'] += len(df)
            print(f"      ✓ Campo ITEM encontrado")
            df['ITEM'] = pd.to_numeric(df['ITEM'], errors='coerce').fillna(1).astype(int)
        else:
            stats['registros_sin_item'] += len(df)
            print(f"      ⚠️ Campo ITEM no encontrado. Generando ITEM por orden de aparición...")
            df['ITEM'] = df.groupby(['NRO_DOCU', 'FECHA']).cumcount() + 1
            print(f"      ✓ Generados ITEMs del 1 al {df['ITEM'].max()}")
        
        # ==========================================
        # ELIMINACIÓN DE DUPLICADOS
        # ==========================================
        df['CLAVE_UNICA'] = df.apply(generar_clave_unica, axis=1)
        antes = len(df)
        df = df.drop_duplicates(subset=['CLAVE_UNICA'])
        duplicados = antes - len(df)
        stats['duplicados_eliminados'] += duplicados
        if duplicados > 0:
            print(f"      Eliminados {duplicados} duplicados")
        
        # ==========================================
        # FILTRO DE PRODUCTO (PALTA HASS)
        # ==========================================
        # Buscar en DESC_ADIC y DESC_COM
        df['ES_HASS'] = False
        if 'DESC_ADIC' in df.columns:
            df['ES_HASS'] = df['ES_HASS'] | df['DESC_ADIC'].apply(es_palta_hass)
        if 'DESC_COM' in df.columns:
            df['ES_HASS'] = df['ES_HASS'] | df['DESC_COM'].apply(es_palta_hass)
        
        antes = len(df)
        df = df[df['ES_HASS'] == True]
        stats['filtro_hass'] += (antes - len(df))
        print(f"      Filtro Hass: {antes - len(df):,} registros excluidos")
        
        # ==========================================
        # ELIMINACIÓN DE NULOS EN CAMPOS CRÍTICOS
        # ==========================================
        campos_criticos = ['FOB_DOLPOL', 'PESO_NETO', 'FECHA', 'CPAIS', 'PAIS_DESC']
        antes = len(df)
        df = df.dropna(subset=campos_criticos)
        stats['filtro_nulos'] += (antes - len(df))
        print(f"      Nulos eliminados: {antes - len(df):,}")
        
        # ==========================================
        # FILTRO DE VALORES POSITIVOS
        # ==========================================
        antes = len(df)
        df = df[(df['FOB_DOLPOL'] > 0) & (df['PESO_NETO'] > 0)]
        stats['filtro_positivos'] += (antes - len(df))
        print(f"      Valores no positivos: {antes - len(df):,}")
        
        # ==========================================
        # FILTRO DE AÑOS (2016-2024)
        # ==========================================
        df['FECHA_DT'] = pd.to_datetime(df['FECHA'].astype(str), format='%Y%m%d', errors='coerce')
        df = df.dropna(subset=['FECHA_DT'])
        df = df[(df['FECHA_DT'].dt.year >= 2016) & (df['FECHA_DT'].dt.year <= 2024)]
        
        stats['finales'] += len(df)
        print(f"      ✅ Registros válidos finales: {len(df):,}")
        
        if len(df) == 0:
            continue
        
        # ==========================================
        # PROCESAR VALORES ÚNICOS PARA DIMENSIONES
        # ==========================================
        # Limpiar textos
        df['PAIS_DESC'] = df['PAIS_DESC'].apply(limpiar_texto)
        df['CPAIS'] = df['CPAIS'].apply(limpiar_texto)
        
        if 'NRO_DOCU' in df.columns:
            df['NRO_DOCU'] = df['NRO_DOCU'].apply(limpiar_texto)
        if 'EXPORTADOR' in df.columns:
            df['EXPORTADOR'] = df['EXPORTADOR'].apply(limpiar_texto)
        if 'CADUANA' in df.columns:
            df['CADUANA'] = df['CADUANA'].apply(limpiar_texto)
        if 'ADUA_DESC' in df.columns:
            df['ADUA_DESC'] = df['ADUA_DESC'].apply(limpiar_texto)
        
        # Fechas únicas
        for fecha in df['FECHA_DT'].dt.date.unique():
            fechas_unicas.add(fecha)
        
        # Países únicos
        for _, row in df.iterrows():
            if row['CPAIS'] and row['PAIS_DESC']:
                paises_unicos.add((row['CPAIS'], row['PAIS_DESC']))
        
        # Exportadores únicos
        if 'NRO_DOCU' in df.columns and 'EXPORTADOR' in df.columns:
            for _, row in df.iterrows():
                if row['NRO_DOCU'] and row['EXPORTADOR']:
                    exportadores_unicos.add((row['NRO_DOCU'], row['EXPORTADOR']))
        
        # Aduanas únicas
        if 'CADUANA' in df.columns and 'ADUA_DESC' in df.columns:
            for _, row in df.iterrows():
                if row['CADUANA'] and row['ADUA_DESC']:
                    aduanas_unicas.add((row['CADUANA'], row['ADUA_DESC']))
        
        # Atributos de calidad desde DESC_ADIC
        if 'DESC_ADIC' in df.columns:
            df['DESC_ADIC'] = df['DESC_ADIC'].fillna('').apply(limpiar_texto)
            for _, row in df.iterrows():
                variedad, calidad, metodo = extraer_atributos_descripcion(row['DESC_ADIC'])
                if variedad != "NO_DEFINIDO":
                    atributos_unicos.add((variedad, calidad, metodo))
        
        # ==========================================
        # PREPARAR DATOS PARA HECHOS
        # ==========================================
        for _, row in df.iterrows():
            hechos.append({
                'fecha': row['FECHA_DT'].date(),
                'anio': row['FECHA_DT'].year,
                'mes': row['FECHA_DT'].month,
                'pais_codigo': row['CPAIS'],
                'pais_nombre': row['PAIS_DESC'],
                'ruc': row.get('NRO_DOCU', ''),
                'exportador': row.get('EXPORTADOR', ''),
                'aduana_codigo': row.get('CADUANA', ''),
                'aduana_nombre': row.get('ADUA_DESC', ''),
                'desc_adic': row.get('DESC_ADIC', ''),
                'valor_fob': float(row['FOB_DOLPOL']),
                'volumen_kg': float(row['PESO_NETO'])
            })
        
    except Exception as e:
        print(f"      ✗ Error procesando: {e}")
        import traceback
        traceback.print_exc()

# ==================================================
# ESTADÍSTICAS DE FILTRADO
# ==================================================

print("\n" + "=" * 80)
print("📊 ESTADÍSTICAS DE FILTRADO")
print("=" * 80)
print(f"   Total registros leídos: {stats['total_leidos']:,}")
print(f"   Registros con campo ITEM: {stats['registros_con_item']:,}")
print(f"   Registros sin campo ITEM: {stats['registros_sin_item']:,}")
print(f"   Duplicados eliminados: {stats['duplicados_eliminados']:,}")
print(f"   Filtro Hass (excluidos): {stats['filtro_hass']:,}")
print(f"   Filtro nulos (excluidos): {stats['filtro_nulos']:,}")
print(f"   Filtro valores positivos (excluidos): {stats['filtro_positivos']:,}")
print(f"   Registros finales: {stats['finales']:,}")
if stats['total_leidos'] > 0:
    print(f"   Porcentaje de retención: {(stats['finales']/stats['total_leidos']*100):.1f}%")

print(f"\n✅ Resumen de extracción para dimensiones:")
print(f"   - Fechas únicas: {len(fechas_unicas):,}")
print(f"   - Países únicos: {len(paises_unicos)}")
print(f"   - Exportadores únicos: {len(exportadores_unicos)}")
print(f"   - Aduanas únicas: {len(aduanas_unicas)}")
print(f"   - Atributos de calidad: {len(atributos_unicos)}")
print(f"   - Registros para hechos: {len(hechos):,}")

# ==================================================
# POBLAR DIM_TIEMPO
# ==================================================

print("\n" + "=" * 80)
print("📋 POBLANDO DIM_TIEMPO")
print("=" * 80)

conn_url = f"postgresql://{POSTGRES_USUARIO}:{POSTGRES_CONTRASEÑA}@{POSTGRES_HOST}:{POSTGRES_PUERTO}/{POSTGRES_DB}"
engine = create_engine(conn_url)

# Limpiar tabla
with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_TIEMPO" RESTART IDENTITY CASCADE'))
    conn.commit()
print("   ✅ Tabla limpiada")

# Preparar datos
tiempo_data = []
for fecha in sorted(fechas_unicas):
    dt = datetime.combine(fecha, datetime.min.time())
    tiempo_data.append({
        'ID_Tiempo': int(fecha.strftime('%Y%m%d')),
        'Fecha': fecha,
        'Año': dt.year,
        'Trimestre': (dt.month - 1) // 3 + 1,
        'Mes': dt.month,
        'Mes_Nombre': dt.strftime('%B'),
        'Semana_Año': dt.isocalendar()[1]
    })

df_tiempo = pd.DataFrame(tiempo_data)
df_tiempo.to_sql('DIM_TIEMPO', engine, if_exists='append', index=False)
print(f"   ✅ {len(df_tiempo)} registros insertados")

# ==================================================
# POBLAR DIM_UBICACION
# ==================================================

print("\n" + "=" * 80)
print("📋 POBLANDO DIM_UBICACION")
print("=" * 80)

with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_UBICACION" RESTART IDENTITY CASCADE'))
    conn.commit()
print("   ✅ Tabla limpiada")

ubicacion_data = []
for i, (codigo, nombre) in enumerate(sorted(paises_unicos), 1):
    ubicacion_data.append({
        'ID_Ubicacion': i,
        'Pais_Codigo': codigo,
        'Pais_Nombre': nombre,
        'Continente': None  # Se puede actualizar después manualmente
    })

if ubicacion_data:
    df_ubicacion = pd.DataFrame(ubicacion_data)
    df_ubicacion.to_sql('DIM_UBICACION', engine, if_exists='append', index=False)
    print(f"   ✅ {len(df_ubicacion)} registros insertados")
else:
    print("   ⚠️ No hay datos para insertar")

# ==================================================
# POBLAR DIM_EXPORTADOR
# ==================================================

print("\n" + "=" * 80)
print("📋 POBLANDO DIM_EXPORTADOR")
print("=" * 80)

with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_EXPORTADOR" RESTART IDENTITY CASCADE'))
    conn.commit()
print("   ✅ Tabla limpiada")

exportador_data = []
for i, (ruc, nombre) in enumerate(sorted(exportadores_unicos), 1):
    exportador_data.append({
        'ID_Exportador': i,
        'RUC': ruc[:15] if len(ruc) > 15 else ruc,
        'Razon_Social': nombre[:200] if len(nombre) > 200 else nombre,
        'Tipo_Empresa': None
    })

if exportador_data:
    df_exportador = pd.DataFrame(exportador_data)
    df_exportador.to_sql('DIM_EXPORTADOR', engine, if_exists='append', index=False)
    print(f"   ✅ {len(df_exportador)} registros insertados")
else:
    print("   ⚠️ No hay datos para insertar")

# ==================================================
# POBLAR DIM_ADUANA
# ==================================================

print("\n" + "=" * 80)
print("📋 POBLANDO DIM_ADUANA")
print("=" * 80)

with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_ADUANA" RESTART IDENTITY CASCADE'))
    conn.commit()
print("   ✅ Tabla limpiada")

aduana_data = []
for i, (codigo, nombre) in enumerate(sorted(aduanas_unicas), 1):
    aduana_data.append({
        'ID_Aduana': i,
        'Codigo_Aduana': codigo[:10] if len(codigo) > 10 else codigo,
        'Nombre_Aduana': nombre[:100] if len(nombre) > 100 else nombre,
        'Region': None,
        'Tipo_Aduana': None
    })

if aduana_data:
    df_aduana = pd.DataFrame(aduana_data)
    df_aduana.to_sql('DIM_ADUANA', engine, if_exists='append', index=False)
    print(f"   ✅ {len(df_aduana)} registros insertados")
else:
    print("   ⚠️ No hay datos para insertar")

# ==================================================
# POBLAR DIM_PRODUCTO (fijo)
# ==================================================

print("\n" + "=" * 80)
print("📋 POBLANDO DIM_PRODUCTO")
print("=" * 80)

with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_PRODUCTO" RESTART IDENTITY CASCADE'))
    conn.commit()

producto_data = pd.DataFrame([{
    'ID_Producto': 1,
    'Partida_Arancelaria': '0804400000',
    'Descripcion_Oficial': 'AGUACATES (PALTAS) FRESCOS O SECOS'
}])
producto_data.to_sql('DIM_PRODUCTO', engine, if_exists='append', index=False)
print(f"   ✅ 1 registro insertado")

# ==================================================
# POBLAR DIM_VARIEDAD_CALIDAD
# ==================================================

print("\n" + "=" * 80)
print("📋 POBLANDO DIM_VARIEDAD_CALIDAD")
print("=" * 80)

with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE "DIM_VARIEDAD_CALIDAD" RESTART IDENTITY CASCADE'))
    conn.commit()
print("   ✅ Tabla limpiada")

calidad_data = []
for i, (variedad, calidad, metodo) in enumerate(sorted(atributos_unicos), 1):
    calidad_data.append({
        'ID_Variedad_Calidad': i,
        'Variedad': variedad,
        'Categoria_Calidad': calidad,
        'Metodo_Produccion': metodo,
        'Fuente_Extraccion': 'Extraído de DESC_ADIC/DESC_COM con Regex'
    })

if calidad_data:
    df_calidad = pd.DataFrame(calidad_data)
    df_calidad.to_sql('DIM_VARIEDAD_CALIDAD', engine, if_exists='append', index=False)
    print(f"   ✅ {len(df_calidad)} registros insertados")
else:
    # Insertar un registro por defecto
    calidad_default = pd.DataFrame([{
        'ID_Variedad_Calidad': 1,
        'Variedad': 'HASS',
        'Categoria_Calidad': 'NO_ESPECIFICA',
        'Metodo_Produccion': 'CONVENCIONAL',
        'Fuente_Extraccion': 'Valor por defecto'
    }])
    calidad_default.to_sql('DIM_VARIEDAD_CALIDAD', engine, if_exists='append', index=False)
    print(f"   ✅ 1 registro por defecto insertado")

# ==================================================
# RESUMEN FINAL
# ==================================================

print("\n" + "=" * 80)
print("✅ ETL COMPLETADO EXITOSAMENTE")
print("=" * 80)

print("\n📊 TABLAS POBLADAS:")
print(f"   DIM_TIEMPO: {len(df_tiempo)} registros")
print(f"   DIM_UBICACION: {len(ubicacion_data)} registros")
print(f"   DIM_EXPORTADOR: {len(exportador_data)} registros")
print(f"   DIM_ADUANA: {len(aduana_data)} registros")
print(f"   DIM_PRODUCTO: 1 registro")
print(f"   DIM_VARIEDAD_CALIDAD: {len(calidad_data) if calidad_data else 1} registros")
print(f"   HECHOS preparados: {len(hechos):,} registros (pendientes de carga a FACT_RENTABILIDAD)")

print("\n" + "=" * 80)
print("🎉 ¡ETL CORREGIDO COMPLETADO!")
print("📌 NOTA: FACT_RENTABILIDAD aún no se ha poblado. Se necesita cruzar con DIM_FINANZAS, DIM_COSTO, etc.")
print("=" * 80)