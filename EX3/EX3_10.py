''' --- DiogoDias - Exercicio 3_10 --- '''

numero = int(input("Digite um número: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

print("Número de divisores:", divisores)