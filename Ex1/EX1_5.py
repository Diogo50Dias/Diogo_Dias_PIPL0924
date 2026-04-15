# DiogoDias - Exercicio 1_5

# Recebe a mensagem
mensagem = input("Digite uma mensagem: ").lower()

# Analisa a mensagem
match mensagem:
    case "olá" | "ola" | "bom dia":
        print("Saudação")
    case _ if mensagem.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in mensagem or "adeus" in mensagem:
        print("Despedida")
    case _:
        print("Mensagem genérica")