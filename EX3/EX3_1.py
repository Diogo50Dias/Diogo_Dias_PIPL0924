''' --- DiogoDias - Exercicio 3_1 --- '''

# Mostra os 30 primeiros pares e ímpares
contador = 0
numero = 1

while contador < 30:
    if numero % 2 == 0:
        print("Par:", numero)
    else:
        print("Ímpar:", numero)
    
    numero += 1
    contador += 1