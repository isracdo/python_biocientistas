Esta pasta contèm os arquivos relacionados ao trabalho final da disciplina "Introdução ao Python para Biocientistas"



A pasta "scripts" possui os arquivos de códigos

- main.py: arquivo que deve ser executado para realizar toda a análise do artigo produzido. Chama as funções contidas nos demais arquivos.

- alfadiv.py: define funções para cálculo da riqueza (s_table()) e dos índices de Shannon-Wiener (shannon()) e Pielou (jeveness()).
  Também define a função para comparar os índices de Shannon-Wiener entre dois tratamentos, com um teste T pareado por amostras (paired_t_test_shannon())

- generate_data.py: define a função otu_table, para gerar uma tabela de OTUs com abundâncias aleatórias, mas dimensões e porcentagem de zeros pré-definidas.

- otu_summary.py: define a função avg_std_table3, usada para obter a média e desvio-padrão do total de reads por amostra

- otu_trat.py: define funções para normalização e tratamento da tabela de OTUs: rarefação (raref()), Total Sum Scaling (TSS) (tss())
  e curva do coletor (collector()) (+ função para plotar as curvas: plot_collector())



A pasta "dados" contém arquivos .tsv gerados pelo script main.py

- collectors_curve_original.tsv: dados da curva do coletor para a tabela original (gerada pela função otu_table())

- collectors_curve_normalizada.tsv: dados da curva do coletor para a tabela normalizada por TSS (gerada pela função tss())

- collectors_curve_rarefeita.tsv: dados da curva do coletor para a tabela normalizada por rarefação (gerada pela função raref())

- otu_table_og.tsv: tabela de OTUs original (gerada pela função otu_table())

- otu_table_rf.tsv: tabela de OTUs rarefeita (gerada pela função raref())

- otu_table_tss.tsv: tabela de OTUs normalizada por TSS (gerada pela função tss())



A pasta "analysis" contém arquivos de imagem referentes às análises implementadas no script main.py

- boxplot_trat.svg: boxplot das somas de reads por amostra, para os três tratamentos (tabelas)

- curva_coletor_original.svg: da curva do coletor para a tabela original (gerada pela função plot_collector(collector_og, "original"))

- curva_coletor_rarefeita.svg: da curva do coletor para a tabela normalizada por rarefação (gerada pela função plot_collector(collector_rf, "rarefeita"))

- curva_coletor_normalizada.svg: da curva do coletor para a tabela normalizada por TSS (gerada pela função plot_collector(collector_tss, "normalizada"))


