''' --- DiogoDias - Exercicio 3_18 --- '''

numero = int(input("Digite número: "))

soma = 0

for i in range(1, numero):
    if numero % i == 0:
        soma += i

if soma == numero:
    print("Número perfeito")
else:
    print("Não é perfeito")