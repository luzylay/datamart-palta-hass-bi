## Query1
| MEASURE\_NAME | EXPRESSION | DESCRIPTION |
| --- | --- | --- |
| Costo Unitario (USD/kg) | SUM('public DIM\_COSTO'[Valor\_Unitario\_USD]) | NaN |
| Costo Total (USD) | [Volumen Total (kg)] \* [Costo Unitario (USD/kg)] | NaN |
| Margen Utilidad (USD) | [Ingreso FOB Total (USD)] - [Costo Total (USD)] | NaN |