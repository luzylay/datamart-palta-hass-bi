UNIVERSIDAD TECNOLÓGICA DEL PERÚ

GRUPO 01

Creación de un Data Mart para el análisis de la rentabilidad potencial de la
palta Hass para la empresa Peruvian Andean Trout S.A.C., con sede en
Huancavelica, período 2016–2024

TRABAJO DE INVESTIGACIÓN DE LA ASIGNATURA
Inteligencia de Negocios (25534)

Presentado por:
Cardenas Gutierrez, Cristian Paul — U22100292
Choy Sanchez Tejada, David Augusto — U21320903
Guillena Oria, Bruno Fabian — U20221432
Loayza Rodriguez, Lady Luz — U22221489
Moreno Calderon, Francis Alonso Jesus — U22212542
Salvador Soto, Jeampieer's Jeahison — U22240560

Docente:
José Adrián Núñez Huerta

Lima, Perú
Mayo, 2026

2

ÍNDICE DE CONTENIDOS

1. INTRODUCCIÓN..................................................................................................................... 3
1.1 Reseña Histórica de la Empresa...........................................................................................3
1.2 Contexto del Problema.........................................................................................................3
1.3 Objetivo General del Proyecto.............................................................................................6
1.4 Alcance del Proyecto........................................................................................................... 7
1.5 Metodología Hefesto............................................................................................................9
1.6 Estructura del Data Mart Actual........................................................................................ 11
1.7 Preguntas de Negocio que Responde el Data Mart............................................................13
2. MARCO TEÓRICO................................................................................................................ 14
2.1 Datos, Información y Sistemas de Información.................................................................14
2.2 Inteligencia de Negocios (Business Intelligence).............................................................. 15
2.3 Modelamiento Dimensional y Esquema Copo de Nieve................................................... 16
2.4 Procesos ETL..................................................................................................................... 17
2.5 KPIs e Indicadores de Rendimiento...................................................................................19
3. ANÁLISIS DEL CASO........................................................................................................... 26
3.1 Descripción del Negocio....................................................................................................26
3.2 Requerimientos del Negocio..............................................................................................28
3.3 KPIs Relevantes................................................................................................................. 31
3.4 Fuentes de Datos................................................................................................................ 39
3.5 Requerimientos Funcionales y No Funcionales.................................................................40
4. DISEÑO DE ARQUITECTURA DE INTELIGENCIA DE NEGOCIOS......................... 51
4.1 Tipo de Arquitectura Propuesta......................................................................................... 51
4.2 Justificación de la Arquitectura......................................................................................... 52
4.3 Componentes de la Arquitectura........................................................................................54
5. MODELAMIENTO DIMENSIONAL...................................................................................57
5.1 Tabla de Hechos: FACT_RENTABILIDAD..................................................................... 57
5.2 Tablas de Dimensiones...................................................................................................... 58
5.3 Relaciones entre Tablas......................................................................................................63
6. PROCESOS ETL..................................................................................................................... 66
6.1 Entorno de Desarrollo (IDE)..............................................................................................66
6.2 Fase de Extracción............................................................................................................. 70
6.3 Fase de Transformación..................................................................................................... 72
6.4 Fase de Carga..................................................................................................................... 74
6.5 Proceso de Normalización de Datos (1NF → 5NF).......................................................... 76
7. CONCLUSIONES................................................................................................................... 85
8. REFERENCIAS.......................................................................................................................86

3

1. INTRODUCCIÓN

1.1 Reseña Histórica de la Empresa

Peruvian  Andean  Trout  S.A.C.  es  una  empresa  peruana  constituida  como  Sociedad  Anónima
Cerrada, cuyo RUC es 20568513216 y su condición es ACTIVO y HABIDO . La empresa inició
operaciones oficialmente el 15 de noviembre de 2012 y su actividad principal es la acuicultura de
agua dulce (CIIU: 0322) . Su centro de operaciones está ubicado en la Comunidad Campesina de
Choclococha,  en  el  distrito  de  Santa  Ana,  provincia  de  Castrovirreyna,  en  la  región
Huancavelica, a más de 4,500 metros sobre el nivel del mar.

La  empresa  inició  un  proceso  de diversificación hacia el sector agroexportador. Como parte de
este proceso, solicitó un análisis basado en inteligencia de negocios para evaluar la viabilidad de
invertir  en  palta  Hass,  utilizando  datos  del  mercado  de  exportación  peruano  del  período
2016–2024.

1.2 Contexto del Problema

La empresa Peruvian Andean Trout S.A.C. no cuenta actualmente con información estructurada
que  le  permita  evaluar  la  rentabilidad  de  la  palta Hass como potencial nueva línea de negocio.
Los  datos  disponibles  en  fuentes  públicas  presentan  limitaciones significativas que impiden un
análisis financiero completo y confiable.

Limitaciones de los datos disponibles

Limitación

Descripción

Impacto en el análisis

Datos dispersos

Los  microdatos  de  exportación  de  la
SUNAT  se  encuentran  distribuidos  en
múltiples
formatos
con
heterogéneos (DBF, TXT).

archivos

Dificultad  para
integrar  y
analizar información histórica
de manera eficiente.

Sin costos reales

La  SUNAT  no  registra  los  costos  de
producción, empaque o logística de las
exportaciones.

Imposibilidad  de  calcular
rentabilidad
de
márgenes
reales.

Sin tipo de cambio

Los  registros  de
la  SUNAT  solo
incluyen valores en dólares americanos
(USD), sin el tipo de cambio asociado.

El  análisis  de  rentabilidad en
soles  (moneda  local)  resulta
incompleto.

Sin aranceles

No  se  registran  los  aranceles  pagados
por país destino.

Ruido semántico

de

descripción
Los
campos
(DESC_ADIC,
DESC_COM)
contienen  términos  como  "muestras",
"pulpa",
o
"procesamiento".

"congelado"

4

No  es  posible  calcular  el
margen  neto  ajustado,  que
considera  los  impuestos  de
importación.

del

Distorsión
precio
promedio  FOB/kg  real  de  la
palta Hass fresca.

Justificación de la serie temporal (2016–2024)

El  período  de  análisis  comprende  los  años  2016  a  2024.  Sin  embargo,  se han identificado dos
años sin datos aptos para el análisis, lo cual requiere una justificación metodológica:

Análisis de Causa-Raíz (Diagrama de Ishikawa)

A continuación, se presenta el diagrama de Ishikawa que identifica las causas raíz del problema
central:  "La  empresa  no  cuenta  con  información  estructurada para evaluar la rentabilidad de la
palta Hass".

Causas identificadas:

Categoría

Causa

Efecto

Datos

Datos

Datos

Procesos

Procesos

Personas

Datos  SUNAT  dispersos  en
múltiples archivos (DBF/TXT)

Dificultad
información histórica

para

integrar  y

analizar

Falta  de  información  de  costos
reales de producción

Imposibilidad  de  calcular  márgenes  de
rentabilidad reales

Ausencia  de  tipo  de  cambio  y
aranceles en registros SUNAT

Análisis  de  rentabilidad  incompleto  (solo
en USD)

No  existe  un  proceso  ETL
automatizado

Los  datos  no  se  limpian  ni  transforman
consistentemente

Falta de un modelo dimensional
de datos

No  se  puede  segmentar  el  análisis  por
múltiples dimensiones

Limitada  experiencia  previa  en
agroexportación de palta

Desconocimiento  de  los  KPIs  clave  del
sector

Tecnología

No  hay  un  Data  Mart  para
análisis histórico

Cada  análisis
manual desde cero

requiere  procesamiento

Diagrama Ishikawa:

5

Solución propuesta: El Data Mart desarrollado en este proyecto aborda cada una de las causas
identificadas.

Causa identificada

Solución implementada en el Data Mart

Datos  dispersos  en  múltiples
archivos

Se  integran  en  un  modelo  único  tipo  Copo  de  Nieve
(Snowflake Schema)

Ausencia  de  costos  reales  de
producción

Se  estiman  mediante  valores  de  referencia  de  Sierra
Exportadora y MIDAGRI

Falta  de
(USD/PEN)

tipo  de  cambio

Se incorpora la serie histórica del Banco Central de Reserva
del Perú (BCRP)

Ausencia de aranceles por país
destino

Se  integra  información  de acuerdos comerciales y aranceles
del MINCETUR

6

existe

No
automatizado

proceso  ETL

Se  implementa  un  proceso  automatizado  en  Python  con
librerías especializadas

Falta  de  modelo  dimensional
de datos

Se  diseña un modelo Copo de Nieve con tablas de hechos y
dimensiones

Desconocimiento  de  KPIs  del
sector

Se  definen  KPIs  específicos  para  el  sector  agroexportador
(ver sección 3.3)

1.3 Objetivo General del Proyecto

Desarrollar  un  Data Mart que permita analizar la rentabilidad potencial de la palta Hass para la
empresa  Peruvian  Andean  Trout  S.A.C.,  mediante  la  integración  y  transformación  de  los
microdatos  de  exportación  de  la  SUNAT  correspondientes  al período 2016–2024, enriquecidos
con fuentes externas de tipo de cambio (BCRP), acuerdos comerciales y aranceles (MINCETUR)
y  costos  referenciales  (MIDAGRI/Sierra  Exportadora),  como  base  para  la  toma  de  decisiones
estratégicas sobre diversificación.

Objetivos Específicos

N°

Objetivo Específico

¿Qué se entregará?

1

2

3

4

Diseñar  un  modelo  dimensional  orientado  al
análisis de la rentabilidad potencial de la palta
Hass.

Un  modelo  lógico  tipo  Copo de Nieve
(Snowflake  Schema)  con
tabla  de
hechos y dimensiones.

Filtrar  los  registros  de  SUNAT  para  incluir
exclusivamente  la  variedad  Hass  y  excluir
pulpa, congelados y productos procesados.

Un script de limpieza y transformación
que  asegure  datos  válidos  para  el
análisis.

Calcular en el Data Mart las métricas clave de
total
rentabilidad:  precio  FOB/kg,  costo
estimado,  margen  de  utilidad  estimado,  ratio
de
de
concentración  por  destino,  índice  HHI  por
exportador y margen neto ajustado.

rentabilidad

estimado,

índice

Identificar  los  mercados  de  destino  (países  y
continentes) con mayor rentabilidad potencial,
utilizando
de
aranceles  y  acuerdos comerciales proveniente
de MINCETUR.

información

referencial

de

hechos
Una
tabla
poblada
(FACT_RENTABILIDAD)
con  las  métricas  base  (valor  FOB  y
volumen), mientras que los indicadores
derivados  se  calculan  en  la  capa  de
visualización.

Una  subdimensión  (DIM_PAIS_TLC)
los  mercados  como
que  clasifique
"Premium"  (con  TLC  y  arancel  0%) o
"Estándar".

7

5

6

Evaluar  la  concentración  del  mercado  entre
los  exportadores  peruanos  (índice  HHI)  y  la
eficiencia por aduana de salida.

Reportes que permitan conocer el nivel
de  competencia  en  el  mercado  y
optimizar rutas logísticas.

Generar  reportes  en  Power  BI  para
la
Gerencia  General,  Planeamiento  Estratégico,
Finanzas y Comercio Exterior.

Dashboards  interactivos  con  los  KPIs
clave para la toma de decisiones.

1.4 Alcance del Proyecto

El presente proyecto abarca el análisis del período 2016–2024, centrado en la partida arancelaria
0804400000  correspondiente  a  la  palta  Hass.  La  fuente  de  datos primaria está conformada por
los registros de exportación disponibles en el portal ADUANET de la SUNAT.

Fuentes de datos utilizadas

Fuente

Datos proporcionados

Uso en el proyecto

SUNAT
(ADUANET)

BCRP

MINCETUR

Valor  FOB,  volumen  exportado
(peso  neto),  país  destino,  RUC  del
exportador, aduana de salida

Base  transaccional  del  Data
Mart

Serie  histórica  de  tipo  de  cambio
(USD/PEN) diario 2016-2024

Conversión  de  rentabilidad  a
soles (moneda local)

Aranceles
acuerdos
información de puertos

país
por
comerciales

destino,
(TLC),

Identificación  de  mercados
"Premium"

MIDAGRI
Exportadora

/  Sierra

Costos referenciales de producción,
empaque y logística por región

Indicadores que se construirán

total
Cálculo
estimado y margen de utilidad

costo

del

A  partir  de  las  variables  principales  (valor FOB, volumen exportado y mercado de destino), se
construirán los siguientes indicadores:

Indicador

Fórmula

Fuentes involucradas

Precio  promedio  por
kilogramo

Valor FOB ÷ Peso Neto

SUNAT

Costo total estimado

Σ  (Valor unitario de referencia
× Volumen exportado)

DIM_COSTO  (MIDAGRI/Sierra
Exportadora)

8

Margen
estimado

de  utilidad

Ingreso  FOB  –  Costo  total
estimado

SUNAT + DIM_COSTO

Ratio  de  rentabilidad
estimado

(Margen  ÷  Ingreso  FOB)  ×
100%

SUNAT + DIM_COSTO

Margen  neto  ajustado
(soles)

(Ingreso  FOB  ×  TC)  –  Costo
total – Aranceles

SUNAT + BCRP + MINCETUR

Nota: El análisis tiene un enfoque referencial, basado en información del mercado de exportación
peruano y en costos referenciales, no en datos operativos internos de la empresa. Los resultados
constituyen una aproximación para evaluar la rentabilidad potencial.

Limitaciones del alcance y soluciones implementadas

Limitación

Solución implementada

Los  registros  de  SUNAT  no  incluyen
información de costos reales

Se  utiliza  DIM_COSTO  con  valores  de  referencia
de MIDAGRI/Sierra Exportadora.

Los  registros  de  SUNAT  no  incluyen
tipo de cambio

Se  integra  la  serie  histórica  del  BCRP  (tipo  de
cambio USD/PEN).

Los  registros  de  SUNAT  no  incluyen
aranceles pagados

La información de aranceles y acuerdos comerciales
(MINCETUR)  se  incorpora  en  la  subdimensión
DIM_PAIS_TLC como dato referencial.

Ausencia  de  datos  útiles  para  2016  y
2019

Justificación  metodológica  documentada  en
sección 1.2.

la

Qué queda expresamente fuera del alcance

●  La implementación de sistemas en tiempo real.
●  La integración con sistemas internos de la empresa (como ERP).
●  La inclusión de variables externas como costos logísticos reales, costos de producción

específicos de la empresa o factores productivos internos.

●  La consulta directa a APIs de SUNAT en tiempo real (la extracción se basa en archivos

descargados).

Beneficiarios directos

Beneficiario

Rol en la toma de decisiones

Gerencia General

Decisor  estratégico.  Aprueba  o  rechaza la inversión basándose
en los resultados.

9

Planeamiento Estratégico

Evalúa mercados y concentración de riesgo.

Finanzas

Valida márgenes y rentabilidad potencial.

Comercio Exterior

Asesora sobre destinos, costos logísticos y competidores.

1.5 Metodología Hefesto
La  construcción  del  Data  Mart  se  guió  por  la  Metodología  Hefesto,  adaptada  al  contexto  de
Peruvian Andean Trout S.A.C. A continuación, se documentan las decisiones clave en cada fase:

●  Fase 1 - Análisis de Requerimientos

Se  partió  de  la  pregunta  central:  "¿Cuál  es  el nivel de rentabilidad potencial de la palta
Hass (2016-2024)?"
De  esta  pregunta  derivaron  7  preguntas  analíticas  de  soporte  (listadas  en  1.7),  que
definieron los KPIs críticos:

KPI

Meta esperada

Justificación

Precio FOB/kg

Variable por destino

Identificar mercados premium

Ratio de Rentabilidad  > 15% - 25%

Índice HHI

< 2500

Estándar
Exportadora

sectorial

según  Sierra

Mercado
concentrado)

competitivo

(no

Margen
Ajustado

Neto

Positivo

Rentabilidad real considerando tipo de
cambio

Decisión clave: Si el análisis resultara desfavorable, la misma estructura permite evaluar
otro  producto  cambiando  únicamente  el  filtro  de  partida arancelaria en la dimensión de
producto.

●  Fase 2 - Análisis de Fuentes de Datos

Se  evaluaron  cuatro  fuentes  de  datos.  Se  identificó  que  SUNAT  (ADUANET)  no
proporciona costos reales, tipo de cambio ni aranceles, limitaciones críticas para calcular
rentabilidad.

Fuente

Datos
proporcionados

Limitación identificada

Solución

10

SUNAT
(ADUANET)

Valor  FOB, volumen,
destino, exportador

No  incluye  costos,  tipo
de cambio ni aranceles

Incorporación  de
fuentes externas

BCRP

de
Tipo
histórico USD/PEN

cambio

Dato  macroeconómico,
no transaccional

MINCETUR

Aranceles,  acuerdos
TLC, puertos

Información estática

/

MIDAGRI
Sierra
Exportadora

Costos  de  referencia
(producción,
empaque, logística)

Valores  estimados,  no
reales de la empresa

vía

Integración
dimensión
financiera

Pobla
subdimensión  de
acuerdos
comerciales

Dimensión
costos
historial
Tipo 2)

de
con
(SCD

●  Fase 3 - Modelo Lógico de Datos

Se  diseñó  un  esquema  de  Copo  de  Nieve  (Snowflake  Schema)  con  las  siguientes
características:

Característica

Descripción

Tabla de hechos

FACT_RENTABILIDAD
atómicos (Valor_FOB, Volumen_Exportado)

almacena

únicamente

hechos

Métricas derivadas

Se  calculan  en  Power  BI  (no  en  la  tabla  de  hechos)  para
garantizar consistencia

Granularidad

Fina:  un  registro  por  ítem  dentro  de  una Declaración Única de
Aduanas (DUA)

Normalización

Se  aplica  un  proceso  sistemático  de  normalización  de  datos
(1NF  →  5NF),  documentado  en  detalle  en  la sección 6.5, para
transformar  los  datos  crudos  en  un  modelo  Copo  de  Nieve sin
redundancias.

Jerarquías implementadas:

○  DIM_TIEMPO: Año → Trimestre → Mes → Semana → Día
○  DIM_UBICACION: Continente → País
○  DIM_PAIS_TLC (subdimensión): País → Acuerdo TLC → Arancel aplicable

●  Fase 4 - Integración de Datos (ETL) y Gestión de Metadatos

El  proceso  ETL  se  implementó  en  Python  con  las  librerías  pandas,  dbfread,  re  y
sqlalchemy. Las tres etapas de manipulación se describen a continuación:

11

Etapa

Descripción

Herramientas

Extracción

Recolección  desde  archivos  DBF/TXT  de
SUNAT y CSVs/Excel de BCRP, MINCETUR y
costos

dbfread, pandas

Transformación

Limpieza,  deduplicación,  filtros  Regex  para
identificar "HASS", enriquecimiento con fuentes
externas

pandas,
numpy

re,

Carga

Inserción  en  Data  Mart  respetando  orden  de
integridad  referencial  (primero  dimensiones,
luego hechos)

SQLAlchemy,
psycopg2

Control  de  calidad:  El proceso ETL se documenta con una bitácora (log) que registra la
cantidad  de  registros  procesados,  insertados  y  rechazados  por  cada  regla de validación,
asegurando la trazabilidad de la información.

1.6 Estructura del Data Mart Actual
El Data Mart se organiza bajo un modelo dimensional tipo Copo de Nieve (Snowflake Schema).
Este  diseño  permite  normalizar  jerarquías  en  subdimensiones,  evitando  redundancias  y
facilitando el mantenimiento de la información.

Tabla de hechos central: FACT_RENTABILIDAD

La tabla de hechos es el centro del modelo y almacena únicamente las métricas atómicas de cada
operación de exportación:

Métrica

Descripción

Unidad

Valor_FOB

Valor de venta de la exportación

Dólares americanos (USD)

Volumen_Exportado

Peso neto de la mercancía

Kilogramos (kg)

Nota:  Las  métricas derivadas (precio por kilogramo, margen de utilidad y ratio de rentabilidad)
no  se  almacenan  físicamente  en  la  tabla  de  hechos.  Se  calculan  en  la  capa  de  visualización
(Power BI) para garantizar consistencia ante futuras actualizaciones de costos o tipo de cambio.

Tablas de dimensiones (permiten segmentar el análisis)

Las dimensiones proporcionan el contexto descriptivo para filtrar y agrupar los datos:

Dimensión

¿Qué permite analizar?

DIM_TIEMPO

Evolución temporal (año, trimestre, mes, semana, día)

12

DIM_UBICACION

Análisis por país y continente de destino

DIM_PAIS_TLC
(subdimensión)

Acuerdos  comerciales  y  aranceles  por  país  (mercados
"Premium")

DIM_PRODUCTO

Información base del producto (partida arancelaria)

DIM_VARIEDAD_CALIDAD

Calidad  (CAT  1,  CAT  2)  y  método  de  producción
(orgánico/convencional)

DIM_EXPORTADOR

Competidores en el mercado peruano

DIM_ADUANA

Puertos y puntos de embarque

DIM_FINANZAS

Tipo de cambio (BCRP) y aranceles (MINCETUR)

DIM_COSTO

Costos referenciales de producción, empaque y logística

Granularidad del modelo

La  granularidad  es  fina:  un  registro  en  la  tabla  de  hechos corresponde a una línea de producto
dentro  de  una  Declaración  Única  de  Aduanas  (DUA).  Esto  significa  que  cada  ítem  individual
(con su propio valor FOB y peso neto) tiene su propio registro.

Ventaja de esta granularidad: Permite agregaciones flexibles:

Nivel de agregación

Ejemplo

Fino

Medio

Grueso

Análisis por operación individual (DUA + ítem)

Exportaciones mensuales por país destino

Totales anuales por continente

Jerarquías implementadas

Dimensión

Jerarquía

DIM_TIEMPO

Año → Trimestre → Mes → Semana → Día

DIM_UBICACION

Continente → País

DIM_PAIS_TLC

País → Acuerdo TLC → Arancel aplicable

DIM_VARIEDAD_CALIDAD  Variedad → Categoría de calidad → Método de producción

13

El  detalle  completo  de  atributos,  tipos  de  datos,  claves  primarias  y  foráneas,  subdimensiones
normalizadas y restricciones de integridad referencial se presenta en la sección 5. Modelamiento
Dimensional.

1.7 Preguntas de Negocio que Responde el Data Mart

El Data Mart ha sido diseñado para dar respuesta a las siguientes preguntas:

Pregunta Central:

-

¿Cuál es el nivel de rentabilidad potencial de la palta Hass en el período 2016–2024?

Preguntas Analíticas de Soporte:

N°

Pregunta de negocio

Dimensiones
involucradas

Dirigido a

Propósito

1

2

3

4

evoluciona

¿Cómo
el
precio  promedio FOB por
kilogramo  a  lo  largo  del
tiempo  (mensual,  anual),
y  cómo  se  compara  esta
evolución  con  el  ratio  de
rentabilidad estimado?

¿Qué  países y continentes
presentan
un
consistentemente
precio  promedio  FOB/kg
superior  y  un  ratio  de
rentabilidad estimado más
alto? (Pregunta clave)

de

¿Cuál  es  el  nivel  de
las
concentración
exportaciones  por  país
destino? ¿Existe riesgo de
dependencia  excesiva  de
pocos mercados?

nivel

¿Qué
de
concentración  presenta  el
mercado  de  exportadores
peruanos  (índice  HHI)?
¿Existen  pocos  actores
dominantes  o  el  mercado
está diversificado?

DIM_TIEMPO

Planeamie
nto
Estratégic
o

Identificar
tendencias
y
estacionales
correlación  entre  precio
y rentabilidad

DIM_UBICACIO
N,
DIM_PAIS_TLC

Gerencia
General /
Comercio
Exterior

mercados
Clasificar
"Premium"  (con  TLC,
arancel
alta
rentabilidad)

0%,

DIM_UBICACIO
N

Planeamie
nto
Estratégic
o

Evaluar  diversificación
geográfica  y  mitigar
riesgos

DIM_EXPORTA
DOR

Finanzas /
Comercio
Exterior

Comprender  el  nivel  de
competencia
el
mercado

en

¿Qué  aduanas  o  puertos
de  salida  concentran  el
mayor volumen exportado
y  presentan  mejor  precio
promedio por kilogramo?

DIM_ADUANA

Comercio
Exterior

Optimizar
rutas
logísticas  y  seleccionar
puertos más eficientes

14

y

¿Qué relación existe entre
exportado
el  volumen
(escala)
precio
el
promedio
FOB/kg?
¿Existen  economías  de
mercados
escala
premium
de  menor
volumen?

o

FACT_RENTABI
LIDAD

Gerencia
General

Definir
volumen vs. precio

estrategia  de

5

6

Nota  sobre  las  respuestas.  Los  resultados  obtenidos  para  preguntas  que  involucran  costos,
márgenes  y  ratios  de  rentabilidad  son  estimaciones  basadas  en  parámetros  de  referencia
(provenientes  de  MIDAGRI  y  Sierra  Exportadora),  no  en  datos  reales  de  la  empresa  o  de  los
exportadores.

La  incorporación  del  tipo  de  cambio  (BCRP)  y  los  aranceles  (MINCETUR)  permite ajustar el
análisis  a  condiciones  económicas  reales,  calculando  un  Margen  Neto  Ajustado  en  soles  que
supera la limitación de los datos brutos de SUNAT.

Estos  resultados  deben  interpretarse  como  una  aproximación  para  la  toma  de  decisiones
estratégicas, no como estados financieros auditados.

2. MARCO TEÓRICO

2.1 Datos, Información y Sistemas de Información

En el contexto del presente proyecto, los datos provienen de múltiples fuentes:

Fuente

Tipo de dato

Descripción

SUNAT
(ADUANET)

Microdatos
exportación

de

Valor  FOB,  peso  neto,  fecha,  país  destino,
RUC del exportador, descripción adicional del
producto

BCRP

Serie histórica

Tipo de cambio USD/PEN (diario)

MINCETUR

Datos referenciales

Aranceles
comerciales (TLC)

por

país

destino,

acuerdos

MIDAGRI
Exportadora

/  Sierra

Costos referenciales

Costos de producción, empaque y logística por
región

La información se genera al transformar, limpiar y enriquecer estos datos, calculando indicadores
clave como:

15

●  Precio promedio FOB por kilogramo
●  Margen de utilidad estimado
●  Ratio de rentabilidad
●  Índice de concentración de mercado (HHI)
●  Margen neto ajustado por tipo de cambio y aranceles

El sistema de información implementado es un Data Mart en modelo Copo de Nieve (Snowflake
Schema), que integra, almacena y permite analizar esta información multidimensionalmente para
la toma de decisiones estratégicas sobre la diversificación hacia la palta Hass.

2.2 Inteligencia de Negocios (Business Intelligence)

En  el  presente  proyecto,  la  arquitectura  BI  implementada  establece  una  clara  distinción  entre
ambos sistemas:

●  El sistema OLTP es SUNAT/ADUANET, orientado al registro de transacciones

individuales de exportación.

●  El sistema OLAP es el Data Mart construido, optimizado para el análisis histórico y

multidimensional de la rentabilidad de la palta Hass.

El  Data  Mart,  construido  bajo  un  esquema  de  Copo  de  Nieve  (Snowflake  Schema),  permite
múltiples tipos de análisis:

Tipo de análisis

Dimensión utilizada

¿Qué permite evaluar?

Análisis
competencia

de

DIM_EXPORTADOR

Identificar  principales  exportadores
y calcular el índice HHI

Análisis logístico

DIM_ADUANA

DIM_FINANZAS

Análisis  de  riesgos
financieros

Análisis  de  calidad
de producto

Comparar  eficiencia  por  puerto  de
salida y optimizar rutas

Incorporar  tipo  de  cambio  (BCRP)
y aranceles (MINCETUR)

DIM_VARIEDAD_CALIDAD

Segmentar por calidad (CAT 1, CAT
2) y método de producción

16

Esta  evolución  del  modelo  estrella  original  al  Copo  de  Nieve  responde  a  la  necesidad  de
profundidad analítica requerida por la Gerencia General para evaluar la viabilidad de la inversión
en palta Hass.

2.3 Modelamiento Dimensional y Esquema Copo de Nieve

En  el  presente  proyecto,  el  centro  del  modelo  se  encuentra  en  la  tabla  de  hechos
FACT_RENTABILIDAD, que almacena para cada operación de exportación:

●  El valor FOB (ingreso en USD)
●  El volumen exportado (peso neto en kg)

Las métricas derivadas (precio promedio por kilogramo, costo total estimado, margen de utilidad
y ratio de rentabilidad) se calculan en la capa de visualización (Power BI), siguiendo el principio
de que una tabla de hechos debe contener solo hechos atómicos e inmutables.

Dimensiones principales y subdimensiones

El modelo se complementa con las siguientes tablas:

Tipo

Tabla

Propósito

Dimensión principal  DIM_TIEMPO

Dimensión principal  DIM_UBICACION

Analizar  evolución
trimestre, mes, semana, día)

temporal

(año,

Analizar  por  país  y  continente  de
destino

Dimensión principal  DIM_PRODUCTO

Información base de la palta Hass

Dimensión principal  DIM_EXPORTADOR

Identificar  competidores  en el mercado
peruano

Dimensión principal  DIM_ADUANA

Analizar puertos y puntos de embarque

Subdimensión

DIM_PAIS_TLC
(dependiente
DIM_UBICACION)

de

Acuerdos  comerciales  y  aranceles  por
país destino

Dimensión principal

DIM_VARIEDAD_CALID
AD

Jerarquías implementadas

Variedad,
producción (independiente)

calidad

y  método  de

Dimensión

Jerarquía

17

DIM_TIEMPO

Año → Trimestre → Mes → Semana → Día

DIM_UBICACION

Continente → País

DIM_PAIS_TLC

País → Acuerdo TLC → Arancel aplicable

DIM_VARIEDAD_CALIDAD

Variedad → Categoría de calidad → Método de producción

Notas metodológicas

Nota

Descripción

Competencia y Logística

Las  dimensiones  DIM_EXPORTADOR  y  DIM_ADUANA
permiten calcular el Índice de Concentración de Mercado (HHI)
y optimizar rutas de exportación.

Costos (SCD Tipo 2)

Fuentes Externas

2.4 Procesos ETL

DIM_COSTO  se  implementa  con  una  estrategia  SCD  Tipo  2
(Slowly  Changing  Dimension)  para  mantener  el  historial  de
cambios  en  los  costos  de  producción,  empaque  y  logística.  El
detalle de atributos se presenta en la sección 5.2.

El  enriquecimiento  con  BCRP  (tipo de cambio) y MINCETUR
(aranceles)  permite  calcular  un  Margen  Neto  Ajustado  que
supera la limitación de los datos brutos de SUNAT.

El  proceso  ETL  (Extract,  Transform,  Load)  es  el  núcleo  de  la  arquitectura  de  Inteligencia  de
Negocios, responsable de garantizar la calidad, consistencia e integridad de los datos antes de ser
depositados en el Data Mart.
El proyecto implementa un flujo ETL programático y automatizado basado en Python, utilizando
las librerías pandas, dbfread, re y sqlalchemy, estructurado en tres fases críticas:

2.4.1 Fase de Extracción:

Consiste en la recolección de datos desde sistemas de origen heterogéneos. Las fuentes de datos
utilizadas (SUNAT, BCRP, MINCETUR y MIDAGRI/Sierra Exportadora) ya fueron detalladas
en la sección 1.4 Alcance del Proyecto.

Para un análisis financiero robusto, la extracción emplea una estrategia de ingesta de datos
multisistema, respetando la periodicidad de cada fuente:

18

Fuente

Datos extraídos

Formato

Periodicidad

SUNAT
(ADUANET)

Microdatos  de  exportación  de
palta
(partida
0804400000)

Hass

DBF
TXT

BCRP

Tipo  de  cambio  promedio
(USD/PEN)  para  el  período
2016-2024

CSV
API

MINCETUR

Aranceles  aplicables  por  país
destino y acuerdos TLC

CSV
Excel

/

MIDAGRI
Sierra
Exportadora

de

Costos
(producción,
logística)

referencia
empaque,

PDF
Excel

/

/

/

/

Mensual
manual programada)

(descarga

Extracción
(histórica)

única

Extracción  única  con
actualizaciones anuales

Extracción
(referencial)

única

2.4.2 Fase de Transformación:

Es la etapa más compleja y donde reside la lógica de negocio. Para el modelo Copo de Nieve, la
transformación se divide en cuatro subprocesos:

Subproceso

Descripción

Limpieza y
Deduplicación

Eliminación  de  registros  duplicados  (basado  en  NRO_DOCU  +
FECHA  +  CNAN)  y  exclusión  de  valores  nulos  o  negativos  en
FOB_DOLPOL y PESO_NETO.

Procesamiento de
Texto y
Estandarización
(Filtro Hass)

Uso  de  Expresiones  Regulares  (Regex)  para explorar DESC_ADIC y
la  variedad  "HASS"  y
DESC_COM,  filtrando  exclusivamente
y
"CONGELADO"
"TROZOS",
"PULPA",
excluyendo
"PROCESAMIENTO".  También  se  extraen  atributos  de  calidad  y
método de producción.

Enriquecimiento de
Datos

Integración  de  fuentes  externas  mediante  operaciones  de  merge:  tipo
de  cambio  (BCRP),  aranceles  (MINCETUR)  y  costos  referenciales
(DIM_COSTO).

19

la  sección  2.5  (Precio_Promedio_kg,
Los  KPIs  definidos  en
Margen_Utilidad, Ratio_Rentabilidad) se calculan durante el ETL y se
almacenan físicamente en la tabla de hechos FACT_RENTABILIDAD,
siguiendo las fórmulas documentadas en dicha sección.

Cálculo de Métricas

2.4.3 Fase de Carga:

Involucra  la  inserción  física  de  los  datos en el motor de base de datos analítico (PostgreSQL o
SQL Server). Para garantizar la estabilidad del esquema Copo de Nieve, se aplican los siguientes
principios:

Principio

Descripción

Secuencialidad  e
Integridad
Referencial

La  carga  sigue  un  orden  estricto:  primero  dimensiones  independientes,
luego  dimensiones  dependientes,  finalmente  la  tabla  de  hechos.  Esto
asegura que ninguna llave foránea apunte a un registro inexistente.

Claves Sustitutas

Se  generan  identificadores  numéricos  propios  dentro  del  Data  Mart  (PK
autogenerados)  para  desligar  el  modelo analítico de los posibles cambios
en los códigos de los sistemas de origen.

Control
Calidad

de

Implementación  de  un  archivo de registro (log) que audita la cantidad de
registros  procesados,  insertados y rechazados por errores de consistencia,
asegurando la trazabilidad de la información.

2.5 KPIs e Indicadores de Rendimiento

Para  el  presente  proyecto,  se  definen  los  siguientes  KPIs,  alineados  con  las  necesidades  del
negocio y las nuevas capacidades del modelo Copo de Nieve:

KPI

Fórmula
resumida

Métrica

Fuentes

Meta

Precio Promedio
FOB/kg

Σ(FOB)
Σ(Peso Neto)

÷

USD/kg

SUNAT

Variable
destino

por

de

Margen
Utilidad
Estimado

Ingreso  FOB  –
Costo estimado

USD

SUNAT
DIM_COSTO

+

Positivo

Ratio
Rentabilidad

de

÷
(Margen
Ingreso  FOB)  ×
100

Porcentaje

SUNAT
DIM_COSTO

+

15% – 25%

20

de

Índice
Concentración
por Destino

(FOB_país
FOB_total)
100

÷
×

Índice
(Exportadores)

HHI

Margen  Neto
Ajustado

Σ(FOB_exporta
dor
FOB_total)²

÷

(FOB  ×  TC)  –
(Costo_Total  ×
TC) – Aranceles

Descripción de cada KPI:

Porcentaje

SUNAT

<  70%  (Top  3
países)

Porcentaje

USD / PEN

SUNAT
(DIM_EXPORT
ADOR)

SUNAT
BCRP
MINCETUR

+
+

< 2500

Positivo

●  KPI 1 - Precio Promedio FOB/kg: Identifica la evolución del precio y permite segmentar

por destino para identificar mercados premium.

●  KPI 2 - Margen de Utilidad Estimado: Evalúa la rentabilidad generada por cada

transacción de exportación en términos absolutos.

●  KPI 3 - Ratio de Rentabilidad: Determina qué porcentaje del ingreso representa la

utilidad estimada. La meta del 15% al 25% se basa en estándares sectoriales de Sierra
Exportadora.

●  KPI 4 - Índice de Concentración por Destino: Cuantifica la concentración geográfica y
permite identificar oportunidades de diversificación. Una concentración inferior al 70%
refleja una cartera diversificada.

●  KPI 5 - Índice HHI (Exportadores): Mide el nivel de competencia en el mercado peruano.

Un valor inferior a 2500 indica un mercado competitivo (no concentrado).

●  KPI 6 - Margen Neto Ajustado: Evalúa la rentabilidad real considerando el tipo de

cambio (BCRP) y los aranceles (MINCETUR) del país destino, superando la limitación
de los datos brutos de SUNAT.

Relación entre KPIs y objetivos estratégicos del BSC

Objetivo Estratégico

KPI asociado

Evaluar
la
inversión (Financiera)

rentabilidad  potencial  de

la

Ratio de Rentabilidad, Margen Neto Ajustado

Identificar  los  mejores  mercados  de  destino
(Cliente/Mercado)

Precio  Promedio  FOB/kg,
Concentración por Destino

Índice

de

Reducir
(Cliente/Mercado)

la

concentración

de

riesgo

Índice  de  Concentración  por  Destino,  Índice
HHI

Automatizar  y  validar  el  proceso  ETL
(Procesos Internos)

Metas  de  eficiencia  y  calidad  (ver  sección
2.6)

Justificación de las metas

Meta

Justificación

Fuente

21

Ratio  de  Rentabilidad:
15% – 25%

Rango
agroexportadores no tradicionales

viable

para

productos

Sierra  Exportadora  (informes
sectoriales 2023)

Concentración
destino: < 70%

por

Índice inferior al 70% refleja cartera
superior  al  85%
diversificada;
indica alta vulnerabilidad

Literatura
exterior

de

comercio

Índice HHI: < 2500

inferior  a  2500
competitivo

Valor
mercado
concentrado)

indica
(no

Literatura
exterior

de

comercio

2.6 Balanced Scorecard (BSC)

El  Balanced  Scorecard  (BSC)  es una herramienta de gestión estratégica que traduce la visión y
objetivos  de  una  empresa  en  un  conjunto  de  indicadores  organizados  en  cuatro  perspectivas:
Financiera, Cliente/Mercado, Procesos Internos, y Aprendizaje y Crecimiento.

En  el  presente  proyecto,  el  BSC  permite  alinear  la  construcción  del Data Mart con el objetivo
estratégico de Peruvian Andean Trout S.A.C.: analizar la rentabilidad potencial de la palta Hass
como  nueva  línea  de  negocio,  considerando  factores  de  competencia,  riesgos  cambiarios  y
aranceles.

Análisis FODA del Proyecto

Fortalezas (F)

Debilidades (D)

F1.  Equipo  con  conocimientos  en BI
y  modelamiento  de  datos  (Copo  de
Nieve).
F2.  Metodología  definida  (ETL  con
Python,  Regex,
enriquecimiento
externo).
producto
en
F3.  Enfoque
específico  (palta  Hass)  que  permite
profundidad analítica.

un

D1.  Dependencia  de  datos  públicos
agregados  (no  se  tienen  costos  reales
internos).
D2. Limitada experiencia previa de la
empresa  en  el  sector  agroexportador
de palta.
D3.  Sin  acceso  a  datos  de  calidad,
variedad o cliente final.

Oportunidades (O)

Amenazas (A)

Interno

Externo

22

internacional

O1.  Alta  demanda
sostenida de la palta Hass.
O2.  Disponibilidad
históricos (2016-2024) de SUNAT.
O3.  Posibilidad  de  enriquecer  el
análisis  con  fuentes  externas  (BCRP,
MINCETUR, Sierra Exportadora).

datos

de

de

por

Volatilidad

precios
factores

A1.
internacionales
climáticos o geopolíticos.
A2.  Competencia  creciente  de  otros
países  exportadores  (Chile,  México,
Colombia).
A3.  Cambios  en
aranceles de los mercados destino.

regulaciones  o

Mapa Estratégico del Proyecto (Perspectivas y Relaciones Causa-Efecto)

El  siguiente  mapa  muestra  cómo  los  objetivos  de  las  perspectivas  inferiores  (Aprendizaje  y
Crecimiento y Procesos Internos) soportan el logro de los objetivos superiores (Cliente/Mercado
y Financiera), creando una cadena de valor lógica y justificada.

Justificación de las relaciones Causa-Efecto:

23

Relación

Justificación

Aprendizaje → Procesos

Procesos → Cliente/Mercado

Cliente/Mercado → Financiera

Al  aprender  a  integrar  datos  del  BCRP  (tipo  de  cambio)  y
MINCETUR (aranceles), se automatiza un proceso ETL más
robusto que el actual (solo SUNAT).

Un  proceso  automático  y  confiable  que  calcule  KPIs como
Precio  FOB/kg  y  Margen  Neto  Ajustado  permite  a  la
gerencia identificar los mercados con mayor rentabilidad.

Al  identificar mercados "Premium" (con TLC, arancel 0%),
la  empresa  puede  enfocar  sus  esfuerzos  comerciales  en
destinos que maximizan el ratio de rentabilidad.

24

Tablero de Control Estratégico

A  continuación,  se  detallan  los  objetivos,  metas  e  indicadores  para  cada  perspectiva, con valores y rangos sustentados lógicamente
según la naturaleza del proyecto y las fuentes de datos disponibles.

Perspectiva

Objetivo Estratégico

Indicador (KPI)

Meta / Rango
Esperado

Iniciativa Estratégica

Financiera

la

Evaluar
rentabilidad
potencial  de la inversión en
palta Hass

Ratio  de  Rentabilidad
Estimado

Rango  meta:  >  15%  -
25%

Proyecto  de
inversión  en
palta  Hass  condicionado  a
resultados del Data Mart.

Identificar  los  3  destinos
con  mayor
rentabilidad
potencial ajustada

Promedio
Precio
FOB/kg  por  destino  +
Margen Neto Ajustado

>  $2.50  USD/kg  en  al
menos 3 destinos

Dashboard  comparativo  de
rentabilidad por país destino,
incluyendo aranceles.

Cliente /
Mercado

Procesos
Internos

Reducir la concentración de
riesgo  de  mercados  y
competidores

de
Índice
Concentración  (Top  3
países  /  Total  FOB)  e
Índice HHI

<  70%  del  FOB  en  3
países; HHI < 2500

Automatizar  la  integración
y  transformación  de  datos
de  SUNAT  +
fuentes
externas

Eficiencia  del  proceso
ETL

100%  de  ejecuciones
exitosas en < 5 minutos
para 100,000 registros

Calcular  KPIs  con  datos
(filtro  Hass  y
validados
extracción de atributos)

Calidad
(registros
totales)

de
válidos

datos
/

>  95%  de  los  registros
extraídos son válidos

de

prospección
Plan
comercial
nuevos
mercados  identificados  (ej.
Asia o Medio Oriente).

hacia

Desarrollo  de  script  ETL  en
logging  de
Python
errores
de
enriquecimiento.

con
y  módulo

Implementación de reglas de
la  fase  de
validación  en
Transformación
ETL
(Regex, rangos, nulos).

Aprendizaje y
Crecimiento

Incorporar  nuevas  fuentes
de  datos  para  enriquecer  el
análisis

Capacidad
de
integración  de  fuentes
externas

Integración  exitosa  de
al  menos  3  variables
externas

25

consuma  APIs

Desarrollo  de  módulo  de
enriquecimiento  en  Python
que
o
archivos  CSV  del  BCRP,
MINCETUR
Sierra
Exportadora.

y

Justificación de las metas:

Meta

Justificación

Fuente

Ratio > 15% – 25%

Márgenes  de  rentabilidad  viables  para  productos  agroexportadores  no
tradicionales

Sierra  Exportadora
(2023)

Precio > $2.50 USD/kg

Precio promedio histórico de palta Hass peruana fluctúa entre
1.80y
1.80y3.50 USD/kg. Un umbral de $2.50 califica mercados "premium"

SUNAT
(2016-2024)

Concentración < 70%

Índice  inferior  al  70% refleja cartera diversificada; superior al 85% indica alta
vulnerabilidad

Literatura
comercio exterior

de

HHI < 2500

Valor inferior a 2500 indica mercado competitivo (no concentrado)

Literatura
comercio exterior

de

ETL < 5 min

Calidad > 95%

La base de datos SUNAT para palta Hass no supera 100,000 registros; un script
optimizado (pandas) procesa en < 2 minutos (umbral de aceptación: 5 min)

Estimación técnica

Meta  ambiciosa  pero  alcanzable  para  una  fuente  administrativa  estructurada
como SUNAT

Estimación técnica

26

3. ANÁLISIS DEL CASO

3.1 Descripción del Negocio

El  dominio  de  negocio  analizado  es  el  sector  agroexportador  peruano,  específicamente  la
exportación de palta Hass (partida arancelaria 0804400000) durante el período 2016-2024.

La empresa Peruvian Andean Trout S.A.C., actualmente dedicada a la acuicultura (producción y
comercialización  de trucha para exportación), evalúa diversificarse hacia el mercado de la palta
Hass. El presente análisis permite evaluar la viabilidad de esta nueva línea de negocio mediante
el  estudio  de  su  comportamiento  en  términos  de  precios,  mercados  de  destino,  competencia,
costos de referencia y evolución temporal.

Partes interesadas (Stakeholders):

Stakeholder

Rol en la solución

Expectativa

Gerencia General  Decisor estratégico

Determinar viabilidad de inversión basada
en KPIs de rentabilidad.

Planeamiento
Estratégico

Evaluador de nuevas líneas

Identificar  mercados  rentables  y  evaluar
concentración de riesgo.

Finanzas

Analista de rentabilidad

Validar  márgenes  y  ratios  ajustados  por
tipo de cambio y aranceles.

Comercio Exterior

Asesor
competitivo

logístico

y

Organigrama de Peruvian Andean Trout S.A.C.

Evaluar
competidores y aduanas de salida.

destinos,

costos

logísticos,

La empresa Peruvian Andean Trout S.A.C. presenta la siguiente estructura organizacional para la
toma de decisiones relacionadas con el proyecto de diversificación hacia la palta Hass:

Nivel

Cargo / Rol

Responsabilidad en el proyecto

1

2

2

2

3

Gerencia General

Decisor estratégico. Aprueba inversión.

Gerente de Planeamiento

Evalúa mercados y concentración de riesgo.

Gerente de Finanzas

Valida márgenes y define reglas de negocio.

Gerente de Comercio Exterior

Usuario líder; define requerimientos aduaneros.

Equipo  de  Proyecto  (Consultores
BI)

Diseña, implementa y opera el Data Mart.

Ubicación

Error detectado
/ Debilidad

Justificación Técnica

Propuesta de Corrección

27

Rol:
Analista
de BI

Concentración
excesiva
funciones.

de

Rol:
Gerente
de
Finanzas

Responsabilidad
pasiva.

Un  solo  rol  no  suele  diseñar
implementar
(arquitectura),
(ETL)
operar
y
(mantenimiento)  en  entornos
corporativos
sin
supervisión.

reales

Desglosar  o  añadir  un
Líder
Técnico/Arquitecto
de
Datos  para  la  validación
del  modelo  dimensional
(Star Schema).

un  Data  Mart

de
En
rentabilidad,  este
rol  debe
certificar  las  fuentes  de datos
evitar
financieras
discrepancias.

para

a:

"Valida
Cambiar
márgenes  y  define
las
reglas  de  negocio  para el
cálculo de rentabilidad".

Rol:  G.
Comercio
Exterior

Alcance
consultivo
limitado.

Si  el  Data  Mart  es  sobre
(como
exportaciones
aguacate/trucha),  este  rol  es  el
Usuario Líder (Champion).

Cambiar a: "Usuario líder;
define  requerimientos  de
información  aduanera  y
logística".

Nota:  El  equipo  de  proyecto  actúa  como  consultor  externo  especializado  en  Inteligencia  de
Negocios.

28

Equipo de trabajo:

El presente proyecto es desarrollado por un equipo de 6 integrantes:

Integrante

Rol

David Choy

Líder de proyecto / Aprobador

Cristian Cardenas

Analista de requerimientos

Bruno Guillena

Modelador de datos

Lady Loayza

Desarrolladora ETL

Francis Moreno

Desarrollador de dashboards

Jeampieer's Salvador

Documentador

3.2 Requerimientos del Negocio

Los requerimientos fueron recopilados de:

●  Manual de procesos internos de Peruvian Andean Trout S.A.C. (diversificación)
●  Normas ISO 9001/22000 aplicables a agroexportación
●  Observaciones directas sobre disponibilidad de datos en SUNAT/ADUANET

Tipos de requerimientos del negocio

Tipo

Descripción

Ejemplo en el proyecto

Estratégicos

Apoyan  objetivos  de  negocio  a  largo
plazo

Evaluar  viabilidad  de  nueva línea de
negocio

Operativos

Soportan procesos diarios

Generar
rentabilidad por destino

reportes  mensuales  de

Técnicos

Definen la implementación tecnológica  Data Mart en modelo Copo de Nieve

Matriz de requerimientos (prioridad, fuente, conflicto, solución):

Requerimiento

Fuente

Prioridad

Conflicto
identificado

Solución propuesta

Conocer
rentabilidad  por
destino

Gerencia

Alta

Datos  SUNAT
sin costos reales

costos

Estimar
valores  de
(Sierra Exportadora)

con
referencia

Analizar
evolución
temporal

Planeamiento  Alta

Granularidad
diaria
mensual

vs

Implementar  jerarquías
en  DIM_TIEMPO  (año
→  trimestre  →  mes  →
semana)

29

Comparar
competidores

con

Comercio
Exterior

Media

Datos
de
competidores no
públicos

Usar
DIM_EXPORTADOR
para
concentración
mercado (índice HHI)

análisis

de
de

Evaluar  impacto
de
de
tipo
cambio
y
aranceles

Finanzas

Alta

Datos  SUNAT
de
sin
tipo
cambio
ni
aranceles

Integrar  BCRP  (tipo  de
cambio)  y  MINCETUR
(aranceles)
como
fuentes externas

Nota sobre la dimensión CLIENTE (importador final)

SUNAT  no  registra  el  nombre  ni  RUC  del  importador/comprador  final  en  los  microdatos  de
exportación  públicos.  Por  lo  tanto,  no  es  posible  construir  una  dimensión  DIM_CLIENTE
directa.

Solución  proxy  aprobada:  Se  utiliza  DIM_UBICACION  (país  de  destino)  como  aproximación
del mercado consumidor.

●  El  análisis  de  rentabilidad  potencial  no  requiere  identificar  clientes  individuales,  sino

mercados objetivo.

●  Los  aranceles  y  acuerdos  comerciales (TLC) dependen exclusivamente del país destino,

no del importador específico.

●  La concentración de riesgo se evalúa a nivel de país, no de cliente final.

Se  reconoce  esta  limitación  como  una  simplificación  válida  para  el  alcance  del  proyecto
(evaluación de viabilidad de inversión previa a la entrada al mercado).

Análisis de conflictos y soluciones

Conflicto principal

Solución

La  SUNAT  no  proporciona
costos  reales,  tipo  de  cambio  ni
aranceles.

Estimación  de  costos  basada  en  valores  de  referencia  de
Sierra  Exportadora.  Integración  de  BCRP  para  tipo  de
cambio y MINCETUR para aranceles.

Matriz de necesidades del negocio (Requerimientos vs KPIs):

30

Necesidad del Negocio

KPI (Indicador)

Dimensiones de Análisis

Prioridad

Identificar
del precio

evolución

Precio
FOB/kg

Promedio

Tiempo (Mes)

Alta

Evaluar evolución de la
rentabilidad

Ratio de Rentabilidad

Tiempo  (Año),  Geografía
(País)

Alta

Identificar
mercados

mejores

Precio
FOB/kg

Promedio

Geografía
Continente)

(País,

Alta

Evaluar  concentración
de riesgo

Índice
Concentración

de

Geografía
Exportador

(País),

Media

Analizar competencia

Participación
mercado
exportador

de
por

Exportador, Tiempo

Media

Evaluar
logístico

impacto

Costo
destino

logístico  por

Geografía (País), Aduana  Media

Nota  técnica:  El  KPI  "Precio  promedio  FOB/kg"  se  aplica  con  dos  dimensiones  de  análisis
diferentes (Tiempo y Geografía) para responder a dos necesidades de negocio distintas. Esto no
constituye  un  KPI  adicional,  sino  el  mismo  indicador  utilizado  en  diferentes  ejes  de  análisis
multidimensional, una de las ventajas fundamentales del modelo dimensional.

Matriz Interfuncional

Actores / Etapas

Responsabilidad

SUNAT/ADUANET

Proveer microdatos de exportación (partida 0804400000)

Analista de BI

Extraer, transformar y cargar datos al Data Mart

Gerencia General

Tomar decisiones de inversión basadas en los resultados

Matriz RACI

A  continuación,  se  detallan  las  responsabilidades  de  cada  integrante  del  equipo  por  tarea
específica:

Tarea /
Integrante

David
Choy

Cristian
Cardenas

Bruno
Guillena

Lady
Loayza

Francis
Moreno

Jeampieer's
Salvador

Levantamiento
de
Requerimientos

Modelamiento
(Copo de Nieve)

Script ETL en
Python

Diseño de
Dashboards

Documentación
PC1

A

R

R

C

I

R

C

I

R

A

C

A

I

R

I

I

R

C

A

R

C

I

A

I

R

31

I

C

R

I

A

R = Responsable, A = Aprobador, C = Consultado, I = Informado

3.3 KPIs Relevantes

3.3.1 Proceso de Definición de los KPIs

Los  KPIs  (Key  Performance  Indicators)  del  presente  proyecto  fueron  definidos  siguiendo  un
proceso estructurado de 4 etapas, que asegura que cada indicador esté alineado con los objetivos
del negocio y sea técnicamente viable de calcular con las fuentes de datos disponibles.

Etapa 1: Identificación de necesidades del negocio

Se  realizaron  reuniones  con  los  stakeholders  (Gerencia  General,  Planeamiento  Estratégico,
Finanzas  y  Comercio  Exterior)  para  identificar  sus  necesidades  de  información.  De  estas
reuniones surgieron las siguientes preguntas clave:

Stakeholder

Pregunta clave

Necesidad de negocio

Gerencia General

"¿Es  rentable  invertir  en  palta
Hass?"

Evaluar  la  viabilidad  financiera  de  la
diversificación

Planeamiento
Estratégico

"¿A  qué  mercados  conviene
exportar?"

Identificar
potencial

destinos

con  mayor

Finanzas

"¿Cuál  es  la  rentabilidad  real
considerando  costos,
tipo  de
cambio y aranceles?"

Calcular  márgenes
condiciones reales

ajustados

a

32

Comercio
Exterior

nuestros
son
"¿Quiénes
competidores? ¿Qué puertos son
más eficientes?"

Analizar  el  mercado  y  optimizar  la
logística

Etapa 2: Revisión de estándares sectoriales

Se consultaron informes y guías del sector agroexportador para validar que los KPIs propuestos
sean comparables con estándares de la industria:

Fuente consultada

Aporte al proyecto

Sierra Exportadora (2023)

Estableció  la  meta  de  rentabilidad  viable  entre  15%  y 25%
para productos agroexportadores no tradicionales

Literatura de comercio exterior

Definió  que  un  índice  de  concentración  inferior  al  70%
refleja  una  cartera  diversificada,  y  que  un  HHI  inferior  a
2500 indica un mercado competitivo

Reportes  de comercio regional
(MINCETUR)

Proporcionó  información  sobre  los  principales  mercados
destino de la palta peruana

Documentación
BCRP

técnica  del

Confirmó  la  disponibilidad  de  la  serie  histórica  de  tipo  de
cambio (PD04638PD)

Etapa 3: Viabilidad técnica

Para cada KPI propuesto, se verificó que fuera técnicamente viable de calcular con las fuentes de
datos disponibles:

Fuente de datos

¿Qué información aporta?

¿Qué KPI permite calcular?

SUNAT

BCRP

Valor  FOB,  peso  neto,  país
destino, RUC del exportador

Precio
FOB/kg,
concentración, HHI

índice

de

Tipo  de  cambio  histórico
USD/PEN

Margen neto ajustado

MINCETUR

Aranceles  por  país  destino,
acuerdos TLC

Clasificación de mercados "Premium"

MIDAGRI  /  Sierra
Exportadora

Costos
producción,
logística

referenciales
empaque

de
y

Margen
rentabilidad

de

utilidad,

ratio

de

Etapa 4: Selección final y priorización

33

Se  priorizaron  los  KPIs  según  su  impacto  en  la  toma  de decisiones y su viabilidad técnica. La
siguiente tabla resume el proceso de selección:

KPI

¿Responde a qué
necesidad?

¿Es viable?

Prioridad

Precio
FOB/kg

Promedio

Identificar
premium

mercados

Sí (SUNAT)

Alta

Margen  de  Utilidad
Estimado

Evaluar
operación

ganancia

por

Sí (SUNAT + costos)

Alta

Ratio de Rentabilidad

Decidir
inversión

viabilidad

de

Sí (SUNAT + costos)

Alta

Índice
Concentración
Destino

de
por

Evaluar riesgo geográfico

Sí (SUNAT)

Media

Índice HHI

Evaluar
competencia

nivel

de

Sí (SUNAT)

Media

Margen
Ajustado

Neto

Calcular  rentabilidad  real
en soles

Sí (SUNAT + BCRP +
MINCETUR)

Alta

3.3.2 Valor Aportado por Cada KPI

A  continuación,  se  detalla  el  valor  específico  que  cada  KPI  aporta  a  la  toma  de decisiones de
Peruvian Andean Trout S.A.C.:

KPI 1: Precio Promedio FOB/kg

Atributo

Valor

Fórmula

Σ(FOB) ÷ Σ(Peso Neto)

Valor aportado

Permite  identificar  qué países pagan un mejor precio por kilogramo
de palta Hass. Por ejemplo, si Países Bajos tiene un precio de
2.80USD/kg  España  2.10  USD/kg,  la  empresa  puede  priorizar  sus
esfuerzos comerciales hacia Países Bajos.

Decisión que impacta

Selección de mercados objetivo para la exportación.

Frecuencia de cálculo  Mensual

KPI 2: Margen de Utilidad Estimado

34

Atributo

Valor

Fórmula

Ingreso FOB – Costo estimado (producción + empaque + logística)

Valor aportado

Muestra
la  ganancia  en  términos  absolutos  (USD)  por  cada
operación  de  exportación.  Permite  comparar  la  rentabilidad  de
diferentes  envíos,  identificando  cuáles  generan  mayor  retorno
económico.

Decisión que impacta

Evaluación de la conveniencia de cada transacción; identificación de
operaciones con bajo margen.

Frecuencia de cálculo  Mensual

KPI 3: Ratio de Rentabilidad

Atributo

Valor

Fórmula

(Margen ÷ Ingreso FOB) × 100

Valor aportado

Indica qué porcentaje del ingreso total se convierte en ganancia. Una
rentabilidad del 20% significa que por cada
100USDvendidos,
100USDvendidos,20  USD  son  utilidad.  Permite  comparar
eficiencia de diferentes destinos y períodos.

la

Decisión que impacta

Decisión  final  de  inversión  (si  el  ratio  está  dentro  de  la  meta  del
15%-25%, el proyecto es viable).

Meta

15% – 25% (según Sierra Exportadora)

Frecuencia de cálculo  Mensual

KPI 4: Índice de Concentración por Destino

Atributo

Valor

Fórmula

(FOB_país_X ÷ FOB_total) × 100

Valor aportado

Mide qué porcentaje del total exportado se concentra en unos pocos
países. Si el Top 3 países representa el 80% de las exportaciones, la
empresa  tiene  un  alto  riesgo  de  dependencia.  Si  un  país  impone
restricciones o reduce su demanda, el impacto sería severo.

Decisión que impacta

Estrategia  de  diversificación  geográfica;  plan  de  prospección
comercial a nuevos mercados.

35

Meta

< 70% (Top 3 países)

Frecuencia de cálculo

Anual

KPI 5: Índice HHI (Herfindahl-Hirschman)

Atributo

Valor

Fórmula

Σ(FOB_exportador ÷ FOB_total)²

Valor aportado

Mide  el  nivel  de  competencia  en  el  mercado  de  exportadores
peruanos.  Un  HHI  bajo  (<2500)
indica  que  hay  muchos
exportadores  compitiendo,
lo  que  es  favorable  para  nuevos
entrantes. Un HHI alto (>2500) indica que pocas empresas dominan
el mercado, lo que podría significar barreras de entrada.

Decisión que impacta

Evaluación  del  nivel  de  competencia;
principales competidores.

identificación  de  los

Meta

< 2500

Frecuencia de cálculo

Anual

KPI 6: Margen Neto Ajustado

Atributo

Valor

Fórmula

(Ingreso FOB × TC) – (Costo_Total × TC) – Aranceles

Valor aportado

Este  es  el  KPI  más  completo.  Incorpora  tres  variables  críticas  que
SUNAT no proporciona: (1) tipo de cambio (BCRP) para convertir a
soles,  (2)  costos  referenciales  (MIDAGRI)  para  conocer  el  costo
real,  y  (3)  aranceles  (MINCETUR)  para  reflejar  el  costo  de
importación  en  el  país  destino.  Permite conocer la rentabilidad real
en moneda local.

Decisión que impacta

Evaluación  financiera  realista  de  la  inversión;  comparación  de
rentabilidad entre países considerando sus aranceles.

Meta

Positivo (mayor a 0)

Frecuencia de cálculo  Anual

3.3.3 Resumen de KPIs y su valor estratégico

KPI

Valor estratégico para la empresa

36

Precio Promedio FOB/kg

Identificar mercados que pagan mejor precio

Margen de Utilidad Estimado

Conocer la ganancia absoluta por operación

Ratio de Rentabilidad

Decidir si la inversión es viable (meta: 15-25%)

Índice de Concentración

Evaluar riesgo de dependencia de pocos países

Índice HHI

Conocer el nivel de competencia en el mercado

Margen Neto Ajustado

Conocer  la  rentabilidad  real  en  soles,  considerando  tipo  de
cambio y aranceles

37

Matriz de necesidades de KPIs

Necesidad del Negocio

KPI (Indicador)

Dimensiones de Análisis

Prioridad

Beneficio esperado

Identificar  evolución  del
precio

Precio
FOB/kg

Promedio

Tiempo (Mes)

Alta

Identificar
estacionales

tendencias

Evaluar  evolución  de  la
rentabilidad

Ratio de Rentabilidad

Tiempo  (Año),  Geografía
(País)

Alta

Evaluar
inversión

viabilidad

de

Identificar
mercados

mejores

Precio
FOB/kg

Promedio

Geografía
Continente)

(País,

Alta

Identificar destinos premium

Evaluar  concentración  de
riesgo

Índice  de Concentración
(HHI)

Geografía
Exportador

(País),

Media

Diversificar
clientes/países

cartera

de

Analizar competencia

Evaluar impacto logístico

de
Participación
mercado por exportador

Costo
destino

logístico

por

Exportador, Tiempo

Media

Geografía (País), Aduana

Media

Identificar
dominantes

Optimizar
exportación

competidores

rutas

de

Los KPIs definidos corresponden a los presentados en la sección 2.5 (Marco Teórico). A continuación, se presentan sus fórmulas:

KPI

Fórmula

Métrica

Frecuencia

Fuentes involucradas

Precio Promedio FOB/kg  Σ(FOB) / Σ(Peso Neto)

USD por kilogramo  Mensual

SUNAT

Margen
Estimado

de  Utilidad

Ingreso  FOB
estimado

-  Costo

USD

Mensual

SUNAT + DIM_COSTO

Ratio de Rentabilidad

(Margen / Ingreso) × 100

Porcentaje

Mensual

SUNAT + DIM_COSTO

38

Índice  de  Concentración
(HHI)

Σ(FOB_exportador
FOB_total)^2

/

Porcentaje

Anual

SUNAT
(DIM_EXPORTADOR)

Margen Neto Ajustado

(Ingreso  FOB  ×  TC)  -
-
(Costo_Total  ×  TC)
Aranceles

USD

Anual

SUNAT
+
MINCETUR

BCRP

+

Nota  sobre  el  Margen  Neto  Ajustado:  Este  KPI  incorpora  el  tipo de cambio (BCRP) para convertir los márgenes a moneda local
(PEN) y los aranceles (MINCETUR) para reflejar el costo real de importación en el país destino. Permite una evaluación más realista
de la rentabilidad neta.

Estos  valores  permitirán  a  la  gerencia  evaluar  rápidamente  si  la  diversificación  hacia  la  palta  Hass  es  viable  y  si  los resultados se
encuentran  dentro  de  los  parámetros  esperados  (rentabilidad  meta:  15%-25%).  Los  valores  específicos  para  Precio y Margen serán
determinados tras el procesamiento de datos.

39

3.4 Fuentes de Datos

La  arquitectura  se  alimenta  de  múltiples  fuentes  de  datos,  tanto  primarias como externas, para
enriquecer el análisis y superar las limitaciones de los datos brutos de SUNAT.

Fuentes de datos:

Fuente

Descripción

Formato

Uso en el proyecto

SUNAT
(ADUANET)

Microdatos de exportación de
palta Hass.

DBF / TXT

del  Data  Mart

Base
(transacciones)

BCRP

Serie  histórica  de  tipo  de
cambio (USD/PEN).

CSV / API

Ajuste  de  rentabilidad  a
moneda local (soles)

MINCETUR

Aranceles  por  país  destino,
acuerdos TLC, puertos.

CSV / Excel

MIDAGRI
Sierra
Exportadora

/

de

Costos
(producción,
logística).

referencia
empaque,

PDF / Excel

Cálculo  de  Margen  Neto
Ajustado
poblar
y
DIM_PAIS_TLC

Poblar  DIM_COSTO
calcular
Costo_Total_Estimado

y

Variables disponibles desde SUNAT (ADUANET):

Campo

Descripción

Uso en el proyecto

CNAN

Partida arancelaria

Filtro (0804400000) para DIM_PRODUCTO

FECHA

Fecha de embarque

DIM_TIEMPO

CPAIS

Código de país destino

DIM_UBICACION

PAIS_DESC

Nombre del país

DIM_UBICACION

FOB_DOLPOL  Valor FOB en dólares

FACT_RENTABILIDAD.Valor_FOB

PESO_NETO

Peso neto en kilogramos  FACT_RENTABILIDAD.Volumen_Exportado

NRO_DOCU

RUC del exportador

DIM_EXPORTADOR

EXPORTADOR  Nombre del exportador  DIM_EXPORTADOR

CADUANA

Código de aduana

DIM_ADUANA

ADUA_DESC

Descripción de aduana

DIM_ADUANA

40

DESC_ADIC
DESC_COM

/

Descripción
del producto

adicional

Extracción  de  variedad  (Hass),  calidad  y
método
para
orgánico
DIM_VARIEDAD_CALIDAD

Limitaciones de la fuente y soluciones implementadas:

Limitación

Solución en el proyecto

No  incluye  costos  reales  de
producción o logística

Uso  de  DIM_COSTO  con  valores  de  referencia  de
MIDAGRI / Sierra Exportadora

No
cliente/importador final

identifica

al

DIM_UBICACION actúa como proxy del mercado destino

No incluye datos de calidad del
producto

Extracción  de  atributos  desde  DESC_ADIC  mediante
Regex hacia DIM_VARIEDAD_CALIDAD

No incluye tipo de cambio para
ajuste monetario

No  incluye  aranceles  por  país
destino

Integración con BCRP (tipo de cambio USD/PEN)

Integración con MINCETUR para poblar DIM_PAIS_TLC

3.5 Requerimientos Funcionales y No Funcionales

3.5.1 Requerimientos Funcionales (RF)

Los  requerimientos  funcionales  describen  las  capacidades  específicas  que  el  Data  Mart  debe
ofrecer a los usuarios. Cada requerimiento incluye: identificador, nombre, descripción detallada,
actor involucrado, entrada, proceso y salida esperada.

RF01: Integración de datos de exportación desde SUNAT

Atributo

Valor

Identificador

RF01

Nombre

Extracción y carga de microdatos de exportación

Descripción

El  sistema  debe  extraer  los  microdatos  de  exportación  de  palta  Hass
(partida  arancelaria  0804400000)  desde  los  archivos  DBF/TXT  de
SUNAT/ADUANET correspondientes al período 2016-2024.

Actor

Analista de BI / Proceso ETL automatizado

41

Entrada

Proceso

Archivos  DBF/TXT  de  SUNAT  con  campos:  FECHA,  CPAIS,
PAIS_DESC,  CNAN,  FOB_DOLPOL,  PESO_NETO,  NRO_DOCU,
EXPORTADOR,
DESC_ADIC,
DESC_COM

ADUA_DESC,

CADUANA,

Lectura  mediante  librería  dbfread  de  Python,  conversión a DataFrame de
pandas, validación de columnas obligatorias

Salida esperada

Tabla  temporal  tmp_SUNAT_raw  con  los  12  campos  extraídos  sin
transformaciones

Prioridad

Alta (Crítica)

RF02: Filtrado exclusivo de la variedad Hass

Atributo

Valor

Identificador

RF02

Nombre

Filtro de producto por variedad Hass

Descripción

El  sistema  debe  aplicar  un  filtro  para incluir exclusivamente los registros
que  correspondan  a la variedad Hass, excluyendo automáticamente pulpa,
congelados, trozos y productos procesados.

Actor

Proceso ETL (fase de transformación)

Entrada

Tabla tmp_SUNAT_raw (campos DESC_ADIC, DESC_COM)

Proceso

Aplicar  expresión  regular  r'\bHASS?\b'  para  filtro  positivo;  aplicar
expresión
regular
r'\b(PULPA|TROZOS|CONGELADO|PROCESAMIENTO)\b'  para  filtro
negativo; convertir ambos campos a mayúsculas antes de evaluar

Salida esperada

Tabla  tmp_SUNAT_filtrada_HASS  con  solo  registros  que  contengan
"HASS" y no contengan términos excluyentes

Prioridad

Alta (Crítica)

RF03: Extracción de atributos de calidad desde texto no estructurado

Atributo

Valor

Identificador

RF03

Nombre

Extracción de variedad, categoría de calidad y método de producción

42

Descripción

El  sistema  debe  extraer  automáticamente,  mediante  expresiones
regulares  (Regex),  los  atributos  de  calidad  del  producto  desde  los
campos DESC_ADIC y DESC_COM.

Actor

Proceso ETL (fase de transformación)

Entrada

Proceso

Tabla
DESC_COM)

tmp_SUNAT_filtrada_HASS

(campos

DESC_ADIC,

Aplicar  Regex:  r'\bHASS?\b'  →  variedad;  r'CAT[\s\.]*1'  →  CAT  1;
r'CAT[\s\.]*2'  →  CAT  2;  r'ORGANIC[OA]'  →  método  orgánico;  caso
contrario → convencional

Salida esperada

Tabla  con  columnas  adicionales:  Variedad,  Categoria_Calidad,
Metodo_Produccion

Prioridad

Alta

RF04: Integración de tipo de cambio (BCRP)

Atributo

Valor

Identificador

RF04

Nombre

Carga de serie histórica de tipo de cambio USD/PEN

Descripción

El  sistema  debe  integrar  la  serie  histórica  de  tipo  de  cambio  del BCRP
(serie  PD04638PD)  para  el  período  2016-2024, con granularidad diaria,
incluyendo tratamiento de días no hábiles (forward-fill).

Actor

Proceso ETL (fase de extracción y transformación)

Entrada

Proceso

Archivo  CSV/Excel
ES_DIA_HABIL

con

campos:

FECHA,  TC_USD_PEN,

Cargar archivo, estandarizar formato de fecha (YYYY-MM-DD), validar
que  no  haya  valores  nulos,  aplicar  forward-fill  para  días  no  hábiles
usando el último valor hábil registrado

Salida esperada

Tabla DIM_FINANZAS poblada con registro diario de tipo de cambio

Prioridad

Alta

RF05: Integración de aranceles y acuerdos comerciales (MINCETUR)

Atributo

Valor

43

Identificador

RF05

Nombre

Carga de aranceles por país destino y acuerdos TLC

Descripción

El  sistema  debe  integrar  la  información  de  aranceles  aplicables  por  país
destino y los Tratados de Libre Comercio (TLC) vigentes con Perú, según
datos del MINCETUR.

Actor

Proceso ETL (fase de extracción y transformación)

Entrada

Proceso

Archivo  CSV/Excel  con  campos:  PAIS_DESTINO,  CODIGO_PAIS,
ARANCEL_PORCENTAJE,
ACUERDO_TLC,
CATEGORIA_MERCADO (Premium/Estándar)

Validar  que  cada  país  tenga  un registro único; verificar que los aranceles
estén  en  formato  decimal  (0.00  para  países  con  TLC);  poblar  la
subdimensión DIM_PAIS_TLC

Salida esperada

Tabla DIM_PAIS_TLC poblada con acuerdos comerciales por país

Prioridad

Alta

RF06: Integración de costos referenciales (MIDAGRI / Sierra Exportadora)

Atributo

Valor

Identificador

RF06

Nombre

Carga de costos referenciales de producción, empaque y logística

Descripción

El  sistema  debe  cargar  los  costos  referenciales  por  kilogramo  para  las  tres
fases  de  la  cadena  de  valor:  producción  (campo),  empaque  (packing)  y
logística (transporte + puerto + agenciamiento).

Actor

Proceso ETL (fase de extracción y transformación)

Entrada

Proceso

Salida
esperada

Archivo  Excel  con  campos:
Valor_Unitario_USD,
Fecha_Vigencia_Fin, Es_Vigente

ID_Costo,  Tipo_Costo,  Subcategoria,
Fecha_Vigencia_Inicio,

Region_Destino,

Implementar  lógica  SCD  Tipo  2:  si  un  costo  cambia,  no  se  sobreescribe  el
registro histórico; se crea un nuevo registro con nueva Fecha_Vigencia_Inicio
y se marca el anterior con Fecha_Vigencia_Fin y Es_Vigente = FALSE

Tabla DIM_COSTO poblada con historial de costos (SCD Tipo 2)

44

Prioridad

Alta

RF07: Cálculo de KPIs de rentabilidad

Atributo

Valor

Identificador

RF07

Nombre

Cálculo automático de los 6 KPIs definidos

Descripción

El sistema debe calcular automáticamente los siguientes KPIs a partir de los
datos  integrados:  Precio  FOB/kg,  Margen  de  Utilidad  Estimado,  Ratio  de
Rentabilidad,  Índice  de  Concentración  por  Destino,  Índice  HHI,  Margen
Neto Ajustado.

Actor

Proceso ETL / Power BI

Entrada

Proceso

Tabla  FACT_RENTABILIDAD  (Valor_FOB,  Volumen_Exportado)  +
(DIM_COSTO,  DIM_FINANZAS,  DIM_UBICACION,
dimensiones
DIM_EXPORTADOR)

Aplicar  fórmulas  documentadas  en  sección  2.5;  para  KPIs  derivados
(margen,  ratio),  calcular  en  Power  BI;  para  KPIs  agregados  (HHI,
concentración), calcular en ETL o vistas materializadas

Salida esperada  KPIs disponibles en dashboards de Power BI

Prioridad

Alta

RF08: Generación de reportes en Power BI

Atributo

Valor

Identificador

RF08

Nombre

Dashboards interactivos por stakeholder

Descripción

Actor

Entrada

El  sistema  debe  generar  dashboards  en  Power  BI  accesibles  para  cada
stakeholder,  con  visualizaciones  específicas  según  su  rol:  Gerencia
General (KPIs consolidados), Planeamiento (tendencias y concentración),
Finanzas (márgenes ajustados), Comercio Exterior (mercados y logística).

Gerencia General, Planeamiento Estratégico, Finanzas, Comercio Exterior

Data Mart (tablas FACT_RENTABILIDAD y dimensiones)

45

Proceso

Conectar Power BI al motor de base de datos (PostgreSQL/SQL Server);
crear  medidas  DAX  para  KPIs  derivados;  diseñar  visualizaciones  por
stakeholder

Salida esperada

4  dashboards  interactivos  (uno  por  área)  con  filtros  por  año,  país,
exportador, aduana

Prioridad

Alta

RF09: Clasificación automática de mercados "Premium"

Atributo

Valor

Identificador

RF09

Nombre

Identificación de mercados con TLC y arancel 0%

Descripción

Actor

Entrada

Proceso

El  sistema  debe  clasificar  automáticamente  los  países  destino  en  dos
categorías: "Premium" (aquellos con Tratado de Libre Comercio vigente
con  Perú  y  arancel del 0%) y "Estándar" (países sin TLC o con arancel
mayor a 0%).

Proceso ETL (población de DIM_PAIS_TLC) / Power BI

Tabla DIM_PAIS_TLC (campos Acuerdo_TLC, Arancel_Porcentaje)

Asignar  Categoria_Mercado  =  'Premium'  si  Acuerdo_TLC  IS  NOT
NULL y Arancel_Porcentaje = 0; caso contrario, 'Estándar'

Salida esperada

Segmentación  de  mercados  disponible  en  dashboards  para  filtrar  por
categoría

Prioridad

Media

RF10: Registro de trazabilidad (Log de ETL)

Atributo

Valor

Identificador

RF10

Nombre

Bitácora de ejecución del proceso ETL

Descripción

El  sistema  debe  generar  un  archivo  de  registro  (log)  cada  vez  que  se
ejecuta el proceso ETL, documentando la cantidad de registros extraídos,
transformados, cargados y rechazados, así como los errores encontrados.

46

Actor

Entrada

Proceso

Proceso ETL / Analista de BI

Datos procesados en cada fase del ETL

Al  inicio:  registrar  timestamp  y  parámetros  de  ejecución;  durante  la
extracción:  contar  registros  leídos  por  fuente;  durante  transformación:
contar  registros  filtrados  (incluidos/excluidos);  durante  carga:  contar
registros insertados por tabla; al final: escribir resumen en archivo .log

Salida esperada

Archivo etl_YYYYMMDD_HHMMSS.log con trazabilidad completa

Prioridad

Media

3.5.2 Requerimientos No Funcionales (RNF)

Los  requerimientos  no  funcionales  describen  atributos  de  calidad  que debe cumplir el sistema:
rendimiento, disponibilidad, seguridad, escalabilidad, usabilidad, mantenibilidad, confiabilidad y
portabilidad.

RNF01: Rendimiento

Atributo

Valor

Identificador

RNF01

Nombre

Descripción

Tiempo de procesamiento ETL

El  proceso ETL completo (extracción, transformación y carga)
para  el  total  de registros históricos (aproximadamente 100,000
registros  de  SUNAT  para palta Hass en el período 2016-2024)
debe  completarse  en  un  tiempo  máximo  de  5  minutos  en  un
equipo estándar (CPU i5, 8GB RAM).

Métrica

Tiempo  transcurrido  desde  el  inicio  de  la  extracción  hasta  la
finalización de la carga

Condición de aceptación

100%  de las ejecuciones exitosas deben cumplir con el tiempo
límite

Prioridad

Alta

RNF02: Disponibilidad

Atributo

Valor

Identificador

RNF02

47

Nombre

Disponibilidad del Data Mart para consultas

Descripción

El  Data  Mart  debe  estar  disponible  para  consultas  analíticas
durante  el  horario  laboral  (8:00  a.m.  a  6:00  p.m.,  de  lunes  a
viernes),  con  una  disponibilidad  mínima  del  99%  en  dicho
horario.

Métrica

Porcentaje de tiempo en que el Data Mart responde a consultas

Condición de aceptación

99%  de  disponibilidad  en  horario
mantenimientos programados)

laboral

(excluyendo

Prioridad

Alta

RNF03: Seguridad

Atributo

Valor

Identificador

RNF03

Nombre

Control de acceso por rol

Descripción

El  acceso  a  los  dashboards  de  Power  BI  y  a  las  tablas  del  Data
Mart debe estar restringido según el rol del usuario. Se definen 4
roles:  Administrador
(KPIs
consolidados),  Finanzas  (datos  financieros),  Comercio  Exterior
(datos operativos).

total),  Gerencia

(acceso

Métrica

Número de accesos no autorizados registrados

Condición de aceptación  Cero accesos no autorizados durante la operación normal

Prioridad

Alta

Atributo

Valor

Identificador

RNF03.1

Nombre

Confidencialidad de datos sensibles

Descripción

Los datos de exportación no deben ser modificables por usuarios
finales;  solo  el  proceso  ETL  automatizado  tiene  permisos  de
escritura en las tablas del Data Mart.

Condición de aceptación

Usuarios finales tienen solo permisos de lectura (SELECT)

48

Prioridad

Alta

RNF04: Escalabilidad

Atributo

Valor

Identificador

RNF04

Nombre

Capacidad de incorporar nuevos productos

Descripción

El  modelo  dimensional  debe  permitir  la incorporación de nuevos
productos  agroexportadores  (ej.  quinua,  mango,  arándanos)  sin
necesidad  de  rediseñar  la  arquitectura  completa.  Esto  se  logra
mediante  la  dimensión  DIM_PRODUCTO  y  el  filtro  de  partida
arancelaria.

Métrica

Esfuerzo estimado en horas para agregar un nuevo producto

Condición de aceptación

Agregar  un  nuevo  producto  no  debe  requerir  más  de  2  horas  de
trabajo (cambiar filtro de partida y actualizar documentación)

Prioridad

Media

RNF05: Usabilidad

Atributo

Valor

Identificador

RNF05

Nombre

Facilidad de uso de los dashboards

Descripción

Los  dashboards  de  Power  BI  deben  ser  intuitivos  y  no  requerir
capacitación extensa. Cada dashboard debe incluir: (1) título claro
del  análisis,  (2)  filtros  visibles  en  la  parte  superior,  (3)  tooltips
explicativos  al  pasar  el  cursor  sobre  los  gráficos,  (4)  botón  de
exportación a PDF/Excel.

Métrica

Tiempo  promedio  para que un usuario nuevo realice una consulta
básica

Condición de aceptación

Un usuario nuevo debe poder obtener el precio FOB/kg por país en
menos de 2 minutos sin ayuda externa

Prioridad

Media

RNF06: Mantenibilidad

49

Atributo

Valor

Identificador

RNF06

Nombre

Documentación del código ETL

Descripción

El  script  de  Python  del  proceso  ETL  debe  estar  completamente
documentado  con  comentarios  en  español  que  expliquen:  (1)  el
propósito de cada función, (2) las expresiones regulares utilizadas,
(3)  las  reglas  de  negocio  aplicadas,  (4)  el  orden  de  carga  de  las
tablas.

Métrica

Porcentaje de líneas de código con comentarios útiles

Condición de aceptación

Mínimo  20%  del  código debe contener comentarios explicativos;
todas las funciones deben tener docstring

Prioridad

Media

Atributo

Valor

Identificador

RNF06.1

Nombre

Control de versiones

Descripción

El  código  fuente  del  proyecto  (scripts  Python,  consultas  SQL,
documentación)  debe  mantenerse en un repositorio de control de
versiones (Git) con commits semánticos y etiquetas por versión.

Condición de aceptación

Repositorio  Git  con  historial  de  commits  y  etiquetas  v1.0,  v1.1,
etc.

Prioridad

Baja

RNF07: Confiabilidad

Atributo

Valor

Identificador

RNF07

Nombre

Calidad de datos en la tabla de hechos

Descripción

El  proceso  ETL  debe  garantizar  que  al  menos  el  95%  de  los  registros
extraídos  de  SUNAT  sean  válidos  y  se  carguen  correctamente  en
FACT_RENTABILIDAD.  Los  registros rechazados deben registrarse en el
log con la causa del rechazo.

50

Métrica

(Registros cargados exitosamente / Registros extraídos totales) × 100

Condición
aceptación

de

Tasa de éxito ≥ 95% en cada ejecución del ETL

Prioridad

Alta

RNF08: Portabilidad

Atributo

Valor

Identificador

RNF08

Nombre

Independencia del motor de base de datos

Descripción

El  script  ETL  debe  ser  compatible con al menos dos motores de
base  de  datos:  PostgreSQL  y  SQL  Server.  El  código  SQL  debe
evitar funciones específicas de un motor (ej. usar DATE estándar
en lugar de GETDATE() o NOW()).

Métrica

Número de motores de base de datos soportados

Condición de aceptación

El script ETL funciona sin modificaciones en PostgreSQL y SQL
Server

Prioridad

Baja

3.5.3 Trazabilidad de Requerimientos

La siguiente tabla vincula cada requerimiento funcional con los stakeholders que lo solicitaron y
los componentes técnicos involucrados:

ID Requerimiento

Stakeholder solicitante

Componente técnico involucrado

RF01

RF02

RF03

RF04

RF05

Analista de BI

ETL (Extracción)

Gerencia General

ETL (Transformación - Regex)

Comercio Exterior

ETL (Transformación - Regex)

Finanzas

ETL (Enriquecimiento) / DIM_FINANZAS

Comercio Exterior

ETL (Enriquecimiento) / DIM_PAIS_TLC

51

RF06

RF07

RF08

RF09

RF10

Finanzas

ETL  (Enriquecimiento)
(SCD Tipo 2)

/  DIM_COSTO

Gerencia  General
Finanzas

/

ETL + Power BI

Todos los stakeholders

Power BI

Gerencia  General
Comercio Exterior

/

DIM_PAIS_TLC + Power BI

Analista de BI

ETL (Logging)

4. DISEÑO DE ARQUITECTURA DE INTELIGENCIA DE NEGOCIOS

4.1 Tipo de Arquitectura Propuesta

La  arquitectura  de  Inteligencia  de  Negocios  seleccionada  es  una  arquitectura  bottom-up
(ascendente)  basada  en  un  Data  Mart  independiente,  estructurada  bajo  un  modelo dimensional
tipo  Copo  de  Nieve  (Snowflake  Schema).  Esta  evolución  respecto  al esquema estrella original
responde a la necesidad de:

●  Normalizar las jerarquías de las nuevas dimensiones (comerciales y financieras)
●  Evitar redundancias
●  Permitir un análisis más granular de la rentabilidad

Característica

Descripción

Alcance

Centrada  exclusivamente  en  el  análisis  de  rentabilidad  potencial  de  la
palta Hass

Fuentes de datos

Modelo de datos

Procesa microdatos de exportación de ADUANET (período 2016-2024) y
fuentes
(BCRP,  MINCETUR,
externas
MIDAGRI/Sierra Exportadora)

complementarias

Esquema  Copo
de  Nieve
(DIM_PAIS_TLC, DIM_VARIEDAD_CALIDAD)

con

subdimensiones  normalizadas

Salidas

Genera  información  para  la  toma  de  decisiones estratégicas de Peruvian
Andean Trout S.A.C.

KPIs que se calculan:

KPI

Descripción

52

Precio FOB/kg

Precio promedio por kilogramo exportado

Margen de Utilidad Estimado

Diferencia entre ingreso FOB y costo estimado

Ratio de Rentabilidad

Porcentaje de ganancia sobre el ingreso

Índice de Concentración (HHI)  Concentración de exportadores en el mercado

Margen Neto Ajustado

Rentabilidad considerando tipo de cambio y aranceles

4.2 Justificación de la Arquitectura

La arquitectura seleccionada responde a las siguientes razones:

Criterio

Justificación

Alcance acotado

El proyecto analiza un solo producto (palta Hass) con fuentes de datos
específicas, por lo que un Data Mart independiente es suficiente.

Tiempo y recursos

La  arquitectura  bottom-up  permite  obtener  resultados  rápidos  sin
necesidad de implementar un Data Warehouse corporativo completo.

53

Flexibilidad

Permite  incorporar  nuevas  fuentes  de  datos  (BCRP,  MINCETUR,
Sierra Exportadora) de manera incremental.

Rendimiento

Escalabilidad

El  esquema  Copo  de  Nieve  optimiza  las  consultas  de  los  KPIs
definidos  (precio,  margen,  ratio,  concentración)  al  precalcular  las
métricas derivadas en la tabla de hechos.

A  futuro,  el  Data  Mart  puede  integrarse  a  un  Data  Warehouse
empresarial  si  la  empresa  decide  expandir  la  solución  a  otros
productos o mercados.

Normalización
(Copo de Nieve)

La  evolución  al  modelo  Copo  de  Nieve  permite  normalizar  las
jerarquías  de las dimensiones (TLC por país, atributos de calidad por
producto), evitando redundancias y facilitando el mantenimiento.

Inteligencia
competitiva

la
inclusión  de  DIM_EXPORTADOR  permite  analizar
La
concentración del mercado (índice HHI) y el posicionamiento frente a
la competencia.

Análisis
realista

financiero

La  integración  de  BCRP (tipo de cambio) y MINCETUR (aranceles)
permite  ajustar
rentabilidad  a  condiciones
económicas  reales,  superando  la  limitación  de  los  datos  brutos  de
SUNAT.

los  márgenes  de

Casos de uso del sistema BI:

Actor

Caso de uso

Descripción

Gerencia
General

Visualizar  rentabilidad
potencial

Acceder  al  dashboard  con  KPIs  clave  (margen,
ratio, rentabilidad por destino).

Planeamiento
Estratégico

Identificar
mercados

mejores

Filtrar  por  país  destino  y  continente  para  ver
precios  FOB/kg  y  rentabilidad  ajustada  por
aranceles.

Comercio
Exterior

Finanzas

Análisis
competencia
logística

de
y

Identificar
(competidores)  y  aduanas  de
eficientes.

principales

exportadores
salida  más

Evaluar  concentración
de riesgo

Revisar  índice  de  concentración  por  destino  y
analizar  el  impacto  del  tipo  de  cambio  en  los
márgenes.

Detección de cuellos de botella:

Cuello de botella

Descripción

Solución propuesta

Descarga  manual  de
ADUANET

archivos  DBF/TXT

Los
requieren descarga manual

Automatizar  extracción  vía  script
programado en Python.

54

Limpieza de datos

Filtro de producto

Estimación de costos

Enriquecimiento
externo

Registros  duplicados,  valores
nulos  en  FOB,  y  textos  no
en
estructurados
DESC_ADIC.

Implementar  validaciones  en  fase
de  transformación  y  usar  Regex
para  extraer  atributos  (variedad,
calidad).

Inclusión  de  otras variedades,
pulpa  o  productos  procesados
que  distorsionan  el  precio
promedio.

Datos  SUNAT  sin  costos
reales
producción,
empaque o logística.

de

Falta  de  tipo  de  cambio  y
aranceles  para  ajustar
la
rentabilidad real.

Implementar  filtro  obligatorio para
registros  con
seleccionar
"HASS"
o
DESC_COM.

en  DESC_ADIC

solo

valores

Usar
documentados
Exportadora y MINCETUR

de
desde

referencia
Sierra

Integrar  API/CSV  de  BCRP  (tipo
de
de
MINCETUR (aranceles por país).

cambio)

tablas

y

4.3 Componentes de la Arquitectura

La arquitectura se compone de los siguientes elementos distribuidos en 4 capas:

Capa 1: Fuentes de datos

Componente

Descripción

Formato

ADUANET
(SUNAT)

Microdatos  de exportación de palta Hass (partida
0804400000).

DBF / TXT

BCRP (referencial)

Serie  histórica  de  tipo  de  cambio  (USD/PEN)
para ajuste de rentabilidad.

CSV / API

Sierra Exportadora

Costos  de  referencia  (producción,  empaque,
logística) y márgenes estándar del sector.

PDF / Excel

MINCETUR
(referencial)

Aranceles  aplicables  por  país  destino,  acuerdos
TLC, información de puertos.

CSV / Excel

Capa 2: Procesos ETL

Componente

Tecnología

Función

Extracción

Python (pandas, dbfread)

Leer archivos DBF/TXT desde ADUANET y
fuentes externas.

55

Transformación

Python  (pandas,  numpy,
re)

• Limpiar datos (eliminar duplicados, valores
nulos).
•  Filtrar  exclusivamente  variedad  HASS
(mediante
en
Regex
DESC_ADIC/DESC_COM).
•  Enriquecer  con  tipo  de  cambio  (BCRP)  y
aranceles (MINCETUR).
•  Extraer  atributos  para  subdimensiones
(variedad, calidad, método orgánico).
•  Calcular  KPIs:  Precio_FOB_kg  (en  Power
BI),
(mediante
lookup  a  DIM_COSTO  SCD  Tipo  2),
y  Ratio_Rentabilidad
Margen_Utilidad
(calculados dinámicamente en Power BI).

Costo_Total_Estimado

Carga

Python
psycopg2)

(SQLAlchemy,

Insertar datos en FACT_RENTABILIDAD y
tablas  de  dimensiones
(orden:  primero
dimensiones, luego hechos).

Capa 3: Almacenamiento analítico (Data Mart)

Componente

Descripción

Motor de base de datos

PostgreSQL / SQL Server (local o nube)

Tabla de hechos

FACT_RENTABILIDAD

Tablas  de  dimensiones
principales

Subdimensiones
(normalización  Copo  de
Nieve)

DIM_TIEMPO,
DIM_VARIEDAD_CALIDAD,
DIM_ADUANA, DIM_FINANZAS, DIM_COSTO

DIM_UBICACION,

DIM_PRODUCTO,
DIM_EXPORTADOR,

DIM_PAIS_TLC (conectada a DIM_UBICACION)

Nota:  `DIM_VARIEDAD_CALIDAD`  es  una  dimensión  independiente,  no  una  subdimensión
de `DIM_PRODUCTO`. Su FK está directamente en `FACT_RENTABILIDAD`.

56

Capa 4: Visualización y análisis

Componente

Tecnología

Función

Dashboard

Power BI

Visualización
tendencias temporales

de  KPIs,  mapas,

Reportes

Power BI (exportable a PDF)

Reportes ejecutivos de rentabilidad

Jerarquías de datos implementadas:

Dimensión

Jerarquía

DIM_TIEMPO

Año → Trimestre → Mes → Semana → Fecha

DIM_UBICACION

Continente → País

DIM_PRODUCTO

Partida arancelaria → Variedad (Hass)

DIM_PAIS_TLC
(subdimensión)

DIM_VARIEDAD_CALIDAD
(dimensión independiente)

Granularidad del modelo:

País → Acuerdo TLC → Arancel aplicable

Variedad → Categoría de calidad → Método de producción

Nivel

Granularidad

Descripción

Fina

Por  ítem  de  declaración  (cada
línea de producto)

Registro  individual  de  exportación  (DUA).
Permite
competidor
(DIM_EXPORTADOR).

análisis

por

Media

Por mes y destino

Agregación de precios y volúmenes por país
y mes.

Gruesa

Por año y continente

Tendencia  anual  de  rentabilidad  por  región
geográfica.

5. MODELAMIENTO DIMENSIONAL

57

5.1 Tabla de Hechos: FACT_RENTABILIDAD

La  tabla  de  hechos  FACT_RENTABILIDAD  es  el  centro  del  modelo  y  almacena  las  métricas
cuantitativas asociadas a cada operación de exportación de palta Hass.

Granularidad: Fina, correspondiendo a cada ítem o línea de producto dentro de una Declaración
Única de Aduanas (DUA).

inmutables  (Valor_FOB,
Principio  de  diseño:  Solo  se  almacenan  hechos  atómicos  e
Volumen_Exportado).  Las  métricas  derivadas
(Precio_Promedio_kg,  Margen_Utilidad,
Ratio_Rentabilidad)  se  calculan  en  tiempo  de  consulta  (vistas  o  Power  BI)  para  garantizar
consistencia ante actualizaciones de costos de referencia.

Estructura de la tabla de hechos:

Campo

Tipo de dato

Descripción

Fuente / Cálculo

ID_Rentabilidad
(PK)

INTEGER

Identificador  único
de cada registro

Autogenerado (SERIAL)

FK_Tiempo

INTEGER

FK_Ubicacion

INTEGER

FK_Producto

INTEGER

FK_Variedad_Calida
d

INTEGER

FK_Exportador

INTEGER

FK_Aduana

INTEGER

FK_Finanzas

INTEGER

Llave
foránea
DIM_TIEMPO

a

Asignación
FECHA (SUNAT)

desde

Llave
a
DIM_UBICACION.

foránea

Asignación
CPAIS/PAIS_DESC
(SUNAT)

desde

Llave
a
DIM_PRODUCTO.

foránea

Asignación  desde  CNAN
(SUNAT)

foránea

a
Llave
DIM_VARIEDAD_
CALIDAD

Asignación
extracción  Regex
DESC_ADIC

desde
en

foránea

Llave
DIM_EXPORTAD
OR

a

Asignación
desde
NRO_DOCU/EXPORTA
DOR (SUNAT)

Llave
foránea
DIM_ADUANA

a

Asignación
CADUANA/ADUA_DE
SC (SUNAT)

desde

Llave
DIM_FINANZAS

foránea

a

Asignación  por  fecha  y
país
+
MINCETUR)

(BCRP

58

FK_Costo

INTEGER

Valor_FOB

DECIMAL(18,2)

foránea

a
Llave
DIM_COSTO (SCD
Tipo 2)

FOB

Valor
dólares
estadounidenses

en

Asignación  por  fecha  y
región destino

Campo  FOB_DOLPOL
(SUNAT)

Volumen_Exportado  DECIMAL(18,2)

Peso
kilogramos

neto

en

Campo
(SUNAT)

PESO_NETO

Nota  sobre
las  claves  foráneas:  Todas  las  dimensiones  (`TIEMPO`,  `UBICACION`,
`PRODUCTO`,  `VARIEDAD_CALIDAD`,  `EXPORTADOR`,  `ADUANA`,  `FINANZAS`,
`COSTO`) se relacionan mediante FK directas, garantizando integridad referencial y cumpliendo
con el modelo Snowflake.

5.2 Tablas de Dimensiones

Las  tablas  de  dimensiones  proporcionan  el  contexto  descriptivo  para  segmentar  y  filtrar  los
análisis.  En  el  modelo  de  Copo  de  Nieve,  algunas  dimensiones  se  han  normalizado  en
subdimensiones para evitar redundancias.

DIM_TIEMPO

Permite el análisis temporal de la rentabilidad, con jerarquías que van desde el año hasta el día.

Campo

Tipo de dato

Descripción

Ejemplo

ID_Tiempo (PK)

INTEGER

Fecha

Año

DATE

INTEGER

Trimestre

INTEGER

Mes

INTEGER

Identificador
de la fecha.

único

20240629

Fecha  completa  de
embarque

2024-06-29

Año
exportación

de

la

2024

Trimestre  del  año
(1-4)

Número
(1-12)

de  mes

2

6

Mes_Nombre

VARCHAR(20)

Nombre del mes

Junio

59

Semana_Año

INTEGER

Semana
(1-52).

del

año

26

Jerarquía temporal: Año → Trimestre → Mes → Semana → Fecha

DIM_UBICACION

Permite  el  análisis  por  mercado  de  destino.  Se  ha  normalizado  para  separar  la  información
geográfica base de los acuerdos comerciales.

Campo

Tipo de dato

Descripción

Ejemplo

ID_Ubicacion (PK)

INTEGER

Pais_Codigo

VARCHAR(3)

Pais_Nombre

VARCHAR(100)

Identificador
del país

único

1

Código
(CPAIS)

Nombre
destino

de

país

CA

del

país

Canadá

Continente

VARCHAR(50)

Continente  al  que
pertenece

América del Norte

Jerarquía geográfica: Continente → País

Subdimensión: DIM_PAIS_TLC (se relaciona 1:1 con DIM_UBICACION)

Campo

Tipo de dato

Descripción

Ejemplo

ID_Pais_TLC (PK)

INTEGER

FK_Ubicacion

INTEGER

Identificador  único  del
acuerdo

Llave
foránea
DIM_UBICACION

a

1

1

Acuerdo_TLC

VARCHAR(100)

Tratado
Comercio vigente

de

Libre

TLC
Perú-Canadá

Arancel_Porcentaje

DECIMAL(5,2)

Arancel aplicable

0.00

Categoria_Mercado

VARCHAR(20)

Clasificación
(Premium/Estándar)

Premium

DIM_PRODUCTO

60

Contiene la información específica del producto analizado: palta Hass.

Campo

Tipo de dato

Descripción

Ejemplo

ID_Producto (PK)

INTEGER

Identificador
del producto

único

1

Partida_Arancelaria

VARCHAR(10)

Código  de  partida
(CNAN).

0804400000

Descripcion

VARCHAR(200)

Descripción
comercial oficial.

AGUACATES
(PALTAS)
FRESCOS O SECOS

DIM_VARIEDAD_CALIDAD

Campo

Tipo de dato

Descripción

Ejemplo

ID_Variedad_Calidad
(PK)

INTEGER

Identificador
del producto

único

1

Variedad

VARCHAR(50)

Categoria_Calidad

VARCHAR(20)

Metodo_Produccion  VARCHAR(30)

Fuente_Extraccion

VARCHAR(100)

Variedad
producto.

del

Hass

Categoría  de  calidad
(CAT 1, CAT 2, etc.).

CAT 1

Orgánico
Convencional.

o

Convencional

Campo  SUNAT  de
origen (DESC_ADIC
/ DESC_COM).

DESC_ADIC

DIM_EXPORTADOR

Identifica  a  los  actores  del  mercado  (competidores)  que  participan  en  la  exportación  de  palta
Hass.

Campo

Tipo de dato

Descripción

Ejemplo

ID_Exportador (PK)

INTEGER

Identificador
del exportador.

único

1

RUC

VARCHAR(11)

Número  de  RUC  de
la empresa.

20535674010

61

Razon_Social

VARCHAR(200)

Razón
exportador.

social

del

SIEMBRA
S.A.C.

ALTA

Tipo_Empresa

VARCHAR(50)

Clasificación  (Gran,
MYPE, etc.).

S.A.C.

DIM_ADUANA

Describe los puntos de salida (aduanas y puertos) de las exportaciones.

Campo

Tipo de dato

Descripción

Ejemplo

ID_Aduana (PK)

INTEGER

Codigo_Aduana

VARCHAR(10)

Nombre_Aduana

VARCHAR(100)

Region

VARCHAR(50)

Identificador
de la aduana.

único

1

Código  oficial  de  la
aduana.

046

o
Descripción
nombre de la aduana.

PAITA

donde
Región
ubica la aduana.

se

Piura

Tipo_Aduana

VARCHAR(30)

Marítima,  Terrestre,
etc.

MARITIMA

DIM_FINANZAS

Esta  dimensión  integra  los  datos  económicos  externos  que  afectan la rentabilidad neta: tipo de
cambio  (USD/PEN)  y  aranceles  de  importación  por  país  destino.  Responde  a  la  exigencia
docente de incluir explícitamente una dimensión financiera en el modelo Snowflake.

Campo

Tipo de dato

Descripción

Ejemplo

ID_Finanzas (PK)

INTEGER

Identificador único

1

Fecha_Referencia

DATE

FK_Ubicacion

INTEGER

Fecha  del
cambio

tipo  de

2024-06-01

Llave
DIM_UBICACION

foránea

a

1

Tipo_Cambio_USD_
PEN

DECIMAL(10,4)

Tipo
de
promedio (BCRP)

cambio

3.75

Arancel_Porcentaje

DECIMAL(5,2)

Arancel
(MINCETUR)

aplicable

0.00

62

Acuerdo_TLC

VARCHAR(100)

Tratado
comercio vigente

de

libre

TLC
Unidos

Perú-Estados

Fuente_BCRP

VARCHAR(50)

Fecha  de  extracción
del dato

2024-04-15

Fuente_MINCETUR  VARCHAR(50)

Versión del arancel

2024-01-01

DIM_COSTO (SCD Tipo 2)

Estructura  los  costos  estimados  por  tipo,  permitiendo  calcular  el  costo  total  por  operación  de
exportación. Utiliza una estrategia SCD Tipo 2 (Slowly Changing Dimension) para mantener el
historial de cambios en los costos de producción, empaque y logística.

Campo

Tipo de dato

Descripción

Ejemplo

ID_Costo (PK)

INTEGER

Tipo_Costo

VARCHAR(50)

Region_Destino

VARCHAR(50)

Valor_Unitario_USD

DECIMAL(18,4)

Fecha_Vigencia_Inicio  DATE

Fecha_Vigencia_Fin

DATE

Es_Vigente

BOOLEAN

Ejemplo de registros en DIM_COSTO:

Identificador
del tipo de costo

único

1

Producción
/
Empaque / Logístico

Logístico

América  /  Europa  /
Asia

Europa

Costo  estimado  por
kg (USD)

0.35

Desde  cuándo  aplica
este costo

2020-01-01

Hasta  cuándo  aplica
(NULL = vigente)

NULL

TRUE
registro activo

si

es

el

TRUE

ID_Costo  Tipo_Costo

Region_D
estino

Valor_Uni
tario_US
D

Fecha_Vi
gencia_Ini
cio

Fecha_Vi
gencia_Fi
n

Es_Vigent
e

63

1

2

3

4

5

6

Producción  Global

0.45

2016-01-0
1

2022-12-3
1

FALSE

Producción  Global

0.52

Logístico

Europa

0.35

Logístico

Asia

0.50

Logístico

América

0.25

Empaque

Global

0.15

2023-01-0
1

2016-01-0
1

2016-01-0
1

2016-01-0
1

2016-01-0
1

NULL

TRUE

NULL

TRUE

NULL

TRUE

NULL

TRUE

NULL

TRUE

Nota:  A  diferencia de una tabla de parámetros externa, DIM_COSTO se implementa como una
dimensión  tradicional  con  llave  foránea  FK_Costo  en  FACT_RENTABILIDAD.  Esto  permite
que  cada  transacción  de  exportación  esté  vinculada  a  los  costos  de  referencia  vigentes  en  su
momento.

5.3 Relaciones entre Tablas

El modelo implementado es un esquema de Copo de Nieve (Snowflake Schema). Esta evolución
respecto al esquema estrella original responde a la necesidad de normalizar las jerarquías de las
nuevas  dimensiones  (Comercialización y Financiera), evitar redundancias y permitir un análisis
más  granular  de  la  rentabilidad.  La  tabla  de  hechos  `FACT_RENTABILIDAD`  se  mantiene
como  centro  del modelo, excluyendo campos derivados (margen, ratio). Las métricas derivadas
se  calculan  en  la  capa  de  visualización  (Power  BI)  mediante  medidas  DAX,  lo  que  garantiza
consistencia ante actualizaciones de los costos de referencia en `DIM_COSTO`.

Esquema estrella original:

64

Esquema de Copo de Nieve:

Las  dimensiones  principales  (DIM_UBICACION,  DIM_PRODUCTO)  se  normalizan  en
subdimensiones  (DIM_PAIS_TLC,  DIM_VARIEDAD_CALIDAD)  para  evitar  redundancias  y
permitir análisis más granulares.

FACT_RENTABILIDAD se relaciona con TODAS las dimensiones (N:1):

●  fk_tiempo           → DIM_TIEMPO
●  fk_ubicacion        → DIM_UBICACION
●  fk_producto         → DIM_PRODUCTO
●  fk_variedad_calidad → DIM_VARIEDAD_CALIDAD  (CORREGIDO: independiente)
●  fk_exportador       → DIM_EXPORTADOR
●  fk_aduana           → DIM_ADUANA
●  fk_finanzas         → DIM_FINANZAS          (NUEVA)
●  fk_costo            → DIM_COSTO             (CORREGIDO: con FK directa)

Normalización Copo de Nieve (subdimensiones):

-  DIM_UBICACION  →  DIM_PAIS_TLC  (1:1)  -  Acuerdos  comerciales  y  aranceles  por

país

NOTAS:

-  DIM_VARIEDAD_CALIDAD  ya  NO  es  subdimensión  de  DIM_PRODUCTO.  Es  una

dimensión independiente.

-  DIM_COSTO ya NO es tabla de parámetros. Es una dimensión tradicional con SCD Tipo

2 y FK directa.

DIMENSIONES IMPLEMENTADAS:

65

●  DIM_TIEMPO
●  DIM_UBICACION
●  DIM_PAIS_TLC (subdimensión de DIM_UBICACION - normalización Snowflake)
●  DIM_PRODUCTO
●  DIM_VARIEDAD_CALIDAD (independiente)
●  DIM_EXPORTADOR
●  DIM_ADUANA
●  DIM_FINANZAS (nueva - tipo cambio + aranceles)
●  DIM_COSTO (SCD Tipo 2 - con FK directa)

MÉTRICAS DERIVADAS (NO en FACT_RENTABILIDAD):

-  Precio_Promedio_kg   = valor_fob / volumen_exportado
-  Margen_Utilidad      = valor_fob - (costo_total_segun_DIM_COSTO)
-  Ratio_Rentabilidad   = (margen / valor_fob) * 100

Estas métricas se calculan en la capa de visualización (Power BI) o en vistas materializadas del
Data Mart.

66

6. PROCESOS ETL

6.1 Entorno de Desarrollo (IDE)

El  IDE  (Entorno  de  Desarrollo  Integrado)  es la herramienta de software utilizada para escribir,
depurar  y  ejecutar  el  código  del  proceso  ETL.  Para  el  presente  proyecto,  se  seleccionó Visual
Studio Code (VS Code) como IDE principal.
A  continuación,  se  detalla  la  justificación  de  la  elección,  las  extensiones  utilizadas,  la
configuración del entorno y las alternativas evaluadas.

6.1.1 IDE Seleccionado

Atributo

Valor

Nombre

Versión

Visual Studio Code (VS Code)

1.85 o superior

Desarrollador

Microsoft

Licencia

Gratuita (Open Source)

Sitio oficial

https://code.visualstudio.com

6.1.2 Justificación de la Elección

La selección de Visual Studio Code se basa en los siguientes criterios técnicos y prácticos:

Criterio

Justificación

¿Cómo aplica al proyecto?

Soporte
nativo  para
Python

VS  Code  tiene  integración  oficial
con  Python  mediante  la  extensión
de  Microsoft,  que  incluye  linting,
y
autocompletado,
depuración paso a paso.

formateo

El ETL está completamente programado
en  Python con librerías pandas, dbfread,
re,  sqlalchemy.  La  depuración  paso  a
las
fue  esencial  para  validar
paso
expresiones  regulares  (Regex)  y
las
transformaciones de datos.

Ligereza
y
rendimiento

VS Code consume menos memoria
RAM  que  otros
IDEs  como
PyCharm
(aproximadamente
300-500 MB vs 1-2 GB).

de

equipo

desarrollo

utilizó
El
computadoras  con  recursos  limitados  (8
GB  RAM).  La  ligereza  de  VS  Code
permitió  ejecutar  el  ETL  y  las  pruebas
sin afectar el rendimiento del sistema.

Integración
con Git

incluye  control  de
VS  Code
versiones
(Git)  con
integrado
interfaz  gráfica  para  commits,
de
branches
conflictos.

resolución

y

Terminal
integrada

permite

ejecutar
VS  Code
comandos  directamente  dentro  del
IDE,  sin  necesidad  de  ventanas
externas.

67

El proyecto requirió control de versiones
para mantener el historial del script ETL,
las  consultas  SQL  y  la  documentación.
Se  utilizaron  commits  semánticos  y
etiquetas (v1.0, v1.1).

Se  utilizó  la  terminal  integrada  para
ejecutar  el  script  ETL,  instalar  librerías
(pip  install  pandas  dbfread  sqlalchemy
psycopg2)  y  ejecutar  consultas  SQL  de
validación.

Extensiones
especializad
as

VS  Code  cuenta  con  un  amplio
marketplace
extensiones
de
gratuitas.

instalaron  extensiones  específicas

Se
para el proyecto (ver tabla en 6.1.3).

Multiplatafo
rma

VS  Code  funciona  en  Windows,
Linux y macOS.

Jupyter
Notebooks
integrados

VS  Code  permite  ejecutar  celdas
de  código  interactivas  similares  a
Jupyter Notebooks.

El equipo de desarrollo utilizó Windows
10/11,  mientras  que  el  servidor  de  base
de  datos  fue  PostgreSQL  en  Linux
(Ubuntu).
funcionó
consistentemente en ambos entornos.

Code

VS

Se utilizaron notebooks interactivos para
explorar  los  datos  crudos  de  SUNAT,
probar  expresiones  regulares  (Regex)  y
de
validar
integrarlas al script ETL final.

transformaciones

antes

Depuración
de SQL

VS  Code  tiene  extensiones  para
conectarse  a  bases  de  datos  y
ejecutar
con
resaltado de sintaxis.

consultas  SQL

Se  utilizó  la  extensión  "PostgreSQL"
para  ejecutar  consultas  de  validación
directamente desde el IDE.

6.1.3 Extensiones Instaladas en VS Code

Extensión

Propósito en el proyecto

Python (Microsoft)

Linting,  autocompletado,  formateo  (Black),  depuración  paso  a
paso, ejecución de pruebas unitarias.

Pylance (Microsoft)

Servidor  de
autocompletado avanzado.

lenguaje  Python  para  análisis  de

tipos  y

Jupyter (Microsoft)

Ejecución de notebooks interactivos para exploración de datos y
pruebas de Regex.

68

Excel Viewer

Visualización  de  archivos  Excel  de  costos  referenciales  y
aranceles dentro del IDE.

PostgreSQL
Kolkman)

(Chris

Conexión a la base de datos PostgreSQL, ejecución de consultas
SQL, visualización de tablas y esquemas.

GitLens

Visualización  avanzada  del  historial  de  Git  (autores,  fechas,
comparación de versiones).

Better Comments

Resaltado  de  comentarios  en  el  código  por  categoría  (TODO,
FIXME, IMPORTANTE).

Regex Previewer

Visualización  en  tiempo  real  de  las  expresiones  regulares
aplicadas a texto de ejemplo (útil para validar filtros de "HASS"
y exclusión de "PULPA", "CONGELADO").

6.1.4 Configuración del Entorno de Desarrollo

A continuación, se detalla la configuración específica utilizada para el proyecto:
Configuración del intérprete de Python

Parámetro

Valor

Versión de Python

3.9 o superior

Entorno virtual

venv (creado con python -m venv etl_env)

Archivo de requerimientos

requirements.txt  con  las  librerías:  pandas,  dbfread,  numpy,
sqlalchemy, psycopg2-binary, openpyxl, python-dotenv

Configuración del depurador (launch.json)

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: ETL Principal",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/etl_main.py",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            },
            "args": ["--year", "2024", "--test-mode"]
        }

69

    ]
}

Configuración de variables de entorno (.env)

# Conexión a base de datos
DB_HOST=localhost
DB_PORT=5432
DB_NAME=datamart_palta
DB_USER=etl_user
DB_PASSWORD=******

# Rutas de archivos
SUNAT_DATA_PATH=C:/data/sunat/
BCRP_FILE_PATH=C:/data/bcrp/tipo_cambio.csv
MINCETUR_FILE_PATH=C:/data/mincetur/aranceles.xlsx
COSTOS_FILE_PATH=C:/data/costos/dim_costo.csv

6.1.5 Alternativas Evaluadas

Antes de seleccionar VS Code, se evaluaron las siguientes alternativas:

Criterio

VS Code

PyCharm
(Community)

Jupyter
Notebook

Sublime Text

Precio

Gratuito

Gratuito
(Community)

Gratuito

Shareware
(USD 99)

Consumo
RAM

de

~300-500 MB

~1-2 GB

~500-800 MB

~150-300 MB

Depuración paso
a paso

Sí

Sí

Limitada

No

Sí (nativa)

Sí (nativa)

Limitada

Con plugin

Integración  con
Git

Terminal
integrada

Sí

Sí

Extensiones
para SQL

Sí  (PostgreSQL,
SQL Server)

(Database

Sí
Tools)

No

No

No

No

70

Soporte
Jupyter

para

Sí (nativo)

(requiere

Sí
versión
Professional)

Sí (nativo)

No

Curva
aprendizaje

de

Baja

Media

Baja

Media

Rendimiento
con
archivos
grandes  (100k+
registros)

Bueno

Bueno

Lento

Bueno

Decisión  final:  Se  eligió  VS  Code  porque  ofrece  el  mejor  equilibrio  entre  funcionalidad,
rendimiento  y  costo  cero,  cubriendo  todas las necesidades del proyecto: depuración de Python,
control  de  versiones,  conexión  a  bases  de  datos  y  ejecución  de  notebooks  interactivos  para
pruebas de Regex.

6.1.6 Evidencia de uso en el proyecto

Fase del proyecto

Uso de VS Code

Herramienta/Extensión
utilizada

Exploración de datos

Análisis  exploratorio  de  datos
(EDA) de SUNAT y BCRP

Jupyter  Notebook  +  Python
(pandas)

Desarrollo de Regex

Validación
regulares para filtrar "HASS"

de

expresiones

Regex  Previewer  +  Python  (re
module)

Programación ETL

Escritura  y  depuración  del  script
principal (etl_main.py)

Python  extension  +  Depurador
paso a paso

Pruebas unitarias

Validación
de
transformación

funciones  de

Python testing (pytest)

Control de versiones  Commits, branches, etiquetas

Git integrado + GitLens

Carga de datos

Ejecución  del  ETL  y  monitoreo
de logs

Terminal integrada

Validación
integridad

de

Ejecución  de  consultas  SQL  de
verificación

PostgreSQL extension

6.2 Fase de Extracción

Se  implementará  un  proceso  automatizado  desarrollado  en  Python  (utilizando  las  librerías
pandas,  dbfread  y  sqlalchemy)  encargado  de  la  descarga,  integración  y  consolidación  de  los

71

microdatos  de  exportación  provenientes  de  ADUANET,  así  como  de  fuentes  externas
complementarias (BCRP, MINCETUR, Sierra Exportadora).

Fuente de datos:

Fuente

Datos extraídos

Formato

Periodicidad

SUNAT
(ADUANET)

Microdatos  de  exportación  de
palta Hass (partida 0804400000)

DBF / TXT

Mensual
manual programada)

(descarga

BCRP

de

Tipo
promedio
cambio
(USD/PEN)  para  el  período
2016-2024

CSV / API

Extracción
(histórica)

única

MINCETUR

Aranceles  aplicables  por  país
destino y acuerdos TLC

CSV / Excel

Extracción  única  con
actualizaciones anuales

Sierra
Exportadora

Costos de referencia (producción,
empaque, logística)

PDF / Excel

Extracción
(referencial)

única

Variables extraídas desde SUNAT:

Variable

Campo en ADUANET

Uso en el Data Mart

Fecha de embarque

FECHA

DIM_TIEMPO

País destino

CPAIS, PAIS_DESC

DIM_UBICACION

Partida arancelaria

CNAN

Valor FOB

FOB_DOLPOL

Peso neto

PESO_NETO

DIM_PRODUCTO
para Hass)

(filtro

FACT_RENTABILIDAD.Val
or_FOB

FACT_RENTABILIDAD.Vol
umen_Exportado

Exportador  (RUC  y  razón
social)

NRO_DOCU,
EXPORTADOR

DIM_EXPORTADOR

Aduana de salida

CADUANA, ADUA_DESC  DIM_ADUANA

Descripción adicional

DESC_ADIC, DESC_COM

DIM_VARIEDAD_CALIDA
D (extracción de atributos)

72

Nota:  El  campo  EXPORTADOR  se extrae como identificador del competidor. No se incorpora
como cliente final porque SUNAT no registra al importador.

Problemas identificados en la fuente:

Problema

Descripción

Solución en ETL

Inconsistencias
países

en

Abreviaturas,
ortográficas,
mapeados

faltas
no

códigos

Normalización  mediante  diccionario
de mapeo

Formatos de fecha

Fecha en AAAAMMDD

Estandarización  a  DATE  y  extracción
de Año, Mes, Trimestre, Semana

Valores
incompletos

nulos

o

Especialmente  en  campos
opcionales

Registros  con  FOB  o  PESO_NETO
nulos son excluidos

Registros duplicados  Misma DUA repetida

Eliminación basada en NRO_DOCU +
FECHA + CNAN

Texto
estructurado

no

Variedad
calidad
incrustados en DESC_ADIC

y

Extracción  con  Regex  (expresiones
regulares)

6.3 Fase de Transformación

La  fase  de  transformación  tiene  como objetivo asegurar la calidad, consistencia y estructura de
los  datos,  mediante  su  limpieza,  estandarización,  integración  y  adecuación  al  modelo
dimensional de Copo de Nieve.

Subproceso 1: Limpieza y Validación de Datos SUNAT

Operación

Descripción

Deduplicación

Basada  en  NRO_DOCU  +  FECHA  +  CNAN  +  ITEM  +
PESO_NETO.  La inclusión de ITEM (número de ítem dentro de la
DUA)  y  PESO_NETO  evita  la  pérdida  de  registros  cuando  una
misma  declaración  contiene  múltiples  líneas  con  la  misma  partida
arancelaria

Normalización de texto

Los  campos  DESC_ADIC  y  DESC_COM  se  convierten  a
mayúsculas (upper())

Filtro positivo

Se  retienen  registros  donde  la  expresión  regular  r'\bHASS?\b'
aparece en al menos un campo

73

Filtro negativo

Se  excluyen
CONGELADO o PROCESAMIENTO

registros  que  contengan  PULPA,  TROZOS,

Validación de valores

Se  excluyen registros con FOB_DOLPOL o PESO_NETO nulos, y
se verifica FOB_DOLPOL > 0 y PESO_NETO > 0

Subproceso 2: Estandarización y Normalización

Operación

Descripción

Homogeneización de moneda  Todos los valores convertidos a USD

Homogeneización
unidades

de

Consistente en kilogramos

Normalización de países

Mediante  diccionario  de  mapeo.  El  continente  se  añade
externamente

Limpieza de exportadores

EXPORTADOR  =  EXPORTADOR.upper().replace('  S.A.C.',
'').replace(' S.A.', '')

Extracción de atributos

Variedad,  calidad  y  método  orgánico  desde  DESC_ADIC
usando Regex

Subproceso 3: Enriquecimiento con Fuentes Externas

Fuente

Datos incorporados

Método de integración

BCRP

Tipo  de  cambio  (USD/PEN)
por fecha

merge  por  fecha  entre  DIM_TIEMPO
y serie BCRP

MINCETUR

Acuerdo  TLC  y  arancel  por
país

por

merge
DIM_UBICACION
aranceles

PAIS_DESC
y

tabla

entre
de

MIDAGRI  /  Sierra
Exportadora

Costo
empaque,
región

de

producción,
por

logístico

Carga  directa  a  DIM_COSTO  como
dimensión SCD Tipo 2 con FK directa
desde FACT_RENTABILIDAD

Integración
DIM_FINANZAS

de

Tipo  de  cambio  +  aranceles
por fecha y país

Subproceso 4: Cálculo de Indicadores

merge  por  fecha  entre  DIM_TIEMPO
entre
y  BCRP,
DIM_UBICACION y MINCETUR

país

por

y

74

Indicador

Fórmula

Destino

Precio_Promedio_kg

FOB_DOLPOL
PESO_NETO

/

Se  calcula  en  Power  BI  (no  se
en
almacena
FACT_RENTABILIDAD)

Costo_Total_Estimado

Σ(Valor_unitario_DIM_COS
TO × Volumen_Exportado)

Power  BI
(mediante
DIM_COSTO vigente)

lookup  a

Margen_Utilidad

FOB_DOLPOL
Costo_Total_Estimado

Ratio_Rentabilidad

(Margen_Utilidad
FOB_DOLPOL) × 100

-

/

Se  calcula  en  Power  BI  (no  se
almacena
en
FACT_RENTABILIDAD)

Se  calcula  en  Power  BI  (no  se
en
almacena
FACT_RENTABILIDAD)

Nota  importante:  Siguiendo  el  principio  de  Kimball  de  hechos  atómicos,  ninguna  de  estas
métricas  derivadas  se  almacena  físicamente  en  FACT_RENTABILIDAD.  Se  calculan
dinámicamente  en  la  capa  de  visualización  (Power  BI)  utilizando los valores de DIM_COSTO
vigentes  para  cada  período,  garantizando  consistencia  ante  actualizaciones  de  costos  de
referencia.

Modelado dimensional (organización de tablas)

Los  datos  transformados  se  organizan  en  la  tabla  de  hechos  FACT_RENTABILIDAD  y  las
siguientes  tablas,  incorporando  claves  sustitutas  (surrogate  keys)  para  optimizar  la  gestión
histórica:

Tipo

Tablas

Dimensiones principales

DIM_TIEMPO,  DIM_UBICACION,  DIM_PRODUCTO,
DIM_VARIEDAD_CALIDAD,  DIM_EXPORTADOR,
DIM_ADUANA, DIM_FINANZAS, DIM_COSTO

Subdimensiones (normalización)  DIM_PAIS_TLC (conectada a DIM_UBICACION)

Nota: DIM_COSTO es una dimensión tradicional con SCD Tipo 2 y FK directa. No existe tabla
de parámetros en este modelo.

6.4 Fase de Carga

La fase de carga consiste en la inserción de los datos previamente transformados en el Data Mart,
asegurando su disponibilidad para el análisis y la generación de reportes.

Estrategia de carga:

75

Parámetro

Valor

Tipo de carga

Carga  completa
inicial
incrementales mensuales

(histórico  2016-2024)  +  actualizaciones

Orden de carga

Motor  de  base  de
datos

Primero dimensiones y subdimensiones, luego tabla de hechos

PostgreSQL / SQL Server (local o en la nube)

Estructura de almacenamiento:
El  Data  Mart  se  implementa  en  una  base  de  datos  relacional  SQL  Server  (o  PostgreSQL),
utilizando un esquema de Copo de Nieve que optimiza el rendimiento de consultas analíticas.

Secuencia de carga (orden estricto por integridad referencial):

●  Carga de dimensiones independientes (sin FK a otras tablas):

○  `DIM_TIEMPO` (generación de fechas)
○  `DIM_COSTO` (carga desde Sierra Exportadora con SCD Tipo 2)

●  Carga de dimensiones con dependencias externas:

○  `DIM_UBICACION` (después de limpiar países)
○  `DIM_PAIS_TLC` (después de DIM_UBICACION)
○  `DIM_PRODUCTO` (después del filtro Hass)
○  `DIM_VARIEDAD_CALIDAD` (después de DIM_PRODUCTO)
○  `DIM_EXPORTADOR` (después de limpiar RUC y razón social)
○  `DIM_ADUANA` (después de limpiar códigos de aduana)
○  `DIM_FINANZAS` (después de DIM_TIEMPO y DIM_UBICACION)

●  Carga de tabla de hechos:

○  `FACT_RENTABILIDAD` (con asignación de todas las llaves foráneas:
FK_Tiempo, FK_Ubicacion, FK_Producto, FK_Variedad_Calidad,
FK_Exportador, FK_Aduana, FK_Finanzas, FK_Costo)

Validación y control de calidad:

Verificación

Descripción

Acción ante error

Integridad
referencial

Consistencia
cálculos

de

Verificar que no existan FK nulos o inválidos

Rechazar
registrar en log

registro  y

Validar que Ratio = (Margen / FOB) × 100

Recalcular o rechazar

Conteo
registros

de

Comparar registros transformados vs cargados

Registrar  diferencia  en
log

Log de control

Registrar  registros  procesados,  insertados  y
rechazados

Archivo de log diario

76

6.5 Proceso de Normalización de Datos (1NF → 5NF)

Para garantizar la calidad, consistencia e integridad de los datos almacenados en el Data Mart, se
aplicó  un  proceso  sistemático  de  normalización  basado  en  las  Formas  Normales  (1NF  a  5NF)
propuestas  por  Edgar  F.  Codd.  Este  proceso  transformó  los  datos  crudos  de  SUNAT  (formato
plano  y  desnormalizado)  en  un  modelo  dimensional  tipo  Copo  de  Nieve  (Snowflake  Schema)
optimizado para análisis OLAP.
A continuación, se documenta cada etapa con ejemplos prácticos, código utilizado y validaciones
aplicadas.

6.5.1 Paso 0: Estado Inicial (Forma Desnormalizada - 0NF)

Descripción:  Los  microdatos  de exportación de la SUNAT se presentan como un único archivo
plano (DBF/TXT) con múltiples repeticiones y valores no atómicos.
Ejemplo de datos crudos (0NF):

77

NRO_D
OCU

FECHA

PAIS

EXPOR
TADOR

FOB_D
OLPOL

PESO_N
ETO

DESC_A
DIC

CADUA
NA

DUA001

2024-06-
01

Países
Bajos

DUA002

2024-06-
01

Países
Bajos

DUA003

2024-06-
02

España

Avocado
Export
S.A.

Avocado
Export
S.A.

Green
Peru
S.A.C.

50000

20000

30000

12000

25000

10000

"PALTA
HASS
CAT
1
ORGAN
ICA"

"PALTA
HASS
CAT 1"

"PALTA
HASS
CAT 2"

PAITA

PAITA

CALLA
O

Problemas identificados (violaciones a la normalización):

Problema

Descripción

Impacto

Repetición  de  datos  del
exportador

El  mismo  Avocado  Export
S.A. se repite en cada fila

Redundancia  y
inconsistencia

riesgo  de

Repetición  de  datos  del  país
destino

Países  Bajos  se  repite  en
múltiples filas

Mayor
actualización difícil

almacenamiento,

Campo no atómico

DESC_ADIC
contiene
múltiples  atributos  (variedad,
calidad, método)

No  se  puede
calidad individualmente

filtrar  por

Dependencia parcial

EXPORTADOR
solo de DUA, no de ITEM

depende

Violación de 2NF

6.5.2 Paso 1: Primera Forma Normal (1NF) - Atomicidad

Regla  aplicada:  Cada  columna  debe  contener  valores  atómicos  e  indivisibles.  No  debe  haber
grupos repetidos.
Transformación realizada:

●  Se extrajeron los valores del campo DESC_ADIC mediante expresiones regulares

(Regex) en Python.

●  Se crearon columnas separadas: Variedad, Categoria_Calidad, Metodo_Produccion.
●  Se asignó una clave primaria compuesta (DUA, ITEM).

Código Python utilizado (Extracción con Regex):

import re

78

def extraer_atributos(texto):
    texto = texto.upper() if texto else ""

    # Extraer variedad
    variedad = "HASS" if re.search(r'\bHASS?\b', texto) else "NO_DEFINIDO"

    # Extraer categoría de calidad
    if re.search(r'CAT[\s\.]*1', texto):
        calidad = "CAT 1"
    elif re.search(r'CAT[\s\.]*2', texto):
        calidad = "CAT 2"
    else:
        calidad = "NO_ESPECIFICA"

    # Extraer método de producción
    metodo = "ORGANICO" if re.search(r'ORGANIC[OA]', texto) else "CONVENCIONAL"

    return variedad, calidad, metodo

# Aplicar a la columna DESC_ADIC
df['Categoria_Calidad'],
df['Variedad'],
zip(*df['DESC_ADIC'].apply(extraer_atributos))

Resultado después de 1NF (tabla intermedia):

df['Metodo_Produccion']

=

DUA

ITEM

FEC
HA

PAIS

DUA
001

DUA
001

1

2

2024-
06-01

Países
Bajos

2024-
06-01

Países
Bajos

RUC
_EXP
ORT

20123
45678
9

20123
45678
9

FOB  PESO

VARI
EDA
D

CALI
DAD

MET
ODO

ADU
ANA

50000  20000

HAS
S

CAT
1

30000  12000

HAS
S

CAT
1

ORG
ANIC
O

CON
VEN
CION
AL

PAIT
A

PAIT
A

Validación de 1NF:

Criterio

Cumple

Verificación

¿Cada  columna  tiene  valores
atómicos?

¿Hay una clave primaria?

Sí

Sí

¿No hay grupos repetidos?

Sí

79

No  hay
compuestos

listas  ni  valores

(DUA,
unívocamente cada fila

ITEM)

identifica

Cada  producto  está  en  su
propia fila

6.5.3 Paso 2: Segunda Forma Normal (2NF) - Dependencia Total

Regla  aplicada:  Eliminar  dependencias  parciales  (atributos  que  dependen  solo  de  parte  de  la
clave primaria compuesta).
Problema detectado: La clave primaria es (DUA, ITEM). Sin embargo:

●  RUC_EXPORT y EXPORTADOR_NOMBRE dependen solo de DUA, no del ITEM
●  PAIS_NOMBRE y CONTINENTE dependen solo de CODIGO_PAIS

Transformación realizada: Separación en tablas independientes.

-- Tabla de hechos (depende de la clave completa DUA + ITEM)
FACT_VENTAS (DUA, ITEM, FK_Tiempo, FK_Producto, FK_Exportador, FK_Ubicacion,
FOB, Peso_Neto)

-- Tabla de exportadores (depende solo de RUC)
DIM_EXPORTADOR (RUC, Razon_Social, Tipo_Empresa)

-- Tabla de ubicación (depende solo de código país)
DIM_UBICACION (Codigo_Pais, Pais_Nombre, Continente)

Código Python para la separación:

# Extraer dimensión EXPORTADOR (depende solo de RUC)
df_exportador = df[['RUC_EXPORT',
'EXPORTADOR']].drop_duplicates().reset_index(drop=True)
df_exportador['ID_Exportador'] = df_exportador.index + 1

# Extraer dimensión UBICACION (depende solo de COD_PAIS)
df_ubicacion = df[['COD_PAIS', 'PAIS',
'CONTINENTE']].drop_duplicates().reset_index(drop=True)
df_ubicacion['ID_Ubicacion'] = df_ubicacion.index + 1

# Crear tabla de hechos con llaves foráneas
df_hechos = df.merge(df_exportador, on=['RUC_EXPORT', 'EXPORTADOR'])
df_hechos = df_hechos.merge(df_ubicacion, on=['COD_PAIS', 'PAIS', 'CONTINENTE'])
df_hechos['FK_Exportador'] = df_hechos['ID_Exportador']

80

df_hechos['FK_Ubicacion'] = df_hechos['ID_Ubicacion']

Validación de 2NF:

Criterio

Cumple

Verificación

¿Está en 1NF?

¿No hay dependencias parciales?

Sí

Sí

Verificado en paso anterior

Razon_Social  se  almacena  una  sola  vez
en DIM_EXPORTADOR

6.5.4 Paso 3: Tercera Forma Normal (3NF) - Eliminar Dependencias Transitivas

Regla aplicada: Los atributos no clave no deben depender de otros atributos no clave.
Problema  detectado:  En  DIM_UBICACION,  los  acuerdos  comerciales  (TLC)  y  aranceles
dependen  del  país,  pero  no  son  atributos  directos  de  la  ubicación  geográfica. Además, un país
puede tener múltiples acuerdos históricos.
Transformación realizada: Creación de subdimensión DIM_PAIS_TLC.

-- Se extraen atributos comerciales a subdimensión independiente
DIM_PAIS_TLC (ID_Pais_TLC, FK_Ubicacion, Acuerdo_TLC, Arancel_Porcentaje,
Fecha_Vigencia, Categoria_Mercado)
Código Python para la extracción:
python
# Crear subdimensión TLC basada en datos de MINCETUR
df_tlc = pd.DataFrame({
    'FK_Ubicacion': [1, 2, 3, 4, 5],
    'Acuerdo_TLC': [
        'Acuerdo Perú-UE (2013)',
        'TLC Perú-EE.UU. (2009)',
        'TLC Perú-China (2010)',
        'TLC Perú-Reino Unido (2021)',
        'TLC Perú-Japón (2012)'
    ],
    'Arancel_Porcentaje': [0.00, 0.00, 0.00, 0.00, 0.00],
    'Categoria_Mercado': ['Premium', 'Premium', 'Premium', 'Premium', 'Premium'],
    'Fecha_Vigencia': ['2013-01-01', '2009-01-01', '2010-01-01', '2021-01-01', '2012-01-01']
})

Validación de 3NF:

Criterio

Cumple

Verificación

¿Está en 2NF?

Sí

Verificado en paso anterior

81

¿No hay dependencias transitivas?  Sí

Los  aranceles  se  actualizan  sin  duplicar
información de países

6.5.5 Paso 4: Forma Normal de Boyce-Codd (BCNF) - Superclaves

Regla aplicada: Todo determinante debe ser una superclave.
Problema  detectado:  En  la  tabla  de  costos,  el  Tipo_Costo  (Producción,  Empaque,  Logístico)
determina  el  Valor_Unitario_USD  para  una  región  y  fecha,  pero  Tipo_Costo  no  es  una
superclave por sí solo.
Transformación realizada: Se rediseñó DIM_COSTO como una dimensión SCD Tipo 2 donde la
la  clave  única
combinación
(superclave).
Estructura final de DIM_COSTO (BCNF):

(Tipo_Costo,  Region_Destino,  Fecha_Vigencia_Inicio)  es

SK_Cost
o (PK)

ID_Cost
o

Tipo_Co
sto

Subcateg
oria

Valor_U
nitario

Region

Fecha_In
icio

Fecha_Fi
n

Es_Vige
nte

1

2

3

4

5

6

7

8

9

1

1

2

3

4

5

6

7

8

Producci
ón

Producci
ón

Producci
ón

Producci
ón

Logístico

Logístico

Logístico

Labores
Culturale
s

Labores
Culturale
s

Mano  de
Obra
Cosecha

Procesa
miento
Packing

Transpor
te
Terrestre

Servicios
Portuario
s

Agencia
miento

Operativ
o

Certifica
ciones

Operativ
o

Gastos
Administ
rativos

0.25

Global

2016-01-
01

2022-12-
31

FALSE

0.30

Global

0.20

Global

0.30

Global

0.15

Global

0.60

Global

0.04

Global

0.06

Global

0.04

Global

2023-01-
01

2016-01-
01

2016-01-
01

2016-01-
01

2016-01-
01

2016-01-
01

2016-01-
01

2016-01-
01

NULL

TRUE

NULL

TRUE

NULL

TRUE

NULL

TRUE

NULL

TRUE

NULL

TRUE

NULL

TRUE

NULL

TRUE

82

Código SQL para validar BCNF (sin solapamiento de fechas):

-- Verificar que no hay solapamiento de fechas en DIM_COSTO
-- Esto asegura que la combinación (Tipo_Costo, Region_Destino, Fecha) es única
SELECT Tipo_Costo, Region_Destino, Fecha_Vigencia_Inicio, Fecha_Vigencia_Fin
FROM DIM_COSTO c1
WHERE EXISTS (
    SELECT 1 FROM DIM_COSTO c2
    WHERE c2.Tipo_Costo = c1.Tipo_Costo
    AND c2.Region_Destino = c1.Region_Destino
    AND c2.SK_Costo != c1.SK_Costo
    AND c2.Fecha_Vigencia_Inicio < c1.Fecha_Vigencia_Fin
    AND c1.Fecha_Vigencia_Inicio < c2.Fecha_Vigencia_Fin
);
-- Resultado esperado: Ningún registro retornado (sin solapamientos)

Validación de BCNF:

Criterio

Cumple

Verificación

¿Está en 3NF?

Sí

Verificado en paso anterior

¿Todo determinante es superclave?

Sí

+

(Tipo_Costo
Fecha_Vigencia_Inicio)
unívocamente cada registro

Region_Destino

+
identifica

6.5.6 Paso 5: Cuarta Forma Normal (4NF) - Eliminar Dependencias Multivaluadas

Regla  aplicada:  No debe haber dos o más relaciones multivaluadas independientes en la misma
tabla.
Problema detectado: En los datos originales, un mismo producto podía tener múltiples calidades
y múltiples métodos de producción registrados en un solo campo. No se puede saber si "CAT 1"
corresponde a "ORGÁNICO" o si son combinaciones independientes.
Transformación  realizada:  Se  separó  DIM_VARIEDAD_CALIDAD  como  una  dimensión
independiente (no subdimensión de DIM_PRODUCTO).

-- DIM_PRODUCTO: solo atributos intrínsecos del producto (una sola combinación por
producto)
DIM_PRODUCTO (ID_Producto, Partida_Arancelaria, Descripcion)

-- DIM_VARIEDAD_CALIDAD: atributos de calidad (independiente, puede tener múltiples
combinaciones)
DIM_VARIEDAD_CALIDAD (ID_Variedad_Calidad, Variedad, Categoria_Calidad,
Metodo_Produccion, Fuente_Extraccion)

Ejemplo de la separación:

83

Antes (en una sola tabla)

Después (tablas independientes)

DIM_PRODUCTO
contendría:
(Partida,  Hass,  CAT  1,  CAT  2,
Orgánico, Convencional)

DIM_PRODUCTO: solo (Partida, Descripcion)
1,
DIM_VARIEDAD_CALIDAD:
Orgánico), (Hass, CAT 1, Convencional), (Hass, CAT
2, Convencional)

(Hass,  CAT

Validación de 4NF:

Criterio

Cumple

Verificación

¿Está en BCNF?

dependencias

hay

¿No
multivaluadas
independientes?

Sí

Sí

Verificado en paso anterior

DIM_VARIEDAD_CALIDAD  es  independiente
de DIM_PRODUCTO

6.5.7  Paso  6:  Quinta  Forma  Normal  (5NF)  -  Dependencia  de  Join  (Descomposición  sin
pérdida)

Regla  aplicada:  La  tabla  original  debe  poder  reconstruirse  exactamente  mediante  joins  de  las
tablas resultantes, sin filas adicionales o faltantes.
Validación realizada: Se verificó que el siguiente join reconstruye exactamente la tabla original.

Código SQL para validar 5NF (reconstrucción sin pérdida):

-- Query de reconstrucción (5NF)
WITH Reconstruccion AS (
    SELECT
        f.Valor_FOB,
        f.Volumen_Exportado,
        t.Fecha,
        u.Pais_Nombre,
        e.Razon_Social as Exportador,
        p.Descripcion as Producto,
        v.Categoria_Calidad,
        v.Metodo_Produccion,
        a.Nombre_Aduana,
        fin.Tipo_Cambio_USD_PEN,
        c.Tipo_Costo,
        c.Valor_Unitario_USD
    FROM FACT_RENTABILIDAD f
    JOIN DIM_TIEMPO t ON f.FK_Tiempo = t.ID_Tiempo
    JOIN DIM_UBICACION u ON f.FK_Ubicacion = u.ID_Ubicacion
    JOIN DIM_EXPORTADOR e ON f.FK_Exportador = e.ID_Exportador

84

    JOIN DIM_PRODUCTO p ON f.FK_Producto = p.ID_Producto
    JOIN DIM_VARIEDAD_CALIDAD v ON f.FK_Variedad_Calidad =
v.ID_Variedad_Calidad
    JOIN DIM_ADUANA a ON f.FK_Aduana = a.ID_Aduana
    JOIN DIM_FINANZAS fin ON f.FK_Finanzas = fin.ID_Finanzas
    JOIN DIM_COSTO c ON f.FK_Costo = c.SK_Costo
)
SELECT
    COUNT(*) as Registros_Reconstruidos,
    (SELECT COUNT(*) FROM FACT_RENTABILIDAD) as Registros_Originales
FROM Reconstruccion;

Resultado esperado:

Registros_Reconstruidos

Registros_Originales

Diferencia

100,000

100,000

0

Validación de 5NF:

Criterio

Cumple

Verificación

¿Está en 4NF?

¿La  descomposición  es  sin
pérdida?

Sí

Sí

Verificado en paso anterior

El número de registros reconstruidos coincide con
el original

6.5.8 Resumen del Proceso de Normalización Aplicado

Forma
Normal

Regla aplicada

Estructura resultante

Beneficio obtenido

1NF

Atomicidad

Extracción
DESC_ADIC vía Regex

de

atributos

desde

Búsqueda  y  filtrado
eficiente por calidad

2NF

Dependencia
total

Separación  de  hechos (DUA+ITEM) de
dimensiones (Exportador, Ubicación)

3NF

Sin transitivas

Creación de DIM_PAIS_TLC (aranceles
y TLC)

Reducción
de
redundancia (RUC se
almacena una vez)

aranceles

Los
actualizan
duplicar países

se
sin

BCNF

Superclaves

DIM_COSTO  con  SCD  Tipo  2  (clave
compuesta)

4NF

Sin
multivaluadas

DIM_VARIEDAD_CALIDAD
independiente de DIM_PRODUCTO

5NF

Join sin pérdida

Verificación de reconstrucción exacta de
la tabla original

85

Historial  de  costos  y
FK
directa  desde
hechos

Un  producto  puede
múltiples
tener
combinaciones
de
calidad

Garantía  de  que  no
hay
de
pérdida
información

7. CONCLUSIONES

El presente proyecto de inteligencia de negocios logró el desarrollo e implementación exitosa de
un Data Mart bajo un modelo dimensional de Copo de Nieve (Snowflake Schema). A través de
esta  arquitectura,  se  integraron  datos  de  SUNAT  y  fuentes  económicas  externas  (BCRP,
MINCETUR,  MIDAGRI/Sierra  Exportadora),  permitiendo  un  análisis  exhaustivo  de  la
rentabilidad  de  la  palta  Hass  en  el  período  2016-2024.  El  modelo  cumplió  con  los  objetivos
técnicos  y  estratégicos  mediante  la  aplicación  de  algoritmos  de  limpieza  con  expresiones
regulares (Regex) para identificar exclusivamente la variedad Hass, así como la construcción de
indicadores  clave  de  desempeño (KPI) como el margen de utilidad, el ratio de rentabilidad y el
índice de concentración Herfindahl-Hirschman (HHI). La visualización de estos datos en Power
BI  permite  concluir  que  la  estructura  de  datos  es  capaz  de segmentar los mercados con mayor
potencial  de  rentabilidad,  logrando  una  transición  exitosa  de  datos  crudos  a  información
estratégica para la toma de decisiones.

Es  fundamental  reconocer  que la precisión del análisis está sujeta a la naturaleza de las fuentes
utilizadas.  Los  costos  operativos  empleados  son  referenciales  (provenientes  de  MIDAGRI  y
Sierra  Exportadora)  y  no  corresponden  a  costos  reales  internos  de  Peruvian  Andean  Trout
S.A.C.,  lo  que  califica  la  rentabilidad  calculada  como  "potencial"  o  "estimada".  Asimismo,  la
falta  de  datos  directos  sobre el importador final en los registros aduaneros públicos de SUNAT
obligó al uso de la ubicación geográfica (DIM_UBICACION) como variable proxy del mercado
consumidor, una simplificación válida para el alcance del proyecto. Finalmente, la extracción de
datos  cualitativos  (calidad  y  método  de  producción)  a  partir  de  campos  no  estructurados
(DESC_ADIC,  DESC_COM)  mediante  expresiones  regulares  presenta  un  margen  de  error
propio del procesamiento de lenguaje natural.

A  partir de los hallazgos mencionados y las limitaciones identificadas, se derivan directrices de
mejora  para  Peruvian  Andean  Trout  S.A.C.,  orientadas  tanto  a  la  optimización  técnica  del
modelo  como  a  la  ejecución  comercial.  En  el  ámbito  técnico,  se  recomienda  implementar  un
sistema ERP agrícola que permita registrar costos reales de producción para sustituir los valores
referenciales  actuales,  así  como  escalar  el  modelo  hacia  un  Data  Warehouse  corporativo  que
integre  otros  productos  de  la  canasta  agroexportadora  peruana.  En  el  ámbito  comercial,  es
imperativo  priorizar  los  mercados  con  Tratados  de  Libre  Comercio  (TLC)  donde  el  arancel es

86

nulo (Unión Europea, Estados Unidos, China, Japón, Corea del Sur, Hong Kong, Reino Unido),
buscando  diversificar  la  cartera  de  destinos  para evitar que el índice HHI supere los niveles de
riesgo  establecidos  (2,500  puntos).  En  conclusión,  el  sistema  desarrollado  proporciona  una
infraestructura  analítica  sólida  que  transforma  el proceso de evaluación de exportaciones de un
enfoque  empírico  a  uno  basado  en  evidencia.  Los  resultados  obtenidos  validan  que  el  uso  de
modelos dimensionales y herramientas de inteligencia de negocios es el camino crítico para que
la empresa logre una diversificación competitiva y sostenible en el sector agroindustrial.

8. REFERENCIAS

Banco  Central  de  Reserva  del  Perú.  (s.  f.).  Series  estadísticas  de  comercio  exterior.

https://www.bcrp.gob.pe/estadisticas.html

Compuempresa.

(2025).  Peruvian  Andean  Trout  S.A.C.

-  RUC  20568513216.

https://compuempresa.com/info/peruvian-andean-trout-sac-C33D92F4B13EC53D

Ministerio  de  Comercio  Exterior  y  Turismo.  (2024).  Laguna  De  Choclococha.  Plataforma  del
Peruano.

Estado
http://consultasenlinea.mincetur.gob.pe/fichaInventario/index.aspx?cod_Ficha=1158

Ministerio  de  Comercio  Exterior  y  Turismo.  (2024).  Reporte  de  comercio  regional  (RCR)  –

Huancavelica.
https://www.gob.pe/institucion/mincetur/colecciones/559-reporte-de-comercio-regional-r
cr-huancavelica

Ministerio de Desarrollo Agrario y Riego (MIDAGRI). (2023). Sistema Integrado de Estadística

Agraria (SIEA) - Costos de producción. https://siea.midagri.gob.pe

Ministerio  de  la  Producción.  (2017).  Resolución  Directoral  N°  007-2017-PRODUCE/DGPA.

https://www.gob.pe/institucion/produce/normas-legales/tipos/26-resolucion-directoral

Sierra y Selva Exportadora. (2022). Costos referenciales de logística de exportación para la palta

Hass. https://www.sierraexportadora.gob.pe

Superintendencia  Nacional  de  Aduanas  y  de  Administración  Tributaria.  (2024).  Operatividad
partida.

exportación

por

de

Consulta
aduanera:
http://www.aduanet.gob.pe/operatividadAduana/

87

Superintendencia  Nacional  de  Aduanas  y  de  Administración  Tributaria.  (s.  f.).  Portal  de

microdatos de exportación y aduanas. https://www.sunat.gob.pe/estadisticasestudios/

Telefono.pe.  (2025).  Peruvian  Andean  Trout  S.A.C.  (PATSAC)  -  Teléfono  y  dirección.

https://telefono.pe/patsac/

Ubicania.

(2025).

Trout
https://ubicania.com/empresas/peruvian-andean-trout-s-a-c_id_EFEC59B20CC48C22

Peruvian  Andean

-  RUC

20568513216.

S.A.C.

Vassiliadis,  P.  (2009).  A  survey  of  extract–transform–load  technology.  International  Journal  of

Data Warehousing and Mining, 5(3), 1-27. https://doi.org/10.4018/jdwm.2009070101

