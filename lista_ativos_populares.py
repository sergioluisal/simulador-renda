#!/usr/bin/env python3
"""
Lista de Ativos Populares para o Simulador de Renda Variável
Contém ações, BDRs e ETFs americanos e brasileiros mais negociados
"""

# Ações Americanas Populares
ACOES_AMERICANAS = {
    # Tecnologia
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Alphabet Inc. (Google)',
    'AMZN': 'Amazon.com Inc.',
    'META': 'Meta Platforms Inc. (Facebook)',
    'TSLA': 'Tesla Inc.',
    'NVDA': 'NVIDIA Corporation',
    'NFLX': 'Netflix Inc.',
    'ADBE': 'Adobe Inc.',
    'CRM': 'Salesforce Inc.',
    'ORCL': 'Oracle Corporation',
    'IBM': 'International Business Machines',
    
    # Financeiro
    'JPM': 'JPMorgan Chase & Co.',
    'BAC': 'Bank of America Corp.',
    'WFC': 'Wells Fargo & Company',
    'GS': 'Goldman Sachs Group Inc.',
    'MS': 'Morgan Stanley',
    'C': 'Citigroup Inc.',
    'V': 'Visa Inc.',
    'MA': 'Mastercard Inc.',
    'PYPL': 'PayPal Holdings Inc.',
    
    # Saúde
    'JNJ': 'Johnson & Johnson',
    'PFE': 'Pfizer Inc.',
    'UNH': 'UnitedHealth Group Inc.',
    'ABBV': 'AbbVie Inc.',
    'MRK': 'Merck & Co. Inc.',
    'TMO': 'Thermo Fisher Scientific',
    
    # Consumo
    'KO': 'The Coca-Cola Company',
    'PEP': 'PepsiCo Inc.',
    'WMT': 'Walmart Inc.',
    'PG': 'Procter & Gamble Co.',
    'NKE': 'Nike Inc.',
    'MCD': 'McDonald\'s Corporation',
    'SBUX': 'Starbucks Corporation',
    
    # Energia
    'XOM': 'Exxon Mobil Corporation',
    'CVX': 'Chevron Corporation',
    'COP': 'ConocoPhillips',
    
    # Industrial
    'BA': 'Boeing Company',
    'CAT': 'Caterpillar Inc.',
    'GE': 'General Electric Company',
    'MMM': '3M Company',
    
    # Telecom
    'T': 'AT&T Inc.',
    'VZ': 'Verizon Communications Inc.',
}

# Ações Brasileiras Populares
ACOES_BRASILEIRAS = {
    # Petróleo e Gás
    'PETR4.SA': 'Petrobras PN',
    'PETR3.SA': 'Petrobras ON',
    'PRIO3.SA': 'PetroRio ON',
    'RRRP3.SA': '3R Petroleum ON',
    
    # Mineração
    'VALE3.SA': 'Vale ON',
    'CSNA3.SA': 'CSN ON',
    'USIM5.SA': 'Usiminas PNA',
    'GGBR4.SA': 'Gerdau PN',
    
    # Bancos
    'ITUB4.SA': 'Itaú Unibanco PN',
    'BBDC4.SA': 'Bradesco PN',
    'BBAS3.SA': 'Banco do Brasil ON',
    'SANB11.SA': 'Santander Units',
    'BPAC11.SA': 'BTG Pactual Units',
    
    # Varejo
    'MGLU3.SA': 'Magazine Luiza ON',
    'LREN3.SA': 'Lojas Renner ON',
    'AMER3.SA': 'Americanas ON',
    'VIIA3.SA': 'Via ON',
    'PCAR3.SA': 'P.Açúcar-CBD ON',
    
    # Bebidas
    'ABEV3.SA': 'Ambev ON',
    'COCA34.SA': 'Coca-Cola BDR',
    
    # Alimentação
    'JBSS3.SA': 'JBS ON',
    'BEEF3.SA': 'Minerva ON',
    'BRFS3.SA': 'BRF ON',
    
    # Telecomunicações
    'VIVT3.SA': 'Vivo ON',
    'TIMS3.SA': 'TIM ON',
    
    # Energia Elétrica
    'ELET3.SA': 'Eletrobras ON',
    'ELET6.SA': 'Eletrobras PNB',
    'CPFE3.SA': 'CPFL Energia ON',
    'ENBR3.SA': 'EDP Brasil ON',
    
    # Papel e Celulose
    'SUZB3.SA': 'Suzano ON',
    'KLBN11.SA': 'Klabin Units',
    
    # Siderurgia
    'GOAU4.SA': 'Gerdau Metalúrgica PN',
    'USIM5.SA': 'Usiminas PNA',
    
    # Construção
    'MRVE3.SA': 'MRV Engenharia ON',
    'CYRE3.SA': 'Cyrela Realty ON',
    'EZTC3.SA': 'EZ Tec ON',
}

# BDRs Populares (Brazilian Depositary Receipts)
BDRS_POPULARES = {
    # Tecnologia
    'AAPL34.SA': 'Apple BDR',
    'MSFT34.SA': 'Microsoft BDR',
    'GOGL34.SA': 'Google BDR',
    'AMZO34.SA': 'Amazon BDR',
    'META34.SA': 'Meta BDR',
    'TSLA34.SA': 'Tesla BDR',
    'NVDC34.SA': 'NVIDIA BDR',
    'NFLX34.SA': 'Netflix BDR',
    
    # Financeiro
    'JPMC34.SA': 'JPMorgan BDR',
    'BOAC34.SA': 'Bank of America BDR',
    'VISA34.SA': 'Visa BDR',
    'MSTR34.SA': 'Mastercard BDR',
    'PYPL34.SA': 'PayPal BDR',
    
    # Saúde
    'JNJB34.SA': 'Johnson & Johnson BDR',
    'PFIZ34.SA': 'Pfizer BDR',
    
    # Consumo
    'COCA34.SA': 'Coca-Cola BDR',
    'PEPB34.SA': 'PepsiCo BDR',
    'WALM34.SA': 'Walmart BDR',
    'NIKE34.SA': 'Nike BDR',
    'MCDC34.SA': 'McDonald\'s BDR',
    
    # Energia
    'XPBR31.SA': 'Exxon Mobil BDR',
    
    # Outros
    'BERK34.SA': 'Berkshire Hathaway BDR',
    'DISB34.SA': 'Disney BDR',
}

# ETFs Brasileiros
ETFS_BRASILEIROS = {
    # Índice Bovespa
    'BOVA11.SA': 'iShares Bovespa ETF',
    'BOVV11.SA': 'Vanguard FTSE Brazil ETF',
    
    # Small Caps
    'SMAL11.SA': 'iShares MSCI Brazil Small-Cap ETF',
    'SMLL11.SA': 'SPDR S&P 600 Small Cap ETF',
    
    # Setoriais
    'FIND11.SA': 'iShares MSCI Brazil Financials ETF',
    'MATB11.SA': 'iShares MSCI Brazil Materials ETF',
    'UTIL11.SA': 'iShares MSCI Brazil Utilities ETF',
    
    # Internacional
    'IVVB11.SA': 'iShares Core S&P 500 ETF',
    'SPXI11.SA': 'SPDR S&P 500 ETF Trust',
    
    # Dividendos
    'DIVO11.SA': 'iShares MSCI Brazil Dividend ETF',
    'XFIX11.SA': 'iShares Core Fixed Income ETF',
    
    # Imobiliário
    'IFIX11.SA': 'iShares MSCI Brazil Real Estate ETF',
    
    # Commodities
    'GOLD11.SA': 'iShares Gold Trust ETF',
    'BCOM11.SA': 'iShares Commodities Select Strategy ETF',
}

# ETFs Americanos
ETFS_AMERICANOS = {
    # Índices Amplos
    'SPY': 'SPDR S&P 500 ETF Trust',
    'VOO': 'Vanguard S&P 500 ETF',
    'IVV': 'iShares Core S&P 500 ETF',
    'VTI': 'Vanguard Total Stock Market ETF',
    'ITOT': 'iShares Core S&P Total US Stock Market ETF',
    
    # Tecnologia
    'QQQ': 'Invesco QQQ Trust ETF (Nasdaq)',
    'XLK': 'Technology Select Sector SPDR Fund',
    'VGT': 'Vanguard Information Technology ETF',
    'FTEC': 'Fidelity MSCI Information Technology ETF',
    
    # Small Cap
    'IWM': 'iShares Russell 2000 ETF',
    'VB': 'Vanguard Small-Cap ETF',
    'VTWO': 'Vanguard Russell 2000 ETF',
    
    # Internacional
    'VEA': 'Vanguard FTSE Developed Markets ETF',
    'VWO': 'Vanguard FTSE Emerging Markets ETF',
    'IEFA': 'iShares Core MSCI EAFE IMI Index ETF',
    'EEM': 'iShares MSCI Emerging Markets ETF',
    
    # Setoriais
    'XLF': 'Financial Select Sector SPDR Fund',
    'XLE': 'Energy Select Sector SPDR Fund',
    'XLV': 'Health Care Select Sector SPDR Fund',
    'XLI': 'Industrial Select Sector SPDR Fund',
    'XLP': 'Consumer Staples Select Sector SPDR Fund',
    'XLY': 'Consumer Discretionary Select Sector SPDR Fund',
    'XLU': 'Utilities Select Sector SPDR Fund',
    'XLB': 'Materials Select Sector SPDR Fund',
    'XLRE': 'Real Estate Select Sector SPDR Fund',
    
    # Dividendos
    'VYM': 'Vanguard High Dividend Yield ETF',
    'SCHD': 'Schwab US Dividend Equity ETF',
    'DVY': 'iShares Select Dividend ETF',
    'HDV': 'iShares Core High Dividend ETF',
    
    # Crescimento
    'VUG': 'Vanguard Growth ETF',
    'IVW': 'iShares Core S&P U.S. Growth ETF',
    
    # Valor
    'VTV': 'Vanguard Value ETF',
    'IVE': 'iShares Core S&P U.S. Value ETF',
    
    # Commodities
    'GLD': 'SPDR Gold Shares',
    'SLV': 'iShares Silver Trust',
    'USO': 'United States Oil Fund',
    'DBA': 'Invesco DB Agriculture Fund',
    
    # Renda Fixa
    'BND': 'Vanguard Total Bond Market ETF',
    'AGG': 'iShares Core U.S. Aggregate Bond ETF',
    'TLT': 'iShares 20+ Year Treasury Bond ETF',
    'HYG': 'iShares iBoxx $ High Yield Corporate Bond ETF',
}

# Função para obter todos os ativos
def obter_todos_ativos():
    """
    Retorna um dicionário com todos os ativos organizados por categoria
    """
    return {
        'acoes_americanas': ACOES_AMERICANAS,
        'acoes_brasileiras': ACOES_BRASILEIRAS,
        'bdrs': BDRS_POPULARES,
        'etfs_brasileiros': ETFS_BRASILEIROS,
        'etfs_americanos': ETFS_AMERICANOS
    }

# Função para buscar ativo por símbolo
def buscar_ativo_por_simbolo(simbolo):
    """
    Busca um ativo em todas as categorias pelo símbolo
    """
    simbolo = simbolo.upper()
    todos_ativos = obter_todos_ativos()
    
    for categoria, ativos in todos_ativos.items():
        if simbolo in ativos:
            return {
                'simbolo': simbolo,
                'nome': ativos[simbolo],
                'categoria': categoria
            }
    
    return None

# Função para obter sugestões por categoria
def obter_sugestoes_por_categoria(categoria):
    """
    Retorna lista de símbolos para uma categoria específica
    """
    todos_ativos = obter_todos_ativos()
    return list(todos_ativos.get(categoria, {}).keys())

if __name__ == "__main__":
    # Exemplo de uso
    print("=== LISTA DE ATIVOS POPULARES ===\n")
    
    # Mostrar algumas estatísticas
    todos_ativos = obter_todos_ativos()
    for categoria, ativos in todos_ativos.items():
        print(f"{categoria.replace('_', ' ').title()}: {len(ativos)} ativos")
    
    print(f"\nTotal de ativos: {sum(len(ativos) for ativos in todos_ativos.values())}")
    
    # Exemplo de busca
    print("\n=== EXEMPLO DE BUSCA ===")
    resultado = buscar_ativo_por_simbolo('AAPL')
    if resultado:
        print(f"Símbolo: {resultado['simbolo']}")
        print(f"Nome: {resultado['nome']}")
        print(f"Categoria: {resultado['categoria']}")

