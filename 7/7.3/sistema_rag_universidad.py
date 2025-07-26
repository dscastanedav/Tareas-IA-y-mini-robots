# -*- coding: utf-8 -*-
"""
Sistema RAG Básico para Universidad Nacional
Tarea 7.3 - Chat con información actualizada de la Universidad Nacional

Este es un sistema RAG (Retrieval-Augmented Generation) simple que:
- Simula información de la Universidad Nacional
- Permite hacer consultas sobre la universidad
- Combina búsqueda de información con generación de respuestas
"""

import re
import json
from datetime import datetime
from typing import List, Dict, Tuple

class SistemaRAGUniversidad:
    """
    Sistema RAG básico para consultas sobre la Universidad Nacional
    
    RAG = Retrieval-Augmented Generation
    - Retrieval: Busca información relevante
    - Augmented: Enriquece la respuesta
    - Generation: Genera respuesta natural
    """
    
    def __init__(self):
        """Inicializa el sistema con datos simulados de la Universidad Nacional"""
        self.nombre_sistema = "ChatUN - Sistema RAG Universidad Nacional"
        self.version = "1.0"
        
        # Base de conocimiento simulada de la Universidad Nacional
        self.base_conocimiento = {
            "informacion_general": {
                "nombre": "Universidad Nacional de Colombia",
                "fundacion": "1867",
                "ubicacion": "Bogotá, Colombia (sede principal)",
                "tipo": "Universidad pública",
                "rector": "Dr. Dolly Montoya Castaño",
                "estudiantes": "Aproximadamente 53,000 estudiantes",
                "sedes": "Bogotá, Medellín, Manizales, Palmira, Arauca, Leticia, San Andrés, Tumaco, La Paz"
            },
            
            "facultades": {
                "ingenieria": {
                    "nombre": "Facultad de Ingeniería",
                    "programas": ["Ingeniería Civil", "Ingeniería de Sistemas", "Ingeniería Eléctrica", 
                                "Ingeniería Mecánica", "Ingeniería Industrial", "Ingeniería Química"],
                    "ubicacion": "Ciudad Universitaria, Bogotá"
                },
                "ciencias": {
                    "nombre": "Facultad de Ciencias",
                    "programas": ["Matemáticas", "Física", "Química", "Biología", "Geología", "Estadística"],
                    "ubicacion": "Ciudad Universitaria, Bogotá"
                },
                "medicina": {
                    "nombre": "Facultad de Medicina",
                    "programas": ["Medicina", "Enfermería", "Nutrición", "Terapia Ocupacional", "Fonoaudiología"],
                    "ubicacion": "Ciudad Universitaria, Bogotá"
                },
                "derecho": {
                    "nombre": "Facultad de Derecho, Ciencias Políticas y Sociales",
                    "programas": ["Derecho", "Ciencia Política", "Trabajo Social", "Sociología"],
                    "ubicacion": "Ciudad Universitaria, Bogotá"
                },
                "artes": {
                    "nombre": "Facultad de Artes",
                    "programas": ["Artes Plásticas", "Música", "Diseño Gráfico", "Cine y Televisión"],
                    "ubicacion": "Ciudad Universitaria, Bogotá"
                }
            },
            
            "servicios": {
                "biblioteca": {
                    "nombre": "Sistema Nacional de Bibliotecas",
                    "horarios": "Lunes a viernes: 7:00 AM - 9:00 PM, Sábados: 8:00 AM - 5:00 PM",
                    "servicios": ["Préstamo de libros", "Salas de estudio", "Acceso a bases de datos", "Internet"],
                    "ubicacion": "Edificio de Biblioteca Central"
                },
                "bienestar": {
                    "nombre": "Dirección de Bienestar Universitario",
                    "servicios": ["Becas", "Alimentación", "Salud", "Cultura", "Deporte", "Psicología"],
                    "contacto": "bienestar_bog@unal.edu.co"
                },
                "registro": {
                    "nombre": "División de Registro y Control Académico",
                    "servicios": ["Inscripciones", "Matrículas", "Certificados", "Notas", "Grados"],
                    "horarios": "Lunes a viernes: 8:00 AM - 5:00 PM"
                }
            },
            
            "admisiones": {
                "proceso": "Examen de admisión PEAMA",
                "fechas_2025": {
                    "inscripciones": "Febrero - Marzo 2025",
                    "examen": "Mayo 2025",
                    "resultados": "Junio 2025"
                },
                "requisitos": ["Título de bachiller", "Documento de identidad", "Pago de inscripción"],
                "costo_inscripcion": "$87,000 COP (2025)"
            },
            
            "contacto": {
                "telefono": "(+57) 1 316 5000",
                "direccion": "Carrera 45 No. 26-85, Bogotá, Colombia",
                "email": "infogeneral_bog@unal.edu.co",
                "pagina_web": "https://unal.edu.co",
                "redes_sociales": {
                    "facebook": "@UNALOficial",
                    "twitter": "@UNALOficial",
                    "instagram": "@universidadnacionaldecolombia"
                }
            }
        }
        
        # Patrones para reconocer tipos de consultas
        self.patrones_consulta = {
            "informacion_general": ["universidad", "fundacion", "historia", "general", "que es"],
            "facultades": ["facultad", "carrera", "programa", "ingenieria", "medicina", "derecho"],
            "servicios": ["biblioteca", "bienestar", "registro", "servicio"],
            "admisiones": ["admision", "inscripcion", "examen", "requisitos", "costo"],
            "contacto": ["telefono", "direccion", "contacto", "email", "ubicacion"]
        }
    
    def buscar_informacion(self, consulta: str) -> List[Dict]:
        """
        Busca información relevante en la base de conocimiento
        
        Args:
            consulta: Pregunta del usuario
            
        Returns:
            Lista de información relevante encontrada
        """
        consulta_lower = consulta.lower()
        resultados = []
        
        # Buscar en cada categoría
        for categoria, palabras_clave in self.patrones_consulta.items():
            # Verificar si la consulta coincide con palabras clave
            if any(palabra in consulta_lower for palabra in palabras_clave):
                if categoria in self.base_conocimiento:
                    resultados.append({
                        "categoria": categoria,
                        "datos": self.base_conocimiento[categoria],
                        "relevancia": self._calcular_relevancia(consulta_lower, palabras_clave)
                    })
        
        # Ordenar por relevancia
        resultados.sort(key=lambda x: x["relevancia"], reverse=True)
        
        return resultados
    
    def _calcular_relevancia(self, consulta: str, palabras_clave: List[str]) -> float:
        """Calcula la relevancia de una categoría para la consulta"""
        coincidencias = sum(1 for palabra in palabras_clave if palabra in consulta)
        return coincidencias / len(palabras_clave)
    
    def generar_respuesta(self, consulta: str, informacion_encontrada: List[Dict]) -> str:
        """
        Genera una respuesta natural basada en la información encontrada
        
        Args:
            consulta: Pregunta original del usuario
            informacion_encontrada: Información relevante encontrada
            
        Returns:
            Respuesta generada
        """
        if not informacion_encontrada:
            return self._respuesta_no_encontrada()
        
        # Tomar la información más relevante
        info_principal = informacion_encontrada[0]
        categoria = info_principal["categoria"]
        datos = info_principal["datos"]
        
        # Generar respuesta según la categoría
        if categoria == "informacion_general":
            return self._generar_respuesta_general(datos)
        elif categoria == "facultades":
            return self._generar_respuesta_facultades(datos, consulta)
        elif categoria == "servicios":
            return self._generar_respuesta_servicios(datos, consulta)
        elif categoria == "admisiones":
            return self._generar_respuesta_admisiones(datos)
        elif categoria == "contacto":
            return self._generar_respuesta_contacto(datos)
        else:
            return self._respuesta_generica(datos)
    
    def _generar_respuesta_general(self, datos: Dict) -> str:
        """Genera respuesta sobre información general"""
        return f"""🏛️ **Universidad Nacional de Colombia**

La Universidad Nacional de Colombia es una institución pública fundada en {datos['fundacion']}. 
Es la principal universidad pública del país con sede principal en {datos['ubicacion']}.

📊 **Datos importantes:**
• Rector: {datos['rector']}
• Estudiantes: {datos['estudiantes']}
• Tipo: {datos['tipo']}

🌍 **Sedes:** {datos['sedes']}

¿Te gustaría conocer más sobre algún aspecto específico de la universidad?"""
    
    def _generar_respuesta_facultades(self, datos: Dict, consulta: str) -> str:
        """Genera respuesta sobre facultades"""
        consulta_lower = consulta.lower()
        
        # Buscar facultad específica
        for nombre_facultad, info in datos.items():
            if nombre_facultad in consulta_lower or any(prog.lower() in consulta_lower for prog in info["programas"]):
                return f"""🎓 **{info['nombre']}**

📍 **Ubicación:** {info['ubicacion']}

📚 **Programas disponibles:**
{chr(10).join(f"• {programa}" for programa in info['programas'])}

¿Necesitas información específica sobre algún programa?"""
        
        # Respuesta general sobre todas las facultades
        respuesta = "🎓 **Facultades de la Universidad Nacional:**\n\n"
        for info in datos.values():
            respuesta += f"• **{info['nombre']}**\n"
            respuesta += f"  Programas: {', '.join(info['programas'][:3])}...\n\n"
        
        respuesta += "¿Te interesa información específica sobre alguna facultad?"
        return respuesta
    
    def _generar_respuesta_servicios(self, datos: Dict, consulta: str) -> str:
        """Genera respuesta sobre servicios"""
        consulta_lower = consulta.lower()
        
        # Buscar servicio específico
        for nombre_servicio, info in datos.items():
            if nombre_servicio in consulta_lower:
                respuesta = f"🏢 **{info['nombre']}**\n\n"
                
                if "horarios" in info:
                    respuesta += f"⏰ **Horarios:** {info['horarios']}\n\n"
                
                if "servicios" in info:
                    respuesta += "📋 **Servicios disponibles:**\n"
                    respuesta += "\n".join(f"• {servicio}" for servicio in info['servicios'])
                    respuesta += "\n\n"
                
                if "contacto" in info:
                    respuesta += f"📧 **Contacto:** {info['contacto']}\n"
                
                return respuesta
        
        # Respuesta general sobre servicios
        respuesta = "🏢 **Servicios de la Universidad Nacional:**\n\n"
        for info in datos.values():
            respuesta += f"• **{info['nombre']}**\n"
        
        respuesta += "\n¿Sobre qué servicio específico necesitas información?"
        return respuesta
    
    def _generar_respuesta_admisiones(self, datos: Dict) -> str:
        """Genera respuesta sobre admisiones"""
        return f"""📝 **Proceso de Admisiones 2025**

🎯 **Proceso:** {datos['proceso']}

📅 **Fechas importantes:**
• Inscripciones: {datos['fechas_2025']['inscripciones']}
• Examen: {datos['fechas_2025']['examen']}
• Resultados: {datos['fechas_2025']['resultados']}

📋 **Requisitos:**
{chr(10).join(f"• {req}" for req in datos['requisitos'])}

💰 **Costo de inscripción:** {datos['costo_inscripcion']}

¿Necesitas más detalles sobre el proceso de admisión?"""
    
    def _generar_respuesta_contacto(self, datos: Dict) -> str:
        """Genera respuesta sobre información de contacto"""
        return f"""📞 **Información de Contacto**

🏢 **Dirección:** {datos['direccion']}
📞 **Teléfono:** {datos['telefono']}
📧 **Email:** {datos['email']}
🌐 **Página web:** {datos['pagina_web']}

📱 **Redes sociales:**
• Facebook: {datos['redes_sociales']['facebook']}
• Twitter: {datos['redes_sociales']['twitter']}
• Instagram: {datos['redes_sociales']['instagram']}

¿Necesitas contactar algún departamento específico?"""
    
    def _respuesta_no_encontrada(self) -> str:
        """Respuesta cuando no se encuentra información"""
        return """❓ **No encontré información específica sobre tu consulta.**

Puedo ayudarte con:
• Información general de la Universidad Nacional
• Facultades y programas académicos
• Servicios universitarios (biblioteca, bienestar, registro)
• Proceso de admisiones
• Información de contacto

¿Podrías reformular tu pregunta o elegir uno de estos temas?"""
    
    def _respuesta_generica(self, datos: Dict) -> str:
        """Respuesta genérica cuando no se puede clasificar"""
        return f"""📋 **Información encontrada:**

{json.dumps(datos, indent=2, ensure_ascii=False)}

¿Necesitas más detalles sobre algún aspecto específico?"""
    
    def procesar_consulta(self, consulta: str) -> str:
        """
        Procesa una consulta completa usando el sistema RAG
        
        Args:
            consulta: Pregunta del usuario
            
        Returns:
            Respuesta generada
        """
        # Paso 1: Buscar información relevante (Retrieval)
        informacion = self.buscar_informacion(consulta)
        
        # Paso 2: Generar respuesta enriquecida (Augmented Generation)
        respuesta = self.generar_respuesta(consulta, informacion)
        
        return respuesta
    
    def mostrar_ayuda(self) -> str:
        """Muestra la ayuda del sistema"""
        return """🤖 **ChatUN - Sistema RAG Universidad Nacional**

**¿Cómo funciona?**
Este sistema RAG (Retrieval-Augmented Generation) busca información relevante sobre la Universidad Nacional y genera respuestas naturales.

**Ejemplos de consultas:**
• "¿Cuándo fue fundada la Universidad Nacional?"
• "¿Qué programas ofrece la facultad de ingeniería?"
• "¿Cuáles son los horarios de la biblioteca?"
• "¿Cómo es el proceso de admisión?"
• "¿Cuál es el teléfono de la universidad?"

**Categorías disponibles:**
📚 Información general
🎓 Facultades y programas
🏢 Servicios universitarios
📝 Admisiones
📞 Contacto

¡Haz tu consulta y te ayudaré a encontrar la información!"""

def demo_sistema():
    """Demuestra el funcionamiento del sistema RAG"""
    print("🤖 DEMO DEL SISTEMA RAG - UNIVERSIDAD NACIONAL")
    print("=" * 50)
    
    sistema = SistemaRAGUniversidad()
    
    # Consultas de ejemplo
    consultas_demo = [
        "¿Cuándo fue fundada la Universidad Nacional?",
        "¿Qué programas ofrece la facultad de ingeniería?",
        "¿Cuáles son los horarios de la biblioteca?",
        "¿Cómo es el proceso de admisión?",
        "¿Cuál es el teléfono de la universidad?",
        "¿Dónde queda la facultad de medicina?"
    ]
    
    for consulta in consultas_demo:
        print(f"\n👤 Consulta: {consulta}")
        print("-" * 40)
        respuesta = sistema.procesar_consulta(consulta)
        print(f"🤖 Respuesta:\n{respuesta}")
        print("=" * 50)

def demo_sistema():
    """Ejecuta una demostración del sistema RAG"""
    print("\n🔬 DEMOSTRACIÓN DEL SISTEMA RAG")
    print("=" * 50)
    
    sistema = SistemaRAGUniversidad()
    
    # Consultas de ejemplo
    consultas_demo = [
        "¿Qué carreras de ingeniería ofrece la Universidad Nacional?",
        "¿Dónde está ubicada la Universidad Nacional?",
        "¿Cuándo fue fundada la universidad?",
        "¿Qué programas de posgrado hay en medicina?",
        "¿Cómo funciona la admisión?",
        "¿Qué sedes tiene la universidad?",
        "¿Quién es el rector actual?",
        "¿Cuántos estudiantes tiene la universidad?"
    ]
    
    for consulta in consultas_demo:
        print(f"\n💬 Consulta: {consulta}")
        respuesta = sistema.procesar_consulta(consulta)
        print(f"🤖 Respuesta:\n{respuesta}")
        print("-" * 50)
    
    print("\n✅ Demo completada!")

def main():
    """Función principal para interactuar con el sistema RAG"""
    print("🤖 CHATUN - SISTEMA RAG UNIVERSIDAD NACIONAL")
    print("=" * 50)
    
    sistema = SistemaRAGUniversidad()
    
    # Mostrar ayuda inicial
    print(sistema.mostrar_ayuda())
    print("\nEscribe 'salir' para terminar, 'ayuda' para ver opciones, 'demo' para ejemplos")
    print("=" * 50)
    
    while True:
        try:
            consulta = input("\n💬 Tu consulta: ").strip()
            
            if consulta.lower() in ['salir', 'exit', 'quit']:
                print("\n🤖 ¡Hasta luego! Gracias por usar ChatUN.")
                break
            
            if consulta.lower() == 'ayuda':
                print(sistema.mostrar_ayuda())
                continue
            
            if consulta.lower() == 'demo':
                demo_sistema()
                continue
            
            if not consulta:
                print("🤖 Por favor, escribe una consulta.")
                continue
            
            # Procesar consulta con RAG
            respuesta = sistema.procesar_consulta(consulta)
            print(f"\n🤖 Respuesta:\n{respuesta}")
            
        except KeyboardInterrupt:
            print("\n\n🤖 ¡Hasta luego! (Ctrl+C detectado)")
            break
        except Exception as e:
            print(f"\n🤖 Error: {e}")

if __name__ == "__main__":
    print("Ejecutando demo automática del Sistema RAG...")
    demo_sistema()
