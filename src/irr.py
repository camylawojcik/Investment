import decimal

# The irr will be calculated through a search algorithm
def npv_function(rate, cashflows):
    total = decimal.Decimal(0.0)
    for index, df_row in cashflows.iterrows():
        total += decimal.Decimal(df_row['preco']) / (1 + decimal.Decimal(rate)) ** decimal.Decimal(df_row['posicao'])
    return total

def calculate_irr(base_ativos, iterations=1000):
    if len(base_ativos) == 0:
        print('Dataframe is empty')
        return -1
    rate = decimal.Decimal(1.0)

    investment = base_ativos['preco'].min()
    for i in range(1, iterations + 1):
        # On each iteration we calculate the npv and compare it with the initial value of the investment
        # Based on result, we adjuste the rate to minimize this difference
        x = 1 - npv_function(rate, base_ativos) / decimal.Decimal(investment)
        rate = rate * x

    return rate