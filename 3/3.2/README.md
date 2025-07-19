# 🗳️ Verdadera Democracia: Distribución del Poder con Algoritmos Genéticos

## 📋 Descripción del Proyecto

Este proyecto simula un sistema de **distribución democrática del poder político** usando **Algoritmos Genéticos** para optimizar la asignación de ministerios y entidades estatales entre partidos políticos, basándose en su representación parlamentaria.

### 🎯 Objetivo Principal

Crear un sistema que distribuya de manera **proporcional y justa** el poder ejecutivo (ministerios, agencias, institutos) entre los partidos políticos según su representación en el congreso, utilizando técnicas de optimización evolutiva.

---

## 🏛️ Escenario de Simulación

### Configuración Política
- **5 partidos políticos** con diferentes ideologías
- **50 curules** distribuidas aleatoriamente entre los partidos
- **50 entidades estatales** con diferentes niveles de poder e influencia

### Entidades a Distribuir
1. **15 Ministerios** (poder alto: 70-100 puntos)
   - Interior, Relaciones Exteriores, Hacienda, Defensa, Justicia, etc.

2. **10 Agencias Importantes** (poder medio: 40-80 puntos)
   - Banco Central, Contraloría, Procuraduría, Fiscalía, etc.

3. **25 Institutos y Servicios** (poder bajo: 1-50 puntos)
   - Institutos especializados, servicios públicos, agencias menores

---

## 🧬 Algoritmo Genético Implementado

### Características del AG
- **Población**: 100 individuos
- **Generaciones**: 200 iteraciones
- **Tasa de Mutación**: 10%
- **Tasa de Cruzamiento**: 80%
- **Elitismo**: Se conservan los 10 mejores individuos

### Representación del Problema
- **Individuo**: Array de 50 posiciones (una por entidad)
- **Gen**: Número del partido asignado (0-4)
- **Fitness**: Inversamente proporcional a la desviación de la proporcionalidad ideal

### Operadores Genéticos
1. **Selección**: Torneo de 3 individuos
2. **Cruzamiento**: Un punto aleatorio
3. **Mutación**: Cambio aleatorio de asignaciones
4. **Elitismo**: Conservación de mejores soluciones

---

## 📊 Función de Fitness

La función de fitness evalúa qué tan **proporcional** es la distribución del poder:

```
fitness = 1 / (1 + Σ|proporción_poder_real - proporción_parlamentaria|)
```

### Criterios de Evaluación
- **Proporcionalidad**: Poder asignado vs representación parlamentaria
- **Equidad**: Minimizar desviaciones extremas
- **Justicia**: Distribución basada en legitimidad democrática

---

## 🚀 Instalación y Uso

### Requisitos del Sistema
```bash
pip install numpy matplotlib seaborn
```

### Ejecución del Programa
```bash
python democracia_algoritmo_genetico.py
```

### Salidas Generadas
1. **Consola**: Análisis detallado de la distribución
2. **Gráficos**: Visualizaciones de resultados
3. **Archivo PNG**: Gráficos guardados automáticamente

---

## 📈 Resultados y Análisis

### Información Mostrada
1. **Composición del Congreso**: Distribución de curules por partido
2. **Entidades Estatales**: Lista completa con pesos de poder
3. **Evolución del AG**: Progreso de la optimización
4. **Distribución Final**: Asignación optimizada de entidades
5. **Análisis de Proporcionalidad**: Comparación ideal vs real

### Visualizaciones
- **Gráfico de Torta**: Composición parlamentaria
- **Línea Temporal**: Evolución del fitness durante el AG
- **Barras Comparativas**: Representación vs poder asignado
- **Desviaciones**: Análisis de proporcionalidad

---

## 🔍 Análisis Matemático

### Problema de Optimización
El sistema resuelve un **problema de asignación discreta** donde:
- Variables: Asignación de 50 entidades a 5 partidos
- Objetivo: Minimizar desviación de proporcionalidad
- Restricciones: Cada entidad se asigna a exactamente un partido

### Complejidad Computacional
- **Espacio de búsqueda**: 5^50 ≈ 7.1 × 10^34 soluciones posibles
- **Algoritmo**: Heurística evolutiva O(n × g × p)
  - n = número de entidades (50)
  - g = generaciones (200)
  - p = tamaño población (100)

---

## 🎓 Fundamentos Teóricos

### Democracia y Proporcionalidad
- **Principio democrático**: El poder debe reflejar la voluntad popular
- **Representación proporcional**: Distribución equitativa según votos
- **Legitimidad política**: Correlación entre apoyo electoral y poder ejecutivo

### Algoritmos Genéticos
- **Inspiración biológica**: Evolución y selección natural
- **Optimización global**: Exploración del espacio de soluciones
- **Robustez**: Resistencia a óptimos locales

---

## 📋 Estructura de Archivos

```
3.2/
├── democracia_algoritmo_genetico.py    # Código principal
├── README.md                           # Documentación (este archivo)
├── analisis_teorico.md                 # Análisis matemático detallado
├── resultados_democracia.png           # Gráficos de resultados
└── requirements.txt                    # Dependencias del proyecto
```

---

## 🔧 Personalización

### Parámetros Modificables
```python
# En la clase SistemaDemocraticoAG
self.tamaño_poblacion = 100      # Tamaño de la población
self.num_generaciones = 200      # Número de generaciones
self.tasa_mutacion = 0.1         # Probabilidad de mutación
self.tasa_cruce = 0.8            # Probabilidad de cruzamiento
self.elite_size = 10             # Individuos élite conservados
```

### Extensiones Posibles
- Agregar más partidos o entidades
- Implementar otros operadores genéticos
- Incluir restricciones adicionales (geografía, competencias)
- Comparar con otros algoritmos de optimización

---

## ⚠️ Consideraciones Importantes

### Limitaciones del Modelo
- Simulación académica, no implementación real
- Pesos de poder asignados aleatoriamente
- No considera factores políticos reales (coaliciones, negociaciones)

### Aspectos Éticos
- El proyecto es educativo y no promueve ninguna ideología política
- Busca ilustrar principios de optimización y democracia
- Los resultados no reflejan recomendaciones políticas reales

---

## 📚 Referencias y Lecturas

### Algoritmos Genéticos
- Holland, J. H. (1992). *Adaptation in Natural and Artificial Systems*
- Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*

### Teoría Democrática
- Dahl, R. A. (1989). *Democracy and its Critics*
- Lijphart, A. (1999). *Patterns of Democracy*

### Optimización Computacional
- Michalewicz, Z. (1996). *Genetic Algorithms + Data Structures = Evolution Programs*

---

## 👨‍💻 Información del Desarrollo

- **Autor**: Estudiante IA
- **Fecha**: Julio 2025
- **Lenguaje**: Python 3.x
- **Licencia**: Uso académico
- **Versión**: 1.0

---

## 🎯 Conclusiones del Proyecto

Este sistema demuestra cómo los **Algoritmos Genéticos** pueden aplicarse a problemas de **distribución democrática del poder**, buscando soluciones que maximicen la proporcionalidad y justicia en la asignación de cargos ejecutivos.

El proyecto ilustra la importancia de la **optimización computacional** en la resolución de problemas complejos de asignación de recursos, especialmente en contextos donde la equidad y la representatividad son fundamentales.

**¡La verdadera democracia está en los detalles de cómo distribuimos el poder! 🗳️✨**
