# DiogoDias - Exercicio 1_6

# Dicionário de exemplo
servidor = {"status": "ok", "tempo_resposta": 350}

# Verifica estado
match servidor["status"]:
    case "ok" if servidor["tempo_resposta"] > 200:
        print("Servidor lento")
    case "ok":
        print("Servidor ativo")
    case "erro":
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")