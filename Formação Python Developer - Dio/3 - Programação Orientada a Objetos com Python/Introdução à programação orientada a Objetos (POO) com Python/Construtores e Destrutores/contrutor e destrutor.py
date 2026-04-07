#Construtor
#É executado quando uma nova instância da classe é criada.
#Inicializamos o estado do objeto.
#__init__

class Doguito:
    def __init__(self, nome, raca, cor, acordado = True):
        self.nome       = nome
        self.raca       = raca  
        self.cor        = cor
        self.acordado   = True
    
#Destrutor
#É executado quando instância/objeto é destruído.abs    
    #Não é tão utilizado quanto em C++, pois o py tem um coletor de lixo que lida com o gerenciamento de memória automaticamente.abs
#__del__

class Cao:
    def __del__(self):
        print('Destruindo instância.')

c = Cao()
del c

################################################

class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe...")
        self.nome       = nome
        self.cor        = cor
        self.acordado   = True
    
    def __del__(self):
        print('Removendo a instância da classe.')
        
    def latir(self):
        print('auauau')

def criar_cachorro():
    c = Cachorro("Hades", 'Cinza', False)
    print(c.nome)

# c = Cachorro('Bob', 'preto')
# c.latir()

criar_cachorro()