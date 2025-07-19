# 🧪 Guía de Experimentos y Uso

## 2.2 Instrucciones para Simulación de Enfermedad

### 🚀 Ejecución Básica

1. **Navegar a la carpeta**:
   ```bash
   cd "c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots\2\2.2"
   ```

2. **Ejecutar simulación**:
   ```bash
   python simulacion_enfermedad.py
   ```

3. **Observar resultados**:
   - Progreso en consola
   - Gráficos generados automáticamente
   - Estadísticas finales

---

## 🔬 Experimentos Sugeridos

### Experimento 1: Efecto de la Probabilidad de Infección

**Objetivo**: Observar cómo afecta la contagiosidad de la enfermedad

**Modificar en el código**:
```python
# Probar diferentes valores
infection_prob = 0.1   # Baja contagiosidad
infection_prob = 0.3   # Contagiosidad media (original)
infection_prob = 0.5   # Alta contagiosidad
infection_prob = 0.7   # Muy alta contagiosidad
```

**Preguntas**:
- ¿Qué pasa con el pico de infectados?
- ¿Cambia la duración de la epidemia?
- ¿Cuánta población total se ve afectada?

### Experimento 2: Efecto de la Probabilidad de Recuperación

**Objetivo**: Estudiar el impacto de la velocidad de recuperación

**Modificar**:
```python
recovery_prob = 0.05   # Recuperación lenta
recovery_prob = 0.1    # Recuperación media (original)
recovery_prob = 0.2    # Recuperación rápida
recovery_prob = 0.3    # Recuperación muy rápida
```

**Preguntas**:
- ¿Cómo afecta la duración de la epidemia?
- ¿Cambia el número máximo de infectados simultáneos?

### Experimento 3: Número de Infectados Iniciales

**Objetivo**: Ver el impacto del "brote inicial"

**Modificar**:
```python
initial_infected = 1    # Un solo paciente cero
initial_infected = 5    # Brote pequeño
initial_infected = 10   # Brote medio (original)
initial_infected = 25   # Brote grande
initial_infected = 50   # Brote masivo
```

### Experimento 4: Tamaño de Población

**Objetivo**: Estudiar el efecto de la densidad poblacional

**Modificar**:
```python
grid_size = 25    # Población pequeña (625 individuos)
grid_size = 50    # Población media (2,500 individuos) - original
grid_size = 75    # Población grande (5,625 individuos)
grid_size = 100   # Población muy grande (10,000 individuos)
```

**Nota**: Poblaciones más grandes tardan más en simular

---

## 📊 Cómo Interpretar los Resultados

### Indicadores Clave

1. **Tiempo al pico**: ¿Cuándo ocurre el máximo de infectados?
2. **Altura del pico**: ¿Cuántos infectados simultáneos máximo?
3. **Duración total**: ¿Cuántos pasos hasta que no hay infectados?
4. **Población afectada**: ¿Qué porcentaje total se infectó?

### Patrones Típicos

**Epidemia explosiva**:
- Pico temprano y alto
- Duración corta
- Alta proporción afectada

**Epidemia moderada**:
- Pico medio en tiempo y altura
- Duración media
- Proporción moderada afectada

**Epidemia contenida**:
- Pico tardío y bajo
- Puede auto-extinguirse
- Baja proporción afectada

---

## 🎮 Variaciones Avanzadas

### Modificación 1: Modelo SEIR

Agregar estado "Expuesto" (incubación):

```python
SUSCEPTIBLE = 0
EXPOSED = 1      # Nuevo: periodo de incubación
INFECTED = 2
RECOVERED = 3
```

### Modificación 2: Mortalidad

```python
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2
DEAD = 3         # Nuevo: individuos que mueren
```

### Modificación 3: Vacunación

```python
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2
VACCINATED = 3   # Nuevo: inmunes por vacuna
```

### Modificación 4: Heterogeneidad

```python
# Diferentes probabilidades por región
infection_prob_urban = 0.4    # Mayor en zonas urbanas
infection_prob_rural = 0.2    # Menor en zonas rurales
```

---

## 🛠️ Troubleshooting

### Problema: No aparecen gráficos
**Solución**:
```python
# Agregar al final del código
plt.show(block=True)
```

### Problema: Simulación muy lenta
**Solución**: Reducir `grid_size` o `steps`

### Problema: Resultados no realistas
**Verificar**:
- Probabilidades entre 0 y 1
- Número de infectados iniciales < población total
- Parámetros no extremos

### Problema: ImportError
**Solución**:
```bash
pip install --upgrade matplotlib numpy
```

---

## 📈 Análisis Estadístico

### Múltiples Ejecuciones

Para resultados más robustos, ejecutar varias veces:

```python
# Modificar al inicio del archivo
np.random.seed(42)  # Para resultados reproducibles
# o comentar esta línea para variabilidad
```

### Métricas a Calcular

1. **R₀ efectivo**: ¿Cuántos infecta cada persona en promedio?
2. **Tiempo de duplicación**: ¿Qué tan rápido crece la epidemia?
3. **Punto de inflexión**: ¿Cuándo empieza a decrecer?

---

## 🎯 Objetivos de Aprendizaje

Después de estos experimentos deberías entender:

1. **Autómatas celulares**: Cómo funcionan y sus aplicaciones
2. **Modelos epidemiológicos**: Conceptos básicos del modelo SIR
3. **Simulación estocástica**: Papel de la aleatoriedad
4. **Análisis de sensibilidad**: Cómo los parámetros afectan resultados
5. **Visualización de datos**: Interpretación de gráficos temporales

---

**¡Diviértete experimentando con diferentes configuraciones!** 🎉
