#1
class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo            = titulo
        self._autor             = autor
        self._ano_publicacao    = ano_publicacao
        self._disponivel        = True

        Livro.livros.append(self)

    #2
    def __str__(self):
        return f'{self._titulo}, de {self._autor} publicado em {self._ano_publicacao}'

    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Indisponível'

    #3
    def emprestar(self):
        self._disponivel = not self._disponivel

    #4
    @classmethod
    def verificar_disponibilidade(cls, ano):
        livros_disponiveis = []
        
        for each in cls.livros:
            if each._ano_publicacao == ano and each.disponivel:
                livros_disponiveis.append(each)
        
        return livros_disponiveis


#2
# livro_Les_Miserables    = Livro('Les Miserables', 'Victor Hugo', 1862)
# livro_The_Hobbit        = Livro('The Hobbit', 'J.R.R. Tolklen', 1937)
# print(livro_Les_Miserables)
# print(livro_The_Hobbit)

#3
# print(livro_Les_Miserables.disponivel)
# print(livro_The_Hobbit.disponivel)



