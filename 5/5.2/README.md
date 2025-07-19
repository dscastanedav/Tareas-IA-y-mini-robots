# Clasificación de Prendas de Vestir - Fashion MNIST

## Descripción
Este proyecto usa TensorFlow para clasificar 10 tipos de prendas de vestir del dataset Fashion MNIST. Es una implementación simple y directa que logra ~88% de precisión.

## 👕 Clases de Prendas
0. **Camiseta** - T-shirt/top
1. **Pantalón** - Trouser  
2. **Suéter** - Pullover
3. **Vestido** - Dress
4. **Abrigo** - Coat
5. **Sandalia** - Sandal
6. **Camisa** - Shirt
7. **Zapatilla** - Sneaker
8. **Bolso** - Bag
9. **Botín** - Ankle boot

## 🚀 Instalación Rápida
```bash
pip install tensorflow numpy matplotlib
```

## 📋 Uso

### Entrenar el modelo:
```bash
python fashion_mnist_classifier.py
```

### Usar modelo entrenado:
```bash
python predictor_simple.py
```

## 📊 Características del Modelo
- **Arquitectura**: Red neuronal simple (Flatten + Dense + Dropout)
- **Parámetros**: 101,770 parámetros entrenables
- **Optimizador**: Adam
- **Función de pérdida**: Sparse categorical crossentropy
- **Épocas**: 10
- **Precisión obtenida**: 88.00%

## 📁 Archivos Generados
- `fashion_mnist_ejemplos.png` - Ejemplos del dataset con etiquetas
- `fashion_mnist_predicciones.png` - Predicciones del modelo (verde=correcto, rojo=incorrecto)
- `fashion_mnist_entrenamiento.png` - Gráficos de pérdida y precisión durante entrenamiento
- `fashion_mnist_modelo.h5` - Modelo entrenado guardado

## 📈 Resultados Obtenidos
- **Precisión final**: 88.00%
- **Tiempo de entrenamiento**: ~3 minutos
- **Dataset**: 60,000 imágenes de entrenamiento, 10,000 de prueba
- **Tamaño de imagen**: 28x28 píxeles en escala de grises

## 🔧 Estructura del Proyecto
```
5.2/
├── fashion_mnist_classifier.py    # Script principal
├── predictor_simple.py           # Predictor con modelo guardado
├── requirements.txt              # Dependencias
├── README.md                     # Esta documentación
├── fashion_mnist_modelo.h5       # Modelo entrenado
└── *.png                        # Gráficos generados
```

## 🎯 Próximos Pasos
- Probar con redes convolucionales (CNN)
- Aumentar datos (data augmentation)
- Ajustar hiperparámetros
- Usar transfer learning
