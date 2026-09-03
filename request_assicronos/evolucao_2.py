from httpx import Client
from pokes import pokes as pokemons

# DEMORA 30 SEGUNDOS PARA PUXAR TODOS O POKEMONSSSS
# essa demora e ruim, eu mesmo n ia querer

def evolution(poke):

    print(f'Entrada: {poke}')

    with Client(base_url='https://pokeapi.co/api/v2/') as client:

        # request 1 -> pega o id do pokemom
        response = client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')


        #request 2 -> pega a url da evolução do pokemon
        response = client.get(f'/pokemon-species/{id_}')
        evolution = response.json().get('evolution_chain').get('url')


        # request 3 -> pega o nome da evolução
        response = client.get(evolution)
        evolution_name = (
            response
            .json()
            .get('chain')
            .get('evolves_to')[0]
            .get('species')
            .get('name')
        )
        print(f'Saida de {poke} -> é {evolution_name}')

for poke in pokemons:
    evolution(poke)