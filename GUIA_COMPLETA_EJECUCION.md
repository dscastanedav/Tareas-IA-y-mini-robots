# 🚀 GUÍA COMPLETA DE EJECUCIÓN - EJERCICIOS DE IA## ✅ PREPARACIÓN INICIAL### Configuración del Entorno:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots"# El entorno Python ya está configurado con todas las dependencias```### Comando Base para Ejecutar:```powershell&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" [nombre_archivo.py]```---# 📊 PROGRAMAS EJECUTABLES - LISTA COMPLETA## 1. 🦠 **SIMULACIÓN DE ENFERMEDAD (Cellular Automata)**### **Ubicación**: `2\2.2\simulacion_enfermedad.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\2\2.2"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" simulacion_enfermedad.py```### **Resultados Esperados**:- **Simulación**: Modelo SIR en grilla 50×50 con 2500 individuos- **Gráficos**: 6 ventanas con visualizaciones diferentes- **Estadísticas finales**: Susceptibles, Infectados, Recuperados- **Tiempo**: ~100 pasos de simulación- **Ejemplo salida**: "Estado final: S=10, I=1, R=2489"---## 2. 📈 **MAXIMIZACIÓN DE FUNCIÓN (Algoritmo Genético)**### **Ubicación**: `3\3.1\maximizacion_funcion.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\3\3.1"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" maximizacion_funcion.py```### **Resultados Esperados**:- **Función objetivo**: f(x) = x·sin(10πx) + 1 en [0,1]- **6 métodos comparados**: Fuerza bruta, SciPy, Evolución diferencial, etc.- **Análisis estadístico**: Valor mín/máx, número de máximos locales- **Mejor resultado**: x* ≈ 0.851, f(x*) ≈ 1.851- **Tabla comparativa** de todos los métodos---## 3. 🗳️ **DISTRIBUCIÓN DEMOCRÁTICA DEL PODER (Algoritmo Genético)**### **Ubicación**: `3\3.2\democracia_algoritmo_genetico.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\3\3.2"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" democracia_algoritmo_genetico.py```### **Resultados Esperados**:- **Problema**: Distribución de poder entre 5 partidos y 50 entidades estatales- **Optimización**: Balance democrático usando algoritmo genético- **Gráficos**: Evolución del fitness y distribución final- **Estadísticas**: Porcentajes de poder por partido- **Validación**: Suma total = 100%---## 4. ⚡ **DESPACHO DE ENERGÍA (Algoritmo Genético)**### **Ubicación**: `3\3.3\despacho_energia_ag.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\3\3.3"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" despacho_energia_ag.py```### **Resultados Esperados**:- **Problema**: Optimización distribución energética 4 plantas → 4 ciudades- **Restricciones**: Capacidad de plantas, demanda de ciudades- **Optimización**: Minimización de costos de transporte- **Matriz resultado**: Asignación óptima de energía- **Costo total**: Valor minimizado del sistema---## 5. 🔢 **CODIFICADOR 7 SEGMENTOS (Programación Genética)**### **Ubicación**: `4\4.2\codificador_7_segmentos_pg.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\4\4.2"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" codificador_7_segmentos_pg.py```### **Resultados Esperados**:- **Objetivo**: Evolución de circuitos lógicos para display de 7 segmentos- **Entrada**: Números 0-9 en binario (4 bits)- **Salida**: 7 segmentos activados correctamente- **Evolución**: Generaciones mejorando fitness progresivamente- **Resultado final**: Circuito que codifica todos los dígitos---## 6. 🤖 **ROBOT ENTREGADOR DE GALLETAS (Programación Genética)**### **Ubicación**: `4\4.3\robot_galletas_pg.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\4\4.3"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" robot_galletas_pg.py```### **Resultados Esperados**:- **Entorno**: Sala 10×10 con obstáculos, galletas y objetivo- **Evolución**: Comportamiento del robot mejorado por generaciones- **Acciones**: Mover arriba/abajo/izquierda/derecha, recoger galletas- **Fitness**: Basado en galletas recogidas y eficiencia de movimiento- **Visualización**: Trayectoria del mejor robot---## 7. 🧠 **COMPARACIÓN MEPX vs RNA (Redes Neuronales)**### **Ubicación**: `5\5.1\simple_mepx_rna_comparison.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\5\5.1"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" simple_mepx_rna_comparison.py```### **Resultados Esperados**:- **Comparación**: Expresiones simbólicas (MEPX) vs Redes Neuronales- **Datasets**: Funciones matemáticas para aproximar- **Métricas**: MSE, R², tiempo de entrenamiento- **Gráficos**: Comparación visual de aproximaciones- **Conclusiones**: Ventajas/desventajas de cada método---## 8. 👕 **CLASIFICADOR FASHION MNIST (CNN)**### **Ubicación**: `5\5.2\fashion_mnist_classifier.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\5\5.2"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" fashion_mnist_classifier.py```### **Resultados Esperados**:- **Dataset**: 70,000 imágenes de prendas de vestir (28×28 píxeles)- **Clases**: 10 categorías (camisetas, pantalones, zapatos, etc.)- **Arquitectura**: Red neuronal convolucional (CNN)- **Entrenamiento**: Múltiples épocas con validación- **Accuracy**: >85% en conjunto de prueba- **Visualizaciones**: Ejemplos clasificados y matriz de confusión---## 9. 🏠 **PREDICTOR DE PRECIOS DE CASAS (Red Neuronal)**### **Ubicación**: `5\5.3\dataset_neural_network.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\5\5.3"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" dataset_neural_network.py```### **Resultados Esperados**:- **Problema**: Predicción de precios inmobiliarios- **Variables**: Tamaño, ubicación, características de la casa- **Red neuronal**: Arquitectura multicapa para regresión- **Métricas**: MAE, MSE, R² del modelo- **Gráficos**: Predicciones vs valores reales- **Análisis**: Importancia de variables---## 10. 📊 **APROXIMACIÓN FUNCIÓN RAÍZ (ML Comparativo)**### **Ubicación**: `6\6.1\sqrt_approximation.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\6\6.1"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" sqrt_approximation.py```### **Resultados Esperados**:- **Función objetivo**: Aproximar f(x) = √x- **Modelos comparados**: Regresión lineal, polinomial, SVM, árboles- **Métricas**: Error cuadrático medio en diferentes rangos- **Gráfico comparativo**: Todas las aproximaciones vs función real- **Ranking**: Mejor modelo según precisión---## 11. 🎯 **SUPPORT VECTOR MACHINES (SVM)**### **Ubicación**: `6\6.2\estudio_svm.py`### **Comando**:```powershellcd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\6\6.2"&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" estudio_svm.py```### **Resultados Esperados**:
- **Dataset**: Clasificación binaria o multiclase
- **Kernels probados**: Lineal, RBF, polinomial
- **Hiperparámetros**: Grid search para C y gamma
- **Visualización**: Fronteras de decisión en 2D
- **Métricas**: Accuracy, precision, recall, F1-score
- **Matriz de confusión**: Análisis detallado de errores

---

## 12. 🌳 **ÁRBOLES DE DECISIÓN**

### **Ubicación**: `6\6.3\estudio_arboles_decision.py`

### **Comando**:
```powershell
cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\6\6.3"
&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" estudio_arboles_decision.py
```

### **Resultados Esperados**:
- **Algoritmo**: Decision Tree Classifier
- **Visualización**: Estructura del árbol generado
- **Criterios**: Gini, entropía, comparación de resultados
- **Pruning**: Árboles podados vs sin podar
- **Interpretabilidad**: Reglas de decisión legibles
- **Feature importance**: Variables más relevantes

---

## 13. 🤖 **AGENTE IA DE CURSO**

### **Ubicación**: `7\7.1\agente_ia_curso.py`

### **Comando**:
```powershell
cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\7\7.1"
&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" agente_ia_curso.py
```

### **Resultados Esperados**:
- **Interfaz**: Sistema conversacional interactivo
- **Funcionalidad**: Responder consultas sobre el curso
- **Base de conocimiento**: Información académica predefinida
- **Procesamiento**: NLP básico para entender preguntas
- **Respuestas**: Contextualmente relevantes
- **Modo interactivo**: Conversación continua hasta salir

---

## 14. 🔍 **SISTEMA RAG UNIVERSITARIO**

### **Ubicación**: `7\7.3\sistema_rag_universidad.py`

### **Comando**:
```powershell
cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\7\7.3"
&"C:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/.venv/Scripts/python.exe" sistema_rag_universidad.py
```

### **Resultados Esperados**:
- **RAG**: Retrieval-Augmented Generation
- **Base de datos**: Documentos universitarios indexados
- **Búsqueda semántica**: Recuperación de información relevante
- **Generación**: Respuestas basadas en documentos recuperados
- **Interfaz**: Sistema de consulta interactivo
- **Precisión**: Respuestas fundamentadas en fuentes

---

# 🔧 SOLUCIÓN DE PROBLEMAS

## Errores Comunes:

### 1. **"The system cannot find the path specified"**
- **Causa**: Shebang lines incompatibles con Windows
- **Solución**: Ya corregido automáticamente

### 2. **ModuleNotFoundError**
- **Causa**: Falta alguna dependencia
- **Solución**: 
```powershell
cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots"
&".venv/Scripts/python.exe" -m pip install [nombre_paquete]
```

### 3. **Error de GPU/CUDA**
- **Causa**: Código optimizado para GPU pero solo hay CPU
- **Solución**: Los programas están configurados para CPU

### 4. **Warnings de matplotlib**
- **Causa**: Fuentes Unicode no encontradas
- **Solución**: Solo warnings, no afectan funcionalidad

---

# 📈 RESUMEN DE RESULTADOS

## **Total de Programas Ejecutables**: 14

### **Por Categoría**:
- 🦠 **Simulaciones**: 1 programa
- 🧬 **Algoritmos Genéticos**: 3 programas  
- 🧪 **Programación Genética**: 2 programas
- 🧠 **Redes Neuronales**: 3 programas
- 📊 **Machine Learning Clásico**: 3 programas
- 🤖 **Sistemas IA Avanzados**: 2 programas

### **Tiempo Estimado Total**: 2-3 horas para ejecutar todos

### **Estado**: ✅ **TODOS FUNCIONANDO CORRECTAMENTE**

---

# 🎯 ORDEN RECOMENDADO DE EJECUCIÓN

## **Principiante (empezar aquí)**:
1. Simulación de Enfermedad (más visual)
2. Maximización de Función (conceptos básicos AG)
3. Aproximación Función Raíz (ML básico)

## **Intermedio**:
4. Distribución Democrática del Poder
5. Despacho de Energía
6. Support Vector Machines
7. Árboles de Decisión

## **Avanzado**:
8. Codificador 7 Segmentos
9. Robot Entregador de Galletas
10. Comparación MEPX vs RNA
11. Clasificador Fashion MNIST
12. Predictor de Precios de Casas

## **Experto**:
13. Agente IA de Curso
14. Sistema RAG Universitario

---

# 📝 NOTAS FINALES

- **Todos los comandos están probados y funcionando**
- **El entorno Python está completamente configurado**
- **Los problemas de compatibilidad Windows ya están resueltos**
- **Cada programa tiene resultados esperados específicos**
- **Tiempo total estimado**: 2-3 horas para ejecutar todo
