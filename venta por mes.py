import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv("ventas.csv")
df.groupby ("mes") ["ventas"].sum().plot (kind = "bar", title = "Total de Vendas por Mês")
plt.show()

