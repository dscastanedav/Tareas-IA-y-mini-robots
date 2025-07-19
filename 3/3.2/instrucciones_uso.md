# 📋 Instrucciones de Uso: Sistema de Distribución Democrática del Poder

## 🚀 Guía de Inicio Rápido

### Paso 1: Verificar Python
```bash
python --version
```
*Requiere Python 3.7 o superior*

### Paso 2: Instalar Dependencias
```bash
pip install numpy matplotlib seaborn
```

### Paso 3: Ejecutar el Sistema
```bash
python democracia_algoritmo_genetico.py
```

### Paso 4: Revisar Resultados
- Los gráficos se mostrarán automáticamente
- Se generará `resultados_democracia.png`
- Análisis detallado aparecerá en la consola

---

## 🔧 Configuración Avanzada

### Modificar Parámetros del Algoritmo Genético

Edita los valores en la clase `SistemaDemocraticoAG`:

```python
# En el método __init__
self.tamaño_poblacion = 100      # Cantidad de soluciones por generación
self.num_generaciones = 200      # Número de iteraciones evolutivas
self.tasa_mutacion = 0.1         # Probabilidad de mutación (0.0-1.0)
self.tasa_cruce = 0.8            # Probabilidad de cruzamiento (0.0-1.0)
self.elite_size = 10             # Mejores individuos conservados
```

### Cambiar Semilla de Aleatoriedad

Para resultados reproducibles:

```python
sistema = SistemaDemocraticoAG(semilla=123)  # Cambiar número
```

### Personalizar Partidos

Modifica la función `_crear_partidos()`:

```python
nombres_partidos = [
    "Tu Partido 1",
    "Tu Partido 2", 
    "Tu Partido 3",
    "Tu Partido 4",
    "Tu Partido 5"
]
```

### Personalizar Entidades

Modifica las listas en `_crear_entidades()` para agregar/quitar ministerios, agencias o institutos.

---

## 📊 Interpretación de Resultados

### Salida en Consola

#### 1. Composición del Congreso
```
🏛️ COMPOSICIÓN DEL CONGRESO
========================================
Total de curules: 50

Partido Progresista      8 curules ( 16.0%) ████
Alianza Democrática     15 curules ( 30.0%) ███████
Movimiento Nacional     18 curules ( 36.0%) █████████
Frente Popular          6 curules ( 12.0%) ███
Coalición Liberal       3 curules (  6.0%) █
```

**Interpretación**: Muestra cómo se distribuyen las 50 curules entre los 5 partidos. La representación parlamentaria determina la proporción "ideal" de poder que cada partido debería recibir.

#### 2. Entidades Estatales
```
🏢 ENTIDADES ESTATALES Y SU PESO DE PODER
================================================
Poder total a distribuir: 2513 puntos

📋 Ministerios:
   Poder de categoría: 1275 puntos
   • Ministerio de Hacienda              95 puntos
   • Ministerio de Defensa               89 puntos
   ...
```

**Interpretación**: Lista todas las entidades con sus pesos de poder. Los ministerios tienen el mayor poder (70-100 puntos), seguidos por agencias (40-80) e institutos (1-50).

#### 3. Progreso del Algoritmo Genético
```
🧬 EJECUTANDO ALGORITMO GENÉTICO
===============================================
Generación   0: Mejor fitness = 0.421573, Promedio = 0.381245
Generación  25: Mejor fitness = 0.847291, Promedio = 0.723456
Generación  50: Mejor fitness = 0.923847, Promedio = 0.856732
...
```

**Interpretación**: 
- **Mejor fitness**: La mejor solución de esa generación
- **Fitness promedio**: Calidad promedio de la población
- **Tendencia**: Debe incrementarse hacia 1.0 (distribución perfecta)

#### 4. Distribución Final
```
🏆 DISTRIBUCIÓN DEL PODER POR PARTIDO:
Partido              Curules  %Parl  Poder    %Poder  Diferencia  Entidades
-----------------------------------------------------------------------------
Partido Progresista  8        16.0   401      15.9    -0.1        10
Alianza Democrática  15       30.0   755      30.1    +0.1        15
...
```

**Interpretación**:
- **%Parl**: Porcentaje de representación parlamentaria (ideal)
- **%Poder**: Porcentaje de poder real asignado por el AG
- **Diferencia**: Desviación de la proporcionalidad (menor es mejor)
- **Entidades**: Número de instituciones asignadas

### Gráficos Generados

#### 1. Composición del Congreso (Gráfico de Torta)
- Muestra visualmente la distribución de curules
- Cada partido tiene un color distintivo
- Los porcentajes indican la representación parlamentaria

#### 2. Evolución del Algoritmo Genético (Líneas)
- **Línea azul**: Mejor fitness por generación
- **Línea roja punteada**: Fitness promedio
- **Tendencia**: Ambas deben subir hacia 1.0
- **Convergencia**: Cuando las líneas se estabilizan

#### 3. Comparación Representación vs Poder (Barras)
- **Barras azules**: Porcentaje parlamentario (ideal)
- **Barras rojas**: Porcentaje de poder asignado (real)
- **Objetivo**: Barras de igual altura por partido

#### 4. Desviación de Proporcionalidad (Barras)
- **Barras verdes**: Partido recibió más poder del ideal
- **Barras rojas**: Partido recibió menos poder del ideal
- **Línea negra**: Proporcionalidad perfecta (0%)
- **Objetivo**: Todas las barras cerca de 0%

---

## 🛠️ Solución de Problemas

### Error: Módulo no encontrado

```bash
ModuleNotFoundError: No module named 'numpy'
```

**Solución**:
```bash
pip install numpy matplotlib seaborn
```

### Error: Sin ventana gráfica

En entornos sin interfaz gráfica:

```python
# Agregar al inicio del archivo
import matplotlib
matplotlib.use('Agg')  # Usar backend sin interfaz gráfica
```

### Error: Memoria insuficiente

Reducir parámetros del AG:

```python
self.tamaño_poblacion = 50       # Reducir de 100
self.num_generaciones = 100      # Reducir de 200
```

### Resultados Poco Satisfactorios

1. **Aumentar generaciones**: Más tiempo de optimización
2. **Aumentar población**: Mayor diversidad de búsqueda
3. **Ajustar tasas**: Probar diferentes valores de mutación/cruce
4. **Verificar pesos**: Asegurar que los pesos de entidades son realistas

---

## 🎯 Casos de Uso Específicos

### Caso 1: Análisis de Escenarios Políticos

**Objetivo**: Comparar diferentes distribuciones de curules

```python
# Ejecutar múltiples veces con diferentes semillas
for semilla in range(10):
    sistema = SistemaDemocraticoAG(semilla=semilla)
    sistema.algoritmo_genetico()
    sistema.analizar_distribucion()
```

### Caso 2: Optimización de Parámetros

**Objetivo**: Encontrar los mejores parámetros del AG

```python
# Probar diferentes configuraciones
parametros = [
    {'poblacion': 50, 'generaciones': 150},
    {'poblacion': 100, 'generaciones': 200},
    {'poblacion': 150, 'generaciones': 250}
]

for config in parametros:
    # Modificar y ejecutar sistema
    pass
```

### Caso 3: Análisis de Sensibilidad

**Objetivo**: Ver cómo afectan cambios en pesos de entidades

```python
# Modificar pesos de ministerios
for entidad in sistema.entidades:
    if entidad.categoria == "Ministerio":
        entidad.peso_poder *= 1.5  # Aumentar 50%
```

---

## 📈 Métricas de Evaluación

### Fitness del Sistema
- **Rango**: 0.0 - 1.0
- **Excelente**: > 0.95
- **Bueno**: 0.85 - 0.95
- **Regular**: 0.70 - 0.85
- **Deficiente**: < 0.70

### Desviación Promedio
```
Desviación = Σ|%Poder - %Parlamentario| / num_partidos
```
- **Excelente**: < 2%
- **Bueno**: 2% - 5%
- **Regular**: 5% - 10%
- **Deficiente**: > 10%

### Índice de Justicia Democrática
```
IJD = 1 - (máx_desviación / 100)
```
- **Excelente**: > 0.95
- **Bueno**: 0.90 - 0.95
- **Aceptable**: 0.80 - 0.90
- **Deficiente**: < 0.80

---

## 🔄 Extensiones y Modificaciones

### Agregar Más Partidos

1. Modificar `_crear_partidos()` para incluir más elementos
2. Ajustar parámetros Dirichlet en `alpha`
3. Actualizar colores y nombres

### Incluir Restricciones

```python
def validar_solucion(self, individuo):
    """
    Verificar restricciones adicionales
    """
    # Ejemplo: Ningún partido puede tener > 60% del poder
    poder_por_partido = self.calcular_poder_por_partido(individuo)
    return max(poder_por_partido) <= 0.6 * sum(poder_por_partido)
```

### Múltiples Objetivos

Implementar optimización multi-objetivo:
- Proporcionalidad
- Eficiencia administrativa  
- Estabilidad política
- Representación regional

---

## 📚 Lecturas Recomendadas

### Para Profundizar en Algoritmos Genéticos
- Capítulos sobre AG en libros de optimización
- Papers sobre aplicaciones políticas de AG
- Documentación de bibliotecas como DEAP

### Para Entender el Contexto Político
- Teoría de sistemas electorales
- Proporcionalidad en democracias
- Casos de estudio de distribución de poder

---

## ⚠️ Limitaciones y Consideraciones

### Limitaciones del Modelo
1. **Simplificación**: No considera negociaciones políticas reales
2. **Pesos arbitrarios**: Los pesos de poder son simulados
3. **Estático**: No modela cambios temporales
4. **Binario**: Cada entidad va a un solo partido

### Consideraciones Éticas
- El modelo es puramente académico
- No constituye una recomendación política
- Los resultados no reflejan ideologías específicas
- Debe usarse con fines educativos únicamente

---

## 📞 Soporte y Recursos

### Documentación Adicional
- `README.md`: Visión general del proyecto
- `analisis_teorico.md`: Fundamentos matemáticos
- Comentarios en el código: Explicaciones detalladas

### Recursos Online
- Documentación de NumPy: https://numpy.org/doc/
- Tutoriales de Matplotlib: https://matplotlib.org/tutorials/
- Guías de Algoritmos Genéticos

**¡Experimenta, aprende y contribuye a entender mejor la democracia! 🗳️📊**
