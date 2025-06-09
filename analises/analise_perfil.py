import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def categorizar_idade(idade):
    """
    Retorna a faixa-etária conforme a idade passada

    :param idade: idade a ser avaliada
    :return: faixa-etaria da idade
    """
    if 20 <= idade <= 25:
        return '20-25'
    elif 26 <= idade <= 30:
        return '25-30'
    elif 31 <= idade <= 35:
        return '30-35'
    else:
        return 'Outros'

def gerar_grafico_analise_genero(dados):

    """
    Gera uma analise da distribuição de gênero dos perfis analisados e salva o gráfico de pizza com o resultado

    :param dados: DataFrame Pandas contendo os dados a serem trabalhados para geração da análise
    """

    #Preparação Dados
    distribuicao_genero = dados['GENDER'].value_counts()
    labels = distribuicao_genero.index
    sizes = distribuicao_genero.values

    #Construção Gráfico 
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=[f"{l}\n({v} - {v/sum(sizes)*100:.1f}%)" for l, v in zip(labels, sizes)],
        colors=['#5dade2', '#ec407a'], startangle=90)
    ax.set_title('Distribuição de Gênero')

    #Salvar e Mostrar Imagem
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Genero.png")
    plt.show()

def gerar_grafico_distribuicao_faixa_etaria(dados):
    """
    Gera uma analise da distribuição de faixa etária dos perfis analisados e salva o gráfico de barra com o resultado

    :param dados: DataFrame Pandas contendo os dados a serem trabalhados para geração da análise
    """

    #Preparação Dados
    dados['AGE'] = pd.to_numeric(dados['AGE'], errors='coerce')
    dados['Faixa Etária'] = dados['AGE'].apply(categorizar_idade)

    faixas_ordenadas = ['25-30', '30-35', '20-25']
    distribuicao_faixa_etaria = dados['Faixa Etária'].value_counts()
    distribuicao_faixa_etaria = distribuicao_faixa_etaria.reindex(faixas_ordenadas).fillna(0).astype(int)

    cores_faixa = ['#4dabf7', '#1e3d59', '#a3d5f7']
    labels = distribuicao_faixa_etaria.index
    valores = distribuicao_faixa_etaria.values

    #Construção Gráfico
    fig, ax = plt.subplots()

    ax.pie(valores, labels=[f"{v}\n({v/sum(valores)*100:.0f}%)" for v in valores],
        colors=cores_faixa, startangle=90)
    ax.legend(labels, title="Faixa Etária", loc="center left",
            bbox_to_anchor=(1, 0.5), fontsize=10)
    ax.set_title('Distribuição Faixa Etária')

    #Salvar e Mostrar Imagem
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Faixa_Etaria.png")
    plt.show()

def gerar_grafico_analise_objetivo(dados):
    """
    Gera uma analise da distribuição de objetivos dos perfis analisados e salva o gráfico de pizza com o resultado

    :param dados: DataFrame Pandas contendo os dados a serem trabalhados para geração da análise
    """
    #Preparação Dados
    distribuicao_objetivo = dados['What is your investment objective?'].value_counts()
    labels = distribuicao_objetivo.index
    sizes = distribuicao_objetivo.values

    #Construção Gráfico
    fig, ax = plt.subplots()
    cores_faixa = ['#4dabf7', '#1e3d59', '#a3d5f7']

    ax.pie(sizes, labels=[f"{l}\n({v} - {v/sum(sizes)*100:.1f}%)" for l, v in zip(labels, sizes)],
        colors=cores_faixa, startangle=90)
    ax.set_title('Objetivo do Investimento')

    #Salvar e Mostrar Imagem
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Objetivo.png")
    plt.show()

def gerar_grafico_analise_expectativa_retorno(dados):
    """
    Gera uma analise da distribuição de gênero dos perfis analisados e salva o gráfico de barra com o resultado

    :param dados: DataFrame Pandas contendo os dados a serem trabalhados para geração da análise
    """
    #Preparação Dados
    distribuicao_expectativa_retorno = dados['How much return do you expect from any investment instrument?'].value_counts()

    #Construção Gráfico

    fig, ax = plt.subplots()
    sns.barplot(y=distribuicao_expectativa_retorno.index, x=distribuicao_expectativa_retorno.values,
                ax=ax, palette='Blues_r')
    ax.set_title('Expectativa de Retorno')
    ax.set_xlabel('QTD')
    ax.set_ylabel('Retorno Esperado')

    #Salvar e Mostrar Imagem
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Expectativa_Retorno.png")
    plt.show()

def gerar_grafico_analise_fonte_informacao(dados):
    """
    Gera uma analise da distribuição de fontes de informação dos perfis analisados e salva o grafico de barra com o resultado 

    :param dados: DataFrame Pandas contendo os dados a serem trabalhados para geração da análise
    """
    #Preparação Dados
    distribuicao_fonte_informacao = dados['Your sources of information for investments is '].value_counts()

    #Construção Gráfico
    fig, ax = plt.subplots()
    sns.barplot(x=distribuicao_fonte_informacao.index, y=distribuicao_fonte_informacao.values,
                ax=ax, palette='Blues')
    ax.set_title('Fontes de Informação')
    ax.set_ylabel('QTD')
    ax.set_xlabel('Fonte')
    ax.tick_params(axis='x', rotation=25)

    plt.tight_layout()

    #Salvar e Mostrar Imagem
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Fonte_Informacao.png")
    plt.show()

def gerar_analise_perfil(dados):
    """
    Gera todas as analises de perfis, exibindo e salvando seus resultados

    :param dados: DataFrame Pandas contendo os dados a serem trabalhados para geração das análises
    """
    gerar_grafico_analise_genero(dados)
    gerar_grafico_distribuicao_faixa_etaria(dados)
    gerar_grafico_analise_objetivo(dados)
    gerar_grafico_analise_expectativa_retorno(dados)
    gerar_grafico_analise_fonte_informacao(dados)

