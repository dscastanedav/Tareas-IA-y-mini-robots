#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verdadera Democracia - Distribución del Poder usando Algoritmos Genéticos
========================================================================

Este script simula la distribución democrática del poder político entre partidos
usando Algoritmos Genéticos para optimizar la asignación de ministerios y entidades
estatales basándose en la representación parlamentaria.

Escenario:
- 5 partidos políticos
- 50 curules distribuidas aleatoriamente
- 50 entidades estatales con diferentes pesos de poder
- Objetivo: Distribución proporcional y justa del poder

Autor: Estudiante IA
Fecha: Julio 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from dataclasses import dataclass
from typing import List, Tuple, Dict
import seaborn as sns

# Configurar estilo de gráficos
plt.style.use('default')
sns.set_palette("husl")

@dataclass
class Partido:
    """Clase para representar un partido político"""
    nombre: str
    color: str
    curules: int
    porcentaje_representacion: float

@dataclass
class Entidad:
    """Clase para representar una entidad estatal"""
    nombre: str
    peso_poder: int
    categoria: str

class SistemaDemocraticoAG:
    """
    Sistema de distribución democrática del poder usando Algoritmos Genéticos
    """
    
    def __init__(self, semilla=42):
        """
        Inicializa el sistema democrático
        
        Args:
            semilla: Semilla para reproducibilidad
        """
        np.random.seed(semilla)
        random.seed(semilla)
        
        self.partidos = self._crear_partidos()
        self.entidades = self._crear_entidades()
        self.matriz_poder = None
        
        # Parámetros del Algoritmo Genético
        self.tamaño_poblacion = 100
        self.num_generaciones = 200
        self.tasa_mutacion = 0.1
        self.tasa_cruce = 0.8
        self.elite_size = 10
        
    def _crear_partidos(self) -> List[Partido]:
        """
        Crea los 5 partidos políticos con distribución aleatoria de curules
        """
        nombres_partidos = [
            "Partido Progresista",
            "Alianza Democrática", 
            "Movimiento Nacional",
            "Frente Popular",
            "Coalición Liberal"
        ]
        
        colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
        
        # Generar distribución aleatoria no uniforme de curules
        # Usar distribución Dirichlet para garantizar que sumen 50
        alpha = [1, 2, 3, 2, 1]  # Parámetros para sesgar la distribución
        proporciones = np.random.dirichlet(alpha)
        curules_distribucion = np.round(proporciones * 50).astype(int)
        
        # Ajustar para que sumen exactamente 50
        diferencia = 50 - curules_distribucion.sum()
        curules_distribucion[0] += diferencia
        
        partidos = []
        for i, (nombre, color) in enumerate(zip(nombres_partidos, colores)):
            curules = curules_distribucion[i]
            porcentaje = (curules / 50) * 100
            partidos.append(Partido(nombre, color, curules, porcentaje))
        
        return partidos
    
    def _crear_entidades(self) -> List[Entidad]:
        """
        Crea 50 entidades estatales con pesos de poder aleatorios
        """
        nombres_ministerios = [
            "Ministerio del Interior", "Ministerio de Relaciones Exteriores",
            "Ministerio de Hacienda", "Ministerio de Defensa", "Ministerio de Justicia",
            "Ministerio de Salud", "Ministerio de Educación", "Ministerio de Trabajo",
            "Ministerio de Agricultura", "Ministerio de Transporte", "Ministerio de Ambiente",
            "Ministerio de Vivienda", "Ministerio de Comunicaciones", "Ministerio de Cultura",
            "Ministerio de Deporte"
        ]
        
        agencias_importantes = [
            "Banco Central", "Contraloría General", "Procuraduría General",
            "Fiscalía General", "Registraduría Nacional", "DANE",
            "Superintendencia Financiera", "Superintendencia de Servicios",
            "Agencia Nacional de Hidrocarburos", "Agencia Nacional de Minería"
        ]
        
        entidades_menores = [
            "Instituto Geográfico", "Instituto de Meteorología", "Instituto de Salud",
            "Centro de Memoria Histórica", "Agencia de Cooperación", "Instituto de Turismo",
            "Servicio Geológico", "Instituto de Vigilancia", "Agencia Digital",
            "Instituto de Desarrollo", "Servicio Nacional de Aprendizaje", "Instituto Cultural",
            "Agencia de Renovación", "Instituto de Investigación", "Servicio de Estadística",
            "Instituto Tecnológico", "Agencia de Infraestructura", "Instituto Científico",
            "Servicio de Información", "Instituto de Innovación", "Agencia de Desarrollo",
            "Instituto de Paz", "Servicio Nacional", "Agencia de Modernización",
            "Instituto de Gestión"
        ]
        
        entidades = []
        
        # Ministerios (alto poder: 70-100 puntos)
        for nombre in nombres_ministerios:
            peso = np.random.randint(70, 101)
            entidades.append(Entidad(nombre, peso, "Ministerio"))
        
        # Agencias importantes (poder medio: 40-80 puntos)
        for nombre in agencias_importantes:
            peso = np.random.randint(40, 81)
            entidades.append(Entidad(nombre, peso, "Agencia"))
        
        # Entidades menores (poder bajo: 1-50 puntos)
        for nombre in entidades_menores:
            peso = np.random.randint(1, 51)
            entidades.append(Entidad(nombre, peso, "Instituto"))
        
        return entidades
    
    def mostrar_congreso(self):
        """
        Muestra la composición del congreso
        """
        print("🏛️ COMPOSICIÓN DEL CONGRESO")
        print("=" * 50)
        
        total_curules = sum(p.curules for p in self.partidos)
        print(f"Total de curules: {total_curules}")
        print()
        
        for partido in self.partidos:
            barra = "█" * int(partido.curules / 2)  # Escala visual
            print(f"{partido.nombre:<20} {partido.curules:2d} curules ({partido.porcentaje:5.1f}%) {barra}")
        
        print()
    
    def mostrar_entidades(self):
        """
        Muestra las entidades estatales y su poder
        """
        print("🏢 ENTIDADES ESTATALES Y SU PESO DE PODER")
        print("=" * 60)
        
        # Agrupar por categoría
        categorias = {}
        for entidad in self.entidades:
            if entidad.categoria not in categorias:
                categorias[entidad.categoria] = []
            categorias[entidad.categoria].append(entidad)
        
        poder_total = sum(e.peso_poder for e in self.entidades)
        print(f"Poder total a distribuir: {poder_total} puntos\n")
        
        for categoria, entidades_cat in categorias.items():
            print(f"📋 {categoria}s:")
            poder_categoria = sum(e.peso_poder for e in entidades_cat)
            print(f"   Poder de categoría: {poder_categoria} puntos")
            
            for entidad in sorted(entidades_cat, key=lambda x: x.peso_poder, reverse=True):
                print(f"   • {entidad.nombre:<35} {entidad.peso_poder:3d} puntos")
            print()
    
    def crear_individuo(self) -> np.ndarray:
        """
        Crea un individuo (solución) aleatorio
        Cada entidad se asigna a un partido (0-4)
        
        Returns:
            Array de asignaciones de entidades a partidos
        """
        return np.random.randint(0, len(self.partidos), len(self.entidades))
    
    def calcular_fitness(self, individuo: np.ndarray) -> float:
        """
        Calcula la fitness de un individuo basándose en la proporcionalidad
        
        Args:
            individuo: Asignación de entidades a partidos
            
        Returns:
            Valor de fitness (mayor es mejor)
        """
        # Calcular poder acumulado por cada partido
        poder_por_partido = np.zeros(len(self.partidos))
        
        for i, partido_asignado in enumerate(individuo):
            poder_por_partido[partido_asignado] += self.entidades[i].peso_poder
        
        poder_total = poder_por_partido.sum()
        proporcion_poder = poder_por_partido / poder_total
        
        # Proporción ideal basada en representación parlamentaria
        proporcion_ideal = np.array([p.porcentaje / 100 for p in self.partidos])
        
        # Calcular diferencia entre proporción real e ideal
        diferencia = np.abs(proporcion_poder - proporcion_ideal)
        
        # Fitness es inversamente proporcional a la diferencia
        # Usar 1 / (1 + suma_diferencias) para que esté entre 0 y 1
        fitness = 1 / (1 + diferencia.sum())
        
        return fitness
    
    def seleccion_torneo(self, poblacion: List[np.ndarray], fitness_scores: List[float], 
                        tamaño_torneo: int = 3) -> np.ndarray:
        """
        Selección por torneo
        
        Args:
            poblacion: Lista de individuos
            fitness_scores: Puntuaciones de fitness
            tamaño_torneo: Tamaño del torneo
            
        Returns:
            Individuo seleccionado
        """
        participantes = random.sample(list(zip(poblacion, fitness_scores)), tamaño_torneo)
        ganador = max(participantes, key=lambda x: x[1])
        return ganador[0].copy()
    
    def cruzamiento(self, padre1: np.ndarray, padre2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Cruzamiento de un punto
        
        Args:
            padre1, padre2: Individuos padre
            
        Returns:
            Dos individuos hijo
        """
        if random.random() > self.tasa_cruce:
            return padre1.copy(), padre2.copy()
        
        punto_cruce = random.randint(1, len(padre1) - 1)
        
        hijo1 = np.concatenate([padre1[:punto_cruce], padre2[punto_cruce:]])
        hijo2 = np.concatenate([padre2[:punto_cruce], padre1[punto_cruce:]])
        
        return hijo1, hijo2
    
    def mutacion(self, individuo: np.ndarray) -> np.ndarray:
        """
        Mutación: cambiar aleatoriamente algunas asignaciones
        
        Args:
            individuo: Individuo a mutar
            
        Returns:
            Individuo mutado
        """
        individuo_mutado = individuo.copy()
        
        for i in range(len(individuo_mutado)):
            if random.random() < self.tasa_mutacion:
                individuo_mutado[i] = random.randint(0, len(self.partidos) - 1)
        
        return individuo_mutado
    
    def algoritmo_genetico(self):
        """
        Ejecuta el algoritmo genético para optimizar la distribución del poder
        """
        print("🧬 EJECUTANDO ALGORITMO GENÉTICO")
        print("=" * 50)
        print(f"Parámetros:")
        print(f"• Tamaño población: {self.tamaño_poblacion}")
        print(f"• Generaciones: {self.num_generaciones}")
        print(f"• Tasa mutación: {self.tasa_mutacion}")
        print(f"• Tasa cruce: {self.tasa_cruce}")
        print()
        
        # Crear población inicial
        poblacion = [self.crear_individuo() for _ in range(self.tamaño_poblacion)]
        
        mejor_fitness_historia = []
        fitness_promedio_historia = []
        
        for generacion in range(self.num_generaciones):
            # Evaluar fitness
            fitness_scores = [self.calcular_fitness(individuo) for individuo in poblacion]
            
            # Estadísticas
            mejor_fitness = max(fitness_scores)
            fitness_promedio = np.mean(fitness_scores)
            
            mejor_fitness_historia.append(mejor_fitness)
            fitness_promedio_historia.append(fitness_promedio)
            
            # Mostrar progreso cada 25 generaciones
            if generacion % 25 == 0:
                print(f"Generación {generacion:3d}: Mejor fitness = {mejor_fitness:.6f}, "
                      f"Promedio = {fitness_promedio:.6f}")
            
            # Elitismo: conservar los mejores individuos
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
            
            # Mantener tamaño de población
            poblacion = nueva_poblacion[:self.tamaño_poblacion]
        
        # Encontrar la mejor solución final
        fitness_final = [self.calcular_fitness(individuo) for individuo in poblacion]
        mejor_individuo = poblacion[np.argmax(fitness_final)]
        mejor_fitness_final = max(fitness_final)
        
        print(f"\n✅ Algoritmo completado!")
        print(f"Mejor fitness final: {mejor_fitness_final:.6f}")
        
        # Guardar matriz de poder
        self.matriz_poder = mejor_individuo
        
        return mejor_fitness_historia, fitness_promedio_historia
    
    def analizar_distribucion(self):
        """
        Analiza la distribución final del poder
        """
        if self.matriz_poder is None:
            print("❌ Primero debe ejecutar el algoritmo genético")
            return
        
        print("\n📊 ANÁLISIS DE LA DISTRIBUCIÓN FINAL")
        print("=" * 60)
        
        # Calcular poder por partido
        poder_por_partido = np.zeros(len(self.partidos))
        entidades_por_partido = [[] for _ in range(len(self.partidos))]
        
        for i, partido_asignado in enumerate(self.matriz_poder):
            entidad = self.entidades[i]
            poder_por_partido[partido_asignado] += entidad.peso_poder
            entidades_por_partido[partido_asignado].append(entidad)
        
        poder_total = poder_por_partido.sum()
        
        print("🏆 DISTRIBUCIÓN DEL PODER POR PARTIDO:")
        print(f"{'Partido':<20} {'Curules':<8} {'%Parl':<6} {'Poder':<8} {'%Poder':<7} {'Diferencia':<10} {'Entidades':<10}")
        print("-" * 80)
        
        for i, partido in enumerate(self.partidos):
            porcentaje_poder = (poder_por_partido[i] / poder_total) * 100
            diferencia = porcentaje_poder - partido.porcentaje_representacion
            num_entidades = len(entidades_por_partido[i])
            
            print(f"{partido.nombre:<20} {partido.curules:<8} {partido.porcentaje_representacion:<6.1f} "
                  f"{poder_por_partido[i]:<8.0f} {porcentaje_poder:<7.1f} {diferencia:<+10.1f} {num_entidades:<10}")
        
        print(f"\nPoder total distribuido: {poder_total:.0f} puntos")
        
        # Mostrar entidades por partido
        print(f"\n🏢 ENTIDADES ASIGNADAS POR PARTIDO:")
        for i, partido in enumerate(self.partidos):
            print(f"\n{partido.nombre} ({len(entidades_por_partido[i])} entidades):")
            entidades_ordenadas = sorted(entidades_por_partido[i], 
                                       key=lambda x: x.peso_poder, reverse=True)
            
            for entidad in entidades_ordenadas[:10]:  # Mostrar top 10
                print(f"  • {entidad.nombre:<35} {entidad.peso_poder:3d} puntos ({entidad.categoria})")
            
            if len(entidades_ordenadas) > 10:
                print(f"  ... y {len(entidades_ordenadas) - 10} entidades más")
    
    def visualizar_resultados(self, historia_fitness):
        """
        Crea visualizaciones de los resultados
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # 1. Composición del Congreso
        nombres = [p.nombre.replace(' ', '\n') for p in self.partidos]
        curules = [p.curules for p in self.partidos]
        colores = [p.color for p in self.partidos]
        
        ax1.pie(curules, labels=nombres, colors=colores, autopct='%1.1f%%', startangle=90)
        ax1.set_title('Composición del Congreso\n(50 curules)', fontsize=12, fontweight='bold')
        
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
        
        # 3. Distribución del poder
        if self.matriz_poder is not None:
            poder_por_partido = np.zeros(len(self.partidos))
            for i, partido_asignado in enumerate(self.matriz_poder):
                poder_por_partido[partido_asignado] += self.entidades[i].peso_poder
            
            poder_total = poder_por_partido.sum()
            porcentaje_poder = (poder_por_partido / poder_total) * 100
            porcentaje_parlamento = [p.porcentaje_representacion for p in self.partidos]
            
            x = np.arange(len(self.partidos))
            width = 0.35
            
            bars1 = ax3.bar(x - width/2, porcentaje_parlamento, width, 
                           label='% Parlamentario', color='lightblue', alpha=0.7)
            bars2 = ax3.bar(x + width/2, porcentaje_poder, width,
                           label='% Poder Asignado', color='lightcoral', alpha=0.7)
            
            ax3.set_xlabel('Partidos')
            ax3.set_ylabel('Porcentaje (%)')
            ax3.set_title('Comparación: Representación vs Poder Asignado', fontweight='bold')
            ax3.set_xticks(x)
            ax3.set_xticklabels([p.nombre.replace(' ', '\n') for p in self.partidos], 
                               rotation=45, ha='right')
            ax3.legend()
            ax3.grid(True, alpha=0.3, axis='y')
            
            # 4. Diferencias (proporcionalidad)
            diferencias = porcentaje_poder - np.array(porcentaje_parlamento)
            colors = ['green' if d >= 0 else 'red' for d in diferencias]
            
            bars = ax4.bar(range(len(diferencias)), diferencias, color=colors, alpha=0.7)
            ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
            ax4.set_xlabel('Partidos')
            ax4.set_ylabel('Diferencia (%)')
            ax4.set_title('Desviación de la Proporcionalidad', fontweight='bold')
            ax4.set_xticks(range(len(self.partidos)))
            ax4.set_xticklabels([p.nombre.replace(' ', '\n') for p in self.partidos],
                               rotation=45, ha='right')
            ax4.grid(True, alpha=0.3, axis='y')
            
            # Agregar valores en las barras
            for bar, valor in zip(bars, diferencias):
                height = bar.get_height()
                ax4.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height >= 0 else -0.3),
                        f'{valor:.1f}%', ha='center', va='bottom' if height >= 0 else 'top')
        
        plt.tight_layout()
        plt.savefig('c:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/3/3.2/resultados_democracia.png',
                   dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """
    Función principal del sistema democrático
    """
    print("🗳️ SISTEMA DE DISTRIBUCIÓN DEMOCRÁTICA DEL PODER")
    print("=" * 60)
    print("Simulación de reparto de poder político usando Algoritmos Genéticos")
    print("=" * 60)
    
    # Crear sistema
    sistema = SistemaDemocraticoAG(semilla=42)
    
    # Mostrar configuración inicial
    sistema.mostrar_congreso()
    sistema.mostrar_entidades()
    
    # Ejecutar algoritmo genético
    historia_fitness = sistema.algoritmo_genetico()
    
    # Analizar resultados
    sistema.analizar_distribucion()
    
    # Visualizar resultados
    sistema.visualizar_resultados(historia_fitness)
    
    print(f"\n🎯 CONCLUSIÓN:")
    print(f"El algoritmo genético ha optimizado la distribución del poder")
    print(f"buscando la mayor proporcionalidad posible entre la representación")
    print(f"parlamentaria y el poder ejecutivo asignado a cada partido.")

if __name__ == "__main__":
    main()
