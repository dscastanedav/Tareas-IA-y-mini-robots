"""
ESTUDIO DETALLADO DEL ALGORITMO SVM (Support Vector Machine)
============================================================

Este script contiene un estudio completo del algoritmo SVM con:
- Explicación teórica detallada
- Implementación práctica
- Ejemplo de aplicación web comentado
- Documentación mejorada para entender cada parte
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

class EstudioSVM:
    """
    Clase para estudiar el algoritmo SVM de forma detallada
    
    SVM (Support Vector Machine) es un algoritmo de aprendizaje supervisado que:
    1. Encuentra el hiperplano que mejor separa las clases
    2. Maximiza el margen entre las clases
    3. Puede usar kernels para datos no linealmente separables
    """
    
    def __init__(self):
        """
        Inicializa el estudio SVM
        """
        self.modelo = None
        self.scaler = StandardScaler()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def explicar_teoria_svm(self):
        """
        Explica la teoría detrás del algoritmo SVM
        """
        print("="*80)
        print("TEORÍA DEL ALGORITMO SVM")
        print("="*80)
        
        print("\n📚 ¿QUÉ ES SVM?")
        print("   SVM (Support Vector Machine) es un algoritmo de clasificación que:")
        print("   • Encuentra el hiperplano óptimo que separa las clases")
        print("   • Maximiza el margen entre las clases")
        print("   • Usa vectores de soporte (puntos más cercanos al hiperplano)")
        
        print("\n🔍 CONCEPTOS CLAVE:")
        print("   1. HIPERPLANO: Línea (2D) o plano (3D+) que separa las clases")
        print("   2. MARGEN: Distancia entre el hiperplano y los puntos más cercanos")
        print("   3. VECTORES DE SOPORTE: Puntos que definen el hiperplano")
        print("   4. KERNEL: Función que transforma datos no lineales")
        
        print("\n⚡ TIPOS DE KERNEL:")
        print("   • LINEAR: Para datos linealmente separables")
        print("   • RBF (Radial): Para datos con patrones circulares")
        print("   • POLYNOMIAL: Para relaciones polinómicas")
        print("   • SIGMOID: Para redes neuronales")
        
        print("\n🎯 VENTAJAS:")
        print("   ✅ Efectivo en espacios de alta dimensión")
        print("   ✅ Funciona bien con pocos datos")
        print("   ✅ Versátil (diferentes kernels)")
        print("   ✅ Eficiente en memoria")
        
        print("\n⚠️ DESVENTAJAS:")
        print("   ❌ Lento con datasets grandes")
        print("   ❌ Sensible a normalización")
        print("   ❌ No proporciona probabilidades directas")
        
    def generar_datos_ejemplo(self):
        """
        Genera un dataset simple para demostrar SVM
        """
        print("\n" + "="*80)
        print("GENERACIÓN DE DATOS DE EJEMPLO")
        print("="*80)
        
        # Generar datos sintéticos
        np.random.seed(42)
        
        # Clase 1: Puntos alrededor de (2, 2)
        clase1_x = np.random.normal(2, 0.8, 50)
        clase1_y = np.random.normal(2, 0.8, 50)
        
        # Clase 2: Puntos alrededor de (6, 6)
        clase2_x = np.random.normal(6, 0.8, 50)
        clase2_y = np.random.normal(6, 0.8, 50)
        
        # Combinar datos
        X = np.column_stack((
            np.concatenate([clase1_x, clase2_x]),
            np.concatenate([clase1_y, clase2_y])
        ))
        
        y = np.concatenate([np.zeros(50), np.ones(50)])
        
        print(f"   ✅ Dataset generado: {len(X)} muestras")
        print(f"   • Clase 0: {np.sum(y == 0)} muestras")
        print(f"   • Clase 1: {np.sum(y == 1)} muestras")
        print(f"   • Características: {X.shape[1]} (X, Y)")
        
        return X, y
    
    def entrenar_svm(self, X, y):
        """
        Entrena diferentes modelos SVM con distintos kernels
        """
        print("\n" + "="*80)
        print("ENTRENAMIENTO DE MODELOS SVM")
        print("="*80)
        
        # Dividir datos
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        
        # Normalizar datos (MUY IMPORTANTE para SVM)
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"   📊 Datos de entrenamiento: {len(self.X_train)} muestras")
        print(f"   📊 Datos de prueba: {len(self.X_test)} muestras")
        print(f"   📊 Datos normalizados: ✅")
        
        # Entrenar diferentes modelos
        modelos = {
            'Linear': SVC(kernel='linear', random_state=42),
            'RBF': SVC(kernel='rbf', random_state=42),
            'Polynomial': SVC(kernel='poly', degree=3, random_state=42)
        }
        
        resultados = {}
        
        for nombre, modelo in modelos.items():
            print(f"\n   🔄 Entrenando SVM con kernel {nombre}...")
            
            # Entrenar modelo
            modelo.fit(self.X_train_scaled, self.y_train)
            
            # Hacer predicciones
            y_pred = modelo.predict(self.X_test_scaled)
            
            # Calcular métricas
            accuracy = accuracy_score(self.y_test, y_pred)
            
            resultados[nombre] = {
                'modelo': modelo,
                'accuracy': accuracy,
                'predicciones': y_pred
            }
            
            print(f"   ✅ {nombre}: Precisión = {accuracy:.4f}")
        
        # Encontrar mejor modelo
        mejor_modelo = max(resultados.items(), key=lambda x: x[1]['accuracy'])
        self.modelo = mejor_modelo[1]['modelo']
        
        print(f"\n   🏆 MEJOR MODELO: {mejor_modelo[0]} (Precisión: {mejor_modelo[1]['accuracy']:.4f})")
        
        return resultados
    
    def analizar_resultados(self, resultados):
        """
        Analiza los resultados de los modelos
        """
        print("\n" + "="*80)
        print("ANÁLISIS DETALLADO DE RESULTADOS")
        print("="*80)
        
        for nombre, datos in resultados.items():
            print(f"\n📈 MODELO: {nombre}")
            print(f"   • Precisión: {datos['accuracy']:.4f}")
            
            # Matriz de confusión
            cm = confusion_matrix(self.y_test, datos['predicciones'])
            print(f"   • Matriz de confusión:")
            print(f"     Verdaderos Negativos: {cm[0,0]}")
            print(f"     Falsos Positivos: {cm[0,1]}")
            print(f"     Falsos Negativos: {cm[1,0]}")
            print(f"     Verdaderos Positivos: {cm[1,1]}")
            
            # Reporte de clasificación
            print(f"   • Reporte detallado:")
            report = classification_report(self.y_test, datos['predicciones'], output_dict=True)
            if '0' in report:
                print(f"     Precisión Clase 0: {report['0']['precision']:.3f}")
                print(f"     Recall Clase 0: {report['0']['recall']:.3f}")
            if '1' in report:
                print(f"     Precisión Clase 1: {report['1']['precision']:.3f}")
                print(f"     Recall Clase 1: {report['1']['recall']:.3f}")
            print(f"     F1-Score Macro: {report['macro avg']['f1-score']:.3f}")
    
    def visualizar_resultados(self, X, y, resultados):
        """
        Crea visualizaciones de los resultados
        """
        print("\n" + "="*80)
        print("GENERANDO VISUALIZACIONES")
        print("="*80)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Estudio Comparativo de SVM con Diferentes Kernels', fontsize=16)
        
        # Datos originales
        axes[0, 0].scatter(X[y == 0, 0], X[y == 0, 1], c='red', marker='o', alpha=0.7, label='Clase 0')
        axes[0, 0].scatter(X[y == 1, 0], X[y == 1, 1], c='blue', marker='s', alpha=0.7, label='Clase 1')
        axes[0, 0].set_title('Datos Originales')
        axes[0, 0].set_xlabel('Característica X')
        axes[0, 0].set_ylabel('Característica Y')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Comparación de precisiones
        nombres = list(resultados.keys())
        precisiones = [resultados[nombre]['accuracy'] for nombre in nombres]
        
        axes[0, 1].bar(nombres, precisiones, color=['skyblue', 'lightgreen', 'lightcoral'])
        axes[0, 1].set_title('Comparación de Precisiones')
        axes[0, 1].set_ylabel('Precisión')
        axes[0, 1].set_ylim(0, 1)
        
        # Agregar valores en las barras
        for i, v in enumerate(precisiones):
            axes[0, 1].text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom')
        
        # Matriz de confusión del mejor modelo
        mejor_modelo = max(resultados.items(), key=lambda x: x[1]['accuracy'])
        cm = confusion_matrix(self.y_test, mejor_modelo[1]['predicciones'])
        
        im = axes[1, 0].imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        axes[1, 0].set_title(f'Matriz de Confusión - {mejor_modelo[0]}')
        axes[1, 0].set_xlabel('Predicción')
        axes[1, 0].set_ylabel('Realidad')
        
        # Agregar texto a la matriz
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                axes[1, 0].text(j, i, format(cm[i, j], 'd'),
                               ha="center", va="center", color="white" if cm[i, j] > cm.max() / 2 else "black")
        
        # Distribución de errores
        axes[1, 1].text(0.1, 0.8, f'RESUMEN DEL ESTUDIO SVM', fontsize=14, weight='bold', transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.7, f'Mejor Modelo: {mejor_modelo[0]}', fontsize=12, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.6, f'Precisión: {mejor_modelo[1]["accuracy"]:.4f}', fontsize=12, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.5, f'Muestras: {len(X)}', fontsize=12, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.4, f'Características: {X.shape[1]}', fontsize=12, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.3, f'Clases: {len(np.unique(y))}', fontsize=12, transform=axes[1, 1].transAxes)
        
        axes[1, 1].text(0.1, 0.1, 'SVM es ideal para:', fontsize=12, weight='bold', transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.05, '• Clasificación binaria', fontsize=10, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.01, '• Datos complejos', fontsize=10, transform=axes[1, 1].transAxes)
        
        axes[1, 1].set_xlim(0, 1)
        axes[1, 1].set_ylim(0, 1)
        axes[1, 1].axis('off')
        
        plt.tight_layout()
        plt.savefig('estudio_svm.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
        
        print("   ✅ Visualizaciones guardadas como 'estudio_svm.png'")

def main():
    """
    Función principal que ejecuta el estudio completo de SVM
    """
    print("="*80)
    print("ESTUDIO COMPLETO DEL ALGORITMO SVM")
    print("="*80)
    
    # Crear instancia del estudio
    estudio = EstudioSVM()
    
    # 1. Explicar la teoría
    estudio.explicar_teoria_svm()
    
    # 2. Generar datos
    X, y = estudio.generar_datos_ejemplo()
    
    # 3. Entrenar modelos
    resultados = estudio.entrenar_svm(X, y)
    
    # 4. Analizar resultados
    estudio.analizar_resultados(resultados)
    
    # 5. Visualizar
    estudio.visualizar_resultados(X, y, resultados)
    
    print("\n" + "="*80)
    print("ESTUDIO SVM COMPLETADO EXITOSAMENTE")
    print("="*80)

if __name__ == "__main__":
    main()
