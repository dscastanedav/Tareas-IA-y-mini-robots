"""
Análisis de Dataset y Diseño de Red Neuronal
Dataset: Precios de Casas en California
Análisis de características y diseño de arquitectura neuronal personalizada
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf
from tensorflow.keras import layers, models
import warnings
warnings.filterwarnings('ignore')

class DatasetAnalyzer:
    """
    Clase para analizar el dataset y sus características
    """
    
    def __init__(self):
        self.data = None
        self.df = None
        self.scaler = StandardScaler()
        
    def cargar_dataset(self):
        """
        Carga el dataset de precios de casas en California
        """
        print("=== CARGANDO DATASET DE PRECIOS DE CASAS ===")
        
        # Cargar dataset
        self.data = fetch_california_housing()
        
        # Crear DataFrame para análisis
        self.df = pd.DataFrame(self.data.data, columns=self.data.feature_names)
        self.df['PRECIO'] = self.data.target
        
        print(f"Dataset cargado exitosamente!")
        print(f"Forma del dataset: {self.df.shape}")
        print(f"Número de características: {len(self.data.feature_names)}")
        
        return self.df
    
    def analizar_caracteristicas(self):
        """
        Analiza las características del dataset
        """
        print("\n=== ANÁLISIS DE CARACTERÍSTICAS ===")
        
        # Información básica
        print("\n1. INFORMACIÓN BÁSICA:")
        print(self.df.info())
        
        # Estadísticas descriptivas
        print("\n2. ESTADÍSTICAS DESCRIPTIVAS:")
        print(self.df.describe().round(2))
        
        # Significado de cada característica
        print("\n3. SIGNIFICADO DE LAS CARACTERÍSTICAS:")
        caracteristicas = {
            'MedInc': 'Ingreso medio del hogar (en decenas de miles de $)',
            'HouseAge': 'Edad media de la casa (años)',
            'AveRooms': 'Número promedio de habitaciones por hogar',
            'AveBedrms': 'Número promedio de dormitorios por hogar', 
            'Population': 'Población del área',
            'AveOccup': 'Ocupación promedio (personas por hogar)',
            'Latitude': 'Latitud (ubicación geográfica)',
            'Longitude': 'Longitud (ubicación geográfica)',
            'PRECIO': 'Precio medio de la casa (en cientos de miles de $)'
        }
        
        for feature, descripcion in caracteristicas.items():
            if feature in self.df.columns:
                valor_min = self.df[feature].min()
                valor_max = self.df[feature].max()
                valor_med = self.df[feature].mean()
                print(f"  • {feature}: {descripcion}")
                print(f"    Rango: {valor_min:.2f} - {valor_max:.2f}, Media: {valor_med:.2f}")
        
        return caracteristicas
    
    def visualizar_dataset(self):
        """
        Crea visualizaciones del dataset
        """
        print("\n=== GENERANDO VISUALIZACIONES ===")
        
        # Configurar estilo
        plt.style.use('default')
        sns.set_palette("husl")
        
        # Crear figura con subplots
        fig, axes = plt.subplots(3, 3, figsize=(15, 12))
        fig.suptitle('Análisis del Dataset de Precios de Casas en California', fontsize=16)
        
        # 1. Distribución del precio (variable objetivo)
        axes[0, 0].hist(self.df['PRECIO'], bins=50, alpha=0.7, color='skyblue')
        axes[0, 0].set_title('Distribución de Precios')
        axes[0, 0].set_xlabel('Precio (cientos de miles $)')
        axes[0, 0].set_ylabel('Frecuencia')
        
        # 2. Correlación con el precio
        correlaciones = self.df.corr()['PRECIO'].sort_values(ascending=False)[1:-1]
        axes[0, 1].barh(range(len(correlaciones)), correlaciones.values)
        axes[0, 1].set_yticks(range(len(correlaciones)))
        axes[0, 1].set_yticklabels(correlaciones.index)
        axes[0, 1].set_title('Correlación con el Precio')
        axes[0, 1].set_xlabel('Correlación')
        
        # 3. Mapa de calor de correlaciones
        correlation_matrix = self.df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                   square=True, ax=axes[0, 2])
        axes[0, 2].set_title('Matriz de Correlaciones')
        
        # 4-8. Distribuciones de características principales
        features_principales = ['MedInc', 'HouseAge', 'AveRooms', 'Population', 'Latitude']
        
        for i, feature in enumerate(features_principales):
            row = (i + 3) // 3
            col = (i + 3) % 3
            axes[row, col].hist(self.df[feature], bins=30, alpha=0.7)
            axes[row, col].set_title(f'Distribución de {feature}')
            axes[row, col].set_ylabel('Frecuencia')
        
        # 9. Precio vs Ingreso Medio (relación más fuerte)
        axes[2, 2].scatter(self.df['MedInc'], self.df['PRECIO'], alpha=0.5)
        axes[2, 2].set_title('Precio vs Ingreso Medio')
        axes[2, 2].set_xlabel('Ingreso Medio')
        axes[2, 2].set_ylabel('Precio')
        
        plt.tight_layout()
        plt.savefig('analisis_dataset.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Visualizaciones guardadas como 'analisis_dataset.png'")
    
    def analizar_valores_atipicos(self):
        """
        Analiza valores atípicos en el dataset
        """
        print("\n=== ANÁLISIS DE VALORES ATÍPICOS ===")
        
        # Detectar valores atípicos usando IQR
        valores_atipicos = {}
        
        for columna in self.df.select_dtypes(include=[np.number]).columns:
            Q1 = self.df[columna].quantile(0.25)
            Q3 = self.df[columna].quantile(0.75)
            IQR = Q3 - Q1
            
            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR
            
            atipicos = self.df[(self.df[columna] < limite_inferior) | 
                              (self.df[columna] > limite_superior)][columna]
            
            valores_atipicos[columna] = len(atipicos)
            porcentaje = (len(atipicos) / len(self.df)) * 100
            
            print(f"  • {columna}: {len(atipicos)} valores atípicos ({porcentaje:.1f}%)")
        
        return valores_atipicos

class NeuralNetworkDesigner:
    """
    Clase para diseñar y entrenar la red neuronal
    """
    
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.model = None
        self.history = None
        self.scaler = StandardScaler()
        
    def preparar_datos(self, test_size=0.2, val_size=0.2):
        """
        Prepara los datos para entrenamiento
        """
        print("\n=== PREPARANDO DATOS ===")
        
        # Dividir en entrenamiento y prueba
        X_temp, self.X_test, y_temp, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=42
        )
        
        # Dividir entrenamiento en entrenamiento y validación
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(
            X_temp, y_temp, test_size=val_size, random_state=42
        )
        
        # Normalizar los datos
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_val_scaled = self.scaler.transform(self.X_val)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"Datos de entrenamiento: {self.X_train_scaled.shape}")
        print(f"Datos de validación: {self.X_val_scaled.shape}")
        print(f"Datos de prueba: {self.X_test_scaled.shape}")
        
        # Mostrar estadísticas de normalización
        print(f"\nEstadísticas después de normalización:")
        print(f"Media de entrenamiento: {self.X_train_scaled.mean():.3f}")
        print(f"Desviación estándar de entrenamiento: {self.X_train_scaled.std():.3f}")
    
    def disenar_arquitectura(self):
        """
        Diseña la arquitectura de la red neuronal
        """
        print("\n=== DISEÑANDO ARQUITECTURA DE RED NEURONAL ===")
        
        # Obtener número de características
        n_features = self.X_train_scaled.shape[1]
        
        print(f"Número de características de entrada: {n_features}")
        print("\nDiseño de la arquitectura:")
        
        # Crear modelo secuencial
        self.model = models.Sequential([
            # Capa de entrada
            layers.Dense(64, activation='relu', input_shape=(n_features,), name='entrada'),
            layers.BatchNormalization(name='batch_norm_1'),
            layers.Dropout(0.3, name='dropout_1'),
            
            # Segunda capa oculta
            layers.Dense(32, activation='relu', name='oculta_1'),
            layers.BatchNormalization(name='batch_norm_2'),
            layers.Dropout(0.2, name='dropout_2'),
            
            # Tercera capa oculta
            layers.Dense(16, activation='relu', name='oculta_2'),
            layers.Dropout(0.1, name='dropout_3'),
            
            # Capa de salida (regresión)
            layers.Dense(1, activation='linear', name='salida')
        ])
        
        # Compilar modelo
        self.model.compile(
            optimizer='adam',
            loss='mse',
            metrics=['mae']
        )
        
        print("\nArquitectura diseñada:")
        print("  1. Entrada: 64 neuronas + BatchNorm + Dropout(0.3)")
        print("  2. Oculta 1: 32 neuronas + BatchNorm + Dropout(0.2)")
        print("  3. Oculta 2: 16 neuronas + Dropout(0.1)")
        print("  4. Salida: 1 neurona (regresión)")
        
        print(f"\nResumen del modelo:")
        self.model.summary()
        
        return self.model
    
    def entrenar_modelo(self, epochs=100):
        """
        Entrena el modelo
        """
        print(f"\n=== ENTRENANDO MODELO ({epochs} ÉPOCAS) ===")
        
        # Callbacks para mejorar el entrenamiento
        callbacks = [
            tf.keras.callbacks.EarlyStopping(
                monitor='val_loss',
                patience=15,
                restore_best_weights=True
            ),
            tf.keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=10,
                min_lr=1e-7
            )
        ]
        
        # Entrenar
        self.history = self.model.fit(
            self.X_train_scaled, self.y_train,
            validation_data=(self.X_val_scaled, self.y_val),
            epochs=epochs,
            batch_size=32,
            callbacks=callbacks,
            verbose=1
        )
        
        print("\nEntrenamiento completado!")
        
        return self.history
    
    def evaluar_modelo(self):
        """
        Evalúa el modelo en datos de prueba
        """
        print("\n=== EVALUANDO MODELO ===")
        
        # Predicciones
        y_pred = self.model.predict(self.X_test_scaled)
        
        # Métricas
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, y_pred)
        mae = np.mean(np.abs(self.y_test - y_pred.flatten()))
        
        print(f"Métricas en datos de prueba:")
        print(f"  • MSE (Error Cuadrático Medio): {mse:.4f}")
        print(f"  • RMSE (Raíz del MSE): {rmse:.4f}")
        print(f"  • MAE (Error Absoluto Medio): {mae:.4f}")
        print(f"  • R² (Coef. Determinación): {r2:.4f}")
        
        return {'mse': mse, 'rmse': rmse, 'mae': mae, 'r2': r2, 'predictions': y_pred}

class WeightAnalyzer:
    """
    Clase para analizar los pesos aprendidos
    """
    
    def __init__(self, model, feature_names):
        self.model = model
        self.feature_names = feature_names
    
    def analizar_pesos(self):
        """
        Analiza los pesos aprendidos por la red
        """
        print("\n=== ANÁLISIS DE PESOS APRENDIDOS ===")
        
        # Obtener pesos de la primera capa
        primera_capa = self.model.get_layer('entrada')
        pesos, sesgos = primera_capa.get_weights()
        
        print(f"Forma de la matriz de pesos: {pesos.shape}")
        print(f"Número de sesgos: {len(sesgos)}")
        
        # Analizar importancia de características
        importancia_features = np.abs(pesos).mean(axis=1)
        
        # Crear DataFrame para análisis
        importancia_df = pd.DataFrame({
            'Característica': self.feature_names,
            'Importancia': importancia_features
        }).sort_values('Importancia', ascending=False)
        
        print(f"\nImportancia de características (basada en pesos):")
        for idx, row in importancia_df.iterrows():
            print(f"  {row['Característica']:12}: {row['Importancia']:.4f}")
        
        return pesos, sesgos, importancia_df
    
    def visualizar_pesos(self, pesos, importancia_df):
        """
        Visualiza los pesos aprendidos
        """
        print("\n=== VISUALIZANDO PESOS ===")
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Análisis de Pesos Aprendidos por la Red Neuronal', fontsize=16)
        
        # 1. Importancia de características
        axes[0, 0].barh(importancia_df['Característica'], importancia_df['Importancia'])
        axes[0, 0].set_title('Importancia de Características')
        axes[0, 0].set_xlabel('Importancia Promedio')
        
        # 2. Distribución de pesos
        axes[0, 1].hist(pesos.flatten(), bins=50, alpha=0.7)
        axes[0, 1].set_title('Distribución de Todos los Pesos')
        axes[0, 1].set_xlabel('Valor del Peso')
        axes[0, 1].set_ylabel('Frecuencia')
        
        # 3. Mapa de calor de pesos (primera capa)
        im = axes[1, 0].imshow(pesos.T, cmap='RdBu', aspect='auto')
        axes[1, 0].set_title('Mapa de Calor de Pesos (Primera Capa)')
        axes[1, 0].set_xlabel('Características')
        axes[1, 0].set_ylabel('Neuronas')
        axes[1, 0].set_xticks(range(len(self.feature_names)))
        axes[1, 0].set_xticklabels(self.feature_names, rotation=45)
        plt.colorbar(im, ax=axes[1, 0])
        
        # 4. Estadísticas de pesos por característica
        pesos_stats = pd.DataFrame({
            'Característica': self.feature_names,
            'Media': pesos.mean(axis=1),
            'Std': pesos.std(axis=1),
            'Min': pesos.min(axis=1),
            'Max': pesos.max(axis=1)
        })
        
        axes[1, 1].scatter(pesos_stats['Media'], pesos_stats['Std'])
        for i, txt in enumerate(pesos_stats['Característica']):
            axes[1, 1].annotate(txt, (pesos_stats['Media'].iloc[i], pesos_stats['Std'].iloc[i]))
        axes[1, 1].set_title('Media vs Desviación Estándar de Pesos')
        axes[1, 1].set_xlabel('Media de Pesos')
        axes[1, 1].set_ylabel('Desviación Estándar')
        
        plt.tight_layout()
        plt.savefig('analisis_pesos.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Análisis de pesos guardado como 'analisis_pesos.png'")
        
        return pesos_stats

def hacer_ejemplos_prediccion(model, scaler, X_test, y_test, feature_names):
    """
    Hace ejemplos de predicción con casos específicos
    """
    print("\n=== EJEMPLOS DE PREDICCIÓN ===")
    
    # Seleccionar algunos casos interesantes
    indices_ejemplo = [0, 100, 500, 1000, 1500]
    
    for i, idx in enumerate(indices_ejemplo):
        if idx < len(X_test):
            # Datos de entrada
            X_ejemplo = X_test.iloc[idx:idx+1]
            X_ejemplo_scaled = scaler.transform(X_ejemplo)
            
            # Predicción
            prediccion = model.predict(X_ejemplo_scaled)[0][0]
            valor_real = y_test.iloc[idx]
            error = abs(prediccion - valor_real)
            
            print(f"\n--- EJEMPLO {i+1} ---")
            print(f"Características de la casa:")
            for j, feature in enumerate(feature_names):
                print(f"  {feature}: {X_ejemplo.iloc[0, j]:.2f}")
            
            print(f"\nPredicción del modelo: ${prediccion:.2f}00k")
            print(f"Precio real: ${valor_real:.2f}00k")
            print(f"Error: ${error:.2f}00k ({(error/valor_real)*100:.1f}%)")

def main():
    """
    Función principal que ejecuta todo el análisis
    """
    print("=== ANÁLISIS DE DATASET Y DISEÑO DE RED NEURONAL ===")
    
    # 1. Cargar y analizar dataset
    analyzer = DatasetAnalyzer()
    df = analyzer.cargar_dataset()
    caracteristicas = analyzer.analizar_caracteristicas()
    analyzer.visualizar_dataset()
    analyzer.analizar_valores_atipicos()
    
    # 2. Preparar datos para la red neuronal
    X = df.drop('PRECIO', axis=1)
    y = df['PRECIO']
    
    # 3. Diseñar y entrenar red neuronal
    nn_designer = NeuralNetworkDesigner(X, y)
    nn_designer.preparar_datos()
    model = nn_designer.disenar_arquitectura()
    history = nn_designer.entrenar_modelo(epochs=50)
    metricas = nn_designer.evaluar_modelo()
    
    # 4. Analizar pesos aprendidos
    weight_analyzer = WeightAnalyzer(model, X.columns.tolist())
    pesos, sesgos, importancia_df = weight_analyzer.analizar_pesos()
    pesos_stats = weight_analyzer.visualizar_pesos(pesos, importancia_df)
    
    # 5. Hacer ejemplos de predicción
    hacer_ejemplos_prediccion(model, nn_designer.scaler, 
                            nn_designer.X_test, nn_designer.y_test, 
                            X.columns.tolist())
    
    # 6. Guardar modelo y resultados
    model.save('modelo_precios_casas.h5')
    print(f"\nModelo guardado como 'modelo_precios_casas.h5'")
    
    print(f"\n=== RESUMEN FINAL ===")
    print(f"Dataset: {df.shape[0]} casas con {df.shape[1]-1} características")
    print(f"Precisión del modelo (R²): {metricas['r2']:.3f}")
    print(f"Error promedio: ${metricas['mae']:.2f}00k")
    print(f"Característica más importante: {importancia_df.iloc[0]['Característica']}")

if __name__ == "__main__":
    main()
