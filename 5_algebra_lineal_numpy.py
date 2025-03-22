import numpy as np

a = np.array([1, 2, 3])
b = np.array([5, 4, 2])
c = np.array([2, 5, 6])

print(a, b, c)

#multiplicacion de vectores
d = np.dot(a, b)
print(d)

# producto entre dos vectores
e = np.cross(a, b)
print(e)

# hacer una matriz
F = np.array([a, b, c])
print(F)

# inversa de una matriz
M = np.linalg.inv(F)
print(M)

# autovalores de una matriz
N = np.linalg.eigvals(M)
print(N)

# traza de una matriz, suma de la diagonal
o = np.trace(M)
print(o)

# cambiar filas por columnas, transponer
O = np.transpose(F)
print(O)

# resolver sistemas de ecuaciones lineales
A = np.array([[1, 2], [5, 4]])
b = np.array([3, 4])
print(np.linalg.solve(A, b))