''' --- DiogoDias - Exercicio 3_12 --- '''

numero = int(input("Digite um número: "))
contador = 0

for i in range(1, numero):
    
    soma = numero + i
    sub = numero - i
    mult = numero * i
    div = numero / i
    
    contador += 4

print("Operações realizadas:", contador)