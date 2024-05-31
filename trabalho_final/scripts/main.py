import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter
from generate_data import otu_table
from otu_treat import raref, tss, collector, plot_collector
from otu_summary import avg_std_table3
from alfadiv import shannon, paired_t_test_shannon, s_table, jeveness

def main():
    np.random.seed(19)
    otu_table_og = otu_table(100, 26, 3990, 40, 75)
    
    otu_table_rf = raref(otu_table_og)
      
    otu_table_tss = tss(otu_table_og, 100000)
    
    summary, sums_trat = avg_std_table3(otu_table_og, otu_table_rf, otu_table_tss)
    sns.boxplot(data = sums_trat,
                x = "Tratamento",
                y = "Soma",
                palette = ['#808080', '#808080', '#808080'])
    plt.savefig("boxplot_trat.svg", dpi = 1200)
    print(f'''\nUm boxplot para a análise acima foi salvo como 'boxplot_trat.svg' em:
{os.getcwd()}''')
    plt.close()
    
    collector_og = collector(otu_table_og, "original")
    plot_collector(collector_og, "original")
    
    collector_rf = collector(otu_table_rf, "rarefeita")
    plot_collector(collector_rf, "rarefeita")

    collector_tss = collector(otu_table_tss, "normalizada")
    plot_collector(collector_tss, "normalizada")
    
    h_og = shannon(otu_table_og, "original")
    h_rf = shannon(otu_table_rf, "rarefada")
    h_tss = shannon(otu_table_tss, "normalizada")
   
    print(paired_t_test_shannon(h_og, "original", h_rf, "rarefada"))
    print(paired_t_test_shannon(h_og, "original", h_tss, "normalizada"))
    
    rich = s_table(otu_table_og, otu_table_rf, otu_table_tss)
    print(rich)
    
    pielou = jeveness(otu_table_og, h_og, otu_table_rf, h_rf, otu_table_tss, h_tss)
    print(pielou)

    print("\nFim do script")

if __name__ == '__main__':
    main()
