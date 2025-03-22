import numpy as np

# hacer un array y dimensionarlo
A = np.linspace(1, 36, 36)
A.reshape(6,6)
print(A)

# suma, resta, multiplicacion
a = np.array([2, 3, 6])
b = np.array([4, 7, 9])

c = a + b
print(c)
c = np.add(a, b)
print(c)

d = a - b
d = np.subtract(a, b)
print(d)

e = a*b
e = np.multiply(a, b)
print(e)

f = a/b
f = np.divide(a, b)
print(f)

g = 3*a
print(g)

M = np.array([1, 2, 3, 4])
N = np.power(M, 3)
print(M, N)
print(np.log(N))
print(np.sqrt(N))

# radianes, no en grados
print(np.sin(N))
print(np.cos(N))
print(np.tan(N))

# operaciones estadisticas
r = np.random.random([5])
print(r)
print(np.mean(r))
print(np.median(r))
print(np.std(r))
print(np.max(r))
print(np.min(r))
