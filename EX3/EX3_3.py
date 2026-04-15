''' --- DiogoDias - Exercicio 3_3 --- '''

soma = 0

# Ler 10 notas
for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    soma += nota

# Calcula média
media = soma / 10

print("Média:", media)