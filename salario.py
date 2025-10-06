import pandas as pd
emp =  pd.read_csv("empleados.csv")
emp.groupby ("departamento") ["salario"].mean().round (2) 
print (emp)