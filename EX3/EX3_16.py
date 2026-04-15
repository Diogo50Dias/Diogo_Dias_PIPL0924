''' --- DiogoDias - Exercicio 3_16 --- '''

contador = 0
soma = 0

while contador < 30:
    
    numero = int(input("Número entre 1 e 50: "))
    
    if numero >= 1 and numero <= 50 and numero % 2 == 0:
        soma += numero
        contador += 1

media = soma / 30

print("Média:", media)