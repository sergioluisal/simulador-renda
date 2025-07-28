# 🚀 Instruções de Instalação - Simulador de Renda Variável

## ⚠️ Problema Identificado
O erro "No module named 'streamlit'" indica que o Streamlit não está instalado ou não está acessível no seu ambiente Python.

## 🔧 Soluções (tente na ordem)

### **Opção 1: Script Automático (Recomendado)**
1. Execute o arquivo `instalar_dependencias.bat` (duplo clique)
2. Aguarde a instalação de todas as dependências
3. Execute o arquivo `executar_simulador.bat` (duplo clique)

### **Opção 2: Instalação Manual**
Abra o **Prompt de Comando** ou **PowerShell** e execute:

```bash
# Instalar todas as dependências
pip install streamlit yfinance pandas numpy plotly

# Executar o simulador
streamlit run app_streamlit.py
```

### **Opção 3: Se o comando 'streamlit' não funcionar**
```bash
# Usar o módulo Python diretamente
python -m streamlit run app_streamlit.py
```

### **Opção 4: Verificar versão do Python**
```bash
# Verificar se está usando Python 3
python --version

# Se necessário, usar python3
python3 -m pip install streamlit yfinance pandas numpy plotly
python3 -m streamlit run app_streamlit.py
```

### **Opção 5: Ambiente Virtual (Mais Seguro)**
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Instalar dependências
pip install streamlit yfinance pandas numpy plotly

# Executar simulador
streamlit run app_streamlit.py
```

## 🎯 Verificação de Instalação

Para verificar se tudo está instalado corretamente:

```bash
python -c "import streamlit; print('Streamlit OK')"
python -c "import yfinance; print('yfinance OK')"
python -c "import pandas; print('pandas OK')"
python -c "import numpy; print('numpy OK')"
python -c "import plotly; print('plotly OK')"
```

## 🌐 Acesso à Aplicação

Após executar com sucesso, a aplicação estará disponível em:
- **URL Local**: http://localhost:8501
- O navegador deve abrir automaticamente

## 📋 Estrutura dos Arquivos

Certifique-se de que os seguintes arquivos estão na mesma pasta:
- `app_streamlit.py` (aplicação principal)
- `simulador_renda_variavel_corrigido.py` (lógica do simulador)
- `requirements.txt` (dependências)

## ❓ Problemas Comuns

### "streamlit: command not found"
- Use: `python -m streamlit run app_streamlit.py`

### "Permission denied"
- Execute o Prompt de Comando como Administrador

### "Multiple Python versions"
- Use ambiente virtual (Opção 5)

### "ModuleNotFoundError"
- Reinstale as dependências: `pip install --upgrade streamlit yfinance pandas numpy plotly`

## 🆘 Se nada funcionar

1. Desinstale e reinstale o Python
2. Use o Anaconda/Miniconda:
   ```bash
   conda install streamlit
   conda install -c conda-forge yfinance
   ```

## 📞 Suporte

Se ainda tiver problemas, me informe:
1. Versão do Python (`python --version`)
2. Sistema operacional
3. Mensagem de erro completa

