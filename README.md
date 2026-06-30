# Project BI Course - Palta Hass

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?logo=powerbi&logoColor=black)

Repositorio organizado para el proyecto de Inteligencia de Negocios sobre el análisis de rentabilidad de la palta Hass.

## Estructura

- `src/etl/`: scripts ETL en Python
- `src/analysis/`: scripts analíticos (validaciones DAX, estacionalidad, etc.)
- `src/utils/`: scripts auxiliares para manejo de documentos PDF/Word
- `sql/`: script de creación del Data Mart y modelos relacionales
- `docs/`: documentación académica del proyecto y diccionarios de datos
- `reports/`: entregables finales, documentos formales y plantillas de Power BI
- `data/raw/`: archivos Excel y CSV de origen (ignorados en git por su peso)
- `assets/`: recursos auxiliares (imágenes, logos)
- `backups/`: copias de respaldo de base de datos (ignorados en git)

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
