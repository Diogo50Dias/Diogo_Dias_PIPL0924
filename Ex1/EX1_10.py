# DiogoDias - Exercicio 1_10

# Recebe jogadas
jogador1 = input("Jogador 1: ").lower()
jogador2 = input("Jogador 2: ").lower()

# Determina resultado
match (jogador1, jogador2):
    case ("pedra", "tesoura"):
        print("Jogador 1 venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra"):
        print("Jogador 2 venceu")
    case ("papel", "tesoura"):
        print("Jogador 2 venceu")
    case ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _ if jogador1 == jogador2:
        print("Empate")
    case _:
        print("Jogada inválida")