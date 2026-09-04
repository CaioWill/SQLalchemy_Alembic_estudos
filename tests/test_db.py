from time_machine import travel
from datetime import datetime
from dataclasses import dataclass, field
from faker import Faker

db = []

@dataclass
class User:
    name: str
    creat_at: datetime = field(default_factory= datetime.now)


def creat_user(name:str) -> User:
    user = User(name)
    db.append(user)
    return user

@travel('2024-11-02', tick=False)
def test_creat_user():
    #arrange
    user_name = 'test'
    user = User(user_name)

    #acr
    resut = creat_user(user_name)

    # assert
    # assert resut.name == user_name
    assert resut == user




def tarefa_periodica():
    """Tarefa executada de hora em hora"""
    if datetime.now().hour == 21:
        print('Enviando relatorio!')
        return True
    else:
        print("coleta de dados")
        return True

@travel('2024-11-02 21:01')
def test_tarefa_periodica():

    # assert datetime.now().hour ==
    assert tarefa_periodica()


def test_faker(faker: Faker):
    fake_data= {
        'name' : faker.name(),
        'email': faker.email()
    }
    assert ...