import matplotlib.pyplot as plt
import numpy as np

# funcion seno(x)
x = np.arange(0, 10, 0.1)
print("Del 0 al 10 en valores que difieren 0.1: ", x)

y = np.sin(x)
print("Los valores del seno de nuestros datos: ", y)

z = np.cos(x)

plt.grid()
plt.plot(x, y, label= 'sin(x)')
plt.plot(x, z)
plt.plot(x, y, label= 'cos(x)')
plt.legend()
plt.title("Mi primera grafica")
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.xlim(0,4)
plt.show()


