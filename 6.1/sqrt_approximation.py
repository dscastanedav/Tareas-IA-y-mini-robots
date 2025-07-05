"""
Ejemplo simple de ML para aproximar la función raíz cuadrada
Este script genera un dataset, entrena un modelo y compara los resultados
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def generar_dataset(n_samples=1000, max_value=100):
    """
    Genera un dataset con valores x y sus raíces cuadradas
    """
    # Generar valores x aleatorios entre 0 y max_value
    x = np.random.uniform(0, max_value, n_samples)
    # Calcular las raíces cuadradas reales
    y = np.sqrt(x)
    
    return x.reshape(-1, 1), y

def entrenar_modelo_lineal(X_train, y_train):
    """
    Entrena un modelo de regresión lineal
    """
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    return modelo

def entrenar_modelo_neuronal(X_train, y_train):
    """
    Entrena una red neuronal simple
    """
    modelo = MLPRegressor(
        hidden_layer_sizes=(50, 30),
        max_iter=1000,
        random_state=42,
        alpha=0.01
    )
    modelo.fit(X_train, y_train)
    return modelo

def evaluar_modelo(modelo, X_test, y_test):
    """
    Evalúa el modelo y retorna métricas
    """
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return y_pred, mse, r2

def comparar_resultados(X_test, y_test, y_pred_lineal, y_pred_neuronal, n_ejemplos=10):
    """
    Compara los resultados de ambos modelos con la función real
    """
    print("\n" + "="*80)
    print("COMPARACIÓN DE RESULTADOS (10 ejemplos)")
    print("="*80)
    print(f"{'Valor X':>10} {'Real sqrt(x)':>15} {'Modelo Lineal':>15} {'Red Neuronal':>15} {'Error Lineal':>15} {'Error Neuronal':>15}")
    print("-" * 95)
    
    # Tomar los primeros n_ejemplos para comparar
    for i in range(min(n_ejemplos, len(X_test))):
        x_val = X_test[i][0]
        real_val = y_test[i]
        pred_lineal = y_pred_lineal[i]
        pred_neuronal = y_pred_neuronal[i]
        
        error_lineal = abs(real_val - pred_lineal)
        error_neuronal = abs(real_val - pred_neuronal)
        
        print(f"{x_val:10.2f} {real_val:15.4f} {pred_lineal:15.4f} {pred_neuronal:15.4f} {error_lineal:15.4f} {error_neuronal:15.4f}")

def crear_graficos(X_test, y_test, y_pred_lineal, y_pred_neuronal):
    """
    Crea gráficos comparativos
    """
    # Ordenar los datos para una mejor visualización
    indices = np.argsort(X_test.flatten())
    X_sorted = X_test[indices]
    y_test_sorted = y_test[indices]
    y_pred_lineal_sorted = y_pred_lineal[indices]
    y_pred_neuronal_sorted = y_pred_neuronal[indices]
    
    plt.figure(figsize=(12, 8))
    
    # Subplot 1: Comparación de predicciones
    plt.subplot(2, 2, 1)
    plt.scatter(X_sorted, y_test_sorted, alpha=0.5, label='Real', color='blue', s=10)
    plt.plot(X_sorted, y_pred_lineal_sorted, 'r-', label='Regresión Lineal', linewidth=2)
    plt.plot(X_sorted, y_pred_neuronal_sorted, 'g-', label='Red Neuronal', linewidth=2)
    plt.xlabel('Valor X')
    plt.ylabel('sqrt(X)')
    plt.title('Comparación de Modelos vs Función Real')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 2: Errores del modelo lineal
    plt.subplot(2, 2, 2)
    errores_lineal = np.abs(y_test_sorted - y_pred_lineal_sorted)
    plt.scatter(X_sorted, errores_lineal, alpha=0.6, color='red', s=10)
    plt.xlabel('Valor X')
    plt.ylabel('Error Absoluto')
    plt.title('Errores - Regresión Lineal')
    plt.grid(True, alpha=0.3)
    
    # Subplot 3: Errores de la red neuronal
    plt.subplot(2, 2, 3)
    errores_neuronal = np.abs(y_test_sorted - y_pred_neuronal_sorted)
    plt.scatter(X_sorted, errores_neuronal, alpha=0.6, color='green', s=10)
    plt.xlabel('Valor X')
    plt.ylabel('Error Absoluto')
    plt.title('Errores - Red Neuronal')
    plt.grid(True, alpha=0.3)
    
    # Subplot 4: Comparación de errores
    plt.subplot(2, 2, 4)
    plt.hist(errores_lineal, bins=30, alpha=0.7, label='Regresión Lineal', color='red')
    plt.hist(errores_neuronal, bins=30, alpha=0.7, label='Red Neuronal', color='green')
    plt.xlabel('Error Absoluto')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de Errores')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('c:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/6.1/comparacion_modelos.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """
    Función principal que ejecuta todo el proceso
    """
    print("="*80)
    print("EJEMPLO DE ML: APROXIMACIÓN DE LA FUNCIÓN RAÍZ CUADRADA")
    print("="*80)
    
    # 1. Generar dataset
    print("\n1. Generando dataset...")
    X, y = generar_dataset(n_samples=2000, max_value=100)
    print(f"   Dataset generado: {len(X)} muestras")
    print(f"   Rango de valores X: {X.min():.2f} - {X.max():.2f}")
    print(f"   Rango de valores Y: {y.min():.2f} - {y.max():.2f}")
    
    # 2. Dividir en entrenamiento y prueba
    print("\n2. Dividiendo dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"   Entrenamiento: {len(X_train)} muestras")
    print(f"   Prueba: {len(X_test)} muestras")
    
    # 3. Entrenar modelos
    print("\n3. Entrenando modelos...")
    print("   Entrenando regresión lineal...")
    modelo_lineal = entrenar_modelo_lineal(X_train, y_train)
    
    print("   Entrenando red neuronal...")
    modelo_neuronal = entrenar_modelo_neuronal(X_train, y_train)
    
    # 4. Evaluar modelos
    print("\n4. Evaluando modelos...")
    y_pred_lineal, mse_lineal, r2_lineal = evaluar_modelo(modelo_lineal, X_test, y_test)
    y_pred_neuronal, mse_neuronal, r2_neuronal = evaluar_modelo(modelo_neuronal, X_test, y_test)
    
    print(f"\n   REGRESIÓN LINEAL:")
    print(f"   - Error Cuadrático Medio: {mse_lineal:.4f}")
    print(f"   - R² Score: {r2_lineal:.4f}")
    
    print(f"\n   RED NEURONAL:")
    print(f"   - Error Cuadrático Medio: {mse_neuronal:.4f}")
    print(f"   - R² Score: {r2_neuronal:.4f}")
    
    # 5. Comparar resultados en 10 ejemplos
    comparar_resultados(X_test, y_test, y_pred_lineal, y_pred_neuronal, n_ejemplos=10)
    
    # 6. Crear gráficos
    print("\n5. Creando gráficos comparativos...")
    crear_graficos(X_test, y_test, y_pred_lineal, y_pred_neuronal)
    print("   Gráficos guardados como 'comparacion_modelos.png'")
    
    # 7. Guardar modelos (opcional)
    print("\n6. Proceso completado exitosamente!")
    print("   - Dataset generado y procesado")
    print("   - Dos modelos entrenados (Regresión Lineal y Red Neuronal)")
    print("   - Comparación de resultados realizada")
    print("   - Gráficos generados y guardados")
    
    # Mostrar cuál modelo es mejor
    if mse_neuronal < mse_lineal:
        print(f"\n   🏆 GANADOR: Red Neuronal (MSE: {mse_neuronal:.4f} vs {mse_lineal:.4f})")
    else:
        print(f"\n   🏆 GANADOR: Regresión Lineal (MSE: {mse_lineal:.4f} vs {mse_neuronal:.4f})")

if __name__ == "__main__":
    main()
