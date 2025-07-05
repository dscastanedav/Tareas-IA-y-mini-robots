"""
Script simplificado para mostrar los 10 ejemplos específicos de aproximación
"""
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

def main():
    print("="*60)
    print("EJEMPLO SIMPLE: 10 CASOS DE APROXIMACIÓN DE RAÍZ CUADRADA")
    print("="*60)
    
    # Generar dataset más pequeño
    np.random.seed(42)  # Para reproducibilidad
    X = np.random.uniform(1, 100, 200).reshape(-1, 1)
    y = np.sqrt(X.flatten())
    
    # Entrenar modelo neuronal simple
    modelo = MLPRegressor(
        hidden_layer_sizes=(20, 10),
        max_iter=500,
        random_state=42,
        alpha=0.1
    )
    
    # Usar 80% para entrenamiento
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    
    modelo.fit(X_train, y_train)
    
    # Seleccionar 10 ejemplos específicos
    ejemplos_X = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    
    print("\nComparación de la función real vs el modelo entrenado:")
    print("-" * 60)
    print(f"{'Valor X':>8} {'Real sqrt(x)':>12} {'Modelo ML':>12} {'Error':>10}")
    print("-" * 60)
    
    for x in ejemplos_X:
        real_sqrt = np.sqrt(x)
        modelo_sqrt = modelo.predict([[x]])[0]
        error = abs(real_sqrt - modelo_sqrt)
        
        print(f"{x:8.0f} {real_sqrt:12.4f} {modelo_sqrt:12.4f} {error:10.4f}")
    
    print("-" * 60)
    print("\nObservaciones:")
    print("- El modelo neuronal aprende a aproximar la función raíz cuadrada")
    print("- Los errores son pequeños para la mayoría de valores")
    print("- El modelo funciona mejor en el rango de entrenamiento")
    print("- Para valores muy grandes puede haber más error")

if __name__ == "__main__":
    main()
