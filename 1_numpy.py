import numpy as np

# Creando arrays con numeros
A = np.array([1, 2, 3])
print(A)

B = np.array([[1, 2],[3, 4]])
print(B)

# Creando arrays con 0 y 1
C = np.zeros([3, 2])
print(C)

D = np.ones([3, 2])
print(D)

# Creando arrays como matriz unitaria
E = np.identity(5)
print(E)

# Creando arrays con numeros
F = np.array([1, 2, 3, 4, 5])
print(F)

# Creando arrays indicando de que se completan
G = np.arange(1, 11, 0.5)
print(G)

H = np.linspace(1, 10, 3)
print(H)

# Crear una matriz con numeros aleatorios
J = np.random.random([3, 2])
print(J)

# acceder a informacion de los array
print(A.ndim) # dimensiones de filas solo
print(A.shape)
print(A.dtype)

# acceder a elementos de un array y modificarlo
K = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(K[2, 1])
K[2,0] = 24
print(K)
print(K[:2,:2])

# FILTRADO DE ELEMENTOS
K = np.array([[1, 7, 3, 4], [2, 12, 4, 1], [2, 9, 7, 8]])
print(K[(K%2==0) & (K>4)])

