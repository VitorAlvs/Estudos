#Set - Eliminar repetições de itens
num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
fruta = "abacaxi"
carros = ("palio", "gol", "celta", "palio")

print(set(num))
print(set(fruta))
print(set(carros))

#conjunto
linguagens = {'python', 'java', 'python', 'php', 'php'}
print(linguagens)

#acessar valores de conjunto
numeros = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5}
numeros = list(numeros)
print(numeros[0])

#OPERAÇÕES------------------------------------------
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

#union
print(conjunto_a.union(conjunto_b))

#intersection
print(conjunto_a.intersection(conjunto_b))

#difference
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#symmetric difference
print(conjunto_a.symmetric_difference(conjunto_b))

#is subset
conjunto_c = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_c))
print(conjunto_c.issubset(conjunto_a))

#is upperset
print(conjunto_a.issuperset(conjunto_c))
print(conjunto_c.issuperset(conjunto_a))

#is disjoint
conjunto_d = {1, 2, 3, 4, 5}
conjunto_e = {6, 7, 8, 9}
conjunto_f = {1, 0}

print(conjunto_d.isdisjoint(conjunto_e))
print(conjunto_d.isdisjoint(conjunto_f))

#add
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

#clear
to_clear = {1, 23}
print(to_clear)
to_clear.clear()
print(to_clear)

#discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5 , 6, 7, 8, 9, 0}
print(numeros)
numeros.discard(1)
numeros.discard(45)
numeros.discard(5)
print(numeros)

#pop
numeros = {1, 2, 3, 1, 2, 4, 5, 5 , 6, 7, 8, 9, 0}
print(numeros)
numeros.pop()
numeros.pop()
print(numeros)

#remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5 , 6, 7, 8, 9, 0}
print(numeros)
numeros.remove(5)
print(numeros)

#len
numeros = {1, 2, 3, 1, 2, 4, 5, 5 , 6, 7, 8, 9, 0}
print(len(numeros))

#in
print(1 in numeros)
print(10 in numeros)