# DiogoDias - Exercicio 1_1

# Recebe o dia da semana
dia = input("Digite um dia da semana: ").lower()

# Verifica se é dia útil ou fim de semana usando match
match dia:
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido")