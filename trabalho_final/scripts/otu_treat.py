import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(19)

def raref(otu_table):
    print(f"\nIniciando rarefação")
    
    minsum = otu_table.sum(axis = 0).min()

    reads = otu_table.T.values

    tot = (otu_table.sum(axis = 0)).to_numpy().reshape(-1, 1)

    prob = reads / tot
    prob = pd.DataFrame(prob.T,
                        columns = [chr(65 + i) for i in range(26)],
                        index = [f'OTU_{n}' for n in range(1, 101)]
                        )
    
    rf_table = pd.DataFrame(np.zeros((100, 26)).astype(int),
                            columns = [chr(65 + i) for i in range(26)],
                            index = [f'OTU_{n}' for n in range(1, 101)]
                            )
    rf_table.index.name = 'OTU'

    print("\nTempo estimado: 5 minutos\n")
    for col in rf_table.columns:
        rf_column = rf_table[col]
        prob_column = prob[col]
        print(f"Trabalhando com a coluna {col}...")
        while rf_column.sum() < minsum:
            idx = np.random.choice(rf_column.index,
                                   p = prob_column,
                                   replace = True
                                   )
            rf_column[idx] += 1
    
    rf_table.to_csv('otu_table_rf.tsv', sep = '\t', header = True)

    print (rf_table.sum(axis = 0))
    print(f'''\nRarefação concluída. Veja acima a soma de reads por amostra
'otu_table_rf.tsv' salva com sucesso em:
{os.getcwd()}''')

    return rf_table


def tss(df, s:int):
    print(f'''\nIniciando a normalização por Total Sum Scaling (TSS),
utilizando {s} como fator de escala''')
    
    otu_array = df.values.T
    tot = (df.sum(axis = 0)).to_numpy().reshape(-1, 1)
    otu_tss = (otu_array * s) / tot

    otu_table_tss = pd.DataFrame(otu_tss.T.astype(int),
                                 columns = [chr(65 + i) for i in range(26)],
                                 index = [f'OTU_{n}' for n in range(1, 101)]
                                 )
    otu_table_tss.index.name = 'OTU'

    colsum = pd.DataFrame(otu_table_tss.sum(axis = 0))
    print(colsum)

    otu_table_tss.to_csv('otu_table_tss.tsv', sep = '\t', header = True)

    print(f'''\nNormalização concluída.
Veja acima os totais de reads por amostra resultantes.
Tabela 'otu_table_tss.tsv' salva com sucesso em:
{os.getcwd()}''')

    return otu_table_tss


def collector(otu_table, trat:chr):
    print(f'''\nIniciando curvas do coletor para amostras da tabela {trat}''')
    
    maxreads = otu_table.sum(axis = 0)
    
    reads = otu_table.T.values
    tot = (otu_table.sum(axis = 0)).to_numpy().reshape(-1, 1)
    prob = reads / tot
    prob = pd.DataFrame(prob.T,
                        columns = [chr(65 + i) for i in range(26)],
                        index = [f'OTU_{n}' for n in range(1, 101)]
                        )
    
    spp = otu_table.index.values
    
    triples = []
    
    print("\nTempo estimado: 2 minutos\n")
    for col in prob.columns:
        prob_col = prob[col]    
        print(f"Trabalhando com a coluna {col}...")
        for n in range(0, maxreads.loc[col], 500):
            ms = []
            for rep in range(10):
                s = len(
                        set(
                            np.random.choice(spp,
                                             size = n,
                                             p = prob_col,
                                             replace = True
                                             )
                            )
                        )
                ms.append(s)
            triples.append([n, col, np.mean(ms)])
    
    curve = pd.DataFrame(triples,
                         columns = ["Nº de reads amostradas", "Amostra", "Riqueza média"]
                         )
             
    curve.to_csv(f'collectors_curve_{trat}.tsv', sep = '\t', header = True)
    
    return curve
    
    print(f'''\nCurvas do coletor geradas com sucesso.
Dados armazenados no arquivo 'collectors_curve_{trat}.tsv', salvo em:
{os.getcwd()}''')


def plot_collector(df, trat:chr):
    # df: pandas DataFrame gerada pela função collector
    sns.lineplot(data = df,
                 x = "Nº de reads amostradas",
                 y = "Riqueza média",
                 hue = "Amostra",
                 legend = False,
                 palette=["black"] * df["Amostra"].nunique())
    plt.title(f"Curva do coletor - tabela {trat}")
    plt.savefig(f"curva_coletor_{trat}.svg", dpi = 1200)
    plt.close()
    print(f'''\nO gráfico com as curvas do coletor para a tabela {trat}
foi salvo como 'curva_coletor_{trat}.svg' em
{os.getcwd()}''')
