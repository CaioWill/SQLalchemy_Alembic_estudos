from asyncio import run, all_tasks, create_task, sleep
from rich import print

async def ola(val, delay):
    print(f'inicio da corrotia {val}')
    await sleep(delay) # -> pausa a task e vai para o proximo na fila
    print(f'Meio da corrotina {val}')
    await sleep(delay)
    print(f'Fim da corrotina {val}')


# loop de eventos ->

async def main():
    task1 = create_task(ola(1,10)) # corrotina
    task2 = create_task(ola(2,1)) # corrotina
    task3 = create_task(ola(3,1)) # corrotina
    task4 = create_task(ola(4,1)) # corrotina

    print('Fila de tasks: ', all_tasks())

    await task1 # await -> vai para a proxima corrotina enquando espera a resposta do request
    await task2 
    await task3
    await task4

    print('todas as tasks: ', all_tasks())

run(main()) # corrotina -> coisa que vai acontecer no futuro