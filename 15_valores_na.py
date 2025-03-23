import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s1 = pd.Series([1, np.nan, 3, np.nan, 5])
print(s1)

df4 = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [3, 2, 5, 5], 'C': [np.nan, 7, np.nan, 2]}, index=['Ene', 'Feb', 'Mar', 'Abr'])
print(df4)

# print(s1.isnull())
# print(pf4.isnull())

# quitar valores nulos
s2 = s1.dropna()
print(s2)

df5 = df4.dropna(axis=1) # elimina las filas/columnas con na
print(df5)

df6 = df4.dropna(how='any') #elimina si tiene al menos un valor nulo
print(df6)

df7 = df4.fillna(0) # los valores nulos se rellenan de 3
print(df7)

# rellena con valor anterior que no es nulo
s2 = s1.fillna(method='ffill')
print(s2)

# rellena con el siguiente valor que no es nulo
s3 = s1.fillna(method='bfill')
print(s3)

# reemplazar con 0 los valores na
df8 = df4.fillna(0)
print(df8)

# se reemplazan los na por los anteriores pero tiene que haber un valor anterior
df9 = df4.fillna(axis=1, method='ffill')
print(df9)