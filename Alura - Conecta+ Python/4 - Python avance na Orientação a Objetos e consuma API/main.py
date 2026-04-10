from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível no mundo da programação
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        
        for each in dados_json:
            if each['Company'] == restaurante:

                dados_restaurante.append({
                    'item': each['Item'],
                    'price': each['price'],
                    'description': each['description']
                })
        return {'Restaurante': restaurante, 'Cardápio': dados_restaurante}
    else:
        return {f'Erro: {response.status_code} - {response.text}'}
