''' --- DiogoDias - Exercicio 2_6 --- '''

# Recebe dados
nome = input("Nome do cliente: ")
compra = float(input("Valor da compra: "))

# Calcula desconto
if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

# Calcula total
total = compra - desconto

# Mostra resultado
print("Nome:", nome)
print("Compra:", compra, "€")
print("Desconto:", desconto, "€")
print("Total a pagar:", total, "€")