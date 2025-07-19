"""
Clasificación de Prendas de Vestir con Fashion MNIST
Usando TensorFlow para clasificar 10 tipos de prendas de vestir
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models

def cargar_datos():
    """
    Carga el dataset Fashion MNIST
    """
    print("Cargando Fashion MNIST...")
    
    # Cargar datos
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    
    # Normalizar los datos (0-255 -> 0-1)
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    print(f"Datos de entrenamiento: {x_train.shape}")
    print(f"Datos de prueba: {x_test.shape}")
    
    return (x_train, y_train), (x_test, y_test)

def mostrar_ejemplos(x_train, y_train):
    """
    Muestra ejemplos del dataset
    """
    # Nombres de las clases
    class_names = ['Camiseta', 'Pantalón', 'Suéter', 'Vestido', 'Abrigo',
                   'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Botín']
    
    print(f"\nClases disponibles: {class_names}")
    
    # Mostrar algunas imágenes
    plt.figure(figsize=(12, 8))
    for i in range(15):
        plt.subplot(3, 5, i + 1)
        plt.imshow(x_train[i], cmap='gray')
        plt.title(f'{class_names[y_train[i]]}')
        plt.axis('off')
    
    plt.suptitle('Ejemplos del Dataset Fashion MNIST', fontsize=16)
    plt.tight_layout()
    plt.show()
    plt.savefig('fashion_mnist_ejemplos.png', dpi=300, bbox_inches='tight')
    print("Ejemplos guardados como 'fashion_mnist_ejemplos.png'")

def crear_modelo():
    """
    Crea un modelo de red neuronal simple
    """
    print("\nCreando modelo de red neuronal...")
    
    model = models.Sequential([
        # Aplanar la imagen de 28x28 a 784 píxeles
        layers.Flatten(input_shape=(28, 28)),
        
        # Capa densa con 128 neuronas
        layers.Dense(128, activation='relu'),
        
        # Dropout para evitar overfitting
        layers.Dropout(0.2),
        
        # Capa de salida con 10 neuronas (10 clases)
        layers.Dense(10, activation='softmax')
    ])
    
    # Compilar el modelo
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Modelo creado exitosamente!")
    print(model.summary())
    
    return model

def entrenar_modelo(model, x_train, y_train, x_test, y_test):
    """
    Entrena el modelo
    """
    print("\nEntrenando modelo...")
    
    # Entrenar por 10 épocas
    history = model.fit(
        x_train, y_train,
        epochs=10,
        validation_data=(x_test, y_test),
        verbose=1
    )
    
    print("Entrenamiento completado!")
    return history

def evaluar_modelo(model, x_test, y_test):
    """
    Evalúa el modelo en datos de prueba
    """
    print("\nEvaluando modelo...")
    
    # Evaluar en datos de prueba
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
    
    print(f"Precisión en prueba: {test_accuracy:.4f}")
    print(f"Pérdida en prueba: {test_loss:.4f}")
    
    return test_accuracy, test_loss

def hacer_predicciones(model, x_test, y_test):
    """
    Hace predicciones y muestra algunos resultados
    """
    print("\nHaciendo predicciones...")
    
    # Nombres de las clases
    class_names = ['Camiseta', 'Pantalón', 'Suéter', 'Vestido', 'Abrigo',
                   'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Botín']
    
    # Hacer predicciones
    predictions = model.predict(x_test)
    
    # Mostrar algunas predicciones
    plt.figure(figsize=(15, 10))
    
    for i in range(20):
        plt.subplot(4, 5, i + 1)
        plt.imshow(x_test[i], cmap='gray')
        
        predicted_class = np.argmax(predictions[i])
        true_class = y_test[i]
        
        # Color verde si es correcto, rojo si es incorrecto
        color = 'green' if predicted_class == true_class else 'red'
        
        plt.title(f'Real: {class_names[true_class]}\nPredicción: {class_names[predicted_class]}', 
                 color=color, fontsize=8)
        plt.axis('off')
    
    plt.suptitle('Predicciones del Modelo (Verde=Correcto, Rojo=Incorrecto)', fontsize=16)
    plt.tight_layout()
    plt.show()
    plt.savefig('fashion_mnist_predicciones.png', dpi=300, bbox_inches='tight')
    print("Predicciones guardadas como 'fashion_mnist_predicciones.png'")

def mostrar_historia_entrenamiento(history):
    """
    Muestra gráficos del entrenamiento
    """
    print("\nMostrando historia del entrenamiento...")
    
    # Crear gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Gráfico de precisión
    ax1.plot(history.history['accuracy'], label='Entrenamiento')
    ax1.plot(history.history['val_accuracy'], label='Validación')
    ax1.set_title('Precisión del Modelo')
    ax1.set_xlabel('Época')
    ax1.set_ylabel('Precisión')
    ax1.legend()
    ax1.grid(True)
    
    # Gráfico de pérdida
    ax2.plot(history.history['loss'], label='Entrenamiento')
    ax2.plot(history.history['val_loss'], label='Validación')
    ax2.set_title('Pérdida del Modelo')
    ax2.set_xlabel('Época')
    ax2.set_ylabel('Pérdida')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()
    plt.savefig('fashion_mnist_entrenamiento.png', dpi=300, bbox_inches='tight')
    print("Historia del entrenamiento guardada como 'fashion_mnist_entrenamiento.png'")

def main():
    """
    Función principal
    """
    print("=== CLASIFICACIÓN DE PRENDAS DE VESTIR CON FASHION MNIST ===")
    
    # 1. Cargar datos
    (x_train, y_train), (x_test, y_test) = cargar_datos()
    
    # 2. Mostrar ejemplos
    mostrar_ejemplos(x_train, y_train)
    
    # 3. Crear modelo
    modelo = crear_modelo()
    
    # 4. Entrenar modelo
    history = entrenar_modelo(modelo, x_train, y_train, x_test, y_test)
    
    # 5. Evaluar modelo
    test_accuracy, test_loss = evaluar_modelo(modelo, x_test, y_test)
    
    # 6. Hacer predicciones
    hacer_predicciones(modelo, x_test, y_test)
    
    # 7. Mostrar historia del entrenamiento
    mostrar_historia_entrenamiento(history)
    
    # 8. Guardar modelo
    modelo.save('fashion_mnist_modelo.h5')
    print("\nModelo guardado como 'fashion_mnist_modelo.h5'")
    
    print("\n=== RESUMEN ===")
    print(f"Precisión final: {test_accuracy:.2%}")
    print("Archivos generados:")
    print("- fashion_mnist_ejemplos.png")
    print("- fashion_mnist_predicciones.png")
    print("- fashion_mnist_entrenamiento.png")
    print("- fashion_mnist_modelo.h5")

if __name__ == "__main__":
    main()
