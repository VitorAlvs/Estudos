from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome      = nome.title()
        self._categoria = categoria.upper()
        self._estado    = False
        self._avaliacao = []
        self._cardapio  = []

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Estado'.ljust(20)}')
        for each in cls.restaurantes:
            print (f'{each._nome.ljust(20)} | {each._categoria.ljust(20)} | {str(each.media_avaliacoes).ljust(20)} | {each.estado}')

    @property
    def estado(self):
        return '✔' if self._estado else '✘'

    def alternar_estado(self):
        self._estado = not self._estado

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
                avaliacao = Avaliacao(cliente, nota)
                self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round((soma_das_notas/quantidade_de_notas),1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante: {self._nome}\n')
        for i, each in enumerate(self._cardapio, start = 1):
            if hasattr(each, 'descricao'):
                mensagem_prato = f'{i}. Nome: {each._nome} | Preço: R${each._preco} | Descrição: {each.descricao}' 
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {each._nome} | Preço: R${each._preco} | Descrição: {each._tamanho}' 
                print(mensagem_bebida)