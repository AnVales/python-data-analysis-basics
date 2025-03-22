import matplotlib.pyplot as plt
import numpy as np

# scatter plot, diagrama de dispersión de puntos
x = np.random.random([50])
y = np.random.random([50])
print(x)

#plt.scatter(x, y)
#plt.show()

# bar plot
opciones= ["si", "no"]
resultados = [40, 50]

#plt.barh(opciones, resultados)
#plt.show()

# histogramas
x = np.random.random([50])
print(x)

#plt.hist(x, 20) #por defecto son 10
#plt.show()

# boxplot
plt.boxplot(x)
plt.show()

# pie plot
plt.pie(resultados, labels=opciones)
plt.show()
