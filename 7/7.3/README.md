# 🤖 Sistema RAG - Universidad Nacional

## Tarea 7.3 - Sistema RAG Sencillo

### ¿Qué es RAG?
**RAG** significa **Retrieval-Augmented Generation** (Generación Aumentada por Recuperación).

Es un sistema que combina:
- **Retrieval** (Recuperación): Busca información relevante en una base de datos
- **Augmented** (Aumentado): Enriquece la respuesta con información encontrada  
- **Generation** (Generación): Genera respuestas naturales y coherentes

### Cómo funciona nuestro sistema

```
Consulta del usuario
        ↓
    Búsqueda en base de conocimiento
        ↓
    Selección de información relevante
        ↓
    Generación de respuesta natural
        ↓
    Respuesta al usuario
```

### Características del sistema

✅ **Básico y funcional**
- Base de conocimiento simulada sobre la Universidad Nacional
- Búsqueda por palabras clave
- Generación de respuestas naturales

✅ **Categorías de información**
- 📚 Información general
- 🎓 Facultades y programas  
- 🏢 Servicios universitarios
- 📝 Admisiones
- 📞 Contacto

✅ **Funcionalidades**
- Chat interactivo
- Respuestas contextualizadas
- Ayuda integrada
- Modo demo

### Cómo usar

1. **Ejecutar el sistema:**
   ```bash
   python sistema_rag_universidad.py
   ```

2. **Tipos de consultas:**
   - "¿Cuándo fue fundada la Universidad Nacional?"
   - "¿Qué programas ofrece ingeniería?"
   - "¿Cuáles son los horarios de la biblioteca?"
   - "¿Cómo es el proceso de admisión?"

3. **Comandos especiales:**
   - `ayuda` - Muestra información del sistema
   - `demo` - Ejecuta ejemplos automáticos
   - `salir` - Termina el programa

### Ejemplo de funcionamiento

```
💬 Tu consulta: ¿Qué programas ofrece la facultad de ingeniería?

🤖 Respuesta:
🎓 Facultad de Ingeniería

📍 Ubicación: Ciudad Universitaria, Bogotá

📚 Programas disponibles:
• Ingeniería Civil
• Ingeniería de Sistemas
• Ingeniería Eléctrica
• Ingeniería Mecánica
• Ingeniería Industrial
• Ingeniería Química

¿Necesitas información específica sobre algún programa?
```

### Estructura del código

#### Clase principal: `SistemaRAGUniversidad`
- `buscar_informacion()` - Busca datos relevantes
- `generar_respuesta()` - Crea respuestas naturales
- `procesar_consulta()` - Combina búsqueda y generación

#### Base de conocimiento:
- **Información general**: Historia, datos básicos
- **Facultades**: Programas por facultad
- **Servicios**: Biblioteca, bienestar, registro
- **Admisiones**: Proceso, fechas, requisitos
- **Contacto**: Teléfonos, direcciones, emails

### Limitaciones (por diseño simple)

- Base de conocimiento simulada (no real)
- Búsqueda básica por palabras clave
- Sin conexión a internet
- Información estática (no se actualiza)
- No usa modelos de IA complejos

### Ventajas del sistema

✅ **Simplicidad**: Fácil de entender y modificar
✅ **Velocidad**: Respuestas inmediatas
✅ **Personalizable**: Fácil agregar nueva información
✅ **Educativo**: Muestra principios de RAG
✅ **Funcional**: Responde consultas reales

### Posibles mejoras

Para un sistema más avanzado se podría:
- Conectar a base de datos real
- Usar embeddings para búsqueda semántica
- Integrar con API de OpenAI o similar
- Añadir más fuentes de información
- Implementar aprendizaje automático

### Comparación con RAG real

| Aspecto | Nuestro sistema | RAG avanzado |
|---------|----------------|--------------|
| **Búsqueda** | Palabras clave | Búsqueda semántica |
| **Base de datos** | Diccionario Python | Vector database |
| **Generación** | Templates | Modelos de lenguaje |
| **Actualización** | Manual | Automática |
| **Precisión** | Básica | Alta |

### Casos de uso reales

Este tipo de sistema se usa en:
- **Chatbots empresariales**: Atención al cliente
- **Asistentes educativos**: Universidades y colegios
- **Soporte técnico**: Bases de conocimiento
- **Bibliotecas digitales**: Búsqueda de documentos

---

**Nota**: Este es un sistema educativo básico que demuestra los principios de RAG de forma simple y comprensible.
