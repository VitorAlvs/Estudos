from modelos.restaurante import Restaurante

restaurante_praca   = Restaurante('praça', 'gourmet')
restaurante_bubble  = Restaurante('bubble', 'Frutos do Mar')
restaurante_leaf    = Restaurante('Leaf', 'vegana')

restaurante_bubble.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__': 
    main()