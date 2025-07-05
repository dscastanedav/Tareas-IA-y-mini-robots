@echo off
echo ==========================================
echo Ejecutando Comparacion Simple MEPX vs RNA
echo ==========================================
echo.

echo Verificando instalacion de Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado
    echo Ejecuta install.bat primero
    pause
    exit /b 1
)

echo.
echo Ejecutando comparacion...
echo.

python simple_mepx_rna_comparison.py

echo.
echo ==========================================
echo Ejecucion completada!
echo ==========================================
echo.
echo Archivos generados:
echo   - rna_vs_mepx_simple.png
echo.
echo Presiona cualquier tecla para cerrar...
pause >nul
