# DiogoDias - Exercicio 1_2

# Recebe a nota
nota = int(input("Digite a nota (0-100): "))

# Classifica a nota
match nota:
    case _ if nota >= 90:
        print("Excelente")
    case _ if nota >= 70:
        print("Bom")
    case _ if nota >= 50:
        print("Suficiente")
    case _ if nota < 50:
        print("Insuficiente")