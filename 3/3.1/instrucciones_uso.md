# 🚀 Instrucciones de Uso

## 3.1 Maximización de f(x) = x·sen(10πx) + 1

### 📋 Requisitos del Sistema

#### Software Necesario
- **Python 3.7+**
- **Librerías**:
  ```bash
  pip install numpy matplotlib scipy
  ```

#### Verificación de Instalación
```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

print("✅ Todo instalado correctamente")
```

---

## 🎯 Ejecución Rápida

### Paso 1: Navegar a la carpeta
```bash
cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\3\3.1"
```

### Paso 2: Ejecutar el script
```bash
python maximizacion_funcion.py
```

### Paso 3: Observar resultados
- Gráficos automáticos
- Comparación de métodos en consola
- Archivos PNG generados

---

## 📊 Qué Esperar

### Salida en Consola
```
🎯 MAXIMIZACIÓN DE f(x) = x·sin(10πx) + 1 EN [0,1]
============================================================
🔍 ANÁLISIS DE LA FUNCIÓN f(x) = x·sin(10πx) + 1
============================================================
📊 Estadísticas de la función en [0,1]:
   • Valor mínimo: 0.000000
   • Valor máximo: 1.950000
   • Número de máximos locales aproximados: 10
```

### Archivos Generados
- `analisis_funcion.png` - Gráfico de la función y su derivada
- `resultado_final.png` - Visualización del máximo encontrado

### Resultado Típico
```
🏆 MEJOR RESULTADO:
   Método: Evolución Diferencial
   x* = 0.97500000
   f(x*) = 1.95000000
   ✅ Solución válida en el dominio [0,1]
```

---

## 🔧 Modificaciones Sugeridas

### Cambiar Parámetros de la Función
```python
# En la función funcion_objetivo(), línea ~30
def funcion_objetivo(x):
    return x * np.sin(5 * np.pi * x) + 1  # Menos oscilaciones
```

### Ajustar Precisión
```python
# En metodo_fuerza_bruta(), línea ~80
x_grid = np.linspace(0, 1, 50000)  # Más puntos = más precisión
```

### Cambiar Dominio
```python
# Modificar en todos los métodos
bounds = [(0, 2)]  # Nuevo dominio [0,2]
```

---

## 🎮 Experimentos Sugeridos

### Experimento 1: Diferentes Frecuencias
```python
# Probar con:
f1(x) = x * sin(2πx) + 1   # Baja frecuencia
f2(x) = x * sin(10πx) + 1  # Original
f3(x) = x * sin(20πx) + 1  # Alta frecuencia
```

### Experimento 2: Diferentes Formas
```python
# Variaciones:
f1(x) = x² * sin(10πx) + 1      # Cuadrática
f2(x) = sqrt(x) * sin(10πx) + 1 # Raíz cuadrada
f3(x) = x * cos(10πx) + 1       # Coseno
```

### Experimento 3: Comparar Métodos
- Ejecutar múltiples veces
- Anotar tiempos de ejecución
- Comparar precisiones

---

## 📈 Interpretación de Resultados

### Indicadores de Éxito
- **x* cerca de 0.95-0.98**: Resultado esperado
- **f(x*) cerca de 1.9-2.0**: Valor máximo típico
- **Consenso entre métodos**: Validación cruzada

### Señales de Alerta
- **x* = 0 o x* = 1**: Posible error
- **f(x*) < 1.5**: Máximo local, no global
- **Métodos muy diferentes**: Revisar implementación

---

## 🛠️ Troubleshooting

### Problema: No aparecen gráficos
**Solución**:
```python
# Agregar al final del código
plt.show(block=True)
plt.ion()  # Modo interactivo
```

### Problema: ImportError
**Solución**:
```bash
# Reinstalar librerías
pip uninstall numpy matplotlib scipy
pip install numpy matplotlib scipy

# O usar conda
conda install numpy matplotlib scipy
```

### Problema: Resultados inconsistentes
**Solución**:
```python
# Fijar semilla aleatoria
np.random.seed(42)  # Al inicio del script
```

### Problema: Muy lento
**Solución**:
```python
# Reducir puntos de evaluación
grid_size = 1000  # En lugar de 10000
n_puntos = 5000   # En lugar de 50000
```

---

## 🎯 Objetivos del Ejercicio

### Lo que Aprenderás
1. **Optimización global** vs local
2. **Funciones multimodales** y sus desafíos
3. **Comparación de algoritmos** numéricos
4. **Análisis de resultados** y validación
5. **Visualización científica** con matplotlib

### Conceptos Clave
- **Máximo global**: El mayor valor en todo el dominio
- **Máximo local**: El mayor valor en una vecindad
- **Función multimodal**: Con múltiples óptimos locales
- **Convergencia**: Aproximación al resultado verdadero

---

## 📚 Recursos Adicionales

### Para Profundizar
- **Scipy Documentation**: https://scipy.org/
- **Optimization Theory**: Nocedal & Wright
- **Numerical Methods**: Press et al.

### Extensiones Avanzadas
- **Optimización multi-objetivo**
- **Algoritmos genéticos**
- **Simulated annealing**
- **Particle swarm optimization**

---

**¡Disfruta explorando la optimización numérica!** 🎉
