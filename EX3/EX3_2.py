''' --- DiogoDias - Exercicio 3_2 --- '''

# Ler 10 números
for i in range(10):
    numero = int(input(f"Número {i+1}: "))
    
    if numero % 2 == 0:
        print("Número Par")
    else:
        print("Número Ímpar")