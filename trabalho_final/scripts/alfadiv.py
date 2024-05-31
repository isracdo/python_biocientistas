import numpy as np
import pandas as pd
import os
from scipy import stats

def shannon(pd_df, trat:chr):
    print(f"\nCalculando o índice de Shannon para cada amostra (coluna) da tabela {trat}")
    
    nsmpl = pd_df.shape[1]
    tot = (pd_df.sum(axis = 0)).to_numpy().reshape(-1, 1)
    otu_array = pd_df.values.T
    otu_prop = otu_array / tot
    otu_ln = np.log(otu_prop)
    h = otu_prop * otu_ln
    h = np.nan_to_num(h, nan = 0.0)
    h = h * -1
    shannon = pd.DataFrame(h.T.sum(axis = 0),
                           columns = [trat],
                           index = [chr(65 + i) for i in range(nsmpl)]
                           )
    return shannon

def boxplot_shannon(df1, df2, df3):
    dfs = [df1, df2, df3]
    h = pd.concat(dfs, axis = 1)
    h = h.reset_index().rename(columns={'index': 'Letra'})
    h = pd.melt(h, id_vars = ['Letra'], var_name = 'Tratamento', value_name = 'Índice de Shannon (H’)')
    h = h.set_index('Letra')
    sns.boxplot(data = h,
                x = "Tratamento",
                y = "Índice de Shannon (H’)",
                hue = "Tratamento",
                legend = False,
                palette = ['#707070', '#707070', '#707070'])
    plt.savefig("boxplot_shannon.svg", dpi = 1200)
    plt.close()


def paired_t_test_shannon(df1, name1:chr, df2, name2:chr):
    print(f'''\nUsando um um teste T pareado para comparar
os índices de Shannon de cada amostra (coluna)
das tabelas {name1} e {name2}\n''')
    
    t1, p1 = stats.shapiro(df1)
    if p1 >= 0.05:
        t2, p2 = stats.shapiro(df2)
        if p2 >= 0.05:
            ttest = stats.ttest_rel(df1, df2, axis = 0)
        else:
            print(f"\nOs dados da tabela {name2} DataFrame não seguem distribuição normal: p = {p2}") 
    else:
        print(f"\nOs dados da tabela {name1} não seguem distribuição normal: p = {p1}")
    return ttest


def s_table(df1, df2, df3):
    dfs = [df1, df2, df3]
    
    for i in range(0, 3):
        dfs[i][dfs[i] > 0] = 1
    
    dfs = [w.sum(axis = 0) for w in dfs]
    
    s_table = pd.concat(dfs, axis = 1)
    s_table.columns = ['Original', 'Rarefada', 'Normalizada']
    
    return s_table

def jeveness(df1, h1, df2, h2, df3, h3):
    dfs = [df1, df2, df3]
    s = ["s1", "s2", "s3"]
    logs = ["logs1", "logs2", "logs3"]
    h = [h1, h2, h3]
    j = ["j1", "j2", "j3"]
    
    for i in range(0, 3):
        dfs[i][dfs[i] > 0] = 1
        s[i] = dfs[i].sum(axis = 0)
        logs[i] = np.log(s[i])
        logs[i] = pd.DataFrame(logs[i],
                               columns = ["ln(s)"],
                               index = [chr(65 + i) for i in range(26)]
                               )
        j[i] = pd.DataFrame(h[i].values / logs[i].values,
                            index = [chr(65 + i) for i in range(26)]
                            )
    
    j_table = pd.concat(j, axis = 1)
    j_table.columns = ['Original', 'Rarefada', 'Normalizada']
    
    return j_table
