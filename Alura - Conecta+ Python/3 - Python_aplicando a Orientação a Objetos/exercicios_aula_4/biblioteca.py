#5
from modelos.livro import Livro

#2
livro_Les_Miserables    = Livro('Les Miserables', 'Victor Hugo', 1862)
livro_The_Hobbit        = Livro('The Hobbit', 'J.R.R. Tolklen', 1937)

#6
livro_Les_Miserables.emprestar()
print(livro_Les_Miserables.disponivel)

#7
Livro.verificar_disponibilidade(1937)
