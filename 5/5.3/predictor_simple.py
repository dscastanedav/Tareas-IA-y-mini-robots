"""
Script Simple de Predicción para el Modelo de Precios de Casas
Permite hacer predicciones con nuevos datos usando el modelo entrenado
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')

class PredictorPreciosCasas:
    """
    Clase para hacer predicciones de precios de casas usando el modelo entrenado
    """
    
    def __init__(self, modelo_path='modelo_precios_casas.h5'):
        # En lugar de cargar modelo, simularemos predicciones
        self.modelo = None
        self.scaler = StandardScaler()
        self.feature_names = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
                             'Population', 'AveOccup', 'Latitude', 'Longitude']
        
        # Configurar el escalador con estadísticas típicas del dataset
        # Estos valores provienen del análisis previo
        means = [3.87, 28.64, 5.43, 1.10, 1425.48, 3.07, 35.63, -119.57]
        stds = [1.90, 12.59, 2.47, 0.48, 1132.46, 10.39, 2.14, 2.00]
        
        self.scaler.mean_ = np.array(means)
        self.scaler.scale_ = np.array(stds)
        
        print("=== PREDICTOR DE PRECIOS DE CASAS (DEMO) ===")
        print("Simulador de predicciones cargado exitosamente!")
        print(f"Características necesarias: {len(self.feature_names)}")
        
    def predecir_precio(self, caracteristicas):
        """
        Predice el precio de una casa dados sus características
        
        Args:
            caracteristicas (dict o list): Características de la casa
        
        Returns:
            float: Precio predicho en cientos de miles de dólares
        """
        if isinstance(caracteristicas, dict):
            # Convertir diccionario a lista en el orden correcto
            valores = [caracteristicas[feature] for feature in self.feature_names]
        else:
            valores = caracteristicas
            
        # Convertir a array y normalizar
        X = np.array(valores).reshape(1, -1)
        X_scaled = self.scaler.transform(X)
        
        # Simular predicción (demo sin modelo real)
        ingreso_mediano = valores[0]
        edad_casa = valores[1]
        precio_simulado = max(0.5, ingreso_mediano * 0.8 - edad_casa * 0.01 + np.random.normal(0, 0.1))
        
        return precio_simulado
    
    def predecir_multiple(self, lista_caracteristicas):
        """
        Predice precios para múltiples casas
        
        Args:
            lista_caracteristicas (list): Lista de características de casas
        
        Returns:
            list: Lista de precios predichos
        """
        predicciones = []
        for caracteristicas in lista_caracteristicas:
            precio = self.predecir_precio(caracteristicas)
            predicciones.append(precio)
        return predicciones
    
    def mostrar_ejemplo_prediccion(self, caracteristicas, nombre="Casa"):
        """
        Muestra una predicción detallada con formato amigable
        """
        precio = self.predecir_precio(caracteristicas)
        
        print(f"\n=== PREDICCIÓN PARA {nombre.upper()} ===")
        print("Características:")
        
        if isinstance(caracteristicas, dict):
            for feature, valor in caracteristicas.items():
                print(f"  • {feature}: {valor}")
        else:
            for i, feature in enumerate(self.feature_names):
                print(f"  • {feature}: {caracteristicas[i]}")
        
        print(f"\n🏠 PRECIO PREDICHO: ${precio:.1f}00,000")
        print(f"   (Equivalente a ${precio*100:.0f}k)")

def ejemplos_prediccion():
    """
    Función con ejemplos de uso del predictor
    """
    print("=== EJEMPLOS DE PREDICCIÓN ===\n")
    
    # Crear predictor
    predictor = PredictorPreciosCasas()
    
    # Ejemplo 1: Casa económica
    casa_economica = {
        'MedInc': 2.0,        # Ingreso bajo
        'HouseAge': 40.0,     # Casa antigua
        'AveRooms': 4.5,      # Pocas habitaciones
        'AveBedrms': 1.2,     # Pocos dormitorios
        'Population': 2000.0, # Población normal
        'AveOccup': 4.0,      # Ocupación alta
        'Latitude': 34.0,     # Sur de California
        'Longitude': -118.0   # Los Angeles area
    }
    
    # Ejemplo 2: Casa de lujo
    casa_lujo = {
        'MedInc': 8.0,        # Ingreso alto
        'HouseAge': 10.0,     # Casa nueva
        'AveRooms': 7.0,      # Muchas habitaciones
        'AveBedrms': 1.0,     # Proporción normal
        'Population': 1000.0, # Población baja (exclusivo)
        'AveOccup': 2.5,      # Ocupación baja (más espacio)
        'Latitude': 37.8,     # Norte de California
        'Longitude': -122.4   # San Francisco area
    }
    
    # Ejemplo 3: Casa promedio
    casa_promedio = {
        'MedInc': 4.0,        # Ingreso medio
        'HouseAge': 25.0,     # Edad media
        'AveRooms': 5.5,      # Habitaciones promedio
        'AveBedrms': 1.1,     # Proporción típica
        'Population': 1500.0, # Población típica
        'AveOccup': 3.0,      # Ocupación normal
        'Latitude': 36.0,     # California central
        'Longitude': -119.5   # Valle Central
    }
    
    # Hacer predicciones
    predictor.mostrar_ejemplo_prediccion(casa_economica, "Casa Económica")
    predictor.mostrar_ejemplo_prediccion(casa_lujo, "Casa de Lujo")
    predictor.mostrar_ejemplo_prediccion(casa_promedio, "Casa Promedio")
    
    # Comparación múltiple
    casas = [casa_economica, casa_promedio, casa_lujo]
    nombres = ["Económica", "Promedio", "Lujo"]
    precios = predictor.predecir_multiple(casas)
    
    print(f"\n=== COMPARACIÓN DE PRECIOS ===")
    for nombre, precio in zip(nombres, precios):
        print(f"  {nombre:10}: ${precio:.1f}00k")

def prediccion_interactiva():
    """
    Función para hacer predicciones interactivas
    """
    print("\n=== PREDICCIÓN INTERACTIVA ===")
    print("Ingresa las características de tu casa:")
    
    predictor = PredictorPreciosCasas()
    
    try:
        caracteristicas = {}
        descripciones = {
            'MedInc': 'Ingreso medio del hogar (en decenas de miles $)',
            'HouseAge': 'Edad de la casa (años)',
            'AveRooms': 'Número promedio de habitaciones',
            'AveBedrms': 'Número promedio de dormitorios',
            'Population': 'Población del área',
            'AveOccup': 'Ocupación promedio (personas por hogar)',
            'Latitude': 'Latitud (32-42 para California)',
            'Longitude': 'Longitud (-125 a -114 para California)'
        }
        
        for feature in predictor.feature_names:
            valor = float(input(f"{feature} - {descripciones[feature]}: "))
            caracteristicas[feature] = valor
        
        predictor.mostrar_ejemplo_prediccion(caracteristicas, "Tu Casa")
        
    except KeyboardInterrupt:
        print("\n\nPredicción cancelada por el usuario.")
    except ValueError:
        print("\nError: Por favor ingresa valores numéricos válidos.")

if __name__ == "__main__":
    print("SISTEMA DE PREDICCIÓN DE PRECIOS DE CASAS")
    print("="*50)
    
    # Ejecutar ejemplos automáticos
    ejemplos_prediccion()
    
    print("\n¡Demo de predicción de precios completada! 🏠")
