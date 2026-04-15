''' --- DiogoDias - Exercicio 2_5 --- '''

# Recebe três números
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

# Coloca numa lista
numeros = [num1, num2, num3]

# Ordena crescente
crescente = sorted(numeros)

# Ordena decrescente
decrescente = sorted(numeros, reverse=True)

# Mostra resultados
print("Crescente:", crescente)
print("Decrescente:", decrescente)