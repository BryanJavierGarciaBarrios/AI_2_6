P_enfermedad = 0.01  # Probabilidad de tener la enfermedad antes de la prueba
P_no_enfermedad = 1 - P_enfermedad  # Probabilidad de no tener la enfermedad antes de la prueba
P_positivo_dado_enfermedad = 0.9  # Probabilidad de dar positivo en la prueba dado que tiene la enfermedad
P_positivo_dado_no_enfermedad = 0.1  # Probabilidad de dar positivo en la prueba dado que no tiene la enfermedad

# Calcular la probabilidad conjunta P(positivo y enfermedad)
P_positivo_y_enfermedad = P_enfermedad * P_positivo_dado_enfermedad

# Calcular la probabilidad conjunta P(positivo y no enfermedad)
P_positivo_y_no_enfermedad = P_no_enfermedad * P_positivo_dado_no_enfermedad

# Calcular la probabilidad marginal P(positivo) usando la regla de la suma
P_positivo = P_positivo_y_enfermedad + P_positivo_y_no_enfermedad

# Calcular la probabilidad condicional P(enfermedad|positivo) utilizando la Regla de Bayes
P_enfermedad_dado_positivo = P_positivo_y_enfermedad / P_positivo

# Imprimir el resultado
print(f"La probabilidad de tener la enfermedad dado un resultado positivo es: {P_enfermedad_dado_positivo:.4f}")
