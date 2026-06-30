import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import json
import sys

def analyze(csv_file):
    df = pd.read_csv(csv_file)
    
    # Clean data: drop nulls and zero volume
    df = df.dropna(subset=['Volumen_Exportado', 'Valor_FOB'])
    df = df[df['Volumen_Exportado'] > 0]
    
    # Calculate Price
    df['Precio_FOB'] = df['Valor_FOB'] / df['Volumen_Exportado']
    
    # Remove extreme outliers for plotting/analysis to get clean models if necessary
    # Or keep them? The prompt implies 10,063 records with mean 2.64 vs 2.21.
    # Let's just run it raw as the user has their data.
    
    # --- T-TEST ---
    us_data = df[df['Pais_Nombre'] == 'UNITED STATES']['Precio_FOB']
    eu_data = df[df['Continente'] == 'EUROPA']['Precio_FOB']
    
    t_stat, p_val = stats.ttest_ind(us_data, eu_data, equal_var=False)
    
    mean_us = us_data.mean()
    mean_eu = eu_data.mean()
    
    # Plot T-Test
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=[us_data, eu_data])
    plt.xticks([0, 1], ['EE.UU.', 'Europa'])
    plt.ylabel('Precio FOB (USD/kg)')
    plt.title(f'T-Test: Precio FOB EE.UU. vs Europa\nP-Value = {p_val:.2e}')
    plt.tight_layout()
    plt.savefig('ttest_plot.png')
    plt.close()
    
    # --- LINEAR REGRESSION ---
    X = df[['Volumen_Exportado']]
    y = df['Precio_FOB']
    
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    r2 = r2_score(y, y_pred)
    
    # Plot Regression
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, alpha=0.1, color='blue', label='Datos Reales')
    plt.plot(X, y_pred, color='red', label='Línea de Regresión')
    plt.xlabel('Volumen Exportado (kg)')
    plt.ylabel('Precio FOB (USD/kg)')
    plt.title(f'Regresión Lineal: Volumen vs Precio\nR² = {r2:.4f}')
    plt.legend()
    plt.tight_layout()
    plt.savefig('regression_plot.png')
    plt.close()
    
    # Results
    res = {
        'p_value': p_val,
        'mean_us': mean_us,
        'mean_eu': mean_eu,
        'r2': r2,
        'total_records': len(df)
    }
    
    with open('analysis_results.json', 'w') as f:
        json.dump(res, f)

if __name__ == '__main__':
    analyze(sys.argv[1])
