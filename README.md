# Project BI Course - Palta Hass

Repositorio organizado para el proyecto de Inteligencia de Negocios sobre el análisis de rentabilidad de la palta Hass.

## Estructura

- `src/etl/`: scripts ETL en Python
- `sql/`: script de creación del Data Mart
- `docs/`: documentación académica del proyecto
- `reports/`: entregables y salidas del proyecto
- `assets/`: recursos auxiliares
- `backups/`: copias de respaldo si se necesitan

## Scripts principales

1. `src/etl/ETL_SUNAT_DIMENSIONES.py`
2. `src/etl/Cargar_DIM_FINANZAS.py`
3. `src/etl/ETL_DIM_COSTO.py`
4. `src/etl/ETL_DIM_PAIS_TLC.py`
5. `src/etl/ETL_FACT_RENTABILIDAD.py`
6. `src/etl/ETL_Palta_Hass.py`
7. `src/etl/verificar_dim_finanzas.py`
8. `src/etl/costos_midagri_docs_csv.py`

## Orden recomendado de ejecución

1. Cargar dimensiones desde SUNAT con `ETL_SUNAT_DIMENSIONES.py`
2. Cargar `DIM_FINANZAS` con `Cargar_DIM_FINANZAS.py`
3. Cargar `DIM_COSTO` con `ETL_DIM_COSTO.py`
4. Cargar `DIM_PAIS_TLC` con `ETL_DIM_PAIS_TLC.py`
5. Cargar `FACT_RENTABILIDAD` con `ETL_FACT_RENTABILIDAD.py`
6. Generar KPIs con `ETL_Palta_Hass.py`

## Requisitos

- Python 3.9 o superior
- PostgreSQL
- Paquetes de Python listados en `requirements.txt`

## Notas

- Los archivos `conversation*.json` y otros archivos de trabajo no se consideran parte del repositorio final.
- Los entregables binarios pueden ubicarse en `reports/` si se desea conservarlos en GitHub.
