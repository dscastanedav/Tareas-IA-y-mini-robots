# 🎯 Maximización de Función

## 3.1 Optimización de f(x) = x·sen(10πx) + 1

### 📋 Descripción del Problema

Este proyecto implementa diferentes métodos para encontrar el **máximo global** de la función:

```
f(x) = x · sen(10πx) + 1
```

En el intervalo **x ∈ [0,1]**.

### 🎯 Objetivo

Encontrar el valor de **x*** que maximiza la función, es decir:

```
x* = arg max f(x)    para x ∈ [0,1]
x*
```

---

## 🔬 Análisis de la Función

### Características Matemáticas

- **Dominio**: [0, 1]
- **Rango**: Aproximadamente [0, 2]
- **Tipo**: Función multimodal (múltiples máximos locales)
- **Derivada**: f'(x) = sen(10πx) + 10πx·cos(10πx)

### Comportamiento

1. **Múltiples máximos locales**: Debido al término sen(10πx)
2. **Crecimiento general**: El factor x hace que los valores aumenten hacia x=1
3. **Oscilaciones rápidas**: 10π ≈ 31.4 oscilaciones en [0,1]

---

## 🛠️ Métodos Implementados

### 1. 🔨 Fuerza Bruta
- **Descripción**: Evalúa la función en una grilla muy fina
- **Ventajas**: Garantiza encontrar el óptimo global
- **Desventajas**: Computacionalmente costoso

### 2. 🔬 SciPy Brute Force
- **Descripción**: Usa `scipy.optimize.brute`
- **Ventajas**: Implementación optimizada
- **Desventajas**: Limitado por el tamaño de grilla

### 3. 🥇 Sección Dorada
- **Descripción**: Método clásico de optimización
- **Ventajas**: Rápido y eficiente
- **Desventajas**: Solo encuentra máximo local

### 4. 🧬 Evolución Diferencial
- **Descripción**: Algoritmo evolutivo global
- **Ventajas**: Excelente para optimización global
- **Desventajas**: Estocástico, puede variar

### 5. 🎲 Búsqueda Aleatoria
- **Descripción**: Monte Carlo con puntos aleatorios
- **Ventajas**: Simple y robusto
- **Desventajas**: Requiere muchas evaluaciones

### 6. 📐 Análisis de Derivada
- **Descripción**: Encuentra puntos críticos analíticamente
- **Ventajas**: Matemáticamente riguroso
- **Desventajas**: Complejo para funciones oscilatorias

---

## 🚀 Cómo Ejecutar

### Requisitos

```bash
pip install numpy matplotlib scipy
```

### Ejecución

```bash
cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\3\3.1"
python maximizacion_funcion.py
```

### Salida Esperada

1. **Análisis de la función**: Gráfico y características
2. **Comparación de métodos**: Resultados de cada algoritmo
3. **Mejor resultado**: Método ganador y visualización
4. **Archivos generados**:
   - `analisis_funcion.png`
   - `resultado_final.png`

---

## 📊 Resultados Esperados

### Máximo Global Aproximado
- **x*** ≈ 0.95 - 0.98
- **f(x*)** ≈ 1.85 - 1.95

### Métodos Más Confiables
1. **Evolución Diferencial**: Mejor balance precisión/eficiencia
2. **Fuerza Bruta**: Más preciso pero más lento
3. **Análisis Derivada**: Matemáticamente riguroso

---

## 🔍 Interpretación Matemática

### ¿Por qué es Difícil este Problema?

1. **Función multimodal**: Muchos máximos locales
2. **Oscilaciones rápidas**: 10π ciclos en [0,1]
3. **Tendencia creciente**: El factor x sesga hacia x=1

### Estrategias de Solución

- **Métodos globales**: Para evitar máximos locales
- **Alta resolución**: Para capturar oscilaciones finas
- **Combinación de métodos**: Validación cruzada

---

## 📈 Análisis de Sensibilidad

### Efecto de Parámetros

```python
# Frecuencia más baja: f(x) = x·sin(2πx) + 1
# Resultado: Menos máximos locales, más fácil

# Frecuencia más alta: f(x) = x·sin(20πx) + 1  
# Resultado: Más máximos locales, más difícil
```

### Validación de Resultados

1. **Verificar dominio**: x* ∈ [0,1]
2. **Comparar métodos**: Consenso entre algoritmos
3. **Análisis visual**: Confirmar en gráfico

---

## 🎛️ Variaciones del Problema

### Funciones Similares

```python
# Variación 1: Cambiar amplitud
f1(x) = 2*x * sin(10*π*x) + 1

# Variación 2: Cambiar frecuencia  
f2(x) = x * sin(5*π*x) + 1

# Variación 3: Función diferente
f3(x) = x² * sin(10*π*x) + 1
```

### Extensiones Posibles

1. **Optimización multi-objetivo**
2. **Restricciones adicionales**
3. **Función en múltiples variables**
4. **Optimización dinámica**

---

## 🔧 Troubleshooting

### Problemas Comunes

**Error de importación**:
```bash
pip install --upgrade scipy matplotlib numpy
```

**Gráficos no aparecen**:
```python
plt.show(block=True)
```

**Resultados inconsistentes**:
- Verificar semillas aleatorias
- Aumentar número de evaluaciones
- Usar múltiples ejecuciones

---

## 📚 Referencias Teóricas

### Optimización Global
- **Algoritmos evolutivos**: Holland, Goldberg
- **Simulated Annealing**: Kirkpatrick et al.
- **Particle Swarm**: Kennedy & Eberhart

### Análisis de Funciones
- **Análisis de Fourier**: Para funciones oscilatorias
- **Teoría de aproximación**: Métodos numéricos
- **Cálculo variacional**: Optimización continua

---

## 🎯 Objetivos de Aprendizaje

Después de este ejercicio deberías entender:

1. **Optimización global vs local**
2. **Métodos determinísticos vs estocásticos**
3. **Análisis de funciones multimodales**
4. **Comparación de algoritmos**
5. **Validación de resultados numéricos**

---

**Nota**: Este es un problema clásico en optimización global que ilustra las dificultades de encontrar óptimos en funciones oscilatorias.
