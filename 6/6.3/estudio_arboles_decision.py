"""
ESTUDIO DETALLADO DEL ALGORITMO ÁRBOLES DE DECISIÓN
===================================================

Este script contiene un estudio completo del algoritmo de árboles de decisión:
- Explicación teórica detallada
- Implementación práctica
- Ejemplo de aplicación web comentado
- Documentación mejorada para entender cada parte
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

class EstudioArbolesDecision:
    """
    Clase para estudiar el algoritmo de árboles de decisión de forma detallada
    
    Los árboles de decisión son algoritmos de ML que:
    1. Toman decisiones siguiendo un flujo de preguntas
    2. Dividen los datos en base a características
    3. Crean reglas claras y comprensibles
    4. Pueden usarse para clasificación y regresión
    """
    
    def __init__(self):
        """
        Inicializa el estudio de árboles de decisión
        """
        self.modelo = None
        self.label_encoder = LabelEncoder()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.feature_names = None
        
    def explicar_teoria_arboles(self):
        """
        Explica la teoría detrás de los árboles de decisión
        """
        print("="*80)
        print("TEORÍA DE LOS ÁRBOLES DE DECISIÓN")
        print("="*80)
        
        print("\n📚 ¿QUÉ SON LOS ÁRBOLES DE DECISIÓN?")
        print("   Los árboles de decisión son algoritmos que:")
        print("   • Toman decisiones siguiendo un flujo de preguntas")
        print("   • Dividen los datos en base a características")
        print("   • Crean reglas claras y fáciles de entender")
        print("   • Funcionan como un diagrama de flujo")
        
        print("\n🌳 ESTRUCTURA DE UN ÁRBOL:")
        print("   • NODO RAÍZ: Primera pregunta/decisión")
        print("   • NODOS INTERNOS: Preguntas intermedias")
        print("   • HOJAS: Decisiones finales (clasificaciones)")
        print("   • RAMAS: Caminos entre nodos")
        
        print("\n🔍 CONCEPTOS CLAVE:")
        print("   1. ENTROPÍA: Medida de desorden/impureza")
        print("   2. GANANCIA DE INFORMACIÓN: Reducción de entropía")
        print("   3. GINI: Medida alternativa de impureza")
        print("   4. PODA: Eliminar ramas para evitar overfitting")
        
        print("\n⚙️ CRITERIOS DE DIVISIÓN:")
        print("   • GINI: Medida de impureza (más común)")
        print("   • ENTROPY: Basado en teoría de información")
        print("   • Busca la división que mejor separe las clases")
        
        print("\n🎯 VENTAJAS:")
        print("   ✅ Fácil de entender e interpretar")
        print("   ✅ No requiere normalización de datos")
        print("   ✅ Maneja datos categóricos y numéricos")
        print("   ✅ Identifica características importantes")
        print("   ✅ Rápido para predicciones")
        
        print("\n⚠️ DESVENTAJAS:")
        print("   ❌ Propenso a overfitting")
        print("   ❌ Inestable (pequeños cambios → árboles diferentes)")
        print("   ❌ Sesgado hacia características con más valores")
        print("   ❌ Dificultad con relaciones lineales")
        
    def generar_datos_ejemplo(self):
        """
        Genera un dataset simple para demostrar árboles de decisión
        """
        print("\n" + "="*80)
        print("GENERACIÓN DE DATOS DE EJEMPLO")
        print("="*80)
        
        # Crear dataset sintético para clasificación
        np.random.seed(42)
        
        # Características: Edad, Salario, Experiencia
        edad = np.random.randint(20, 65, 200)
        salario = np.random.randint(30000, 120000, 200)
        experiencia = np.random.randint(0, 30, 200)
        
        # Reglas para crear las clases (simulando aprobación de préstamo)
        aprobado = np.zeros(200)
        for i in range(200):
            # Reglas simples para aprobar préstamo
            if edad[i] >= 25 and salario[i] >= 50000 and experiencia[i] >= 2:
                aprobado[i] = 1
            elif salario[i] >= 80000:
                aprobado[i] = 1
            elif edad[i] >= 40 and experiencia[i] >= 10:
                aprobado[i] = 1
            # Agregar algo de ruido
            if np.random.random() < 0.1:
                aprobado[i] = 1 - aprobado[i]
        
        # Crear dataset
        X = np.column_stack((edad, salario, experiencia))
        y = aprobado.astype(int)
        
        # Nombres de características
        self.feature_names = ['Edad', 'Salario', 'Experiencia']
        
        print(f"   ✅ Dataset generado: {len(X)} muestras")
        print(f"   • Características: {X.shape[1]} (Edad, Salario, Experiencia)")
        print(f"   • Clase 0 (Rechazado): {np.sum(y == 0)} muestras")
        print(f"   • Clase 1 (Aprobado): {np.sum(y == 1)} muestras")
        print(f"   • Problema: Aprobación de préstamos")
        
        return X, y
    
    def entrenar_arbol(self, X, y):
        """
        Entrena diferentes árboles de decisión con distintos parámetros
        """
        print("\n" + "="*80)
        print("ENTRENAMIENTO DE ÁRBOLES DE DECISIÓN")
        print("="*80)
        
        # Dividir datos
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        
        print(f"   📊 Datos de entrenamiento: {len(self.X_train)} muestras")
        print(f"   📊 Datos de prueba: {len(self.X_test)} muestras")
        
        # Entrenar diferentes árboles
        modelos = {
            'Árbol Simple': DecisionTreeClassifier(random_state=42),
            'Árbol Limitado': DecisionTreeClassifier(
                max_depth=5, 
                min_samples_split=10, 
                random_state=42
            ),
            'Árbol con Gini': DecisionTreeClassifier(
                criterion='gini', 
                max_depth=4, 
                random_state=42
            ),
            'Árbol con Entropía': DecisionTreeClassifier(
                criterion='entropy', 
                max_depth=4, 
                random_state=42
            )
        }
        
        resultados = {}
        
        for nombre, modelo in modelos.items():
            print(f"\n   🌳 Entrenando {nombre}...")
            
            # Entrenar modelo
            modelo.fit(self.X_train, self.y_train)
            
            # Hacer predicciones
            y_pred = modelo.predict(self.X_test)
            
            # Calcular métricas
            accuracy = accuracy_score(self.y_test, y_pred)
            
            # Información del árbol
            n_nodes = modelo.tree_.node_count
            depth = modelo.tree_.max_depth
            
            resultados[nombre] = {
                'modelo': modelo,
                'accuracy': accuracy,
                'predicciones': y_pred,
                'nodos': n_nodes,
                'profundidad': depth
            }
            
            print(f"   ✅ {nombre}: Precisión = {accuracy:.4f}")
            print(f"      • Nodos: {n_nodes}, Profundidad: {depth}")
        
        # Encontrar mejor modelo
        mejor_modelo = max(resultados.items(), key=lambda x: x[1]['accuracy'])
        self.modelo = mejor_modelo[1]['modelo']
        
        print(f"\n   🏆 MEJOR MODELO: {mejor_modelo[0]} (Precisión: {mejor_modelo[1]['accuracy']:.4f})")
        
        return resultados
    
    def analizar_importancia_caracteristicas(self):
        """
        Analiza la importancia de las características
        """
        print("\n" + "="*80)
        print("ANÁLISIS DE IMPORTANCIA DE CARACTERÍSTICAS")
        print("="*80)
        
        importancias = self.modelo.feature_importances_
        
        print("   📊 Importancia de cada característica:")
        for i, (nombre, importancia) in enumerate(zip(self.feature_names, importancias)):
            print(f"   • {nombre}: {importancia:.4f} ({importancia*100:.1f}%)")
        
        # Encontrar la característica más importante
        mas_importante = np.argmax(importancias)
        print(f"\n   🏆 CARACTERÍSTICA MÁS IMPORTANTE: {self.feature_names[mas_importante]}")
        
        return importancias
    
    def mostrar_reglas_decision(self):
        """
        Muestra las reglas de decisión del árbol
        """
        print("\n" + "="*80)
        print("REGLAS DE DECISIÓN DEL ÁRBOL")
        print("="*80)
        
        # Extraer reglas del árbol
        tree = self.modelo.tree_
        feature_names = self.feature_names
        
        def get_rules(node, depth=0):
            """Función recursiva para extraer reglas"""
            indent = "  " * depth
            
            if tree.feature[node] != -2:  # No es una hoja
                feature = feature_names[tree.feature[node]]
                threshold = tree.threshold[node]
                
                print(f"{indent}SI {feature} <= {threshold:.2f}:")
                get_rules(tree.children_left[node], depth + 1)
                
                print(f"{indent}SI {feature} > {threshold:.2f}:")
                get_rules(tree.children_right[node], depth + 1)
            else:  # Es una hoja
                clase = np.argmax(tree.value[node])
                confianza = np.max(tree.value[node]) / np.sum(tree.value[node])
                resultado = "APROBADO" if clase == 1 else "RECHAZADO"
                print(f"{indent}→ {resultado} (confianza: {confianza:.2f})")
        
        print("   🌳 Reglas extraídas del árbol:")
        get_rules(0)
        
    def analizar_resultados(self, resultados):
        """
        Analiza los resultados de los diferentes modelos
        """
        print("\n" + "="*80)
        print("ANÁLISIS COMPARATIVO DE MODELOS")
        print("="*80)
        
        for nombre, datos in resultados.items():
            print(f"\n📈 MODELO: {nombre}")
            print(f"   • Precisión: {datos['accuracy']:.4f}")
            print(f"   • Nodos: {datos['nodos']}")
            print(f"   • Profundidad: {datos['profundidad']}")
            
            # Matriz de confusión
            cm = confusion_matrix(self.y_test, datos['predicciones'])
            print(f"   • Matriz de confusión:")
            print(f"     Rechazados correctos: {cm[0,0]}")
            print(f"     Falsos aprobados: {cm[0,1]}")
            print(f"     Falsos rechazados: {cm[1,0]}")
            print(f"     Aprobados correctos: {cm[1,1]}")
            
            # Interpretación del negocio
            if cm[0,1] > 0:
                print(f"   ⚠️ Riesgo: {cm[0,1]} préstamos riesgosos aprobados")
            if cm[1,0] > 0:
                print(f"   💰 Pérdida: {cm[1,0]} buenos clientes rechazados")
    
    def visualizar_arbol(self, X, y, resultados):
        """
        Crea visualizaciones del árbol de decisión
        """
        print("\n" + "="*80)
        print("GENERANDO VISUALIZACIONES")
        print("="*80)
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Estudio de Árboles de Decisión', fontsize=16)
        
        # Visualizar el árbol
        axes[0, 0].set_title('Estructura del Mejor Árbol')
        plot_tree(self.modelo, 
                 feature_names=self.feature_names,
                 class_names=['Rechazado', 'Aprobado'],
                 filled=True,
                 rounded=True,
                 ax=axes[0, 0])
        
        # Importancia de características
        importancias = self.modelo.feature_importances_
        axes[0, 1].bar(self.feature_names, importancias, color=['skyblue', 'lightgreen', 'lightcoral'])
        axes[0, 1].set_title('Importancia de Características')
        axes[0, 1].set_ylabel('Importancia')
        
        # Comparación de precisiones
        nombres = list(resultados.keys())
        precisiones = [resultados[nombre]['accuracy'] for nombre in nombres]
        
        axes[1, 0].bar(range(len(nombres)), precisiones, color='lightblue')
        axes[1, 0].set_title('Comparación de Precisiones')
        axes[1, 0].set_ylabel('Precisión')
        axes[1, 0].set_xticks(range(len(nombres)))
        axes[1, 0].set_xticklabels(nombres, rotation=45)
        
        # Información del modelo
        axes[1, 1].text(0.1, 0.8, f'RESUMEN DEL ESTUDIO', fontsize=14, weight='bold', transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.7, f'Mejor Modelo: {max(resultados.items(), key=lambda x: x[1]["accuracy"])[0]}', 
                        fontsize=12, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.6, f'Precisión: {max(resultados.values(), key=lambda x: x["accuracy"])["accuracy"]:.4f}', 
                        fontsize=12, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.5, f'Muestras: {len(X)}', fontsize=12, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.4, f'Características: {X.shape[1]}', fontsize=12, transform=axes[1, 1].transAxes)
        
        axes[1, 1].text(0.1, 0.2, 'Ventajas de Árboles:', fontsize=12, weight='bold', transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.15, '• Fácil interpretación', fontsize=10, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.1, '• Reglas claras', fontsize=10, transform=axes[1, 1].transAxes)
        axes[1, 1].text(0.1, 0.05, '• No requiere normalización', fontsize=10, transform=axes[1, 1].transAxes)
        
        axes[1, 1].set_xlim(0, 1)
        axes[1, 1].set_ylim(0, 1)
        axes[1, 1].axis('off')
        
        plt.tight_layout()
        plt.savefig('estudio_arboles.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
        
        print("   ✅ Visualizaciones guardadas como 'estudio_arboles.png'")

def main():
    """
    Función principal que ejecuta el estudio completo de árboles de decisión
    """
    print("="*80)
    print("ESTUDIO COMPLETO DE ÁRBOLES DE DECISIÓN")
    print("="*80)
    
    # Crear instancia del estudio
    estudio = EstudioArbolesDecision()
    
    # 1. Explicar la teoría
    estudio.explicar_teoria_arboles()
    
    # 2. Generar datos
    X, y = estudio.generar_datos_ejemplo()
    
    # 3. Entrenar modelos
    resultados = estudio.entrenar_arbol(X, y)
    
    # 4. Analizar importancia
    estudio.analizar_importancia_caracteristicas()
    
    # 5. Mostrar reglas
    estudio.mostrar_reglas_decision()
    
    # 6. Analizar resultados
    estudio.analizar_resultados(resultados)
    
    # 7. Visualizar
    estudio.visualizar_arbol(X, y, resultados)
    
    print("\n" + "="*80)
    print("ESTUDIO DE ÁRBOLES DE DECISIÓN COMPLETADO")
    print("="*80)

if __name__ == "__main__":
    main()
