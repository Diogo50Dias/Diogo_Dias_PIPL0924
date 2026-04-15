# DiogoDias - Exercicio 1_3

# Dicionário de exemplo
pedido = {"tipo": "venda", "valor": 250}

# Analisa o pedido
match pedido["tipo"]:
    case "compra":
        print(f"Compra de {pedido['valor']}€")
    case "venda":
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Pedido desconhecido")