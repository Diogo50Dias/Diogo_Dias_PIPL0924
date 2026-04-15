''' --- DiogoDias - Exercicio 3_15 --- '''

contador = 0

for i in range(256):
    
    print(i, "-", chr(i))
    contador += 1
    
    if contador == 20:
        continuar = input("Continuar? (s/n): ")
        
        if continuar.lower() != "s":
            break
        
        contador = 0