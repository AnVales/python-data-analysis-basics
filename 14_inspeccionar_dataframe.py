import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('Catalog_v2.csv', sep=',')
df1.set_index('levelType', inplace=True)
# print(df1.head())

# print(df1['code'])
# print(df1.loc['FAMILY']) # se busca por su index

# print(df1.iloc[2]) # Access group of rows and columns by integer position(s)

# rangos y filtrado de datos
print(df1.iloc[1:4]) # rango de filas
prod = df1[(df1['catalogType']=='PRODUCT') & (df1['name']=='Street Lighting')]
print(prod)


