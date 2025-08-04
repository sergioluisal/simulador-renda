#!/usr/bin/env python3
"""
Simulador de Investimentos em Renda Variável
Suporta ações, BDRs e ETFs com dados do Yahoo Finance
Inclui funcionalidades de dividendos e aportes mensais
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class SimuladorRendaVariavel:
    def __init__(self):
        pass
        
    def buscar_dados_ativo(self, symbol, region='US', interval='1d', range_period='1y'):
        """
        Busca dados históricos de um ativo
        """
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(period=range_period, interval=interval)
            
            if df.empty:
                return None, None

            # Renomear colunas para consistência
            df.columns = [col.lower() for col in df.columns]
            df.index.name = 'date'

            # Obter metadados
            info = ticker.info
            meta = {
                'symbol': symbol,
                'longName': info.get('longName', symbol),
                'exchangeName': info.get('exchangeName', 'N/A'),
                'currency': info.get('currency', 'USD'),
                'regularMarketPrice': info.get('regularMarketPrice', df['close'].iloc[-1]),
                'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh', 'N/A'),
                'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow', 'N/A'),
                'regularMarketVolume': info.get('regularMarketVolume', 'N/A'),
                'regularMarketDayHigh': info.get('regularMarketDayHigh', 'N/A'),
                'regularMarketDayLow': info.get('regularMarketDayLow', 'N/A'),
            }
            
            return df, meta
                
        except Exception as e:
            print(f"Erro ao buscar dados para {symbol}: {str(e)}")
            return None, None
    
    def buscar_dividendos(self, symbol, start_date=None, end_date=None):
        """
        Busca dados de dividendos de um ativo.
        """
        try:
            ticker = yf.Ticker(symbol)
            dividends = ticker.dividends
            if start_date and end_date:
                dividends = dividends[(dividends.index >= start_date) & (dividends.index <= end_date)]
            return dividends
        except Exception as e:
            print(f"Erro ao buscar dividendos para {symbol}: {str(e)}")
            return pd.Series()
    
    def calcular_rentabilidade(self, df, valor_inicial, data_compra=None, considerar_dividendos=False, reinvestir_dividendos=False, symbol=None):
        """
        Calcula a rentabilidade de um investimento
        """
        if df is None or df.empty:
            return None
            
        if data_compra is None:
            data_compra = df.index[0]
        
        # Encontrar preço de compra mais próximo da data
        preco_compra = df.loc[df.index >= data_compra, 'close'].iloc[0]
        
        # Calcular quantidade de ações inicial
        quantidade_acoes = valor_inicial / preco_compra
        
        # Se considerar dividendos
        dividendos_recebidos = 0
        if considerar_dividendos and symbol:
            dividendos_df = self.buscar_dividendos(symbol, start_date=data_compra, end_date=df.index[-1])
            if not dividendos_df.empty:
                for index, dividendo_por_acao in dividendos_df.items():
                    
                    # Se reinvestir, comprar mais ações
                    if reinvestir_dividendos:
                        # Preço da ação na data do dividendo
                        preco_na_data_dividendo = df.loc[df.index >= index, 'close'].iloc[0]
                        acoes_compradas = (quantidade_acoes * dividendo_por_acao) / preco_na_data_dividendo
                        quantidade_acoes += acoes_compradas
                    else:
                        # Apenas somar os dividendos recebidos
                        dividendos_recebidos += quantidade_acoes * dividendo_por_acao

        preco_atual = df['close'].iloc[-1]
        
        # Valor atual do investimento (incluindo ações compradas com reinvestimento)
        valor_atual_ativos = quantidade_acoes * preco_atual
        valor_atual = valor_atual_ativos + dividendos_recebidos
        
        # Rentabilidade
        rentabilidade_absoluta = valor_atual - valor_inicial
        rentabilidade_percentual = (valor_atual / valor_inicial - 1) * 100
        
        # Período do investimento
        periodo_dias = (df.index[-1] - data_compra).days
        
        return {
            'valor_inicial': valor_inicial,
            'preco_compra': preco_compra,
            'preco_atual': preco_atual,
            'quantidade_acoes': quantidade_acoes,
            'valor_atual': valor_atual,
            'rentabilidade_absoluta': rentabilidade_absoluta,
            'rentabilidade_percentual': rentabilidade_percentual,
            'periodo_dias': periodo_dias,
            'data_compra': data_compra,
            'data_atual': df.index[-1],
            'dividendos_recebidos': dividendos_recebidos
        }
    
    def calcular_volatilidade(self, df):
        """
        Calcula a volatilidade do ativo
        """
        if df is None or df.empty:
            return None
            
        # Calcular retornos diários
        retornos = df['close'].pct_change().dropna()
        
        # Volatilidade anualizada (252 dias úteis)
        volatilidade_anual = retornos.std() * np.sqrt(252) * 100
        
        return volatilidade_anual
    
    def calcular_sharpe_ratio(self, df, taxa_livre_risco=0.05):
        """
        Calcula o Sharpe Ratio
        """
        if df is None or df.empty:
            return None
            
        # Calcular retornos diários
        retornos = df['close'].pct_change().dropna()
        
        # Retorno médio anualizado
        retorno_medio_anual = retornos.mean() * 252
        
        # Volatilidade anualizada
        volatilidade_anual = retornos.std() * np.sqrt(252)
        
        # Sharpe Ratio
        sharpe_ratio = (retorno_medio_anual - taxa_livre_risco) / volatilidade_anual
        
        return sharpe_ratio
    
    def calcular_drawdown_maximo(self, df):
        """
        Calcula o drawdown máximo
        """
        if df is None or df.empty:
            return None
            
        # Calcular picos cumulativos
        picos_cumulativos = df['close'].cummax()
        
        # Calcular drawdown
        drawdown = (df['close'] - picos_cumulativos) / picos_cumulativos * 100
        
        # Drawdown máximo
        drawdown_maximo = drawdown.min()
        
        return drawdown_maximo
    
    def simular_investimento(self, symbol, valor_inicial, data_compra=None, region='US', periodo='1y', considerar_dividendos=False, reinvestir_dividendos=False, aporte_mensal=0):
        """
        Simula um investimento completo
        """
        print(f"Simulando investimento em {symbol}...")
        
        # Buscar dados
        df, meta = self.buscar_dados_ativo(symbol, region=region, range_period=periodo)
        
        if df is None:
            return None
        
        # Definir data de compra se não fornecida
        if data_compra is None:
            data_compra = df.index[0]
            
        # Se houver aporte mensal, simular ao longo do tempo
        if aporte_mensal > 0:
            # Criar um DataFrame para acompanhar a evolução do investimento
            evolucao_investimento = pd.DataFrame(columns=[
                'data', 'valor_investido', 'valor_atual_ativos', 'dividendos_acumulados', 'quantidade_acoes_acumulada'
            ])

            valor_total_investido = valor_inicial
            quantidade_acoes_acumulada = valor_inicial / df.loc[df.index >= data_compra, 'close'].iloc[0]
            dividendos_acumulados = 0

            # Iterar mês a mês
            data_atual_simulacao = data_compra
            while data_atual_simulacao <= df.index[-1]:
                # Adicionar aporte mensal no início do mês
                if data_atual_simulacao != data_compra:
                    valor_total_investido += aporte_mensal
                    # Comprar ações com o aporte mensal ao preço do início do mês
                    preco_no_mes = df.loc[df.index >= data_atual_simulacao, 'close'].iloc[0]
                    if preco_no_mes > 0:
                        quantidade_acoes_acumulada += aporte_mensal / preco_no_mes

                # Calcular dividendos para o período
                if considerar_dividendos and symbol:
                    # Buscar dividendos apenas para o mês atual
                    proximo_mes = (data_atual_simulacao.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
                    dividendos_do_mes = self.buscar_dividendos(symbol, start_date=data_atual_simulacao, end_date=proximo_mes)
                    
                    if not dividendos_do_mes.empty:
                        for index, dividendo_por_acao in dividendos_do_mes.items():
                            if reinvestir_dividendos:
                                preco_na_data_dividendo = df.loc[df.index >= index, 'close'].iloc[0]
                                if preco_na_data_dividendo > 0:
                                    acoes_compradas_com_dividendo = (quantidade_acoes_acumulada * dividendo_por_acao) / preco_na_data_dividendo
                                    quantidade_acoes_acumulada += acoes_compradas_com_dividendo
                            else:
                                dividendos_acumulados += quantidade_acoes_acumulada * dividendo_por_acao

                # Valor atual dos ativos no final do mês
                preco_final_mes = df.loc[df.index >= data_atual_simulacao, 'close'].iloc[0]
                valor_atual_ativos = quantidade_acoes_acumulada * preco_final_mes

                evolucao_investimento = pd.concat([
                    evolucao_investimento,
                    pd.DataFrame([{
                        'data': data_atual_simulacao,
                        'valor_investido': valor_total_investido,
                        'valor_atual_ativos': valor_atual_ativos,
                        'dividendos_acumulados': dividendos_acumulados,
                        'quantidade_acoes_acumulada': quantidade_acoes_acumulada
                    }])
                ], ignore_index=True)

                # Avançar para o próximo mês
                data_atual_simulacao = (data_atual_simulacao.replace(day=1) + timedelta(days=32)).replace(day=1)
                if data_atual_simulacao > df.index[-1]:
                    break

            # Usar o último valor da simulação para os resultados finais
            valor_final_total = evolucao_investimento['valor_atual_ativos'].iloc[-1] + evolucao_investimento['dividendos_acumulados'].iloc[-1]
            rentabilidade_absoluta = valor_final_total - valor_inicial
            rentabilidade_percentual = (valor_final_total / valor_inicial - 1) * 100
            
            # Período do investimento
            periodo_dias = (df.index[-1] - data_compra).days

            rentabilidade = {
                'valor_inicial': valor_inicial,
                'preco_compra': df.loc[df.index >= data_compra, 'close'].iloc[0],
                'preco_atual': df['close'].iloc[-1],
                'quantidade_acoes': quantidade_acoes_acumulada,
                'valor_atual': valor_final_total,
                'rentabilidade_absoluta': rentabilidade_absoluta,
                'rentabilidade_percentual': rentabilidade_percentual,
                'periodo_dias': periodo_dias,
                'data_compra': data_compra,
                'data_atual': df.index[-1],
                'dividendos_recebidos': evolucao_investimento['dividendos_acumulados'].iloc[-1],
                'valor_total_aportado': valor_total_investido
            }

        else:
            # Lógica existente para simulação sem aporte mensal
            rentabilidade = self.calcular_rentabilidade(df, valor_inicial, data_compra, considerar_dividendos, reinvestir_dividendos, symbol)

        volatilidade = self.calcular_volatilidade(df)
        sharpe = self.calcular_sharpe_ratio(df)
        drawdown_max = self.calcular_drawdown_maximo(df)
        
        resultado = {
            'symbol': symbol,
            'meta': meta,
            'dados_historicos': df,
            'rentabilidade': rentabilidade,
            'volatilidade': volatilidade,
            'sharpe_ratio': sharpe,
            'drawdown_maximo': drawdown_max
        }
        
        return resultado

class AnalisadorHistorico:
    def __init__(self, simulador):
        self.simulador = simulador
    
    def criar_grafico_precos(self, symbol, region='US', periodo='1y'):
        """
        Cria gráfico de evolução de preços
        """
        df, meta = self.simulador.buscar_dados_ativo(symbol, region=region, range_period=periodo)
        
        if df is None:
            return None
            
        fig = go.Figure()
        
        # Adicionar linha de preços
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['close'],
            mode='lines',
            name=f'{symbol} - Preço de Fechamento',
            line=dict(color='blue', width=2)
        ))
        
        # Configurar layout
        fig.update_layout(
            title=f'Evolução do Preço - {symbol}',
            xaxis_title='Data',
            yaxis_title='Preço (USD)',
            hovermode='x unified',
            showlegend=True
        )
        
        return fig
    
    def criar_grafico_candlestick(self, symbol, region='US', periodo='3mo'):
        """
        Cria gráfico de candlestick
        """
        df, meta = self.simulador.buscar_dados_ativo(symbol, region=region, range_period=periodo)
        
        if df is None:
            return None
            
        fig = go.Figure(data=go.Candlestick(
            x=df.index,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name=symbol
        ))
        
        fig.update_layout(
            title=f'Gráfico Candlestick - {symbol}',
            xaxis_title='Data',
            yaxis_title='Preço (USD)',
            xaxis_rangeslider_visible=False
        )
        
        return fig
    
    def comparar_ativos(self, symbols_regions, periodo='1y'):
        """
        Compara múltiplos ativos
        """
        fig = go.Figure()
        
        for symbol, region in symbols_regions:
            df, meta = self.simulador.buscar_dados_ativo(symbol, region=region, range_period=periodo)
            
            if df is not None:
                # Normalizar preços (base 100)
                precos_normalizados = (df['close'] / df['close'].iloc[0]) * 100
                
                fig.add_trace(go.Scatter(
                    x=df.index,
                    y=precos_normalizados,
                    mode='lines',
                    name=symbol,
                    line=dict(width=2)
                ))
        
        fig.update_layout(
            title='Comparação de Ativos (Base 100)',
            xaxis_title='Data',
            yaxis_title='Valor Normalizado',
            hovermode='x unified',
            showlegend=True
        )
        
        return fig
    
    def criar_grafico_volatilidade(self, symbol, region='US', periodo='1y'):
        """
        Cria gráfico de volatilidade móvel
        """
        df, meta = self.simulador.buscar_dados_ativo(symbol, region=region, range_period=periodo)
        
        if df is None:
            return None
            
        # Calcular retornos diários
        retornos = df['close'].pct_change().dropna()
        
        # Volatilidade móvel de 30 dias
        volatilidade_movel = retornos.rolling(window=30).std() * np.sqrt(252) * 100
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=volatilidade_movel.index,
            y=volatilidade_movel,
            mode='lines',
            name=f'Volatilidade 30d - {symbol}',
            line=dict(color='red', width=2)
        ))
        
        fig.update_layout(
            title=f'Volatilidade Móvel (30 dias) - {symbol}',
            xaxis_title='Data',
            yaxis_title='Volatilidade Anualizada (%)',
            hovermode='x unified'
        )
        
        return fig
    
    def calcular_correlacao(self, symbols_regions, periodo='1y'):
        """
        Calcula matriz de correlação entre ativos
        """
        dados_correlacao = {}
        
        for symbol, region in symbols_regions:
            df, meta = self.simulador.buscar_dados_ativo(symbol, region=region, range_period=periodo)
            
            if df is not None:
                retornos = df['close'].pct_change().dropna()
                dados_correlacao[symbol] = retornos
        
        if len(dados_correlacao) < 2:
            return None, None
            
        # Criar DataFrame com todos os retornos
        df_correlacao = pd.DataFrame(dados_correlacao)
        
        # Calcular matriz de correlação
        matriz_correlacao = df_correlacao.corr()
        
        # Criar heatmap
        fig = px.imshow(
            matriz_correlacao,
            text_auto=True,
            aspect="auto",
            title="Matriz de Correlação entre Ativos",
            color_continuous_scale='RdBu_r'
        )
        
        return fig, matriz_correlacao

def exemplo_uso():
    """
    Exemplo de uso do simulador com funcionalidades avançadas
    """
    simulador = SimuladorRendaVariavel()
    
    # Exemplos de ativos
    ativos = [
        {'symbol': 'AAPL', 'region': 'US', 'nome': 'Apple Inc.'},
        {'symbol': 'PETR4.SA', 'region': 'BR', 'nome': 'Petrobras'},
        {'symbol': 'BOVA11.SA', 'region': 'BR', 'nome': 'ETF Bovespa'},
    ]
    
    valor_investimento = 10000  # R$ 10.000
    
    print("=== SIMULADOR DE RENDA VARIÁVEL AVANÇADO ===\n")
    
    for ativo in ativos:
        # Simulação com dividendos e aportes mensais
        resultado = simulador.simular_investimento(
            ativo['symbol'], 
            valor_investimento, 
            region=ativo["region"],
            periodo="1y", # Adicionando período padrão para o exemplo
            considerar_dividendos=True,
            reinvestir_dividendos=True,
            aporte_mensal=500
        )
        
        if resultado:
            print(f"\n--- {ativo['nome']} ({ativo['symbol']}) ---")
            print("(Com dividendos reinvestidos e aportes mensais de R$ 500)")
            
            rent = resultado['rentabilidade']
            if rent:
                print(f"Valor Investido Inicial: R$ {rent['valor_inicial']:,.2f}")
                if 'valor_total_aportado' in rent:
                    print(f"Valor Total Aportado: R$ {rent['valor_total_aportado']:,.2f}")
                print(f"Preço de Compra: R$/${rent['preco_compra']:.2f}")
                print(f"Preço Atual: R$/${rent['preco_atual']:.2f}")
                print(f"Quantidade de Ações: {rent['quantidade_acoes']:.2f}")
                print(f"Valor Atual: R$ {rent['valor_atual']:,.2f}")
                print(f"Rentabilidade: R$ {rent['rentabilidade_absoluta']:,.2f} ({rent['rentabilidade_percentual']:.2f}%)")
                if 'dividendos_recebidos' in rent and rent['dividendos_recebidos'] > 0:
                    print(f"Dividendos Recebidos: R$ {rent['dividendos_recebidos']:,.2f}")
                print(f"Período: {rent['periodo_dias']} dias")
            
            if resultado['volatilidade']:
                print(f"Volatilidade Anual: {resultado['volatilidade']:.2f}%")
            
            if resultado['sharpe_ratio']:
                print(f"Sharpe Ratio: {resultado['sharpe_ratio']:.2f}")
            
            if resultado['drawdown_maximo']:
                print(f"Drawdown Máximo: {resultado['drawdown_maximo']:.2f}%")
        else:
            print(f"\nErro ao simular {ativo['nome']}")

if __name__ == "__main__":
    exemplo_uso()
