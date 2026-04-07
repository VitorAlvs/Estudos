#1
class Carro:
    
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor    = cor
        self.ano    = ano

carro2 = Carro('Uno', 'Prata', '1995')

#2
class Restaurante:

    def __init__(self, nome, categoria, estado, tamanho):
        self.nome       = nome
        self.categoria  = categoria
        self.ativo      = False
        self.estado     = estado
        self.tamanho    = tamanho

restaurante_praca = Restaurante('Praça', 'Gourmet', 'SP', 'Médio')

#3
class Restaurante:

    def __init__(self, nome, categoria):
        self.nome        = nome
        self.categoria   = categoria
        self.estado      = False

restaurante_praca = Restaurante('Praça', 'Gourmet')

#4
class Restaurante:

    def __init__(self, nome, categoria):
        self.nome        = nome
        self.categoria   = categoria
        self.estado      = False
    
    def __str__(self):        
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça', 'Gourmet')
print(restaurante_praca)

#5
class Cliente:

    def __init__(self, nome, idade, altura, peso):
        self.nome   = nome
        self.idade  = idade
        self.altura = altura
        self.peso   = peso

cliente_Pedro   = Cliente('Pedro', 28, 1.80, 75)
cliente_Rodrigo = Cliente('Rodrigo', 17, 1.73, 64)
cliente_Carla   = Cliente('Carla', 34, 1.62, 55)