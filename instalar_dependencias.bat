@echo off
echo Instalando dependencias do Simulador de Renda Variavel...
echo.

echo 1. Instalando yfinance...
pip install yfinance

echo.
echo 2. Instalando streamlit...
pip install streamlit

echo.
echo 3. Instalando pandas...
pip install pandas

echo.
echo 4. Instalando numpy...
pip install numpy

echo.
echo 5. Instalando plotly...
pip install plotly

echo.
echo Instalacao concluida!
echo.
echo Para executar o simulador, digite:
echo streamlit run app_streamlit.py
echo.
pause

