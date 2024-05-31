import numpy as np
import pandas as pd
from collections import Counter
import os

np.random.seed(19)

def otu_table(i:int, j:int, cellmax:int, minz:int, maxz:int):
    print(f'''\nIniciando geração de tabela de OTUs com {i} linhas e {j} colunas,
com cada coluna não excedendo 100.000 reads no total e contendo entre {minz} e {maxz}% de zeros'''
          )
    
    reads = [
             np.random.choice(range(0, cellmax + 1),
                              size = j,
                              p = [(z := np.random.randint(minz, maxz + 1) / 100)]
                                  + [(1 - z) / cellmax] * cellmax,
                              replace = True
                              )
             for n in range(1, i + 1)
             ]                     
             
    otu_table = pd.DataFrame(reads,
                             columns = [chr(65 + i) for i in range(26)],
                             index = [f'OTU_{n}' for n in range(1, 101)]
                             )
    
    otu_table.index.name = 'OTU'
                                   
    readsum = pd.DataFrame(otu_table.sum(axis = 0))
    
    checkzeros = {col: Counter(otu_table[col])[0] for col in otu_table.columns}
    
    print(f'''Tabela gerada com sucesso.

TOTAL DE READS POR COLUNA (AMOSTRA)
Média: {readsum.mean(axis = 0).loc[0]} 
Máximo: {readsum.max(axis = 0).loc[0]}
Mínimo: {readsum.min(axis = 0).loc[0]}
    
TOTAL DE ZEROS POR COLUNA (AMOSTRA)
    
Média: {np.mean(list(checkzeros.values()))}
Máximo: {np.max(list(checkzeros.values()))}
Mínimo: {np.min(list(checkzeros.values()))}''')
    
    otu_table.to_csv('otu_table_og.tsv', sep = '\t', header = True)
    
    print(f'''\notu_table_og.tsv' foi salva em:
{os.getcwd()}''')
    
    return otu_table
