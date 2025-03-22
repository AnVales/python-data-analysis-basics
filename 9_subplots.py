import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)  # 200 puntos de 0 a 10
y1 = np.sin(x)
y2 = np.exp(x / 2)  # Ajuste para mejor visualización
y3 = np.power(x, 2)
y4 = np.cos(x)

fig, ax = plt.subplots(2, 2, figsize=(16, 9))  # Corrección aquí
fig.suptitle("Graficas de datos")
ax[0, 0].plot(x, y1, color='r')
ax[0, 0].set_title('Sen(x)', color='g')
ax[0, 0].grid()
ax[0, 0].set_xlabel('Eje x')
ax[0, 0].set_ylabel('Eje y')

ax[0, 1].scatter(x, y2)
ax[0, 1].set_title('Exp(x)')

ax[1, 0].plot(x, y3)
ax[1, 0].set_title('Pot(x)')

ax[1, 1].plot(x, y4)
ax[1, 1].set_title('Cos(x)')

plt.show()