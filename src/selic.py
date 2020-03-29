import requests
import pandas as pd


def get_selic(data_base):
    # getting selic base
    r = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
    base = r.json()
    df_selic = pd.DataFrame(base)
    df_selic['data'] = pd.to_datetime(df_selic['data'], format="%d/%m/%Y")
    df_selic['valor'] = df_selic['valor'].astype('float')

    # Most recent selic rate before the date of initial investment
    max_date = (df_selic['data'].loc[(df_selic['data'] == df_selic[df_selic['data'] <= data_base]['data'].max())])
    max_rate = float(df_selic['valor'].loc[(df_selic['data'] == df_selic[df_selic['data'] <= data_base]['data'].max())])

    return max_rate, (max_date.item())
