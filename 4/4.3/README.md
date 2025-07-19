# 🤖 Robot Entregador de Galletas con Programación Genética

## 📋 Descripción del Problema

Un robot debe entregar galletas a un grupo de ingenieros distribuidos en una sala cuadrada. Usando **Programación Genética**, evolucionamos el comportamiento del robot para maximizar las entregas exitosas y los puntos obtenidos.

### 🎯 Objetivo
Evolucionar un **árbol de comportamiento** que permita al robot navegar eficientemente, encontrar ingenieros y entregar galletas, maximizando la puntuación total.

---

## 🔧 Componentes de la Programación Genética

### 1. **Conjunto de Terminales**

#### Acciones Primitivas:
```python
acciones = [
    'MOVER_NORTE', 'MOVER_SUR', 'MOVER_ESTE', 'MOVER_OESTE',
    'ENTREGAR_GALLETA', 'BUSCAR_INGENIERO', 'PARAR'
]
```

#### Sensores:
```python
sensores = [
    'HAY_INGENIERO_CERCA',    # Detecta ingeniero en casilla adyacente
    'HAY_PARED_NORTE',        # Detecta pared al norte
    'HAY_PARED_SUR',          # Detecta pared al sur
    'HAY_PARED_ESTE',         # Detecta pared al este
    'HAY_PARED_OESTE',        # Detecta pared al oeste
    'TENGO_GALLETAS'          # Verifica si quedan galletas
]
```

### 2. **Conjunto de Funciones**
```python
funciones = {
    'SI': 3,        # Condicional: SI(condición, then, else)
    'SECUENCIA': 2, # Ejecutar acciones en secuencia
    'REPETIR': 2    # Repetir acción N veces
}
```

### 3. **Función de Aptitud**
```python
fitness = puntos_promedio - penalidad_tamaño

donde:
puntos = (entregas_exitosas × 10) + bonus_eficiencia
bonus_eficiencia = (entregas / pasos_usados) × 5
penalidad_tamaño = min(5, tamaño_árbol / 20)
```

---

## 🏗️ Escenario de Simulación

### Configuración del Entorno
- **Sala**: Cuadrada 10×10 casillas
- **Robot**: Inicia en posición (0,0)
- **Ingenieros**: 8 distribuidos aleatoriamente
- **Galletas**: 10 galletas iniciales
- **Tiempo límite**: 50 pasos máximos

### Sistema de Puntuación
- **+10 puntos** por cada galleta entregada exitosamente
- **+bonus** por eficiencia (entregas/pasos)
- **-penalty** por árboles de comportamiento muy complejos

---

## 🧬 Algoritmo de Programación Genética

### Representación
- **Individuo**: Árbol de comportamiento del robot
- **Nodos internos**: Funciones de control (SI, SECUENCIA, REPETIR)
- **Hojas**: Acciones primitivas y sensores

### Ejemplo de Comportamiento Evolucionado:
```
SI(HAY_INGENIERO_CERCA,
   ENTREGAR_GALLETA,
   SECUENCIA(
     SI(TENGO_GALLETAS, BUSCAR_INGENIERO, PARAR),
     MOVER_NORTE
   )
)
```

### Operadores Genéticos
1. **Selección**: Torneo de 3 individuos
2. **Cruzamiento**: Intercambio de subárboles (70%)
3. **Mutación**: Reemplazo de subárboles (20%)
4. **Elitismo**: Conserva 5 mejores soluciones

### Parámetros
```python
tamaño_poblacion = 40
num_generaciones = 80
tasa_mutacion = 0.2
tasa_cruce = 0.7
profundidad_maxima = 5
```

---

## 🚀 Uso del Programa

### Instalación
```bash
pip install numpy matplotlib
```

### Ejecución
```bash
python robot_galletas_pg.py
```

### Resultados
- **Consola**: Evolución del comportamiento y análisis final
- **Gráfico 1**: Evolución del fitness durante la PG
- **Gráfico 2**: Visualización del recorrido del robot en la sala
- **Métricas**: Puntos, entregas, eficiencia

---

## 📊 Ejemplo de Resultado

### Comportamiento Evolucionado:
```
🎯 Escenario de prueba:
Ingenieros en: [(3,2), (7,4), (5,8), (1,6), (9,3), (4,9), (8,1), (2,7)]

📈 RESULTADOS:
• Puntos obtenidos: 85
• Entregas realizadas: 7/8
• Pasos utilizados: 32/50
• Eficiencia: 21.9% (entregas/paso)
• Entregas en: [(3,2), (7,4), (5,8), (1,6), (9,3), (4,9), (8,1)]
```

### Visualización:
- **Línea azul**: Trayectoria del robot
- **Punto verde**: Posición inicial
- **Punto rojo**: Posición final
- **Estrellas doradas**: Entregas exitosas
- **Colores de fondo**: 
  - Rojo: Ingeniero sin atender
  - Verde: Ingeniero atendido

---

## 🔍 Análisis del Comportamiento

### Estrategias Emergentes Típicas:

1. **Exploración Sistemática**
   ```
   SECUENCIA(BUSCAR_INGENIERO, 
             SI(HAY_INGENIERO_CERCA, ENTREGAR_GALLETA, MOVER_NORTE))
   ```

2. **Navegación Inteligente**
   ```
   SI(HAY_PARED_NORTE, MOVER_SUR, 
      SI(TENGO_GALLETAS, BUSCAR_INGENIERO, PARAR))
   ```

3. **Optimización de Recursos**
   ```
   SI(TENGO_GALLETAS,
      SECUENCIA(BUSCAR_INGENIERO, ENTREGAR_GALLETA),
      PARAR)
   ```

---

## 📈 Métricas de Evaluación

### Fitness Típico por Generación:
- **Gen 0**: ~15-25 puntos (comportamiento aleatorio)
- **Gen 20**: ~40-50 puntos (estrategias básicas)
- **Gen 40**: ~60-75 puntos (comportamiento especializado)
- **Gen 80**: ~75-90 puntos (estrategias optimizadas)

### Factores de Éxito:
- **Entregas**: Prioridad máxima (10 puntos c/u)
- **Eficiencia**: Minimizar pasos innecesarios
- **Cobertura**: Visitar áreas con ingenieros
- **Gestión de recursos**: Usar galletas sabiamente

---

## 🔧 Personalización

### Modificar Entorno:
```python
# Sala más grande
self.tamaño_sala = 15

# Más ingenieros
self.num_ingenieros = 12

# Más tiempo
self.pasos_maximos = 100
```

### Nuevas Acciones:
```python
# Agregar a terminales
'RECARGAR_GALLETAS',    # Acción especial
'COMUNICAR_INGENIERO',  # Interacción social
'OPTIMIZAR_RUTA'        # Planificación avanzada
```

### Sensores Adicionales:
```python
'DISTANCIA_A_INGENIERO',  # Sensor de distancia
'ENERGIA_RESTANTE',       # Estado del robot
'TIEMPO_TRANSCURRIDO'     # Gestión temporal
```

---

## 📁 Archivos del Proyecto

- `robot_galletas_pg.py` - Código principal
- `README.md` - Esta documentación
- `resultados_robot_galletas.png` - Visualizaciones generadas

---

## 🎯 Ventajas de la Programación Genética

### ✅ **Comportamiento Emergente**
- Estrategias no programadas explícitamente
- Adaptación automática al entorno
- Soluciones creativas e inesperadas

### ✅ **Robustez**
- Funciona con diferentes distribuciones de ingenieros
- Resistente a cambios en el entorno
- No requiere programación manual de estrategias

### ✅ **Escalabilidad**
- Fácil agregar nuevas acciones/sensores
- Adapta complejidad según el problema
- Reutilizable para otros robots/tareas

---

## ⚠️ Consideraciones

- **Tiempo de ejecución**: 2-4 minutos típicamente
- **Variabilidad**: Resultados pueden diferir entre ejecuciones
- **Complejidad**: Comportamientos pueden ser difíciles de interpretar
- **Evaluación**: Se prueba en múltiples escenarios para robustez

---

**¡La evolución artificial enseñando robots a ser amables y eficientes! 🤖🍪**
