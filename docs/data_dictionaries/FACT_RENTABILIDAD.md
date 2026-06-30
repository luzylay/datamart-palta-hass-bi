## Query1
| MEASURE\_NAME | EXPRESSION | DESCRIPTION |
| --- | --- | --- |
| Ingreso FOB Total (USD) | SUM('public FACT\_RENTABILIDAD'[Valor\_FOB]) | NaN |
| Volumen Total (kg) | SUM('public FACT\_RENTABILIDAD'[Volumen\_Exportado]) | NaN |
| Precio FOB/kg (USD) | DIVIDE([Ingreso FOB Total (USD)], [Volumen Total (kg)], 0) | NaN |
| Ratio de Rentabilidad (%) | DIVIDE([Margen Utilidad (USD)], [Ingreso FOB Total (USD)], 0) \* 100 | NaN |
| Estado Rentabilidad | VAR Ratio = [Ratio de Rentabilidad (%)]\nRETURN\n IF(Ratio > 25, "🟢 Óptima (>25%)",\n IF(Ratio >= 15, "🟡 En objetivo (15-25%)",\n "🔴 Por debajo del mínimo (<15%)")) | NaN |
| Rentabilidad GENERAL | VAR Ratio = [Ratio de Rentabilidad (%)]\nRETURN\n IF(Ratio < 15, "🔴 " & FORMAT(Ratio, "0.00") & "%",\n IF(Ratio >= 25, "🟢 " & FORMAT(Ratio, "0.00") & "%",\n "🟡 " & FORMAT(Ratio, "0.00") & "%")) | NaN |
| Color Rentabilidad | VAR Ratio = [Ratio de Rentabilidad (%)]\nRETURN\n SWITCH(\n TRUE(),\n Ratio >= 25, "#2ECC71", // Verde - Óptima\n Ratio >= 15, "#F39C12", // Amarillo - En objetivo\n Ratio < 15, "#E74C3C", // Rojo - Bajo\n "#FFFFFF" // Blanco (por defecto)\n ) | NaN |
| Mensaje Estado | VAR Ratio = [Ratio de Rentabilidad (%)]\nRETURN\n SWITCH(\n TRUE(),\n Ratio > 25, "✅✅✅ EXCELENTE ✅✅✅\n La rentabilidad supera el 25%, está por encima del objetivo óptimo.",\n Ratio >= 15, "✅ VIABLE ✅\n La rentabilidad está dentro del rango esperado (15-25%).",\n Ratio < 15, "⚠️ ATENCIÓN ⚠️\n La rentabilidad está por debajo del mínimo esperado (15%). Requiere revisión estratégica.",\n "📊 Sin datos"\n ) | NaN |
| Margen Neto Ajustado | SUMX(\n 'public FACT\_RENTABILIDAD',\n ('public FACT\_RENTABILIDAD'[Valor\_FOB] \* RELATED('public DIM\_FINANZAS'[Tipo\_Cambio\_USD\_PEN])) -\n ('public FACT\_RENTABILIDAD'[Volumen\_Exportado] \* RELATED('public DIM\_COSTO'[Valor\_Unitario\_USD]) \* RELATED('public DIM\_FINANZAS'[Tipo\_Cambio\_USD\_PEN])) -\n ('public FACT\_RENTABILIDAD'[Valor\_FOB] \* RELATED('public DIM\_FINANZAS'[Arancel\_Porcentaje]) / 100)\n) | NaN |
| Categoria\_Precio\_Medida | VAR PrecioPais = [Precio FOB/kg (USD)]\nRETURN\n SWITCH(\n TRUE(),\n PrecioPais >= 3.00, "Alto",\n PrecioPais >= 2.00, "Medio",\n PrecioPais < 2.00, "Bajo",\n "Sin datos"\n ) | NaN |