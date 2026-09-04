from dataclasses import dataclass
from datetime import date

# Schema
@dataclass
class Pessoa:
    nome: str
    email: str
    cpf: str
    password: str
    bhrirday: date


from factory import Factory, Faker

# Criação de um factory para criar um radom do Schema
class PessoaFactory(Factory):
    class Meta:
        model = Pessoa

    nome = Faker('name', locale = 'pt_br')
    email = Faker('email', locale = 'pt_br')
    cpf = Faker('cpf', locale = 'pt_br')
    password = Faker('password')
    bhrirday = Faker('date_object')

# para dados iguais so especificar quando fhamar a class
# PessoaFactory(name='test')

# PessoaFactory.build_batch(10) -> cria quantos for passado

print(PessoaFactory())
