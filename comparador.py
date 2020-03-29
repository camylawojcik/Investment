import pandas as pd
from src.cleaning import *
from src.irr import calculate_irr
from src.selic import get_selic
import os


def load_database():

    base_ativos = pd.read_csv('Ativos.csv', sep=';')

    return base_ativos

if __name__ == '__main__':

    base_ativos = load_database()

    base_ativos = cleaning_base(base_ativos)

    rate = calculate_irr(base_ativos)

    selic_rate, max_date = get_selic(base_ativos['vencimento'].min())

    print(f'IRR Rate:   {round(rate,6) *100}%')
    print(f'Taxa Selic {max_date}: {selic_rate}')

    print(f"Projeção de Taxa Selic Acumulada entre {base_ativos['vencimento'].min()} "
          f"- {base_ativos['vencimento'].max()}:   {selic_rate * base_ativos['posicao'].max()}%")