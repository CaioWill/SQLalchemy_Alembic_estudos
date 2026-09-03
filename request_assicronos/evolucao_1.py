from httpx import Client

poke = 'eevee'

with Client(base_url='https://pokeapi.co/api/v2/') as client:
    # request 1 -> pega o id do pokemom
    response = client.get(f'/pokemon/{poke}')
    id_ = response.json().get('id')

    #request 2 -> pega a url da evolução do pokemon
    response = client.get(f'/pokemon-species/{id_}')
    evolution = response.json().get('evolution_chain').get('url')

    print(evolution)

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

    print(evolution_name)