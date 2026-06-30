-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA public IS 'standard public schema';

-- DROP SEQUENCE public."FACT_RENTABILIDAD_ID_Rentabilidad_seq";

CREATE SEQUENCE public."FACT_RENTABILIDAD_ID_Rentabilidad_seq"
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.dim_costo_id_seq;

CREATE SEQUENCE public.dim_costo_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.dim_finanzas_id_seq;

CREATE SEQUENCE public.dim_finanzas_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.dim_pais_tlc_id_seq;

CREATE SEQUENCE public.dim_pais_tlc_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;-- public."DIM_ADUANA" definition

-- Drop table

-- DROP TABLE public."DIM_ADUANA";

CREATE TABLE public."DIM_ADUANA" (
	"ID_Aduana" int4 NOT NULL, -- Identificador único de la aduana
	"Codigo_Aduana" varchar NULL, -- Código oficial de la aduana - Campo SUNAT: CADUANA
	"Nombre_Aduana" varchar NULL, -- Descripción o nombre de la aduana - Campo SUNAT: ADUA_DESC
	"Region" varchar NULL, -- Región donde se ubica la aduana (Ej. Piura, Callao, Lima)
	"Tipo_Aduana" varchar NULL, -- Tipo de aduana: MARITIMA, TERRESTRE, AEREA
	CONSTRAINT "DIM_ADUANA_pkey" PRIMARY KEY ("ID_Aduana")
);

-- Column comments

COMMENT ON COLUMN public."DIM_ADUANA"."ID_Aduana" IS 'Identificador único de la aduana';
COMMENT ON COLUMN public."DIM_ADUANA"."Codigo_Aduana" IS 'Código oficial de la aduana - Campo SUNAT: CADUANA';
COMMENT ON COLUMN public."DIM_ADUANA"."Nombre_Aduana" IS 'Descripción o nombre de la aduana - Campo SUNAT: ADUA_DESC';
COMMENT ON COLUMN public."DIM_ADUANA"."Region" IS 'Región donde se ubica la aduana (Ej. Piura, Callao, Lima)';
COMMENT ON COLUMN public."DIM_ADUANA"."Tipo_Aduana" IS 'Tipo de aduana: MARITIMA, TERRESTRE, AEREA';


-- public."DIM_COSTO" definition

-- Drop table

-- DROP TABLE public."DIM_COSTO";

CREATE TABLE public."DIM_COSTO" (
	"ID_Costo" int4 DEFAULT nextval('dim_costo_id_seq'::regclass) NOT NULL, -- Identificador único del tipo de costo
	"Tipo_Costo" varchar NULL, -- Clasificación: Producción, Logístico, Operativo
	"Subcategoria" varchar NULL, -- Detalle específico: Labores Culturales, Packing, Flete Terrestre, Servicios Portuarios, Agenciamiento, Certificaciones, Gastos Administrativos
	"Region_Destino" varchar NULL, -- Región de destino: Global, América, Europa, Asia
	"Valor_Unitario_USD" numeric NULL, -- Costo estimado en USD por kilogramo
	"Fecha_Vigencia_Inicio" date NULL, -- Desde cuándo aplica este costo
	"Fecha_Vigencia_Fin" date NULL, -- Hasta cuándo aplica este costo (NULL = vigente actual)
	"Es_Vigente" bool NULL, -- TRUE = registro activo, FALSE = registro histórico
	"Fuente_Estimacion" varchar NULL, -- Fuente de los costos: MIDAGRI / Sierra Exportadora
	CONSTRAINT "DIM_COSTO_pkey" PRIMARY KEY ("ID_Costo")
);

-- Column comments

COMMENT ON COLUMN public."DIM_COSTO"."ID_Costo" IS 'Identificador único del tipo de costo';
COMMENT ON COLUMN public."DIM_COSTO"."Tipo_Costo" IS 'Clasificación: Producción, Logístico, Operativo';
COMMENT ON COLUMN public."DIM_COSTO"."Subcategoria" IS 'Detalle específico: Labores Culturales, Packing, Flete Terrestre, Servicios Portuarios, Agenciamiento, Certificaciones, Gastos Administrativos';
COMMENT ON COLUMN public."DIM_COSTO"."Region_Destino" IS 'Región de destino: Global, América, Europa, Asia';
COMMENT ON COLUMN public."DIM_COSTO"."Valor_Unitario_USD" IS 'Costo estimado en USD por kilogramo';
COMMENT ON COLUMN public."DIM_COSTO"."Fecha_Vigencia_Inicio" IS 'Desde cuándo aplica este costo';
COMMENT ON COLUMN public."DIM_COSTO"."Fecha_Vigencia_Fin" IS 'Hasta cuándo aplica este costo (NULL = vigente actual)';
COMMENT ON COLUMN public."DIM_COSTO"."Es_Vigente" IS 'TRUE = registro activo, FALSE = registro histórico';
COMMENT ON COLUMN public."DIM_COSTO"."Fuente_Estimacion" IS 'Fuente de los costos: MIDAGRI / Sierra Exportadora';


-- public."DIM_EXPORTADOR" definition

-- Drop table

-- DROP TABLE public."DIM_EXPORTADOR";

CREATE TABLE public."DIM_EXPORTADOR" (
	"ID_Exportador" int4 NOT NULL, -- Identificador único del exportador
	"RUC" varchar NULL, -- Número de RUC del exportador - Campo SUNAT: NRO_DOCU
	"Razon_Social" varchar NULL, -- Razón social del exportador - Campo SUNAT: EXPORTADOR
	"Tipo_Empresa" varchar NULL, -- Clasificación: Gran Empresa, MYPE, etc.
	CONSTRAINT "DIM_EXPORTADOR_pkey" PRIMARY KEY ("ID_Exportador")
);

-- Column comments

COMMENT ON COLUMN public."DIM_EXPORTADOR"."ID_Exportador" IS 'Identificador único del exportador';
COMMENT ON COLUMN public."DIM_EXPORTADOR"."RUC" IS 'Número de RUC del exportador - Campo SUNAT: NRO_DOCU';
COMMENT ON COLUMN public."DIM_EXPORTADOR"."Razon_Social" IS 'Razón social del exportador - Campo SUNAT: EXPORTADOR';
COMMENT ON COLUMN public."DIM_EXPORTADOR"."Tipo_Empresa" IS 'Clasificación: Gran Empresa, MYPE, etc.';


-- public."DIM_PRODUCTO" definition

-- Drop table

-- DROP TABLE public."DIM_PRODUCTO";

CREATE TABLE public."DIM_PRODUCTO" (
	"ID_Producto" int4 NOT NULL, -- Identificador único del producto
	"Partida_Arancelaria" varchar NULL, -- Código de partida - Campo SUNAT: CNAN. Filtro: 0804400000 (Palta Hass)
	"Descripcion_Oficial" varchar NULL, -- Descripción comercial oficial (Ej. AGUACATES (PALTAS) FRESCOS O SECOS)
	CONSTRAINT "DIM_PRODUCTO_pkey" PRIMARY KEY ("ID_Producto")
);

-- Column comments

COMMENT ON COLUMN public."DIM_PRODUCTO"."ID_Producto" IS 'Identificador único del producto';
COMMENT ON COLUMN public."DIM_PRODUCTO"."Partida_Arancelaria" IS 'Código de partida - Campo SUNAT: CNAN. Filtro: 0804400000 (Palta Hass)';
COMMENT ON COLUMN public."DIM_PRODUCTO"."Descripcion_Oficial" IS 'Descripción comercial oficial (Ej. AGUACATES (PALTAS) FRESCOS O SECOS)';


-- public."DIM_TIEMPO" definition

-- Drop table

-- DROP TABLE public."DIM_TIEMPO";

CREATE TABLE public."DIM_TIEMPO" (
	"ID_Tiempo" int4 NOT NULL, -- Identificador único de la fecha
	"Fecha" date NULL, -- Fecha completa de embarque - Campo SUNAT: FECHA
	"Año" int4 NULL, -- Año de la exportación
	"Trimestre" int4 NULL, -- Trimestre del año (1-4)
	"Mes" int4 NULL, -- Número de mes (1-12)
	"Mes_Nombre" varchar NULL, -- Nombre del mes (Enero, Febrero, etc.)
	"Semana_Año" int4 NULL, -- Semana del año (1-52)
	CONSTRAINT "DIM_TIEMPO_pkey" PRIMARY KEY ("ID_Tiempo")
);

-- Column comments

COMMENT ON COLUMN public."DIM_TIEMPO"."ID_Tiempo" IS 'Identificador único de la fecha';
COMMENT ON COLUMN public."DIM_TIEMPO"."Fecha" IS 'Fecha completa de embarque - Campo SUNAT: FECHA';
COMMENT ON COLUMN public."DIM_TIEMPO"."Año" IS 'Año de la exportación';
COMMENT ON COLUMN public."DIM_TIEMPO"."Trimestre" IS 'Trimestre del año (1-4)';
COMMENT ON COLUMN public."DIM_TIEMPO"."Mes" IS 'Número de mes (1-12)';
COMMENT ON COLUMN public."DIM_TIEMPO"."Mes_Nombre" IS 'Nombre del mes (Enero, Febrero, etc.)';
COMMENT ON COLUMN public."DIM_TIEMPO"."Semana_Año" IS 'Semana del año (1-52)';


-- public."DIM_UBICACION" definition

-- Drop table

-- DROP TABLE public."DIM_UBICACION";

CREATE TABLE public."DIM_UBICACION" (
	"ID_Ubicacion" int4 NOT NULL, -- Identificador único del país
	"Pais_Codigo" varchar NULL, -- Código de país (CPAIS) - Campo SUNAT: CPAIS
	"Pais_Nombre" varchar NULL, -- Nombre del país destino - Campo SUNAT: PAIS_DESC
	"Continente" varchar NULL, -- Continente al que pertenece el país
	CONSTRAINT "DIM_UBICACION_pkey" PRIMARY KEY ("ID_Ubicacion")
);

-- Column comments

COMMENT ON COLUMN public."DIM_UBICACION"."ID_Ubicacion" IS 'Identificador único del país';
COMMENT ON COLUMN public."DIM_UBICACION"."Pais_Codigo" IS 'Código de país (CPAIS) - Campo SUNAT: CPAIS';
COMMENT ON COLUMN public."DIM_UBICACION"."Pais_Nombre" IS 'Nombre del país destino - Campo SUNAT: PAIS_DESC';
COMMENT ON COLUMN public."DIM_UBICACION"."Continente" IS 'Continente al que pertenece el país';


-- public."DIM_VARIEDAD_CALIDAD" definition

-- Drop table

-- DROP TABLE public."DIM_VARIEDAD_CALIDAD";

CREATE TABLE public."DIM_VARIEDAD_CALIDAD" (
	"ID_Variedad_Calidad" int4 NOT NULL, -- Identificador único de la combinación variedad/calidad
	"Variedad" varchar NULL, -- Variedad del producto. Filtro Regex: HASS
	"Categoria_Calidad" varchar NULL, -- Categoría de calidad: CAT 1, CAT 2, NO_ESPECIFICA
	"Metodo_Produccion" varchar NULL, -- Método de producción: ORGANICO o CONVENCIONAL
	"Fuente_Extraccion" varchar NULL, -- Campo SUNAT de origen (DESC_ADIC / DESC_COM)
	CONSTRAINT "DIM_VARIEDAD_CALIDAD_pkey" PRIMARY KEY ("ID_Variedad_Calidad")
);

-- Column comments

COMMENT ON COLUMN public."DIM_VARIEDAD_CALIDAD"."ID_Variedad_Calidad" IS 'Identificador único de la combinación variedad/calidad';
COMMENT ON COLUMN public."DIM_VARIEDAD_CALIDAD"."Variedad" IS 'Variedad del producto. Filtro Regex: HASS';
COMMENT ON COLUMN public."DIM_VARIEDAD_CALIDAD"."Categoria_Calidad" IS 'Categoría de calidad: CAT 1, CAT 2, NO_ESPECIFICA';
COMMENT ON COLUMN public."DIM_VARIEDAD_CALIDAD"."Metodo_Produccion" IS 'Método de producción: ORGANICO o CONVENCIONAL';
COMMENT ON COLUMN public."DIM_VARIEDAD_CALIDAD"."Fuente_Extraccion" IS 'Campo SUNAT de origen (DESC_ADIC / DESC_COM)';


-- public."FACT_RENTABILIDAD_TEMP_BACKUP" definition

-- Drop table

-- DROP TABLE public."FACT_RENTABILIDAD_TEMP_BACKUP";

CREATE TABLE public."FACT_RENTABILIDAD_TEMP_BACKUP" (
	"CNAN" text NULL,
	"DESCRIP" text NULL,
	"FECHA" timestamp NULL,
	"CADUANA" text NULL,
	"ADUA_DESC" text NULL,
	"CPAIS" text NULL,
	"PAIS_DESC" text NULL,
	"FOB_DOLPOL" int8 NULL,
	"PESO_NETO" int8 NULL,
	"PESO_BRUTO" int8 NULL,
	"UNID_FIQTY" int8 NULL,
	"UNID_FIDES" text NULL,
	"TIPO_DOCU" text NULL,
	"NRO_DOCU" text NULL,
	"PUER_EMBAR" text NULL,
	"EXPORTADOR" text NULL,
	"PUER_DESC" text NULL,
	"DESC_COM" text NULL,
	"DESC_ADIC" text NULL,
	"FEC_NUM" int8 NULL,
	"FEC_REG" int8 NULL,
	"NDCL" text NULL,
	"NDCLREG" text NULL,
	"NUME_SERIE" text NULL,
	"VIA_TRANSP" text NULL,
	"VIAT_DESC" text NULL,
	"CAGE" text NULL,
	"CAGE_DESC" text NULL,
	"CEMPTRA" text NULL,
	"CEMPT_DESC" text NULL,
	"CADUMANIF" text NULL,
	"ANN_MANIF" text NULL,
	"NUM_MANIF" text NULL,
	"PRECIO_PROMEDIO_KG" float8 NULL,
	"ANIO" int4 NULL,
	"MES" int4 NULL,
	"DIA" int4 NULL,
	"TRIMESTRE" int4 NULL,
	"NOMBRE_MES" text NULL
);


-- public.fact_rentabilidad_temp_backup definition

-- Drop table

-- DROP TABLE public.fact_rentabilidad_temp_backup;

CREATE TABLE public.fact_rentabilidad_temp_backup (
	"CNAN" text NULL,
	"DESCRIP" text NULL,
	"FECHA" timestamp NULL,
	"CADUANA" text NULL,
	"ADUA_DESC" text NULL,
	"CPAIS" text NULL,
	"PAIS_DESC" text NULL,
	"FOB_DOLPOL" int8 NULL,
	"PESO_NETO" int8 NULL,
	"PESO_BRUTO" int8 NULL,
	"UNID_FIQTY" int8 NULL,
	"UNID_FIDES" text NULL,
	"TIPO_DOCU" text NULL,
	"NRO_DOCU" text NULL,
	"PUER_EMBAR" text NULL,
	"EXPORTADOR" text NULL,
	"PUER_DESC" text NULL,
	"DESC_COM" text NULL,
	"DESC_ADIC" text NULL,
	"FEC_NUM" int8 NULL,
	"FEC_REG" int8 NULL,
	"NDCL" text NULL,
	"NDCLREG" text NULL,
	"NUME_SERIE" text NULL,
	"VIA_TRANSP" text NULL,
	"VIAT_DESC" text NULL,
	"CAGE" text NULL,
	"CAGE_DESC" text NULL,
	"CEMPTRA" text NULL,
	"CEMPT_DESC" text NULL,
	"CADUMANIF" text NULL,
	"ANN_MANIF" text NULL,
	"NUM_MANIF" text NULL,
	"PRECIO_PROMEDIO_KG" float8 NULL,
	"ANIO" int4 NULL,
	"MES" int4 NULL,
	"DIA" int4 NULL,
	"TRIMESTRE" int4 NULL
);


-- public.kpi_resumen_anual definition

-- Drop table

-- DROP TABLE public.kpi_resumen_anual;

CREATE TABLE public.kpi_resumen_anual (
	"ANIO" int4 NULL,
	total_transacciones int8 NULL,
	fob_total_usd numeric NULL,
	volumen_total_kg numeric NULL,
	precio_promedio_usd_kg numeric NULL,
	total_paises int8 NULL
);


-- public.kpi_resumen_pais_backup definition

-- Drop table

-- DROP TABLE public.kpi_resumen_pais_backup;

CREATE TABLE public.kpi_resumen_pais_backup (
	pais text NULL,
	transacciones int8 NULL,
	fob_total_usd numeric NULL,
	volumen_total_kg numeric NULL,
	precio_promedio_usd_kg numeric NULL
);


-- public."DIM_FINANZAS" definition

-- Drop table

-- DROP TABLE public."DIM_FINANZAS";

CREATE TABLE public."DIM_FINANZAS" (
	"ID_Finanzas" int4 DEFAULT nextval('dim_finanzas_id_seq'::regclass) NOT NULL, -- Identificador único del registro financiero
	"Fecha_Referencia" date NULL, -- Fecha del tipo de cambio (diario)
	"FK_Ubicacion" int4 NULL, -- Llave foránea a DIM_UBICACION
	"Tipo_Cambio_USD_PEN" numeric NULL, -- Tipo de cambio USD/PEN - Fuente: BCRP Serie PD04638PD
	"Arancel_Porcentaje" numeric NULL, -- Arancel aplicable por país destino - Fuente: MINCETUR
	"Acuerdo_TLC" varchar NULL, -- Tratado de Libre Comercio vigente
	"Fuente_BCRP" varchar NULL, -- Fecha de extracción del dato BCRP
	"Fuente_MINCETUR" varchar NULL, -- Versión o fecha de la fuente MINCETUR
	CONSTRAINT "DIM_FINANZAS_pkey" PRIMARY KEY ("ID_Finanzas"),
	CONSTRAINT "DIM_FINANZAS_FK_Ubicacion_fkey" FOREIGN KEY ("FK_Ubicacion") REFERENCES public."DIM_UBICACION"("ID_Ubicacion") DEFERRABLE
);

-- Column comments

COMMENT ON COLUMN public."DIM_FINANZAS"."ID_Finanzas" IS 'Identificador único del registro financiero';
COMMENT ON COLUMN public."DIM_FINANZAS"."Fecha_Referencia" IS 'Fecha del tipo de cambio (diario)';
COMMENT ON COLUMN public."DIM_FINANZAS"."FK_Ubicacion" IS 'Llave foránea a DIM_UBICACION';
COMMENT ON COLUMN public."DIM_FINANZAS"."Tipo_Cambio_USD_PEN" IS 'Tipo de cambio USD/PEN - Fuente: BCRP Serie PD04638PD';
COMMENT ON COLUMN public."DIM_FINANZAS"."Arancel_Porcentaje" IS 'Arancel aplicable por país destino - Fuente: MINCETUR';
COMMENT ON COLUMN public."DIM_FINANZAS"."Acuerdo_TLC" IS 'Tratado de Libre Comercio vigente';
COMMENT ON COLUMN public."DIM_FINANZAS"."Fuente_BCRP" IS 'Fecha de extracción del dato BCRP';
COMMENT ON COLUMN public."DIM_FINANZAS"."Fuente_MINCETUR" IS 'Versión o fecha de la fuente MINCETUR';


-- public."DIM_PAIS_TLC" definition

-- Drop table

-- DROP TABLE public."DIM_PAIS_TLC";

CREATE TABLE public."DIM_PAIS_TLC" (
	"ID_Pais_TLC" int4 DEFAULT nextval('dim_pais_tlc_id_seq'::regclass) NOT NULL, -- Identificador único del acuerdo comercial
	"FK_Ubicacion" int4 NULL, -- Llave foránea a DIM_UBICACION
	"Acuerdo_TLC" varchar NULL, -- Tratado de Libre Comercio vigente con Perú
	"Arancel_Aplicable" numeric NULL, -- Arancel porcentual aplicable (0% para países con TLC)
	"Categoria_Mercado" varchar NULL, -- Clasificación: 'Premium' (TLC + arancel 0%) o 'Estándar'
	CONSTRAINT "DIM_PAIS_TLC_pkey" PRIMARY KEY ("ID_Pais_TLC"),
	CONSTRAINT "DIM_PAIS_TLC_FK_Ubicacion_fkey" FOREIGN KEY ("FK_Ubicacion") REFERENCES public."DIM_UBICACION"("ID_Ubicacion") DEFERRABLE
);

-- Column comments

COMMENT ON COLUMN public."DIM_PAIS_TLC"."ID_Pais_TLC" IS 'Identificador único del acuerdo comercial';
COMMENT ON COLUMN public."DIM_PAIS_TLC"."FK_Ubicacion" IS 'Llave foránea a DIM_UBICACION';
COMMENT ON COLUMN public."DIM_PAIS_TLC"."Acuerdo_TLC" IS 'Tratado de Libre Comercio vigente con Perú';
COMMENT ON COLUMN public."DIM_PAIS_TLC"."Arancel_Aplicable" IS 'Arancel porcentual aplicable (0% para países con TLC)';
COMMENT ON COLUMN public."DIM_PAIS_TLC"."Categoria_Mercado" IS 'Clasificación: ''Premium'' (TLC + arancel 0%) o ''Estándar''';


-- public."FACT_RENTABILIDAD" definition

-- Drop table

-- DROP TABLE public."FACT_RENTABILIDAD";

CREATE TABLE public."FACT_RENTABILIDAD" (
	"ID_Rentabilidad" int4 GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL, -- Identificador único de cada registro - Autogenerado (SERIAL)
	"FK_Tiempo" int4 NULL, -- Llave foránea a DIM_TIEMPO. Asignación desde FECHA (SUNAT)
	"FK_Ubicacion" int4 NULL, -- Llave foránea a DIM_UBICACION. Asignación desde CPAIS/PAIS_DESC (SUNAT)
	"FK_Producto" int4 NULL, -- Llave foránea a DIM_PRODUCTO. Asignación desde CNAN (SUNAT)
	"FK_Variedad_Calidad" int4 NULL, -- Llave foránea a DIM_VARIEDAD_CALIDAD. Asignación desde extracción Regex en DESC_ADIC
	"FK_Exportador" int4 NULL, -- Llave foránea a DIM_EXPORTADOR. Asignación desde NRO_DOCU/EXPORTADOR (SUNAT)
	"FK_Aduana" int4 NULL, -- Llave foránea a DIM_ADUANA. Asignación desde CADUANA/ADUA_DESC (SUNAT)
	"FK_Finanzas" int4 NULL, -- Llave foránea a DIM_FINANZAS. Asignación por fecha y país (BCRP + MINCETUR)
	"FK_Costo" int4 NULL, -- Llave foránea a DIM_COSTO (SCD Tipo 2). Asignación por fecha y región destino
	"Valor_FOB" numeric NULL, -- Valor FOB en dólares estadounidenses - Campo SUNAT: FOB_DOLPOL
	"Volumen_Exportado" numeric NULL, -- Peso neto en kilogramos - Campo SUNAT: PESO_NETO
	"NRO_DOCU" varchar(20) NULL,
	"ITEM" int4 NULL,
	CONSTRAINT "FACT_RENTABILIDAD_pkey" PRIMARY KEY ("ID_Rentabilidad"),
	CONSTRAINT "FACT_RENTABILIDAD_FK_Aduana_fkey" FOREIGN KEY ("FK_Aduana") REFERENCES public."DIM_ADUANA"("ID_Aduana") DEFERRABLE,
	CONSTRAINT "FACT_RENTABILIDAD_FK_Costo_fkey" FOREIGN KEY ("FK_Costo") REFERENCES public."DIM_COSTO"("ID_Costo") DEFERRABLE,
	CONSTRAINT "FACT_RENTABILIDAD_FK_Exportador_fkey" FOREIGN KEY ("FK_Exportador") REFERENCES public."DIM_EXPORTADOR"("ID_Exportador") DEFERRABLE,
	CONSTRAINT "FACT_RENTABILIDAD_FK_Finanzas_fkey" FOREIGN KEY ("FK_Finanzas") REFERENCES public."DIM_FINANZAS"("ID_Finanzas") DEFERRABLE,
	CONSTRAINT "FACT_RENTABILIDAD_FK_Producto_fkey" FOREIGN KEY ("FK_Producto") REFERENCES public."DIM_PRODUCTO"("ID_Producto") DEFERRABLE,
	CONSTRAINT "FACT_RENTABILIDAD_FK_Tiempo_fkey" FOREIGN KEY ("FK_Tiempo") REFERENCES public."DIM_TIEMPO"("ID_Tiempo") DEFERRABLE,
	CONSTRAINT "FACT_RENTABILIDAD_FK_Ubicacion_fkey" FOREIGN KEY ("FK_Ubicacion") REFERENCES public."DIM_UBICACION"("ID_Ubicacion") DEFERRABLE,
	CONSTRAINT "FACT_RENTABILIDAD_FK_Variedad_Calidad_fkey" FOREIGN KEY ("FK_Variedad_Calidad") REFERENCES public."DIM_VARIEDAD_CALIDAD"("ID_Variedad_Calidad") DEFERRABLE
);

-- Column comments

COMMENT ON COLUMN public."FACT_RENTABILIDAD"."ID_Rentabilidad" IS 'Identificador único de cada registro - Autogenerado (SERIAL)';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Tiempo" IS 'Llave foránea a DIM_TIEMPO. Asignación desde FECHA (SUNAT)';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Ubicacion" IS 'Llave foránea a DIM_UBICACION. Asignación desde CPAIS/PAIS_DESC (SUNAT)';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Producto" IS 'Llave foránea a DIM_PRODUCTO. Asignación desde CNAN (SUNAT)';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Variedad_Calidad" IS 'Llave foránea a DIM_VARIEDAD_CALIDAD. Asignación desde extracción Regex en DESC_ADIC';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Exportador" IS 'Llave foránea a DIM_EXPORTADOR. Asignación desde NRO_DOCU/EXPORTADOR (SUNAT)';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Aduana" IS 'Llave foránea a DIM_ADUANA. Asignación desde CADUANA/ADUA_DESC (SUNAT)';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Finanzas" IS 'Llave foránea a DIM_FINANZAS. Asignación por fecha y país (BCRP + MINCETUR)';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."FK_Costo" IS 'Llave foránea a DIM_COSTO (SCD Tipo 2). Asignación por fecha y región destino';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."Valor_FOB" IS 'Valor FOB en dólares estadounidenses - Campo SUNAT: FOB_DOLPOL';
COMMENT ON COLUMN public."FACT_RENTABILIDAD"."Volumen_Exportado" IS 'Peso neto en kilogramos - Campo SUNAT: PESO_NETO';