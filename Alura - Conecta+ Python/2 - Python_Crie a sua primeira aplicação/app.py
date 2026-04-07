import os

restaurantes = [{'nome': 'Sushi House',     'categoria': 'Japonesa',        'estado': False},
                {'nome': 'Lasagna Man',     'categoria': 'Italiana',        'estado': True},
                {'nome': 'Coffee Poarch',   'categoria': 'Café da manhã',   'estado': True}]

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)

    print(linha)
    print(texto)
    print(linha)

    print()

def finalizar_programa():
    exibir_subtitulo('Finalizando app')

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante         = input('Digite o nome do restaurante: ')
    categoria_do_restaurante    = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante        = {'nome': nome_do_restaurante,   'categoria': categoria_do_restaurante,   'estado': False}
    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso')

    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('R̲e̲s̲t̲a̲u̲r̲a̲n̲t̲e̲s̲')

    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Estado')

    for each in restaurantes:
        nome        = each['nome']
        categoria   = each['categoria']
        ativo       = 'Ativado' if each['estado'] else 'Desativado'
        print(f'.{nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternado estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')

    restaurante_encontrado = False

    for each in restaurantes:
        if each['nome'] == nome_restaurante:
            restaurante_encontrado = True
            each['estado'] = not each['estado']

            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if each['estado'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                print('Ativar restaurante')
                alternar_estado_restaurante()
            case 4:
                print('Finalizar app')
                finalizar_programa()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


main()