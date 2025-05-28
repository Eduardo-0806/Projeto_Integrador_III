import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_media_de_crescimento(dados):
    #Preparação dos Dados

    growth_by_country = dados.groupby('Country')['Growth Rate (%)'].mean().sort_values(ascending=False)

    # Construção do gráfico
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x=growth_by_country.values, y=growth_by_country.index, palette='Blues_r')
    plt.title('Média de Porcentagem de Crescimento por País\n(Ordenado por Desempenho)', fontsize=14, pad=20)
    plt.xlabel('Média de Crescimento (%)', fontsize=12)
    plt.ylabel('País', fontsize=12)

    # Adicionar valores nas barras
    for i, value in enumerate(growth_by_country.values):
        ax.text(value + 0.5, i, f'{value:.1f}%', va='center', color='white', fontweight='bold')

    plt.tight_layout()
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Crescimento.png')
    plt.show()

def gerar_grafico_quantidade_investidores_pais(dados):

    #Preparação Dados
    plt.figure(figsize=(12, 8))
    investors_by_country = dados.groupby('Country')['Number of Investors'].sum().sort_values(ascending=False)

    # Construção Gráfico
    ax = sns.barplot(x=investors_by_country.values, y=investors_by_country.index, palette='Blues_r')
    plt.title('Total de Investidores por País\n(Ordenado por Volume)', fontsize=14, pad=20)
    plt.xlabel('Número Total de Investidores', fontsize=12)
    plt.ylabel('País', fontsize=12)

    # Destacar o país com maior número de investidores
    max_investors = investors_by_country.max()
    for i, value in enumerate(investors_by_country.values):
        color = 'gold' if value == max_investors else 'white'
        ax.text(value + 5, i, f'{value:,}', va='center', color=color, fontweight='bold')

    plt.tight_layout()
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_QTD_Investidores.png')
    plt.show()

def gerar_tabela_maior_investimento_pais(dados):
    
    #Preparação Dados
    max_invest_by_country = dados.groupby('Country')['Investment Amount (USD)'].max().sort_values(ascending=False)
    table_df_startup = max_invest_by_country.reset_index()
    table_df_startup.columns = ['País', 'Maior Investimento (USD)']
    table_df_startup['Maior Investimento (USD)'] = table_df_startup['Maior Investimento (USD)'].apply(lambda x: f"${x/1e6:.2f}M")

    total_valor = max_invest_by_country.sum()
    print(f"Valor calculado para TOTAL/MÉDIA: ${total_valor:,.2f}")
    total_row = pd.DataFrame([['TOTAL', f"${total_valor/1e6:.2f}M"]], columns=table_df_startup.columns)
    table_df_startup = pd.concat([table_df_startup, total_row], ignore_index=True)

    #Construção Tabela
    fig, ax = plt.subplots(figsize=(10, len(table_df_startup)*0.6))
    ax.axis('off')

    cell_colors = [['#1a3a5f', '#2a4a7f']] * (len(table_df_startup)-1) + [['#8a6bd1', '#8a6bd1']]
    table = ax.table(
        cellText=table_df_startup.values,
        colLabels=table_df_startup.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5']*2,
        cellColours=cell_colors
    )

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.5)

    # Destacar cabeçalho e total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(table_df_startup):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    plt.title('Maiores Investimentos por País', fontsize=16, color='white', pad=30)
    plt.tight_layout()
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Maior_Valor.png')
    plt.show()

def gerar_grafico_surgimento_startup_anual(dados):
    
    #Preparação Dados
    startups_by_year = dados['Year Founded'].value_counts().sort_index()

    #Construção Gráfico
    plt.figure(figsize=(12, 6))
    ax = sns.lineplot(
        x=startups_by_year.index, 
        y=startups_by_year.values, 
        marker='o', 
        markersize=8,
        linewidth=2.5,
        color='cyan'
    )

    # Configurações do gráfico
    plt.title('Evolução Anual de Fundação de Startups', fontsize=14, pad=20)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Número de Novas Startups', fontsize=12)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Surgimento_Startup.png')
    plt.show()

def gerar_analise_startup_pais(dados):
    gerar_grafico_media_de_crescimento(dados)
    gerar_grafico_quantidade_investidores_pais(dados)
    gerar_tabela_maior_investimento_pais(dados)
    gerar_grafico_surgimento_startup_anual(dados)
