#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diseño de Circuito Codificador de 7 Segmentos usando Programación Genética
==========================================================================

Utiliza Programación Genética para evolucionar expresiones lógicas que
implementen un codificador de 7 segmentos (BCD a 7 segmentos).

Entrada: 4 bits BCD (A, B, C, D) - números 0-9
Salida: 7 bits para segmentos (a, b, c, d, e, f, g)

Autor: Estudiante IA
Fecha: Julio 2025
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Any

class NodoGenetico:
    """Representa un nodo en el árbol de expresión lógica"""
    
    def __init__(self, valor, es_terminal=False, hijos=None):
        self.valor = valor
        self.es_terminal = es_terminal
        self.hijos = hijos if hijos else []
    
    def evaluar(self, entradas: Dict[str, bool]) -> bool:
        """Evalúa el nodo con las entradas dadas"""
        if self.es_terminal:
            if self.valor in entradas:
                return entradas[self.valor]
            else:
                return self.valor  # Constante booleana
        
        # Es una función
        if self.valor == 'AND':
            return all(hijo.evaluar(entradas) for hijo in self.hijos)
        elif self.valor == 'OR':
            return any(hijo.evaluar(entradas) for hijo in self.hijos)
        elif self.valor == 'NOT':
            return not self.hijos[0].evaluar(entradas)
        elif self.valor == 'XOR':
            return sum(hijo.evaluar(entradas) for hijo in self.hijos) % 2 == 1
        
        return False
    
    def copiar(self):
        """Crea una copia profunda del nodo"""
        nuevos_hijos = [hijo.copiar() for hijo in self.hijos]
        return NodoGenetico(self.valor, self.es_terminal, nuevos_hijos)
    
    def tamaño(self) -> int:
        """Calcula el tamaño del árbol"""
        if self.es_terminal:
            return 1
        return 1 + sum(hijo.tamaño() for hijo in self.hijos)
    
    def __str__(self):
        if self.es_terminal:
            return str(self.valor)
        
        if self.valor == 'NOT':
            return f"NOT({self.hijos[0]})"
        else:
            hijos_str = ', '.join(str(hijo) for hijo in self.hijos)
            return f"{self.valor}({hijos_str})"

class CodificadorSieteSegmentos:
    """
    Sistema de Programación Genética para diseñar codificador de 7 segmentos
    """
    
    def __init__(self):
        """Inicializa el sistema"""
        
        # Conjunto de terminales (entradas BCD)
        self.terminales = ['A', 'B', 'C', 'D', True, False]
        
        # Conjunto de funciones lógicas
        self.funciones = {
            'AND': 2,   # 2 argumentos
            'OR': 2,    # 2 argumentos  
            'NOT': 1,   # 1 argumento
            'XOR': 2    # 2 argumentos
        }
        
        # Tabla de verdad para codificador de 7 segmentos
        # Segmentos: a, b, c, d, e, f, g
        #     a
        #   f   b
        #     g
        #   e   c
        #     d
        self.tabla_verdad = {
            0: [1, 1, 1, 1, 1, 1, 0],  # 0
            1: [0, 1, 1, 0, 0, 0, 0],  # 1
            2: [1, 1, 0, 1, 1, 0, 1],  # 2
            3: [1, 1, 1, 1, 0, 0, 1],  # 3
            4: [0, 1, 1, 0, 0, 1, 1],  # 4
            5: [1, 0, 1, 1, 0, 1, 1],  # 5
            6: [1, 0, 1, 1, 1, 1, 1],  # 6
            7: [1, 1, 1, 0, 0, 0, 0],  # 7
            8: [1, 1, 1, 1, 1, 1, 1],  # 8
            9: [1, 1, 1, 1, 0, 1, 1]   # 9
        }
        
        # Parámetros de la Programación Genética
        self.tamaño_poblacion = 50
        self.num_generaciones = 100
        self.tasa_mutacion = 0.15
        self.tasa_cruce = 0.8
        self.profundidad_maxima = 6
        self.elite_size = 5
        
        # Nombres de los segmentos
        self.nombres_segmentos = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        
        print("🔢 CODIFICADOR DE 7 SEGMENTOS - PROGRAMACIÓN GENÉTICA")
        print("=" * 60)
        self.mostrar_configuracion()
    
    def mostrar_configuracion(self):
        """Muestra la configuración del problema"""
        print("\n📋 CONFIGURACIÓN DEL PROBLEMA:")
        print(f"• Terminales: {self.terminales}")
        print(f"• Funciones: {list(self.funciones.keys())}")
        print(f"• Entradas: 4 bits BCD (A, B, C, D)")
        print(f"• Salidas: 7 segmentos (a, b, c, d, e, f, g)")
        
        print("\n🎯 TABLA DE VERDAD (muestra):")
        print("BCD | a b c d e f g | Dígito")
        print("----|---------------|-------")
        for i in range(3):  # Mostrar solo primeros 3 para brevedad
            bits = format(i, '04b')
            segmentos = ' '.join(str(x) for x in self.tabla_verdad[i])
            print(f"{bits} | {segmentos} |   {i}")
        print("... (continúa hasta 9)")
    
    def crear_terminal_aleatorio(self):
        """Crea un nodo terminal aleatorio"""
        valor = random.choice(self.terminales)
        return NodoGenetico(valor, es_terminal=True)
    
    def crear_funcion_aleatoria(self, profundidad_actual, profundidad_max):
        """Crea un nodo función aleatorio con sus hijos"""
        if profundidad_actual >= profundidad_max:
            return self.crear_terminal_aleatorio()
        
        funcion = random.choice(list(self.funciones.keys()))
        num_args = self.funciones[funcion]
        
        hijos = []
        for _ in range(num_args):
            # 50% probabilidad de crear función u hoja
            if random.random() < 0.5 and profundidad_actual < profundidad_max - 1:
                hijo = self.crear_funcion_aleatoria(profundidad_actual + 1, profundidad_max)
            else:
                hijo = self.crear_terminal_aleatorio()
            hijos.append(hijo)
        
        return NodoGenetico(funcion, es_terminal=False, hijos=hijos)
    
    def crear_individuo(self):
        """Crea un individuo (7 árboles, uno por segmento)"""
        individuo = []
        for _ in range(7):  # 7 segmentos
            arbol = self.crear_funcion_aleatoria(0, self.profundidad_maxima)
            individuo.append(arbol)
        return individuo
    
    def evaluar_individuo(self, individuo):
        """Evalúa qué tan bien funciona un individuo"""
        aciertos_totales = 0
        total_posible = 10 * 7  # 10 dígitos × 7 segmentos
        
        for digito in range(10):
            # Convertir dígito a BCD
            bcd = format(digito, '04b')
            entradas = {'A': bcd[0] == '1', 'B': bcd[1] == '1', 
                       'C': bcd[2] == '1', 'D': bcd[3] == '1'}
            
            # Evaluar cada segmento
            for i, arbol_segmento in enumerate(individuo):
                try:
                    resultado = arbol_segmento.evaluar(entradas)
                    esperado = self.tabla_verdad[digito][i] == 1
                    
                    if resultado == esperado:
                        aciertos_totales += 1
                except:
                    # Error en evaluación, penalizar
                    pass
        
        # Fitness = porcentaje de aciertos
        fitness = aciertos_totales / total_posible
        
        # Penalizar árboles muy grandes (parsimonia)
        tamaño_total = sum(arbol.tamaño() for arbol in individuo)
        penalty = min(0.1, tamaño_total / 1000)  # Penalidad máxima 10%
        
        return max(0, fitness - penalty)
    
    def seleccion_torneo(self, poblacion, fitness_scores, tamaño_torneo=3):
        """Selección por torneo"""
        participantes = random.sample(list(zip(poblacion, fitness_scores)), tamaño_torneo)
        ganador = max(participantes, key=lambda x: x[1])
        return [arbol.copiar() for arbol in ganador[0]]
    
    def cruzamiento(self, padre1, padre2):
        """Cruzamiento entre dos individuos"""
        if random.random() > self.tasa_cruce:
            return ([arbol.copiar() for arbol in padre1], 
                   [arbol.copiar() for arbol in padre2])
        
        hijo1 = [arbol.copiar() for arbol in padre1]
        hijo2 = [arbol.copiar() for arbol in padre2]
        
        # Intercambiar algunos árboles al azar
        for i in range(7):
            if random.random() < 0.3:  # 30% probabilidad por segmento
                hijo1[i], hijo2[i] = hijo2[i], hijo1[i]
        
        return hijo1, hijo2
    
    def mutar_arbol(self, arbol, probabilidad=0.1):
        """Muta un árbol de expresión"""
        if random.random() < probabilidad:
            # Reemplazar con nuevo árbol pequeño
            return self.crear_funcion_aleatoria(0, 3)
        
        if not arbol.es_terminal:
            # Mutar hijos recursivamente
            arbol.hijos = [self.mutar_arbol(hijo, probabilidad/2) for hijo in arbol.hijos]
        
        return arbol
    
    def mutacion(self, individuo):
        """Mutación de un individuo"""
        individuo_mutado = []
        for arbol in individuo:
            arbol_mutado = self.mutar_arbol(arbol.copiar(), self.tasa_mutacion)
            individuo_mutado.append(arbol_mutado)
        return individuo_mutado
    
    def programacion_genetica(self):
        """Ejecuta la Programación Genética"""
        print(f"\n🧬 EJECUTANDO PROGRAMACIÓN GENÉTICA")
        print("=" * 45)
        print(f"Población: {self.tamaño_poblacion}, Generaciones: {self.num_generaciones}")
        
        # Crear población inicial
        poblacion = [self.crear_individuo() for _ in range(self.tamaño_poblacion)]
        
        mejor_fitness_historia = []
        fitness_promedio_historia = []
        mejor_individuo = None
        mejor_fitness_global = 0
        
        for generacion in range(self.num_generaciones):
            # Evaluar fitness
            fitness_scores = [self.evaluar_individuo(individuo) for individuo in poblacion]
            
            # Estadísticas
            mejor_fitness = max(fitness_scores)
            fitness_promedio = np.mean(fitness_scores)
            
            mejor_fitness_historia.append(mejor_fitness)
            fitness_promedio_historia.append(fitness_promedio)
            
            # Actualizar mejor solución
            if mejor_fitness > mejor_fitness_global:
                mejor_fitness_global = mejor_fitness
                mejor_individuo = [arbol.copiar() for arbol in poblacion[np.argmax(fitness_scores)]]
            
            # Mostrar progreso
            if generacion % 20 == 0 or generacion == self.num_generaciones - 1:
                print(f"Gen {generacion:3d}: Mejor = {mejor_fitness:.4f} ({mejor_fitness*100:.1f}%), "
                      f"Promedio = {fitness_promedio:.4f}")
            
            # Si encontramos solución perfecta, terminar
            if mejor_fitness >= 0.99:
                print(f"¡Solución perfecta encontrada en generación {generacion}!")
                break
            
            # Crear nueva población
            nueva_poblacion = []
            
            # Elitismo
            indices_elite = np.argsort(fitness_scores)[-self.elite_size:]
            for i in indices_elite:
                nueva_poblacion.append([arbol.copiar() for arbol in poblacion[i]])
            
            # Generar resto de la población
            while len(nueva_poblacion) < self.tamaño_poblacion:
                padre1 = self.seleccion_torneo(poblacion, fitness_scores)
                padre2 = self.seleccion_torneo(poblacion, fitness_scores)
                
                hijo1, hijo2 = self.cruzamiento(padre1, padre2)
                
                hijo1 = self.mutacion(hijo1)
                hijo2 = self.mutacion(hijo2)
                
                nueva_poblacion.extend([hijo1, hijo2])
            
            poblacion = nueva_poblacion[:self.tamaño_poblacion]
        
        print(f"\n✅ Evolución completada!")
        print(f"Mejor fitness: {mejor_fitness_global:.4f} ({mejor_fitness_global*100:.1f}%)")
        
        return mejor_individuo, mejor_fitness_historia, fitness_promedio_historia
    
    def analizar_solucion(self, individuo):
        """Analiza la mejor solución encontrada"""
        print(f"\n📊 ANÁLISIS DE LA MEJOR SOLUCIÓN")
        print("=" * 50)
        
        # Mostrar expresiones para cada segmento
        print("\n🔗 EXPRESIONES LÓGICAS POR SEGMENTO:")
        for i, (nombre, arbol) in enumerate(zip(self.nombres_segmentos, individuo)):
            print(f"Segmento {nombre}: {arbol}")
        
        # Probar con todos los dígitos
        print(f"\n✅ VERIFICACIÓN COMPLETA:")
        print("Dígito | A B C D | a b c d e f g | Esperado  | Obtenido  | ✓")
        print("-------|---------|---------------|-----------|-----------|---")
        
        aciertos = 0
        total = 0
        
        for digito in range(10):
            # BCD del dígito
            bcd = format(digito, '04b')
            entradas = {'A': bcd[0] == '1', 'B': bcd[1] == '1', 
                       'C': bcd[2] == '1', 'D': bcd[3] == '1'}
            
            # Evaluar segmentos
            resultado = []
            for arbol in individuo:
                try:
                    valor = arbol.evaluar(entradas)
                    resultado.append(1 if valor else 0)
                except:
                    resultado.append(0)
            
            esperado = self.tabla_verdad[digito]
            coincide = resultado == esperado
            
            resultado_str = ' '.join(str(x) for x in resultado)
            esperado_str = ' '.join(str(x) for x in esperado)
            check = "✓" if coincide else "✗"
            
            print(f"  {digito}    | {bcd} | {resultado_str} | {esperado_str} | {resultado_str} | {check}")
            
            if coincide:
                aciertos += 1
            total += 1
        
        print(f"\nPrecisión total: {aciertos}/{total} = {aciertos/total*100:.1f}%")
    
    def visualizar_resultados(self, historia_fitness):
        """Visualiza los resultados"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # 1. Evolución del fitness
        mejor_fitness, fitness_promedio = historia_fitness
        generations = range(len(mejor_fitness))
        
        ax1.plot(generations, mejor_fitness, 'b-', linewidth=2, label='Mejor fitness')
        ax1.plot(generations, fitness_promedio, 'r--', linewidth=1, label='Fitness promedio')
        ax1.set_xlabel('Generación')
        ax1.set_ylabel('Fitness')
        ax1.set_title('Evolución de la Programación Genética', fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1)
        
        # 2. Visualización del display de 7 segmentos
        # Crear una representación visual simple
        def dibujar_digito(ax, digito, segmentos):
            """Dibuja un dígito en el display de 7 segmentos"""
            ax.set_xlim(0, 3)
            ax.set_ylim(0, 4)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Posiciones de los segmentos
            segs = {
                'a': [(0.5, 3.5), (2.5, 3.5)],      # horizontal superior
                'b': [(2.5, 3.5), (2.5, 2)],        # vertical derecha superior
                'c': [(2.5, 2), (2.5, 0.5)],        # vertical derecha inferior
                'd': [(0.5, 0.5), (2.5, 0.5)],      # horizontal inferior
                'e': [(0.5, 0.5), (0.5, 2)],        # vertical izquierda inferior
                'f': [(0.5, 2), (0.5, 3.5)],        # vertical izquierda superior
                'g': [(0.5, 2), (2.5, 2)]           # horizontal medio
            }
            
            # Dibujar segmentos
            for i, (nombre, coords) in enumerate(segs.items()):
                if segmentos[i]:
                    ax.plot([coords[0][0], coords[1][0]], 
                           [coords[0][1], coords[1][1]], 
                           'red', linewidth=8)
                else:
                    ax.plot([coords[0][0], coords[1][0]], 
                           [coords[0][1], coords[1][1]], 
                           'lightgray', linewidth=2)
            
            ax.set_title(f'Dígito {digito}', fontsize=12, fontweight='bold')
        
        # Mostrar algunos dígitos como ejemplo
        ax2.text(0.5, 0.5, 'Visualización del Display de 7 Segmentos\n\n'
                           'Los segmentos evolucionados pueden mostrar\n'
                           'los dígitos 0-9 en formato de 7 segmentos.\n\n'
                           'Cada segmento tiene su propia expresión\n'
                           'lógica optimizada por la PG.', 
                 ha='center', va='center', fontsize=12,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.5))
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.axis('off')
        ax2.set_title('Conceptual: Display de 7 Segmentos', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('c:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/4/4.2/resultados_codificador.png',
                   dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """Función principal"""
    print("🔢 DISEÑO DE CIRCUITO CODIFICADOR DE 7 SEGMENTOS")
    print("=" * 60)
    print("Programación Genética para Circuitos Lógicos")
    print("=" * 60)
    
    # Crear sistema
    sistema = CodificadorSieteSegmentos()
    
    # Ejecutar programación genética
    mejor_solucion, mejor_fitness_historia, fitness_promedio_historia = sistema.programacion_genetica()
    
    # Analizar resultados
    if mejor_solucion:
        sistema.analizar_solucion(mejor_solucion)
    
    # Visualizar resultados
    sistema.visualizar_resultados((mejor_fitness_historia, fitness_promedio_historia))
    
    print(f"\n🎯 CONCLUSIÓN:")
    print(f"La Programación Genética evolucionó expresiones lógicas")
    print(f"para implementar un codificador de 7 segmentos BCD.")

if __name__ == "__main__":
    main()
