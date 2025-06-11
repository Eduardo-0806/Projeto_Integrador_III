from analises.analise_startup_segmento import gerar_analise_startup_segmento, gerar_analise_startup_segmento_complementar
from analises.analise_startup_pais import gerar_analise_startup_pais, gerar_analise_startup_pais_complementar
from analises.analise_perfil import gerar_analise_perfil
import matplotlib.pyplot as plt
import pandas as pd

def run():
    
    #Importação dos Dados
    df_startup_principal = pd.read_csv("data/startup_growth_investment_data.csv")
    df_startup_complementar = pd.read_csv("data/global_startup_success_dataset.csv")
    df_perfil = pd.read_csv("data/Original_data.csv")

    #Configurações estéticas gerais dos gráficos gerados
    plt.rcParams['axes.facecolor'] = '#5a8dc4'
    plt.rcParams['figure.facecolor'] = '#5a8dc4'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.edgecolor'] = 'white'

    #Geração das Analises

    #Gera Analise Principal de Startup por Segmento Internacional e Nacional
    gerar_analise_startup_segmento(df_startup_principal, False)
    gerar_analise_startup_segmento(df_startup_principal, True)

    #Gera Analise Complementar de Startup por Segmento Internacional e Nacional
    gerar_analise_startup_segmento_complementar(df_startup_complementar,False)
    gerar_analise_startup_segmento_complementar(df_startup_complementar,True)

    #Gera Analise Principal de Startup por Pais
    gerar_analise_startup_pais(df_startup_principal)

    #Gera Analise Complementar de Startup por Pais
    gerar_analise_startup_pais_complementar(df_startup_complementar)

    #Gera Analise de Perfil
    gerar_analise_perfil(df_perfil)
if __name__ == '__main__':
    run()
