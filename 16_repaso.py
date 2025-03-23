import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# datos de:
# https://datos.bancomundial.org/indicador/SP.POP.TOTL
# API_SP.POP.TOTL_DS2_es_csv_v2_2688.csv

# leer los datos
dfpob = pd.read_csv('API_SP.POP.TOTL_DS2_es_csv_v2_2688.csv', skiprows= 3)
# print(dfpob.head())

# unq columna que nos relacione cada fila
dfpob.set_index('Country Code', inplace=True)
print(dfpob.head())

# seleccionar columnas a trabajar, solo queremos los años con nuestro indice
dfpob2=dfpob[[str(k) for k in range (1960, 2021)]]
print(dfpob2)

# elegir aquellas filas que nos interesan
paises={'MEX': 'México', 'PER': 'Perú', 'COL': 'Colombia', 'ESP': 'España'}
dfpob4 = dfpob2.loc[paises.keys()]
print(dfpob4)

# realizamos graficos 
plt.figure(figsize=(12,6))

for pais in paises.keys():
    plt.plot(dfpob4.loc[pais], label=paises[pais])

plt.legend()
plt.grid()

xvalues = np.arange(1960, 2021, 5)
xvalues = [str(k) for k in xvalues]

plt.xticks(xvalues)

plt.title("Crecimiento poblacional en diferentes países")
plt.xlabel('Años')
plt.ylabel('Población')
plt.xlim('1960','2020')
plt.show()

# como ha estado al inicio y al final
# grafico de barras

plt.figure(figsize=(12,6))
ancho_barras = 0.35
plt.grid(axis='y')
indice_barras = np.arange(4)
plt.bar(indice_barras, dfpob4['1960'], width=ancho_barras, label='1960')
plt.bar(indice_barras+ancho_barras, dfpob4['2020'], width=ancho_barras, label='2020')
plt.xticks(indice_barras+ancho_barras/2, [paises[p] for p in dfpob4.index])
plt.legend()
plt.title("Comparación de la población en 1960 y 2020")
plt.ylabel('Población')
plt.xlabel('Países')
plt.show()

# figura de tarta
plt.figure(figsize=(12, 6))
plt.pie(dfpob4['1960'], labels=paises.values(), shadow=True, autopct='%.1f%%')
plt.title("Comparación de la población en 1960")
plt.show()

plt.figure(figsize=(12, 6))
plt.pie(dfpob4['2020'], labels=paises.values(), shadow=True, autopct='%.1f%%')
plt.title("Comparación de la población en 2020")
plt.show()