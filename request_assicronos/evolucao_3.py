from asyncio import run, gather
from aiometer import run_all
from httpx import AsyncClient
from pokes import pokes
from rich import print

# pokes = ['bulbasaur', 'charmander', 'squirtle']

# ele apre a conexao do get e faz os requests para aquele soquete

async def evolutin(poke):
    async with AsyncClient(base_url='https://pokeapi.co/api/v2/') as client:
        # -> pega o id do pokemom
        print(f'request 1: [b][red]{poke}[/]') 
        response = await client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')

        # -> pega a url da evolução do pokemon
        print(f'request 2: [b][green]{poke}[/]') 
        response = await client.get(f'/pokemon-species/{id_}')
        evolution = response.json().get('evolution_chain').get('url')


        # -> pega o nome da evolução
        print(f'request 3: [b][blue]{poke}[/]') 
        response = await client.get(evolution)
        evolution_name = (
            response
            .json()
            .get('chain')
            .get('evolves_to')[0]
            .get('species')
            .get('name')
        )
        print(f'Evolucao de {poke} -> é {evolution_name}')


async def main():
    result = gather(*[evolutin(poke) for poke in pokes])

    await result

run(main())