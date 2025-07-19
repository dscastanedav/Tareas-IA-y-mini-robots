# Aproximación de Función Raíz Cuadrada con Machine Learning

Este proyecto demuestra cómo usar Machine Learning para aproximar la función matemática raíz cuadrada.

## Descripción

El programa:
1. **Genera un dataset** con valores aleatorios y sus raíces cuadradas reales
2. **Entrena dos modelos**:
   - Regresión Lineal
   - Red Neuronal (MLP)
3. **Compara los resultados** de ambos modelos con la función real en 10 ejemplos
4. **Genera gráficos** comparativos para visualizar el rendimiento

## Archivos

- `sqrt_approximation.py`: Script principal con todo el código
- `requirements.txt`: Dependencias necesarias
- `comparacion_modelos.png`: Gráficos generados (se crea al ejecutar)

## Instalación

1. Asegúrate de tener Python 3.7+ instalado
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

```bash
python sqrt_approximation.py
```

## Resultados Esperados

El programa mostrará:
- Información sobre el dataset generado
- Métricas de rendimiento (MSE y R²) para ambos modelos
- Tabla comparativa con 10 ejemplos específicos
- Gráficos comparativos guardados como imagen

## Notas Técnicas

- **Dataset**: 2000 muestras con valores entre 0 y 100
- **División**: 80% entrenamiento, 20% prueba
- **Regresión Lineal**: Modelo simple pero rápido
- **Red Neuronal**: 2 capas ocultas (50 y 30 neuronas) para mejor aproximación no lineal

## Interpretación

La función raíz cuadrada es no lineal, por lo que esperamos que la red neuronal tenga mejor rendimiento que la regresión lineal, especialmente en valores más altos donde la curvatura es más pronunciada.
