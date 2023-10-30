import random

# Datos de ejemplo
total_emails = 1000  # Número total de correos electrónicos
spam_emails = 300  # Número de correos electrónicos etiquetados como spam
non_spam_emails = total_emails - spam_emails  # Número de correos electrónicos no spam

# Calcular la probabilidad a priori de spam y no spam
prior_prob_spam = spam_emails / total_emails
prior_prob_non_spam = non_spam_emails / total_emails

print(f"Probabilidad a priori de Spam: {prior_prob_spam:.2f}")
print(f"Probabilidad a priori de No Spam: {prior_prob_non_spam:.2f}")

# Simular una muestra de correos electrónicos nuevos
sample_size = 50  # Tamaño de la muestra
new_emails = [random.choice(["spam", "non_spam"]) for _ in range(sample_size)]

# Clasificar los correos electrónicos basados en la probabilidad a priori
spam_count = new_emails.count("spam")
non_spam_count = new_emails.count("non_spam")

# Probabilidad condicional basada en la probabilidad a priori
conditional_prob_spam = spam_count / sample_size
conditional_prob_non_spam = non_spam_count / sample_size

print(f"\nProbabilidad condicional de Spam: {conditional_prob_spam:.2f}")
print(f"Probabilidad condicional de No Spam: {conditional_prob_non_spam:.2f}")
