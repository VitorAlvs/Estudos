#1
class Veiculo:
    def __init__(self, marca, modelo):
        self._marca     = marca
        self._modelo    = modelo
        self._ligado    = False
    #2
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Estado: {self.estado}'
    
    @property
    def estado(self):
        return 'Ligado' if self._ligado else 'Desligado'
    
#3
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas    = portas

    #4
    def __str__(self):
        info_pai = super().__str__()
        return f'{info_pai} | Portas: {self._portas}'
    
#5
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    #6
    def __str__(self):
        info_pai = super().__str__()
        return f'{info_pai} | Tipo: {self._tipo}' 