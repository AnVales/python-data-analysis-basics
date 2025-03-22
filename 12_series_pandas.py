import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Estudiantes = {'Felipe': 14, 'Diana': 15}
pd.Series(Estudiantes, index=['Felipe', 'Diana', 'Alejo'])
print(Estudiantes)

pd.Series(8, index=['a', 'b', 'c'])
A = np.array([[1, 2], [4, 6]])
print(A)
B = pd.DataFrame(A, index=['a', 'b'], columns=['col1', 'col2'])
print(B)