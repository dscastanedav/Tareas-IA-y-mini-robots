# -*- coding: utf-8 -*-
"""
Simulación de Propagación de Enfermedad usando Autómatas Celulares Probabilísticos
=================================================================================

Este script simula la propagación de una enfermedad en una población usando
autómatas celulares con reglas probabilísticas.

Estados:
🟦 SUSCEPTIBLE - Personas sanas que pueden infectarse
🟥 INFECTED - Personas infectadas que pueden contagiar
🟩 RECOVERED - Personas recuperadas (inmunes)

Autor: Estudiante IA
Fecha: Julio 2025
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
grid_size = 50          # Tamaño de la cuadrícula
infection_prob = 0.3    # Probabilidad de infección
recovery_prob = 0.1     # Probabilidad de recuperación
initial_infected = 10   # Número de infectados al inicio
steps = 100             # Número de pasos de simulación

# Estados
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

def initialize_grid(size, num_infected):
    """
    Inicializa la grilla con individuos susceptibles y algunos infectados aleatorios
    
    Args:
        size: Tamaño de la grilla (size x size)
        num_infected: Número inicial de infectados
    
    Returns:
        grid: Grilla inicializada
    """
    grid = np.zeros((size, size), dtype=int)
    
    # Colocar infectados iniciales en posiciones aleatorias
    for _ in range(num_infected):
        x, y = np.random.randint(0, size, 2)
        grid[x, y] = INFECTED
    
    return grid

def count_infected_neighbors(x, y, grid):
    """
    Cuenta el número de vecinos infectados (4-conectividad con bordes periódicos)
    
    Args:
        x, y: Coordenadas del individuo
        grid: Grilla actual
    
    Returns:
        Número de vecinos infectados
    """
    size = grid.shape[0]
    neighbors = [
        ((x-1) % size, y),      # Arriba
        ((x+1) % size, y),      # Abajo
        (x, (y-1) % size),      # Izquierda
        (x, (y+1) % size)       # Derecha
    ]
    return sum(grid[nx, ny] == INFECTED for nx, ny in neighbors)

def update_grid(grid, infection_prob, recovery_prob):
    """
    Actualiza la grilla aplicando las reglas del autómata celular
    
    Args:
        grid: Grilla actual
        infection_prob: Probabilidad de infección
        recovery_prob: Probabilidad de recuperación
    
    Returns:
        Nueva grilla actualizada
    """
    size = grid.shape[0]
    new_grid = grid.copy()
    
    for i in range(size):
        for j in range(size):
            if grid[i, j] == SUSCEPTIBLE:
                # Regla: Un susceptible se infecta si tiene vecinos infectados
                if count_infected_neighbors(i, j, grid) > 0:
                    if np.random.rand() < infection_prob:
                        new_grid[i, j] = INFECTED
            
            elif grid[i, j] == INFECTED:
                # Regla: Un infectado se recupera con cierta probabilidad
                if np.random.rand() < recovery_prob:
                    new_grid[i, j] = RECOVERED
    
    return new_grid

def simulate_disease_spread():
    """
    Ejecuta la simulación completa de propagación de enfermedad
    
    Returns:
        history_s, history_i, history_r: Listas con el historial de cada estado
    """
    # Inicializar
    grid = initialize_grid(grid_size, initial_infected)
    
    # Historial para graficar
    history_s = []
    history_i = []
    history_r = []
    
    print("🦠 Iniciando simulación de propagación de enfermedad...")
    print(f"📊 Parámetros:")
    print(f"   • Tamaño de grilla: {grid_size}x{grid_size}")
    print(f"   • Probabilidad de infección: {infection_prob}")
    print(f"   • Probabilidad de recuperación: {recovery_prob}")
    print(f"   • Infectados iniciales: {initial_infected}")
    print(f"   • Pasos de simulación: {steps}")
    print()
    
    # Simulación
    for step in range(steps):
        # Actualizar grilla
        grid = update_grid(grid, infection_prob, recovery_prob)
        
        # Registrar estadísticas
        susceptible_count = np.sum(grid == SUSCEPTIBLE)
        infected_count = np.sum(grid == INFECTED)
        recovered_count = np.sum(grid == RECOVERED)
        
        history_s.append(susceptible_count)
        history_i.append(infected_count)
        history_r.append(recovered_count)
        
        # Mostrar progreso cada 20 pasos
        if step % 20 == 0:
            print(f"Paso {step:3d}: S={susceptible_count:4d}, I={infected_count:4d}, R={recovered_count:4d}")
        
        # Terminar si no hay más infectados
        if infected_count == 0:
            print(f"\n🎯 Simulación terminó en el paso {step} (no hay más infectados)")
            break
    
    print(f"\n✅ Simulación completada!")
    return history_s, history_i, history_r

def plot_results(history_s, history_i, history_r):
    """
    Crea gráficos de los resultados de la simulación
    
    Args:
        history_s, history_i, history_r: Historiales de cada estado
    """
    plt.figure(figsize=(12, 8))
    
    # Gráfico principal
    plt.subplot(2, 1, 1)
    plt.plot(history_s, label='🟦 Susceptible', color='blue', linewidth=2)
    plt.plot(history_i, label='🟥 Infected', color='red', linewidth=2)
    plt.plot(history_r, label='🟩 Recovered', color='green', linewidth=2)
    plt.xlabel("Paso de tiempo")
    plt.ylabel("Número de individuos")
    plt.title("Simulación de Propagación de Enfermedad usando Autómatas Celulares Probabilísticos")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfico de porcentajes
    plt.subplot(2, 1, 2)
    total_population = grid_size * grid_size
    plt.plot([s/total_population*100 for s in history_s], label='% Susceptible', color='blue', linewidth=2)
    plt.plot([i/total_population*100 for i in history_i], label='% Infected', color='red', linewidth=2)
    plt.plot([r/total_population*100 for r in history_r], label='% Recovered', color='green', linewidth=2)
    plt.xlabel("Paso de tiempo")
    plt.ylabel("Porcentaje de población")
    plt.title("Distribución Porcentual de Estados")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Estadísticas finales
    print(f"\n📈 Estadísticas finales:")
    print(f"   • Susceptibles: {history_s[-1]} ({history_s[-1]/total_population*100:.1f}%)")
    print(f"   • Infectados: {history_i[-1]} ({history_i[-1]/total_population*100:.1f}%)")
    print(f"   • Recuperados: {history_r[-1]} ({history_r[-1]/total_population*100:.1f}%)")
    print(f"   • Total afectados: {history_r[-1] + history_i[-1]} ({(history_r[-1] + history_i[-1])/total_population*100:.1f}%)")

def main():
    """Función principal"""
    print("=" * 80)
    print("🦠 SIMULACIÓN DE PROPAGACIÓN DE ENFERMEDAD")
    print("   Usando Autómatas Celulares Probabilísticos")
    print("=" * 80)
    
    # Ejecutar simulación
    history_s, history_i, history_r = simulate_disease_spread()
    
    # Mostrar resultados
    plot_results(history_s, history_i, history_r)

if __name__ == "__main__":
    main()
