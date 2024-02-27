a = input() 
b = input() 
c = input() 

vertebrado = {
    'ave' : {
        'carnivoro': 'aguia',
        'onivoro': 'pomba'
    },
    'mamifero' : {
        'onivoro': 'homem',
        'herbivoro': 'vaca'
    }
}

invertebrado = {
    'inseto': {
        'hematofago': 'pulga',
        'herbivoro': 'lagarta'
    },
    'anelideo': {
        'hematofago': 'sanguessuga',
        'onivoro': 'minhoca'
    }
}

def descobrir_animal(a, b, c):
    if a == 'vertebrado': 
        if b == 'ave':
            if c == 'carnivoro':
                return vertebrado['ave']['carnivoro']
            elif c == 'onivoro':
                return vertebrado['ave']['onivoro']
        elif b == 'mamifero':
            if c == 'onivoro':
                return vertebrado['mamifero']['onivoro']
            elif c == 'herbivoro':
                return vertebrado['mamifero']['herbivoro']
    elif a == 'invertebrado':
        if b == 'inseto':
            if c == 'hematofago':
                return invertebrado['inseto']['hematofago']
            elif c == 'herbivoro':
                return invertebrado['inseto']['herbivoro']
        elif b == 'anelideo':
            if c == 'hematofago':
                return invertebrado['anelideo']['hematofago']
            elif c == 'onivoro':
                return invertebrado['anelideo']['onivoro']


print(descobrir_animal(a, b, c))