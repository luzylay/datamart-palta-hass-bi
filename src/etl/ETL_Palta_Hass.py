# SCRIPT ETL V4 - DATA MART PALTA HASS (SOLUCION DEFINITIVA CODIFICACION)
# Versión: 4.0

import pandas as pd
from dbfread import DBF
from sqlalchemy import create_engine, text
import os
from datetime import datetime
import unicodedata

# ==================================================
# CONFIGURACIÓN - ¡CAMBIA TU CONTRASEÑA!
# ==================================================

CARPETA_DATOS = r"C:\Users\Loayza\Downloads\PROYECTO_PALTA_HASS\DATOS_ORIGINALES"

POSTGRES_USUARIO = "postgres"
POSTGRES_CONTRASEÑA = "LLLR123"
POSTGRES_HOST = "localhost"
POSTGRES_PUERTO = "5432"
POSTGRES_DB = "Palta_Hass_DM"

# ==================================================
# FUNCION PARA LIMPIAR TEXTOS (elimina acentos y caracteres raros)
# ==================================================

def limpiar_texto(texto):
    """Elimina acentos y caracteres especiales"""
    if pd.isna(texto):
        return ""
    texto = str(texto)
    # Normalizar y eliminar acentos
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    # Reemplazar caracteres problemáticos
    texto = texto.replace('ñ', 'n').replace('Ñ', 'N')
    # Eliminar cualquier caracter no ASCII
    texto = ''.join([c for c in texto if ord(c) < 128])
    return texto.strip()

# ==================================================
# FUNCION PARA LEER DBF
# ==================================================

def leer_archivo_dbf(ruta_archivo):
    """Lee un archivo DBF"""
    print(f"Leyendo: {os.path.basename(ruta_archivo)}")
    try:
        tabla = DBF(ruta_archivo, encoding='latin-1', ignore_missing_memofile=True)
        df = pd.DataFrame(iter(tabla))
        print(f"  ✓ {len(df)} filas, {len(df.columns)} columnas")
        return df
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None

# ==================================================
# FUNCION PARA TRANSFORMAR DATOS
# ==================================================

def transformar_datos(df, nombre_archivo):
    """Limpia y transforma los datos"""
    
    print(f"Transformando: {nombre_archivo}")
    
    # 1. Renombrar columnas a mayúsculas
    df.columns = [col.upper() for col in df.columns]
    
    # 2. Verificar columnas necesarias
    columnas_necesarias = ['FOB_DOLPOL', 'PESO_NETO', 'FECHA', 'CPAIS', 'PAIS_DESC']
    for col in columnas_necesarias:
        if col not in df.columns:
            print(f"  ✗ Columna faltante: {col}")
            return None
    
    # 3. Eliminar nulos
    filas_antes = len(df)
    df = df.dropna(subset=['FOB_DOLPOL', 'PESO_NETO'])
    print(f"  ✓ Eliminados {filas_antes - len(df)} nulos")
    
    # 4. Filtrar valores positivos
    df = df[(df['FOB_DOLPOL'] > 0) & (df['PESO_NETO'] > 0)]
    
    # 5. Calcular precio promedio
    df['PRECIO_PROMEDIO_KG'] = df['FOB_DOLPOL'] / df['PESO_NETO']
    
    # 6. Convertir fechas (formato YYYYMMDD)
    df['FECHA'] = pd.to_datetime(df['FECHA'].astype(str), format='%Y%m%d', errors='coerce')
    df = df.dropna(subset=['FECHA'])
    
    # 7. Componentes de fecha
    df['ANIO'] = df['FECHA'].dt.year
    df['MES'] = df['FECHA'].dt.month
    df['DIA'] = df['FECHA'].dt.day
    df['TRIMESTRE'] = df['FECHA'].dt.quarter
    
    # 8. LIMPIAR TEXTOS PROBLEMATICOS (¡SOLUCION DEL ERROR 0xf3!)
    print(f"  ✓ Limpiando caracteres especiales...")
    df['PAIS_DESC'] = df['PAIS_DESC'].apply(limpiar_texto)
    df['CPAIS'] = df['CPAIS'].apply(limpiar_texto)
    
    años = sorted(df['ANIO'].unique())
    print(f"  ✓ Años: {años}")
    print(f"  ✓ Filas finales: {len(df)}")
    
    return df

# ==================================================
# FUNCION PARA CARGAR A POSTGRESQL (SIN ERRORES)
# ==================================================

def cargar_a_postgres(df, nombre_tabla):
    """Carga datos a PostgreSQL sin errores de codificacion"""
    
    print(f"\nCargando a PostgreSQL: {nombre_tabla}")
    
    nombre_tabla = nombre_tabla.lower()
    
    url_conexion = f"postgresql://{POSTGRES_USUARIO}:{POSTGRES_CONTRASEÑA}@{POSTGRES_HOST}:{POSTGRES_PUERTO}/{POSTGRES_DB}"
    engine = create_engine(url_conexion)
    
    try:
        # Probar conexion
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("  ✓ Conexion exitosa")
        
        # Convertir TODAS las columnas de texto a string limpio
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).apply(lambda x: limpiar_texto(x))
        
        # Asegurar que no hay NaN en columnas clave
        df = df.fillna(0)
        
        # Cargar datos
        df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)
        print(f"  ✓ Datos cargados")
        
        # Verificar
        with engine.connect() as conn:
            resultado = conn.execute(text(f'SELECT COUNT(*) FROM "{nombre_tabla}"'))
            count = resultado.fetchone()[0]
            print(f"  ✓ Registros: {count}")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

# ==================================================
# FUNCION PARA CREAR KPIs
# ==================================================

def crear_tablas_kpis(nombre_tabla_hechos):
    """Crea tablas resumen con KPIs"""
    
    print("\nCreando tablas de KPIs...")
    
    nombre_tabla_hechos = nombre_tabla_hechos.lower()
    
    url_conexion = f"postgresql://{POSTGRES_USUARIO}:{POSTGRES_CONTRASEÑA}@{POSTGRES_HOST}:{POSTGRES_PUERTO}/{POSTGRES_DB}"
    engine = create_engine(url_conexion)
    
    queries = [
        f"""
        DROP TABLE IF EXISTS kpi_resumen_anual;
        CREATE TABLE kpi_resumen_anual AS
        SELECT 
            ANIO,
            COUNT(*) as total_transacciones,
            ROUND(SUM(FOB_DOLPOL)::numeric, 2) as fob_total_usd,
            ROUND(SUM(PESO_NETO)::numeric, 2) as volumen_total_kg,
            ROUND(AVG(PRECIO_PROMEDIO_KG)::numeric, 4) as precio_promedio_usd_kg,
            COUNT(DISTINCT CPAIS) as total_paises
        FROM "{nombre_tabla_hechos}"
        WHERE ANIO > 2000
        GROUP BY ANIO
        ORDER BY ANIO;
        """,
        f"""
        DROP TABLE IF EXISTS kpi_resumen_pais;
        CREATE TABLE kpi_resumen_pais AS
        SELECT 
            PAIS_DESC as pais,
            COUNT(*) as transacciones,
            ROUND(SUM(FOB_DOLPOL)::numeric, 2) as fob_total_usd,
            ROUND(AVG(PRECIO_PROMEDIO_KG)::numeric, 4) as precio_promedio_usd_kg
        FROM "{nombre_tabla_hechos}"
        GROUP BY PAIS_DESC
        ORDER BY fob_total_usd DESC
        LIMIT 15;
        """
    ]
    
    try:
        with engine.connect() as conn:
            for query in queries:
                conn.execute(text(query))
                conn.commit()
        print("  ✓ KPIs creados")
        
        # Mostrar resultados
        with engine.connect() as conn:
            resultado = conn.execute(text("SELECT * FROM kpi_resumen_anual ORDER BY anio"))
            print("\n  📊 RESULTADOS POR AÑO:")
            print("  " + "-" * 55)
            for row in resultado:
                print(f"    {row[0]}: ${row[4]:.2f}/kg | {row[1]:,} transacciones | ${row[2]:,.0f} FOB")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

# ==================================================
# MAIN
# ==================================================

def main():
    print("=" * 60)
    print("PROCESO ETL V4 - PALTA HASS (CODIFICACION CORREGIDA)")
    print(f"Inicio: {datetime.now()}")
    print("=" * 60)
    
    if not os.path.exists(CARPETA_DATOS):
        print(f"\nERROR: Carpeta no existe")
        return
    
    archivos = [f for f in os.listdir(CARPETA_DATOS) if f.upper().endswith('.DBF')]
    print(f"\nArchivos: {len(archivos)}")
    
    # Procesar archivos
    todos_datos = []
    for archivo in archivos:
        print(f"\n--- {archivo} ---")
        df_raw = leer_archivo_dbf(os.path.join(CARPETA_DATOS, archivo))
        if df_raw is not None:
            df_limpio = transformar_datos(df_raw, archivo)
            if df_limpio is not None and len(df_limpio) > 0:
                todos_datos.append(df_limpio)
    
    if len(todos_datos) == 0:
        print("\nNo se procesó ningún archivo")
        return
    
    # Combinar
    print("\n--- COMBINANDO ---")
    df_final = pd.concat(todos_datos, ignore_index=True)
    print(f"Total registros: {len(df_final):,}")
    print(f"Años: {sorted(df_final['ANIO'].unique())}")
    print(f"Precio promedio: ${df_final['PRECIO_PROMEDIO_KG'].mean():.2f} USD/kg")
    
    # Cargar a PostgreSQL
    if cargar_a_postgres(df_final, "FACT_RENTABILIDAD_TEMP"):
        crear_tablas_kpis("FACT_RENTABILIDAD_TEMP")
    
    print("\n" + "=" * 60)
    print("PROCESO COMPLETADO")
    print("=" * 60)

if __name__ == "__main__":
    main()