import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# introduccion a las series de datos
Estudiantes = pd.Series([16, 12, 17], index=['Pepito', 'Maria', 'Ana'])
print(Estudiantes)

print(Estudiantes['Pepito'])
print(Estudiantes.index)
print(Estudiantes.values)

# introduccion a dataframes
Estudiantes = pd.DataFrame({'edades' :[16, 12, 17], 'escolaridad': ['s', 's', 'u'] }, index=['Pepito', 'Maria', 'Ana'])
print(Estudiantes.dtypes)
print(Estudiantes.axes)
print(Estudiantes.columns)