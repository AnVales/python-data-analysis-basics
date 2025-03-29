import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Datos = pd.DataFrame({'Matematica': [10, 8, 7],
                      'Fisica': [6, 5, 9],
                      'Programacion': [7, 9, 10]},
                     index= ['Pepito', 'Ana', 'Maria'])

print(Datos)

matematica = Datos['Matematica']
print(matematica)

# funciom
def restaruno(n):
    return n-1

print(matematica.apply(restaruno ))

print(Datos.applymap(restaruno))

def promedio(lista):
    return sum(lista)/len(lista)

print(Datos.apply(promedio, axis = 1)) # media por estudiante

print(Datos.agg([min, max, promedio], axis = 1))
print(Datos.agg([min, max, promedio], axis = 0))