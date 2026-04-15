# DiogoDias - Exercicio 1_4

# Valor de teste
valor = [10, 20, 30]

# Verifica o tipo do valor
match valor:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case str() if valor.isnumeric():
        print("String numérica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Tipo desconhecido")