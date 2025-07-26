# -*- coding: utf-8 -*-
"""
Despacho Óptimo de Energía Eléctrica usando Algoritmos Genéticos
================================================================

Optimiza la distribución de energía eléctrica desde 4 plantas generadoras
hacia 4 ciudades, minimizando costos de transporte y generación.

Plantas: C, B, M, B (capacidades: 3, 6, 5, 4 GW)
Ciudades: Cali, Bogotá, Medellín, Barranquilla (demandas: 4, 3, 5, 3 GW)

Autor: Estudiante IA
Fecha: Julio 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import random

class DespachoEnergiaAG:
    """
    Sistema de despacho óptimo de energía usando Algoritmos Genéticos
    """
    
    def __init__(self):
        """Inicializa el sistema de despacho de energía"""
        
        # Configuración del problema
        self.plantas = ['Planta C', 'Planta B', 'Planta M', 'Planta B2']
        self.ciudades = ['Cali', 'Bogotá', 'Medellín', 'Barranquilla']
        
        # Capacidades de generación (GW)
        self.capacidades = np.array([3, 6, 5, 4])  # C, B, M, B2
        
        # Demandas de las ciudades (GW)
        self.demandas = np.array([4, 3, 5, 3])     # Cali, Bogotá, Medellín, Barranquilla
        
        # Costos de transporte ($/GW) - matriz 4x4
        self.costos_transporte = np.array([
            [1, 4, 3, 6],  # Planta C
            [4, 1, 4, 5],  # Planta B
            [3, 4, 1, 4],  # Planta M
            [6, 5, 4, 1]   # Planta B2
        ])
        
        # Costos de generación ($/KW-H)
        self.costos_generacion = np.array([680, 720, 660, 750])  # C, B, M, B2
        
        # Parámetros del Algoritmo Genético
        self.tamaño_poblacion = 80
        self.num_generaciones = 150
        self.tasa_mutacion = 0.15
        self.tasa_cruce = 0.8
        self.elite_size = 8
        
        print("⚡ SISTEMA DE DESPACHO DE ENERGÍA INICIALIZADO")
        print("=" * 50)
        self.mostrar_configuracion()
    
    def mostrar_configuracion(self):
        """Muestra la configuración del problema"""
        print("\n🏭 PLANTAS GENERADORAS:")
        for i, planta in enumerate(self.plantas):
            print(f"  {planta}: {self.capacidades[i]} GW - ${self.costos_generacion[i]}/KW-H")
        
        print(f"\nOferta total: {self.capacidades.sum()} GW")
        
        print("\n🏙️ CIUDADES Y DEMANDAS:")
        for i, ciudad in enumerate(self.ciudades):
            print(f"  {ciudad}: {self.demandas[i]} GW")
        
        print(f"Demanda total: {self.demandas.sum()} GW")
        
        print("\n🚛 COSTOS DE TRANSPORTE ($/GW):")
        print("        ", "  ".join(f"{c:8s}" for c in self.ciudades))
        for i, planta in enumerate(self.plantas):
            costos_str = "  ".join(f"{self.costos_transporte[i,j]:8.0f}" for j in range(len(self.ciudades)))
            print(f"{planta:8s} {costos_str}")
    
    def crear_individuo(self):
        """
        Crea un individuo (solución) válido
        
        Returns:
            Matriz 4x4 con la distribución de energía
        """
        # Inicializar matriz de distribución
        distribucion = np.zeros((4, 4))
        
        # Capacidades y demandas disponibles
        cap_disponible = self.capacidades.copy()
        dem_pendiente = self.demandas.copy()
        
        # Llenar la matriz satisfaciendo restricciones
        for ciudad in range(4):
            for planta in range(4):
                if cap_disponible[planta] > 0 and dem_pendiente[ciudad] > 0:
                    # Asignar la menor cantidad entre capacidad disponible y demanda pendiente
                    cantidad = min(cap_disponible[planta], dem_pendiente[ciudad])
                    # Agregar aleatoriedad (0% a 100% de la cantidad posible)
                    cantidad = random.uniform(0, cantidad)
                    
                    distribucion[planta, ciudad] = cantidad
                    cap_disponible[planta] -= cantidad
                    dem_pendiente[ciudad] -= cantidad
        
        # Ajustar para satisfacer exactamente las demandas
        for ciudad in range(4):
            deficit = self.demandas[ciudad] - distribucion[:, ciudad].sum()
            if deficit > 0:
                # Buscar plantas con capacidad disponible
                for planta in range(4):
                    if cap_disponible[planta] > 0:
                        cantidad_agregar = min(deficit, cap_disponible[planta])
                        distribucion[planta, ciudad] += cantidad_agregar
                        cap_disponible[planta] -= cantidad_agregar
                        deficit -= cantidad_agregar
                        if deficit <= 0:
                            break
        
        return distribucion
    
    def calcular_fitness(self, individuo):
        """
        Calcula el fitness de un individuo (menor costo es mejor)
        
        Args:
            individuo: Matriz 4x4 de distribución de energía
            
        Returns:
            Fitness (se invierte para que mayor sea mejor)
        """
        # Verificar restricciones
        if not self.es_factible(individuo):
            return 0.001  # Penalizar soluciones no factibles
        
        # Calcular costo de transporte
        costo_transporte = np.sum(individuo * self.costos_transporte)
        
        # Calcular costo de generación
        generacion_por_planta = np.sum(individuo, axis=1)
        costo_generacion = np.sum(generacion_por_planta * self.costos_generacion)
        
        costo_total = costo_transporte + costo_generacion
        
        # Invertir para que mayor fitness sea mejor
        return 1.0 / (1.0 + costo_total)
    
    def es_factible(self, individuo):
        """
        Verifica si una solución es factible
        
        Args:
            individuo: Matriz de distribución
            
        Returns:
            True si es factible, False si no
        """
        # Verificar capacidades de plantas
        generacion_por_planta = np.sum(individuo, axis=1)
        if np.any(generacion_por_planta > self.capacidades + 0.01):  # Tolerancia pequeña
            return False
        
        # Verificar satisfacción de demandas
        suministro_por_ciudad = np.sum(individuo, axis=0)
        if np.any(np.abs(suministro_por_ciudad - self.demandas) > 0.01):  # Tolerancia pequeña
            return False
        
        # Verificar no negativos
        if np.any(individuo < 0):
            return False
        
        return True
    
    def seleccion_torneo(self, poblacion, fitness_scores, tamaño_torneo=3):
        """Selección por torneo"""
        participantes = random.sample(list(zip(poblacion, fitness_scores)), tamaño_torneo)
        ganador = max(participantes, key=lambda x: x[1])
        return ganador[0].copy()
    
    def cruzamiento(self, padre1, padre2):
        """
        Cruzamiento aritmético entre dos padres
        
        Returns:
            Dos hijos como combinación de los padres
        """
        if random.random() > self.tasa_cruce:
            return padre1.copy(), padre2.copy()
        
        # Cruzamiento aritmético con peso aleatorio
        alpha = random.uniform(0, 1)
        hijo1 = alpha * padre1 + (1 - alpha) * padre2
        hijo2 = (1 - alpha) * padre1 + alpha * padre2
        
        # Reparar si es necesario
        hijo1 = self.reparar_solucion(hijo1)
        hijo2 = self.reparar_solucion(hijo2)
        
        return hijo1, hijo2
    
    def mutacion(self, individuo):
        """
        Mutación: pequeñas variaciones aleatorias
        
        Returns:
            Individuo mutado
        """
        individuo_mutado = individuo.copy()
        
        # Aplicar mutación con cierta probabilidad
        if random.random() < self.tasa_mutacion:
            # Seleccionar posiciones aleatorias para mutar
            for _ in range(random.randint(1, 3)):
                i, j = random.randint(0, 3), random.randint(0, 3)
                # Pequeña variación aleatoria
                variacion = random.uniform(-0.5, 0.5)
                individuo_mutado[i, j] += variacion
                
                # Asegurar no negativos
                if individuo_mutado[i, j] < 0:
                    individuo_mutado[i, j] = 0
        
        # Reparar la solución
        return self.reparar_solucion(individuo_mutado)
    
    def reparar_solucion(self, individuo):
        """
        Repara una solución para que cumpla las restricciones
        
        Returns:
            Solución reparada
        """
        individuo_reparado = individuo.copy()
        
        # Paso 1: Asegurar que no se excedan capacidades
        for planta in range(4):
            generacion_total = np.sum(individuo_reparado[planta, :])
            if generacion_total > self.capacidades[planta]:
                # Escalar proporcionalmente
                factor = self.capacidades[planta] / generacion_total
                individuo_reparado[planta, :] *= factor
        
        # Paso 2: Ajustar para satisfacer demandas
        for ciudad in range(4):
            suministro_actual = np.sum(individuo_reparado[:, ciudad])
            deficit = self.demandas[ciudad] - suministro_actual
            
            if abs(deficit) > 0.01:
                # Distribuir el déficit entre plantas con capacidad disponible
                for planta in range(4):
                    cap_disponible = self.capacidades[planta] - np.sum(individuo_reparado[planta, :])
                    if cap_disponible > 0 and deficit > 0:
                        cantidad = min(deficit, cap_disponible)
                        individuo_reparado[planta, ciudad] += cantidad
                        deficit -= cantidad
        
        return individuo_reparado
    
    def algoritmo_genetico(self):
        """Ejecuta el algoritmo genético"""
        print(f"\n🧬 EJECUTANDO ALGORITMO GENÉTICO")
        print("=" * 40)
        print(f"Población: {self.tamaño_poblacion}, Generaciones: {self.num_generaciones}")
        
        # Crear población inicial
        poblacion = [self.crear_individuo() for _ in range(self.tamaño_poblacion)]
        
        mejor_fitness_historia = []
        fitness_promedio_historia = []
        mejor_solucion = None
        mejor_fitness_global = 0
        
        for generacion in range(self.num_generaciones):
            # Evaluar fitness
            fitness_scores = [self.calcular_fitness(individuo) for individuo in poblacion]
            
            # Estadísticas
            mejor_fitness = max(fitness_scores)
            fitness_promedio = np.mean(fitness_scores)
            
            mejor_fitness_historia.append(mejor_fitness)
            fitness_promedio_historia.append(fitness_promedio)
            
            # Actualizar mejor solución global
            if mejor_fitness > mejor_fitness_global:
                mejor_fitness_global = mejor_fitness
                mejor_solucion = poblacion[np.argmax(fitness_scores)].copy()
            
            # Mostrar progreso
            if generacion % 30 == 0 or generacion == self.num_generaciones - 1:
                costo = 1.0 / mejor_fitness - 1.0 if mejor_fitness > 0 else float('inf')
                print(f"Gen {generacion:3d}: Fitness = {mejor_fitness:.6f}, Costo = ${costo:,.0f}")
            
            # Elitismo
            indices_elite = np.argsort(fitness_scores)[-self.elite_size:]
            elite = [poblacion[i].copy() for i in indices_elite]
            
            # Crear nueva población
            nueva_poblacion = elite.copy()
            
            while len(nueva_poblacion) < self.tamaño_poblacion:
                # Selección
                padre1 = self.seleccion_torneo(poblacion, fitness_scores)
                padre2 = self.seleccion_torneo(poblacion, fitness_scores)
                
                # Cruzamiento
                hijo1, hijo2 = self.cruzamiento(padre1, padre2)
                
                # Mutación
                hijo1 = self.mutacion(hijo1)
                hijo2 = self.mutacion(hijo2)
                
                nueva_poblacion.extend([hijo1, hijo2])
            
            poblacion = nueva_poblacion[:self.tamaño_poblacion]
        
        print(f"\n✅ Optimización completada!")
        costo_final = 1.0 / mejor_fitness_global - 1.0
        print(f"Mejor costo encontrado: ${costo_final:,.0f}")
        
        return mejor_solucion, mejor_fitness_historia, fitness_promedio_historia
    
    def analizar_solucion(self, solucion):
        """Analiza y muestra la mejor solución encontrada"""
        print(f"\n📊 ANÁLISIS DE LA SOLUCIÓN ÓPTIMA")
        print("=" * 50)
        
        # Mostrar matriz de distribución
        print("\n⚡ DISTRIBUCIÓN DE ENERGÍA (GW):")
        print("        ", "  ".join(f"{c:8s}" for c in self.ciudades))
        for i, planta in enumerate(self.plantas):
            valores_str = "  ".join(f"{solucion[i,j]:8.2f}" for j in range(4))
            print(f"{planta:8s} {valores_str}")
        
        # Verificaciones
        print(f"\n✅ VERIFICACIÓN DE RESTRICCIONES:")
        
        # Generación por planta
        generacion_por_planta = np.sum(solucion, axis=1)
        print("Generación por planta:")
        for i, planta in enumerate(self.plantas):
            print(f"  {planta}: {generacion_por_planta[i]:.2f} GW (máx: {self.capacidades[i]} GW)")
        
        # Suministro por ciudad
        suministro_por_ciudad = np.sum(solucion, axis=0)
        print("\nSuministro por ciudad:")
        for i, ciudad in enumerate(self.ciudades):
            print(f"  {ciudad}: {suministro_por_ciudad[i]:.2f} GW (req: {self.demandas[i]} GW)")
        
        # Cálculo de costos
        costo_transporte = np.sum(solucion * self.costos_transporte)
        costo_generacion = np.sum(generacion_por_planta * self.costos_generacion)
        costo_total = costo_transporte + costo_generacion
        
        print(f"\n💰 ANÁLISIS DE COSTOS:")
        print(f"Costo de transporte: ${costo_transporte:,.0f}")
        print(f"Costo de generación: ${costo_generacion:,.0f}")
        print(f"COSTO TOTAL: ${costo_total:,.0f}")
    
    def visualizar_resultados(self, solucion, historia_fitness):
        """Crea visualizaciones de los resultados"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Matriz de distribución
        im = ax1.imshow(solucion, cmap='Blues', aspect='auto')
        ax1.set_title('Distribución de Energía (GW)', fontweight='bold')
        ax1.set_xlabel('Ciudades')
        ax1.set_ylabel('Plantas')
        ax1.set_xticks(range(4))
        ax1.set_xticklabels(self.ciudades, rotation=45)
        ax1.set_yticks(range(4))
        ax1.set_yticklabels(self.plantas)
        
        # Agregar valores en la matriz
        for i in range(4):
            for j in range(4):
                ax1.text(j, i, f'{solucion[i,j]:.1f}', ha='center', va='center', fontweight='bold')
        
        plt.colorbar(im, ax=ax1)
        
        # 2. Evolución del fitness
        mejor_fitness, fitness_promedio = historia_fitness
        generations = range(len(mejor_fitness))
        
        ax2.plot(generations, mejor_fitness, 'b-', linewidth=2, label='Mejor fitness')
        ax2.plot(generations, fitness_promedio, 'r--', linewidth=1, label='Fitness promedio')
        ax2.set_xlabel('Generación')
        ax2.set_ylabel('Fitness')
        ax2.set_title('Evolución del Algoritmo Genético', fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Generación vs Capacidad
        generacion_por_planta = np.sum(solucion, axis=1)
        x = np.arange(len(self.plantas))
        
        bars1 = ax3.bar(x - 0.2, self.capacidades, 0.4, label='Capacidad máxima', alpha=0.7, color='lightblue')
        bars2 = ax3.bar(x + 0.2, generacion_por_planta, 0.4, label='Generación asignada', alpha=0.7, color='orange')
        
        ax3.set_xlabel('Plantas')
        ax3.set_ylabel('Energía (GW)')
        ax3.set_title('Capacidad vs Generación por Planta', fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(self.plantas, rotation=45)
        ax3.legend()
        ax3.grid(True, alpha=0.3, axis='y')
        
        # 4. Demanda vs Suministro
        suministro_por_ciudad = np.sum(solucion, axis=0)
        x = np.arange(len(self.ciudades))
        
        bars1 = ax4.bar(x - 0.2, self.demandas, 0.4, label='Demanda requerida', alpha=0.7, color='lightcoral')
        bars2 = ax4.bar(x + 0.2, suministro_por_ciudad, 0.4, label='Suministro asignado', alpha=0.7, color='lightgreen')
        
        ax4.set_xlabel('Ciudades')
        ax4.set_ylabel('Energía (GW)')
        ax4.set_title('Demanda vs Suministro por Ciudad', fontweight='bold')
        ax4.set_xticks(x)
        ax4.set_xticklabels(self.ciudades, rotation=45)
        ax4.legend()
        ax4.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig('c:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/3/3.3/resultados_despacho.png',
                   dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """Función principal"""
    print("⚡ DESPACHO ÓPTIMO DE ENERGÍA ELÉCTRICA")
    print("=" * 50)
    print("Optimización usando Algoritmos Genéticos")
    print("=" * 50)
    
    # Crear sistema
    sistema = DespachoEnergiaAG()
    
    # Ejecutar algoritmo genético
    mejor_solucion, mejor_fitness_historia, fitness_promedio_historia = sistema.algoritmo_genetico()
    
    # Analizar resultados
    sistema.analizar_solucion(mejor_solucion)
    
    # Visualizar resultados
    sistema.visualizar_resultados(mejor_solucion, (mejor_fitness_historia, fitness_promedio_historia))
    
    print(f"\n🎯 CONCLUSIÓN:")
    print(f"El algoritmo genético encontró la distribución óptima de energía")
    print(f"que minimiza los costos totales de transporte y generación.")

if __name__ == "__main__":
    main()
