import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def gerar_grafico_soma_valor_estimado(dados):
    
    #Preparação Dados
    series_valorizacao_segmento = dados.groupby("Industry")["Valuation (USD)"].sum()
    series_valorizacao_segmento = (series_valorizacao_segmento / 1000000000000).round(3)
    series_valorizacao_segmento.sort_values(ascending= False, inplace=True)

    #Criação Gráfico
    fg, ax = plt.subplots()
    sns.barplot(x=series_valorizacao_segmento.index, y=series_valorizacao_segmento.values,
                ax=ax, palette='Blues')
    plt.title("Soma de Valor Estimado por Segmento", fontsize=12, fontweight='bold', pad=10)
    plt.ylabel("Valor (USD)")
    plt.xticks(rotation=45, ha='right')

    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width() / 2.,
            height + 0.01,                    
            f'${height:.2f}T',                 
            ha='center', va='bottom', fontsize=10
        )

    plt.tight_layout()
    plt.savefig("imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Soma_Valorizacao")
    plt.show()

def gerar_grafico_total_investimento_anual(dados):
    
    #Preparação Dados
    series_total_investimento = dados.groupby("Year Founded")["Investment Amount (USD)"].sum()
    series_total_investimento = (series_total_investimento / 1000000000000).round(3)

    #Criação Gráfico
    plt.plot(series_total_investimento, color="cyan")
    plt.title("Total de Investimento em Startup Por Ano", fontsize=12, fontweight='bold', pad=10)
    plt.ylabel("Valor (USD)")
    plt.savefig("imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Total_Investimento")
    plt.show()

def gerar_tabela_quantidade_startup_por_segmento(dados):
    
    #Preparação Dados
    quantidade = dados["Industry"].value_counts()
    porcentagem = (dados["Industry"].value_counts(normalize=True) * 100).round(2)

    df_quantidade_startup = pd.DataFrame({"Segmento": quantidade.index, "Quantidade": quantidade.values, "%": porcentagem.values})
    df_quantidade_startup.sort_values(by="Quantidade", ascending=False, inplace=True)
    df_quantidade_startup.loc[len(df_quantidade_startup)] = {"Segmento": "Total", "Quantidade": sum(quantidade.values), 
                                                            "%": sum(porcentagem.values)}

    # Criar a tabela
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')

    cell_colors = [['#1a3a5f', '#2a4a7f', '#4065a3']] * (len(df_quantidade_startup)-1) + [['#8a6bd1', '#8a6bd1', '#8a6bd1']]
    table = ax.table(
        cellText=df_quantidade_startup.values,
        colLabels=df_quantidade_startup.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5'] * 3,
        cellColours=cell_colors
    )

    #Destacar o Cabeçalho e Total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(df_quantidade_startup):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    # Estilo da tabela
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    plt.title("Quantidade de Startup por Segmento", fontsize=14, fontweight='bold', color='white', pad=20)
    plt.savefig("imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_QTD")
    plt.show()

def gerar_tabela_valor_investido_por_segmento(dados):
    
    #Preparação Dados
    soma_valores = dados.groupby("Industry")["Investment Amount (USD)"].sum()
    porcentagem = (soma_valores/soma_valores.sum()* 100)

    df_investimento_por_segmento = pd.DataFrame({"Segmento": soma_valores.index, "Valor Investido Total(USD)": soma_valores.values,
                                    "%": porcentagem.values})
    df_investimento_por_segmento["%"] = df_investimento_por_segmento["%"].round(2)
    df_investimento_por_segmento["Valor Investido Total(USD)"] = (df_investimento_por_segmento["Valor Investido Total(USD)"]/1000000000000).round(2)
    df_investimento_por_segmento.sort_values(by="Valor Investido Total(USD)", ascending=False, inplace=True)
    df_investimento_por_segmento.loc[len(df_investimento_por_segmento)] = {"Segmento": "Total", 
                                                                        "Valor Investido Total(USD)": 
                                                                        sum(df_investimento_por_segmento["Valor Investido Total(USD)"]),
                                                                        "%": sum(porcentagem)}

    #Criação tabela

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')

    cell_colors = [['#1a3a5f', '#2a4a7f', '#4065a3']] * (len(df_investimento_por_segmento)-1) + [['#8a6bd1', '#8a6bd1', '#8a6bd1']]

    table = ax.table(
        cellText=df_investimento_por_segmento.values,
        colLabels=df_investimento_por_segmento.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5'] * 3,
        cellColours = cell_colors
    )

    #Destacar o Cabeçalho e Total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(df_investimento_por_segmento):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    # Estilo da tabela
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    # Título
    plt.title("Valor Investidor por Segmento", fontsize=12, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.savefig("imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Valor_Investido")
    plt.show()

def gerar_analise_startup_segmento(dados):
    gerar_grafico_soma_valor_estimado(dados)
    gerar_grafico_total_investimento_anual(dados)
    gerar_tabela_quantidade_startup_por_segmento(dados)
    gerar_tabela_valor_investido_por_segmento(dados)
