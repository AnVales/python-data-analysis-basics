import matplotlib.pyplot as plt
import numpy as np

# tamaños, colores, estilos de lineas y marcadores
y = np.array([1, 4, 3, 17, 16, 7, 30, 25, 50])
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# indicar el tamaño
plt.figure(figsize=(12, 6))
# lo ponemos con cuadriculas
plt.grid()
# le ponemos marcadores "https://matplotlib.org/stable/api/markers_api.html!"
plt.plot(x, y, "*:", c="r", mfc="b", mec="g", ms=10)
plt.show()
