"""
APLICACIÓN WEB DE SVM - EJEMPLO COMENTADO
==========================================

Este archivo contiene un ejemplo completo de cómo adaptar el algoritmo SVM 
para una aplicación web. Incluye:

1. Backend con Flask/FastAPI
2. Frontend con HTML/JavaScript
3. API REST para predicciones
4. Base de datos para almacenar resultados
5. Interfaz web interactiva

NOTA: Este es un ejemplo comentado, no requiere implementación real.
"""

# =====================================================
# BACKEND - SERVIDOR WEB CON FLASK
# =====================================================

"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import pickle
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde el frontend

# Cargar modelo SVM preentrenado
with open('modelo_svm.pkl', 'rb') as f:
    modelo_svm = pickle.load(f)

# Configuración de base de datos
def init_db():
    '''Inicializa la base de datos para guardar predicciones'''
    conn = sqlite3.connect('predicciones.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predicciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATETIME,
            entrada TEXT,
            prediccion TEXT,
            confianza REAL
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    '''Página principal de la aplicación'''
    return render_template('index.html')

@app.route('/api/predecir', methods=['POST'])
def predecir():
    '''
    API endpoint para realizar predicciones con SVM
    
    Recibe:
    - datos: lista de características [x1, x2, x3, ...]
    
    Retorna:
    - prediccion: clase predicha
    - confianza: nivel de confianza
    - tiempo: tiempo de procesamiento
    '''
    try:
        # Obtener datos del request
        datos = request.json
        caracteristicas = np.array(datos['caracteristicas']).reshape(1, -1)
        
        # Realizar predicción
        start_time = time.time()
        prediccion = modelo_svm.predict(caracteristicas)[0]
        
        # Calcular confianza (distancia al hiperplano)
        distancia = modelo_svm.decision_function(caracteristicas)[0]
        confianza = abs(distancia)  # Mientras más lejos, más confianza
        
        tiempo_procesamiento = time.time() - start_time
        
        # Guardar en base de datos
        conn = sqlite3.connect('predicciones.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO predicciones (fecha, entrada, prediccion, confianza)
            VALUES (?, ?, ?, ?)
        ''', (datetime.now(), str(caracteristicas.tolist()), str(prediccion), confianza))
        conn.commit()
        conn.close()
        
        # Retornar resultado
        return jsonify({
            'success': True,
            'prediccion': int(prediccion),
            'confianza': float(confianza),
            'tiempo': tiempo_procesamiento,
            'mensaje': 'Predicción realizada exitosamente'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/estadisticas', methods=['GET'])
def estadisticas():
    '''Endpoint para obtener estadísticas de uso'''
    conn = sqlite3.connect('predicciones.db')
    cursor = conn.cursor()
    
    # Obtener estadísticas
    cursor.execute('SELECT COUNT(*) FROM predicciones')
    total_predicciones = cursor.fetchone()[0]
    
    cursor.execute('SELECT AVG(confianza) FROM predicciones')
    confianza_promedio = cursor.fetchone()[0]
    
    cursor.execute('SELECT prediccion, COUNT(*) FROM predicciones GROUP BY prediccion')
    distribucion = cursor.fetchall()
    
    conn.close()
    
    return jsonify({
        'total_predicciones': total_predicciones,
        'confianza_promedio': confianza_promedio,
        'distribucion_clases': dict(distribucion)
    })

@app.route('/api/entrenar', methods=['POST'])
def entrenar_modelo():
    '''
    Endpoint para re-entrenar el modelo con nuevos datos
    (En una aplicación real, esto se haría con validación y seguridad)
    '''
    try:
        datos = request.json
        X_nuevos = np.array(datos['X'])
        y_nuevos = np.array(datos['y'])
        
        # Re-entrenar modelo
        modelo_svm.fit(X_nuevos, y_nuevos)
        
        # Guardar modelo actualizado
        with open('modelo_svm.pkl', 'wb') as f:
            pickle.dump(modelo_svm, f)
        
        return jsonify({
            'success': True,
            'mensaje': 'Modelo re-entrenado exitosamente'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
"""

# =====================================================
# FRONTEND - INTERFAZ WEB (HTML + JavaScript)
# =====================================================

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clasificador SVM - Aplicación Web</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #555;
        }
        
        input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        
        button {
            background-color: #007bff;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            margin-top: 20px;
        }
        
        button:hover {
            background-color: #0056b3;
        }
        
        .resultado {
            margin-top: 30px;
            padding: 20px;
            border-radius: 5px;
            display: none;
        }
        
        .resultado.positivo {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
        }
        
        .resultado.negativo {
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            color: #721c24;
        }
        
        .estadisticas {
            margin-top: 30px;
            padding: 20px;
            background-color: #e9ecef;
            border-radius: 5px;
        }
        
        .loading {
            text-align: center;
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 Clasificador SVM</h1>
        
        <div class="input-group">
            <label for="caracteristica1">Característica 1:</label>
            <input type="number" id="caracteristica1" step="0.1" placeholder="Ingrese valor">
        </div>
        
        <div class="input-group">
            <label for="caracteristica2">Característica 2:</label>
            <input type="number" id="caracteristica2" step="0.1" placeholder="Ingrese valor">
        </div>
        
        <button onclick="realizarPrediccion()">Clasificar</button>
        
        <div id="resultado" class="resultado">
            <h3>Resultado:</h3>
            <p id="prediccion-texto"></p>
            <p id="confianza-texto"></p>
            <p id="tiempo-texto"></p>
        </div>
        
        <div class="estadisticas">
            <h3>📊 Estadísticas del Sistema</h3>
            <p>Total de predicciones: <span id="total-predicciones">-</span></p>
            <p>Confianza promedio: <span id="confianza-promedio">-</span></p>
            <button onclick="cargarEstadisticas()">Actualizar Estadísticas</button>
        </div>
    </div>

    <script>
        // Función para realizar predicción
        async function realizarPrediccion() {
            const caracteristica1 = parseFloat(document.getElementById('caracteristica1').value);
            const caracteristica2 = parseFloat(document.getElementById('caracteristica2').value);
            
            // Validar entrada
            if (isNaN(caracteristica1) || isNaN(caracteristica2)) {
                alert('Por favor ingrese valores válidos');
                return;
            }
            
            // Mostrar loading
            document.getElementById('resultado').style.display = 'block';
            document.getElementById('prediccion-texto').innerHTML = 
                '<div class="loading">Clasificando...</div>';
            
            try {
                // Realizar petición a la API
                const response = await fetch('/api/predecir', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        caracteristicas: [caracteristica1, caracteristica2]
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    // Mostrar resultado
                    const resultadoDiv = document.getElementById('resultado');
                    resultadoDiv.className = 'resultado ' + (data.prediccion === 1 ? 'positivo' : 'negativo');
                    
                    document.getElementById('prediccion-texto').innerHTML = 
                        `<strong>Clase predicha:</strong> ${data.prediccion === 1 ? 'Positiva' : 'Negativa'}`;
                    document.getElementById('confianza-texto').innerHTML = 
                        `<strong>Confianza:</strong> ${data.confianza.toFixed(4)}`;
                    document.getElementById('tiempo-texto').innerHTML = 
                        `<strong>Tiempo:</strong> ${(data.tiempo * 1000).toFixed(2)}ms`;
                    
                    // Actualizar estadísticas automáticamente
                    cargarEstadisticas();
                } else {
                    throw new Error(data.error);
                }
                
            } catch (error) {
                document.getElementById('prediccion-texto').innerHTML = 
                    `<strong>Error:</strong> ${error.message}`;
                document.getElementById('resultado').className = 'resultado negativo';
            }
        }
        
        // Función para cargar estadísticas
        async function cargarEstadisticas() {
            try {
                const response = await fetch('/api/estadisticas');
                const data = await response.json();
                
                document.getElementById('total-predicciones').textContent = data.total_predicciones;
                document.getElementById('confianza-promedio').textContent = 
                    data.confianza_promedio ? data.confianza_promedio.toFixed(4) : 'N/A';
                
            } catch (error) {
                console.error('Error al cargar estadísticas:', error);
            }
        }
        
        // Cargar estadísticas al iniciar
        document.addEventListener('DOMContentLoaded', cargarEstadisticas);
    </script>
</body>
</html>
'''

# =====================================================
# APLICACIÓN MÓVIL - EJEMPLO CON FLUTTER/REACT NATIVE
# =====================================================

MOBILE_APP_EXAMPLE = '''
// Ejemplo de aplicación móvil con React Native
import React, { useState, useEffect } from 'react';
import {
  View, 
  Text, 
  TextInput, 
  TouchableOpacity, 
  StyleSheet, 
  Alert,
  ActivityIndicator
} from 'react-native';

const SVMClassifierApp = () => {
  const [feature1, setFeature1] = useState('');
  const [feature2, setFeature2] = useState('');
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);
  const [estadisticas, setEstadisticas] = useState({});

  // Función para realizar predicción
  const realizarPrediccion = async () => {
    const f1 = parseFloat(feature1);
    const f2 = parseFloat(feature2);
    
    if (isNaN(f1) || isNaN(f2)) {
      Alert.alert('Error', 'Por favor ingrese valores válidos');
      return;
    }
    
    setLoading(true);
    
    try {
      const response = await fetch('https://tu-servidor.com/api/predecir', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          caracteristicas: [f1, f2]
        })
      });
      
      const data = await response.json();
      
      if (data.success) {
        setResultado(data);
        cargarEstadisticas();
      } else {
        Alert.alert('Error', data.error);
      }
    } catch (error) {
      Alert.alert('Error', 'Error de conexión');
    } finally {
      setLoading(false);
    }
  };

  // Función para cargar estadísticas
  const cargarEstadisticas = async () => {
    try {
      const response = await fetch('https://tu-servidor.com/api/estadisticas');
      const data = await response.json();
      setEstadisticas(data);
    } catch (error) {
      console.error('Error al cargar estadísticas:', error);
    }
  };

  useEffect(() => {
    cargarEstadisticas();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🤖 Clasificador SVM</Text>
      
      <View style={styles.inputContainer}>
        <Text style={styles.label}>Característica 1:</Text>
        <TextInput
          style={styles.input}
          value={feature1}
          onChangeText={setFeature1}
          keyboardType="numeric"
          placeholder="Ingrese valor"
        />
      </View>
      
      <View style={styles.inputContainer}>
        <Text style={styles.label}>Característica 2:</Text>
        <TextInput
          style={styles.input}
          value={feature2}
          onChangeText={setFeature2}
          keyboardType="numeric"
          placeholder="Ingrese valor"
        />
      </View>
      
      <TouchableOpacity 
        style={styles.button} 
        onPress={realizarPrediccion}
        disabled={loading}
      >
        {loading ? (
          <ActivityIndicator color="white" />
        ) : (
          <Text style={styles.buttonText}>Clasificar</Text>
        )}
      </TouchableOpacity>
      
      {resultado && (
        <View style={[
          styles.resultContainer,
          resultado.prediccion === 1 ? styles.positivo : styles.negativo
        ]}>
          <Text style={styles.resultTitle}>Resultado:</Text>
          <Text>Clase: {resultado.prediccion === 1 ? 'Positiva' : 'Negativa'}</Text>
          <Text>Confianza: {resultado.confianza.toFixed(4)}</Text>
          <Text>Tiempo: {(resultado.tiempo * 1000).toFixed(2)}ms</Text>
        </View>
      )}
      
      <View style={styles.statsContainer}>
        <Text style={styles.statsTitle}>📊 Estadísticas</Text>
        <Text>Total predicciones: {estadisticas.total_predicciones || 0}</Text>
        <Text>Confianza promedio: {estadisticas.confianza_promedio?.toFixed(4) || 'N/A'}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 30,
    color: '#333',
  },
  inputContainer: {
    marginBottom: 20,
  },
  label: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 5,
    color: '#555',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 5,
    padding: 10,
    fontSize: 16,
    backgroundColor: 'white',
  },
  button: {
    backgroundColor: '#007bff',
    padding: 15,
    borderRadius: 5,
    alignItems: 'center',
    marginTop: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
  resultContainer: {
    marginTop: 20,
    padding: 15,
    borderRadius: 5,
    borderWidth: 1,
  },
  positivo: {
    backgroundColor: '#d4edda',
    borderColor: '#c3e6cb',
  },
  negativo: {
    backgroundColor: '#f8d7da',
    borderColor: '#f5c6cb',
  },
  resultTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  statsContainer: {
    marginTop: 20,
    padding: 15,
    backgroundColor: '#e9ecef',
    borderRadius: 5,
  },
  statsTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});

export default SVMClassifierApp;
'''

# =====================================================
# CASOS DE USO REALES PARA APLICACIONES WEB
# =====================================================

print("="*80)
print("CASOS DE USO REALES DE SVM EN APLICACIONES WEB")
print("="*80)

print("\n🌐 APLICACIONES WEB TÍPICAS DONDE SE USA SVM:")

print("\n1. 📧 FILTRO DE SPAM EN EMAIL")
print("   • Clasificar emails como spam o legítimos")
print("   • Características: palabras clave, remitente, asunto")
print("   • Implementación: API REST que recibe texto y retorna clasificación")

print("\n2. 🛒 DETECCIÓN DE FRAUDE EN E-COMMERCE")
print("   • Identificar transacciones fraudulentas")
print("   • Características: monto, ubicación, historial del usuario")
print("   • Implementación: Validación en tiempo real durante el checkout")

print("\n3. 📱 MODERACIÓN DE CONTENIDO EN REDES SOCIALES")
print("   • Clasificar comentarios como apropiados o inapropiados")
print("   • Características: texto, emojis, context")
print("   • Implementación: Filtro automático antes de publicar")

print("\n4. 🏥 DIAGNÓSTICO MÉDICO ASISTIDO")
print("   • Clasificar síntomas o imágenes médicas")
print("   • Características: síntomas, edad, historial médico")
print("   • Implementación: Herramienta de apoyo para profesionales")

print("\n5. 💰 APROBACIÓN DE PRÉSTAMOS")
print("   • Decidir si aprobar o rechazar una solicitud")
print("   • Características: ingresos, historial crediticio, edad")
print("   • Implementación: Sistema de evaluación automática")

print("\n💡 VENTAJAS DE SVM EN APLICACIONES WEB:")
print("   ✅ Rápidas predicciones en tiempo real")
print("   ✅ Buena precisión con datos limitados")
print("   ✅ Funciona bien con datos de alta dimensión")
print("   ✅ Robusto contra overfitting")
print("   ✅ Interpretable para toma de decisiones")

print("\n⚙️ ARQUITECTURA TÍPICA:")
print("   1. Frontend: Interfaz web (React/Vue/Angular)")
print("   2. Backend: API REST (Flask/FastAPI/Node.js)")
print("   3. ML Model: Modelo SVM entrenado (scikit-learn)")
print("   4. Database: Almacén de datos y predicciones")
print("   5. Monitoring: Dashboard para métricas del modelo")

print("\n🔄 FLUJO DE TRABAJO:")
print("   1. Usuario ingresa datos en la web")
print("   2. Frontend envía petición HTTP a la API")
print("   3. Backend procesa datos y usa modelo SVM")
print("   4. Se retorna predicción al frontend")
print("   5. Se guarda resultado en base de datos")
print("   6. Se muestra resultado al usuario")

print("\n" + "="*80)
print("EJEMPLO COMENTADO COMPLETO - LISTO PARA REFERENCIA")
print("="*80)
