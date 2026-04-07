from modelos.restaurante import Restaurante

restaurante_praca   = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Luisa', 7)
restaurante_praca.receber_avaliacao('Paulo', 5)

restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__': 
    main()