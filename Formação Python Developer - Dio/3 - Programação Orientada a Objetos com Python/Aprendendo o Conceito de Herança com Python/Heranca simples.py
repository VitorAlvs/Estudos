import random

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print(f'Ligando o motor do veículo {self.cor} de {self.numero_rodas} rodas e de placa {self.placa}')

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    carregado = random.choice([0, 1]) 
    def _init__(self, carregado):
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} está carregado.')
    
moto = Motocicleta('preta', 'ABC-1234', 2)
moto.ligar_motor()

carro = Carro('branco', 'XYZ-9876', 4)
carro.ligar_motor()

caminhao = Caminhao('vermelho', 'DEF-4567', 6)
caminhao.ligar_motor()
caminhao.esta_carregado()   