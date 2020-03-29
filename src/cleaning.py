import pandas as pd
from datetime import datetime

def cleaning_base(base_ativos: pd.DataFrame):

    # Removing empty columns
    base_ativos.dropna(axis='columns', inplace=True)
    base_ativos["preco"].replace({"R[$]": "", "[\s*]": "", "[\.]": "", "[,]": "."}, inplace=True, regex=True)

    base_ativos['vencimento'] = pd.to_datetime(base_ativos['vencimento'], format="%d/%m/%Y")

    # Day D
    base_ativos = base_ativos.append(
        {'Ativo': 'ativo', 'vencimento': datetime.strptime('01/08/2020', "%d/%m/%Y"), 'preco': '-300000'},
        ignore_index=True)
    base_ativos["preco"] = base_ativos["preco"].astype("float")
    base_ativos['Ativo'] = 'ativo'
    # Grouping for data
    base_ativos = base_ativos.groupby(['Ativo', 'vencimento'], as_index=False).agg({'preco': 'sum'})

    # setting the position based on the number of calendar days
    base_ativos['posicao'] = (base_ativos['vencimento'] - base_ativos['vencimento'].min()).dt.days.astype('int64')

    return base_ativos