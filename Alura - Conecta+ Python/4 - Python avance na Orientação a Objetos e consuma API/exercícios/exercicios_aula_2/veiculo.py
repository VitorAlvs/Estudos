#1
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    #2
    def __init__(self, marca, modelo):
        self._marca     = marca
        self._modelo    = modelo

#3
class Carro(Veiculo):
    
    #4
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def ligar(self):
        pass