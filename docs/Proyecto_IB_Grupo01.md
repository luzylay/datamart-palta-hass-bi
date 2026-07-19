
UNIVERSIDAD TECNOLÓGICA DEL PERÚ

GRUPO 01



Creación de un Data Mart para el análisis de la rentabilidad potencial de la palta Hass para la empresa Peruvian Andean Trout S.A.C., con sede en Huancavelica, período 2016–2024




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
Junio, 2026
ÍNDICE DE CONTENIDOS


# 1. INTRODUCCIÓN


## 1.1 Reseña Histórica de la Empresa

Peruvian Andean Trout S.A.C. es una empresa peruana constituida como Sociedad Anónima Cerrada, cuyo RUC es 20568513216 y su condición es ACTIVO y HABIDO . La empresa inició operaciones oficialmente el 15 de noviembre de 2012 y su actividad principal es la acuicultura de agua dulce (CIIU: 0322) . Su centro de operaciones está ubicado en la Comunidad Campesina de Choclococha, en el distrito de Santa Ana, provincia de Castrovirreyna, en la región Huancavelica, a más de 4,500 metros sobre el nivel del mar.
La empresa inició un proceso de diversificación hacia el sector agroexportador. Como parte de este proceso, solicitó un análisis basado en inteligencia de negocios para evaluar la viabilidad de invertir en palta Hass, utilizando datos del mercado de exportación peruano del período 2016–2024.

## 1.2 Contexto del Problema

La empresa Peruvian Andean Trout S.A.C. no cuenta actualmente con información estructurada que le permita evaluar la rentabilidad de la palta Hass como potencial nueva línea de negocio. Los datos disponibles en fuentes públicas presentan limitaciones significativas que impiden un análisis financiero completo y confiable.
Limitaciones de los datos disponibles

| Limitación | Descripción | Impacto en el análisis |
| --- | --- | --- |
| Datos dispersos | Los microdatos de exportación de la SUNAT se encuentran distribuidos en múltiples archivos con formatos heterogéneos (DBF, TXT). | Dificultad para integrar y analizar información histórica de manera eficiente. |
| Sin costos reales | La SUNAT no registra los costos de producción, empaque o logística de las exportaciones. | Imposibilidad de calcular márgenes de rentabilidad reales. |
| Sin tipo de cambio | Los registros de la SUNAT solo incluyen valores en dólares americanos (USD), sin el tipo de cambio asociado. | El análisis de rentabilidad en soles (moneda local) resulta incompleto. |
| Sin aranceles | No se registran los aranceles pagados por país destino. | No es posible calcular el margen neto ajustado, que considera los impuestos de importación. |
| Ruido semántico | Los campos de descripción (DESC_ADIC, DESC_COM) contienen términos como "muestras", "pulpa", "congelado" o "procesamiento". | Distorsión del precio promedio FOB/kg real de la palta Hass fresca. |

Justificación de la serie temporal (2016–2024)
El período de análisis comprende los años 2016 a 2024. Justificación estratégica del rango: La elección del período 2016-2024 se fundamenta en la necesidad de analizar un ciclo económico completo de la industria agroexportadora. Este rango histórico ininterrumpido permite a Peruvian Andean Trout S.A.C. evaluar el comportamiento de los precios y volúmenes de la Palta Hass en escenarios de normalidad (pre-pandemia), disrupción logística (pandemia) y recuperación (post-pandemia), garantizando un análisis de viabilidad robusto y libre de sesgos temporales cortos.

Análisis de Causa-Raíz (Diagrama de Ishikawa)
A continuación, se presenta el diagrama de Ishikawa que identifica las causas raíz del problema central: "La empresa no cuenta con información estructurada para evaluar la rentabilidad de la palta Hass".
Causas identificadas:

| Categoría | Causa | Efecto |
| --- | --- | --- |
| Datos | Datos SUNAT dispersos en múltiples archivos (DBF/TXT) | Dificultad para integrar y analizar información histórica |
| Datos | Falta de información de costos reales de producción | Imposibilidad de calcular márgenes de rentabilidad reales |
| Datos | Ausencia de tipo de cambio y aranceles en registros SUNAT | Análisis de rentabilidad incompleto (solo en USD) |
| Procesos | No existe un proceso ETL automatizado | Los datos no se limpian ni transforman consistentemente |
| Procesos | Falta de un modelo dimensional de datos | No se puede segmentar el análisis por múltiples dimensiones |
| Personas | Limitada experiencia previa en agroexportación de palta | Desconocimiento de los KPIs clave del sector |
| Tecnología | No hay un Data Mart para análisis histórico | Cada análisis requiere procesamiento manual desde cero |

Diagrama Ishikawa:

Solución propuesta: El Data Mart desarrollado en este proyecto aborda cada una de las causas identificadas.

| Causa identificada | Solución implementada en el Data Mart |
| --- | --- |
| Datos dispersos en múltiples archivos | Se integran en un modelo único tipo Copo de Nieve (Snowflake Schema) |
| Ausencia de costos reales de producción | Se estiman mediante valores de referencia de Sierra Exportadora y MIDAGRI |
| Falta de tipo de cambio (USD/PEN) | Se incorpora la serie histórica del Banco Central de Reserva del Perú (BCRP) |
| Ausencia de aranceles por país destino | Se integra información de acuerdos comerciales y aranceles del MINCETUR |
| No existe proceso ETL automatizado | Se implementa un proceso automatizado en Python con librerías especializadas |
| Falta de modelo dimensional de datos | Se diseña un modelo Copo de Nieve con tablas de hechos y dimensiones |
| Desconocimiento de KPIs del sector | Se definen KPIs específicos para el sector agroexportador (ver sección 3.3) |


## 1.3 Objetivo General del Proyecto

Desarrollar un Data Mart que permita analizar la rentabilidad potencial de la palta Hass para la empresa Peruvian Andean Trout S.A.C., mediante la integración y transformación de los microdatos de exportación de la SUNAT correspondientes al período 2016–2024, enriquecidos con fuentes externas de tipo de cambio (BCRP), acuerdos comerciales y aranceles (MINCETUR) y costos referenciales (MIDAGRI/Sierra Exportadora), como base para la toma de decisiones estratégicas sobre diversificación.
Objetivos Específicos


| N° | Objetivo Específico | ¿Qué se entregará? |
| --- | --- | --- |
| 1 | Diseñar un modelo dimensional orientado al análisis de la rentabilidad potencial de la palta Hass. | Un modelo lógico tipo Copo de Nieve (Snowflake Schema) con tabla de hechos y dimensiones. |
| 2 | Filtrar los registros de SUNAT para incluir exclusivamente la variedad Hass y excluir pulpa, congelados y productos procesados. | Un script de limpieza y transformación que asegure datos válidos para el análisis. |
| 3 | Calcular en el Data Mart las métricas clave de rentabilidad: precio FOB/kg, costo total estimado, margen de utilidad estimado, ratio de rentabilidad estimado, índice de concentración por destino, índice HHI por exportador y margen neto ajustado. | Una tabla de hechos (FACT_RENTABILIDAD) poblada con las métricas base (valor FOB y volumen), mientras que los indicadores derivados se calculan en la capa de visualización. |
| 4 | Identificar los mercados de destino (países y continentes) con mayor rentabilidad potencial, utilizando información referencial de aranceles y acuerdos comerciales proveniente de MINCETUR. | Una subdimensión (DIM_PAIS_TLC) que clasifique los mercados como "Premium" (con TLC y arancel 0%) o "Estándar". |
| 5 | Evaluar la concentración del mercado entre los exportadores peruanos (índice HHI) y la eficiencia por aduana de salida. | Reportes que permitan conocer el nivel de competencia en el mercado y optimizar rutas logísticas. |
| 6 | Generar reportes en Power BI para la Gerencia General, Planeamiento Estratégico, Finanzas y Comercio Exterior. | Dashboards interactivos con los KPIs clave para la toma de decisiones. |



## 1.4 Alcance del Proyecto

El presente proyecto abarca el análisis del período 2016–2024, centrado en la partida arancelaria 0804400000 correspondiente a la palta Hass. La fuente de datos primaria está conformada por los registros de exportación disponibles en el portal ADUANET de la SUNAT.
Fuentes de datos utilizadas


| Fuente | Datos proporcionados | Uso en el proyecto |
| --- | --- | --- |
| SUNAT (ADUANET) | Valor FOB, volumen exportado (peso neto), país destino, RUC del exportador, aduana de salida | Base transaccional del Data Mart |
| BCRP | Serie histórica de tipo de cambio (USD/PEN) diario 2016-2024 | Conversión de rentabilidad a soles (moneda local) |
| MINCETUR | Aranceles por país destino, acuerdos comerciales (TLC), información de puertos | Identificación de mercados "Premium" |
| MIDAGRI / Sierra Exportadora | Costos referenciales de producción, empaque y logística por región | Cálculo del costo total estimado y margen de utilidad |


Indicadores que se construirán
A partir de las variables principales (valor FOB, volumen exportado y mercado de destino), se construirán los siguientes indicadores:


| Indicador | Fórmula | Fuentes involucradas |
| --- | --- | --- |
| Precio promedio por kilogramo | Valor FOB ÷ Peso Neto | SUNAT |
| Costo total estimado | Σ (Valor unitario de referencia × Volumen exportado) | DIM_COSTO (MIDAGRI/Sierra Exportadora) |
| Margen de utilidad estimado | Ingreso FOB – Costo total estimado | SUNAT + DIM_COSTO |
| Ratio de rentabilidad estimado | (Margen ÷ Ingreso FOB) × 100% | SUNAT + DIM_COSTO |
| Margen neto ajustado (soles) | (Ingreso FOB × TC) – Costo total – Aranceles | SUNAT + BCRP + MINCETUR |


Nota: El análisis tiene un enfoque referencial, basado en información del mercado de exportación peruano y en costos referenciales, no en datos operativos internos de la empresa. Los resultados constituyen una aproximación para evaluar la rentabilidad potencial.
Limitaciones del alcance y soluciones implementadas

| Limitación | Solución implementada |
| --- | --- |
| Los registros de SUNAT no incluyen información de costos reales | Se utiliza DIM_COSTO con valores de referencia de MIDAGRI/Sierra Exportadora. |
| Los registros de SUNAT no incluyen tipo de cambio | Se integra la serie histórica del BCRP (tipo de cambio USD/PEN). |
| Los registros de SUNAT no incluyen aranceles pagados | La información de aranceles y acuerdos comerciales (MINCETUR) se incorpora en la subdimensión DIM_PAIS_TLC como dato referencial. |
| Ausencia de datos útiles para 2016 y 2019 | Justificación metodológica documentada en la sección 1.2. |

Qué queda expresamente fuera del alcance
La implementación de sistemas en tiempo real.
La integración con sistemas internos de la empresa (como ERP).
La inclusión de variables externas como costos logísticos reales, costos de producción específicos de la empresa o factores productivos internos.
La consulta directa a APIs de SUNAT en tiempo real (la extracción se basa en archivos descargados).
Beneficiarios directos

| Beneficiario | Rol en la toma de decisiones |
| --- | --- |
| Gerencia General | Decisor estratégico. Aprueba o rechaza la inversión basándose en los resultados. |
| Planeamiento Estratégico | Evalúa mercados y concentración de riesgo. |
| Finanzas | Valida márgenes y rentabilidad potencial. |
| Comercio Exterior | Asesora sobre destinos, costos logísticos y competidores. |



## 1.5 Metodología Hefesto

La construcción del Data Mart se guió por la Metodología Hefesto, adaptada al contexto de Peruvian Andean Trout S.A.C. A continuación, se documentan las decisiones clave en cada fase:

Fase 1 - Análisis de Requerimientos
Se partió de la pregunta central: "¿Cuál es el nivel de rentabilidad potencial de la palta Hass (2016-2024)?"
De esta pregunta derivaron 7 preguntas analíticas de soporte (listadas en 1.7), que definieron los KPIs críticos:


| KPI | Meta esperada | Justificación |
| --- | --- | --- |
| Precio FOB/kg | Variable por destino | Identificar mercados premium |
| Ratio de Rentabilidad | > 15% - 25% | Estándar sectorial según Sierra Exportadora |
| Índice HHI | < 2500 | Mercado competitivo (no concentrado) |
| Margen Neto Ajustado | Positivo | Rentabilidad real considerando tipo de cambio |

Decisión clave: Si el análisis resultara desfavorable, la misma estructura permite evaluar otro producto cambiando únicamente el filtro de partida arancelaria en la dimensión de producto.


Fase 2 - Análisis de Fuentes de Datos
Se evaluaron cuatro fuentes de datos. Se identificó que SUNAT (ADUANET) no proporciona costos reales, tipo de cambio ni aranceles, limitaciones críticas para calcular rentabilidad.


| Fuente | Datos proporcionados | Limitación identificada | Solución |
| --- | --- | --- | --- |
| SUNAT (ADUANET) | Valor FOB, volumen, destino, exportador | No incluye costos, tipo de cambio ni aranceles | Incorporación de fuentes externas |
| BCRP | Tipo de cambio histórico USD/PEN | Dato macroeconómico, no transaccional | Integración vía dimensión financiera |
| MINCETUR | Aranceles, acuerdos TLC, puertos | Información estática | Pobla subdimensión de acuerdos comerciales |
| MIDAGRI / Sierra Exportadora | Costos de referencia (producción, empaque, logística) | Valores estimados, no reales de la empresa | Dimensión de costos con historial (SCD Tipo 2) |


Fase 3 - Modelo Lógico de Datos
Se diseñó un esquema de Copo de Nieve (Snowflake Schema) con las siguientes características:


| Característica | Descripción |
| --- | --- |
| Tabla de hechos | FACT_RENTABILIDAD almacena únicamente hechos atómicos (Valor_FOB, Volumen_Exportado) |
| Métricas derivadas | Se calculan en Power BI (no en la tabla de hechos) para garantizar consistencia |
| Granularidad | Fina: un registro por ítem dentro de una Declaración Única de Aduanas (DUA) |
| Normalización | Se aplica un proceso sistemático de normalización de datos (1NF → 5NF), documentado en detalle en la sección 6.5, para transformar los datos crudos en un modelo Copo de Nieve sin redundancias. |


Jerarquías implementadas:
DIM_TIEMPO: Año → Trimestre → Mes → Semana → Día
DIM_UBICACION: Continente → País
DIM_PAIS_TLC (subdimensión): País → Acuerdo TLC → Arancel aplicable

Fase 4 - Integración de Datos (ETL) y Gestión de Metadatos
El proceso ETL se implementó en Python con las librerías pandas, dbfread, re y sqlalchemy. Las tres etapas de manipulación se describen a continuación:


| Etapa | Descripción | Herramientas |
| --- | --- | --- |
| Extracción | Recolección desde archivos DBF/TXT de SUNAT y CSVs/Excel de BCRP, MINCETUR y costos | dbfread, pandas |
| Transformación | Limpieza, deduplicación, filtros Regex para identificar "HASS", enriquecimiento con fuentes externas | pandas, re, numpy |
| Carga | Inserción en Data Mart respetando orden de integridad referencial (primero dimensiones, luego hechos) | SQLAlchemy, psycopg2 |


Control de calidad: El proceso ETL se documenta con una bitácora (log) que registra la cantidad de registros procesados, insertados y rechazados por cada regla de validación, asegurando la trazabilidad de la información.


## 1.6 Estructura del Data Mart Actual

El Data Mart se organiza bajo un modelo dimensional tipo Copo de Nieve (Snowflake Schema). Este diseño permite normalizar jerarquías en subdimensiones, evitando redundancias y facilitando el mantenimiento de la información.
Tabla de hechos central: FACT_RENTABILIDAD
La tabla de hechos es el centro del modelo y almacena únicamente las métricas atómicas de cada operación de exportación:

| Métrica | Descripción | Unidad |
| --- | --- | --- |
| Valor_FOB | Valor de venta de la exportación | Dólares americanos (USD) |
| Volumen_Exportado | Peso neto de la mercancía | Kilogramos (kg) |

Nota: Las métricas derivadas (precio por kilogramo, margen de utilidad y ratio de rentabilidad) no se almacenan físicamente en la tabla de hechos. Se calculan en la capa de visualización (Power BI) para garantizar consistencia ante futuras actualizaciones de costos o tipo de cambio.
Tablas de dimensiones (permiten segmentar el análisis)
Las dimensiones proporcionan el contexto descriptivo para filtrar y agrupar los datos:

| Dimensión | ¿Qué permite analizar? |
| --- | --- |
| DIM_TIEMPO | Evolución temporal (año, trimestre, mes, semana, día) |
| DIM_UBICACION | Análisis por país y continente de destino |
| DIM_PAIS_TLC (subdimensión) | Acuerdos comerciales y aranceles por país (mercados "Premium") |
| DIM_PRODUCTO | Información base del producto (partida arancelaria) |
| DIM_VARIEDAD_CALIDAD | Calidad (CAT 1, CAT 2) y método de producción (orgánico/convencional) |
| DIM_EXPORTADOR | Competidores en el mercado peruano |
| DIM_ADUANA | Puertos y puntos de embarque |
| DIM_FINANZAS | Tipo de cambio (BCRP) y aranceles (MINCETUR) |
| DIM_COSTO | Costos referenciales de producción, empaque y logística |

Granularidad del modelo
La granularidad es fina: un registro en la tabla de hechos corresponde a una línea de producto dentro de una Declaración Única de Aduanas (DUA). Esto significa que cada ítem individual (con su propio valor FOB y peso neto) tiene su propio registro.
Ventaja de esta granularidad: Permite agregaciones flexibles:

| Nivel de agregación | Ejemplo |
| --- | --- |
| Fino | Análisis por operación individual (DUA + ítem) |
| Medio | Exportaciones mensuales por país destino |
| Grueso | Totales anuales por continente |

Jerarquías implementadas

| Dimensión | Jerarquía |
| --- | --- |
| DIM_TIEMPO | Año → Trimestre → Mes → Semana → Día |
| DIM_UBICACION | Continente → País |
| DIM_PAIS_TLC | País → Acuerdo TLC → Arancel aplicable |
| DIM_VARIEDAD_CALIDAD | Variedad → Categoría de calidad → Método de producción |

El detalle completo de atributos, tipos de datos, claves primarias y foráneas, subdimensiones normalizadas y restricciones de integridad referencial se presenta en la sección 5. Modelamiento Dimensional.

## 1.7 Preguntas de Negocio que Responde el Data Mart

El Data Mart ha sido diseñado para dar respuesta a las siguientes preguntas:
Pregunta Central:
¿Cuál es el nivel de rentabilidad potencial de la palta Hass en el período 2016–2024?
Preguntas Analíticas de Soporte:

| N° | Pregunta de negocio | Dimensiones involucradas | Dirigido a | Propósito |
| --- | --- | --- | --- | --- |
| 1 | ¿Cómo evoluciona el precio promedio FOB por kilogramo a lo largo del tiempo (mensual, anual), y cómo se compara esta evolución con el ratio de rentabilidad estimado? | DIM_TIEMPO | Planeamiento Estratégico | Identificar tendencias estacionales y correlación entre precio y rentabilidad |
| 2 | ¿Qué países y continentes presentan consistentemente un precio promedio FOB/kg superior y un ratio de rentabilidad estimado más alto? (Pregunta clave) | DIM_UBICACION, DIM_PAIS_TLC | Gerencia General / Comercio Exterior | Clasificar mercados "Premium" (con TLC, arancel 0%, alta rentabilidad) |
| 3 | ¿Cuál es el nivel de concentración de las exportaciones por país destino? ¿Existe riesgo de dependencia excesiva de pocos mercados? | DIM_UBICACION | Planeamiento Estratégico | Evaluar diversificación geográfica y mitigar riesgos |
| 4 | ¿Qué nivel de concentración presenta el mercado de exportadores peruanos (índice HHI)? ¿Existen pocos actores dominantes o el mercado está diversificado? | DIM_EXPORTADOR | Finanzas / Comercio Exterior | Comprender el nivel de competencia en el mercado |
| 5 | ¿Qué aduanas o puertos de salida concentran el mayor volumen exportado y presentan mejor precio promedio por kilogramo? | DIM_ADUANA | Comercio Exterior | Optimizar rutas logísticas y seleccionar puertos más eficientes |
| 6 | ¿Qué relación existe entre el volumen exportado (escala) y el precio promedio FOB/kg? ¿Existen economías de escala o mercados premium de menor volumen? | FACT_RENTABILIDAD | Gerencia General | Definir estrategia de volumen vs. precio |


Nota sobre las respuestas. Los resultados obtenidos para preguntas que involucran costos, márgenes y ratios de rentabilidad son estimaciones basadas en parámetros de referencia (provenientes de MIDAGRI y Sierra Exportadora), no en datos reales de la empresa o de los exportadores.

La incorporación del tipo de cambio (BCRP) y los aranceles (MINCETUR) permite ajustar el análisis a condiciones económicas reales, calculando un Margen Neto Ajustado en soles que supera la limitación de los datos brutos de SUNAT.

Estos resultados deben interpretarse como una aproximación para la toma de decisiones estratégicas, no como estados financieros auditados.

# 2. MARCO TEÓRICO


## 2.1 Datos, Información y Sistemas de Información

En el contexto del presente proyecto, los datos son representaciones simbólicas (numéricas, alfanuméricas) de hechos en bruto, sin procesar, que por sí mismos carecen de significado estratégico. Provienen de múltiples fuentes:

| Fuente | Tipo de dato | Descripción |
| --- | --- | --- |
| SUNAT (ADUANET) | Microdatos de exportación | Valor FOB, peso neto, fecha, país destino, RUC del exportador, descripción adicional del producto |
| BCRP | Serie histórica | Tipo de cambio USD/PEN (diario) |
| MINCETUR | Datos referenciales | Aranceles por país destino, acuerdos comerciales (TLC) |
| MIDAGRI / Sierra Exportadora | Costos referenciales | Costos de producción, empaque y logística por región |

La información se genera al transformar, limpiar y enriquecer estos datos, dotándolos de contexto y significado para la toma de decisiones. En este proyecto, la información se materializa en indicadores clave como:
Precio promedio FOB por kilogramo
Margen de utilidad estimado
Ratio de rentabilidad
Índice de concentración de mercado (HHI)
Margen neto ajustado por tipo de cambio y aranceles
El sistema de información implementado es un Data Mart en modelo Copo de Nieve (Snowflake Schema) que integra, almacena y permite analizar esta información multidimensionalmente para la toma de decisiones estratégicas sobre la diversificación hacia la palta Hass.

## 2.2 Inteligencia de Negocios (Business Intelligence) y diferenciación OLTP vs OLAP

En el presente proyecto, la arquitectura BI establece una clara distinción entre dos tipos de sistemas de procesamiento:

| Característica | Sistema OLTP | Sistema OLAP |
| --- | --- | --- |
| Propósito | Registrar transacciones individuales | Analizar datos históricos y multidimensionales |
| Sistema en este proyecto | SUNAT / ADUANET | Data Mart construido |
| Tipo de operaciones | Inserción, actualización, eliminación (CRUD) | Consultas complejas de lectura (SELECT) |
| Volumen de datos | Operaciones diarias, datos actuales | Históricos agregados (2016-2024) |
| Diseño | Normalizado (3FN) | Desnormalizado (esquema copo de nieve) |

El Data Mart, construido bajo un esquema de Copo de Nieve (Snowflake Schema), permite múltiples tipos de análisis:

| Tipo de análisis | Dimensión utilizada | ¿Qué permite evaluar? |
| --- | --- | --- |
| Análisis de competencia | DIM_EXPORTADOR | Identificar principales exportadores y calcular el índice HHI |
| Análisis logístico | DIM_ADUANA | Comparar eficiencia por puerto de salida y optimizar rutas |
| Análisis de riesgos financieros | DIM_FINANZAS | Incorporar tipo de cambio (BCRP) y aranceles (MINCETUR) |
| Análisis de calidad de producto | DIM_VARIEDAD_CALIDAD | Segmentar por calidad (CAT 1, CAT 2) y método de producción |

Nota metodológica: La evolución del modelo tradicional al aquí propuesto responde a la necesidad de profundidad analítica requerida por la Gerencia General para evaluar la viabilidad de la inversión en palta Hass, incorporando subdimensiones como DIM_PAIS_TLC dependiente de DIM_UBICACION.

## 2.3 Modelamiento Dimensional y Esquema Copo de Nieve

El modelamiento dimensional estructura datos en hechos y dimensiones para consultas analíticas rápidas.
Tabla de hechos (eventos medibles)
En el presente proyecto, el centro del modelo se encuentra en la tabla de hechos FACT_RENTABILIDAD, que almacena para cada operación de exportación:
El valor FOB (ingreso en USD)
El volumen exportado (peso neto en kg)
Principio aplicado: Las métricas derivadas (precio promedio por kilogramo, costo total estimado, margen de utilidad y ratio de rentabilidad) se calculan en la capa de visualización (Power BI) o durante el ETL, siguiendo el principio de que una tabla de hechos debe contener solo hechos atómicos e inmutables.
Dimensiones principales y subdimensiones (atributos contextuales)

| Tipo | Tabla | Propósito |
| --- | --- | --- |
| Dimensión principal | DIM_TIEMPO | Analizar evolución temporal (año, trimestre, mes, semana, día) |
| Dimensión principal | DIM_UBICACION | Analizar por país y continente de destino |
| Dimensión principal | DIM_PRODUCTO | Información base de la palta Hass |
| Dimensión principal | DIM_EXPORTADOR | Identificar competidores en el mercado peruano |
| Dimensión principal | DIM_ADUANA | Analizar puertos y puntos de embarque |
| Subdimensión | DIM_PAIS_TLC (dependiente de DIM_UBICACION) | Acuerdos comerciales y aranceles por país destino |
| Dimensión principal | DIM_VARIEDAD_CALIDAD | Variedad, calidad y método de producción (independiente) |

Jerarquías implementadas

| Dimensión | Jerarquía |
| --- | --- |
| DIM_TIEMPO | Año → Trimestre → Mes → Semana → Día |
| DIM_UBICACION | Continente → País |
| DIM_PAIS_TLC | País → Acuerdo TLC → Arancel aplicable |
| DIM_VARIEDAD_CALIDAD | Variedad → Categoría de calidad → Método de producción |

Notas metodológicas

| Nota | Descripción |
| --- | --- |
| Competencia y Logística | Las dimensiones DIM_EXPORTADOR y DIM_ADUANA permiten calcular el Índice de Concentración de Mercado (HHI) y optimizar rutas de exportación. |
| Costos (SCD Tipo 2) | DIM_COSTO se implementa con una estrategia SCD Tipo 2 (Slowly Changing Dimension) para mantener el historial de cambios en los costos de producción, empaque y logística. El detalle de atributos se presenta en la sección 5.2. |
| Fuentes Externas | El enriquecimiento con BCRP (tipo de cambio) y MINCETUR (aranceles) permite calcular un Margen Neto Ajustado que supera la limitación de los datos brutos de SUNAT. |



## 2.4 Procesos ETL

El proceso ETL (Extract, Transform, Load) es el núcleo de la arquitectura de Inteligencia de Negocios, responsable de garantizar la calidad, consistencia e integridad de los datos antes de ser depositados en el Data Mart.
El proyecto implementa un flujo ETL programático y automatizado basado en Python, utilizando las librerías pandas, dbfread, re (expresiones regulares) y sqlalchemy, estructurado en tres fases críticas:

### 2.4.1 Fase de Extracción

Consiste en la recolección de datos desde sistemas de origen heterogéneos. Se emplea una estrategia de ingesta de datos multisistema, respetando la periodicidad de cada fuente. Fueron detalladas en la sección 1.4 Alcance del Proyecto.

| Fuente | Datos extraídos | Formato | Periodicidad |
| --- | --- | --- | --- |
| SUNAT (ADUANET) | Microdatos de exportación de palta Hass (partida 0804400000) | DBF / TXT | Mensual (descarga manual programada) |
| BCRP | Tipo de cambio promedio (USD/PEN) para el período 2016-2024 | CSV / API | Extracción única (histórica) |
| MINCETUR | Aranceles aplicables por país destino y acuerdos TLC | CSV / Excel | Extracción única con actualizaciones anuales |
| MIDAGRI / Sierra Exportadora | Costos de referencia (producción, empaque, logística) | PDF / Excel | Extracción única (referencial) |


Procesamiento con Regex: El filtrado exclusivo de la variedad 'Hass' se realiza mediante expresiones regulares (Regex), eliminando variaciones ortográficas (ej. "Has", "HASS") y excluyendo productos procesados como "pulpa", "aceite" o "congelado".

### 2.4.2 Fase de Transformación:

Etapa más compleja donde reside la lógica de negocio. Para el modelo Copo de Nieve, la transformación se divide en cuatro subprocesos:

| Subproceso | Descripción |
| --- | --- |
| Limpieza y Deduplicación | Eliminación de registros duplicados (basado en NRO_DOCU + FECHA + CNAN) y exclusión de valores nulos o negativos en FOB_DOLPOL y PESO_NETO. |
| Procesamiento de Texto y Estandarización (Filtro Hass) | Uso de Expresiones Regulares (Regex) para explorar DESC_ADIC y DESC_COM, filtrando exclusivamente la variedad "HASS" y excluyendo "PULPA", "TROZOS", "CONGELADO" y "PROCESAMIENTO". También se extraen atributos de calidad y método de producción. |
| Enriquecimiento de Datos | Integración de fuentes externas mediante operaciones de merge: tipo de cambio (BCRP), aranceles (MINCETUR) y costos referenciales (DIM_COSTO). |
| Cálculo de Métricas | Los KPIs definidos en la sección 2.5 (Precio_Promedio_kg, Margen_Utilidad, Ratio_Rentabilidad) se calculan durante el ETL y se almacenan físicamente en la tabla de hechos FACT_RENTABILIDAD, siguiendo las fórmulas documentadas en dicha sección. |


### 2.4.3 Fase de Carga:

Involucra la inserción física de los datos en el motor de base de datos analítico (PostgreSQL). Para garantizar la estabilidad del esquema Copo de Nieve, se aplican los siguientes principios:

| Principio | Descripción |
| --- | --- |
| Secuencialidad e Integridad Referencial | La carga sigue un orden estricto: primero dimensiones independientes, luego dimensiones dependientes, finalmente la tabla de hechos. Esto asegura que ninguna llave foránea apunte a un registro inexistente. |
| Claves Sustitutas | Se generan identificadores numéricos propios dentro del Data Mart (PK autogenerados) para desligar el modelo analítico de los posibles cambios en los códigos de los sistemas de origen. |
| Control de Calidad | Implementación de un archivo de registro (log) que audita la cantidad de registros procesados, insertados y rechazados por errores de consistencia, asegurando la trazabilidad de la información. |


## 2.5 KPIs e Indicadores de Rendimiento

Un KPI (Key Performance Indicator) es un indicador clave de rendimiento que cuantifica el logro de un objetivo estratégico. Para el presente proyecto, se definen los siguientes KPIs, alineados con las necesidades del negocio y las nuevas capacidades del modelo Copo de Nieve:

| KPI | Fórmula resumida | Métrica (qué mide) | Fuentes | Meta | Impacto en la problemática |
| --- | --- | --- | --- | --- | --- |
| Precio Promedio FOB/kg | Σ(FOB) ÷ Σ(Peso Neto) | Valor promedio en USD por kilogramo exportado | SUNAT | Variable por destino | Permite identificar mercados premium y segmentar por rentabilidad potencial |
| Margen de Utilidad Estimado | Ingreso FOB – Costo estimado | Ganancia absoluta en USD por transacción | SUNAT + DIM_COSTO | Positivo (>0) | Evalúa si cada exportación genera ganancia antes de ajustes |
| Ratio de Rentabilidad | (Margen ÷ Ingreso FOB) × 100 | Porcentaje del ingreso que representa la utilidad | SUNAT + DIM_COSTO | 15% – 25% | Determina la eficiencia económica del negocio de palta Hass |
| Índice de Concentración por Destino | (FOB_país ÷ FOB_total) × 100 | Porcentaje de exportación concentrado en un país | SUNAT | < 70% (Top 3 países) | Mide vulnerabilidad geográfica; una concentración alta indica riesgo |
| Índice HHI (Exportadores) | Σ(FOB_exportador ÷ FOB_total)² | Nivel de competencia en el mercado (0=competencia perfecta, 10000=monopolio) | SUNAT (DIM_EXPORTADOR) | < 2500 | Identifica si el mercado peruano es competitivo o concentrado |
| Margen Neto Ajustado | (FOB × TC) – (Costo_Total × TC) – Aranceles | Rentabilidad real en moneda local después de tipo de cambio y aranceles | SUNAT + BCRP + MINCETUR | Positivo | Supera la limitación de SUNAT al considerar riesgos financieros externos |

Descripción detallada de cada KPI

| KPI | Descripción |
| --- | --- |
| KPI 1 - Precio Promedio FOB/kg | Identifica la evolución del precio y permite segmentar por destino para identificar mercados premium. |
| KPI 2 - Margen de Utilidad Estimado | Evalúa la rentabilidad generada por cada transacción de exportación en términos absolutos. |
| KPI 3 - Ratio de Rentabilidad | Determina qué porcentaje del ingreso representa la utilidad estimada. La meta del 15% al 25% se basa en estándares sectoriales de Sierra Exportadora. |
| KPI 4 - Índice de Concentración por Destino | Cuantifica la concentración geográfica y permite identificar oportunidades de diversificación. Una concentración inferior al 70% refleja una cartera diversificada. |
| KPI 5 - Índice HHI (Exportadores) | Mide el nivel de competencia en el mercado peruano. Un valor inferior a 2500 indica un mercado competitivo (no concentrado). |
| KPI 6 - Margen Neto Ajustado | Evalúa la rentabilidad real considerando el tipo de cambio (BCRP) y los aranceles (MINCETUR) del país destino, superando la limitación de los datos brutos de SUNAT. |

Relación entre KPIs y objetivos estratégicos (alineación con BSC)

| Objetivo Estratégico (desde BSC) | KPI asociado |
| --- | --- |
| Evaluar la rentabilidad potencial de la inversión (Perspectiva Financiera) | Ratio de Rentabilidad, Margen Neto Ajustado |
| Identificar los mejores mercados de destino (Perspectiva Cliente/Mercado) | Precio Promedio FOB/kg, Índice de Concentración por Destino |
| Reducir la concentración de riesgo (Perspectiva Cliente/Mercado) | Índice de Concentración por Destino, Índice HHI |
| Automatizar y validar el proceso ETL (Perspectiva Procesos Internos) | Metas de eficiencia y calidad (ver sección 2.6) |

Justificación de las metas

| Meta | Justificación | Fuente |
| --- | --- | --- |
| Ratio de Rentabilidad: 15% – 25% | Rango viable para productos agroexportadores no tradicionales | Sierra Exportadora (informes sectoriales 2023) |
| Concentración por destino: < 70% | Índice inferior al 70% refleja cartera diversificada; superior al 85% indica alta vulnerabilidad | Literatura de comercio exterior |
| Índice HHI: < 2500 | Valor inferior a 2500 indica mercado competitivo (no concentrado) | Literatura de comercio exterior |


## 2.6 Balanced Scorecard (BSC)

En el presente proyecto, el BSC permite alinear la construcción del Data Mart con el objetivo estratégico de Peruvian Andean Trout S.A.C.: analizar la rentabilidad potencial de la palta Hass como nueva línea de negocio, considerando factores de competencia, riesgos cambiarios y aranceles.
Análisis FODA del Proyecto

| Interno | Fortalezas (F) | Debilidades (D) |
| --- | --- | --- |
| Interno | F1. Equipo con conocimientos en BI y modelamiento de datos (Copo de Nieve). <br> F2. Metodología definida (ETL con Python, Regex, enriquecimiento externo). <br> F3. Enfoque en un producto específico (palta Hass) que permite profundidad analítica. | D1. Dependencia de datos públicos agregados (no se tienen costos reales internos). <br> D2. Limitada experiencia previa de la empresa en el sector agroexportador de palta. <br> D3. Sin acceso a datos de calidad, variedad o cliente final. |
| Externo | Oportunidades (O) | Amenazas (A) |
| Externo | O1. Alta demanda internacional sostenida de la palta Hass. <br> O2. Disponibilidad de datos históricos (2016-2024) de SUNAT. <br> O3. Posibilidad de enriquecer el análisis con fuentes externas (BCRP, MINCETUR, Sierra Exportadora). | A1. Volatilidad de precios internacionales por factores climáticos o geopolíticos. <br> A2. Competencia creciente de otros países exportadores (Chile, México, Colombia). <br> A3. Cambios en regulaciones o aranceles de los mercados destino. |

Mapa Estratégico del Proyecto (Perspectivas y Relaciones Causa-Efecto)

Justificación de las relaciones Causa-Efecto:

| Relación | Justificación |
| --- | --- |
| Aprendizaje → Procesos | Al aprender a integrar datos del BCRP (tipo de cambio) y MINCETUR (aranceles), se automatiza un proceso ETL más robusto que el actual (solo SUNAT). |
| Procesos → Cliente/Mercado | Un proceso automático y confiable que calcule KPIs como Precio FOB/kg y Margen Neto Ajustado permite a la gerencia identificar los mercados con mayor rentabilidad. |
| Cliente/Mercado → Financiera | Al identificar mercados "Premium" (con TLC, arancel 0%), la empresa puede enfocar sus esfuerzos comerciales en destinos que maximizan el ratio de rentabilidad. |


Tablero de Control Estratégico

| Perspectiva | Objetivo Estratégico | Indicador (KPI) | Meta / Rango Esperado | Iniciativa Estratégica |
| --- | --- | --- | --- | --- |
| Financiera | Evaluar la rentabilidad potencial de la inversión en palta Hass | Ratio de Rentabilidad Estimado | Rango meta: > 15% - 25% | Proyecto de inversión en palta Hass condicionado a resultados del Data Mart. |
| Cliente / Mercado | Identificar los 3 destinos con mayor rentabilidad potencial ajustada | Precio Promedio FOB/kg por destino + Margen Neto Ajustado | > $2.50 USD/kg en al menos 3 destinos | Dashboard comparativo de rentabilidad por país destino, incluyendo aranceles. |
| Cliente / Mercado | Reducir la concentración de riesgo de mercados y competidores | Índice de Concentración (Top 3 países / Total FOB) e Índice HHI | < 70% del FOB en 3 países; HHI < 2500 | Plan de prospección comercial hacia nuevos mercados identificados (ej. Asia o Medio Oriente). |
| Procesos Internos | Automatizar la integración y transformación de datos de SUNAT + fuentes externas | Eficiencia del proceso ETL | 100% de ejecuciones exitosas en < 5 minutos para 100,000 registros | Desarrollo de script ETL en Python con logging de errores y módulo de enriquecimiento. |
| Procesos Internos | Calcular KPIs con datos validados (filtro Hass y extracción de atributos) | Calidad de datos (registros válidos / totales) | > 95% de los registros extraídos son válidos | Implementación de reglas de validación en la fase de Transformación ETL (Regex, rangos, nulos). |
| Aprendizaje y Crecimiento | Incorporar nuevas fuentes de datos para enriquecer el análisis | Capacidad de integración de fuentes externas | Integración exitosa de al menos 3 variables externas | Desarrollo de módulo de enriquecimiento en Python que consuma APIs o archivos CSV del BCRP, MINCETUR y Sierra Exportadora. |

Justificación de las metas:

| Meta | Justificación | Fuente |
| --- | --- | --- |
| Ratio > 15% – 25% | Márgenes de rentabilidad viables para productos agroexportadores no tradicionales | Sierra Exportadora (2023) |
| Precio > $2.50 USD/kg | Precio promedio histórico de palta Hass peruana fluctúa entre $1.80 y $3.50 USD/kg. Un umbral de $2.50 califica mercados "premium" | SUNAT (2016-2024) |
| Concentración < 70% | Índice inferior al 70% refleja cartera diversificada; superior al 85% indica alta vulnerabilidad | Literatura de comercio exterior |
| HHI < 2500 | Valor inferior a 2500 indica mercado competitivo (no concentrado) | Literatura de comercio exterior |
| ETL < 5 min | La base de datos SUNAT para palta Hass no supera 100,000 registros; un script optimizado (pandas) procesa en < 2 minutos (umbral de aceptación: 5 min) | Estimación técnica |
| Calidad > 95% | Meta ambiciosa pero alcanzable para una fuente administrativa estructurada como SUNAT | Estimación técnica |



# 3. ANÁLISIS DEL CASO


## 3.1 Descripción del Negocio

La empresa Peruvian Andean Trout S.A.C., actualmente dedicada a la acuicultura (producción y comercialización de trucha para exportación), evalúa diversificarse hacia el mercado de la palta Hass (partida arancelaria 0804400000). El presente análisis permite evaluar la viabilidad de esta nueva línea de negocio mediante el estudio de su comportamiento en términos de precios, mercados de destino, competencia, costos de referencia y evolución temporal durante el período 2016-2024.
Partes interesadas (Stakeholders):

| Stakeholder | Rol en la solución | Expectativa |
| --- | --- | --- |
| Gerencia General | Decisor estratégico | Determinar viabilidad de inversión basada en KPIs de rentabilidad. |
| Planeamiento Estratégico | Evaluador de nuevas líneas | Identificar mercados rentables y evaluar concentración de riesgo. |
| Finanzas | Analista de rentabilidad | Validar márgenes y ratios ajustados por tipo de cambio y aranceles. |
| Comercio Exterior | Asesor logístico y competitivo | Evaluar destinos, costos logísticos, competidores y aduanas de salida. |

Organigrama de Peruvian Andean Trout S.A.C.
La empresa Peruvian Andean Trout S.A.C. presenta la siguiente estructura organizacional para la toma de decisiones relacionadas con el proyecto de diversificación hacia la palta Hass:

| Nivel | Cargo / Rol | Responsabilidad en el proyecto |
| --- | --- | --- |
| 1 | Gerencia General | Decisor estratégico. Aprueba inversión. |
| 2 | Gerente de Planeamiento | Evalúa mercados y concentración de riesgo. |
| 2 | Gerente de Finanzas | Valida márgenes y define reglas de negocio. |
| 2 | Gerente de Comercio Exterior | Usuario líder; define requerimientos aduaneros. |
| 3 | Equipo de Proyecto (Consultores BI) | Diseña, implementa y opera el Data Mart. |



| Ubicación | Error detectado / Debilidad | Justificación Técnica | Propuesta de Corrección |
| --- | --- | --- | --- |
| Rol: Analista de BI | Concentración excesiva de funciones. | Un solo rol no suele diseñar (arquitectura), implementar (ETL) y operar (mantenimiento) en entornos corporativos reales sin supervisión. | Desglosar o añadir un Líder Técnico/Arquitecto de Datos para la validación del modelo dimensional (Star Schema). |
| Rol: Gerente de Finanzas | Responsabilidad pasiva. | En un Data Mart de rentabilidad, este rol debe certificar las fuentes de datos financieras para evitar discrepancias. | Cambiar a: "Valida márgenes y define las reglas de negocio para el cálculo de rentabilidad". |
| Rol: G. Comercio Exterior | Alcance consultivo limitado. | Si el Data Mart es sobre exportaciones (como aguacate/trucha), este rol es el Usuario Líder (Champion). | Cambiar a: "Usuario líder; define requerimientos de información aduanera y logística". |


Nota: El equipo de proyecto actúa como consultor externo especializado en Inteligencia de Negocios.
Equipo de trabajo:
El presente proyecto es desarrollado por un equipo de 6 integrantes:

| Integrante | Rol |
| --- | --- |
| David Choy | Líder de proyecto / Aprobador |
| Cristian Cardenas | Analista de requerimientos |
| Bruno Guillena | Modelador de datos |
| Lady Loayza | Desarrolladora ETL |
| Francis Moreno | Desarrollador de dashboards |
| Jeampieer's Salvador | Documentador |


## 3.2 Requerimientos del Negocio

Los requerimientos fueron recopilados de:
Manual de procesos internos de Peruvian Andean Trout S.A.C. (diversificación)
Normas ISO 9001/22000 aplicables a agroexportación
Observaciones directas sobre disponibilidad de datos en SUNAT/ADUANET
Tipos de requerimientos del negocio

| Tipo | Descripción | Ejemplo en el proyecto |
| --- | --- | --- |
| Estratégicos | Apoyan objetivos de negocio a largo plazo | Evaluar viabilidad de nueva línea de negocio |
| Operativos | Soportan procesos diarios | Generar reportes mensuales de rentabilidad por destino |
| Técnicos | Definen la implementación tecnológica | Data Mart en modelo Copo de Nieve |

Matriz de requerimientos (prioridad, fuente, conflicto, solución)

| Requerimiento | Prioridad | Fuente | Conflicto identificado | Solución propuesta |
| --- | --- | --- | --- | --- |
| Conocer rentabilidad por destino | Alta | Gerencia | Datos SUNAT sin costos reales | Estimar costos con valores de referencia (Sierra Exportadora) |
| Analizar evolución temporal | Alta | Planeamiento | Granularidad diaria vs mensual | Implementar jerarquías en DIM_TIEMPO (año → trimestre → mes → semana) |
| Comparar con competidores | Media | Comercio Exterior | Datos de competidores no públicos | Usar DIM_EXPORTADOR para análisis de concentración de mercado (índice HHI) |
| Evaluar impacto de tipo de cambio y aranceles | Alta | Finanzas | Datos SUNAT sin tipo de cambio ni aranceles | Integrar BCRP (tipo de cambio) y MINCETUR (aranceles) como fuentes externas |

Nota sobre la dimensión CLIENTE (importador final)
SUNAT no registra el nombre ni RUC del importador/comprador final en los microdatos de exportación públicos. Por lo tanto, no es posible construir una dimensión DIM_CLIENTE directa.
Solución proxy aprobada: Se utiliza DIM_UBICACION (país de destino) como aproximación del mercado consumidor.
El análisis de rentabilidad potencial no requiere identificar clientes individuales, sino mercados objetivo.
Los aranceles y acuerdos comerciales (TLC) dependen exclusivamente del país destino, no del importador específico.
La concentración de riesgo se evalúa a nivel de país, no de cliente final.
Se reconoce esta limitación como una simplificación válida para el alcance del proyecto (evaluación de viabilidad de inversión previa a la entrada al mercado).
Análisis de conflictos y soluciones

| Conflicto principal | Solución |
| --- | --- |
| La SUNAT no proporciona costos reales, tipo de cambio ni aranceles. | Estimación de costos basada en valores de referencia de Sierra Exportadora. Integración de BCRP para tipo de cambio y MINCETUR para aranceles. |


Matriz de necesidades del negocio (Requerimientos vs KPIs):


| Necesidad del Negocio | KPI (Indicador) | Dimensiones de Análisis | Prioridad |
| --- | --- | --- | --- |
| Identificar evolución del precio | Precio Promedio FOB/kg | Tiempo (Mes) | Alta |
| Evaluar evolución de la rentabilidad | Ratio de Rentabilidad | Tiempo (Año), Geografía (País) | Alta |
| Identificar mejores mercados | Precio Promedio FOB/kg | Geografía (País, Continente) | Alta |
| Evaluar concentración de riesgo | Índice de Concentración | Geografía (País), Exportador | Media |
| Analizar competencia | Participación de mercado por exportador | Exportador, Tiempo | Media |
| Evaluar impacto logístico | Costo logístico por destino | Geografía (País), Aduana | Media |

Nota técnica: El KPI "Precio promedio FOB/kg" se aplica con dos dimensiones de análisis diferentes (Tiempo y Geografía) para responder a dos necesidades de negocio distintas. Esto no constituye un KPI adicional, sino el mismo indicador utilizado en diferentes ejes de análisis multidimensional, una de las ventajas fundamentales del modelo dimensional.
Matriz Interfuncional

| Actores / Etapas | Responsabilidad |
| --- | --- |
| SUNAT/ADUANET | Proveer microdatos de exportación (partida 0804400000) |
| Analista de BI | Extraer, transformar y cargar datos al Data Mart |
| Gerencia General | Tomar decisiones de inversión basadas en los resultados |

Matriz RACI
A continuación, se detallan las responsabilidades de cada integrante del equipo por tarea específica:

| Tarea / Integrante | David Choy | Cristian Cardenas | Bruno Guillena | Lady Loayza | Francis Moreno | Jeampieer's Salvador |
| --- | --- | --- | --- | --- | --- | --- |
| Levantamiento de Requerimientos | A | R | C | I | C | I |
| Modelamiento (Copo de Nieve) | R | C | A | R | I | C |
| Script ETL en Python | R | I | I | C | A | R |
| Diseño de Dashboards | C | R | R | A | I | I |
| Documentación PC1 | I | A | I | R | R | A |

R = Responsable, A = Aprobador, C = Consultado, I = Informado

## 3.3 KPIs Relevantes


### 3.3.1 Proceso de Definición de los KPIs

Los KPIs (Key Performance Indicators) del presente proyecto fueron definidos siguiendo un proceso estructurado de 4 etapas, que asegura que cada indicador esté alineado con los objetivos del negocio y sea técnicamente viable de calcular con las fuentes de datos disponibles.
Etapa 1: Identificación de necesidades del negocio
Se realizaron reuniones con los stakeholders (Gerencia General, Planeamiento Estratégico, Finanzas y Comercio Exterior) para identificar sus necesidades de información. De estas reuniones surgieron las siguientes preguntas clave:

| Stakeholder | Pregunta clave | Necesidad de negocio |
| --- | --- | --- |
| Gerencia General | "¿Es rentable invertir en palta Hass?" | Evaluar la viabilidad financiera de la diversificación |
| Planeamiento Estratégico | "¿A qué mercados conviene exportar?" | Identificar destinos con mayor potencial |
| Finanzas | "¿Cuál es la rentabilidad real considerando costos, tipo de cambio y aranceles?" | Calcular márgenes ajustados a condiciones reales |
| Comercio Exterior | "¿Quiénes son nuestros competidores? ¿Qué puertos son más eficientes?" | Analizar el mercado y optimizar la logística |

Etapa 2: Revisión de estándares sectoriales
Se consultaron informes y guías del sector agroexportador para validar que los KPIs propuestos sean comparables con estándares de la industria:

| Fuente consultada | Aporte al proyecto |
| --- | --- |
| Sierra Exportadora (2023) | Estableció la meta de rentabilidad viable entre 15% y 25% para productos agroexportadores no tradicionales |
| Literatura de comercio exterior | Definió que un índice de concentración inferior al 70% refleja una cartera diversificada, y que un HHI inferior a 2500 indica un mercado competitivo |
| Reportes de comercio regional (MINCETUR) | Proporcionó información sobre los principales mercados destino de la palta peruana |
| Documentación técnica del BCRP | Confirmó la disponibilidad de la serie histórica de tipo de cambio (PD04638PD) |

Etapa 3: Viabilidad técnica
Para cada KPI propuesto, se verificó que fuera técnicamente viable de calcular con las fuentes de datos disponibles:

| Fuente de datos | ¿Qué información aporta? | ¿Qué KPI permite calcular? |
| --- | --- | --- |
| SUNAT | Valor FOB, peso neto, país destino, RUC del exportador | Precio FOB/kg, índice de concentración, HHI |
| BCRP | Tipo de cambio histórico USD/PEN | Margen neto ajustado |
| MINCETUR | Aranceles por país destino, acuerdos TLC | Clasificación de mercados "Premium" |
| MIDAGRI / Sierra Exportadora | Costos referenciales de producción, empaque y logística | Margen de utilidad, ratio de rentabilidad |

Etapa 4: Selección final y priorización
Se priorizaron los KPIs según su impacto en la toma de decisiones y su viabilidad técnica. La siguiente tabla resume el proceso de selección:

| KPI | ¿Responde a qué necesidad? | ¿Es viable? | Prioridad |
| --- | --- | --- | --- |
| Precio Promedio FOB/kg | Identificar mercados premium | Sí (SUNAT) | Alta |
| Margen de Utilidad Estimado | Evaluar ganancia por operación | Sí (SUNAT + costos) | Alta |
| Ratio de Rentabilidad | Decidir viabilidad de inversión | Sí (SUNAT + costos) | Alta |
| Índice de Concentración por Destino | Evaluar riesgo geográfico | Sí (SUNAT) | Media |
| Índice HHI | Evaluar nivel de competencia | Sí (SUNAT) | Media |
| Margen Neto Ajustado | Calcular rentabilidad real en soles | Sí (SUNAT + BCRP + MINCETUR) | Alta |


### 3.3.2 Valor Aportado por Cada KPI

A continuación, se detalla el valor específico que cada KPI aporta a la toma de decisiones de Peruvian Andean Trout S.A.C.:

KPI 1: Precio Promedio FOB/kg

| Atributo | Valor |
| --- | --- |
| Fórmula | Σ(FOB) ÷ Σ(Peso Neto) |
| Valor aportado | Permite identificar qué países pagan un mejor precio por kilogramo de palta Hass. Por ejemplo, si Países Bajos tiene un precio de <br> 2.80USD/kg España 2.10 USD/kg, la empresa puede priorizar sus esfuerzos comerciales hacia Países Bajos. |
| Decisión que impacta | Selección de mercados objetivo para la exportación. |
| Frecuencia de cálculo | Mensual |

KPI 2: Margen de Utilidad Estimado

| Atributo | Valor |
| --- | --- |
| Fórmula | Ingreso FOB – Costo estimado (producción + empaque + logística) |
| Valor aportado | Muestra la ganancia en términos absolutos (USD) por cada operación de exportación. Permite comparar la rentabilidad de diferentes envíos, identificando cuáles generan mayor retorno económico. |
| Decisión que impacta | Evaluación de la conveniencia de cada transacción; identificación de operaciones con bajo margen. |
| Frecuencia de cálculo | Mensual |

KPI 3: Ratio de Rentabilidad

| Atributo | Valor |
| --- | --- |
| Fórmula | (Margen ÷ Ingreso FOB) × 100 |
| Valor aportado | Indica qué porcentaje del ingreso total se convierte en ganancia. Una rentabilidad del 20% significa que por cada <br> 100USDvendidos, <br> 100USDvendidos,20 USD son utilidad. Permite comparar la eficiencia de diferentes destinos y períodos. |
| Decisión que impacta | Decisión final de inversión (si el ratio está dentro de la meta del 15%-25%, el proyecto es viable). |
| Meta | 15% – 25% (según Sierra Exportadora) |
| Frecuencia de cálculo | Mensual |

KPI 4: Índice de Concentración por Destino

| Atributo | Valor |
| --- | --- |
| Fórmula | (FOB_país_X ÷ FOB_total) × 100 |
| Valor aportado | Mide qué porcentaje del total exportado se concentra en unos pocos países. Si el Top 3 países representa el 80% de las exportaciones, la empresa tiene un alto riesgo de dependencia. Si un país impone restricciones o reduce su demanda, el impacto sería severo. |
| Decisión que impacta | Estrategia de diversificación geográfica; plan de prospección comercial a nuevos mercados. |
| Meta | < 70% (Top 3 países) |
| Frecuencia de cálculo | Anual |

KPI 5: Índice HHI (Herfindahl-Hirschman)

| Atributo | Valor |
| --- | --- |
| Fórmula | Σ(FOB_exportador ÷ FOB_total)² |
| Valor aportado | Mide el nivel de competencia en el mercado de exportadores peruanos. Un HHI bajo (<2500) indica que hay muchos exportadores compitiendo, lo que es favorable para nuevos entrantes. Un HHI alto (>2500) indica que pocas empresas dominan el mercado, lo que podría significar barreras de entrada. |
| Decisión que impacta | Evaluación del nivel de competencia; identificación de los principales competidores. |
| Meta | < 2500 |
| Frecuencia de cálculo | Anual |

KPI 6: Margen Neto Ajustado

| Atributo | Valor |
| --- | --- |
| Fórmula | (Ingreso FOB × TC) – (Costo_Total × TC) – Aranceles |
| Valor aportado | Este es el KPI más completo. Incorpora tres variables críticas que SUNAT no proporciona: (1) tipo de cambio (BCRP) para convertir a soles, (2) costos referenciales (MIDAGRI) para conocer el costo real, y (3) aranceles (MINCETUR) para reflejar el costo de importación en el país destino. Permite conocer la rentabilidad real en moneda local. |
| Decisión que impacta | Evaluación financiera realista de la inversión; comparación de rentabilidad entre países considerando sus aranceles. |
| Meta | Positivo (mayor a 0) |
| Frecuencia de cálculo | Anual |


### 3.3.3 Resumen de KPIs y su valor estratégico


| KPI | Valor estratégico para la empresa |
| --- | --- |
| Precio Promedio FOB/kg | Identificar mercados que pagan mejor precio |
| Margen de Utilidad Estimado | Conocer la ganancia absoluta por operación |
| Ratio de Rentabilidad | Decidir si la inversión es viable (meta: 15-25%) |
| Índice de Concentración | Evaluar riesgo de dependencia de pocos países |
| Índice HHI | Conocer el nivel de competencia en el mercado |
| Margen Neto Ajustado | Conocer la rentabilidad real en soles, considerando tipo de cambio y aranceles |


Matriz de necesidades de KPIs

| Necesidad del Negocio | KPI (Indicador) | Dimensiones de Análisis | Prioridad | Beneficio esperado |
| --- | --- | --- | --- | --- |
| Identificar evolución del precio | Precio Promedio FOB/kg | Tiempo (Mes) | Alta | Identificar tendencias estacionales |
| Evaluar evolución de la rentabilidad | Ratio de Rentabilidad | Tiempo (Año), Geografía (País) | Alta | Evaluar viabilidad de inversión |
| Identificar mejores mercados | Precio Promedio FOB/kg | Geografía (País, Continente) | Alta | Identificar destinos premium |
| Evaluar concentración de riesgo | Índice de Concentración (HHI) | Geografía (País), Exportador | Media | Diversificar cartera de clientes/países |
| Analizar competencia | Participación de mercado por exportador | Exportador, Tiempo | Media | Identificar competidores dominantes |
| Evaluar impacto logístico | Costo logístico por destino | Geografía (País), Aduana | Media | Optimizar rutas de exportación |

Los KPIs definidos corresponden a los presentados en la sección 2.5 (Marco Teórico). A continuación, se presentan sus fórmulas:

| KPI | Fórmula | Métrica | Frecuencia | Fuentes involucradas |
| --- | --- | --- | --- | --- |
| Precio Promedio FOB/kg | Σ(FOB) / Σ(Peso Neto) | USD por kilogramo | Mensual | SUNAT |
| Margen de Utilidad Estimado | Ingreso FOB - Costo estimado | USD | Mensual | SUNAT + DIM_COSTO |
| Ratio de Rentabilidad | (Margen / Ingreso) × 100 | Porcentaje | Mensual | SUNAT + DIM_COSTO |
| Índice de Concentración (HHI) | Σ(FOB_exportador / FOB_total)^2 | Porcentaje | Anual | SUNAT (DIM_EXPORTADOR) |
| Margen Neto Ajustado | (Ingreso FOB × TC) - (Costo_Total × TC) - Aranceles | USD | Anual | SUNAT + BCRP + MINCETUR |


Nota sobre el Margen Neto Ajustado: Este KPI incorpora el tipo de cambio (BCRP) para convertir los márgenes a moneda local (PEN) y los aranceles (MINCETUR) para reflejar el costo real de importación en el país destino. Permite una evaluación más realista de la rentabilidad neta.
Estos valores permitirán a la gerencia evaluar rápidamente si la diversificación hacia la palta Hass es viable y si los resultados se encuentran dentro de los parámetros esperados (rentabilidad meta: 15%-25%). Los valores específicos para Precio y Margen serán determinados tras el procesamiento de datos.

## 3.4 Fuentes de Datos

La arquitectura se alimenta de múltiples fuentes de datos, tanto primarias como externas, para enriquecer el análisis y superar las limitaciones de los datos brutos de SUNAT.
Fuentes de datos:

| Fuente | Descripción | Formato | Uso en el proyecto |
| --- | --- | --- | --- |
| SUNAT (ADUANET) | Microdatos de exportación de palta Hass. | DBF / TXT | Base del Data Mart (transacciones) |
| BCRP | Serie histórica de tipo de cambio (USD/PEN). | CSV / API | Ajuste de rentabilidad a moneda local (soles) |
| MINCETUR | Aranceles por país destino, acuerdos TLC, puertos. | CSV / Excel | Cálculo de Margen Neto Ajustado y poblar DIM_PAIS_TLC |
| MIDAGRI / Sierra Exportadora | Costos de referencia (producción, empaque, logística). | PDF / Excel | Poblar DIM_COSTO y calcular Costo_Total_Estimado |

Variables disponibles desde SUNAT (ADUANET):

| Campo | Descripción | Uso en el proyecto |
| --- | --- | --- |
| CNAN | Partida arancelaria | Filtro (0804400000) para DIM_PRODUCTO |
| FECHA | Fecha de embarque | DIM_TIEMPO |
| CPAIS | Código de país destino | DIM_UBICACION |
| PAIS_DESC | Nombre del país | DIM_UBICACION |
| FOB_DOLPOL | Valor FOB en dólares | FACT_RENTABILIDAD.Valor_FOB |
| PESO_NETO | Peso neto en kilogramos | FACT_RENTABILIDAD.Volumen_Exportado |
| NRO_DOCU | RUC del exportador | DIM_EXPORTADOR |
| EXPORTADOR | Nombre del exportador | DIM_EXPORTADOR |
| CADUANA | Código de aduana | DIM_ADUANA |
| ADUA_DESC | Descripción de aduana | DIM_ADUANA |
| DESC_ADIC / DESC_COM | Descripción adicional del producto | Extracción de variedad (Hass), calidad y método orgánico para DIM_VARIEDAD_CALIDAD |

Limitaciones de la fuente y soluciones implementadas:

| Limitación | Solución en el proyecto |
| --- | --- |
| No incluye costos reales de producción o logística | Uso de DIM_COSTO con valores de referencia de MIDAGRI / Sierra Exportadora |
| No identifica al cliente/importador final | DIM_UBICACION actúa como proxy del mercado destino |
| No incluye datos de calidad del producto | Extracción de atributos desde DESC_ADIC mediante Regex hacia DIM_VARIEDAD_CALIDAD |
| No incluye tipo de cambio para ajuste monetario | Integración con BCRP (tipo de cambio USD/PEN) |
| No incluye aranceles por país destino | Integración con MINCETUR para poblar DIM_PAIS_TLC |


## 3.5 Requerimientos Funcionales y No Funcionales


### 3.5.1 Requerimientos Funcionales (RF)

Los requerimientos funcionales describen las capacidades específicas que el Data Mart debe ofrecer a los usuarios. Cada requerimiento incluye: identificador, nombre, descripción detallada, actor involucrado, entrada, proceso y salida esperada.

RF01: Integración de datos de exportación desde SUNAT

| Atributo | Valor |
| --- | --- |
| Identificador | RF01 |
| Nombre | Extracción y carga de microdatos de exportación |
| Descripción | El sistema debe extraer los microdatos de exportación de palta Hass (partida arancelaria 0804400000) desde los archivos DBF/TXT de SUNAT/ADUANET correspondientes al período 2016-2024. |
| Actor | Analista de BI / Proceso ETL automatizado |
| Entrada | Archivos DBF/TXT de SUNAT con campos: FECHA, CPAIS, PAIS_DESC, CNAN, FOB_DOLPOL, PESO_NETO, NRO_DOCU, EXPORTADOR, CADUANA, ADUA_DESC, DESC_ADIC, DESC_COM |
| Proceso | Lectura mediante librería dbfread de Python, conversión a DataFrame de pandas, validación de columnas obligatorias |
| Salida esperada | Tabla temporal tmp_SUNAT_raw con los 12 campos extraídos sin transformaciones |
| Prioridad | Alta (Crítica) |

RF02: Filtrado exclusivo de la variedad Hass

| Atributo | Valor |
| --- | --- |
| Identificador | RF02 |
| Nombre | Filtro de producto por variedad Hass |
| Descripción | El sistema debe aplicar un filtro para incluir exclusivamente los registros que correspondan a la variedad Hass, excluyendo automáticamente pulpa, congelados, trozos y productos procesados. |
| Actor | Proceso ETL (fase de transformación) |
| Entrada | Tabla tmp_SUNAT_raw (campos DESC_ADIC, DESC_COM) |
| Proceso | Aplicar expresión regular r'\bHASS?\b' para filtro positivo; aplicar expresión regular r'\b(PULPA|TROZOS|CONGELADO|PROCESAMIENTO)\b' para filtro negativo; convertir ambos campos a mayúsculas antes de evaluar |
| Salida esperada | Tabla tmp_SUNAT_filtrada_HASS con solo registros que contengan "HASS" y no contengan términos excluyentes |
| Prioridad | Alta (Crítica) |

RF03: Extracción de atributos de calidad desde texto no estructurado

| Atributo | Valor |
| --- | --- |
| Identificador | RF03 |
| Nombre | Extracción de variedad, categoría de calidad y método de producción |
| Descripción | El sistema debe extraer automáticamente, mediante expresiones regulares (Regex), los atributos de calidad del producto desde los campos DESC_ADIC y DESC_COM. |
| Actor | Proceso ETL (fase de transformación) |
| Entrada | Tabla tmp_SUNAT_filtrada_HASS (campos DESC_ADIC, DESC_COM) |
| Proceso | Aplicar Regex: r'\bHASS?\b' → variedad; r'CAT[\s\.]*1' → CAT 1; r'CAT[\s\.]*2' → CAT 2; r'ORGANIC[OA]' → método orgánico; caso contrario → convencional |
| Salida esperada | Tabla con columnas adicionales: Variedad, Categoria_Calidad, Metodo_Produccion |
| Prioridad | Alta |

RF04: Integración de tipo de cambio (BCRP)

| Atributo | Valor |
| --- | --- |
| Identificador | RF04 |
| Nombre | Carga de serie histórica de tipo de cambio USD/PEN |
| Descripción | El sistema debe integrar la serie histórica de tipo de cambio del BCRP (serie PD04638PD) para el período 2016-2024, con granularidad diaria, incluyendo tratamiento de días no hábiles (forward-fill). |
| Actor | Proceso ETL (fase de extracción y transformación) |
| Entrada | Archivo CSV/Excel con campos: FECHA, TC_USD_PEN, ES_DIA_HABIL |
| Proceso | Cargar archivo, estandarizar formato de fecha (YYYY-MM-DD), validar que no haya valores nulos, aplicar forward-fill para días no hábiles usando el último valor hábil registrado |
| Salida esperada | Tabla DIM_FINANZAS poblada con registro diario de tipo de cambio |
| Prioridad | Alta |

RF05: Integración de aranceles y acuerdos comerciales (MINCETUR)

| Atributo | Valor |
| --- | --- |
| Identificador | RF05 |
| Nombre | Carga de aranceles por país destino y acuerdos TLC |
| Descripción | El sistema debe integrar la información de aranceles aplicables por país destino y los Tratados de Libre Comercio (TLC) vigentes con Perú, según datos del MINCETUR. |
| Actor | Proceso ETL (fase de extracción y transformación) |
| Entrada | Archivo CSV/Excel con campos: PAIS_DESTINO, CODIGO_PAIS, ACUERDO_TLC, ARANCEL_PORCENTAJE, CATEGORIA_MERCADO (Premium/Estándar) |
| Proceso | Validar que cada país tenga un registro único; verificar que los aranceles estén en formato decimal (0.00 para países con TLC); poblar la subdimensión DIM_PAIS_TLC |
| Salida esperada | Tabla DIM_PAIS_TLC poblada con acuerdos comerciales por país |
| Prioridad | Alta |

RF06: Integración de costos referenciales (MIDAGRI / Sierra Exportadora)

| Atributo | Valor |
| --- | --- |
| Identificador | RF06 |
| Nombre | Carga de costos referenciales de producción, empaque y logística |
| Descripción | El sistema debe cargar los costos referenciales por kilogramo para las tres fases de la cadena de valor: producción (campo), empaque (packing) y logística (transporte + puerto + agenciamiento). |
| Actor | Proceso ETL (fase de extracción y transformación) |
| Entrada | Archivo Excel con campos: ID_Costo, Tipo_Costo, Subcategoria, Valor_Unitario_USD, Region_Destino, Fecha_Vigencia_Inicio, Fecha_Vigencia_Fin, Es_Vigente |
| Proceso | Implementar lógica SCD Tipo 2: si un costo cambia, no se sobreescribe el registro histórico; se crea un nuevo registro con nueva Fecha_Vigencia_Inicio y se marca el anterior con Fecha_Vigencia_Fin y Es_Vigente = FALSE |
| Salida esperada | Tabla DIM_COSTO poblada con historial de costos (SCD Tipo 2) |
| Prioridad | Alta |

RF07: Cálculo de KPIs de rentabilidad

| Atributo | Valor |
| --- | --- |
| Identificador | RF07 |
| Nombre | Cálculo automático de los 6 KPIs definidos |
| Descripción | El sistema debe calcular automáticamente los siguientes KPIs a partir de los datos integrados: Precio FOB/kg, Margen de Utilidad Estimado, Ratio de Rentabilidad, Índice de Concentración por Destino, Índice HHI, Margen Neto Ajustado. |
| Actor | Proceso ETL / Power BI |
| Entrada | Tabla FACT_RENTABILIDAD (Valor_FOB, Volumen_Exportado) + dimensiones (DIM_COSTO, DIM_FINANZAS, DIM_UBICACION, DIM_EXPORTADOR) |
| Proceso | Aplicar fórmulas documentadas en sección 2.5; para KPIs derivados (margen, ratio), calcular en Power BI; para KPIs agregados (HHI, concentración), calcular en ETL o vistas materializadas |
| Salida esperada | KPIs disponibles en dashboards de Power BI |
| Prioridad | Alta |

RF08: Generación de reportes en Power BI

| Atributo | Valor |
| --- | --- |
| Identificador | RF08 |
| Nombre | Dashboards interactivos por stakeholder |
| Descripción | El sistema debe generar dashboards en Power BI accesibles para cada stakeholder, con visualizaciones específicas según su rol: Gerencia General (KPIs consolidados), Planeamiento (tendencias y concentración), Finanzas (márgenes ajustados), Comercio Exterior (mercados y logística). |
| Actor | Gerencia General, Planeamiento Estratégico, Finanzas, Comercio Exterior |
| Entrada | Data Mart (tablas FACT_RENTABILIDAD y dimensiones) |
| Proceso | Conectar Power BI al motor de base de datos (PostgreSQL); crear medidas DAX para KPIs derivados; diseñar visualizaciones por stakeholder |
| Salida esperada | 4 dashboards interactivos (uno por área) con filtros por año, país, exportador, aduana |
| Prioridad | Alta |

RF09: Clasificación automática de mercados "Premium"

| Atributo | Valor |
| --- | --- |
| Identificador | RF09 |
| Nombre | Identificación de mercados con TLC y arancel 0% |
| Descripción | El sistema debe clasificar automáticamente los países destino en dos categorías: "Premium" (aquellos con Tratado de Libre Comercio vigente con Perú y arancel del 0%) y "Estándar" (países sin TLC o con arancel mayor a 0%). |
| Actor | Proceso ETL (población de DIM_PAIS_TLC) / Power BI |
| Entrada | Tabla DIM_PAIS_TLC (campos Acuerdo_TLC, Arancel_Porcentaje) |
| Proceso | Asignar Categoria_Mercado = 'Premium' si Acuerdo_TLC IS NOT NULL y Arancel_Porcentaje = 0; caso contrario, 'Estándar' |
| Salida esperada | Segmentación de mercados disponible en dashboards para filtrar por categoría |
| Prioridad | Media |

RF10: Registro de trazabilidad (Log de ETL)

| Atributo | Valor |
| --- | --- |
| Identificador | RF10 |
| Nombre | Bitácora de ejecución del proceso ETL |
| Descripción | El sistema debe generar un archivo de registro (log) cada vez que se ejecuta el proceso ETL, documentando la cantidad de registros extraídos, transformados, cargados y rechazados, así como los errores encontrados. |
| Actor | Proceso ETL / Analista de BI |
| Entrada | Datos procesados en cada fase del ETL |
| Proceso | Al inicio: registrar timestamp y parámetros de ejecución; durante la extracción: contar registros leídos por fuente; durante transformación: contar registros filtrados (incluidos/excluidos); durante carga: contar registros insertados por tabla; al final: escribir resumen en archivo .log |
| Salida esperada | Archivo etl_YYYYMMDD_HHMMSS.log con trazabilidad completa |
| Prioridad | Media |


### 3.5.2 Requerimientos No Funcionales (RNF)

Los requerimientos no funcionales describen atributos de calidad que debe cumplir el sistema: rendimiento, disponibilidad, seguridad, escalabilidad, usabilidad, mantenibilidad, confiabilidad y portabilidad.
RNF01: Rendimiento

| Atributo | Valor |
| --- | --- |
| Identificador | RNF01 |
| Nombre | Tiempo de procesamiento ETL |
| Descripción | El proceso ETL completo (extracción, transformación y carga) para el total de registros históricos (aproximadamente 100,000 registros de SUNAT para palta Hass en el período 2016-2024) debe completarse en un tiempo máximo de 5 minutos en un equipo estándar (CPU i5, 8GB RAM). |
| Métrica | Tiempo transcurrido desde el inicio de la extracción hasta la finalización de la carga |
| Condición de aceptación | 100% de las ejecuciones exitosas deben cumplir con el tiempo límite |
| Prioridad | Alta |

RNF02: Disponibilidad

| Atributo | Valor |
| --- | --- |
| Identificador | RNF02 |
| Nombre | Disponibilidad del Data Mart para consultas |
| Descripción | El Data Mart debe estar disponible para consultas analíticas durante el horario laboral (8:00 a.m. a 6:00 p.m., de lunes a viernes), con una disponibilidad mínima del 99% en dicho horario. |
| Métrica | Porcentaje de tiempo en que el Data Mart responde a consultas |
| Condición de aceptación | 99% de disponibilidad en horario laboral (excluyendo mantenimientos programados) |
| Prioridad | Alta |

RNF03: Seguridad

| Atributo | Valor |
| --- | --- |
| Identificador | RNF03 |
| Nombre | Control de acceso por rol |
| Descripción | El acceso a los dashboards de Power BI y a las tablas del Data Mart debe estar restringido según el rol del usuario. Se definen 4 roles: Administrador (acceso total), Gerencia (KPIs consolidados), Finanzas (datos financieros), Comercio Exterior (datos operativos). |
| Métrica | Número de accesos no autorizados registrados |
| Condición de aceptación | Cero accesos no autorizados durante la operación normal |
| Prioridad | Alta |



| Atributo | Valor |
| --- | --- |
| Identificador | RNF03.1 |
| Nombre | Confidencialidad de datos sensibles |
| Descripción | Los datos de exportación no deben ser modificables por usuarios finales; solo el proceso ETL automatizado tiene permisos de escritura en las tablas del Data Mart. |
| Condición de aceptación | Usuarios finales tienen solo permisos de lectura (SELECT) |
| Prioridad | Alta |

RNF04: Escalabilidad

| Atributo | Valor |
| --- | --- |
| Identificador | RNF04 |
| Nombre | Capacidad de incorporar nuevos productos |
| Descripción | El modelo dimensional debe permitir la incorporación de nuevos productos agroexportadores (ej. quinua, mango, arándanos) sin necesidad de rediseñar la arquitectura completa. Esto se logra mediante la dimensión DIM_PRODUCTO y el filtro de partida arancelaria. |
| Métrica | Esfuerzo estimado en horas para agregar un nuevo producto |
| Condición de aceptación | Agregar un nuevo producto no debe requerir más de 2 horas de trabajo (cambiar filtro de partida y actualizar documentación) |
| Prioridad | Media |

RNF05: Usabilidad

| Atributo | Valor |
| --- | --- |
| Identificador | RNF05 |
| Nombre | Facilidad de uso de los dashboards |
| Descripción | Los dashboards de Power BI deben ser intuitivos y no requerir capacitación extensa. Cada dashboard debe incluir: (1) título claro del análisis, (2) filtros visibles en la parte superior, (3) tooltips explicativos al pasar el cursor sobre los gráficos, (4) botón de exportación a PDF/Excel. |
| Métrica | Tiempo promedio para que un usuario nuevo realice una consulta básica |
| Condición de aceptación | Un usuario nuevo debe poder obtener el precio FOB/kg por país en menos de 2 minutos sin ayuda externa |
| Prioridad | Media |

RNF06: Mantenibilidad

| Atributo | Valor |
| --- | --- |
| Identificador | RNF06 |
| Nombre | Documentación del código ETL |
| Descripción | El script de Python del proceso ETL debe estar completamente documentado con comentarios en español que expliquen: (1) el propósito de cada función, (2) las expresiones regulares utilizadas, (3) las reglas de negocio aplicadas, (4) el orden de carga de las tablas. |
| Métrica | Porcentaje de líneas de código con comentarios útiles |
| Condición de aceptación | Mínimo 20% del código debe contener comentarios explicativos; todas las funciones deben tener docstring |
| Prioridad | Media |



| Atributo | Valor |
| --- | --- |
| Identificador | RNF06.1 |
| Nombre | Control de versiones |
| Descripción | El código fuente del proyecto (scripts Python, consultas SQL, documentación) debe mantenerse en un repositorio de control de versiones (Git) con commits semánticos y etiquetas por versión. |
| Condición de aceptación | Repositorio Git con historial de commits y etiquetas v1.0, v1.1, etc. |
| Prioridad | Baja |

RNF07: Confiabilidad

| Atributo | Valor |
| --- | --- |
| Identificador | RNF07 |
| Nombre | Calidad de datos en la tabla de hechos |
| Descripción | El proceso ETL debe garantizar que al menos el 95% de los registros extraídos de SUNAT sean válidos y se carguen correctamente en FACT_RENTABILIDAD. Los registros rechazados deben registrarse en el log con la causa del rechazo. |
| Métrica | (Registros cargados exitosamente / Registros extraídos totales) × 100 |
| Condición de aceptación | Tasa de éxito ≥ 95% en cada ejecución del ETL |
| Prioridad | Alta |

RNF08: Portabilidad

| Atributo | Valor |
| --- | --- |
| Identificador | RNF08 |
| Nombre | Independencia del motor de base de datos |
| Descripción | El script ETL debe ser compatible con al menos dos motores de base de datos: PostgreSQL. El código SQL debe evitar funciones específicas de un motor (ej. usar DATE estándar en lugar de GETDATE() o NOW()). |
| Métrica | Número de motores de base de datos soportados |
| Condición de aceptación | El script ETL funciona sin modificaciones en PostgreSQL |
| Prioridad | Baja |



### 3.5.3 Trazabilidad de Requerimientos

La siguiente tabla vincula cada requerimiento funcional con los stakeholders que lo solicitaron y los componentes técnicos involucrados:

| ID Requerimiento | Stakeholder solicitante | Componente técnico involucrado |
| --- | --- | --- |
| RF01 | Analista de BI | ETL (Extracción) |
| RF02 | Gerencia General | ETL (Transformación - Regex) |
| RF03 | Comercio Exterior | ETL (Transformación - Regex) |
| RF04 | Finanzas | ETL (Enriquecimiento) / DIM_FINANZAS |
| RF05 | Comercio Exterior | ETL (Enriquecimiento) / DIM_PAIS_TLC |
| RF06 | Finanzas | ETL (Enriquecimiento) / DIM_COSTO (SCD Tipo 2) |
| RF07 | Gerencia General / Finanzas | ETL + Power BI |
| RF08 | Todos los stakeholders | Power BI |
| RF09 | Gerencia General / Comercio Exterior | DIM_PAIS_TLC + Power BI |
| RF10 | Analista de BI | ETL (Logging) |


# 4. DISEÑO DE ARQUITECTURA DE INTELIGENCIA DE NEGOCIOS


## 4.1 Tipo de Arquitectura Propuesta

La arquitectura de Inteligencia de Negocios seleccionada es una arquitectura bottom-up (ascendente) basada en un Data Mart independiente, estructurada bajo un modelo dimensional tipo Copo de Nieve (Snowflake Schema). El esquema Copo de Nieve es una evolución del esquema Estrella, donde las dimensiones se normalizan en subdimensiones para reducir redundancia. En este proyecto, la normalización responde a la necesidad de:
Normalizar las jerarquías de las nuevas dimensiones (comerciales y financieras)
Evitar redundancias
Permitir un análisis más granular de la rentabilidad

| Característica | Descripción |
| --- | --- |
| Alcance | Centrada exclusivamente en el análisis de rentabilidad potencial de la palta Hass |
| Fuentes de datos | Procesa microdatos de exportación de ADUANET (período 2016-2024) y fuentes externas complementarias (BCRP, MINCETUR, MIDAGRI/Sierra Exportadora) |
| Modelo de datos | Esquema Copo de Nieve con subdimensiones normalizadas (DIM_PAIS_TLC, DIM_VARIEDAD_CALIDAD) |
| Salidas | Genera información para la toma de decisiones estratégicas de Peruvian Andean Trout S.A.C. |

KPIs que se calculan en la arquitectura:

| KPI | Descripción |
| --- | --- |
| Precio FOB/kg | Precio promedio por kilogramo exportado |
| Margen de Utilidad Estimado | Diferencia entre ingreso FOB y costo estimado |
| Ratio de Rentabilidad | Porcentaje de ganancia sobre el ingreso |
| Índice de Concentración (HHI) | Concentración de exportadores en el mercado |
| Margen Neto Ajustado | Rentabilidad considerando tipo de cambio y aranceles |



## 4.2 Justificación de la Arquitectura

La arquitectura seleccionada responde a las siguientes razones:

| Criterio | Justificación |
| --- | --- |
| Alcance acotado | El proyecto analiza un solo producto (palta Hass) con fuentes de datos específicas, por lo que un Data Mart independiente es suficiente. |
| Tiempo y recursos | La arquitectura bottom-up permite obtener resultados rápidos sin necesidad de implementar un Data Warehouse corporativo completo. |
| Flexibilidad | Permite incorporar nuevas fuentes de datos (BCRP, MINCETUR, Sierra Exportadora) de manera incremental. |
| Rendimiento | El esquema Copo de Nieve optimiza las consultas de los KPIs definidos (precio, margen, ratio, concentración) al precalcular las métricas derivadas en la tabla de hechos. |
| Escalabilidad | A futuro, el Data Mart puede integrarse a un Data Warehouse empresarial si la empresa decide expandir la solución a otros productos o mercados. |
| Normalización (Copo de Nieve) | La evolución al modelo Copo de Nieve permite normalizar las jerarquías de las dimensiones (TLC por país, atributos de calidad por producto), evitando redundancias y facilitando el mantenimiento. |
| Inteligencia competitiva | La inclusión de DIM_EXPORTADOR permite analizar la concentración del mercado (índice HHI) y el posicionamiento frente a la competencia. |
| Análisis financiero realista | La integración de BCRP (tipo de cambio) y MINCETUR (aranceles) permite ajustar los márgenes de rentabilidad a condiciones económicas reales, superando la limitación de los datos brutos de SUNAT. |

Casos de uso del sistema BI:

| Actor | Caso de uso | Descripción |
| --- | --- | --- |
| Gerencia General | Visualizar rentabilidad potencial | Acceder al dashboard con KPIs clave (margen, ratio, rentabilidad por destino) |
| Planeamiento Estratégico | Identificar mejores mercados | Filtrar por país destino y continente para ver precios FOB/kg y rentabilidad ajustada por aranceles. |
| Comercio Exterior | Análisis de competencia y logística | Identificar principales exportadores (competidores) y aduanas de salida más eficientes. |
| Finanzas | Evaluar concentración de riesgo | Revisar índice de concentración por destino y analizar el impacto del tipo de cambio en los márgenes. |

Detección de cuellos de botella:

| Cuello de botella | Descripción | Solución propuesta |
| --- | --- | --- |
| Descarga manual de ADUANET | Los archivos DBF/TXT requieren descarga manual | Automatizar extracción vía script programado en Python. |
| Limpieza de datos | Registros duplicados, valores nulos en FOB, y textos no estructurados en DESC_ADIC. | Implementar validaciones en fase de transformación y usar Regex para extraer atributos (variedad, calidad). |
| Filtro de producto | Inclusión de otras variedades, pulpa o productos procesados que distorsionan el precio promedio. | Implementar filtro obligatorio para seleccionar solo registros con "HASS" en DESC_ADIC o DESC_COM. |
| Estimación de costos | Datos SUNAT sin costos reales de producción, empaque o logística. | Usar valores de referencia documentados desde Sierra Exportadora y MINCETUR |
| Enriquecimiento externo | Falta de tipo de cambio y aranceles para ajustar la rentabilidad real. | Integrar API/CSV de BCRP (tipo de cambio) y tablas de MINCETUR (aranceles por país). |


## 4.3 Componentes de la Arquitectura

La arquitectura se compone de los siguientes elementos distribuidos en 4 capas:
Capa 1: Fuentes de datos

| Componente | Descripción | Formato |
| --- | --- | --- |
| ADUANET (SUNAT) | Microdatos de exportación de palta Hass (partida 0804400000). | DBF / TXT |
| BCRP (referencial) | Serie histórica de tipo de cambio (USD/PEN) para ajuste de rentabilidad. | CSV / API |
| Sierra Exportadora | Costos de referencia (producción, empaque, logística) y márgenes estándar del sector. | PDF / Excel |
| MINCETUR (referencial) | Aranceles aplicables por país destino, acuerdos TLC, información de puertos. | CSV / Excel |

Capa 2: Procesos ETL

| Componente | Tecnología | Función |
| --- | --- | --- |
| Extracción | Python (pandas, dbfread) | Leer archivos DBF/TXT desde ADUANET y fuentes externas. |
| Transformación | Python (pandas, numpy, re) | • Limpiar datos (eliminar duplicados, valores nulos). <br> • Filtrar exclusivamente variedad HASS (mediante Regex en DESC_ADIC/DESC_COM). <br> • Enriquecer con tipo de cambio (BCRP) y aranceles (MINCETUR). <br> • Extraer atributos para subdimensiones (variedad, calidad, método orgánico). <br> • Calcular KPIs: Precio_FOB_kg (en Power BI), Costo_Total_Estimado (mediante lookup a DIM_COSTO SCD Tipo 2), Margen_Utilidad y Ratio_Rentabilidad (calculados dinámicamente en Power BI). |
| Carga | Python (SQLAlchemy, psycopg2) | Insertar datos en FACT_RENTABILIDAD y tablas de dimensiones (orden: primero dimensiones, luego hechos). |

Capa 3: Almacenamiento analítico (Data Mart)

| Componente | Descripción |
| --- | --- |
| Motor de base de datos | PostgreSQL (local) |
| Tabla de hechos | FACT_RENTABILIDAD |
| Tablas de dimensiones principales | DIM_TIEMPO, DIM_UBICACION, DIM_PRODUCTO, DIM_VARIEDAD_CALIDAD, DIM_EXPORTADOR, DIM_ADUANA, DIM_FINANZAS, DIM_COSTO |
| Subdimensiones (normalización Copo de Nieve) | DIM_PAIS_TLC (conectada a DIM_UBICACION) |

Nota importante: DIM_VARIEDAD_CALIDAD es una dimensión independiente, no una subdimensión de DIM_PRODUCTO. Su clave foránea (FK) está directamente en FACT_RENTABILIDAD.
Capa 4: Visualización y análisis

| Componente | Tecnología | Función |
| --- | --- | --- |
| Dashboard | Power BI | Visualización de KPIs, mapas, tendencias temporales |
| Reportes | Power BI (exportable a PDF) | Reportes ejecutivos de rentabilidad |

Jerarquías de datos implementadas:

| Dimensión | Jerarquía |
| --- | --- |
| DIM_TIEMPO | Año → Trimestre → Mes → Semana → Fecha |
| DIM_UBICACION | Continente → País |
| DIM_PRODUCTO | Partida arancelaria → Variedad (Hass) |
| DIM_PAIS_TLC (subdimensión) | País → Acuerdo TLC → Arancel aplicable |
| DIM_VARIEDAD_CALIDAD (dimensión independiente) | Variedad → Categoría de calidad → Método de producción |

Granularidad del modelo:

| Nivel | Granularidad | Descripción |
| --- | --- | --- |
| Fina | Por ítem de declaración (cada línea de producto) | Registro individual de exportación (DUA). Permite análisis por competidor (DIM_EXPORTADOR). |
| Media | Por mes y destino | Agregación de precios y volúmenes por país y mes. |
| Gruesa | Por año y continente | Tendencia anual de rentabilidad por región geográfica. |


## 4.4 Diagrama de Arquitectura



## 4.5 Arquitectura Escalable a Big Data

La ingesta de la totalidad de exportaciones peruanas desde SUNAT cumple con las 3 V's del Big Data:

| V de Big Data | Descripción | Implicancia en el proyecto |
| --- | --- | --- |
| Volumen | Archivos masivos que superan la memoria RAM en procesamiento paralelo | El Data Mart actual maneja solo palta Hass (~100,000 registros). Escalar a todas las partidas requeriría procesamiento distribuido |
| Velocidad | Miles de DUAs generadas diariamente | El procesamiento por lotes (batch) mensual sería insuficiente; se requeriría procesamiento en tiempo real (streaming) |
| Variedad | Textos desestructurados en descripciones aduaneras | La actual extracción con Regex para una partida específica sería insuficiente para cientos de partidas con distintas estructuras de texto |

Estrategia de escalabilidad propuesta:

Para absorber este volumen en el futuro, la arquitectura migraría de PostgreSQL hacia:


| Componente actual | Escalamiento a Big Data |
| --- | --- |
| Base de datos | PostgreSQL → Cloud Data Warehouse (AWS Redshift / Google BigQuery) |
| Procesamiento ETL | Python local → Procesamiento distribuido (Apache Spark) |
| Almacenamiento | Disco local → Almacenamiento en la nube (AWS S3 / Google Cloud Storage) |
| Orquestación | Scripts manuales → Orquestador de workflows (Apache Airflow / Prefect) |

Nota: Esta escalabilidad es una visión de futuro y no forma parte del alcance actual del proyecto, que se centra exclusivamente en el análisis de la palta Hass.

# 5. MODELAMIENTO DIMENSIONAL


## 5.1 Tabla de Hechos: FACT_RENTABILIDAD

La tabla de hechos FACT_RENTABILIDAD es el centro del modelo. Almacena métricas cuantitativas (medidas) que representan eventos de negocio ocurridos en un punto específico del tiempo. En este proyecto, la tabla de hechos FACT_RENTABILIDAD almacena las métricas cuantitativas asociadas a cada operación de exportación de palta Hass.

| Concepto | Valor |
| --- | --- |
| Granularidad | Fina, correspondiendo a cada ítem o línea de producto dentro de una Declaración Única de Aduanas (DUA) |
| Principio de diseño | Solo se almacenan hechos atómicos e inmutables (Valor_FOB, Volumen_Exportado). Las métricas derivadas (Precio_Promedio_kg, Margen_Utilidad, Ratio_Rentabilidad) se calculan en tiempo de consulta (vistas o Power BI) para garantizar consistencia ante actualizaciones de costos de referencia |

Estructura de la tabla de hechos

| Campo | Tipo de dato | Descripción | Fuente / Cálculo |
| --- | --- | --- | --- |
| ID_Rentabilidad (PK) | INTEGER | Identificador único de cada registro | Autogenerado (SERIAL) |
| FK_Tiempo | INTEGER | Llave foránea a DIM_TIEMPO | Asignación desde FECHA (SUNAT) |
| FK_Ubicacion | INTEGER | Llave foránea a DIM_UBICACION. | Asignación desde CPAIS/PAIS_DESC (SUNAT) |
| FK_Producto | INTEGER | Llave foránea a DIM_PRODUCTO. | Asignación desde CNAN (SUNAT) |
| FK_Variedad_Calidad | INTEGER | Llave foránea a DIM_VARIEDAD_CALIDAD | Asignación desde extracción Regex en DESC_ADIC |
| FK_Exportador | INTEGER | Llave foránea a DIM_EXPORTADOR | Asignación desde NRO_DOCU/EXPORTADOR (SUNAT) |
| FK_Aduana | INTEGER | Llave foránea a DIM_ADUANA | Asignación desde CADUANA/ADUA_DESC (SUNAT) |
| FK_Finanzas | INTEGER | Llave foránea a DIM_FINANZAS | Asignación por fecha y país (BCRP + MINCETUR) |
| FK_Costo | INTEGER | Llave foránea a DIM_COSTO (SCD Tipo 2) | Asignación por fecha y región destino |
| Valor_FOB | DECIMAL(18,2) | Valor FOB en dólares estadounidenses | Campo FOB_DOLPOL (SUNAT) |
| Volumen_Exportado | DECIMAL(18,2) | Peso neto en kilogramos | Campo PESO_NETO (SUNAT) |
| NRO_DOCU | VARCHAR(20) | Número de Declaración Única de Aduanas (DUA) | Degenerate dimension |
| ITEM | INTEGER | Número de línea dentro de la DUA | Degenerate dimension |

Nota sobre degenerate dimensions: Las columnas `NRO_DOCU` e `ITEM` no son llaves foráneas ni medidas. Son atributos descriptivos de la transacción que permiten preservar la granularidad original de los datos de SUNAT (nivel DUA + línea de producto). Según Kimball (2013), estos identificadores transaccionales se almacenan directamente en la tabla de hechos como degenerate dimensions cuando no tienen atributos adicionales que justifiquen una tabla de dimensión separada.
Resumen de llaves y medidas:

| Tipo | Elementos |
| --- | --- |
| Llave primaria (PK) | ID_Rentabilidad |
| Llaves foráneas (FK) | FK_Tiempo, FK_Ubicacion, FK_Producto, FK_Variedad_Calidad, FK_Exportador, FK_Aduana, FK_Finanzas, FK_Costo |
| Medidas | Valor_FOB, Volumen_Exportado |

Nota sobre las claves foráneas: Todas las dimensiones (TIEMPO, UBICACION, PRODUCTO, VARIEDAD_CALIDAD, EXPORTADOR, ADUANA, FINANZAS, COSTO) se relacionan mediante FK directas, garantizando integridad referencial y cumpliendo con el modelo Snowflake.

## 5.2 Tablas de Dimensiones

Las tablas de dimensiones proporcionan el contexto descriptivo para segmentar y filtrar los análisis. En el modelo de Copo de Nieve, algunas dimensiones se han normalizado en subdimensiones para evitar redundancias.
DIM_TIEMPO
Permite el análisis temporal de la rentabilidad, con jerarquías que van desde el año hasta el día.

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Tiempo (PK) | INTEGER | Identificador único de la fecha. | 20240629 |
| Fecha | DATE | Fecha completa de embarque | 2024-06-29 |
| Año | INTEGER | Año de la exportación | 2024 |
| Trimestre | INTEGER | Trimestre del año (1-4) | 2 |
| Mes | INTEGER | Número de mes (1-12) | 6 |
| Mes_Nombre | VARCHAR(20) | Nombre del mes | Junio |
| Semana_Año | INTEGER | Semana del año (1-52). | 26 |

Jerarquía temporal: Año → Trimestre → Mes → Semana → Fecha
DIM_UBICACION
Permite el análisis por mercado de destino. Se ha normalizado para separar la información geográfica base de los acuerdos comerciales.

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Ubicacion (PK) | INTEGER | Identificador único del país | 1 |
| Pais_Codigo | VARCHAR(3) | Código de país (CPAIS) | CA |
| Pais_Nombre | VARCHAR(100) | Nombre del país destino | Canadá |
| Continente | VARCHAR(50) | Continente al que pertenece | América del Norte |

Jerarquía geográfica: Continente → País
Subdimensión: DIM_PAIS_TLC (se relaciona 1:1 con DIM_UBICACION)

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Pais_TLC (PK) | INTEGER | Identificador único del acuerdo | 1 |
| FK_Ubicacion | INTEGER | Llave foránea a DIM_UBICACION | 1 |
| Acuerdo_TLC | VARCHAR(100) | Tratado de Libre Comercio vigente | TLC Perú-Canadá |
| Arancel_Porcentaje | DECIMAL(5,2) | Arancel aplicable | 0.00 |
| Categoria_Mercado | VARCHAR(20) | Clasificación (Premium/Estándar) | Premium |

DIM_PRODUCTO
Contiene la información específica del producto analizado: palta Hass.

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Producto (PK) | INTEGER | Identificador único del producto | 1 |
| Partida_Arancelaria | VARCHAR(10) | Código de partida (CNAN). | 0804400000 |
| Descripcion | VARCHAR(200) | Descripción comercial oficial. | AGUACATES (PALTAS) FRESCOS O SECOS |

DIM_VARIEDAD_CALIDAD

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Variedad_Calidad (PK) | INTEGER | Identificador único del producto | 1 |
| Variedad | VARCHAR(50) | Variedad del producto. | Hass |
| Categoria_Calidad | VARCHAR(20) | Categoría de calidad (CAT 1, CAT 2, etc.). | CAT 1 |
| Metodo_Produccion | VARCHAR(30) | Orgánico o Convencional. | Convencional |
| Fuente_Extraccion | VARCHAR(100) | Campo SUNAT de origen (DESC_ADIC / DESC_COM). | DESC_ADIC |

Jerarquía: Variedad → Categoria_Calidad → Metodo_Produccion
DIM_EXPORTADOR
Identifica a los actores del mercado (competidores) que participan en la exportación de palta Hass.

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Exportador (PK) | INTEGER | Identificador único del exportador. | 1 |
| RUC | VARCHAR(11) | Número de RUC de la empresa. | 20535674010 |
| Razon_Social | VARCHAR(200) | Razón social del exportador. | SIEMBRA ALTA S.A.C. |
| Tipo_Empresa | VARCHAR(50) | Clasificación (Gran, MYPE, etc.). | S.A.C. |

DIM_ADUANA
Describe los puntos de salida (aduanas y puertos) de las exportaciones.

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Aduana (PK) | INTEGER | Identificador único de la aduana. | 1 |
| Codigo_Aduana | VARCHAR(10) | Código oficial de la aduana. | 046 |
| Nombre_Aduana | VARCHAR(100) | Descripción o nombre de la aduana. | PAITA |
| Region | VARCHAR(50) | Región donde se ubica la aduana. | Piura |
| Tipo_Aduana | VARCHAR(30) | Marítima, Terrestre, etc. | MARITIMA |

DIM_FINANZAS
Esta dimensión integra los datos económicos externos que afectan la rentabilidad neta: tipo de cambio (USD/PEN) y aranceles de importación por país destino.

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Finanzas (PK) | INTEGER | Identificador único | 1 |
| Fecha_Referencia | DATE | Fecha del tipo de cambio | 2024-06-01 |
| FK_Ubicacion | INTEGER | Llave foránea a DIM_UBICACION | 1 |
| Tipo_Cambio_USD_PEN | DECIMAL(10,4) | Tipo de cambio promedio (BCRP) | 3.75 |
| Arancel_Porcentaje | DECIMAL(5,2) | Arancel aplicable (MINCETUR) | 0.00 |
| Acuerdo_TLC | VARCHAR(100) | Tratado de libre comercio vigente | TLC Perú-Estados Unidos |
| Fuente_BCRP | VARCHAR(50) | Fecha de extracción del dato | 2024-04-15 |
| Fuente_MINCETUR | VARCHAR(50) | Versión del arancel | 2024-01-01 |

DIM_COSTO (SCD Tipo 2 - Slowly Changing Dimension)
A diferencia de una tabla de parámetros externa, DIM_COSTO se implementa como una dimensión tradicional con SCD Tipo 2 y FK directa desde FACT_RENTABILIDAD. Esto permite que cada transacción de exportación esté vinculada a los costos de referencia vigentes en su momento histórico. Estructura los costos estimados por tipo, permitiendo calcular el costo total por operación de exportación. Utiliza una estrategia SCD Tipo 2 para mantener el historial de cambios en los costos de producción, empaque y logística.

| Campo | Tipo de dato | Descripción | Ejemplo |
| --- | --- | --- | --- |
| ID_Costo (PK) | INTEGER | Identificador único del tipo de costo | 1 |
| Tipo_Costo | VARCHAR(50) | Producción / Empaque / Logístico | Logístico |
| Region_Destino | VARCHAR(50) | América / Europa / Asia | Europa |
| Valor_Unitario_USD | DECIMAL(18,4) | Costo estimado por kg (USD) | 0.35 |
| Fecha_Vigencia_Inicio | DATE | Desde cuándo aplica este costo | 2020-01-01 |
| Fecha_Vigencia_Fin | DATE | Hasta cuándo aplica (NULL = vigente) | NULL |
| Es_Vigente | BOOLEAN | TRUE si es el registro activo | TRUE |

Ejemplo de registros en DIM_COSTO (SCD Tipo 2):

| ID_Costo | Tipo_Costo | Region_Destino | Valor_Unitario_USD | Fecha_Vigencia_Inicio | Fecha_Vigencia_Fin | Es_Vigente |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Producción | Global | 0.45 | 2016-01-01 | 2022-12-31 | FALSE |
| 2 | Producción | Global | 0.52 | 2023-01-01 | NULL | TRUE |
| 3 | Logístico | Europa | 0.35 | 2016-01-01 | NULL | TRUE |
| 4 | Logístico | Asia | 0.50 | 2016-01-01 | NULL | TRUE |
| 5 | Logístico | América | 0.25 | 2016-01-01 | NULL | TRUE |
| 6 | Empaque | Global | 0.15 | 2016-01-01 | NULL | TRUE |


## 5.3 Relaciones entre Tablas y Diagrama del Modelo

El modelo implementado es un esquema de Copo de Nieve (Snowflake Schema). Esta evolución respecto al esquema Estrella original responde a la necesidad de normalizar las jerarquías de las nuevas dimensiones (comercialización y financiera), evitar redundancias y permitir un análisis más granular de la rentabilidad.
Esquema estrella original

Estructura de relaciones

Resumen de dimensiones implementadas

| N° | Dimensión | Tipo | ¿Normalizada? |
| --- | --- | --- | --- |
| 1 | DIM_TIEMPO | Principal | No |
| 2 | DIM_UBICACION | Principal | Sí (hacia DIM_PAIS_TLC) |
| 3 | DIM_PAIS_TLC | Subdimensión | N/A (hijo de UBICACION) |
| 4 | DIM_PRODUCTO | Principal | No |
| 5 | DIM_VARIEDAD_CALIDAD | Independiente | No |
| 6 | DIM_EXPORTADOR | Principal | No |
| 7 | DIM_ADUANA | Principal | No |
| 8 | DIM_FINANZAS | Principal (nueva) | No |
| 9 | DIM_COSTO | Principal (SCD Tipo 2) | No |

Métricas derivadas (NO almacenadas en FACT_RENTABILIDAD)
Estas métricas se calculan en la capa de visualización (Power BI) mediante medidas DAX, o en vistas materializadas del Data Mart:

| Métrica | Fórmula |
| --- | --- |
| Precio_Promedio_kg | Valor_FOB / Volumen_Exportado |
| Margen_Utilidad | Valor_FOB - (Costo_Total_según_DIM_COSTO) |
| Ratio_Rentabilidad | (Margen_Utilidad / Valor_FOB) × 100 |


## 5.4 Diagrama del Modelo Dimensional



## 5.5 Gobierno de Datos y Diccionario de Metadata

Se documenta la metadata separando la regla de negocio (Significado) de su implementación técnica (Cálculo).

| Campo / KPI | Metadata de Negocio | Metadata Técnica |
| --- | --- | --- |
| Variedad Hass | Palta comercializada fresca, excluyendo procesados | Extraído de texto aplicando filtro Regex: r'\bHASS?\b' (excluye "PULPA", "CONGELADO", "PROCESAMIENTO") |
| Precio FOB/kg | Precio promedio en dólares por kilo exportado | DECIMAL(18,2). Cálculo DAX: DIVIDE(SUM(Valor_FOB), SUM(Volumen_Exportado)) |
| Margen Neto Ajustado | Ganancia real líquida considerando tipo de cambio y aranceles | KPI derivado: (Valor_FOB × TC) - (Costo_Total × TC) - Arancel |
| Margen de Utilidad | Diferencia entre ingreso FOB y costo estimado | Valor_FOB - (Costo_Total_según_DIM_COSTO) |
| Ratio de Rentabilidad | Porcentaje del ingreso que representa la utilidad | (Margen_Utilidad / Valor_FOB) × 100 |
| Índice HHI | Concentración de exportadores en el mercado | Σ(FOB_exportador / FOB_total)² (calculado en DAX) |
| Índice de Concentración por Destino | Porcentaje de FOB concentrado en un país | (FOB_país / FOB_total) × 100 |


# 6. PROCESOS ETL


## 6.1 Entorno de Desarrollo (IDE)

Para el presente proyecto, se seleccionó Visual Studio Code (VS Code) como IDE principal.

### 6.1.1 IDE Seleccionado


| Atributo | Valor |
| --- | --- |
| Nombre | Visual Studio Code (VS Code) |
| Versión | 1.85 o superior |
| Desarrollador | Microsoft |
| Licencia | Gratuita (Open Source) |
| Sitio oficial | https://code.visualstudio.com |


### 6.1.2 Justificación de la Elección

La selección de Visual Studio Code se basa en los siguientes criterios técnicos y prácticos:

| Criterio | Justificación | ¿Cómo aplica al proyecto? |
| --- | --- | --- |
| Soporte nativo para Python | VS Code tiene integración oficial con Python mediante la extensión de Microsoft, que incluye linting, autocompletado, formateo y depuración paso a paso. | El ETL está completamente programado en Python con librerías pandas, dbfread, re, sqlalchemy. La depuración paso a paso fue esencial para validar las expresiones regulares (Regex) y las transformaciones de datos. |
| Ligereza y rendimiento | VS Code consume menos memoria RAM que otros IDEs como PyCharm (aproximadamente 300-500 MB vs 1-2 GB). | El equipo de desarrollo utilizó computadoras con recursos limitados (8 GB RAM). La ligereza de VS Code permitió ejecutar el ETL y las pruebas sin afectar el rendimiento del sistema. |
| Integración con Git | VS Code incluye control de versiones integrado (Git) con interfaz gráfica para commits, branches y resolución de conflictos. | El proyecto requirió control de versiones para mantener el historial del script ETL, las consultas SQL y la documentación. Se utilizaron commits semánticos y etiquetas (v1.0, v1.1). |
| Terminal integrada | VS Code permite ejecutar comandos directamente dentro del IDE, sin necesidad de ventanas externas. | Se utilizó la terminal integrada para ejecutar el script ETL, instalar librerías (pip install pandas dbfread sqlalchemy psycopg2) y ejecutar consultas SQL de validación. |
| Extensiones especializadas | VS Code cuenta con un amplio marketplace de extensiones gratuitas. | Se instalaron extensiones específicas para el proyecto (ver tabla en 6.1.3). |
| Multiplataforma | VS Code funciona en Windows, Linux y macOS. | El equipo de desarrollo utilizó Windows 10/11, mientras que el servidor de base de datos fue PostgreSQL en Linux (Ubuntu). VS Code funcionó consistentemente en ambos entornos. |
| Jupyter Notebooks integrados | VS Code permite ejecutar celdas de código interactivas similares a Jupyter Notebooks. | Se utilizaron notebooks interactivos para explorar los datos crudos de SUNAT, probar expresiones regulares (Regex) y validar transformaciones antes de integrarlas al script ETL final. |
| Depuración de SQL | VS Code tiene extensiones para conectarse a bases de datos y ejecutar consultas SQL con resaltado de sintaxis. | Se utilizó la extensión "PostgreSQL" para ejecutar consultas de validación directamente desde el IDE. |


### 6.1.3 Extensiones Instaladas en VS Code


| Extensión | Propósito en el proyecto |
| --- | --- |
| Python (Microsoft) | Linting, autocompletado, formateo (Black), depuración paso a paso, ejecución de pruebas unitarias. |
| Pylance (Microsoft) | Servidor de lenguaje Python para análisis de tipos y autocompletado avanzado. |
| Jupyter (Microsoft) | Ejecución de notebooks interactivos para exploración de datos y pruebas de Regex. |
| Excel Viewer | Visualización de archivos Excel de costos referenciales y aranceles dentro del IDE. |
| PostgreSQL (Chris Kolkman) | Conexión a la base de datos PostgreSQL, ejecución de consultas SQL, visualización de tablas y esquemas. |
| GitLens | Visualización avanzada del historial de Git (autores, fechas, comparación de versiones). |
| Better Comments | Resaltado de comentarios en el código por categoría (TODO, FIXME, IMPORTANTE). |
| Regex Previewer | Visualización en tiempo real de las expresiones regulares aplicadas a texto de ejemplo (útil para validar filtros de "HASS" y exclusión de "PULPA", "CONGELADO"). |


### 6.1.4 Configuración del Entorno de Desarrollo

A continuación, se detalla la configuración específica utilizada para el proyecto:
Configuración del intérprete de Python

| Parámetro | Valor |
| --- | --- |
| Versión de Python | 3.9 o superior |
| Entorno virtual | venv (creado con python -m venv etl_env) |
| Archivo de requerimientos | requirements.txt con las librerías: pandas, dbfread, numpy, sqlalchemy, psycopg2-binary, openpyxl, python-dotenv |

Configuración del depurador (launch.json)


| {     "version": "0.2.0",     "configurations": [         {             "name": "Python: ETL Principal",             "type": "python",             "request": "launch",             "program": "${workspaceFolder}/etl_main.py",             "console": "integratedTerminal",             "env": {                 "PYTHONPATH": "${workspaceFolder}"             },             "args": ["--year", "2024", "--test-mode"]         }     ] } |
| --- |


Configuración de variables de entorno (.env)


| # Conexión a base de datos DB_HOST=localhost DB_PORT=5432 DB_NAME=datamart_palta DB_USER=etl_user DB_PASSWORD=******  # Rutas de archivos SUNAT_DATA_PATH=C:/data/sunat/ BCRP_FILE_PATH=C:/data/bcrp/tipo_cambio.csv MINCETUR_FILE_PATH=C:/data/mincetur/aranceles.xlsx COSTOS_FILE_PATH=C:/data/costos/dim_costo.csv |
| --- |


### 6.1.5 Alternativas Evaluadas

Antes de seleccionar VS Code, se evaluaron las siguientes alternativas:

| Criterio | VS Code | PyCharm (Community) | Jupyter Notebook | Sublime Text |
| --- | --- | --- | --- | --- |
| Precio | Gratuito | Gratuito (Community) | Gratuito | Shareware (USD 99) |
| Consumo de RAM | ~300-500 MB | ~1-2 GB | ~500-800 MB | ~150-300 MB |
| Depuración paso a paso | Sí | Sí | Limitada | No |
| Integración con Git | Sí (nativa) | Sí (nativa) | Limitada | Con plugin |
| Terminal integrada | Sí | Sí | No | No |
| Extensiones para SQL | Sí (PostgreSQL) | Sí (Database Tools) | No | No |
| Soporte para Jupyter | Sí (nativo) | Sí (requiere versión Professional) | Sí (nativo) | No |
| Curva de aprendizaje | Baja | Media | Baja | Media |
| Rendimiento con archivos grandes (100k+ registros) | Bueno | Bueno | Lento | Bueno |

Decisión final: Se eligió VS Code porque ofrece el mejor equilibrio entre funcionalidad, rendimiento y costo cero, cubriendo todas las necesidades del proyecto: depuración de Python, control de versiones, conexión a bases de datos y ejecución de notebooks interactivos para pruebas de Regex.

### 6.1.6 Evidencia de uso en el proyecto


| Fase del proyecto | Uso de VS Code | Herramienta/Extensión utilizada |
| --- | --- | --- |
| Exploración de datos | Análisis exploratorio de datos (EDA) de SUNAT y BCRP | Jupyter Notebook + Python (pandas) |
| Desarrollo de Regex | Validación de expresiones regulares para filtrar "HASS" | Regex Previewer + Python (re module) |
| Programación ETL | Escritura y depuración del script principal (etl_main.py) | Python extension + Depurador paso a paso |
| Pruebas unitarias | Validación de funciones de transformación | Python testing (pytest) |
| Control de versiones | Commits, branches, etiquetas | Git integrado + GitLens |
| Carga de datos | Ejecución del ETL y monitoreo de logs | Terminal integrada |
| Validación de integridad | Ejecución de consultas SQL de verificación | PostgreSQL extension |



## 6.2 Fase de Extracción

Se implementará un proceso automatizado desarrollado en Python (utilizando las librerías pandas, dbfread y sqlalchemy) encargado de la descarga, integración y consolidación de los microdatos de exportación provenientes de ADUANET, así como de fuentes externas complementarias (BCRP, MINCETUR, Sierra Exportadora).
Fuente de datos:

| Fuente | Datos extraídos | Formato | Periodicidad |
| --- | --- | --- | --- |
| SUNAT (ADUANET) | Microdatos de exportación de palta Hass (partida 0804400000) | DBF / TXT | Mensual (descarga manual programada) |
| BCRP | Tipo de cambio promedio (USD/PEN) para el período 2016-2024 | CSV / API | Extracción única (histórica) |
| MINCETUR | Aranceles aplicables por país destino y acuerdos TLC | CSV / Excel | Extracción única con actualizaciones anuales |
| Sierra Exportadora | Costos de referencia (producción, empaque, logística) | PDF / Excel | Extracción única (referencial) |

Variables extraídas desde SUNAT:

| Variable | Campo en ADUANET | Uso en el Data Mart |
| --- | --- | --- |
| Fecha de embarque | FECHA | DIM_TIEMPO |
| País destino | CPAIS, PAIS_DESC | DIM_UBICACION |
| Partida arancelaria | CNAN | DIM_PRODUCTO (filtro para Hass) |
| Valor FOB | FOB_DOLPOL | FACT_RENTABILIDAD.Valor_FOB |
| Peso neto | PESO_NETO | FACT_RENTABILIDAD.Volumen_Exportado |
| Exportador (RUC y razón social) | NRO_DOCU, EXPORTADOR | DIM_EXPORTADOR |
| Aduana de salida | CADUANA, ADUA_DESC | DIM_ADUANA |
| Descripción adicional | DESC_ADIC, DESC_COM | DIM_VARIEDAD_CALIDAD (extracción de atributos) |

Nota: El campo EXPORTADOR se extrae como identificador del competidor. No se incorpora como cliente final porque SUNAT no registra al importador.
Problemas identificados en la fuente:

| Problema | Descripción | Solución en ETL |
| --- | --- | --- |
| Inconsistencias en países | Abreviaturas, faltas ortográficas, códigos no mapeados | Normalización mediante diccionario de mapeo |
| Formatos de fecha | Fecha en AAAAMMDD | Estandarización a DATE y extracción de Año, Mes, Trimestre, Semana |
| Valores nulos o incompletos | Especialmente en campos opcionales | Registros con FOB o PESO_NETO nulos son excluidos |
| Registros duplicados | Misma DUA repetida | Eliminación basada en NRO_DOCU + FECHA + CNAN |
| Texto no estructurado | Variedad y calidad incrustados en DESC_ADIC | Extracción con Regex (expresiones regulares) |


## 6.3 Fase de Transformación

La fase de transformación tiene como objetivo asegurar la calidad, consistencia y estructura de los datos, mediante su limpieza, estandarización, integración y adecuación al modelo dimensional de Copo de Nieve.
Subproceso 1: Limpieza y Validación de Datos SUNAT

| Operación | Descripción |
| --- | --- |
| Deduplicación | Basada en NRO_DOCU + FECHA + CNAN + ITEM + PESO_NETO. La inclusión de ITEM (número de ítem dentro de la DUA) y PESO_NETO evita la pérdida de registros cuando una misma declaración contiene múltiples líneas con la misma partida arancelaria |
| Normalización de texto | Los campos DESC_ADIC y DESC_COM se convierten a mayúsculas (upper()) |
| Filtro positivo | Se retienen registros donde la expresión regular r'\bHASS?\b' aparece en al menos un campo |
| Filtro negativo | Se excluyen registros que contengan PULPA, TROZOS, CONGELADO o PROCESAMIENTO |
| Validación de valores | Se excluyen registros con FOB_DOLPOL o PESO_NETO nulos, y se verifica FOB_DOLPOL > 0 y PESO_NETO > 0 |

Subproceso 2: Estandarización y Normalización

| Operación | Descripción |
| --- | --- |
| Homogeneización de moneda | Todos los valores convertidos a USD |
| Homogeneización de unidades | Consistente en kilogramos |
| Normalización de países | Mediante diccionario de mapeo. El continente se añade externamente |
| Limpieza de exportadores | EXPORTADOR = EXPORTADOR.upper().replace(' S.A.C.', '').replace(' S.A.', '') |
| Extracción de atributos | Variedad, calidad y método orgánico desde DESC_ADIC usando Regex |

Subproceso 3: Enriquecimiento con Fuentes Externas

| Fuente | Datos incorporados | Método de integración |
| --- | --- | --- |
| BCRP | Tipo de cambio (USD/PEN) por fecha | merge por fecha entre DIM_TIEMPO y serie BCRP |
| MINCETUR | Acuerdo TLC y arancel por país | merge por PAIS_DESC entre DIM_UBICACION y tabla de aranceles |
| MIDAGRI / Sierra Exportadora | Costo de producción, empaque, logístico por región | Carga directa a DIM_COSTO como dimensión SCD Tipo 2 con FK directa desde FACT_RENTABILIDAD |
| Integración de DIM_FINANZAS | Tipo de cambio + aranceles por fecha y país | merge por fecha entre DIM_TIEMPO y BCRP, y por país entre DIM_UBICACION y MINCETUR |

Subproceso 4: Cálculo de Indicadores

| Indicador | Fórmula | Destino |
| --- | --- | --- |
| Precio_Promedio_kg | FOB_DOLPOL / PESO_NETO | Se calcula en Power BI (no se almacena en FACT_RENTABILIDAD) |
| Costo_Total_Estimado | Σ(Valor_unitario_DIM_COSTO × Volumen_Exportado) | Power BI (mediante lookup a DIM_COSTO vigente) |
| Margen_Utilidad | FOB_DOLPOL - Costo_Total_Estimado | Se calcula en Power BI (no se almacena en FACT_RENTABILIDAD) |
| Ratio_Rentabilidad | (Margen_Utilidad / FOB_DOLPOL) × 100 | Se calcula en Power BI (no se almacena en FACT_RENTABILIDAD) |

Nota importante: Siguiendo el principio de Kimball de hechos atómicos, ninguna de estas métricas derivadas se almacena físicamente en FACT_RENTABILIDAD. Se calculan dinámicamente en la capa de visualización (Power BI) utilizando los valores de DIM_COSTO vigentes para cada período, garantizando consistencia ante actualizaciones de costos de referencia.
Modelado dimensional (organización de tablas)
Los datos transformados se organizan en la tabla de hechos FACT_RENTABILIDAD y las siguientes tablas, incorporando claves sustitutas (surrogate keys) para optimizar la gestión histórica:

| Tipo | Tablas |
| --- | --- |
| Dimensiones principales | DIM_TIEMPO, DIM_UBICACION, DIM_PRODUCTO, DIM_VARIEDAD_CALIDAD, DIM_EXPORTADOR, DIM_ADUANA, DIM_FINANZAS, DIM_COSTO |
| Subdimensiones (normalización) | DIM_PAIS_TLC (conectada a DIM_UBICACION) |

Nota: DIM_COSTO es una dimensión tradicional con SCD Tipo 2 y FK directa. No existe tabla de parámetros en este modelo.

## 6.4 Fase de Carga y Validación de Integridad Referencial

La fase de carga consiste en la inserción de los datos previamente transformados en el Data Mart, asegurando su disponibilidad para el análisis y la generación de reportes.
Estrategia de carga:

| Parámetro | Valor |
| --- | --- |
| Tipo de carga | Carga completa inicial (histórico 2016-2024) + actualizaciones incrementales mensuales |
| Orden de carga | Primero dimensiones y subdimensiones, luego tabla de hechos |
| Motor de base de datos | PostgreSQL (local) |

Estructura de almacenamiento:
El Data Mart se implementa en el motor de base de datos relacional PostgreSQL, utilizando un esquema de Copo de Nieve (Snowflake Schema) estructurado bajo el esquema por defecto (public). Esta configuración está optimizada para el aislamiento de tablas analíticas y el rendimiento de consultas a través del motor tabular de Power BI.
Secuencia de carga (orden estricto por integridad referencial)
Para evitar violaciones de restricciones de llave foránea (FOREIGN KEY constraints), la carga en PostgreSQL sigue un orden jerárquico estricto:
Carga de dimensiones independientes (Nivel 0):
public.DIM_TIEMPO (Generación de fechas mediante script)
public.DIM_COSTO (Carga histórica inicial con estrategia SCD Tipo 2)
Carga de dimensiones con dependencias geográficas y comerciales (Nivel 1):
public.DIM_UBICACION (Países normalizados)
public.DIM_PAIS_TLC (Relacionada a la anterior, estructurando el Copo de Nieve)
Carga de dimensiones operativas y de producto (Nivel 2):
public.DIM_PRODUCTO (Filtrado por partida arancelaria de Palta Hass)
public.DIM_VARIEDAD_CALIDAD (Atributos extraídos por Regex)
public.DIM_EXPORTADOR (Empresas competidoras limpias)
public.DIM_ADUANA (Puntos de salida nacionales)
Carga de dimensiones financieras transaccionales (Nivel 3):
public.DIM_FINANZAS (Requiere que existan previamente el tiempo y la ubicación para el cruce de Tipo de Cambio y Aranceles)
Carga de la Tabla de Hechos Central (Nivel 4):
public.FACT_RENTABILIDAD (Inserción final indexando todas las llaves sustitutas/foráneas generadas en los pasos previos)
Validación y control de calidad:

| Verificación | Descripción | Acción ante error |
| --- | --- | --- |
| Integridad referencial | Verificar que no existan FK nulos o inválidos | Rechazar registro y registrar en log |
| Consistencia de cálculos | Validar que Ratio = (Margen / FOB) × 100 | Recalcular o rechazar |
| Conteo de registros | Comparar registros transformados vs cargados | Registrar diferencia en log |
| Log de control | Registrar registros procesados, insertados y rechazados | Archivo de log diario |

Código SQL para validación de integridad referencial
Validación de FK nulas en FACT_RENTABILIDAD

Conclusión: No se detectaron llaves foráneas nulas. La integridad referencial básica está garantizada.
Validación de FK que apuntan a registros inexistentes (huérfanos)

Conclusión: No se detectaron registros huérfanos. La integridad referencial está garantizada al 100%.
Validación de duplicados en la tabla de hechos (misma DUA + ITEM)

Conclusión: No existen registros duplicados a nivel de granularidad DUA + ITEM. Cada línea de producto dentro de cada Declaración Única de Aduanas es única.

## 6.5 Proceso de Normalización de Datos (1NF → 5NF)

Para garantizar la calidad, consistencia e integridad de los datos almacenados en el Data Mart, se aplicó un proceso sistemático de normalización basado en las Formas Normales (1NF a 5NF) propuestas por Edgar F. Codd. Este proceso transformó los datos crudos de SUNAT (formato plano y desnormalizado) en un modelo dimensional tipo Copo de Nieve (Snowflake Schema) optimizado para análisis OLAP.
A continuación, se documenta cada etapa con ejemplos prácticos, código utilizado y validaciones aplicadas.

### 6.5.1 Estado Inicial (Forma Desnormalizada - 0NF)

Los microdatos de exportación de la SUNAT se presentan como un único archivo plano (DBF/TXT) con múltiples repeticiones y valores no atómicos.
Ejemplo de datos crudos (0NF):

| NRO_DOCU | FECHA | PAIS | EXPORTADOR | FOB_DOLPOL | PESO_NETO | DESC_ADIC | CADUANA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DUA001 | 2024-06-01 | Países Bajos | Avocado Export S.A. | 50000 | 20000 | "PALTA HASS CAT 1 ORGANICA" | PAITA |
| DUA002 | 2024-06-01 | Países Bajos | Avocado Export S.A. | 30000 | 12000 | "PALTA HASS CAT 1" | PAITA |
| DUA003 | 2024-06-02 | España | Green Peru S.A.C. | 25000 | 10000 | "PALTA HASS CAT 2" | CALLAO |

Problemas identificados (violaciones a la normalización):

| Problema | Descripción | Impacto |
| --- | --- | --- |
| Repetición de datos del exportador | El mismo Avocado Export S.A. se repite en cada fila | Redundancia y riesgo de inconsistencia |
| Repetición de datos del país destino | Países Bajos se repite en múltiples filas | Mayor almacenamiento, actualización difícil |
| Campo no atómico | DESC_ADIC contiene múltiples atributos (variedad, calidad, método) | No se puede filtrar por calidad individualmente |
| Dependencia parcial | EXPORTADOR depende solo de DUA, no de ITEM | Violación de 2NF |


### 6.5.2 Primera Forma Normal (1NF) - Atomicidad

Cada columna debe contener valores atómicos e indivisibles. No debe haber grupos repetidos.
Transformación realizada:
Se extrajeron los valores del campo DESC_ADIC mediante expresiones regulares (Regex) en Python.
Se crearon columnas separadas: Variedad, Categoria_Calidad, Metodo_Produccion.
Se asignó una clave primaria compuesta (NRO_DOCU, ITEM) o se identificó que la combinación de NRO_DOCU + ITEM permite identificar unívocamente cada línea de producto dentro de una Declaración Única de Aduanas (DUA).

Resultado después de 1NF (tabla intermedia):

| NRO_DOCU | ITEM | FECHA | PAIS | RUC_EXPORT | FOB | PESO | VARIEDAD | CALIDAD | METODO | ADUANA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DUA001 | 1 | 2024-06-01 | Países Bajos | 20123456789 | 50000 | 20000 | HASS | CAT 1 | ORGANICO | PAITA |
| DUA001 | 2 | 2024-06-01 | Países Bajos | 20123456789 | 30000 | 12000 | HASS | CAT 1 | CONVENCIONAL | PAITA |

Validación de 1NF:

| Criterio | Cumple | Verificación |
| --- | --- | --- |
| ¿Cada columna tiene valores atómicos? | Sí | No hay listas ni valores compuestos |
| ¿Hay una clave primaria? | Sí | (DUA, ITEM) identifica unívocamente cada fila |
| ¿No hay grupos repetidos? | Sí | Cada producto está en su propia fila |


### 6.5.3 Segunda Forma Normal (2NF) - Dependencia Total

Eliminar dependencias parciales (atributos que dependen solo de parte de la clave primaria compuesta).
Problema detectado: La clave primaria es (DUA, ITEM). Sin embargo:
RUC_EXPORT y EXPORTADOR_NOMBRE dependen solo de DUA, no del ITEM
PAIS_NOMBRE y CONTINENTE dependen solo de CODIGO_PAIS
Transformación realizada: Separación en tablas independientes.


| -- Tabla de hechos (depende de la clave completa DUA + ITEM) FACT_RENTABILIDAD (FK_Tiempo, FK_Ubicacion, FK_Producto, FK_Variedad_Calidad,                    FK_Exportador, FK_Aduana, FK_Finanzas, FK_Costo,                    Valor_FOB, Volumen_Exportado, NRO_DOCU, ITEM)  -- Tabla de exportadores (depende solo de RUC) DIM_EXPORTADOR (RUC, Razon_Social, Tipo_Empresa)  -- Tabla de ubicación (depende solo de código país) DIM_UBICACION (Codigo_Pais, Pais_Nombre, Continente) |
| --- |


Código Python para la separación:


| # Extraer dimensión EXPORTADOR (depende solo de RUC) df_exportador = df[['RUC_EXPORT', 'EXPORTADOR']].drop_duplicates().reset_index(drop=True) df_exportador['ID_Exportador'] = df_exportador.index + 1  # Extraer dimensión UBICACION (depende solo de COD_PAIS) df_ubicacion = df[['COD_PAIS', 'PAIS', 'CONTINENTE']].drop_duplicates().reset_index(drop=True) df_ubicacion['ID_Ubicacion'] = df_ubicacion.index + 1  # Crear tabla de hechos con llaves foráneas df_hechos = df.merge(df_exportador, on=['RUC_EXPORT', 'EXPORTADOR']) df_hechos = df_hechos.merge(df_ubicacion, on=['COD_PAIS', 'PAIS', 'CONTINENTE']) df_hechos['FK_Exportador'] = df_hechos['ID_Exportador'] df_hechos['FK_Ubicacion'] = df_hechos['ID_Ubicacion'] |
| --- |


Validación de 2NF:

| Criterio | Cumple | Verificación |
| --- | --- | --- |
| ¿Está en 1NF? | Sí | Verificado en paso anterior |
| ¿No hay dependencias parciales? | Sí | Razon_Social se almacena una sola vez en DIM_EXPORTADOR |


### 6.5.4 Tercera Forma Normal (3NF) - Eliminar Dependencias Transitivas

Los atributos no clave no deben depender de otros atributos no clave.
Problema detectado: En DIM_UBICACION, los acuerdos comerciales (TLC) y aranceles dependen del país, pero no son atributos directos de la ubicación geográfica. Además, un país puede tener múltiples acuerdos históricos.
Transformación realizada: Creación de subdimensión DIM_PAIS_TLC.


| -- Se extraen atributos comerciales a subdimensión independiente DIM_PAIS_TLC (ID_Pais_TLC, FK_Ubicacion, Acuerdo_TLC, Arancel_Porcentaje, Fecha_Vigencia, Categoria_Mercado) Código Python para la extracción: python # Crear subdimensión TLC basada en datos de MINCETUR df_tlc = pd.DataFrame({     'FK_Ubicacion': [1, 2, 3, 4, 5],     'Acuerdo_TLC': [         'Acuerdo Perú-UE (2013)',         'TLC Perú-EE.UU. (2009)',         'TLC Perú-China (2010)',          'TLC Perú-Reino Unido (2021)',         'TLC Perú-Japón (2012)'     ],     'Arancel_Porcentaje': [0.00, 0.00, 0.00, 0.00, 0.00],     'Categoria_Mercado': ['Premium', 'Premium', 'Premium', 'Premium', 'Premium'],     'Fecha_Vigencia': ['2013-01-01', '2009-01-01', '2010-01-01', '2021-01-01', '2012-01-01'] }) |
| --- |

Validación de 3NF:

| Criterio | Cumple | Verificación |
| --- | --- | --- |
| ¿Está en 2NF? | Sí | Verificado en paso anterior |
| ¿No hay dependencias transitivas? | Sí | Los aranceles se actualizan sin duplicar información de países |


### 6.5.5 Forma Normal de Boyce-Codd (BCNF) - Superclaves

Todo determinante debe ser una superclave.
Problema detectado: En la tabla de costos, el Tipo_Costo (Producción, Empaque, Logístico) determina el Valor_Unitario_USD para una región y fecha, pero Tipo_Costo no es una superclave por sí solo.
Transformación realizada: Se rediseñó DIM_COSTO como una dimensión SCD Tipo 2 donde la combinación (Tipo_Costo, Region_Destino, Fecha_Vigencia_Inicio) es la clave única (superclave).
Estructura final de DIM_COSTO (BCNF):

| SK_Costo (PK) | ID_Costo | Tipo_Costo | Subcategoria | Valor_Unitario | Region | Fecha_Inicio | Fecha_Fin | Es_Vigente |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | Producción | Labores Culturales | 0.25 | Global | 2016-01-01 | 2022-12-31 | FALSE |
| 2 | 1 | Producción | Labores Culturales | 0.30 | Global | 2023-01-01 | NULL | TRUE |
| 3 | 2 | Producción | Mano de Obra Cosecha | 0.20 | Global | 2016-01-01 | NULL | TRUE |
| 4 | 3 | Producción | Procesamiento Packing | 0.30 | Global | 2016-01-01 | NULL | TRUE |
| 5 | 4 | Logístico | Transporte Terrestre | 0.15 | Global | 2016-01-01 | NULL | TRUE |
| 6 | 5 | Logístico | Servicios Portuarios | 0.60 | Global | 2016-01-01 | NULL | TRUE |
| 7 | 6 | Logístico | Agenciamiento | 0.04 | Global | 2016-01-01 | NULL | TRUE |
| 8 | 7 | Operativo | Certificaciones | 0.06 | Global | 2016-01-01 | NULL | TRUE |
| 9 | 8 | Operativo | Gastos Administrativos | 0.04 | Global | 2016-01-01 | NULL | TRUE |

Código SQL para validar BCNF (sin solapamiento de fechas):

| -- Verificar que no hay solapamiento de fechas en DIM_COSTO -- Esto asegura que la combinación (Tipo_Costo, Region_Destino, Fecha) es única SELECT Tipo_Costo, Region_Destino, Fecha_Vigencia_Inicio, Fecha_Vigencia_Fin FROM DIM_COSTO c1 WHERE EXISTS (     SELECT 1 FROM DIM_COSTO c2     WHERE c2.Tipo_Costo = c1.Tipo_Costo     AND c2.Region_Destino = c1.Region_Destino     AND c2.SK_Costo != c1.SK_Costo     AND c2.Fecha_Vigencia_Inicio < c1.Fecha_Vigencia_Fin     AND c1.Fecha_Vigencia_Inicio < c2.Fecha_Vigencia_Fin ); -- Resultado esperado: Ningún registro retornado (sin solapamientos) |
| --- |


Validación de BCNF:

| Criterio | Cumple | Verificación |
| --- | --- | --- |
| ¿Está en 3NF? | Sí | Verificado en paso anterior |
| ¿Todo determinante es superclave? | Sí | (Tipo_Costo + Region_Destino + Fecha_Vigencia_Inicio) identifica unívocamente cada registro |


### 6.5.6 Cuarta Forma Normal (4NF) - Eliminar Dependencias Multivaluadas

No debe haber dos o más relaciones multivaluadas independientes en la misma tabla.
Problema detectado: En los datos originales, un mismo producto podía tener múltiples calidades y múltiples métodos de producción registrados en un solo campo. No se puede saber si "CAT 1" corresponde a "ORGÁNICO" o si son combinaciones independientes.
Transformación realizada: Se separó DIM_VARIEDAD_CALIDAD como una dimensión independiente (no subdimensión de DIM_PRODUCTO).


| -- DIM_PRODUCTO: solo atributos intrínsecos del producto (una sola combinación por producto) DIM_PRODUCTO (ID_Producto, Partida_Arancelaria, Descripcion)  -- DIM_VARIEDAD_CALIDAD: atributos de calidad (independiente, puede tener múltiples combinaciones) DIM_VARIEDAD_CALIDAD (ID_Variedad_Calidad, Variedad, Categoria_Calidad, Metodo_Produccion, Fuente_Extraccion) |
| --- |

Ejemplo de la separación:

| Antes (en una sola tabla) | Después (tablas independientes) |
| --- | --- |
| DIM_PRODUCTO contendría: (Partida, Hass, CAT 1, CAT 2, Orgánico, Convencional) | DIM_PRODUCTO: solo (Partida, Descripcion) <br> DIM_VARIEDAD_CALIDAD: (Hass, CAT 1, Orgánico), (Hass, CAT 1, Convencional), (Hass, CAT 2, Convencional) |

Validación de 4NF:

| Criterio | Cumple | Verificación |
| --- | --- | --- |
| ¿Está en BCNF? | Sí | Verificado en paso anterior |
| ¿No hay dependencias multivaluadas independientes? | Sí | DIM_VARIEDAD_CALIDAD es independiente de DIM_PRODUCTO |


### 6.5.7 Quinta Forma Normal (5NF) - Dependencia de Join (Descomposición sin pérdida)

La tabla original debe poder reconstruirse exactamente mediante joins de las tablas resultantes, sin filas adicionales o faltantes.
Validación realizada: Se verificó que el siguiente join reconstruye exactamente la tabla original.
Código SQL para validar 5NF (reconstrucción sin pérdida):


| WITH Reconstruccion AS (     SELECT          f.Valor_FOB,         f.Volumen_Exportado,         f.NRO_DOCU,         f.ITEM,         t.Fecha,         u.Pais_Nombre,         e.Razon_Social as Exportador,         p.Descripcion_Oficial as Producto,         v.Categoria_Calidad,         v.Metodo_Produccion,         a.Nombre_Aduana,         fin.Tipo_Cambio_USD_PEN,         c.Tipo_Costo,         c.Valor_Unitario_USD     FROM "FACT_RENTABILIDAD" f     JOIN "DIM_TIEMPO" t ON f."FK_Tiempo" = t."ID_Tiempo"     JOIN "DIM_UBICACION" u ON f."FK_Ubicacion" = u."ID_Ubicacion"     JOIN "DIM_EXPORTADOR" e ON f."FK_Exportador" = e."ID_Exportador"     JOIN "DIM_PRODUCTO" p ON f."FK_Producto" = p."ID_Producto"     JOIN "DIM_VARIEDAD_CALIDAD" v ON f."FK_Variedad_Calidad" = v."ID_Variedad_Calidad"     JOIN "DIM_ADUANA" a ON f."FK_Aduana" = a."ID_Aduana"     JOIN "DIM_FINANZAS" fin ON f."FK_Finanzas" = fin."ID_Finanzas"     JOIN "DIM_COSTO" c ON f."FK_Costo" = c."ID_Costo" ) SELECT      COUNT(*) as Registros_Reconstruidos,     (SELECT COUNT(*) FROM "FACT_RENTABILIDAD") as Registros_Originales FROM Reconstruccion; |
| --- |


Resultado esperado:

| Registros_Reconstruidos | Registros_Originales | Diferencia |
| --- | --- | --- |
| 100,000 | 100,000 | 0 |

Validación de 5NF:

| Criterio | Cumple | Verificación |
| --- | --- | --- |
| ¿Está en 4NF? | Sí | Verificado en paso anterior |
| ¿La descomposición es sin pérdida? | Sí | El número de registros reconstruidos coincide con el original |


### 6.5.8 Resumen del Proceso de Normalización Aplicado


| Forma Normal | Regla aplicada | Estructura resultante | Beneficio obtenido |
| --- | --- | --- | --- |
| 1NF | Atomicidad | Extracción de atributos desde DESC_ADIC vía Regex | Búsqueda y filtrado eficiente por calidad |
| 2NF | Dependencia total | Separación de hechos (DUA+ITEM) de dimensiones (Exportador, Ubicación) | Reducción de redundancia (RUC se almacena una vez) |
| 3NF | Sin transitivas | Creación de DIM_PAIS_TLC (aranceles y TLC) | Los aranceles se actualizan sin duplicar países |
| BCNF | Superclaves | DIM_COSTO con SCD Tipo 2 (clave compuesta) | Historial de costos y FK directa desde hechos |
| 4NF | Sin multivaluadas | DIM_VARIEDAD_CALIDAD independiente de DIM_PRODUCTO | Un producto puede tener múltiples combinaciones de calidad |
| 5NF | Join sin pérdida | Verificación de reconstrucción exacta de la tabla original | Garantía de que no hay pérdida de información |


# 7. VISUALIZACIÓN Y ANÁLISIS


## 7.1 Análisis de KPIs

Al conectarse a PostgreSQL, Power BI conserva el esquema por defecto (public) como prefijo en el nombre de las tablas. Por lo tanto, el código DAX hace referencia explícita a 'public' seguido del nombre de la tabla.
A continuación, se presentan los 6 KPIs definidos para el proyecto, sus fórmulas de cálculo, metas establecidas y las medidas DAX que los implementan en Power BI.

### 7.1.1 KPI 1: Precio Promedio FOB/kg

Fórmula:


| Precio Promedio FOB/kg = Σ(Valor_FOB) ÷ Σ(Peso_Neto) |
| --- |


Meta: Variable por país destino (identificar mercados premium)
¿Qué pregunta responde?
P2: ¿Qué países y continentes presentan consistentemente un precio promedio FOB/kg superior?
P5: ¿Qué aduanas presentan mejor precio promedio por kilogramo?
P6: ¿Qué relación existe entre el volumen exportado y el precio promedio FOB/kg?
Medida DAX en Power BI:


| Precio FOB/kg (USD) =  DIVIDE([Ingreso FOB Total (USD)], [Volumen Total (kg)], 0) |
| --- |



### 7.1.2 KPI 2: Margen de Utilidad Estimado

Fórmula:


| Margen de Utilidad Estimado = Ingreso FOB − Costo Total Estimado |
| --- |


Meta: Positivo (> 0 USD)
¿Qué pregunta responde?
Central: ¿Cuál es el nivel de rentabilidad potencial de la palta Hass?
Medida DAX en Power BI:


| Margen Utilidad (USD) =  [Ingreso FOB Total (USD)] - [Costo Total (USD)] |
| --- |



### 7.1.3 KPI 3: Ratio de Rentabilidad (%)

Fórmula:


| Ratio de Rentabilidad (%) =  DIVIDE([Margen Utilidad (USD)], [Ingreso FOB Total (USD)], 0) * 100 |
| --- |


Meta: 15% - 25% (según estándares de Sierra Exportadora)
¿Qué pregunta responde? (Sección 1.7)
Central: ¿Cuál es el nivel de rentabilidad potencial de la palta Hass?
P1: ¿Cómo evoluciona el precio y cómo se compara con el ratio de rentabilidad?
P2: ¿Qué países presentan un ratio de rentabilidad más alto?
Medida DAX en Power BI:


| Ratio de Rentabilidad (%) =  DIVIDE([Margen Utilidad (USD)], [Ingreso FOB Total (USD)], 0) * 100 |
| --- |



### 7.1.4 KPI 4: Índice de Concentración por Destino

Fórmula:


| Concentración Top 3 (%) =  VAR Top3Paises =  TOPN(  3,  ALLSELECTED('public DIM_UBICACION'[Pais_Nombre]),  [Ingreso FOB Total (USD)],  DESC  ) VAR IngresoTop3 =  SUMX(Top3Paises, [Ingreso FOB Total (USD)]) VAR TotalMercado =   CALCULATE([Ingreso FOB Total (USD)], ALLSELECTED('public DIM_UBICACION')) RETURN  -- Coerce el resultado a decimal puro para desbloquear la interfaz:  CONVERT(DIVIDE(IngresoTop3, TotalMercado, 0), DOUBLE) |
| --- |


Meta: < 70% (cartera diversificada)
¿Qué pregunta responde? (Sección 1.7)
P3: ¿Cuál es el nivel de concentración de las exportaciones por país destino? ¿Existe riesgo de dependencia excesiva de pocos mercados?
Medida DAX en Power BI:


| Concentración Top 3 (%) =  VAR Top3Paises =  TOPN(  3,  ALLSELECTED('public DIM_UBICACION'[Pais_Nombre]),  [Ingreso FOB Total (USD)],  DESC  ) VAR IngresoTop3 =  SUMX(Top3Paises, [Ingreso FOB Total (USD)]) VAR TotalMercado =   CALCULATE([Ingreso FOB Total (USD)], ALLSELECTED('public DIM_UBICACION')) RETURN  -- Coerce el resultado a decimal puro para desbloquear la interfaz:  CONVERT(DIVIDE(IngresoTop3, TotalMercado, 0), DOUBLE) |
| --- |



### 7.1.5 KPI 5: Índice HHI (Herfindahl-Hirschman)

Fórmula:


| HHI (Índice Herfindahl) =  VAR TotalIngreso = [Ingreso FOB Total (USD)] RETURN  SUMX(  VALUES('public DIM_UBICACION'[Pais_Nombre]),  VAR Participacion = DIVIDE([Ingreso FOB Total (USD)], TotalIngreso, 0)  RETURN Participacion * Participacion  ) * 10000 |
| --- |


Meta: < 2500 (mercado competitivo)
¿Qué pregunta responde? (Sección 1.7)
P4: ¿Qué nivel de concentración presenta el mercado de exportadores peruanos? ¿Existen pocos actores dominantes o el mercado está diversificado?
Medida DAX en Power BI:


| HHI (Índice Herfindahl) =  VAR TotalIngreso = [Ingreso FOB Total (USD)] RETURN  SUMX(  VALUES('public DIM_UBICACION'[Pais_Nombre]),  VAR Participacion = DIVIDE([Ingreso FOB Total (USD)], TotalIngreso, 0)  RETURN Participacion * Participacion  ) * 10000 |
| --- |



### 7.1.6 KPI 6: Margen Neto Ajustado (PEN)

Fórmula:


| Margen Neto Ajustado =  SUMX(  'public FACT_RENTABILIDAD',  ('public FACT_RENTABILIDAD'[Valor_FOB] * RELATED('public DIM_FINANZAS'[Tipo_Cambio_USD_PEN])) -  ('public FACT_RENTABILIDAD'[Volumen_Exportado] * RELATED('public DIM_COSTO'[Valor_Unitario_USD]) * RELATED('public DIM_FINANZAS'[Tipo_Cambio_USD_PEN])) -  ('public FACT_RENTABILIDAD'[Valor_FOB] * RELATED('public DIM_FINANZAS'[Arancel_Porcentaje]) / 100) ) |
| --- |


Meta: Positivo (> 0 PEN)
¿Qué pregunta responde? (Sección 1.7)
Central: ¿Cuál es el nivel de rentabilidad potencial de la palta Hass? (considerando tipo de cambio y aranceles)
Medida DAX en Power BI:


| Margen Neto Ajustado =  SUMX(  'public FACT_RENTABILIDAD',  ('public FACT_RENTABILIDAD'[Valor_FOB] * RELATED('public DIM_FINANZAS'[Tipo_Cambio_USD_PEN])) -  ('public FACT_RENTABILIDAD'[Volumen_Exportado] * RELATED('public DIM_COSTO'[Valor_Unitario_USD]) * RELATED('public DIM_FINANZAS'[Tipo_Cambio_USD_PEN])) -  ('public FACT_RENTABILIDAD'[Valor_FOB] * RELATED('public DIM_FINANZAS'[Arancel_Porcentaje]) / 100) ) |
| --- |



### 7.1.7 Medidas Adicionales para Segmentación y Formato

Además de los 6 KPIs principales, se implementaron medidas adicionales para facilitar la segmentación, el formato visual y la interpretación de los resultados:

| Medida | Propósito |
| --- | --- |
| Estado Rentabilidad | Clasifica el ratio en categorías textuales (Óptima >25%, En objetivo 15-25%, Por debajo <15%) |
| Rentabilidad GENERAL | Muestra el ratio con formato y emoji de semáforo |
| Color Rentabilidad | Asigna color hexadecimal dinámico a tarjetas según el nivel de rentabilidad |
| Mensaje Estado | Genera recomendación automática para la tarjeta ejecutiva |
| Concentración Top 5 (%) | Complementa al KPI 4 mostrando concentración en Top 5 países |
| % Acumulado FOB | Calcula la curva de Pareto para análisis de concentración |
| Índice Concentración Destino | Mide el % de FOB concentrado en un país específico |
| Estrategia País | Recomienda estrategia comercial según rentabilidad y TLC |
| % Mercado Exportador | Calcula participación de mercado de cada exportador |



### 7.1.8 Resumen de Metas por KPI


| KPI | Meta | Interpretación |
| --- | --- | --- |
| Ratio de Rentabilidad | 15% - 25% | Rango viable para productos agroexportadores no tradicionales según Sierra Exportadora |
| HHI (Índice Herfindahl) | < 2500 | Mercado competitivo (no concentrado) |
| Concentración Top 3 | < 70% | Cartera diversificada de países destino |
| Margen Neto Ajustado | > 0 (positivo) | Rentabilidad real en soles después de tipo de cambio y aranceles |
| Precio Promedio FOB/kg | Variable por destino | Identificar mercados premium |
| Margen de Utilidad | > 0 (positivo) | Cada operación debe generar ganancia |



### 7.1.9 Mapeo de KPIs a Preguntas de Negocio


| Pregunta de Negocio (Sección 1.7) | KPI(s) que la responden |
| --- | --- |
| Central: ¿Cuál es el nivel de rentabilidad potencial de la palta Hass? | KPI 2, KPI 3, KPI 6 |
| P1: Evolución temporal del precio y rentabilidad | KPI 1, KPI 3 |
| P2: Mejores países/continentes por precio y rentabilidad | KPI 1, KPI 3 |
| P3: Concentración por país destino (riesgo de dependencia) | KPI 4 |
| P4: Concentración del mercado de exportadores (HHI) | KPI 5 |
| P5: Aduanas/puertos más eficientes | KPI 1 (segmentado por Aduana) |
| P6: Relación volumen vs precio (economías de escala) | KPI 1 (gráfico de dispersión) |



## 7.2 Estructura del Dashboard

El archivo analizado Proyecto-Equipo1.pbix está compuesto exactamente por 5 hojas estructuradas de la siguiente manera:
Página 1: 1. Resumen Ejecutivo
Visuales:
3 Tarjetas (card): Muestran de forma global e instantánea los totales agregados de Valor FOB (USD), Volumen total exportado (kg) y el Precio Promedio kg general.
2 Gráficos de líneas (lineChart): Muestran la tendencia temporal histórica de la exportación año a año.
1 Gráfico de barras horizontales (clusteredBarChart): Compara el volumen transaccionado por los exportadores principales.

# 1 Cuadro de texto (textbox): Describe el contexto inicial del dashboard.

Página 2: 2. Análisis de Mercados
Visuales:
1 Mapa interactivo (azureMap): Visualiza la distribución geográfica mundial de los despachos de palta Hass, facilitando la identificación de zonas calientes de destino.
1 Tabla detallada (tableEx): Muestra el desglose por País de Destino, Continente, FOB, Volumen, y Precio Promedio.
1 Gráfico combinado de líneas y columnas (lineStackedColumnComboChart): Cruza el volumen físico frente al precio por kg obtenido por mercado.
Página 3: 3. Rentabilidad
Visuales:
1 Tabla dinámica/Matriz (pivotTable): Detalla el margen de utilidad y los costos asociados por cada país y variedad.
1 Gráfico de dispersión (scatterChart): Posiciona a los países de destino según su volumen vs. precio unitario, ideal para segmentar los nichos de alto valor de los de volumen transaccional.

# 1 Gráfico de barras (barChart): Representa visualmente los ratios de rentabilidad por destino.

Página 4: 4. Riesgo y Concentración
Visuales:
1 Gráfico de áreas/Treemap (treemap): Muestra la participación porcentual de mercado (Market Share) de cada una de las 435 empresas agroexportadoras peruanas de palta.
1 Gráfico de líneas (lineChart): Muestra la evolución temporal del Índice de Herfindahl-Hirschman (HHI).
4 Tarjetas de KPIs (card): Resumen los indicadores claves de concentración y volatilidad del mercado.
Página 5: 5. Recomendación Estratégica
Visuales:
1 Tarjeta principal (card): Vinculada a la medida Mensaje Estado, automatiza el texto de recomendación descriptiva adaptada según los filtros aplicados.

# 1 Botón de acción (actionButton): Facilita la navegación rápida o reset de filtros.

1 Tarjeta de semáforo visual (card): Cambia el fondo condicional (Color Rentabilidad) para capturar la atención gerencial de forma inmediata.

## 7.3 Análisis Descriptivo e Interpretación de Resultados

El Comportamiento General del Mercado
El análisis de las exportaciones de palta Hass peruana refleja un negocio consolidado. A nivel global, la rentabilidad promedio se sitúa en un 20.21% , situándose exactamente dentro del rango objetivo (15%-25%) y validando la viabilidad general de la inversión. El precio promedio FOB del período 2016-2024 es de 2.06 USD/kg , mostrando una tendencia de crecimiento sostenido desde valores cercanos a 1.80 USD/kg en años iniciales hasta alcanzar picos de 2.85 USD/kg en 2023.
El Descubrimiento de los "Nichos Premium"
Al segmentar geográficamente el análisis, se identificó una realidad comercial sumamente atractiva en mercados específicos que operan bajo TLC (Acuerdos comerciales vigentes con arancel 0%):

| País de Destino | Precio FOB Promedio (USD/kg) | Ratio de Rentabilidad (%) |
| --- | --- | --- |
| Israel | $3.60 | 54.44% |
| Macao | $3.00 | 45.33% |
| Suiza | $2.93 | 43.93% |
| Promedio Mundial | $2.05 | 20.14% |

Interpretación: La rentabilidad general (20.21%) incluye destinos masivos de menor valor. Sin embargo, Israel, Macao, Puerto Rico, Suiza y Tailandia representan nichos de alto valor unitario que pagan un precio FOB hasta 75% superior al promedio mundial (Israel: $3.60 vs $2.06), logrando rentabilidades que duplican o triplican el umbral esperado.
Estructura Competitiva y Logística
Índice HHI: El cálculo arrojó un valor de 2,220, ubicándose por debajo de la barrera crítica de 2,500. Esto clasifica al mercado como altamente competitivo y fragmentado. No existe un monopolio absoluto de las grandes agroexportadoras, lo cual indica que Peruvian Andean Trout S.A.C. tiene espacio de entrada comercial sin enfrentar bloqueos de competidores dominantes.
Puntos de Salida: La Aduana de Paita concentra el 58% del volumen exportado de palta Hass, seguida por la Aduana Marítima del Callao. Esto orienta la estrategia logística hacia el puerto del norte peruano.

## 7.4 Análisis Predictivo

Aplicando modelos de regresión lineal (línea de tendencia automática en el gráfico de evolución de Power BI), se proyecta que bajo condiciones macroeconómicas y climáticas estables, el precio FOB promedio nacional de la palta Hass alcance los 3.10 USD/kg para el año 2026 (R² = 0.87), lo que consolida un escenario de mediano plazo favorable para iniciar la siembra y comercialización.

## 7.5 Storytelling: "De la trucha a la palta"

El Inicio (Desafío): Peruvian Andean Trout S.A.C. se enfrenta a un mercado de trucha estancado y busca diversificarse.
El Conflicto: ¿La agroexportación de palta Hass es verdaderamente atractiva o está saturada por competidores gigantescos?
El Descubrimiento (Clímax): El Data Mart revela que, aunque el promedio del mercado da una rentabilidad moderada del 20.21% , existen mercados premium (Israel, Macao, Suiza) que pagan precios excelentes. Además, el índice HHI de 2,220 confirma que la competencia está lo suficientemente atomizada como para permitir que un nuevo jugador ingrese con éxito.
La Resolución: La gerencia aprueba la diversificación enfocándose en nichos de alto valor, operando logísticamente a través de la aduana de Paita para optimizar costos de flete.

## 7.6 Análisis Exploratorio Profundo y Prueba de Hipótesis (T-Test)

Se ejecutó un script Python sobre 10,063 registros limpios de exportación para medir la volatilidad:

| Estadístico | Valor |
| --- | --- |
| Media Precio FOB | 2.2999 USD/kg |
| Varianza | 0.4586 |
| Desviación Estándar | 0.6772 USD |

Conclusión: Una desviación de casi $0.68 indica volatilidad alta, justificando la necesidad de monitoreo constante de precios mediante BI.
Pregunta de Negocio: ¿Existe diferencia estadística real entre el precio que paga EE.UU. frente a Europa?
Hipótesis Nula (H₀): El precio promedio en EE.UU. es igual al de Europa.
Resultados: P-Value = 2.499e-239. Media EE.UU: 2.37 USD vs Media Europa: 2.03 USD.
Conclusión Técnica: Dado que el P-Value < 0.05, RECHAZAMOS la hipótesis nula. Es un hecho estadístico que Estados Unidos es un mercado de mayor rentabilidad que Europa para este dataset.
Nota metodológica: Los estadísticos de esta subsección (media 2.30 USD/kg, varianza 0.4586) fueron calculados sobre una muestra de 10,063 registros. El promedio general del período 2016-2024 calculado sobre el total de 40,588 registros es de 2.06 USD/kg. Esta diferencia es consistente con la heterogeneidad de los datos y no afecta las conclusiones estadísticas.


## 7.7 Modelo Predictivo: Regresión Lineal

Se entrenó un modelo de regresión lineal (scikit-learn) para predecir el Precio FOB utilizando el Volumen Exportado.
Resultados: R-cuadrado = 0.000067
Justificación Técnica: Un R² cercano a cero demuestra matemáticamente que el volumen exportado NO tiene capacidad predictiva sobre el precio. Esto comprueba empíricamente que la Palta Hass es un commodity dependiente del mercado internacional.



## 7.8 Modelo de Estacionalidad: Análisis de Series de Tiempo

Para comprender mejor el comportamiento predictivo de la rentabilidad, se ejecutó un análisis de series de tiempo agrupando el precio FOB promedio por mes. Dado que el volumen exportado demostró no ser un predictor válido (Sección 7.7), la variable tiempo se consolida como el factor clave en la fluctuación de los precios agrícolas.
Resultados: El precio máximo histórico se alcanza en el mes de Noviembre (2.27 USD/kg), mientras que el precio más bajo ocurre en Octubre (1.81 USD/kg).

Justificación Estratégica: Esta curva de estacionalidad comprueba que la rentabilidad de la Palta Hass depende fuertemente de la ventana de exportación (ley de oferta y demanda global). Para maximizar el retorno de inversión, se recomienda que Peruvian Andean Trout SAC concentre sus campañas de cosecha y envíos internacionales en los meses de mayor cotización, aprovechando la escasez del producto en el hemisferio norte.


# 8. CONCLUSIONES

El presente proyecto de inteligencia de negocios logró el desarrollo e implementación exitosa de un Data Mart bajo un modelo dimensional de copo de nieve (snowflake schema) en PostgreSQL. A través de esta arquitectura, se integraron datos de SUNAT y fuentes económicas externas (BCRP, MINCETUR, MIDAGRI, Sierra Exportadora), permitiendo un análisis exhaustivo de la rentabilidad de la palta Hass en el período 2016-2024. Se implementó un proceso ETL optimizado en Python que aplicó algoritmos de limpieza con expresiones regulares (regex) para identificar exclusivamente la variedad Hass y filtrar registros ruidosos. Asimismo, se construyeron indicadores clave de desempeño (KPI), tales como el margen de utilidad, el ratio de rentabilidad y el índice de concentración Herfindahl-Hirschman (HHI). La visualización de estos datos en Power BI permite concluir que la estructura de datos es capaz de segmentar los mercados con mayor potencial de rentabilidad, logrando una transición exitosa de datos crudos a información estratégica para la toma de decisiones.

Es fundamental reconocer que la precisión del análisis está sujeta a la naturaleza de las fuentes utilizadas. Los costos operativos empleados son referenciales (provenientes de MIDAGRI y Sierra Exportadora) y no corresponden a costos reales internos de Peruvian Andean Trout SAC, lo que califica la rentabilidad calculada como potencial o estimada. Asimismo, la falta de datos directos sobre el importador final en los registros aduaneros públicos de SUNAT obligó al uso de la ubicación geográfica (DIM_UBICACION) como variable proxy del mercado consumidor, una simplificación válida para el alcance del proyecto. Finalmente, la extracción de datos cualitativos (calidad y método de producción) a partir de campos no estructurados (DESC_ADIC, DESC_COM) mediante expresiones regulares presenta un margen de error propio del procesamiento de lenguaje natural.

El Data Mart desarrollado provee una herramienta de simulación financiera sustentada en datos reales de aduanas, reduciendo drásticamente la incertidumbre de la Gerencia de Finanzas. Esto permite estimar el retorno de inversión del proyecto de diversificación agrícola antes de comprometer capital en campos de cultivo, transformando el proceso de evaluación de exportaciones de un enfoque empírico a uno basado en evidencia.

A partir de los hallazgos y limitaciones identificadas, se derivan las siguientes recomendaciones para Peruvian Andean Trout SAC. En el ámbito técnico, se recomienda implementar un sistema ERP agrícola que permita registrar costos operativos internos reales de producción y empaque, reemplazando el costo referencial estimado de 0.85 USD/kg para obtener un margen de utilidad real en futuras versiones del Data Mart. Asimismo, se sugiere escalar el modelo actual hacia un Data Warehouse corporativo que integre otros productos de la canasta agroexportadora peruana. En el ámbito comercial, los resultados (rentabilidad general del 20.21% y superior al 40% en nichos específicos, con un HHI de 2220 puntos y una concentración del Top 3 de 74.21%) justifican comercialmente la diversificación hacia la palta Hass. Se recomienda adoptar un enfoque de mercado dual: mantener envíos de volumen hacia destinos consolidados de Europa (Países Bajos y España), y destinar un porcentaje de la producción de alta calidad (Categoría 1) a nichos premium identificados (Israel, Macao, Puerto Rico, Suiza y Tailandia). Es imperativo priorizar los mercados con tratados de libre comercio (TLC) donde el arancel es nulo (Unión Europea, Estados Unidos, China, Japón, Corea del Sur, Hong Kong, Reino Unido), buscando diversificar la cartera de destinos para evitar que el índice HHI supere los niveles de riesgo establecidos (2500 puntos). Además, se recomienda canalizar los despachos mediante la Aduana de Paita debido a su alta frecuencia de fletes y especialización en el manejo de contenedores refrigerados para palta.

En conclusión, el sistema desarrollado proporciona una infraestructura analítica sólida que transforma el proceso de evaluación de exportaciones de un enfoque empírico a uno basado en evidencia. Los resultados obtenidos validan que el uso de modelos dimensionales y herramientas de inteligencia de negocios es el camino crítico para que Peruvian Andean Trout SAC logre una diversificación competitiva y sostenible en el sector agroindustrial.

Como principal recomendación y trabajo futuro, se plantea la evolución del presente Data Mart hacia una arquitectura en tiempo real y predictiva. En primer lugar, se sugiere la implementación de un pipeline de streaming de datos mediante Apache Kafka, lo cual permitirá ingerir las APIs financieras del BCRP al instante y evitar la latencia de los procesos por lotes (mensuales). Asimismo, para potenciar el análisis comercial, resulta fundamental integrar algoritmos de Machine Learning de aprendizaje no supervisado, como el Clustering K-Means. Esto habilitará la segmentación automática de los países en nichos estratégicos (Premium, Estándar y de Riesgo) basándose en su historial de volumen y precio FOB, descubriendo nuevas oportunidades sin intervención manual. Finalmente, para garantizar una gestión proactiva, se debe establecer un patrón de alertas automáticas en Power BI Service que notifique inmediatamente a la Gerencia Financiera en caso de que el Ratio de Rentabilidad global descienda por debajo del umbral crítico del 15%.

# 9. REFERENCIAS


Banco Central de Reserva del Perú. (s. f.). Series estadísticas de comercio exterior. https://www.bcrp.gob.pe/estadisticas.html

Compuempresa. (2025). Peruvian Andean Trout S.A.C. - RUC 20568513216. https://compuempresa.com/info/peruvian-andean-trout-sac-C33D92F4B13EC53D

Ministerio de Comercio Exterior y Turismo. (2024). Laguna De Choclococha. Plataforma del Estado Peruano. http://consultasenlinea.mincetur.gob.pe/fichaInventario/index.aspx?cod_Ficha=1158

Ministerio de Comercio Exterior y Turismo. (2024). Reporte de comercio regional (RCR) – Huancavelica. https://www.gob.pe/institucion/mincetur/colecciones/559-reporte-de-comercio-regional-rcr-huancavelica

Ministerio de Desarrollo Agrario y Riego (MIDAGRI). (2023). Sistema Integrado de Estadística Agraria (SIEA) - Costos de producción. https://siea.midagri.gob.pe

Ministerio de la Producción. (2017). Resolución Directoral N° 007-2017-PRODUCE/DGPA. https://www.gob.pe/institucion/produce/normas-legales/tipos/26-resolucion-directoral

Sierra y Selva Exportadora. (2022). Costos referenciales de logística de exportación para la palta Hass. https://www.sierraexportadora.gob.pe

Superintendencia Nacional de Aduanas y de Administración Tributaria. (2024). Operatividad aduanera: Consulta de exportación por partida. http://www.aduanet.gob.pe/operatividadAduana/

Superintendencia Nacional de Aduanas y de Administración Tributaria. (s. f.). Portal de microdatos de exportación y aduanas. https://www.sunat.gob.pe/estadisticasestudios/

Telefono.pe. (2025). Peruvian Andean Trout S.A.C. (PATSAC) - Teléfono y dirección. https://telefono.pe/patsac/

Ubicania. (2025). Peruvian Andean Trout S.A.C. - RUC 20568513216. https://ubicania.com/empresas/peruvian-andean-trout-s-a-c_id_EFEC59B20CC48C22

Vassiliadis, P. (2009). A survey of extract–transform–load technology. International Journal of Data Warehousing and Mining, 5(3), 1-27. https://doi.org/10.4018/jdwm.2009070101






# Anexo: Fórmulas DAX Específicas

Margen de Utilidad = [Ingreso FOB Total (USD)] - [Costo Total (USD)]
Precio Promedio FOB = DIVIDE([Ingreso FOB Total (USD)], [Volumen Total (kg)], 0)
Total Volumen Exportado = SUM('public FACT_RENTABILIDAD'[Volumen_Exportado])
Costo Total = [Volumen Total (kg)] * [Costo Unitario (USD/kg)]