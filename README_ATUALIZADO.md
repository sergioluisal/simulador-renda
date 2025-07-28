# 📊 Simulador de Renda Variável Avançado

Um simulador completo de investimentos em renda variável com funcionalidades avançadas para análise de ações, BDRs e ETFs.

## 🚀 Funcionalidades Principais

### 💰 **Cálculo de Dividendos e JCP**
- ✅ Busca automática de dados de dividendos e Juros Sobre Capital Próprio
- ✅ Cálculo do dividend yield
- ✅ Opção de reinvestimento automático dos proventos
- ✅ Análise do impacto dos dividendos na rentabilidade total

### 📈 **Simulação de Aportes Mensais**
- ✅ Simulação de investimentos mensais regulares
- ✅ Compra automática de ações com aportes
- ✅ Cálculo do valor total aportado ao longo do tempo
- ✅ Análise do efeito do dollar-cost averaging

### 📊 **Análise Completa de Investimentos**
- ✅ Rentabilidade absoluta e percentual
- ✅ Volatilidade anualizada
- ✅ Sharpe Ratio
- ✅ Drawdown máximo
- ✅ Gráficos interativos com Plotly

### 🌐 **Interface Streamlit Intuitiva**
- ✅ Design responsivo e moderno
- ✅ Configurações na barra lateral
- ✅ Resultados em tempo real
- ✅ Comparação entre múltiplos ativos

## 📋 Ativos Suportados

- **Ações Americanas**: AAPL, GOOGL, MSFT, TSLA, AMZN, NVDA, META, etc.
- **Ações Brasileiras**: PETR4.SA, VALE3.SA, ITUB4.SA, BBDC4.SA, MGLU3.SA, etc.
- **BDRs**: AAPL34.SA, GOGL34.SA, MSFT34.SA, TSLA34.SA, AMZO34.SA, etc.
- **ETFs Brasileiros**: BOVA11.SA, SMAL11.SA, IVVB11.SA, DIVO11.SA, etc.
- **ETFs Americanos**: SPY, QQQ, VTI, VOO, IWM, etc.

## 🛠️ Instalação e Uso

### Pré-requisitos
```bash
pip install streamlit pandas numpy yfinance plotly
```

### Executando a Aplicação
```bash
streamlit run app_streamlit.py
```

### Usando o Simulador via Script
```python
from simulador_renda_variavel_corrigido import SimuladorRendaVariavel

simulador = SimuladorRendaVariavel()
resultado = simulador.simular_investimento(
    symbol='AAPL',
    valor_inicial=10000,
    considerar_dividendos=True,
    reinvestir_dividendos=True,
    aporte_mensal=500
)
```

## 📊 Exemplos de Uso

### 1. Simulação Básica
```python
# Investimento único em Apple
resultado = simulador.simular_investimento('AAPL', 10000)
```

### 2. Com Dividendos e Reinvestimento
```python
# Investimento com reinvestimento de dividendos
resultado = simulador.simular_investimento(
    'AAPL', 
    10000, 
    considerar_dividendos=True,
    reinvestir_dividendos=True
)
```

### 3. Com Aportes Mensais
```python
# Investimento com aportes mensais de R$ 500
resultado = simulador.simular_investimento(
    'AAPL', 
    10000, 
    aporte_mensal=500
)
```

### 4. Simulação Completa
```python
# Todas as funcionalidades ativadas
resultado = simulador.simular_investimento(
    'AAPL', 
    10000, 
    considerar_dividendos=True,
    reinvestir_dividendos=True,
    aporte_mensal=500
)
```

## 📈 Métricas Calculadas

### **Rentabilidade**
- Ganho/perda absoluta em R$
- Rentabilidade percentual
- Período de investimento

### **Dividendos e JCP**
- Total de proventos recebidos
- Dividend yield
- Impacto do reinvestimento

### **Aportes Mensais**
- Valor total aportado
- Quantidade de ações acumuladas
- Efeito do dollar-cost averaging

### **Análise de Risco**
- Volatilidade anualizada
- Sharpe Ratio
- Drawdown máximo

## 🔧 Arquivos do Projeto

- `simulador_renda_variavel_corrigido.py` - Lógica principal do simulador
- `app_streamlit.py` - Interface web com Streamlit
- `lista_ativos_populares.py` - Lista de ativos sugeridos
- `requirements.txt` - Dependências do projeto
- `README_ATUALIZADO.md` - Documentação atualizada
- `todo.md` - Histórico de desenvolvimento

## ⚠️ Importante

Este simulador utiliza dados históricos reais do Yahoo Finance e serve apenas para fins educacionais e de análise. **Não constitui recomendação de investimento.**

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Adicionar novos ativos à lista

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

