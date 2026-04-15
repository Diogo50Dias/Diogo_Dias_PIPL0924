# DiogoDias - Exercicio 1_9

# Exemplo
requisicao = {"metodo": "POST", "conteudo": ""}

# Analisa requisição
match requisicao["metodo"]:
    case "GET":
        print("Requisição GET recebida")
    case "POST" if requisicao["conteudo"]:
        print("Requisição POST com dados válidos")
    case "POST":
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")