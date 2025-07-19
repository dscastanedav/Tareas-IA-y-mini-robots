# 📐 Análisis Matemático Teórico

## 3.1 Estudio Analítico de f(x) = x·sen(10πx) + 1

### 🔢 Propiedades Matemáticas

#### Función Original
```
f(x) = x · sen(10πx) + 1
```

#### Derivada Primera
```
f'(x) = d/dx [x · sen(10πx) + 1]
f'(x) = sen(10πx) + x · 10π · cos(10πx)
f'(x) = sen(10πx) + 10πx · cos(10πx)
```

#### Derivada Segunda
```
f''(x) = d/dx [sen(10πx) + 10πx · cos(10πx)]
f''(x) = 10π · cos(10πx) + 10π · cos(10πx) - 100π²x · sen(10πx)
f''(x) = 20π · cos(10πx) - 100π²x · sen(10πx)
```

---

## 🎯 Análisis de Puntos Críticos

### Condición Necesaria para Máximo
Para que x* sea un máximo local:
```
f'(x*) = 0
sen(10πx*) + 10πx* · cos(10πx*) = 0
```

### Reorganizando la Ecuación
```
sen(10πx*) = -10πx* · cos(10πx*)
tan(10πx*) = -10πx*    (cuando cos(10πx*) ≠ 0)
```

### Número de Soluciones
En el intervalo [0,1]:
- La función sen(10πx) completa **10 ciclos** (0 a 10π)
- Esto genera aproximadamente **20 puntos críticos**
- Algunos son máximos, otros mínimos

---

## 📊 Comportamiento Asintótico

### Análisis de Términos

1. **Término lineal**: x
   - Crece monotónicamente de 0 a 1
   - Sesga la función hacia valores altos cerca de x=1

2. **Término oscilatorio**: sen(10πx)
   - Oscila entre -1 y +1
   - Frecuencia alta: 10π ≈ 31.4 rad en [0,1]

3. **Producto**: x·sen(10πx)
   - Amplitud variable: crece con x
   - Oscilaciones más pronunciadas cerca de x=1

### Estimación del Máximo Global

**Intuición matemática**:
- El máximo probablemente está cerca de x=1 (donde x es máximo)
- Debe coincidir con un máximo local de sen(10πx)
- Candidatos: x ≈ 0.95, 0.975, etc.

---

## 🔍 Análisis de Frecuencia

### Transformada de Fourier (Conceptual)

La función puede descomponerse como:
```
f(x) = 1 + x · sen(10πx)
     = 1 + (1/2i)[x·e^(i10πx) - x·e^(-i10πx)]
```

### Componentes de Frecuencia
- **Componente DC**: +1 (constante)
- **Componente fundamental**: 10π rad/unidad
- **Modulación de amplitud**: lineal en x

---

## 🧮 Métodos Analíticos Aproximados

### Método 1: Serie de Taylor
Alrededor de un punto x₀:
```
f(x) ≈ f(x₀) + f'(x₀)(x-x₀) + (1/2)f''(x₀)(x-x₀)²
```

### Método 2: Aproximación de Máximos
Para encontrar máximos de sen(10πx):
```
10πx = π/2 + 2πk  →  x = 1/20 + k/5
```
donde k = 0, 1, 2, ..., 4

### Candidatos a Máximo Global
```
x₁ = 0.05  →  f(0.05) ≈ 1.05
x₂ = 0.25  →  f(0.25) ≈ 1.25  
x₃ = 0.45  →  f(0.45) ≈ 1.45
x₄ = 0.65  →  f(0.65) ≈ 1.65
x₅ = 0.85  →  f(0.85) ≈ 1.85
```

**Predicción**: El máximo está cerca de x₅ = 0.85

---

## 📈 Análisis de Estabilidad

### Test de la Segunda Derivada
Para x* punto crítico:
- Si f''(x*) < 0  →  máximo local
- Si f''(x*) > 0  →  mínimo local
- Si f''(x*) = 0  →  punto de inflexión

### Comportamiento Near-Optimal
Cerca del máximo global x*:
```
f(x) ≈ f(x*) - (1/2)|f''(x*)|(x-x*)²
```

---

## 🎲 Análisis Estocástico

### Sensibilidad al Ruido
Si x* es el máximo teórico y x̃ = x* + ε (con ruido):
```
E[f(x̃)] ≈ f(x*) - (1/2)|f''(x*)|σ²
```
donde σ² es la varianza del ruido.

### Robustez del Método
- **Métodos globales**: Menos sensibles al ruido
- **Métodos locales**: Pueden fallar con pequeñas perturbaciones

---

## 🔬 Comparación con Funciones Clásicas

### vs. Función de Rastrigin
```
Rastrigin: f(x) = x² + 10·cos(2πx) + 10
Nuestra:   f(x) = x·sen(10πx) + 1
```

**Similitudes**:
- Múltiples máximos locales
- Componente oscilatorio

**Diferencias**:
- Amplitud variable vs constante
- Frecuencia diferente

### vs. Función de Ackley
- Ambas tienen múltiples óptimos locales
- Ambas requieren métodos de optimización global

---

## 📊 Complejidad Computacional

### Análisis de Métodos

| Método | Complejidad | Precisión | Garantía Global |
|--------|-------------|-----------|-----------------|
| Fuerza Bruta | O(n) | Alta | Sí |
| Evolución Diferencial | O(g·p·n) | Media | Probabilística |
| Sección Dorada | O(log n) | Media | No |
| Monte Carlo | O(n) | Variable | Probabilística |

Donde:
- n = número de evaluaciones
- g = generaciones
- p = tamaño población

---

## 🎯 Solución Analítica Exacta

### Problema Trascendental
La ecuación f'(x) = 0 es **trascendental**:
```
sen(10πx) + 10πx·cos(10πx) = 0
```

**No tiene solución algebraica cerrada** → Requiere métodos numéricos

### Métodos Numéricos Recomendados
1. **Newton-Raphson** para refinar candidatos
2. **Bisección** para garantizar convergencia
3. **Híbridos** para combinar velocidad y robustez

---

## 🔍 Validación Teórica

### Verificaciones Necesarias

1. **Dominio**: ¿x* ∈ [0,1]?
2. **Derivada**: ¿f'(x*) ≈ 0?
3. **Segunda derivada**: ¿f''(x*) < 0?
4. **Globalidad**: ¿Es el mayor de todos los máximos locales?

### Tolerancias Típicas
- |f'(x*)| < 1×10⁻⁶
- |x* - x_numérico| < 1×10⁻⁸

---

## 🎓 Conclusiones Teóricas

### Características del Problema
1. **Multimodal**: ~10 máximos locales
2. **No separable**: x y sen(10πx) están acoplados
3. **Mal condicionado**: Oscilaciones rápidas

### Estrategias Óptimas
1. **Métodos globales** son esenciales
2. **Alta resolución** para capturar detalles
3. **Validación múltiple** para confirmar resultados

### Aplicaciones Similares
- Ajuste de antenas (patrones de radiación)
- Procesamiento de señales (filtros oscilatorios)
- Física (interferencia de ondas)

---

**Nota Matemática**: Este problema ilustra la importancia de combinar intuición analítica con métodos numéricos robustos para funciones complejas.
