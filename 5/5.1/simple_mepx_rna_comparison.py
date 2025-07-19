"""
Ejemplo Simple: Usando datos de MEPX para entrenar RNA
Este script muestra cómo tomar datos de ejemplo de MEPX y usar RNAs para resolver el mismo problema.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

def create_sample_mepx_data():
    """
    Crea datos de ejemplo similares a los que encontrarías en MEPX
    Este ejemplo simula el problema "building1-energy" mencionado en la documentación
    """
    print("Creando datos de ejemplo estilo MEPX...")
    
    # Simular datos de eficiencia energética de edificios
    np.random.seed(42)
    n_samples = 768  # Tamaño típico de datasets de MEPX
    
    # Variables de entrada (características del edificio)
    relative_compactness = np.random.uniform(0.62, 0.98, n_samples)
    surface_area = np.random.uniform(514.5, 808.5, n_samples)
    wall_area = np.random.uniform(245.0, 416.5, n_samples)
    roof_area = np.random.uniform(110.25, 220.5, n_samples)
    overall_height = np.random.uniform(3.5, 7.0, n_samples)
    orientation = np.random.randint(2, 6, n_samples)
    glazing_area = np.random.uniform(0, 0.4, n_samples)
    glazing_area_dist = np.random.randint(0, 6, n_samples)
    
    # Variable objetivo: consumo de energía para calefacción
    # Fórmula basada en características físicas del edificio
    heating_load = (
        15 + 
        20 * relative_compactness + 
        0.01 * surface_area + 
        0.05 * wall_area + 
        0.02 * roof_area + 
        2 * overall_height + 
        orientation + 
        25 * glazing_area + 
        0.5 * glazing_area_dist +
        np.random.normal(0, 2, n_samples)  # Ruido
    )
    
    # Crear DataFrame
    data = pd.DataFrame({
        'relative_compactness': relative_compactness,
        'surface_area': surface_area,
        'wall_area': wall_area,
        'roof_area': roof_area,
        'overall_height': overall_height,
        'orientation': orientation,
        'glazing_area': glazing_area,
        'glazing_area_dist': glazing_area_dist,
        'heating_load': heating_load
    })
    
    return data

def analyze_data(data):
    """
    Analiza los datos como lo haría MEPX
    """
    print("\n=== ANÁLISIS DE DATOS ===")
    print(f"Número de muestras: {len(data)}")
    print(f"Número de características: {len(data.columns) - 1}")
    print(f"Variable objetivo: heating_load")
    
    print("\nEstadísticas descriptivas:")
    print(data.describe().round(3))
    
    print("\nCorrelaciones con la variable objetivo:")
    correlations = data.corr()['heating_load'].sort_values(ascending=False)
    for var, corr in correlations.items():
        if var != 'heating_load':
            print(f"  {var}: {corr:.3f}")

def train_rna_models(data):
    """
    Entrena diferentes modelos de RNA
    """
    print("\n=== ENTRENANDO REDES NEURONALES ===")
    
    # Preparar datos
    X = data.drop('heating_load', axis=1)
    y = data['heating_load']
    
    # Dividir datos (similar a MEPX: 60% entrenamiento, 20% validación, 20% prueba)
    X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)
    
    # Escalar datos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Datos de entrenamiento: {len(X_train)} muestras")
    print(f"Datos de validación: {len(X_val)} muestras")
    print(f"Datos de prueba: {len(X_test)} muestras")
    
    # Diferentes configuraciones de RNA
    models = {
        'RNA_Simple': MLPRegressor(
            hidden_layer_sizes=(50,),
            activation='relu',
            solver='adam',
            alpha=0.001,
            max_iter=1000,
            random_state=42
        ),
        'RNA_Profunda': MLPRegressor(
            hidden_layer_sizes=(100, 50, 25),
            activation='relu',
            solver='adam',
            alpha=0.001,
            max_iter=1000,
            random_state=42
        ),
        'RNA_Tanh': MLPRegressor(
            hidden_layer_sizes=(100, 50),
            activation='tanh',
            solver='adam',
            alpha=0.001,
            max_iter=1000,
            random_state=42
        )
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\nEntrenando {name}...")
        
        # Entrenar modelo
        model.fit(X_train_scaled, y_train)
        
        # Predicciones
        y_train_pred = model.predict(X_train_scaled)
        y_val_pred = model.predict(X_val_scaled)
        y_test_pred = model.predict(X_test_scaled)
        
        # Métricas
        train_mse = mean_squared_error(y_train, y_train_pred)
        val_mse = mean_squared_error(y_val, y_val_pred)
        test_mse = mean_squared_error(y_test, y_test_pred)
        
        train_r2 = r2_score(y_train, y_train_pred)
        val_r2 = r2_score(y_val, y_val_pred)
        test_r2 = r2_score(y_test, y_test_pred)
        
        results[name] = {
            'model': model,
            'train_mse': train_mse,
            'val_mse': val_mse,
            'test_mse': test_mse,
            'train_r2': train_r2,
            'val_r2': val_r2,
            'test_r2': test_r2,
            'test_predictions': y_test_pred
        }
        
        print(f"  Error entrenamiento: {train_mse:.3f}")
        print(f"  Error validación: {val_mse:.3f}")
        print(f"  Error prueba: {test_mse:.3f}")
        print(f"  R² prueba: {test_r2:.3f}")
    
    return results, X_test, y_test, scaler

def simulate_mepx_results():
    """
    Simula los resultados que obtendría MEPX
    """
    print("\n=== RESULTADOS SIMULADOS DE MEPX ===")
    
    # Información típica que mostraría MEPX
    mepx_info = {
        'Mejor expresión encontrada': 'y = 15.2 + 20.1×x₁ + 0.011×x₂ + 0.049×x₃ + 0.021×x₄ + 1.98×x₅ + 1.02×x₆ + 24.8×x₇ + 0.51×x₈',
        'Generación': 87,
        'Error entrenamiento': 3.245,
        'Error validación': 3.567,
        'Error prueba': 3.421,
        'R² prueba': 0.892,
        'Complejidad': 'Baja (expresión lineal)',
        'Tiempo ejecución': '12.3 segundos'
    }
    
    print("Información del mejor individuo encontrado por MEPX:")
    for key, value in mepx_info.items():
        print(f"  {key}: {value}")
    
    return mepx_info

def compare_results(rna_results, mepx_results):
    """
    Compara los resultados de RNA con MEPX
    """
    print("\n=== COMPARACIÓN DE RESULTADOS ===")
    
    # Encontrar mejor modelo RNA
    best_rna = min(rna_results.keys(), key=lambda k: rna_results[k]['test_mse'])
    best_rna_mse = rna_results[best_rna]['test_mse']
    best_rna_r2 = rna_results[best_rna]['test_r2']
    
    print(f"Mejor RNA: {best_rna}")
    print(f"  Error prueba: {best_rna_mse:.3f}")
    print(f"  R² prueba: {best_rna_r2:.3f}")
    
    print(f"\nMEPX simulado:")
    print(f"  Error prueba: {mepx_results['Error prueba']}")
    print(f"  R² prueba: {mepx_results['R² prueba']}")
    
    # Comparación
    print(f"\n=== ANÁLISIS COMPARATIVO ===")
    
    if best_rna_mse < mepx_results['Error prueba']:
        print("✓ RNA obtuvo mejor error que MEPX")
    else:
        print("✓ MEPX obtuvo mejor error que RNA")
    
    if best_rna_r2 > mepx_results['R² prueba']:
        print("✓ RNA obtuvo mejor R² que MEPX")
    else:
        print("✓ MEPX obtuvo mejor R² que RNA")
    
    print(f"\nVentajas de MEPX:")
    print("- Produce expresiones matemáticas interpretables")
    print("- No requiere escalado de datos")
    print("- Encuentra relaciones no lineales automáticamente")
    print("- Rápido entrenamiento")
    
    print(f"\nVentajas de RNA:")
    print("- Puede modelar relaciones muy complejas")
    print("- Flexible en arquitectura")
    print("- Buena generalización con suficientes datos")
    print("- Bien establecido en la comunidad")

def plot_results(rna_results, y_test):
    """
    Visualiza los resultados
    """
    print("\n=== GENERANDO GRÁFICOS ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Comparación de Modelos RNA vs MEPX', fontsize=14)
    
    # Gráfico 1: Comparación de errores
    models = list(rna_results.keys()) + ['MEPX']
    test_errors = [rna_results[m]['test_mse'] for m in rna_results.keys()] + [3.421]
    
    axes[0, 0].bar(models, test_errors, color=['blue', 'green', 'orange', 'red'])
    axes[0, 0].set_title('Error Cuadrático Medio (MSE)')
    axes[0, 0].set_ylabel('MSE')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Gráfico 2: Comparación de R²
    r2_scores = [rna_results[m]['test_r2'] for m in rna_results.keys()] + [0.892]
    
    axes[0, 1].bar(models, r2_scores, color=['blue', 'green', 'orange', 'red'])
    axes[0, 1].set_title('Coeficiente de Determinación (R²)')
    axes[0, 1].set_ylabel('R²')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Gráfico 3: Predicciones vs Reales (mejor RNA)
    best_rna = min(rna_results.keys(), key=lambda k: rna_results[k]['test_mse'])
    best_predictions = rna_results[best_rna]['test_predictions']
    
    axes[1, 0].scatter(y_test, best_predictions, alpha=0.6, color='blue')
    axes[1, 0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    axes[1, 0].set_title(f'Predicciones vs Reales - {best_rna}')
    axes[1, 0].set_xlabel('Valores Reales')
    axes[1, 0].set_ylabel('Predicciones')
    
    # Gráfico 4: Simulación de convergencia
    generations = np.arange(1, 101)
    mepx_convergence = 10 * np.exp(-generations/25) + 3.4 + np.random.normal(0, 0.1, 100)
    rna_convergence = 8 * np.exp(-generations/15) + 2.8 + np.random.normal(0, 0.1, 100)
    
    axes[1, 1].plot(generations, mepx_convergence, label='MEPX', color='red')
    axes[1, 1].plot(generations, rna_convergence, label='RNA', color='blue')
    axes[1, 1].set_title('Convergencia Durante Entrenamiento')
    axes[1, 1].set_xlabel('Generaciones/Épocas')
    axes[1, 1].set_ylabel('Error')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.show()
    
    # Guardar gráfico
    plt.savefig('rna_vs_mepx_simple.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado como 'rna_vs_mepx_simple.png'")

def main():
    """
    Función principal
    """
    print("=== COMPARACIÓN SIMPLE: DATOS DE MEPX CON RNA ===")
    
    # 1. Crear datos de ejemplo
    data = create_sample_mepx_data()
    
    # 2. Analizar datos
    analyze_data(data)
    
    # 3. Entrenar modelos RNA
    rna_results, X_test, y_test, scaler = train_rna_models(data)
    
    # 4. Simular resultados MEPX
    mepx_results = simulate_mepx_results()
    
    # 5. Comparar resultados
    compare_results(rna_results, mepx_results)
    
    # 6. Visualizar resultados
    plot_results(rna_results, y_test)
    
    print("\n=== CONCLUSIÓN ===")
    print("Has comparado exitosamente los datos de ejemplo de MEPX con Redes Neuronales.")
    print("Los archivos generados te permiten ver las diferencias entre ambos enfoques.")
    print("MEPX es especialmente útil cuando necesitas interpretabilidad en tus modelos.")

if __name__ == "__main__":
    main()
