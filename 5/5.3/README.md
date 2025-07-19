# 5.3 - Análisis de Dataset y Diseño de Red Neuronal

## Descripción
Este proyecto realiza un análisis completo del dataset de precios de casas en California, incluyendo análisis de características, diseño de arquitectura neuronal personalizada y análisis de los pesos aprendidos.

## Características del Proyecto

### 1. Análisis de Dataset
- **Dataset**: California Housing Prices
- **Características**: 8 variables predictoras
- **Objetivo**: Predecir el precio de viviendas
- **Análisis estadístico**: Estadísticas descriptivas, correlaciones, distribuciones

### 2. Diseño de Red Neuronal
- **Arquitectura**: Red neuronal densa de 4 capas
- **Capas**: 64, 32, 16, 1 neuronas
- **Activación**: ReLU en capas ocultas
- **Optimizador**: Adam
- **Función de pérdida**: MSE (para regresión)

### 3. Análisis de Pesos
- **Visualización**: Histogramas y heatmaps de pesos
- **Análisis**: Importancia de características basada en pesos
- **Estadísticas**: Distribución de pesos por capa

### 4. Ejemplos de Predicción
- **Predicciones**: Casos de prueba con valores reales vs predichos
- **Métricas**: R², MAE, RMSE
- **Visualización**: Comparación de resultados

## Archivos Generados

### Scripts
- `dataset_neural_network.py` - Script principal del análisis

### Visualizaciones
- `distribucion_caracteristicas.png` - Distribución de variables
- `matriz_correlacion.png` - Matriz de correlaciones
- `arquitectura_neuronal.png` - Diagrama de la red neuronal
- `historial_entrenamiento.png` - Pérdida durante entrenamiento
- `pesos_por_capa.png` - Distribución de pesos por capa
- `heatmap_pesos.png` - Mapa de calor de pesos
- `importancia_caracteristicas.png` - Importancia de características

### Modelos y Resultados
- `modelo_precios_casas.h5` - Modelo entrenado guardado
- `metricas_evaluacion.csv` - Métricas de evaluación
- `importancia_caracteristicas.csv` - Ranking de características
- `ejemplos_prediccion.csv` - Ejemplos de predicciones

## Instalación

### Opción 1: Usando pip
```bash
pip install -r requirements.txt
```

### Opción 2: Instalación manual
```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
```

## Uso

### Ejecutar análisis completo
```bash
python dataset_neural_network.py
```

Este comando ejecutará:
1. Carga y análisis del dataset
2. Visualización de características
3. Diseño y entrenamiento de la red neuronal
4. Análisis de pesos aprendidos
5. Ejemplos de predicción
6. Guardado del modelo

## Resultados Esperados

### Rendimiento del Modelo
- **R² Score**: ~0.60-0.70 (varía según ejecución)
- **MAE**: ~$50,000-60,000 (error promedio)
- **RMSE**: ~$70,000-80,000

### Características Más Importantes
Basado en el análisis de pesos:
1. **MedInc** (Ingreso medio)
2. **AveOccup** (Ocupación promedio)
3. **HouseAge** (Edad de la casa)
4. **AveRooms** (Habitaciones promedio)

## Estructura del Código

### Clases Principales
- `DatasetAnalyzer`: Análisis exploratorio de datos
- `NeuralNetworkDesigner`: Diseño y entrenamiento de la red
- `WeightAnalyzer`: Análisis de pesos aprendidos

### Funciones Auxiliares
- `hacer_ejemplos_prediccion()`: Genera ejemplos de predicción
- `main()`: Función principal que coordina todo el análisis

## Visualizaciones Clave

### 1. Análisis de Datos
- Distribución de cada característica
- Matriz de correlaciones entre variables
- Estadísticas descriptivas

### 2. Arquitectura Neuronal
- Diagrama de la red neuronal
- Número de parámetros por capa
- Historial de entrenamiento

### 3. Análisis de Pesos
- Distribución de pesos por capa
- Importancia de características
- Visualización de conectividad

## Notas Técnicas

- **Normalización**: Se aplica StandardScaler a todas las características
- **División de datos**: 80% entrenamiento, 20% prueba
- **Épocas**: 50 épocas de entrenamiento
- **Validación**: 20% de datos de entrenamiento para validación
- **Métricas**: Se calculan múltiples métricas para evaluación completa

## Personalización

El código está diseñado para ser fácilmente modificable:
- Cambiar arquitectura de la red en `disenar_arquitectura()`
- Modificar hiperparámetros en `entrenar_modelo()`
- Ajustar visualizaciones en cada clase

## Autor
Análisis de Dataset y Diseño de Red Neuronal - Proyecto 5.3
