class Restaurante:
    nome        = ''
    categoria   = ''
    estado      = False

restaurante_praca = Restaurante()
restaurante_praca.nome      = 'Praça'

#1
restaurante_praca.categoria = 'Italiana'

#2
print(restaurante_praca.nome)

#3
mensagem = f'O restaurante {restaurante_praca.nome} está ativo.' if restaurante_praca.estado else f'O restaurante {restaurante_praca.nome} está inativo.'
print(mensagem)

#4
categoria = Restaurante.categoria

#5
restaurante_praca.nome = 'Bistrô'

#6
restaurante_pizza = Restaurante()
restaurante_pizza.nome      = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

#7
mensagem2 = restaurante_pizza.categoria == 'Fast Food' 
print(mensagem2)

#8
restaurante_pizza.estado = not restaurante_pizza.estado

#9
print(f'{restaurante_praca.nome}\n{restaurante_praca.categoria}')