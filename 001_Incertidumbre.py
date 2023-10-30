import numpy as np

# Calcular la probabilidad de obtener un número par al lanzar un dado justo de 6 caras
num_caras = 6
num_pares = 3  # Números pares en un dado de 6 caras: 2, 4, y 6
probabilidad_par = num_pares / num_caras

print(f"La probabilidad de obtener un número par es: {probabilidad_par:.2f}")

# Calcular la probabilidad de obtener un número impar
probabilidad_impar = 1 - probabilidad_par

print(f"La probabilidad de obtener un número impar es: {probabilidad_impar:.2f}")

# Calcular la probabilidad de obtener un número mayor o igual a 4
num_mayor_igual_4 = 3  # Números mayores o iguales a 4 en un dado de 6 caras: 4, 5, y 6
probabilidad_mayor_igual_4 = num_mayor_igual_4 / num_caras

print(f"La probabilidad de obtener un número mayor o igual a 4 es: {probabilidad_mayor_igual_4:.2f}")

# Calcular la probabilidad conjunta de obtener un número par y mayor o igual a 4
probabilidad_conjunta = (num_pares - 1) / num_caras  # Solo 4 y 6 son pares y mayores o iguales a 4

print(f"La probabilidad conjunta de obtener un número par y mayor o igual a 4 es: {probabilidad_conjunta:.2f}")
