''' --- DiogoDias - Teste Final --- '''


# Função para verificar se número é primo
def verificar_primo(numero):  # Define função chamada verificar_primo que recebe numero
    
    if numero <= 1:  # Se número menor ou igual a 1
        return False  # Não é primo
    
    for i in range(2, numero):  # Loop de 2 até numero-1
        if numero % i == 0:  # Se número for divisível por i
            return False  # Não é primo
    
    return True  # Se não encontrou divisores, é primo


# Função para contar divisores
def contar_divisores(numero):  # Define função contar_divisores
    
    contador = 0  # Variável contador começa em 0
    
    for i in range(1, numero + 1):  # Loop de 1 até numero
        if numero % i == 0:  # Se numero for divisível por i
            contador += 1  # Soma 1 ao contador
    
    return contador  # Retorna total de divisores


# Função verificar número perfeito
def numero_perfeito(numero):  # Define função numero_perfeito
    
    soma = 0  # Variável soma começa em 0
    
    for i in range(1, numero):  # Loop de 1 até numero-1
        if numero % i == 0:  # Se for divisor
            soma += i  # Soma divisor
    
    return soma == numero  # Retorna True se soma igual ao número


# Função calculadora
def calculadora():  # Define função calculadora
    
    num1 = float(input("Número 1: "))  # Recebe primeiro número
    operacao = input("Operação (+ - * /): ")  # Recebe operação
    num2 = float(input("Número 2: "))  # Recebe segundo número
    
    if operacao == "+":  # Se operação for soma
        print("Resultado:", num1 + num2)  # Mostra soma
        
    elif operacao == "-":  # Se operação for subtração
        print("Resultado:", num1 - num2)  # Mostra subtração
        
    elif operacao == "*":  # Se operação for multiplicação
        print("Resultado:", num1 * num2)  # Mostra multiplicação
        
    elif operacao == "/":  # Se operação for divisão
        print("Resultado:", num1 / num2)  # Mostra divisão
        
    else:  # Caso operação inválida
        print("Operação inválida")  # Mostra erro


# Função tabuada
def tabuada():  # Define função tabuada
    
    numero = int(input("Número da tabuada: "))  # Recebe número
    limite = int(input("Até quanto: "))  # Recebe limite
    
    contador = 0  # Contador começa em 0
    
    for i in range(1, limite + 1):  # Loop até limite
        
        print(numero, "x", i, "=", numero * i)  # Mostra multiplicação
        
        contador += 1  # Soma 1 ao contador
        
        if contador == 20:  # Se chegou a 20 linhas
            
            continuar = input("Continuar? (s/n): ")  # Pergunta continuar
            
            if continuar != "s":  # Se não quiser continuar
                break  # Sai do loop
            
            contador = 0  # Reset contador


# Menu principal
while True:  # Loop infinito
    
    print("\n--- MENU ---")  # Mostra menu
    print("1 - Análise de números")  # Opção 1
    print("2 - Calculadora")  # Opção 2
    print("3 - Tabuada")  # Opção 3
    print("0 - Sair")  # Opção sair
    
    opcao = input("Escolha: ")  # Recebe opção
    
    
    if opcao == "1":  # Se escolher opção 1
        
        numero = int(input("Número entre 1 e 30000: "))  # Recebe número
        
        if numero < 1 or numero > 30000:  # Validação
            print("Número inválido")  # Mostra erro
            continue  # Volta ao menu
        
        contador = 0  # Contador
        
        for i in range(numero, 0, -1):  # Loop regressivo
            
            print("\nNúmero:", i)  # Mostra número
            
            if verificar_primo(i):  # Verifica primo
                print("Primo")  # Mostra primo
            else:
                print("Não primo")  # Não primo
            
            print("Divisores:", contar_divisores(i))  # Mostra divisores
            
            if numero_perfeito(i):  # Verifica perfeito
                print("Número perfeito")  # Mostra perfeito
            
            contador += 1  # Soma contador
            
            if contador == 10:  # Pausa de 10 em 10
                
                continuar = input("Continuar? (s/n): ")  # Pergunta
                
                if continuar != "s":  # Se não
                    break  # Sai
                
                contador = 0  # Reset
    
    
    elif opcao == "2":  # Opção calculadora
        calculadora()  # Chama função
    
    
    elif opcao == "3":  # Opção tabuada
        tabuada()  # Chama função
    
    
    elif opcao == "0":  # Opção sair
        break  # Sai do programa
    
    
    else:  # Opção inválida
        print("Opção inválida")  # Mostra erro