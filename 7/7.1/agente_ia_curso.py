"""
AGENTE DE IA SIMPLE PARA MANEJO DE TAREAS DEL CURSO
===================================================

Este es un agente de IA básico que ayuda a gestionar las tareas del curso.
Funcionalidades:
- Listado de tareas completadas
- Recordatorios de tareas pendientes
- Información sobre proyectos
- Ayuda con conceptos básicos
- Chatbot simple con respuestas predefinidas
"""

import datetime
import json
import re
from typing import Dict, List

class AgenteIACurso:
    """
    Agente de IA simple para manejo de tareas del curso
    
    Un chatbot básico que puede:
    - Responder preguntas sobre tareas
    - Proporcionar información del curso
    - Dar recordatorios
    - Ayudar con conceptos básicos
    """
    
    def __init__(self):
        """
        Inicializa el agente con datos del curso
        """
        self.nombre = "AsistenteIA-Curso"
        self.version = "1.0"
        self.estado = "activo"
        
        # Base de conocimientos del curso
        self.tareas_curso = {
            "6.1": {
                "titulo": "Aproximación de Función Raíz Cuadrada con ML",
                "estado": "completado",
                "descripcion": "Script de ML para aproximar función matemática",
                "archivos": ["sqrt_approximation.py", "requirements.txt", "README.md"],
                "fecha_completado": "2025-07-04"
            },
            "6.2": {
                "titulo": "Estudio Detallado del Algoritmo SVM",
                "estado": "completado", 
                "descripcion": "Estudio completo de SVM con aplicación web",
                "archivos": ["estudio_svm.py", "aplicacion_web_svm.py", "README.md"],
                "fecha_completado": "2025-07-04"
            },
            "6.3": {
                "titulo": "Estudio de Árboles de Decisión",
                "estado": "completado",
                "descripcion": "Análisis completo de árboles de decisión con aplicación",
                "archivos": ["estudio_arboles_decision.py", "aplicacion_web_arboles.py", "README.md"],
                "fecha_completado": "2025-07-04"
            },
            "7.1": {
                "titulo": "Agente de IA para Manejo de Tareas",
                "estado": "en_progreso",
                "descripcion": "Desarrollo de chatbot para gestión del curso",
                "archivos": ["agente_ia_curso.py"],
                "fecha_inicio": "2025-07-05"
            }
        }
        
        # Conceptos del curso
        self.conceptos_ml = {
            "machine learning": "Rama de la IA que permite a las máquinas aprender de datos sin programación explícita",
            "regresión lineal": "Algoritmo que encuentra la línea que mejor se ajusta a los datos",
            "red neuronal": "Modelo inspirado en el cerebro humano con capas de neuronas interconectadas",
            "svm": "Support Vector Machine - Algoritmo que encuentra el hiperplano óptimo para separar clases",
            "árboles de decisión": "Algoritmo que toma decisiones siguiendo un flujo de preguntas",
            "overfitting": "Cuando un modelo memoriza los datos de entrenamiento pero no generaliza bien",
            "precisión": "Porcentaje de predicciones correctas sobre el total",
            "dataset": "Conjunto de datos usado para entrenar modelos de ML"
        }
        
        # Patrones de respuesta
        self.patrones_respuesta = {
            r".*hola.*|.*buenos días.*|.*buenas tardes.*": [
                "¡Hola! Soy tu asistente de IA para el curso. ¿En qué puedo ayudarte?",
                "¡Hola! ¿Necesitas ayuda con alguna tarea del curso?",
                "¡Saludos! Estoy aquí para ayudarte con el curso de IA."
            ],
            r".*qué puedes hacer.*|.*ayuda.*|.*help.*": [
                "Puedo ayudarte con:\n- Ver tareas completadas\n- Recordatorios pendientes\n- Explicar conceptos de ML\n- Información del curso"
            ],
            r".*tareas.*completadas.*|.*progreso.*": [
                "Te muestro el progreso del curso..."
            ],
            r".*pendientes.*|.*que falta.*": [
                "Verificando tareas pendientes..."
            ],
            r".*explica.*|.*qué es.*": [
                "¿Sobre qué concepto necesitas información?"
            ],
            r".*gracias.*|.*thank you.*": [
                "¡De nada! Estoy aquí para ayudarte cuando lo necesites.",
                "¡Un placer ayudarte! ¿Algo más en lo que pueda asistirte?"
            ],
            r".*adiós.*|.*bye.*|.*hasta luego.*": [
                "¡Hasta luego! Que tengas éxito con tus estudios de IA.",
                "¡Nos vemos! Cualquier duda que tengas, estaré aquí."
            ]
        }
    
    def procesar_consulta(self, consulta: str) -> str:
        """
        Procesa una consulta del usuario y retorna una respuesta
        """
        consulta = consulta.lower().strip()
        
        # Verificar patrones específicos
        for patron, respuestas in self.patrones_respuesta.items():
            if re.search(patron, consulta):
                if "tareas.*completadas" in patron or "progreso" in patron:
                    return self.mostrar_progreso()
                elif "pendientes" in patron or "que falta" in patron:
                    return self.mostrar_pendientes()
                elif "explica" in patron or "qué es" in patron:
                    return self.explicar_concepto(consulta)
                else:
                    return respuestas[0] if len(respuestas) == 1 else respuestas[0]
        
        # Buscar conceptos específicos
        for concepto, definicion in self.conceptos_ml.items():
            if concepto in consulta:
                return f"📚 {concepto.title()}:\n{definicion}"
        
        # Buscar tareas específicas
        for codigo, tarea in self.tareas_curso.items():
            if codigo in consulta or tarea["titulo"].lower() in consulta:
                return self.info_tarea(codigo)
        
        # Respuesta por defecto
        return self.respuesta_default()
    
    def mostrar_progreso(self) -> str:
        """
        Muestra el progreso del curso
        """
        completadas = sum(1 for t in self.tareas_curso.values() if t["estado"] == "completado")
        total = len(self.tareas_curso)
        porcentaje = (completadas / total) * 100
        
        respuesta = f"📊 PROGRESO DEL CURSO\n{'='*30}\n"
        respuesta += f"Tareas completadas: {completadas}/{total} ({porcentaje:.1f}%)\n\n"
        
        for codigo, tarea in self.tareas_curso.items():
            estado_emoji = "✅" if tarea["estado"] == "completado" else "🔄" if tarea["estado"] == "en_progreso" else "⏳"
            respuesta += f"{estado_emoji} {codigo}: {tarea['titulo']}\n"
        
        return respuesta
    
    def mostrar_pendientes(self) -> str:
        """
        Muestra las tareas pendientes
        """
        pendientes = [codigo for codigo, tarea in self.tareas_curso.items() 
                     if tarea["estado"] != "completado"]
        
        if not pendientes:
            return "🎉 ¡Excelente! No tienes tareas pendientes en este momento."
        
        respuesta = "📋 TAREAS PENDIENTES\n" + "="*25 + "\n"
        for codigo in pendientes:
            tarea = self.tareas_curso[codigo]
            estado_emoji = "🔄" if tarea["estado"] == "en_progreso" else "⏳"
            respuesta += f"{estado_emoji} {codigo}: {tarea['titulo']}\n"
            respuesta += f"   📝 {tarea['descripcion']}\n\n"
        
        return respuesta
    
    def info_tarea(self, codigo: str) -> str:
        """
        Proporciona información detallada de una tarea
        """
        if codigo not in self.tareas_curso:
            return f"❌ No encontré información sobre la tarea {codigo}"
        
        tarea = self.tareas_curso[codigo]
        estado_emoji = "✅" if tarea["estado"] == "completado" else "🔄" if tarea["estado"] == "en_progreso" else "⏳"
        
        respuesta = f"📁 INFORMACIÓN DE TAREA {codigo}\n{'='*35}\n"
        respuesta += f"{estado_emoji} {tarea['titulo']}\n"
        respuesta += f"📝 Descripción: {tarea['descripcion']}\n"
        respuesta += f"📊 Estado: {tarea['estado']}\n"
        
        if "fecha_completado" in tarea:
            respuesta += f"📅 Completado: {tarea['fecha_completado']}\n"
        if "fecha_inicio" in tarea:
            respuesta += f"📅 Iniciado: {tarea['fecha_inicio']}\n"
        
        respuesta += f"📄 Archivos: {', '.join(tarea['archivos'])}\n"
        
        return respuesta
    
    def explicar_concepto(self, consulta: str) -> str:
        """
        Explica conceptos de ML mencionados en la consulta
        """
        conceptos_encontrados = []
        for concepto in self.conceptos_ml.keys():
            if concepto in consulta:
                conceptos_encontrados.append(concepto)
        
        if conceptos_encontrados:
            respuesta = "📚 CONCEPTOS ENCONTRADOS\n" + "="*30 + "\n"
            for concepto in conceptos_encontrados:
                respuesta += f"• {concepto.title()}: {self.conceptos_ml[concepto]}\n\n"
            return respuesta
        else:
            return "🤔 No encontré conceptos específicos en tu consulta. ¿Podrías ser más específico? Puedo explicar: machine learning, SVM, árboles de decisión, redes neuronales, etc."
    
    def respuesta_default(self) -> str:
        """
        Respuesta por defecto cuando no se entiende la consulta
        """
        respuestas = [
            "🤔 No estoy seguro de entender tu consulta. ¿Podrías reformularla?",
            "💭 Hmm, no tengo información específica sobre eso. ¿Puedo ayudarte con algo más?",
            "❓ No comprendí completamente. Puedo ayudarte con tareas del curso, conceptos de ML o progreso."
        ]
        return respuestas[0]
    
    def obtener_estadisticas(self) -> Dict:
        """
        Retorna estadísticas del curso
        """
        completadas = sum(1 for t in self.tareas_curso.values() if t["estado"] == "completado")
        en_progreso = sum(1 for t in self.tareas_curso.values() if t["estado"] == "en_progreso")
        pendientes = sum(1 for t in self.tareas_curso.values() if t["estado"] == "pendiente")
        
        return {
            "total_tareas": len(self.tareas_curso),
            "completadas": completadas,
            "en_progreso": en_progreso,
            "pendientes": pendientes,
            "porcentaje_completado": (completadas / len(self.tareas_curso)) * 100
        }

def main():
    """
    Función principal que ejecuta el chatbot
    """
    print("="*60)
    print("🤖 AGENTE DE IA PARA MANEJO DE TAREAS DEL CURSO")
    print("="*60)
    print("¡Hola! Soy tu asistente de IA para el curso.")
    print("Puedo ayudarte con:")
    print("• Ver progreso de tareas")
    print("• Recordatorios pendientes") 
    print("• Explicar conceptos de ML")
    print("• Información del curso")
    print("\nEscribe 'salir' para terminar la conversación.")
    print("="*60)
    
    agente = AgenteIACurso()
    
    while True:
        try:
            # Obtener consulta del usuario
            consulta = input("\n🧑 Tú: ").strip()
            
            # Verificar si quiere salir
            if consulta.lower() in ['salir', 'exit', 'quit', 'adiós']:
                print("🤖 Agente: ¡Hasta luego! Que tengas éxito con tus estudios de IA.")
                break
            
            # Verificar consulta vacía
            if not consulta:
                print("🤖 Agente: ¿En qué puedo ayudarte?")
                continue
            
            # Procesar consulta y obtener respuesta
            respuesta = agente.procesar_consulta(consulta)
            print(f"🤖 Agente: {respuesta}")
            
        except KeyboardInterrupt:
            print("\n🤖 Agente: ¡Hasta luego! Presiona Ctrl+C para salir.")
            break
        except Exception as e:
            print(f"🤖 Agente: Lo siento, hubo un error: {str(e)}")

def demo_funcionalidades():
    """
    Demuestra las funcionalidades del agente
    """
    print("="*60)
    print("🔬 DEMO DE FUNCIONALIDADES DEL AGENTE")
    print("="*60)
    
    agente = AgenteIACurso()
    
    # Lista de consultas de prueba
    consultas_demo = [
        "Hola, ¿cómo estás?",
        "¿Qué puedes hacer?",
        "Muéstrame las tareas completadas",
        "¿Qué tareas están pendientes?",
        "Explícame qué es machine learning",
        "¿Qué es SVM?",
        "Dame información sobre la tarea 6.1",
        "¿Cómo va mi progreso?",
        "Gracias por la ayuda"
    ]
    
    for consulta in consultas_demo:
        print(f"\n🧑 Usuario: {consulta}")
        respuesta = agente.procesar_consulta(consulta)
        print(f"🤖 Agente: {respuesta}")
        print("-" * 40)
    
    # Mostrar estadísticas
    print("\n📊 ESTADÍSTICAS DEL CURSO:")
    stats = agente.obtener_estadisticas()
    for key, value in stats.items():
        print(f"   {key}: {value}")

if __name__ == "__main__":
    print("Ejecutando demo automática del agente...")
    demo_funcionalidades()
