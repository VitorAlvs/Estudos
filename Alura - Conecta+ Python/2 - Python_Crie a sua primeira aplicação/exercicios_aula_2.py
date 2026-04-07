#1
numero = int(input('Digite um número: '))
if numero%2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

#2
idade = int(input('Digite a sua idade: '))
if idade <= 12:
    print('Você é uma criança')
elif idade <= 18:
    print('Você é um adolescente')
else:
    print("Você é um adulto")

#3
usuario = 'jsantos'
senha   = 'Mudar@123'

def validar_usuario():
    usuario_input   = input('Digite seu usuário: ')
    if usuario_input != usuario:
        print('Usuário inválido, tente novamente.')
        validar_usuario()

def validar_senha():
    senha_input     = input('Digite sua senha: ')
    if senha_input != senha:
        print('Senha inválida, tente novamente.')
        validar_senha()

def login():
    validar_usuario()
    validar_senha()
    print('Login realizado com sucesso')

login()

#4
x = int(input("Insira a coordenada x: "))
y = int(input("Insira a coordenada y: "))

if (x>0) and (y>0):
    print('Primeiro Quadrante')
elif (x<0) and (y>0):
    print('Segundo Quadrante')
elif (x<0) and (y<0):
    print('Terceiro Quadrante')
elif (x>0) and (y<0):
    print('Quarto Quadrante')
else:
    print('Eixo ou Origem')