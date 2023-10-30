# Probabilidad de tener la enfermedad (P(A))
prob_enfermedad = 0.02

# Probabilidad de dar positivo en la prueba dado que tiene la enfermedad (P(B|A))
prob_positivo_dado_enfermedad = 1.0

# Probabilidad de dar positivo en la prueba dado que no tiene la enfermedad (P(B|¬A))
prob_positivo_dado_no_enfermedad = 0.05

# Probabilidad de dar positivo en la prueba (P(B))
prob_positivo = (prob_positivo_dado_enfermedad * prob_enfermedad) + ((prob_positivo_dado_no_enfermedad) * (1 - prob_enfermedad))

# Probabilidad condicionada de tener la enfermedad dado un resultado positivo en la prueba (P(A|B))
prob_enfermedad_dado_positivo = (prob_positivo_dado_enfermedad * prob_enfermedad) / prob_positivo

print("Probabilidad de tener la enfermedad dado un resultado positivo en la prueba:", prob_enfermedad_dado_positivo)
