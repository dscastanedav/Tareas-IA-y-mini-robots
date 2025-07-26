# -*- coding: utf-8 -*-
"""
Maximización de la función f(x) = x * sin(10πx) + 1
==================================================

Este script implementa diferentes métodos para encontrar el máximo global
de la función f(x) = x * sin(10πx) + 1 en el intervalo [0,1].

La función tiene múltiples máximos locales debido al término sinusoidal,
lo que la convierte en un problema interesante de optimización global.

Autor: Estudiante IA
Fecha: Julio 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, differential_evolution, brute
import warnings
warnings.filterwarnings('ignore')

def funcion_objetivo(x):
    """
    Función a maximizar: f(x) = x * sin(10πx) + 1
    
    Args:
        x: Valor de entrada en el intervalo [0,1]
    
    Returns:
        Valor de la función f(x)
    """
    return x * np.sin(10 * np.pi * x) + 1

def funcion_negativa(x):
    """
    Función negativa para usar con minimizadores
    Maximizar f(x) = Minimizar -f(x)
    
    Args:
        x: Valor de entrada
    
    Returns:
        -f(x)
    """
    return -funcion_objetivo(x)

def derivada_funcion(x):
    """
    Derivada analítica de f(x) = x * sin(10πx) + 1
    f'(x) = sin(10πx) + 10πx * cos(10πx)
    
    Args:
        x: Valor de entrada
    
    Returns:
        Valor de la derivada f'(x)
    """
    return np.sin(10 * np.pi * x) + 10 * np.pi * x * np.cos(10 * np.pi * x)

def analizar_funcion():
    """
    Analiza las características de la función y genera gráfico
    """
    print("🔍 ANÁLISIS DE LA FUNCIÓN f(x) = x·sin(10πx) + 1")
    print("=" * 60)
    
    # Generar puntos para el gráfico
    x = np.linspace(0, 1, 1000)
    y = funcion_objetivo(x)
    dy = derivada_funcion(x)
    
    # Crear gráfico
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Gráfico de la función
    ax1.plot(x, y, 'b-', linewidth=2, label='f(x) = x·sin(10πx) + 1')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('Función Objetivo a Maximizar')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Encontrar aproximadamente los máximos locales
    maximos_locales = []
    for i in range(1, len(y)-1):
        if y[i] > y[i-1] and y[i] > y[i+1]:
            maximos_locales.append((x[i], y[i]))
    
    # Marcar máximos locales
    if maximos_locales:
        max_x, max_y = zip(*maximos_locales)
        ax1.plot(max_x, max_y, 'ro', markersize=6, label=f'Máximos locales ({len(maximos_locales)})')
        ax1.legend()
    
    # Gráfico de la derivada
    ax2.plot(x, dy, 'r-', linewidth=2, label="f'(x)")
    ax2.axhline(y=0, color='k', linestyle='--', alpha=0.5, label='f\'(x) = 0')
    ax2.set_xlabel('x')
    ax2.set_ylabel("f'(x)")
    ax2.set_title('Derivada de la Función')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('c:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/3/3.1/analisis_funcion.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    # Estadísticas básicas
    print(f"📊 Estadísticas de la función en [0,1]:")
    print(f"   • Valor mínimo: {np.min(y):.6f}")
    print(f"   • Valor máximo: {np.max(y):.6f}")
    print(f"   • Número de máximos locales aproximados: {len(maximos_locales)}")
    print(f"   • Rango de valores: [{np.min(y):.6f}, {np.max(y):.6f}]")
    
    return maximos_locales

def metodo_fuerza_bruta():
    """
    Método de fuerza bruta: evaluar en una grilla fina
    """
    print("\n🔨 MÉTODO 1: FUERZA BRUTA")
    print("-" * 40)
    
    # Crear grilla muy fina
    x_grid = np.linspace(0, 1, 10000)
    y_grid = funcion_objetivo(x_grid)
    
    # Encontrar máximo
    idx_max = np.argmax(y_grid)
    x_max = x_grid[idx_max]
    f_max = y_grid[idx_max]
    
    print(f"   🎯 Resultado:")
    print(f"      x* = {x_max:.8f}")
    print(f"      f(x*) = {f_max:.8f}")
    print(f"      Evaluaciones: {len(x_grid)}")
    
    return x_max, f_max

def metodo_scipy_brute():
    """
    Método scipy.optimize.brute (búsqueda en grilla)
    """
    print("\n🔬 MÉTODO 2: SCIPY BRUTE FORCE")
    print("-" * 40)
    
    # Usar scipy brute force
    resultado = brute(funcion_negativa, ranges=[(0, 1)], Ns=1000, full_output=True)
    
    x_max = resultado[0][0]
    f_max = -resultado[1]  # Negativo porque minimizamos -f(x)
    
    print(f"   🎯 Resultado:")
    print(f"      x* = {x_max:.8f}")
    print(f"      f(x*) = {f_max:.8f}")
    print(f"      Evaluaciones: ~1000")
    
    return x_max, f_max

def metodo_golden_section():
    """
    Método de sección dorada (para funciones unimodales)
    Nota: No funcionará bien aquí porque la función es multimodal
    """
    print("\n🥇 MÉTODO 3: SECCIÓN DORADA")
    print("-" * 40)
    
    try:
        resultado = minimize_scalar(funcion_negativa, bounds=(0, 1), method='golden')
        
        x_max = resultado.x
        f_max = -resultado.fun
        
        print(f"   🎯 Resultado (máximo local):")
        print(f"      x* = {x_max:.8f}")
        print(f"      f(x*) = {f_max:.8f}")
        print(f"      Evaluaciones: {resultado.nfev}")
        print(f"   ⚠️  Nota: Encuentra un máximo local, no necesariamente global")
        
        return x_max, f_max
    
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None, None

def metodo_diferencial_evolution():
    """
    Algoritmo evolutivo diferencial (bueno para optimización global)
    """
    print("\n🧬 MÉTODO 4: EVOLUCIÓN DIFERENCIAL")
    print("-" * 40)
    
    # Configurar evolución diferencial
    bounds = [(0, 1)]
    resultado = differential_evolution(funcion_negativa, bounds, 
                                     seed=42, maxiter=100, popsize=15)
    
    x_max = resultado.x[0]
    f_max = -resultado.fun
    
    print(f"   🎯 Resultado:")
    print(f"      x* = {x_max:.8f}")
    print(f"      f(x*) = {f_max:.8f}")
    print(f"      Evaluaciones: {resultado.nfev}")
    print(f"      Éxito: {'✅' if resultado.success else '❌'}")
    
    return x_max, f_max

def metodo_busqueda_aleatoria():
    """
    Búsqueda aleatoria Monte Carlo
    """
    print("\n🎲 MÉTODO 5: BÚSQUEDA ALEATORIA (MONTE CARLO)")
    print("-" * 40)
    
    # Generar puntos aleatorios
    np.random.seed(42)
    n_puntos = 50000
    x_random = np.random.uniform(0, 1, n_puntos)
    y_random = funcion_objetivo(x_random)
    
    # Encontrar el mejor
    idx_max = np.argmax(y_random)
    x_max = x_random[idx_max]
    f_max = y_random[idx_max]
    
    print(f"   🎯 Resultado:")
    print(f"      x* = {x_max:.8f}")
    print(f"      f(x*) = {f_max:.8f}")
    print(f"      Evaluaciones: {n_puntos}")
    
    return x_max, f_max

def metodo_analisis_derivada():
    """
    Método basado en análisis de la derivada
    """
    print("\n📐 MÉTODO 6: ANÁLISIS DE DERIVADA")
    print("-" * 40)
    
    # Encontrar raíces de la derivada (puntos críticos)
    x_test = np.linspace(0, 1, 10000)
    dy_test = derivada_funcion(x_test)
    
    # Encontrar cambios de signo (aproximación de raíces)
    puntos_criticos = []
    for i in range(1, len(dy_test)):
        if dy_test[i-1] * dy_test[i] < 0:  # Cambio de signo
            x_critico = x_test[i]
            puntos_criticos.append(x_critico)
    
    # Incluir extremos del intervalo
    puntos_criticos.extend([0, 1])
    
    # Evaluar función en todos los puntos críticos
    valores = [(x, funcion_objetivo(x)) for x in puntos_criticos]
    
    # Encontrar el máximo
    x_max, f_max = max(valores, key=lambda item: item[1])
    
    print(f"   🎯 Resultado:")
    print(f"      x* = {x_max:.8f}")
    print(f"      f(x*) = {f_max:.8f}")
    print(f"      Puntos críticos encontrados: {len(puntos_criticos)}")
    
    return x_max, f_max

def comparar_metodos():
    """
    Compara todos los métodos y encuentra el mejor resultado
    """
    print("\n📊 COMPARACIÓN DE MÉTODOS")
    print("=" * 60)
    
    metodos = [
        ("Fuerza Bruta", metodo_fuerza_bruta),
        ("SciPy Brute", metodo_scipy_brute),
        ("Sección Dorada", metodo_golden_section),
        ("Evolución Diferencial", metodo_diferencial_evolution),
        ("Búsqueda Aleatoria", metodo_busqueda_aleatoria),
        ("Análisis Derivada", metodo_analisis_derivada)
    ]
    
    resultados = []
    
    for nombre, metodo in metodos:
        try:
            x_opt, f_opt = metodo()
            if x_opt is not None and f_opt is not None:
                resultados.append((nombre, x_opt, f_opt))
        except Exception as e:
            print(f"   ❌ Error en {nombre}: {e}")
    
    # Mostrar comparación
    print(f"\n📈 RESUMEN DE RESULTADOS:")
    print(f"{'Método':<20} {'x*':<12} {'f(x*)':<12}")
    print("-" * 50)
    
    for nombre, x, f in resultados:
        print(f"{nombre:<20} {x:<12.8f} {f:<12.8f}")
    
    # Encontrar el mejor resultado
    if resultados:
        mejor = max(resultados, key=lambda item: item[2])
        print(f"\n🏆 MEJOR RESULTADO:")
        print(f"   Método: {mejor[0]}")
        print(f"   x* = {mejor[1]:.8f}")
        print(f"   f(x*) = {mejor[2]:.8f}")
        
        # Verificar que está en el dominio
        if 0 <= mejor[1] <= 1:
            print(f"   ✅ Solución válida en el dominio [0,1]")
        else:
            print(f"   ⚠️  Solución fuera del dominio")
        
        return mejor
    
    return None

def visualizar_resultado_final(mejor_resultado):
    """
    Crea una visualización final con el mejor resultado
    """
    if mejor_resultado is None:
        return
    
    nombre, x_opt, f_opt = mejor_resultado
    
    # Generar puntos para el gráfico
    x = np.linspace(0, 1, 1000)
    y = funcion_objetivo(x)
    
    # Crear gráfico final
    plt.figure(figsize=(12, 8))
    
    # Gráfico principal
    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'b-', linewidth=2, label='f(x) = x·sin(10πx) + 1')
    plt.plot(x_opt, f_opt, 'ro', markersize=10, label=f'Máximo global\n({x_opt:.6f}, {f_opt:.6f})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Maximización de f(x) = x·sin(10πx) + 1\nMétodo ganador: {nombre}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Zoom alrededor del máximo
    plt.subplot(2, 1, 2)
    delta = 0.05
    x_zoom = np.linspace(max(0, x_opt-delta), min(1, x_opt+delta), 200)
    y_zoom = funcion_objetivo(x_zoom)
    plt.plot(x_zoom, y_zoom, 'b-', linewidth=2)
    plt.plot(x_opt, f_opt, 'ro', markersize=10)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Zoom alrededor del máximo (±{delta})')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('c:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/3/3.1/resultado_final.png', 
                dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """
    Función principal que ejecuta todos los métodos
    """
    print("🎯 MAXIMIZACIÓN DE f(x) = x·sin(10πx) + 1 EN [0,1]")
    print("=" * 60)
    
    # 1. Analizar la función
    maximos_locales = analizar_funcion()
    
    # 2. Aplicar diferentes métodos
    mejor_resultado = comparar_metodos()
    
    # 3. Visualizar resultado final
    visualizar_resultado_final(mejor_resultado)
    
    # 4. Análisis final
    print(f"\n🔬 ANÁLISIS FINAL:")
    print(f"   • La función tiene múltiples máximos locales debido al término sin(10πx)")
    print(f"   • El factor x hace que los máximos cerca de x=1 sean más altos")
    print(f"   • Los métodos globales (evolución diferencial, fuerza bruta) son más confiables")
    print(f"   • El máximo global teórico está cerca de x ≈ 0.95-0.98")

if __name__ == "__main__":
    main()
