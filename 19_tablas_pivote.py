import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# extraer de los datos subtablas donde apreciar caracteristicas

Tabla = pd.DataFrame({
    'tipo': ['moto', 'auto', 'moto', 'moto', 'auto', 'auto', 'moto', 'moto'],
    'velocidad': [12, 23, 34, 26, 43, 21, 28, 30],
    'propietario': ['Juan', 'Jorge', 'Maria', 'Ana', 'Juan', 'Maria', 'Bob', 'Camilo'],
    'nuevo': ['si', 'no', 'no', 'si', 'no', 'si', 'si', 'no'],
    'precio': [5000, 6000, 7500, 5500, 8000, 4000, 6500, 10000]
})

print(Tabla)
print(Tabla.pivot_table(index='tipo', columns='nuevo', values='precio', aggfunc='mean'))
print(Tabla.pivot_table(index='tipo', columns='nuevo', values='velocidad', aggfunc='min'))
print(Tabla.pivot_table(index='tipo', columns='nuevo', values='velocidad', aggfunc='count'))
print(Tabla.pivot_table(index='propietario', columns='tipo', values='velocidad', aggfunc='count').fillna(0))



