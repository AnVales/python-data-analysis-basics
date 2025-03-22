# construir un array de 3 filas
import numpy as np
A = np.zeros([3, 4])
print(A)
print()

# la primera fila formada por 1, 2, 3, 4
A[0] = [1, 2, 3, 4]
print(A)
print()

# los elementos de la segunda fila son el triple de los de la primera
A[1]= 3*A[0]
print(A)
print()

# los elementos de la tercera fila son el cuadrado de los de la segunda fila
A[2] = (A[1])**2
print(A)
print()
# ¿cuántos elementos del array son impares?
I = A[(A%2!=0)]
print(I.shape)
