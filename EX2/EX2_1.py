''' --- DiogoDias - Exercicio 2_1 --- '''

# Recebe o valor em segundos
segundos = int(input("Digite os segundos: "))

# Calcula horas
horas = segundos // 3600

# Calcula minutos
minutos = (segundos % 3600) // 60

# Calcula segundos restantes
segundos_restantes = segundos % 60

# Mostra resultado
print(f"{horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s)")