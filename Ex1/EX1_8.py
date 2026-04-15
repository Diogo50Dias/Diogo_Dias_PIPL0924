# DiogoDias - Exercicio 1_8

# Recebe dados
operacao = input("Operação: ").lower()
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

# Executa operação
match operacao:
    case "soma":
        print(num1 + num2)
    case "subtrai":
        print(num1 - num2)
    case "multiplica":
        print(num1 * num2)
    case "divide":
        print(num1 / num2)
    case _:
        print("Operação inválida")