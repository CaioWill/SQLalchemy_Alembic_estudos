from asyncio import run, all_tasks, create_task, sleep, gather
from rich import print

async def ola(val):
    print(f'inicio da corrotia {val}')
    await sleep(1) # -> pausa a task e vai para o proximo na fila
    print(f'Meio da corrotina {val}')
    await sleep(1)
    print(f'Fim da corrotina {val}')

    return val

# loop de eventos ->

async def main():
    tasks = gather(
        *[ola(n) for n in range(30)]
    )

    print('Fila de tasks: ', all_tasks())

    result = await tasks # await -> para oque vc ta fazendo e espera essa tarefa terminar

    print('todas as tasks: ', all_tasks())
    print(result)

run(main()) # corrotina -> coisa que vai acontecer no futuro