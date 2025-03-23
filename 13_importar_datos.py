import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('Catalog_v2.xlsx')
print(df1.head())

df2 = pd.read_csv('Catalog_v2.csv', sep=',')
print(df2.head())

print(df2.shape)