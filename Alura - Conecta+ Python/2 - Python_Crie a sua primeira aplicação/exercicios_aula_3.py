#1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes   = ['Ricardo', 'Pâmela', 'Margarida']
anos    = [2005, 2026]

#2
lista_loop = [123, 'amêndoa', 12.6, 'abóbora']
for each in lista_loop:
    print(each)

#3
tres = 0
for each in range(0, 11):
    if (each % 2) != 0:
        tres += each
print(tres)

#4
um_a_dez = []
for each in range(0, 11):
    um_a_dez.append(each)
um_a_dez.sort(reverse=True)
for each in um_a_dez:
    print(each)

#5
numero = int(input('Digite um número: '))
for each in range (0, 11):
    print(f'{each} * {numero} = {each*numero}')

#6
numeros_soma = [1, 2, 3, 4, 's', 6, 7, 8, None, 10]
soma = 0
for each in numeros_soma:
    try:
        soma += each        
    except:
        pass
print(soma)

#7
lista_valores = [2, 4, 6, 8, 10]
soma_valores = 0

try:
    for each in lista_valores:
        soma_valores += each
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")