import numpy as np
import pandas as pd
import os

np.random.seed(19)

def avg_std_table3(df1, df2, df3):
    print(f'''\nCalculando média e desvio-padrão dos totais de reads por amostra
para cada uma das três tabelas\n''')
    
    dfs = [df1, df2, df3]
    dfs = [w.sum(axis = 0) for w in dfs]
    sums = pd.concat(dfs, axis = 1)
    sums.columns = ['Original', 'Rarefada', 'Normalizada']
    summary = pd.concat([sums.mean(axis = 0), sums.std(axis = 0)], axis = 1)
    summary.columns = ['Média', 'Desvio-padrão']
    trat = sums.reset_index().rename(columns={'index': 'Letra'})
    trat = pd.melt(trat, id_vars = ['Letra'], var_name = 'Tratamento', value_name = 'Soma')
    trat = trat.set_index('Letra')
    print(summary)
    return summary, trat


