# randomização de dados

from faker import Faker


fake = Faker(locale= 'PT_BR')


user = (
    fake.name(),
    fake.email(30),
    fake.date(),
    fake.city(),
    fake.cpf(),
    fake.cnpj(),
    fake.user_name(),
    fake.postcode(),
    fake.bank()
)
print('\n'.join(user))