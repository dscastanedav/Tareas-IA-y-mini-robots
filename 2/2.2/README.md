# 🦠 Simulación de Propagación de Enfermedad

## 2.2 Autómatas Celulares Probabilísticos

### 📋 Descripción del Proyecto

Este proyecto implementa una **simulación de propagación de enfermedad** usando autómatas celulares probabilísticos. Es una representación simplificada de cómo se puede extender una epidemia en una población.

### 🎯 Objetivo

Desarrollar un modelo de difusión usando autómatas celulares probabilísticos para simular la propagación de una enfermedad en una población.

---

## 🧮 Modelo Matemático

### Estados de los Individuos

- 🟦 **SUSCEPTIBLE (0)**: Personas sanas que pueden infectarse
- 🟥 **INFECTED (1)**: Personas infectadas que pueden contagiar a sus vecinos
- 🟩 **RECOVERED (2)**: Personas recuperadas (inmunes, ya no contagian ni se infectan)

### Reglas del Autómata

1. **Infección**: Un individuo susceptible se infecta si:
   - Al menos un vecino está infectado
   - Con probabilidad `infection_prob = 0.3`

2. **Recuperación**: Un individuo infectado se recupera con:
   - Probabilidad `recovery_prob = 0.1`

3. **Inmunidad**: Los individuos recuperados no pueden volver a infectarse

### Topología

- **Grilla**: 50 x 50 = 2,500 individuos
- **Vecindario**: 4-conectividad (arriba, abajo, izquierda, derecha)
- **Bordes**: Periódicos (la grilla se "envuelve")

---

## ⚙️ Parámetros de Simulación

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `grid_size` | 50 | Tamaño de la cuadrícula (50x50) |
| `infection_prob` | 0.3 | Probabilidad de infección (30%) |
| `recovery_prob` | 0.1 | Probabilidad de recuperación (10%) |
| `initial_infected` | 10 | Número de infectados al inicio |
| `steps` | 100 | Número máximo de pasos de simulación |

---

## 🚀 Cómo Ejecutar

### Requisitos

```bash
pip install matplotlib numpy
```

### Ejecución

```bash
cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\2\2.2"
python simulacion_enfermedad.py
```

### Salida Esperada

1. **Información en consola**: Progreso de la simulación paso a paso
2. **Gráficos**: 
   - Número absoluto de individuos por estado vs. tiempo
   - Porcentaje de población por estado vs. tiempo
3. **Estadísticas finales**: Resumen del resultado de la simulación

---

## 📊 Interpretación de Resultados

### Curvas Típicas

![Diagrama de curvas SIR](diagrama.png)

- **Susceptibles (azul)**: Decrece monotónicamente
- **Infectados (rojo)**: Aumenta rápidamente, luego decrece
- **Recuperados (verde)**: Aumenta monotónicamente

### Fases de la Epidemia

1. **Fase inicial**: Pocos infectados, muchos susceptibles
2. **Fase de crecimiento**: Aumento exponencial de infectados
3. **Pico epidémico**: Máximo número de infectados simultáneos
4. **Fase de declive**: Disminución de infectados, aumento de recuperados
5. **Fase final**: Pocos o ningún infectado, población mayormente recuperada

---

## 🔬 Fundamentos Teóricos

### Autómatas Celulares

Los **autómatas celulares** son modelos matemáticos discretos que consisten en:

- **Células**: Dispuestas en una grilla regular
- **Estados**: Cada célula tiene un estado finito
- **Reglas**: Determinan cómo evoluciona cada célula
- **Tiempo discreto**: La evolución ocurre en pasos

### Modelo SIR

Este modelo implementa una variante del clásico **modelo SIR epidemiológico**:

- **S**: Susceptible
- **I**: Infected (Infectado)
- **R**: Recovered (Recuperado)

### Probabilidades

El uso de **probabilidades** introduce:
- **Estocasticidad**: Variabilidad en los resultados
- **Realismo**: Las infecciones no son determinísticas
- **Flexibilidad**: Permite ajustar la "fuerza" de la epidemia

---

## 🎛️ Variaciones Posibles

### Modificar Parámetros

```python
# Epidemia más contagiosa
infection_prob = 0.5

# Recuperación más lenta
recovery_prob = 0.05

# Población más densa
grid_size = 100
```

### Extensiones

1. **Estados adicionales**:
   - Período de incubación
   - Mortalidad
   - Vacunación

2. **Topologías diferentes**:
   - Vecindario de Moore (8 vecinos)
   - Redes complejas
   - Grafos aleatorios

3. **Parámetros variables**:
   - Probabilidades que cambian con el tiempo
   - Heterogeneidad espacial

---

## 📈 Análisis de Sensibilidad

### Efecto de `infection_prob`

- **Baja (< 0.2)**: Epidemias localizadas, pocos afectados
- **Media (0.2-0.4)**: Propagación moderada
- **Alta (> 0.4)**: Epidemias masivas, mayoría afectada

### Efecto de `recovery_prob`

- **Baja (< 0.05)**: Epidemias prolongadas
- **Media (0.05-0.15)**: Duración moderada
- **Alta (> 0.15)**: Epidemias cortas

---

## 🔍 Validación del Modelo

### Verificaciones

1. **Conservación**: El número total de individuos se mantiene constante
2. **Transiciones válidas**: Solo ocurren transiciones S→I→R
3. **Convergencia**: La simulación eventualmente estabiliza

### Limitaciones

- **Simplicidad**: No considera factores demográficos reales
- **Homogeneidad**: Todos los individuos son idénticos
- **Espacialidad**: No hay movimiento de individuos

---

## 📚 Referencias

- Wolfram, S. (2002). *A New Kind of Science*
- Kermack, W. O., & McKendrick, A. G. (1927). *A contribution to the mathematical theory of epidemics*
- White, S. H., et al. (2007). *Modeling epidemics using cellular automata*

---

**Nota**: Este es un modelo educativo simplificado. Los modelos epidemiológicos reales son mucho más complejos y consideran múltiples factores adicionales.
