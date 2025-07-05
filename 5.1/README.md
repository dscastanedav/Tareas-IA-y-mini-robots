# Comparación MEPX vs Redes Neuronales Artificiales

Este proyecto compara los resultados de Multi Expression Programming (MEPX) con Redes Neuronales Artificiales (RNA) usando conjuntos de datos de ejemplo.

## Descripción

MEPX es una técnica de programación genética que encuentra expresiones matemáticas interpretables para problemas de regresión simbólica y clasificación. Este proyecto toma datos de ejemplo típicos de MEPX y los compara con soluciones usando Redes Neuronales Artificiales.

## Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

1. **Opción 1: Instalar desde requirements.txt**
```bash
pip install -r requirements.txt
```

2. **Opción 2: Instalar manualmente**
```bash
pip install numpy pandas matplotlib scikit-learn seaborn
```

## Archivos del Proyecto

- `mepx_vs_rna_comparison.py` - Comparación completa con múltiples modelos
- `simple_mepx_rna_comparison.py` - Ejemplo simple y directo
- `requirements.txt` - Lista de dependencias
- `README.md` - Este archivo

## Uso

### Ejemplo Simple
```bash
python simple_mepx_rna_comparison.py
```

### Comparación Completa
```bash
python mepx_vs_rna_comparison.py
```

## Características

### Datos de Ejemplo
- **Eficiencia Energética**: Basado en características de edificios (similar al ejemplo "building1-energy" de MEPX)
- **Regresión Simbólica**: Funciones matemáticas conocidas con ruido
- **Formato PROBEN1**: Datos estructurados como los archivos de MEPX

### Modelos Comparados

#### MEPX (Simulado)
- Expresiones simbólicas interpretables
- Optimización evolutiva
- Resultados típicos de MEP

#### Redes Neuronales Artificiales
- **RNA Simple**: 1 capa oculta (50 neuronas)
- **RNA Media**: 2 capas ocultas (100, 50 neuronas)
- **RNA Profunda**: 3 capas ocultas (200, 100, 50 neuronas)
- **RNA Tanh**: 2 capas con activación tanh

### Métricas de Evaluación
- **MSE** (Error Cuadrático Medio)
- **R²** (Coeficiente de Determinación)
- **MAE** (Error Absoluto Medio)
- División: 60% entrenamiento, 20% validación, 20% prueba

## Resultados

### Archivos Generados
- `mepx_vs_rna_comparison.png` - Gráficos comparativos
- `mepx_vs_rna_results.csv` - Tabla de resultados
- `best_model_predictions.csv` - Predicciones del mejor modelo
- `rna_vs_mepx_simple.png` - Gráficos del ejemplo simple

### Interpretación
- **MEPX**: Produce expresiones matemáticas interpretables
- **RNA**: Puede modelar relaciones más complejas pero menos interpretables

## Ventajas de Cada Enfoque

### MEPX
✅ **Interpretabilidad**: Expresiones matemáticas claras
✅ **Velocidad**: Entrenamiento rápido
✅ **Robustez**: No requiere escalado de datos
✅ **Automatización**: Encuentra relaciones no lineales automáticamente

### Redes Neuronales
✅ **Flexibilidad**: Múltiples arquitecturas disponibles
✅ **Capacidad**: Puede modelar relaciones muy complejas
✅ **Generalización**: Buena con suficientes datos
✅ **Ecosistema**: Amplio soporte en la comunidad

## Casos de Uso Recomendados

### Usar MEPX cuando:
- Necesitas interpretabilidad del modelo
- Tienes datos limitados
- Quieres descubrir relaciones matemáticas
- La velocidad de entrenamiento es importante

### Usar RNA cuando:
- Tienes grandes volúmenes de datos
- La precisión es más importante que la interpretabilidad
- Las relaciones son muy complejas
- Tienes recursos computacionales suficientes

## Datos de Ejemplo Típicos de MEPX

### Conjuntos de Datos Incluidos en MEPX:
1. **Building Energy**: Eficiencia energética de edificios
2. **Concrete Strength**: Resistencia del concreto
3. **Wine Quality**: Calidad del vino
4. **Airfoil**: Características aerodinámicas
5. **Boston Housing**: Precios de viviendas

### Formato de Datos
```
# Archivo típico de MEPX (.txt)
# Comentario: Descripción del problema
# Variables: x1, x2, x3, ..., target
1.2 3.4 5.6 ... 12.3
2.1 4.5 6.7 ... 15.8
...
```

## Extensiones Posibles

### Para Mejorar la Comparación:
1. **Datos Reales**: Usar archivos reales de MEPX
2. **Más Algoritmos**: Comparar con SVM, Random Forest, etc.
3. **Optimización**: Tunear hiperparámetros de RNA
4. **Validación Cruzada**: Usar k-fold cross-validation
5. **Métricas Adicionales**: RMSE, MAPE, etc.

### Para Emular Mejor MEPX:
1. **Programación Genética**: Usar `gplearn` o `deap`
2. **Búsqueda Simbólica**: Implementar algoritmos evolutivos
3. **Expresiones Complejas**: Generar funciones más elaboradas

## Solución de Problemas

### Error de Importación
```bash
ImportError: No module named 'pandas'
```
**Solución**: Instalar dependencias
```bash
pip install pandas
```

### Error de Matplotlib
```bash
ImportError: No module named 'matplotlib'
```
**Solución**: Instalar matplotlib
```bash
pip install matplotlib
```

### Error de Scikit-learn
```bash
ImportError: No module named 'sklearn'
```
**Solución**: Instalar scikit-learn
```bash
pip install scikit-learn
```

## Contacto y Recursos

### Recursos sobre MEPX:
- [Sitio oficial](https://mepx.org)
- [Documentación](https://mepx.github.io/)
- [GitHub](https://github.com/mepx/mepx)
- [Grupo de discusión](https://groups.google.com/d/forum/mepx)

### Recursos sobre RNA:
- [Scikit-learn MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)

## Licencia

Este proyecto está bajo la licencia MIT, similar a MEPX.

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Changelog

### v1.0.0
- Implementación inicial
- Comparación básica MEPX vs RNA
- Generación de datos de ejemplo
- Visualizaciones comparativas
- Exportación de resultados
