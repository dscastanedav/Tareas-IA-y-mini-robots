"""
Script Simple para Usar el Modelo Entrenado de Fashion MNIST
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def cargar_modelo_y_datos():
    """
    Carga el modelo entrenado y datos de prueba
    """
    print("Cargando modelo entrenado...")
    modelo = tf.keras.models.load_model('fashion_mnist_modelo.h5')
    
    print("Cargando datos de prueba...")
    (_, _), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    x_test = x_test.astype('float32') / 255.0
    
    return modelo, x_test, y_test

def predecir_imagen(modelo, imagen, indice_real):
    """
    Predice una sola imagen
    """
    class_names = ['Camiseta', 'Pantalón', 'Suéter', 'Vestido', 'Abrigo',
                   'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Botín']
    
    # Hacer predicción
    prediccion = modelo.predict(imagen.reshape(1, 28, 28))
    clase_predicha = np.argmax(prediccion)
    confianza = np.max(prediccion) * 100
    
    # Mostrar resultado
    plt.figure(figsize=(6, 6))
    plt.imshow(imagen, cmap='gray')
    plt.title(f'Real: {class_names[indice_real]}\n'
              f'Predicción: {class_names[clase_predicha]}\n'
              f'Confianza: {confianza:.1f}%')
    plt.axis('off')
    plt.show()
    
    print(f"Clase real: {class_names[indice_real]}")
    print(f"Clase predicha: {class_names[clase_predicha]}")
    print(f"Confianza: {confianza:.1f}%")
    
    return clase_predicha, confianza

def main():
    """
    Función principal - ejemplo simple
    """
    print("=== PREDICTOR SIMPLE DE FASHION MNIST ===")
    
    # Cargar modelo y datos
    modelo, x_test, y_test = cargar_modelo_y_datos()
    
    # Elegir una imagen aleatoria
    indice = np.random.randint(0, len(x_test))
    imagen = x_test[indice]
    etiqueta_real = y_test[indice]
    
    print(f"\nProbando con imagen #{indice}")
    
    # Hacer predicción
    predecir_imagen(modelo, imagen, etiqueta_real)

if __name__ == "__main__":
    main()
