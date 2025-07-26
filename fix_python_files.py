# -*- coding: utf-8 -*-
"""
Script para arreglar todos los archivos Python en Windows
=========================================================

Este script corrige los shebangs de Unix a formato compatible con Windows
"""

import os
import glob

def fix_python_files():
    """Arregla todos los archivos .py en el directorio y subdirectorios"""
    
    base_path = r"c:\Users\santi\OneDrive\Documentos\Tareas IA y mini robots"
    
    # Encontrar todos los archivos .py
    python_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"Encontrados {len(python_files)} archivos Python")
    
    fixed_count = 0
    
    for file_path in python_files:
        try:
            # Leer el archivo
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Verificar si necesita corrección
            if lines and lines[0].startswith('#!/usr/bin/env python3'):
                print(f"Corrigiendo: {file_path}")
                
                # Remover la primera línea del shebang
                lines = lines[1:]
                
                # Escribir el archivo corregido
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                fixed_count += 1
            
        except Exception as e:
            print(f"Error procesando {file_path}: {e}")
    
    print(f"\n✅ Corregidos {fixed_count} archivos")
    print("Ahora puedes ejecutar los archivos directamente con:")
    print("python nombre_archivo.py")

if __name__ == "__main__":
    fix_python_files()
