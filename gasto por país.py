import pandas as pd 
import matplotlib.pyplot as plt
cli = pd.read_csv("clientes.csv")
cli.groupby ("pais") ["gasto_total"].sum().plot(kind= "pie", autopct= "%1.1f%%", ylabel= "")
plt.show()
