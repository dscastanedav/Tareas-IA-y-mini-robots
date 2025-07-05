# 🤖 Agente de IA para Tareas del Curso

## Descripción
Este es un agente de IA básico creado para la **Tarea 7.1** que ayuda a gestionar las tareas del curso de IA y mini robots.

## Funcionalidades

### 🎯 Principales características:
- **Gestión de tareas**: Lista tareas completadas y pendientes
- **Seguimiento de progreso**: Muestra estadísticas del curso
- **Asistente de conceptos**: Explica términos de Machine Learning
- **Información de proyectos**: Detalles sobre cada tarea
- **Chatbot interactivo**: Respuestas en lenguaje natural

### 💬 Tipos de consultas que puede responder:
- "¿Qué tareas tengo pendientes?"
- "Muéstrame mi progreso"
- "¿Qué es machine learning?"
- "Dame información sobre la tarea 6.1"
- "¿Qué puedes hacer?"

## Cómo usar

### Ejecutar el agente:
```bash
python agente_ia_curso.py
```

### Opciones disponibles:
1. **Chatbot interactivo** - Conversación en tiempo real
2. **Demo de funcionalidades** - Muestra ejemplos de uso

## Estructura del código

### Clase principal: `AgenteIACurso`
- `procesar_consulta()` - Procesa las preguntas del usuario
- `mostrar_progreso()` - Estadísticas del curso
- `listar_pendientes()` - Tareas sin completar
- `listar_completadas()` - Tareas finalizadas
- `explicar_concepto()` - Definiciones de ML
- `obtener_info_tarea()` - Detalles de proyectos

### Base de conocimientos:
- **Tareas del curso**: 6.1, 6.2, 6.3, 7.1
- **Conceptos de ML**: Definiciones básicas
- **Respuestas predefinidas**: Saludos, despedidas, ayuda

## Características técnicas

- **Lenguaje**: Python 3.x
- **Dependencias**: Solo librerías estándar
- **Interfaz**: Consola de texto
- **Almacenamiento**: Datos en memoria (no persistente)

## Limitaciones (diseñadas para ser básico)

- No guarda datos entre sesiones
- Respuestas basadas en patrones simples
- Base de conocimientos limitada
- Sin conexión a internet ni APIs externas

## Ejemplo de uso

```
🧑 Usuario: Hola
🤖 Agente: ¡Hola! Soy tu asistente de IA para el curso.

🧑 Usuario: ¿Qué tareas tengo pendientes?
🤖 Agente: 📋 TAREAS PENDIENTES:
• 7.1: Desarrollo de Agente de IA
  Estado: En progreso

🧑 Usuario: ¿Qué es machine learning?
🤖 Agente: 🧠 MACHINE LEARNING:
Es una rama de la IA que permite a las máquinas aprender automáticamente...
```

---

**Nota**: Este agente fue diseñado específicamente para ser básico y funcional, cumpliendo con los requisitos de la Tarea 7.1.
