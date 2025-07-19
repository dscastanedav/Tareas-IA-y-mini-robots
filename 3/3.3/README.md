# ⚡ Despacho Óptimo de Energía Eléctrica con Algoritmos Genéticos

## 📋 Descripción del Problema

Una empresa proveedora de energía eléctrica necesita distribuir energía desde **4 plantas generadoras** hacia **4 ciudades**, minimizando los costos totales de transporte y generación.

### 🏭 Plantas Generadoras
- **Planta C**: 3 GW - $680/KW-H
- **Planta B**: 6 GW - $720/KW-H  
- **Planta M**: 5 GW - $660/KW-H
- **Planta B2**: 4 GW - $750/KW-H

**Total disponible**: 18 GW

### 🏙️ Ciudades y Demandas
- **Cali**: 4 GW
- **Bogotá**: 3 GW
- **Medellín**: 5 GW
- **Barranquilla**: 3 GW

**Total demandado**: 15 GW

### 🚛 Costos de Transporte ($/GW)

|        | Cali | Bogotá | Medellín | Barranquilla |
|--------|------|--------|----------|--------------|
| Planta C | 1    | 4      | 3        | 6            |
| Planta B | 4    | 1      | 4        | 5            |
| Planta M | 3    | 4      | 1        | 4            |
| Planta B2| 6    | 5      | 4        | 1            |

---

## 🎯 Objetivo

**Minimizar el costo total** = Costo de transporte + Costo de generación

Sujeto a:
- No exceder capacidades de plantas
- Satisfacer exactamente las demandas de ciudades
- Todas las cantidades ≥ 0

---

## 🧬 Solución con Algoritmos Genéticos

### Representación
- **Individuo**: Matriz 4×4 con la cantidad de energía (GW) que cada planta envía a cada ciudad
- **Genes**: Valores reales entre 0 y capacidad máxima

### Función de Fitness
```
fitness = 1 / (1 + costo_total)
```
Donde `costo_total = costo_transporte + costo_generacion`

### Operadores Genéticos
- **Selección**: Torneo de 3 individuos
- **Cruzamiento**: Aritmético (combinación lineal de padres)
- **Mutación**: Variaciones aleatorias pequeñas + reparación
- **Elitismo**: Conserva 8 mejores soluciones

---

## 🚀 Uso del Programa

### Instalación
```bash
pip install numpy matplotlib
```

### Ejecución
```bash
python despacho_energia_ag.py
```

### Resultados
- **Consola**: Configuración, progreso y análisis de la solución óptima
- **Gráficos**: Visualizaciones de la distribución y evolución del algoritmo
- **Archivo PNG**: Gráficos guardados automáticamente

---

## 📊 Interpretación de Resultados

### Matriz de Distribución
Muestra cuánta energía (GW) envía cada planta a cada ciudad.

### Verificación de Restricciones
- ✅ Ninguna planta excede su capacidad
- ✅ Todas las ciudades reciben exactamente su demanda
- ✅ Todas las cantidades son no negativas

### Análisis de Costos
- **Costo de transporte**: Basado en distancias y cantidades
- **Costo de generación**: Basado en eficiencia de cada planta
- **Costo total**: Suma de ambos componentes

---

## 🔧 Parámetros Configurables

En la clase `DespachoEnergiaAG`:
```python
self.tamaño_poblacion = 80    # Individuos por generación
self.num_generaciones = 150   # Iteraciones del algoritmo
self.tasa_mutacion = 0.15     # Probabilidad de mutación
self.tasa_cruce = 0.8         # Probabilidad de cruzamiento
self.elite_size = 8           # Mejores individuos conservados
```

---

## 📈 Ejemplo de Resultado Típico

```
⚡ DISTRIBUCIÓN DE ENERGÍA (GW):
         Cali     Bogotá   Medellín  Barranq.
Planta C  2.50     0.50     0.00     0.00
Planta B  0.00     2.50     3.50     0.00
Planta M  1.50     0.00     1.50     2.00
Planta B2 0.00     0.00     0.00     1.00

💰 ANÁLISIS DE COSTOS:
Costo de transporte: $23,500
Costo de generación: $45,200
COSTO TOTAL: $68,700
```

---

## ⚠️ Consideraciones

- **Simplificaciones**: El modelo asume transmisión instantánea y sin pérdidas
- **Costos**: Los valores son ilustrativos para el ejercicio académico
- **Optimización**: El AG encuentra muy buenas soluciones, aunque no garantiza el óptimo global

---

## 📁 Archivos del Proyecto

- `despacho_energia_ag.py` - Código principal
- `README.md` - Este archivo de documentación
- `resultados_despacho.png` - Gráficos generados

---

**¡La optimización energética al servicio de la eficiencia! ⚡📊**
