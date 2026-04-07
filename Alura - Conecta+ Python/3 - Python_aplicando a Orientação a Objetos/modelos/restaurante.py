from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome      = nome.title()
        self._categoria = categoria.upper()
        self._estado    = False
        self._avaliacao = []

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Estado'.ljust(20)}')
        for each in cls.restaurantes:
            print (f'{each._nome.ljust(20)} | {each._categoria.ljust(20)} | {each.estado}')

    @property
    def estado(self):
        return '✔' if self._estado else '✘'

    def alternar_estado(self):
        self._estado = not self._estado

    def receber_avaliacao(self, cliente, nota):
        pass