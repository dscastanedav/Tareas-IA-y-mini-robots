# -*- coding: utf-8 -*-
"""
Robot Entregador de Galletas usando Programación Genética
=========================================================

Utiliza Programación Genética para evolucionar el comportamiento de un robot
que debe entregar galletas a ingenieros distribuidos en una sala cuadrada,
maximizando los puntos obtenidos por entregas exitosas.

Escenario:
- Sala cuadrada 10x10
- Robot inicia en posición (0,0)
- Ingenieros distribuidos aleatoriamente
- Objetivo: Maximizar entregas de galletas

Autor: Estudiante IA
Fecha: Julio 2025
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict

class NodoComportamiento:
    """Representa un nodo en el árbol de comportamiento del robot"""
    
    def __init__(self, valor, es_terminal=False, hijos=None):
        self.valor = valor
        self.es_terminal = es_terminal
        self.hijos = hijos if hijos else []
    
    def ejecutar(self, estado_robot):
        """Ejecuta el comportamiento representado por este nodo"""
        if self.es_terminal:
            return self.valor  # Acción primitiva
        
        # Es una función de control
        if self.valor == 'SI':
            # Si condición es verdadera, ejecutar primer hijo, sino segundo
            condicion = self.hijos[0].ejecutar(estado_robot)
            if condicion:
                return self.hijos[1].ejecutar(estado_robot)
            else:
                return self.hijos[2].ejecutar(estado_robot)
        
        elif self.valor == 'SECUENCIA':
            # Ejecutar hijos en secuencia
            for hijo in self.hijos:
                resultado = hijo.ejecutar(estado_robot)
                if resultado is not None:
                    return resultado
            return None
        
        elif self.valor == 'REPETIR':
            # Repetir primer hijo N veces (N del segundo hijo)
            accion = self.hijos[0]
            veces = min(3, abs(hash(str(self.hijos[1])) % 4) + 1)  # 1-3 repeticiones
            for _ in range(veces):
                resultado = accion.ejecutar(estado_robot)
                if resultado:
                    return resultado
            return None
        
        return None
    
    def copiar(self):
        """Crea una copia profunda del nodo"""
        nuevos_hijos = [hijo.copiar() for hijo in self.hijos]
        return NodoComportamiento(self.valor, self.es_terminal, nuevos_hijos)
    
    def tamaño(self):
        """Calcula el tamaño del árbol"""
        if self.es_terminal:
            return 1
        return 1 + sum(hijo.tamaño() for hijo in self.hijos)

class RobotGalletas:
    """
    Sistema de Programación Genética para robot entregador de galletas
    """
    
    def __init__(self):
        """Inicializa el sistema"""
        
        # Tamaño de la sala
        self.tamaño_sala = 10
        
        # Conjunto de terminales (acciones y sensores)
        self.terminales = [
            'MOVER_NORTE', 'MOVER_SUR', 'MOVER_ESTE', 'MOVER_OESTE',
            'ENTREGAR_GALLETA', 'BUSCAR_INGENIERO', 'PARAR',
            'HAY_INGENIERO_CERCA', 'HAY_PARED_NORTE', 'HAY_PARED_SUR', 
            'HAY_PARED_ESTE', 'HAY_PARED_OESTE', 'TENGO_GALLETAS'
        ]
        
        # Conjunto de funciones de control
        self.funciones = {
            'SI': 3,        # Condicional: condición, then, else
            'SECUENCIA': 2, # Ejecutar en secuencia
            'REPETIR': 2    # Repetir N veces
        }
        
        # Parámetros de simulación
        self.num_ingenieros = 8
        self.galletas_iniciales = 10
        self.pasos_maximos = 50
        
        # Parámetros PG
        self.tamaño_poblacion = 40
        self.num_generaciones = 80
        self.tasa_mutacion = 0.2
        self.tasa_cruce = 0.7
        self.profundidad_maxima = 5
        self.elite_size = 5
        
        print("🤖 ROBOT ENTREGADOR DE GALLETAS - PROGRAMACIÓN GENÉTICA")
        print("=" * 60)
        self.mostrar_configuracion()
    
    def mostrar_configuracion(self):
        """Muestra la configuración del problema"""
        print(f"\n📋 CONFIGURACIÓN:")
        print(f"• Sala: {self.tamaño_sala}x{self.tamaño_sala} casillas")
        print(f"• Ingenieros: {self.num_ingenieros}")
        print(f"• Galletas iniciales: {self.galletas_iniciales}")
        print(f"• Pasos máximos: {self.pasos_maximos}")
        
        print(f"\n🎯 TERMINALES (Acciones y Sensores):")
        acciones = [t for t in self.terminales if t.startswith('MOVER_') or t in ['ENTREGAR_GALLETA', 'BUSCAR_INGENIERO', 'PARAR']]
        sensores = [t for t in self.terminales if t.startswith('HAY_') or t == 'TENGO_GALLETAS']
        print(f"  Acciones: {acciones}")
        print(f"  Sensores: {sensores}")
        
        print(f"\n🔧 FUNCIONES DE CONTROL:")
        print(f"  {list(self.funciones.keys())}")
    
    def crear_escenario(self):
        """Crea un escenario aleatorio con ingenieros distribuidos"""
        ingenieros = []
        posiciones_ocupadas = {(0, 0)}  # Robot inicia en (0,0)
        
        for _ in range(self.num_ingenieros):
            while True:
                x = random.randint(1, self.tamaño_sala - 1)
                y = random.randint(1, self.tamaño_sala - 1)
                if (x, y) not in posiciones_ocupadas:
                    ingenieros.append((x, y))
                    posiciones_ocupadas.add((x, y))
                    break
        
        return ingenieros
    
    def crear_terminal_aleatorio(self):
        """Crea un nodo terminal aleatorio"""
        valor = random.choice(self.terminales)
        return NodoComportamiento(valor, es_terminal=True)
    
    def crear_funcion_aleatoria(self, profundidad_actual, profundidad_max):
        """Crea un nodo función aleatorio"""
        if profundidad_actual >= profundidad_max:
            return self.crear_terminal_aleatorio()
        
        funcion = random.choice(list(self.funciones.keys()))
        num_args = self.funciones[funcion]
        
        hijos = []
        for _ in range(num_args):
            if random.random() < 0.6 and profundidad_actual < profundidad_max - 1:
                hijo = self.crear_funcion_aleatoria(profundidad_actual + 1, profundidad_max)
            else:
                hijo = self.crear_terminal_aleatorio()
            hijos.append(hijo)
        
        return NodoComportamiento(funcion, es_terminal=False, hijos=hijos)
    
    def crear_individuo(self):
        """Crea un individuo (árbol de comportamiento)"""
        return self.crear_funcion_aleatoria(0, self.profundidad_maxima)
    
    def simular_robot(self, arbol_comportamiento, ingenieros, visualizar=False):
        """Simula el comportamiento del robot con el árbol dado"""
        # Estado inicial del robot
        estado = {
            'x': 0, 'y': 0,
            'galletas': self.galletas_iniciales,
            'puntos': 0,
            'ingenieros_restantes': set(ingenieros),
            'pasos': 0
        }
        
        trayectoria = [(0, 0)]
        entregas = []
        
        for paso in range(self.pasos_maximos):
            estado['pasos'] = paso
            
            # Ejecutar comportamiento
            accion = self.ejecutar_comportamiento(arbol_comportamiento, estado)
            
            if accion == 'PARAR':
                break
            
            # Procesar acción
            if accion == 'MOVER_NORTE' and estado['y'] < self.tamaño_sala - 1:
                estado['y'] += 1
            elif accion == 'MOVER_SUR' and estado['y'] > 0:
                estado['y'] -= 1
            elif accion == 'MOVER_ESTE' and estado['x'] < self.tamaño_sala - 1:
                estado['x'] += 1
            elif accion == 'MOVER_OESTE' and estado['x'] > 0:
                estado['x'] -= 1
            elif accion == 'ENTREGAR_GALLETA':
                pos_actual = (estado['x'], estado['y'])
                if pos_actual in estado['ingenieros_restantes'] and estado['galletas'] > 0:
                    estado['galletas'] -= 1
                    estado['puntos'] += 10  # 10 puntos por entrega
                    estado['ingenieros_restantes'].remove(pos_actual)
                    entregas.append(pos_actual)
            elif accion == 'BUSCAR_INGENIERO':
                # Moverse hacia el ingeniero más cercano
                if estado['ingenieros_restantes']:
                    ingeniero_cercano = min(estado['ingenieros_restantes'],
                                          key=lambda ing: abs(ing[0] - estado['x']) + abs(ing[1] - estado['y']))
                    
                    if ingeniero_cercano[0] > estado['x'] and estado['x'] < self.tamaño_sala - 1:
                        estado['x'] += 1
                    elif ingeniero_cercano[0] < estado['x'] and estado['x'] > 0:
                        estado['x'] -= 1
                    elif ingeniero_cercano[1] > estado['y'] and estado['y'] < self.tamaño_sala - 1:
                        estado['y'] += 1
                    elif ingeniero_cercano[1] < estado['y'] and estado['y'] > 0:
                        estado['y'] -= 1
            
            trayectoria.append((estado['x'], estado['y']))
            
            # Terminar si se entregaron todas las galletas o no quedan ingenieros
            if estado['galletas'] == 0 or len(estado['ingenieros_restantes']) == 0:
                break
        
        # Bonificación por eficiencia
        entregas_realizadas = len(entregas)
        pasos_usados = len(trayectoria) - 1
        
        # Penalizar por pasos excesivos
        if pasos_usados > 0:
            eficiencia = entregas_realizadas / pasos_usados
            estado['puntos'] += int(eficiencia * 5)  # Bonus por eficiencia
        
        return estado['puntos'], entregas_realizadas, trayectoria, entregas
    
    def ejecutar_comportamiento(self, nodo, estado):
        """Ejecuta un nodo de comportamiento y retorna una acción"""
        if nodo.es_terminal:
            # Evaluar sensores
            if nodo.valor == 'HAY_INGENIERO_CERCA':
                pos_actual = (estado['x'], estado['y'])
                return any(abs(ing[0] - pos_actual[0]) + abs(ing[1] - pos_actual[1]) <= 1 
                          for ing in estado['ingenieros_restantes'])
            elif nodo.valor == 'HAY_PARED_NORTE':
                return estado['y'] >= self.tamaño_sala - 1
            elif nodo.valor == 'HAY_PARED_SUR':
                return estado['y'] <= 0
            elif nodo.valor == 'HAY_PARED_ESTE':
                return estado['x'] >= self.tamaño_sala - 1
            elif nodo.valor == 'HAY_PARED_OESTE':
                return estado['x'] <= 0
            elif nodo.valor == 'TENGO_GALLETAS':
                return estado['galletas'] > 0
            else:
                return nodo.valor  # Acción de movimiento
        
        # Función de control
        if nodo.valor == 'SI':
            condicion = self.ejecutar_comportamiento(nodo.hijos[0], estado)
            if condicion:
                return self.ejecutar_comportamiento(nodo.hijos[1], estado)
            else:
                return self.ejecutar_comportamiento(nodo.hijos[2], estado)
        
        elif nodo.valor == 'SECUENCIA':
            # Ejecutar primer hijo que retorne una acción válida
            for hijo in nodo.hijos:
                resultado = self.ejecutar_comportamiento(hijo, estado)
                if isinstance(resultado, str) and resultado.startswith(('MOVER_', 'ENTREGAR_', 'BUSCAR_', 'PARAR')):
                    return resultado
        
        elif nodo.valor == 'REPETIR':
            return self.ejecutar_comportamiento(nodo.hijos[0], estado)
        
        return 'PARAR'  # Acción por defecto
    
    def evaluar_individuo(self, individuo):
        """Evalúa un individuo en múltiples escenarios"""
        puntos_total = 0
        entregas_total = 0
        
        # Probar en 3 escenarios diferentes
        for _ in range(3):
            ingenieros = self.crear_escenario()
            puntos, entregas, _, _ = self.simular_robot(individuo, ingenieros)
            puntos_total += puntos
            entregas_total += entregas
        
        # Fitness promedio
        fitness_base = puntos_total / 3
        
        # Penalizar árboles muy grandes
        tamaño = individuo.tamaño()
        penalty = min(5, tamaño / 20)  # Penalidad máxima de 5 puntos
        
        return max(0, fitness_base - penalty)
    
    def seleccion_torneo(self, poblacion, fitness_scores, tamaño_torneo=3):
        """Selección por torneo"""
        participantes = random.sample(list(zip(poblacion, fitness_scores)), tamaño_torneo)
        ganador = max(participantes, key=lambda x: x[1])
        return ganador[0].copiar()
    
    def cruzamiento(self, padre1, padre2):
        """Cruzamiento por intercambio de subárboles"""
        if random.random() > self.tasa_cruce:
            return padre1.copiar(), padre2.copiar()
        
        hijo1 = padre1.copiar()
        hijo2 = padre2.copiar()
        
        # Intercambio simple en un punto aleatorio
        if random.random() < 0.5 and len(hijo1.hijos) > 0 and len(hijo2.hijos) > 0:
            idx1 = random.randint(0, len(hijo1.hijos) - 1)
            idx2 = random.randint(0, len(hijo2.hijos) - 1)
            hijo1.hijos[idx1], hijo2.hijos[idx2] = hijo2.hijos[idx2], hijo1.hijos[idx1]
        
        return hijo1, hijo2
    
    def mutar_arbol(self, arbol, probabilidad=0.1):
        """Muta un árbol de comportamiento"""
        if random.random() < probabilidad:
            # Reemplazar con nuevo subárbol
            return self.crear_funcion_aleatoria(0, 3)
        
        if not arbol.es_terminal:
            arbol.hijos = [self.mutar_arbol(hijo, probabilidad/2) for hijo in arbol.hijos]
        
        return arbol
    
    def mutacion(self, individuo):
        """Mutación de un individuo"""
        return self.mutar_arbol(individuo.copiar(), self.tasa_mutacion)
    
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
                mejor_individuo = poblacion[np.argmax(fitness_scores)].copiar()
            
            # Mostrar progreso
            if generacion % 20 == 0 or generacion == self.num_generaciones - 1:
                print(f"Gen {generacion:3d}: Mejor = {mejor_fitness:.1f} puntos, "
                      f"Promedio = {fitness_promedio:.1f}")
            
            # Crear nueva población
            nueva_poblacion = []
            
            # Elitismo
            indices_elite = np.argsort(fitness_scores)[-self.elite_size:]
            for i in indices_elite:
                nueva_poblacion.append(poblacion[i].copiar())
            
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
        print(f"Mejor fitness: {mejor_fitness_global:.1f} puntos")
        
        return mejor_individuo, mejor_fitness_historia, fitness_promedio_historia
    
    def analizar_solucion(self, individuo):
        """Analiza la mejor solución encontrada"""
        print(f"\n📊 ANÁLISIS DE LA MEJOR SOLUCIÓN")
        print("=" * 50)
        
        # Crear escenario de prueba
        ingenieros = self.crear_escenario()
        print(f"🎯 Escenario de prueba:")
        print(f"Ingenieros en: {ingenieros}")
        
        # Simular comportamiento
        puntos, entregas, trayectoria, posiciones_entrega = self.simular_robot(
            individuo, ingenieros, visualizar=True)
        
        print(f"\n📈 RESULTADOS:")
        print(f"• Puntos obtenidos: {puntos}")
        print(f"• Entregas realizadas: {entregas}/{self.num_ingenieros}")
        print(f"• Pasos utilizados: {len(trayectoria)-1}/{self.pasos_maximos}")
        print(f"• Eficiencia: {entregas/(len(trayectoria)-1)*100:.1f}% (entregas/paso)")
        
        if posiciones_entrega:
            print(f"• Entregas en: {posiciones_entrega}")
        
        return trayectoria, ingenieros, posiciones_entrega
    
    def visualizar_resultados(self, historia_fitness, trayectoria=None, ingenieros=None, entregas=None):
        """Visualiza los resultados"""
        if trayectoria:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        else:
            fig, ax1 = plt.subplots(1, 1, figsize=(10, 6))
        
        # 1. Evolución del fitness
        mejor_fitness, fitness_promedio = historia_fitness
        generations = range(len(mejor_fitness))
        
        ax1.plot(generations, mejor_fitness, 'b-', linewidth=2, label='Mejor fitness')
        ax1.plot(generations, fitness_promedio, 'r--', linewidth=1, label='Fitness promedio')
        ax1.set_xlabel('Generación')
        ax1.set_ylabel('Fitness (puntos)')
        ax1.set_title('Evolución de la Programación Genética', fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Visualización del recorrido del robot
        if trayectoria and ingenieros:
            # Crear mapa de la sala
            mapa = np.zeros((self.tamaño_sala, self.tamaño_sala))
            
            # Marcar ingenieros
            for ing in ingenieros:
                mapa[ing[1], ing[0]] = 1  # Ingeniero sin atender
            
            # Marcar entregas
            if entregas:
                for ent in entregas:
                    mapa[ent[1], ent[0]] = 2  # Ingeniero atendido
            
            im = ax2.imshow(mapa, cmap='RdYlGn', origin='lower', alpha=0.7)
            
            # Dibujar trayectoria
            traj_x = [pos[0] for pos in trayectoria]
            traj_y = [pos[1] for pos in trayectoria]
            ax2.plot(traj_x, traj_y, 'b-', linewidth=2, alpha=0.8, label='Trayectoria')
            ax2.plot(traj_x[0], traj_y[0], 'go', markersize=10, label='Inicio')
            ax2.plot(traj_x[-1], traj_y[-1], 'ro', markersize=10, label='Fin')
            
            # Marcar entregas
            if entregas:
                ent_x = [pos[0] for pos in entregas]
                ent_y = [pos[1] for pos in entregas]
                ax2.scatter(ent_x, ent_y, c='gold', s=200, marker='*', 
                           edgecolors='black', label='Entregas', zorder=5)
            
            ax2.set_xlim(-0.5, self.tamaño_sala-0.5)
            ax2.set_ylim(-0.5, self.tamaño_sala-0.5)
            ax2.set_xlabel('X')
            ax2.set_ylabel('Y')
            ax2.set_title('Recorrido del Robot en la Sala', fontweight='bold')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            
            # Agregar información de colores
            ax2.text(0.02, 0.98, 'Rojo: Ingeniero sin atender\nVerde: Ingeniero atendido', 
                    transform=ax2.transAxes, verticalalignment='top',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
        
        plt.tight_layout()
        plt.savefig('c:/Users/santi/OneDrive/Documentos/Tareas IA y mini robots/4/4.3/resultados_robot_galletas.png',
                   dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """Función principal"""
    print("🤖 ROBOT ENTREGADOR DE GALLETAS")
    print("=" * 50)
    print("Programación Genética para Comportamiento de Robot")
    print("=" * 50)
    
    # Crear sistema
    sistema = RobotGalletas()
    
    # Ejecutar programación genética
    mejor_solucion, mejor_fitness_historia, fitness_promedio_historia = sistema.programacion_genetica()
    
    # Analizar resultados
    trayectoria, ingenieros, entregas = None, None, None
    if mejor_solucion:
        trayectoria, ingenieros, entregas = sistema.analizar_solucion(mejor_solucion)
    
    # Visualizar resultados
    sistema.visualizar_resultados((mejor_fitness_historia, fitness_promedio_historia), 
                                 trayectoria, ingenieros, entregas)
    
    print(f"\n🎯 CONCLUSIÓN:")
    print(f"La Programación Genética evolucionó un comportamiento")
    print(f"para que el robot entregue galletas de manera eficiente.")

if __name__ == "__main__":
    main()
