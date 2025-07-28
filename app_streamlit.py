#!/usr/bin/env python3
"""
Aplicação Streamlit para Simulador de Renda Variável
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from simulador_integrado import SimuladorRendaVariavel, AnalisadorHistorico
from lista_ativos_populares import obter_todos_ativos, buscar_ativo_por_simbolo

# Configuração da página
st.set_page_config(
    page_title="Simulador de Renda Variável",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .positive {
        color: #28a745;
        font-weight: bold;
    }
    .negative {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar simulador
@st.cache_resource
def get_simulador():
    return SimuladorRendaVariavel()

@st.cache_resource
def get_analisador():
    simulador = get_simulador()
    return AnalisadorHistorico(simulador)

def main():
    # Título principal
    st.markdown('<h1 class="main-header">📈 Simulador de Renda Variável</h1>', unsafe_allow_html=True)
    st.markdown("### Simule investimentos em Ações, BDRs e ETFs")
    
    # Sidebar para configurações
    st.sidebar.header("⚙️ Configurações do Investimento")
    
    # Seleção do tipo de ativo
    tipo_ativo = st.sidebar.selectbox(
        "Tipo de Ativo:",
        ["Ações Americanas", "Ações Brasileiras", "BDRs", "ETFs Brasileiros", "ETFs Americanos"]
    )
    
    # Mapeamento de regiões
    region_map = {
        "Ações Americanas": "US",
        "Ações Brasileiras": "BR", 
        "BDRs": "US",
        "ETFs Brasileiros": "BR",
        "ETFs Americanos": "US"
    }
    
    # Obter lista completa de ativos
    todos_ativos = obter_todos_ativos()
    
    # Sugestões de símbolos por tipo
    simbolos_sugeridos = {
        "Ações Americanas": list(todos_ativos['acoes_americanas'].keys()),
        "Ações Brasileiras": list(todos_ativos['acoes_brasileiras'].keys()),
        "BDRs": list(todos_ativos['bdrs'].keys()),
        "ETFs Brasileiros": list(todos_ativos['etfs_brasileiros'].keys()),
        "ETFs Americanos": list(todos_ativos['etfs_americanos'].keys())
    }
    
    # Input do símbolo
    simbolo_sugerido = st.sidebar.selectbox(
        "Símbolos Sugeridos:",
        [""] + simbolos_sugeridos[tipo_ativo]
    )
    
    simbolo = st.sidebar.text_input(
        "Símbolo do Ativo:",
        value=simbolo_sugerido,
        help="Digite o símbolo do ativo (ex: AAPL, PETR4.SA)"
    )
    
    # Valor do investimento
    valor_investimento = st.sidebar.number_input(
        "Valor do Investimento (R$):",
        min_value=100.0,
        max_value=1000000.0,
        value=10000.0,
        step=1000.0
    )
    
    # Período de análise
    periodo_analise = st.sidebar.selectbox(
        "Período de Análise:",
        ["1mo", "3mo", "6mo", "1y", "2y", "5y"],
        index=3
    )
    
    # Seção de Dividendos e JCP
    st.sidebar.markdown("---")
    st.sidebar.header("💰 Dividendos e JCP")
    
    considerar_dividendos = st.sidebar.checkbox(
        "Considerar Dividendos/JCP",
        value=False,
        help="Incluir dividendos e juros sobre capital próprio no cálculo"
    )
    
    reinvestir_dividendos = st.sidebar.checkbox(
        "Reinvestir Dividendos/JCP",
        value=False,
        disabled=not considerar_dividendos,
        help="Reinvestir automaticamente os dividendos recebidos"
    )
    
    # Seção de Aportes Mensais
    st.sidebar.markdown("---")
    st.sidebar.header("📈 Aportes Mensais")
    
    aporte_mensal = st.sidebar.number_input(
        "Aporte Mensal (R$):",
        min_value=0.0,
        max_value=100000.0,
        value=0.0,
        step=100.0,
        help="Valor a ser investido mensalmente"
    )
    
    # Botão para simular
    if st.sidebar.button("🚀 Simular Investimento", type="primary"):
        if simbolo:
            simular_investimento(simbolo, valor_investimento, region_map[tipo_ativo], periodo_analise, 
                               considerar_dividendos, reinvestir_dividendos, aporte_mensal)
        else:
            st.error("Por favor, digite um símbolo válido!")
    
    # Seção de comparação
    st.sidebar.markdown("---")
    st.sidebar.header("📊 Comparação de Ativos")
    
    # Múltiplos símbolos para comparação
    simbolos_comparacao = st.sidebar.text_area(
        "Símbolos para Comparação:",
        help="Digite os símbolos separados por vírgula (ex: AAPL,GOOGL,MSFT)",
        placeholder="AAPL,GOOGL,MSFT"
    )
    
    if st.sidebar.button("📈 Comparar Ativos"):
        if simbolos_comparacao:
            comparar_ativos(simbolos_comparacao, periodo_analise)

    if not st.session_state.get("simulacao_executada", False):
        mostrar_informacoes_iniciais()

def simular_investimento(simbolo, valor_investimento, region, periodo, considerar_dividendos=False, reinvestir_dividendos=False, aporte_mensal=0):
    """
    Executa a simulação de investimento
    """
    simulador = get_simulador()
    analisador = get_analisador()
    
    with st.spinner(f'Simulando investimento em {simbolo}...'):
        # Executar simulação
        resultado = simulador.simular_investimento(simbolo, valor_investimento, data_compra=None, region=region, periodo=periodo,
                                                 considerar_dividendos=considerar_dividendos, 
                                                 reinvestir_dividendos=reinvestir_dividendos, 
                                                 aporte_mensal=aporte_mensal)        
        if resultado is None:
            st.error(f"Não foi possível obter dados para {simbolo}. Verifique se o símbolo está correto.")
            return
        
        # Marcar que a simulação foi executada
        st.session_state['simulacao_executada'] = True
        
        # Exibir resultados
        exibir_resultados(resultado, simbolo, periodo, analisador, region, 
                         considerar_dividendos, reinvestir_dividendos, aporte_mensal)

def exibir_resultados(resultado, simbolo, periodo, analisador, region, considerar_dividendos=False, reinvestir_dividendos=False, aporte_mensal=0):
    """
    Exibe os resultados da simulação
    """
    rent = resultado['rentabilidade']
    meta = resultado['meta']
    
    # Informações do ativo
    st.subheader(f"📊 Resultados para {simbolo}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Empresa",
            meta.get('longName', simbolo),
            delta=f"Bolsa: {meta.get('exchangeName', 'N/A')}"
        )
    
    with col2:
        st.metric(
            "Preço Atual",
            f"${rent['preco_atual']:.2f}",
            delta=f"Compra: ${rent['preco_compra']:.2f}"
        )
    
    with col3:
        st.metric(
            "Moeda",
            meta.get('currency', 'USD'),
            delta=f"Volume: {meta.get('regularMarketVolume', 0):,}"
        )
    
    # Métricas de rentabilidade
    st.subheader("💰 Análise de Rentabilidade")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Valor Investido",
            f"R$ {rent['valor_inicial']:,.2f}"
        )
    
    with col2:
        st.metric(
            "Valor Atual",
            f"R$ {rent['valor_atual']:,.2f}"
        )
    
    with col3:
        delta_color = "normal" if rent['rentabilidade_absoluta'] >= 0 else "inverse"
        st.metric(
            "Ganho/Perda",
            f"R$ {rent['rentabilidade_absoluta']:,.2f}",
            delta=f"{rent['rentabilidade_percentual']:.2f}%",
            delta_color=delta_color
        )
    
    with col4:
        if aporte_mensal > 0 and 'valor_total_aportado' in rent:
            st.metric(
                "Total Aportado",
                f"R$ {rent['valor_total_aportado']:,.2f}",
                delta=f"Aportes: R$ {rent['valor_total_aportado'] - rent['valor_inicial']:,.2f}"
            )
        else:
            st.metric(
                "Quantidade de Ações",
                f"{rent['quantidade_acoes']:.2f}",
                delta=f"Período: {rent['periodo_dias']} dias"
            )
    
    # Informações sobre dividendos (se aplicável)
    if considerar_dividendos and 'dividendos_recebidos' in rent and rent['dividendos_recebidos'] > 0:
        st.subheader("💰 Dividendos e JCP")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Dividendos/JCP Recebidos",
                f"R$ {rent['dividendos_recebidos']:,.2f}"
            )
        
        with col2:
            dividend_yield = (rent['dividendos_recebidos'] / rent['valor_inicial']) * 100
            st.metric(
                "Dividend Yield",
                f"{dividend_yield:.2f}%"
            )
        
        with col3:
            if reinvestir_dividendos:
                st.metric(
                    "Status",
                    "Reinvestido",
                    delta="Dividendos reinvestidos automaticamente"
                )
            else:
                st.metric(
                    "Status",
                    "Recebido em Dinheiro",
                    delta="Dividendos mantidos como caixa"
                )
    
    # Métricas de risco
    st.subheader("⚠️ Análise de Risco")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        volatilidade = resultado.get('volatilidade', 0)
        st.metric(
            "Volatilidade Anual",
            f"{volatilidade:.2f}%"
        )
    
    with col2:
        sharpe = resultado.get('sharpe_ratio', 0)
        st.metric(
            "Sharpe Ratio",
            f"{sharpe:.2f}"
        )
    
    with col3:
        drawdown = resultado.get('drawdown_maximo', 0)
        st.metric(
            "Drawdown Máximo",
            f"{drawdown:.2f}%"
        )
    
    # Gráficos
    st.subheader("📈 Análise Gráfica")
    
    tab1, tab2, tab3 = st.tabs(["Evolução de Preços", "Candlestick", "Volatilidade"])
    
    with tab1:
        fig_precos = analisador.criar_grafico_precos(simbolo, region, periodo)
        if fig_precos:
            st.plotly_chart(fig_precos, use_container_width=True)
    
    with tab2:
        fig_candle = analisador.criar_grafico_candlestick(simbolo, region, periodo)
        if fig_candle:
            st.plotly_chart(fig_candle, use_container_width=True)
    
    with tab3:
        fig_vol = analisador.criar_grafico_volatilidade(simbolo, region, periodo)
        if fig_vol:
            st.plotly_chart(fig_vol, use_container_width=True)

def comparar_ativos(simbolos_str, periodo):
    """
    Compara múltiplos ativos
    """
    analisador = get_analisador()
    
    # Processar símbolos
    simbolos = [s.strip().upper() for s in simbolos_str.split(',') if s.strip()]
    
    if len(simbolos) < 2:
        st.error("Digite pelo menos 2 símbolos para comparação!")
        return
    
    # Determinar região automaticamente
    symbols_regions = []
    for simbolo in simbolos:
        if '.SA' in simbolo:
            symbols_regions.append((simbolo, 'BR'))
        else:
            symbols_regions.append((simbolo, 'US'))
    
    with st.spinner('Comparando ativos...'):
        # Gráfico de comparação
        fig_comp = analisador.comparar_ativos(symbols_regions, periodo)
        
        if fig_comp:
            st.subheader("📊 Comparação de Ativos")
            st.plotly_chart(fig_comp, use_container_width=True)
        
        # Matriz de correlação
        fig_corr, matriz_corr = analisador.calcular_correlacao(symbols_regions, periodo)
        
        if fig_corr:
            st.subheader("🔗 Matriz de Correlação")
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.plotly_chart(fig_corr, use_container_width=True)
            
            with col2:
                st.dataframe(matriz_corr.round(3))

def mostrar_informacoes_iniciais():
    """
    Mostra informações iniciais da aplicação
    """
    st.markdown("""
    ## 🎯 Como usar este simulador:
    
    1. **Selecione o tipo de ativo** na barra lateral
    2. **Digite o símbolo** do ativo que deseja analisar
    3. **Defina o valor** do investimento inicial
    4. **Escolha o período** de análise
    5. **Configure dividendos/JCP** (opcional)
    6. **Defina aportes mensais** (opcional)
    7. **Clique em "Simular Investimento"**
    
    ## 📋 Tipos de ativos suportados:
    
    - **Ações Americanas**: AAPL, GOOGL, MSFT, TSLA, etc.
    - **Ações Brasileiras**: PETR4.SA, VALE3.SA, ITUB4.SA, etc.
    - **BDRs**: AAPL34.SA, GOGL34.SA, MSFT34.SA, etc.
    - **ETFs**: BOVA11.SA, SPY, QQQ, etc.
    
    ## 📊 Métricas calculadas:
    
    - **Rentabilidade**: Ganho/perda absoluta e percentual
    - **Dividendos/JCP**: Proventos recebidos e reinvestidos
    - **Aportes Mensais**: Simulação de investimentos regulares
    - **Volatilidade**: Risco do investimento
    - **Sharpe Ratio**: Relação risco-retorno
    - **Drawdown Máximo**: Maior perda do período
    
    ## 💰 Funcionalidades Avançadas:
    
    ### **Dividendos e JCP**
    - ✅ Cálculo automático de dividendos e juros sobre capital próprio
    - ✅ Opção de reinvestimento automático dos proventos
    - ✅ Análise do dividend yield
    
    ### **Aportes Mensais**
    - ✅ Simulação de investimentos mensais regulares
    - ✅ Compra automática de ações com aportes
    - ✅ Cálculo do valor total aportado
    
    ## ⚠️ Importante:
    
    Este simulador utiliza dados históricos reais e serve apenas para fins educacionais. 
    Não constitui recomendação de investimento.
    """)

if __name__ == "__main__":
    main()

