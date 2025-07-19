"""
Ejemplo Simple: Aproximar una Función Matemática con Machine Learning
Función elegida: Raíz Cuadrada
Comparación entre modelo ML y función real
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

def generar_dataset(n_puntos=1000):
    """
    Genera un dataset para la función raíz cuadrada
    """
    print("=== GENERANDO DATASET PARA RAÍZ CUADRADA ===")
    
    # Generar valores de entrada (x) entre 0 y 100
    np.random.seed(42)
    x = np.random.uniform(0, 100, n_puntos)
    
    # Calcular la raíz cuadrada (y = √x)
    y = np.sqrt(x)
    
    # Agregar un poco de ruido para simular datos reales
    ruido = np.random.normal(0, 0.1, n_puntos)
    y_con_ruido = y + ruido
    
    print(f"Dataset generado con {n_puntos} puntos")
    print(f"Rango de entrada (x): {x.min():.2f} - {x.max():.2f}")
    print(f"Rango de salida (y): {y_con_ruido.min():.2f} - {y_con_ruido.max():.2f}")
    
    return x, y_con_ruido, y

def entrenar_modelo(x, y):
    """
    Entrena un modelo de Machine Learning para aproximar la función
    """
    print("\n=== ENTRENANDO MODELO DE ML ===")
    
    # Preparar datos (sklearn espera arrays 2D)
    X = x.reshape(-1, 1)
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Crear y entrenar el modelo (Random Forest)
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    
    # Evaluar el modelo
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"Modelo entrenado exitosamente!")
    print(f"Datos de entrenamiento: {len(X_train)} puntos")
    print(f"Datos de prueba: {len(X_test)} puntos")
    print(f"Error cuadrático medio: {mse:.4f}")
    
    return modelo

def comparar_resultados(modelo, valores_prueba):
    """
    Compara los resultados del modelo ML con la función real
    """
    print("\n=== COMPARACIÓN: MODELO ML vs FUNCIÓN REAL ===")
    print(f"{'Valor':<8} {'ML':<10} {'Real':<10} {'Error':<10} {'Error %':<10}")
    print("-" * 55)
    
    errores = []
    
    for valor in valores_prueba:
        # Predicción del modelo ML
        prediccion_ml = modelo.predict([[valor]])[0]
        
        # Cálculo real de la función
        valor_real = math.sqrt(valor)
        
        # Calcular error
        error_absoluto = abs(prediccion_ml - valor_real)
        error_porcentual = (error_absoluto / valor_real) * 100
        
        errores.append(error_absoluto)
        
        print(f"{valor:<8.1f} {prediccion_ml:<10.3f} {valor_real:<10.3f} "
              f"{error_absoluto:<10.3f} {error_porcentual:<10.2f}%")
    
    # Estadísticas de error
    error_promedio = np.mean(errores)
    error_maximo = np.max(errores)
    
    print("-" * 55)
    print(f"Error promedio: {error_promedio:.4f}")
    print(f"Error máximo: {error_maximo:.4f}")
    
    return errores

def visualizar_resultados(x, y_real, modelo, valores_prueba):
    """
    Crea visualizaciones de los resultados
    """
    print("\n=== GENERANDO VISUALIZACIONES ===")
    
    # Crear puntos para la gráfica
    x_grafica = np.linspace(0, 100, 1000)
    y_real_grafica = np.sqrt(x_grafica)
    y_ml_grafica = modelo.predict(x_grafica.reshape(-1, 1))
    
    # Crear figura con 2 subgráficas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfica 1: Comparación de funciones
    ax1.plot(x_grafica, y_real_grafica, 'b-', label='Función Real (√x)', linewidth=2)
    ax1.plot(x_grafica, y_ml_grafica, 'r--', label='Modelo ML', linewidth=2)
    ax1.scatter(x[:100], y_real[:100], alpha=0.3, s=10, c='gray', label='Datos de entrenamiento')
    ax1.set_xlabel('x')
    ax1.set_ylabel('√x')
    ax1.set_title('Comparación: Función Real vs Modelo ML')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfica 2: Puntos de prueba específicos
    predicciones_prueba = [modelo.predict([[x]])[0] for x in valores_prueba]
    valores_reales_prueba = [math.sqrt(x) for x in valores_prueba]
    
    ax2.scatter(valores_prueba, valores_reales_prueba, c='blue', s=100, 
                label='Función Real', marker='o')
    ax2.scatter(valores_prueba, predicciones_prueba, c='red', s=100, 
                label='Modelo ML', marker='x')
    
    # Líneas conectando los puntos
    for i in range(len(valores_prueba)):
        ax2.plot([valores_prueba[i], valores_prueba[i]], 
                [valores_reales_prueba[i], predicciones_prueba[i]], 
                'k--', alpha=0.5)
    
    ax2.set_xlabel('Valor de entrada (x)')
    ax2.set_ylabel('Salida (√x)')
    ax2.set_title('Comparación en 10 Puntos de Prueba')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('funcion_matematica_ml.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Visualización guardada como 'funcion_matematica_ml.png'")

def main():
    """
    Función principal que ejecuta todo el proceso
    """
    print("=== APROXIMACIÓN DE FUNCIÓN MATEMÁTICA CON ML ===")
    print("Función objetivo: Raíz Cuadrada (√x)")
    print()
    
    # 1. Generar dataset
    x, y_con_ruido, y_real = generar_dataset(1000)
    
    # 2. Entrenar modelo
    modelo = entrenar_modelo(x, y_con_ruido)
    
    # 3. Definir 10 valores de prueba
    valores_prueba = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(f"\nValores de prueba seleccionados: {valores_prueba}")
    
    # 4. Comparar resultados
    errores = comparar_resultados(modelo, valores_prueba)
    
    # 5. Crear visualizaciones
    visualizar_resultados(x, y_real, modelo, valores_prueba)
    
    # 6. Resumen final
    print(f"\n=== RESUMEN FINAL ===")
    print(f"✓ Dataset generado: 1000 puntos")
    print(f"✓ Modelo entrenado: Random Forest")
    print(f"✓ Precisión promedio: {(1 - np.mean(errores)/np.mean([math.sqrt(v) for v in valores_prueba]))*100:.1f}%")
    print(f"✓ El modelo puede aproximar la función √x con buena precisión")
    print(f"✓ Visualización guardada como 'funcion_matematica_ml.png'")

if __name__ == "__main__":
    main()
