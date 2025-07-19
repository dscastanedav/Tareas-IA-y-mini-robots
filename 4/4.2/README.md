# 🔢 Codificador de 7 Segmentos con Programación Genética

## 📋 Descripción del Problema

Diseñar un **circuito lógico codificador de 7 segmentos** que convierta números BCD (0-9) a patrones de display de 7 segmentos usando **Programación Genética**.

### 🎯 Objetivo
Evolucionar **7 expresiones lógicas** (una por segmento) que generen correctamente los patrones para mostrar dígitos 0-9.

---

## 🔧 Componentes de la Programación Genética

### 1. **Conjunto de Terminales**
```python
terminales = ['A', 'B', 'C', 'D', True, False]
```
- **A, B, C, D**: Entradas BCD (4 bits)
- **True, False**: Constantes booleanas

### 2. **Conjunto de Funciones**
```python
funciones = {
    'AND': 2,    # Compuerta AND (2 entradas)
    'OR': 2,     # Compuerta OR (2 entradas)
    'NOT': 1,    # Compuerta NOT (1 entrada)
    'XOR': 2     # Compuerta XOR (2 entradas)
}
```

### 3. **Función de Aptitud**
```python
fitness = (aciertos_totales / total_posible) - penalidad_tamaño
```
- **Aciertos**: Segmentos correctos para todos los dígitos (0-9)
- **Total posible**: 70 (10 dígitos × 7 segmentos)
- **Penalidad**: Reduce fitness para árboles muy grandes

---

## 📊 Tabla de Verdad del Codificador

| Dígito | A B C D | a b c d e f g | Display |
|--------|---------|---------------|---------|
|   0    | 0 0 0 0 | 1 1 1 1 1 1 0 |    ⬜   |
|   1    | 0 0 0 1 | 0 1 1 0 0 0 0 |    ⬜   |
|   2    | 0 0 1 0 | 1 1 0 1 1 0 1 |    ⬜   |
|   3    | 0 0 1 1 | 1 1 1 1 0 0 1 |    ⬜   |
|   ...  |   ...   |      ...      |   ...   |

### Segmentos del Display:
```
  a
f   b
  g
e   c
  d
```

---

## 🧬 Algoritmo de Programación Genética

### Representación
- **Individuo**: 7 árboles de expresión (uno por segmento)
- **Nodo**: Función lógica o terminal
- **Árbol**: Expresión lógica completa

### Operadores Genéticos
1. **Selección**: Torneo de 3 individuos
2. **Cruzamiento**: Intercambio de árboles entre padres
3. **Mutación**: Reemplazo de subárboles
4. **Elitismo**: Conserva 5 mejores soluciones

### Parámetros
```python
tamaño_poblacion = 50
num_generaciones = 100
tasa_mutacion = 0.15
tasa_cruce = 0.8
profundidad_maxima = 6
```

---

## 🚀 Uso del Programa

### Instalación
```bash
pip install numpy matplotlib
```

### Ejecución
```bash
python codificador_7_segmentos_pg.py
```

### Resultados
- **Consola**: Evolución y expresiones lógicas finales
- **Verificación**: Prueba completa con dígitos 0-9
- **Gráficos**: Evolución del fitness

---

## 📈 Ejemplo de Resultado

### Expresiones Evolucionadas (ejemplo):
```
Segmento a: OR(NOT(B), AND(A, C))
Segmento b: OR(NOT(A), XOR(B, D))
Segmento c: AND(OR(A, B), NOT(XOR(C, D)))
...
```

### Verificación:
```
Dígito | A B C D | a b c d e f g | Esperado  | Obtenido  | ✓
-------|---------|---------------|-----------|-----------|---
  0    | 0 0 0 0 | 1 1 1 1 1 1 0 | 1 1 1 1 1 1 0 | 1 1 1 1 1 1 0 | ✓
  1    | 0 0 0 1 | 0 1 1 0 0 0 0 | 0 1 1 0 0 0 0 | 0 1 1 0 0 0 0 | ✓
  ...
```

---

## 🎯 Ventajas de la Programación Genética

### ✅ **Automática**
- No requiere diseño manual del circuito
- Encuentra soluciones no evidentes

### ✅ **Flexible**
- Puede optimizar para diferentes criterios
- Adapta complejidad según necesidad

### ✅ **Robusta**
- Explora múltiples arquitecturas
- Evita óptimos locales

---

## 🔍 Análisis de Complejidad

### Espacio de Búsqueda
- **Árboles posibles**: Exponencial en profundidad
- **Combinaciones**: ~10^20 expresiones diferentes
- **PG explora**: ~5,000 soluciones (eficiente)

### Convergencia Típica
- **Generación 0**: ~30% precisión
- **Generación 50**: ~80% precisión  
- **Generación 100**: ~95-100% precisión

---

## 📁 Archivos del Proyecto

- `codificador_7_segmentos_pg.py` - Código principal
- `README.md` - Esta documentación
- `resultados_codificador.png` - Gráficos generados

---

## 🔧 Personalización

### Modificar Funciones Lógicas
```python
# Agregar nuevas funciones
self.funciones['NAND'] = 2
self.funciones['NOR'] = 2
```

### Cambiar Parámetros
```python
# Población más grande para mejor exploración
self.tamaño_poblacion = 100
self.num_generaciones = 200
```

### Diferentes Displays
```python
# Modificar tabla_verdad para otros patrones
# Ejemplo: display de 16 segmentos, caracteres alfanuméricos
```

---

## ⚠️ Consideraciones

- **Tiempo de ejecución**: 1-3 minutos típicamente
- **Soluciones**: Pueden variar entre ejecuciones
- **Complejidad**: Expresiones pueden ser no optimales pero funcionales
- **Extensibilidad**: Base para circuitos más complejos

---

**¡La evolución artificial diseñando circuitos digitales! 🔢⚡**
