"""
Simulador de Datos de MEPX
Este script simula diferentes conjuntos de datos típicos que se encuentran en MEPX
"""

import numpy as np
import pandas as pd
import os

def create_building_energy_data():
    """
    Simula el conjunto de datos de eficiencia energética de edificios
    Basado en el ejemplo "building1-energy" mencionado en MEPX
    """
    np.random.seed(42)
    n_samples = 768
    
    # Generar datos realistas de edificios
    data = {
        'relative_compactness': np.random.uniform(0.62, 0.98, n_samples),
        'surface_area': np.random.uniform(514.5, 808.5, n_samples),
        'wall_area': np.random.uniform(245.0, 416.5, n_samples),
        'roof_area': np.random.uniform(110.25, 220.5, n_samples),
        'overall_height': np.random.uniform(3.5, 7.0, n_samples),
        'orientation': np.random.randint(2, 6, n_samples),
        'glazing_area': np.random.uniform(0, 0.4, n_samples),
        'glazing_area_dist': np.random.randint(0, 6, n_samples)
    }
    
    # Calcular consumo energético basado en características físicas
    heating_load = (
        15 + 
        20 * data['relative_compactness'] + 
        0.01 * data['surface_area'] + 
        0.05 * data['wall_area'] + 
        0.02 * data['roof_area'] + 
        2 * data['overall_height'] + 
        data['orientation'] + 
        25 * data['glazing_area'] + 
        0.5 * data['glazing_area_dist'] +
        np.random.normal(0, 2, n_samples)
    )
    
    data['heating_load'] = heating_load
    
    return pd.DataFrame(data)

def create_concrete_strength_data():
    """
    Simula datos de resistencia del concreto
    """
    np.random.seed(123)
    n_samples = 1030
    
    data = {
        'cement': np.random.uniform(102, 540, n_samples),
        'blast_furnace_slag': np.random.uniform(0, 359, n_samples),
        'fly_ash': np.random.uniform(0, 200, n_samples),
        'water': np.random.uniform(121, 247, n_samples),
        'superplasticizer': np.random.uniform(0, 32, n_samples),
        'coarse_aggregate': np.random.uniform(708, 1145, n_samples),
        'fine_aggregate': np.random.uniform(594, 992, n_samples),
        'age': np.random.uniform(1, 365, n_samples)
    }
    
    # Fórmula basada en propiedades del concreto
    strength = (
        0.1 * data['cement'] +
        0.05 * data['blast_furnace_slag'] +
        0.08 * data['fly_ash'] +
        -0.2 * data['water'] +
        0.5 * data['superplasticizer'] +
        0.01 * data['coarse_aggregate'] +
        0.02 * data['fine_aggregate'] +
        0.1 * np.log(data['age'] + 1) +
        np.random.normal(0, 3, n_samples)
    )
    
    data['strength'] = np.maximum(strength, 0)  # La resistencia no puede ser negativa
    
    return pd.DataFrame(data)

def create_wine_quality_data():
    """
    Simula datos de calidad del vino
    """
    np.random.seed(456)
    n_samples = 1599
    
    data = {
        'fixed_acidity': np.random.uniform(4.6, 15.9, n_samples),
        'volatile_acidity': np.random.uniform(0.12, 1.58, n_samples),
        'citric_acid': np.random.uniform(0, 1, n_samples),
        'residual_sugar': np.random.uniform(0.9, 15.5, n_samples),
        'chlorides': np.random.uniform(0.012, 0.611, n_samples),
        'free_sulfur_dioxide': np.random.uniform(1, 72, n_samples),
        'total_sulfur_dioxide': np.random.uniform(6, 289, n_samples),
        'density': np.random.uniform(0.99007, 1.00369, n_samples),
        'pH': np.random.uniform(2.74, 4.01, n_samples),
        'sulphates': np.random.uniform(0.33, 2.0, n_samples),
        'alcohol': np.random.uniform(8.4, 14.9, n_samples)
    }
    
    # Calidad basada en características químicas
    quality = (
        5 +
        0.2 * data['fixed_acidity'] +
        -2 * data['volatile_acidity'] +
        0.5 * data['citric_acid'] +
        0.1 * data['residual_sugar'] +
        -10 * data['chlorides'] +
        0.02 * data['free_sulfur_dioxide'] +
        -0.01 * data['total_sulfur_dioxide'] +
        -2 * (data['density'] - 0.996) +
        0.5 * data['pH'] +
        0.8 * data['sulphates'] +
        0.3 * data['alcohol'] +
        np.random.normal(0, 0.8, n_samples)
    )
    
    data['quality'] = np.clip(np.round(quality), 3, 9)  # Calidad entre 3 y 9
    
    return pd.DataFrame(data)

def create_airfoil_data():
    """
    Simula datos de ruido aerodinámico
    """
    np.random.seed(789)
    n_samples = 1503
    
    data = {
        'frequency': np.random.uniform(200, 20000, n_samples),
        'angle_of_attack': np.random.uniform(0, 22.2, n_samples),
        'chord_length': np.random.uniform(0.0254, 0.3048, n_samples),
        'free_stream_velocity': np.random.uniform(31.7, 71.3, n_samples),
        'displacement_thickness': np.random.uniform(0.0020, 0.0584, n_samples)
    }
    
    # Nivel de ruido basado en parámetros aerodinámicos
    noise = (
        100 +
        0.01 * data['frequency'] +
        2 * data['angle_of_attack'] +
        50 * data['chord_length'] +
        0.5 * data['free_stream_velocity'] +
        1000 * data['displacement_thickness'] +
        np.random.normal(0, 5, n_samples)
    )
    
    data['noise_level'] = noise
    
    return pd.DataFrame(data)

def save_in_mepx_format(data, filename, problem_type, target_column):
    """
    Guarda los datos en formato similar a MEPX
    """
    # Crear directorio data si no existe
    os.makedirs('data', exist_ok=True)
    
    # Crear archivo de texto estilo MEPX
    filepath = f'data/{filename}.txt'
    
    with open(filepath, 'w') as f:
        # Encabezado con información del problema
        f.write(f"# {filename.upper()} Dataset\n")
        f.write(f"# Problem type: {problem_type}\n")
        f.write(f"# Target variable: {target_column}\n")
        f.write(f"# Number of samples: {len(data)}\n")
        f.write(f"# Number of features: {len(data.columns) - 1}\n")
        f.write("#\n")
        
        # Nombres de las variables
        feature_names = [col for col in data.columns if col != target_column]
        f.write("# Variables: " + ", ".join(feature_names) + f", {target_column}\n")
        f.write("#\n")
        
        # Datos
        for _, row in data.iterrows():
            # Escribir características
            for feature in feature_names:
                f.write(f"{row[feature]:.6f}\t")
            # Escribir variable objetivo
            f.write(f"{row[target_column]:.6f}\n")
    
    # También guardar como CSV
    data.to_csv(f'data/{filename}.csv', index=False)
    
    print(f"Datos guardados en 'data/{filename}.txt' y 'data/{filename}.csv'")

def main():
    """
    Genera todos los conjuntos de datos de ejemplo
    """
    print("=== GENERADOR DE DATOS DE EJEMPLO ESTILO MEPX ===")
    print()
    
    # Crear directorio para los datos
    os.makedirs('data', exist_ok=True)
    
    # Generar conjunto de datos de eficiencia energética
    print("1. Generando datos de eficiencia energética de edificios...")
    building_data = create_building_energy_data()
    save_in_mepx_format(building_data, 'building_energy', 'Regression', 'heating_load')
    
    # Generar conjunto de datos de resistencia del concreto
    print("2. Generando datos de resistencia del concreto...")
    concrete_data = create_concrete_strength_data()
    save_in_mepx_format(concrete_data, 'concrete_strength', 'Regression', 'strength')
    
    # Generar conjunto de datos de calidad del vino
    print("3. Generando datos de calidad del vino...")
    wine_data = create_wine_quality_data()
    save_in_mepx_format(wine_data, 'wine_quality', 'Classification', 'quality')
    
    # Generar conjunto de datos de ruido aerodinámico
    print("4. Generando datos de ruido aerodinámico...")
    airfoil_data = create_airfoil_data()
    save_in_mepx_format(airfoil_data, 'airfoil_noise', 'Regression', 'noise_level')
    
    print()
    print("=== RESUMEN DE DATOS GENERADOS ===")
    
    datasets = [
        ('building_energy', building_data, 'heating_load'),
        ('concrete_strength', concrete_data, 'strength'),
        ('wine_quality', wine_data, 'quality'),
        ('airfoil_noise', airfoil_data, 'noise_level')
    ]
    
    for name, data, target in datasets:
        print(f"\n{name.upper()}:")
        print(f"  Muestras: {len(data)}")
        print(f"  Características: {len(data.columns) - 1}")
        print(f"  Variable objetivo: {target}")
        print(f"  Rango objetivo: {data[target].min():.2f} - {data[target].max():.2f}")
    
    print("\n=== ARCHIVOS GENERADOS ===")
    print("Directorio 'data' creado con los siguientes archivos:")
    for name, _, _ in datasets:
        print(f"  - {name}.txt (formato MEPX)")
        print(f"  - {name}.csv (formato CSV)")
    
    print("\nPuedes usar estos archivos para:")
    print("1. Cargar en MEPX y obtener expresiones simbólicas")
    print("2. Usar en los scripts de comparación con RNA")
    print("3. Experimentar con diferentes algoritmos de ML")

if __name__ == "__main__":
    main()
