#1
informacoes_pessoais = [{'nome': 'Maria do Carmo',  'idade': 67, 'cidade': 'Salvador'},
                        {'nome': 'Pablo Picasso',   'idade': 45, 'cidade': 'Lisboa'},
                        {'nome': 'Marisa Monte',    'idade': 73, 'cidade': 'Rio'}]

#2
informacoes_pessoais[1]['idade'] = 46
informacoes_pessoais[1]['Profissão'] = 'Pintor'
informacoes_pessoais[2]['cidade'] = ''

#3
quadrados = []

for each in range(1, 6):
    dic = {each: each**2}
    quadrados.append(dic)

#4
restaurantes = {'nome': 'Sushi House',     'categoria': 'Japonesa',        'estado': False}

if 'nome' in restaurantes:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

#5
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)