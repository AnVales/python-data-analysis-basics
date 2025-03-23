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

df5 = df4.dropna(axis=1) # elimina las filas con na
print(df5)