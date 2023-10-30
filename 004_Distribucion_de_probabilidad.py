import numpy as np
import matplotlib.pyplot as plt

# Crear una distribución de probabilidad de un dado de seis caras
probabilidades = [1/6] * 6  # Se asume que todas las caras son igualmente probables

# Valores posibles del dado
valores = [1, 2, 3, 4, 5, 6]

# Generar una muestra aleatoria de la distribución
muestra = np.random.choice(valores, size=1000, p=probabilidades)

# Contar las frecuencias de los valores en la muestra
frecuencias = np.bincount(muestra)[1:]

# Crear un gráfico de barras para visualizar la distribución
plt.bar(valores, frecuencias / sum(frecuencias), tick_label=valores)
plt.title("Distribución de probabilidad de un dado de seis caras")
plt.xlabel("Valor en el dado")
plt.ylabel("Probabilidad")
plt.show()
