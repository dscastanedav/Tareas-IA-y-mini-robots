"""
APLICACIÓN WEB DE ÁRBOLES DE DECISIÓN - EJEMPLO COMENTADO
=========================================================

Este archivo contiene un ejemplo completo de cómo adaptar árboles de decisión 
para una aplicación web. Incluye:

1. Backend con Flask para API REST
2. Frontend con HTML/JavaScript interactivo
3. Sistema de aprobación de préstamos
4. Dashboard con reglas de decisión
5. Aplicación móvil con React Native

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
import json

app = Flask(__name__)
CORS(app)

# Cargar modelo de árbol de decisión preentrenado
with open('arbol_decision.pkl', 'rb') as f:
    modelo_arbol = pickle.load(f)

# Configuración de base de datos
def init_db():
    '''Inicializa la base de datos para guardar solicitudes'''
    conn = sqlite3.connect('solicitudes.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATETIME,
            edad INTEGER,
            salario INTEGER,
            experiencia INTEGER,
            decision TEXT,
            confianza REAL,
            reglas_aplicadas TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def extraer_reglas_decision(modelo, sample):
    '''
    Extrae las reglas específicas que llevaron a una decisión
    '''
    tree = modelo.tree_
    feature_names = ['Edad', 'Salario', 'Experiencia']
    
    def get_path(node, sample, path=[]):
        if tree.feature[node] != -2:  # No es hoja
            feature = feature_names[tree.feature[node]]
            threshold = tree.threshold[node]
            
            if sample[tree.feature[node]] <= threshold:
                path.append(f"{feature} <= {threshold:.0f}")
                return get_path(tree.children_left[node], sample, path)
            else:
                path.append(f"{feature} > {threshold:.0f}")
                return get_path(tree.children_right[node], sample, path)
        else:
            clase = np.argmax(tree.value[node])
            confianza = np.max(tree.value[node]) / np.sum(tree.value[node])
            return path, clase, confianza
    
    reglas, clase, confianza = get_path(0, sample)
    return reglas, clase, confianza

@app.route('/')
def index():
    '''Página principal - Sistema de aprobación de préstamos'''
    return render_template('prestamos.html')

@app.route('/api/evaluar_prestamo', methods=['POST'])
def evaluar_prestamo():
    '''
    API endpoint para evaluar solicitudes de préstamo
    
    Recibe:
    - edad: edad del solicitante
    - salario: salario anual
    - experiencia: años de experiencia laboral
    
    Retorna:
    - decision: "aprobado" o "rechazado"
    - confianza: nivel de confianza (0-1)
    - reglas: reglas que llevaron a la decisión
    - recomendaciones: sugerencias para el solicitante
    '''
    try:
        datos = request.json
        edad = int(datos['edad'])
        salario = int(datos['salario'])
        experiencia = int(datos['experiencia'])
        
        # Validar datos
        if edad < 18 or edad > 100:
            return jsonify({'error': 'Edad debe estar entre 18 y 100 años'}), 400
        if salario < 0:
            return jsonify({'error': 'Salario debe ser positivo'}), 400
        if experiencia < 0:
            return jsonify({'error': 'Experiencia debe ser positiva'}), 400
        
        # Preparar datos para el modelo
        sample = np.array([[edad, salario, experiencia]])
        
        # Realizar predicción
        decision_numerica = modelo_arbol.predict(sample)[0]
        probabilidades = modelo_arbol.predict_proba(sample)[0]
        
        # Extraer reglas aplicadas
        reglas, clase, confianza = extraer_reglas_decision(modelo_arbol, sample[0])
        
        # Convertir a texto
        decision = "aprobado" if decision_numerica == 1 else "rechazado"
        
        # Generar recomendaciones
        recomendaciones = []
        if decision == "rechazado":
            if salario < 50000:
                recomendaciones.append("Incrementar ingresos a más de $50,000")
            if experiencia < 2:
                recomendaciones.append("Ganar más experiencia laboral (mínimo 2 años)")
            if edad < 25:
                recomendaciones.append("Considerar aplicar con un co-deudor")
        
        # Guardar en base de datos
        conn = sqlite3.connect('solicitudes.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO solicitudes 
            (fecha, edad, salario, experiencia, decision, confianza, reglas_aplicadas)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            datetime.now(), edad, salario, experiencia, 
            decision, confianza, json.dumps(reglas)
        ))
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'decision': decision,
            'confianza': float(confianza),
            'probabilidades': {
                'rechazo': float(probabilidades[0]),
                'aprobacion': float(probabilidades[1])
            },
            'reglas_aplicadas': reglas,
            'recomendaciones': recomendaciones,
            'datos_solicitante': {
                'edad': edad,
                'salario': salario,
                'experiencia': experiencia
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/estadisticas', methods=['GET'])
def estadisticas():
    '''Obtiene estadísticas de solicitudes procesadas'''
    conn = sqlite3.connect('solicitudes.db')
    cursor = conn.cursor()
    
    # Estadísticas generales
    cursor.execute('SELECT COUNT(*) FROM solicitudes')
    total_solicitudes = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM solicitudes WHERE decision = "aprobado"')
    aprobadas = cursor.fetchone()[0]
    
    cursor.execute('SELECT AVG(confianza) FROM solicitudes')
    confianza_promedio = cursor.fetchone()[0]
    
    cursor.execute('SELECT AVG(edad), AVG(salario), AVG(experiencia) FROM solicitudes WHERE decision = "aprobado"')
    perfil_aprobado = cursor.fetchone()
    
    conn.close()
    
    tasa_aprobacion = (aprobadas / total_solicitudes * 100) if total_solicitudes > 0 else 0
    
    return jsonify({
        'total_solicitudes': total_solicitudes,
        'solicitudes_aprobadas': aprobadas,
        'tasa_aprobacion': tasa_aprobacion,
        'confianza_promedio': confianza_promedio,
        'perfil_aprobado': {
            'edad_promedio': perfil_aprobado[0],
            'salario_promedio': perfil_aprobado[1],
            'experiencia_promedio': perfil_aprobado[2]
        }
    })

@app.route('/api/reglas_negocio', methods=['GET'])
def reglas_negocio():
    '''Retorna las reglas de negocio extraídas del árbol'''
    # En una aplicación real, estas reglas se extraerían automáticamente
    reglas = {
        'reglas_principales': [
            "Si Salario > 50000 y Experiencia > 2 años → Probable Aprobación",
            "Si Edad > 25 y Salario > 40000 → Revisar Experiencia",
            "Si Salario > 80000 → Aprobación Automática",
            "Si Edad > 40 y Experiencia > 10 años → Aprobación Probable"
        ],
        'factores_criticos': [
            "Salario es el factor más importante (45% de peso)",
            "Experiencia laboral es crucial (30% de peso)",
            "Edad influye moderadamente (25% de peso)"
        ],
        'umbrales_importantes': {
            'salario_minimo': 35000,
            'experiencia_minima': 1,
            'edad_minima': 18
        }
    }
    
    return jsonify(reglas)

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
    <title>Sistema de Aprobación de Préstamos - Árboles de Decisión</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            background-color: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        
        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #555;
            font-size: 1.1em;
        }
        
        input[type="number"] {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input[type="number"]:focus {
            border-color: #667eea;
            outline: none;
        }
        
        .btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            width: 100%;
            margin-top: 20px;
            transition: transform 0.2s;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        .resultado {
            margin-top: 30px;
            padding: 25px;
            border-radius: 10px;
            display: none;
            animation: fadeIn 0.5s;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .aprobado {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
        }
        
        .rechazado {
            background: linear-gradient(45deg, #f44336, #d32f2f);
            color: white;
        }
        
        .reglas-container {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        
        .regla {
            background-color: white;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            border-left: 4px solid #667eea;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
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
        <h1>🏦 Sistema de Aprobación de Préstamos</h1>
        <p style="text-align: center; font-size: 1.2em; color: #666;">
            Powered by Árboles de Decisión
        </p>
        
        <div class="form-grid">
            <div class="input-group">
                <label for="edad">🎂 Edad (años):</label>
                <input type="number" id="edad" min="18" max="100" placeholder="Ej: 30">
            </div>
            
            <div class="input-group">
                <label for="salario">💰 Salario Anual ($):</label>
                <input type="number" id="salario" min="0" placeholder="Ej: 65000">
            </div>
            
            <div class="input-group">
                <label for="experiencia">💼 Experiencia Laboral (años):</label>
                <input type="number" id="experiencia" min="0" placeholder="Ej: 5">
            </div>
        </div>
        
        <button class="btn" onclick="evaluarSolicitud()">Evaluar Solicitud</button>
        
        <div id="resultado" class="resultado">
            <h2>📋 Resultado de la Evaluación</h2>
            <div id="decision-texto"></div>
            <div id="confianza-texto"></div>
            <div id="reglas-aplicadas"></div>
            <div id="recomendaciones"></div>
        </div>
    </div>
    
    <div class="container">
        <h2>📊 Estadísticas del Sistema</h2>
        <div class="stats-grid" id="estadisticas">
            <div class="stat-card">
                <div class="stat-number" id="total-solicitudes">-</div>
                <div>Total Solicitudes</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="tasa-aprobacion">-</div>
                <div>Tasa de Aprobación</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="confianza-promedio">-</div>
                <div>Confianza Promedio</div>
            </div>
        </div>
        
        <button class="btn" onclick="cargarEstadisticas()">Actualizar Estadísticas</button>
    </div>
    
    <div class="container">
        <h2>🌳 Reglas de Negocio</h2>
        <div id="reglas-negocio" class="reglas-container">
            <div class="loading">Cargando reglas...</div>
        </div>
    </div>

    <script>
        // Función para evaluar solicitud de préstamo
        async function evaluarSolicitud() {
            const edad = parseInt(document.getElementById('edad').value);
            const salario = parseInt(document.getElementById('salario').value);
            const experiencia = parseInt(document.getElementById('experiencia').value);
            
            // Validar entrada
            if (isNaN(edad) || isNaN(salario) || isNaN(experiencia)) {
                alert('Por favor complete todos los campos');
                return;
            }
            
            if (edad < 18 || edad > 100) {
                alert('La edad debe estar entre 18 y 100 años');
                return;
            }
            
            // Mostrar loading
            const resultadoDiv = document.getElementById('resultado');
            resultadoDiv.style.display = 'block';
            resultadoDiv.className = 'resultado';
            document.getElementById('decision-texto').innerHTML = 
                '<div class="loading">Evaluando solicitud...</div>';
            
            try {
                const response = await fetch('/api/evaluar_prestamo', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        edad: edad,
                        salario: salario,
                        experiencia: experiencia
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    // Mostrar resultado
                    resultadoDiv.className = 'resultado ' + data.decision;
                    
                    const decision = data.decision === 'aprobado' ? '✅ APROBADO' : '❌ RECHAZADO';
                    document.getElementById('decision-texto').innerHTML = 
                        `<h3>${decision}</h3>`;
                    
                    document.getElementById('confianza-texto').innerHTML = 
                        `<p><strong>Confianza:</strong> ${(data.confianza * 100).toFixed(1)}%</p>
                         <p><strong>Probabilidad de Aprobación:</strong> ${(data.probabilidades.aprobacion * 100).toFixed(1)}%</p>`;
                    
                    // Mostrar reglas aplicadas
                    const reglasHtml = data.reglas_aplicadas.map(regla => 
                        `<div class="regla">📋 ${regla}</div>`
                    ).join('');
                    document.getElementById('reglas-aplicadas').innerHTML = 
                        `<h4>Reglas Aplicadas:</h4>${reglasHtml}`;
                    
                    // Mostrar recomendaciones
                    if (data.recomendaciones.length > 0) {
                        const recomendacionesHtml = data.recomendaciones.map(rec => 
                            `<li>${rec}</li>`
                        ).join('');
                        document.getElementById('recomendaciones').innerHTML = 
                            `<h4>💡 Recomendaciones:</h4><ul>${recomendacionesHtml}</ul>`;
                    } else {
                        document.getElementById('recomendaciones').innerHTML = 
                            '<p>✅ Perfil excelente para aprobación</p>';
                    }
                    
                    // Actualizar estadísticas
                    cargarEstadisticas();
                } else {
                    throw new Error(data.error);
                }
                
            } catch (error) {
                document.getElementById('decision-texto').innerHTML = 
                    `<strong>Error:</strong> ${error.message}`;
                resultadoDiv.className = 'resultado rechazado';
            }
        }
        
        // Función para cargar estadísticas
        async function cargarEstadisticas() {
            try {
                const response = await fetch('/api/estadisticas');
                const data = await response.json();
                
                document.getElementById('total-solicitudes').textContent = data.total_solicitudes;
                document.getElementById('tasa-aprobacion').textContent = 
                    data.tasa_aprobacion.toFixed(1) + '%';
                document.getElementById('confianza-promedio').textContent = 
                    data.confianza_promedio ? (data.confianza_promedio * 100).toFixed(1) + '%' : 'N/A';
                
            } catch (error) {
                console.error('Error al cargar estadísticas:', error);
            }
        }
        
        // Función para cargar reglas de negocio
        async function cargarReglas() {
            try {
                const response = await fetch('/api/reglas_negocio');
                const data = await response.json();
                
                let html = '<h3>🎯 Reglas Principales:</h3>';
                data.reglas_principales.forEach(regla => {
                    html += `<div class="regla">${regla}</div>`;
                });
                
                html += '<h3>⚡ Factores Críticos:</h3>';
                data.factores_criticos.forEach(factor => {
                    html += `<div class="regla">${factor}</div>`;
                });
                
                document.getElementById('reglas-negocio').innerHTML = html;
                
            } catch (error) {
                document.getElementById('reglas-negocio').innerHTML = 
                    '<p>Error al cargar reglas de negocio</p>';
            }
        }
        
        // Cargar datos al iniciar
        document.addEventListener('DOMContentLoaded', function() {
            cargarEstadisticas();
            cargarReglas();
        });
    </script>
</body>
</html>
'''

# =====================================================
# APLICACIÓN MÓVIL - EJEMPLO CON REACT NATIVE
# =====================================================

MOBILE_APP_EXAMPLE = '''
// Ejemplo de aplicación móvil para evaluación de préstamos
import React, { useState, useEffect } from 'react';
import {
  View, 
  Text, 
  TextInput, 
  TouchableOpacity, 
  StyleSheet, 
  Alert,
  ScrollView,
  ActivityIndicator
} from 'react-native';

const PrestamosApp = () => {
  const [edad, setEdad] = useState('');
  const [salario, setSalario] = useState('');
  const [experiencia, setExperiencia] = useState('');
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);
  const [estadisticas, setEstadisticas] = useState({});

  const evaluarSolicitud = async () => {
    const edadNum = parseInt(edad);
    const salarioNum = parseInt(salario);
    const experienciaNum = parseInt(experiencia);
    
    if (isNaN(edadNum) || isNaN(salarioNum) || isNaN(experienciaNum)) {
      Alert.alert('Error', 'Por favor complete todos los campos');
      return;
    }
    
    if (edadNum < 18 || edadNum > 100) {
      Alert.alert('Error', 'La edad debe estar entre 18 y 100 años');
      return;
    }
    
    setLoading(true);
    
    try {
      const response = await fetch('https://tu-servidor.com/api/evaluar_prestamo', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          edad: edadNum,
          salario: salarioNum,
          experiencia: experienciaNum
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
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>🏦 Evaluación de Préstamos</Text>
        <Text style={styles.subtitle}>Árboles de Decisión</Text>
      </View>
      
      <View style={styles.form}>
        <View style={styles.inputGroup}>
          <Text style={styles.label}>🎂 Edad (años)</Text>
          <TextInput
            style={styles.input}
            value={edad}
            onChangeText={setEdad}
            keyboardType="numeric"
            placeholder="Ej: 30"
          />
        </View>
        
        <View style={styles.inputGroup}>
          <Text style={styles.label}>💰 Salario Anual ($)</Text>
          <TextInput
            style={styles.input}
            value={salario}
            onChangeText={setSalario}
            keyboardType="numeric"
            placeholder="Ej: 65000"
          />
        </View>
        
        <View style={styles.inputGroup}>
          <Text style={styles.label}>💼 Experiencia (años)</Text>
          <TextInput
            style={styles.input}
            value={experiencia}
            onChangeText={setExperiencia}
            keyboardType="numeric"
            placeholder="Ej: 5"
          />
        </View>
        
        <TouchableOpacity 
          style={styles.button} 
          onPress={evaluarSolicitud}
          disabled={loading}
        >
          {loading ? (
            <ActivityIndicator color="white" />
          ) : (
            <Text style={styles.buttonText}>Evaluar Solicitud</Text>
          )}
        </TouchableOpacity>
      </View>
      
      {resultado && (
        <View style={[
          styles.resultContainer,
          resultado.decision === 'aprobado' ? styles.aprobado : styles.rechazado
        ]}>
          <Text style={styles.resultTitle}>
            {resultado.decision === 'aprobado' ? '✅ APROBADO' : '❌ RECHAZADO'}
          </Text>
          <Text style={styles.resultText}>
            Confianza: {(resultado.confianza * 100).toFixed(1)}%
          </Text>
          <Text style={styles.resultText}>
            Probabilidad: {(resultado.probabilidades.aprobacion * 100).toFixed(1)}%
          </Text>
          
          <View style={styles.rulesContainer}>
            <Text style={styles.rulesTitle}>Reglas Aplicadas:</Text>
            {resultado.reglas_aplicadas.map((regla, index) => (
              <Text key={index} style={styles.ruleText}>• {regla}</Text>
            ))}
          </View>
          
          {resultado.recomendaciones.length > 0 && (
            <View style={styles.recommendationsContainer}>
              <Text style={styles.recommendationsTitle}>💡 Recomendaciones:</Text>
              {resultado.recomendaciones.map((rec, index) => (
                <Text key={index} style={styles.recommendationText}>• {rec}</Text>
              ))}
            </View>
          )}
        </View>
      )}
      
      <View style={styles.statsContainer}>
        <Text style={styles.statsTitle}>📊 Estadísticas del Sistema</Text>
        <View style={styles.statsGrid}>
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>{estadisticas.total_solicitudes || 0}</Text>
            <Text style={styles.statLabel}>Total Solicitudes</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>
              {estadisticas.tasa_aprobacion ? estadisticas.tasa_aprobacion.toFixed(1) + '%' : '0%'}
            </Text>
            <Text style={styles.statLabel}>Tasa Aprobación</Text>
          </View>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    backgroundColor: '#667eea',
    padding: 30,
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 5,
  },
  subtitle: {
    fontSize: 16,
    color: 'rgba(255,255,255,0.8)',
  },
  form: {
    padding: 20,
    backgroundColor: 'white',
    margin: 20,
    borderRadius: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 5 },
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  inputGroup: {
    marginBottom: 20,
  },
  label: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 8,
    color: '#333',
  },
  input: {
    borderWidth: 2,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    backgroundColor: '#fafafa',
  },
  button: {
    backgroundColor: '#667eea',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  resultContainer: {
    margin: 20,
    padding: 20,
    borderRadius: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 5 },
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  aprobado: {
    backgroundColor: '#4CAF50',
  },
  rechazado: {
    backgroundColor: '#f44336',
  },
  resultTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 10,
  },
  resultText: {
    fontSize: 16,
    color: 'white',
    marginBottom: 5,
  },
  rulesContainer: {
    marginTop: 15,
    padding: 15,
    backgroundColor: 'rgba(255,255,255,0.2)',
    borderRadius: 8,
  },
  rulesTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 10,
  },
  ruleText: {
    fontSize: 14,
    color: 'white',
    marginBottom: 5,
  },
  recommendationsContainer: {
    marginTop: 15,
    padding: 15,
    backgroundColor: 'rgba(255,255,255,0.2)',
    borderRadius: 8,
  },
  recommendationsTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 10,
  },
  recommendationText: {
    fontSize: 14,
    color: 'white',
    marginBottom: 5,
  },
  statsContainer: {
    margin: 20,
    padding: 20,
    backgroundColor: 'white',
    borderRadius: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 5 },
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  statsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 15,
    textAlign: 'center',
  },
  statsGrid: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  statCard: {
    alignItems: 'center',
    flex: 1,
  },
  statNumber: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#667eea',
  },
  statLabel: {
    fontSize: 12,
    color: '#666',
    textAlign: 'center',
  },
});

export default PrestamosApp;
'''

# =====================================================
# CASOS DE USO REALES PARA ÁRBOLES DE DECISIÓN
# =====================================================

print("="*80)
print("CASOS DE USO REALES DE ÁRBOLES DE DECISIÓN EN APLICACIONES WEB")
print("="*80)

print("\n🌐 APLICACIONES WEB TÍPICAS DONDE SE USAN ÁRBOLES DE DECISIÓN:")

print("\n1. 🏦 APROBACIÓN DE PRÉSTAMOS Y CRÉDITOS")
print("   • Evaluar solicitudes de préstamos automáticamente")
print("   • Características: ingresos, historial crediticio, edad, empleo")
print("   • Implementación: Sistema de evaluación en tiempo real")

print("\n2. 🩺 DIAGNÓSTICO MÉDICO ASISTIDO")
print("   • Ayudar en diagnósticos basados en síntomas")
print("   • Características: síntomas, edad, historial médico")
print("   • Implementación: Sistema de apoyo para médicos")

print("\n3. 🎯 SEGMENTACIÓN DE CLIENTES")
print("   • Clasificar clientes por comportamiento de compra")
print("   • Características: edad, ingresos, historial de compras")
print("   • Implementación: Personalización de ofertas")

print("\n4. 🔍 DETECCIÓN DE FRAUDE")
print("   • Identificar transacciones sospechosas")
print("   • Características: monto, ubicación, hora, frecuencia")
print("   • Implementación: Sistema de alertas automáticas")

print("\n5. 📚 SISTEMAS DE RECOMENDACIÓN")
print("   • Recomendar productos o contenido")
print("   • Características: historial, preferencias, demografía")
print("   • Implementación: Motor de recomendaciones personalizado")

print("\n6. 🏢 SELECCIÓN DE RECURSOS HUMANOS")
print("   • Filtrar candidatos en procesos de selección")
print("   • Características: experiencia, educación, habilidades")
print("   • Implementación: Sistema de pre-selección automática")

print("\n💡 VENTAJAS DE ÁRBOLES DE DECISIÓN EN APLICACIONES WEB:")
print("   ✅ Reglas claras y comprensibles")
print("   ✅ Fácil explicación de decisiones")
print("   ✅ No requiere normalización de datos")
print("   ✅ Maneja datos categóricos y numéricos")
print("   ✅ Identificación automática de patrones")
print("   ✅ Rápidas predicciones en tiempo real")
print("   ✅ Cumplimiento regulatorio (explicabilidad)")

print("\n⚙️ ARQUITECTURA TÍPICA:")
print("   1. Frontend: Interfaz web (React/Vue/Angular)")
print("   2. Backend: API REST (Flask/FastAPI/Node.js)")
print("   3. ML Model: Árbol de decisión entrenado")
print("   4. Database: Almacén de datos y decisiones")
print("   5. Dashboard: Visualización de reglas y métricas")

print("\n🔄 FLUJO DE TRABAJO:")
print("   1. Usuario ingresa datos en formulario web")
print("   2. Frontend valida y envía datos a API")
print("   3. Backend aplica árbol de decisión")
print("   4. Se extraen reglas aplicadas")
print("   5. Se retorna decisión con explicación")
print("   6. Se almacena resultado para auditoria")
print("   7. Se muestra resultado y reglas al usuario")

print("\n🎯 EJEMPLO DE IMPLEMENTACIÓN - APROBACIÓN DE PRÉSTAMOS:")
print("   • Input: Edad, Salario, Experiencia")
print("   • Proceso: Árbol evalúa cada característica")
print("   • Output: Aprobado/Rechazado + Reglas + Recomendaciones")
print("   • Ventaja: Decisiones auditables y explicables")

print("\n" + "="*80)
print("EJEMPLO COMENTADO COMPLETO - ÁRBOLES DE DECISIÓN")
print("="*80)
