from analises.analise_startup_segmento import gerar_analise_startup_segmento
from analises.analise_startup_pais import gerar_analise_startup_pais
from analises.analise_perfil import gerar_analise_perfil
import matplotlib.pyplot as plt
import pandas as pd

def run():
    df_startup_principal = pd.read_csv("data/startup_growth_investment_data.csv")
    df_perfil = pd.read_csv("data/Original_data.csv")

    plt.rcParams['axes.facecolor'] = '#5a8dc4'
    plt.rcParams['figure.facecolor'] = '#5a8dc4'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.edgecolor'] = 'white'

    gerar_analise_startup_segmento(df_startup_principal)
    gerar_analise_startup_pais(df_startup_principal)
    gerar_analise_perfil(df_perfil)
if __name__ == '__main__':
    run()
