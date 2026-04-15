''' --- DiogoDias - Exercicio 2_8 --- '''

# Lista para guardar notas
notas = []

# Lê 10 notas
for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

# Calcula média
media = sum(notas) / len(notas)

# Conta notas acima ou iguais à média
contador = 0
for nota in notas:
    if nota >= media:
        contador += 1

# Mostra resultados
print("Média:", round(media, 2))
print("Alunos acima ou iguais à média:", contador)