@echo off
echo ==========================================
echo Instalador para Comparacion MEPX vs RNA
echo ==========================================
echo.

echo Verificando instalacion de Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor, instala Python desde https://python.org
    pause
    exit /b 1
)

echo Python encontrado!
python --version

echo.
echo Instalando dependencias...
echo.

echo Instalando numpy...
pip install numpy>=1.21.0

echo Instalando pandas...
pip install pandas>=1.3.0

echo Instalando matplotlib...
pip install matplotlib>=3.5.0

echo Instalando scikit-learn...
pip install scikit-learn>=1.0.0

echo Instalando seaborn...
pip install seaborn>=0.11.0

echo.
echo ==========================================
echo Instalacion completada!
echo ==========================================
echo.
echo Puedes ejecutar los scripts con:
echo   python simple_mepx_rna_comparison.py
echo   python mepx_vs_rna_comparison.py
echo.
pause
