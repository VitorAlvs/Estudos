def antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero +1
    return f"O antecessor de {numero} é {antecessor}, e seu sucessor é {sucessor}."

print(antecessor_e_sucessor(400))

# ********************************

def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([12, 24, 36]))

#*args recebe tuplas
#*kwargs recebe dicionários