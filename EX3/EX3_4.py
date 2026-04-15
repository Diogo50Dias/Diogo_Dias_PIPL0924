''' --- DiogoDias - Exercicio 3_4 --- '''

numero = int(input("Digite um número: "))

primo = True

if numero <= 1:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print("Número Primo")
else:
    print("Não é Primo")