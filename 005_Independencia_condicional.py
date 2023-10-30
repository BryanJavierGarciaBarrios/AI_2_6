# Definir las probabilidades de A, B y C
P_A = 0.3  # Probabilidad de A
P_B = 0.4  # Probabilidad de B
P_C = 0.2  # Probabilidad de C

# Definir las probabilidades condicionales P(A|C) y P(B|C)
P_A_dado_C = 0.5  # Probabilidad de A dado C
P_B_dado_C = 0.3  # Probabilidad de B dado C

# Calcular la probabilidad conjunta P(A y B|C) usando la independencia condicional
P_A_y_B_dado_C = P_A_dado_C * P_B_dado_C

# Calcular la probabilidad conjunta P(A|C) * P(B|C)
P_A_dado_C_x_P_B_dado_C = P_A_dado_C * P_B_dado_C

# Verificar la independencia condicional
son_independientes_condicionalmente = abs(P_A_y_B_dado_C - P_A_dado_C_x_P_B_dado_C) < 1e-6

# Imprimir el resultado
if son_independientes_condicionalmente:
    print("A y B son independientes dado C.")
else:
    print("A y B no son independientes dado C.")
