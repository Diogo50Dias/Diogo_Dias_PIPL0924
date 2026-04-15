''' --- DiogoDias - Exercicio 2_7 --- '''

# Recebe notas
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

# Calcula média ponderada
media = (nota1*2 + nota2*3 + nota3*5) / 10

# Mostra média
print("Média:", round(media, 1))

# Verifica aprovação
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")