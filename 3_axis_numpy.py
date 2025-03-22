import numpy as np

A = np.array([7, 2, 9, 10])
print(A)

B = np.array([[5.2, 3.0, 4.5], [9.1, 0.1, 0.3]])
print(B)

# Eliminar y añadir elementos
C = np.delete(A, 1)
print(C)

D = np.delete(B, 0, axis = 1)
print(D)

# añadir, hay que tener cuidado con donde lo metes
E = np.append(B, [[6], [7]], axis = 1)
print(E)
