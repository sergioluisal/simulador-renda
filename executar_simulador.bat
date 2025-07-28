@echo off
echo Iniciando Simulador de Renda Variavel...
echo.

REM Verificar se o streamlit esta instalado
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo ERRO: Streamlit nao encontrado!
    echo Execute primeiro: instalar_dependencias.bat
    echo.
    pause
    exit /b 1
)

REM Verificar se o yfinance esta instalado
python -c "import yfinance" 2>nul
if errorlevel 1 (
    echo ERRO: yfinance nao encontrado!
    echo Execute primeiro: instalar_dependencias.bat
    echo.
    pause
    exit /b 1
)

echo Todas as dependencias encontradas!
echo Iniciando aplicacao...
echo.

REM Tentar executar com streamlit
streamlit run app_streamlit.py

REM Se falhar, tentar com python -m streamlit
if errorlevel 1 (
    echo Tentando metodo alternativo...
    python -m streamlit run app_streamlit.py
)

pause

