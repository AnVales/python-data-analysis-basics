import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# unir dos DataFrame
General = pd.DataFrame({'nombre': ['Pepito', 'Maria', 'Ana'],
                        'edades': [16, 12, 17],
                        'escolaridad': ['P', 'S', 'U']})

print(General)

Cursos = pd.DataFrame({'nombre': ['Maria', 'Ana', 'Pepito'],
                       'cursos': ['Math', 'Science', 'Data Science'],
                       'clasifications': [9, 8, 10],
                       'asistencias': [25, 24, 26]})

print(Cursos)

general_cursos = pd.merge(General[['nombre', 'edades']], Cursos[['nombre', 'asistencias']], on='nombre', how='inner')
print(general_cursos)

# Unir 2 DataFrames apilandolos, NO HACE EMPAREJAMIENTO DE CLAVES
general_cursos1 = pd.concat([General, Cursos], axis=1, ignore_index=True)
print(general_cursos1)
