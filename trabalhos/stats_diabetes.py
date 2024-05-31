import pandas as pd
import numpy as np
from scipy import stats

np.random.seed(19)

df = pd.read_table("diabetes.tsv.gz",
                   sep = "\t",
                   header = "infer")


p = 1.0
diff = 0.0

print('''\nProcurando um grupo de 80 pessoas com glicemia acima de 126 mg/dL,
valor estabelecido pela diretriz da Sociedade Brasileira de Diabetes.''')

df_hi = df[df['blood sugar'] > 126]

while p >= 0.05:
    sub = df_hi.sample(80, replace = False)["blood sugar"]
    w, p = stats.wilcoxon(sub - 126)

print(f"\nEncontrado! A mediana do grupo é {sub.median(axis = 0)}")
print(f"\nAqui está a lista dos pacientes no grupo:")
print(sub)