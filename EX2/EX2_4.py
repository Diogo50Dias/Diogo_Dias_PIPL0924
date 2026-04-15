''' --- DiogoDias - Exercicio 2_4 --- '''

# Recebe saldo e valor do cheque
saldo = float(input("Saldo: "))
cheque = float(input("Valor do cheque: "))

# Verifica se pode descontar
if cheque <= saldo:
    saldo -= cheque
    print("Cheque descontado, saldo:", saldo)
else:
    print("Cheque não pode ser descontado")