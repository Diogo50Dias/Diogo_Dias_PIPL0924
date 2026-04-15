''' --- DiogoDias - Exercicio 2_Loop --- '''

pares = 0
impares = 0

# Lê 10 números
for i in range(10):
    num = int(input(f"Número {i+1}: "))
    
    # Verifica par ou ímpar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostra resultado
print("Pares:", pares)
print("Ímpares:", impares)