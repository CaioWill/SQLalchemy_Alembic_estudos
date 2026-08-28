from datetime import date

from sqlalchemy import create_engine, func, select, insert
from sqlalchemy.orm import Mapped, mapped_column, registry, Session


engine = create_engine('postgresql+psycopg://app_user:senha123@localhost:5432/sqlalchemy')

reg = registry()



@reg.mapped_as_dataclass
class Test:
    __tablename__ = 'test'

    id: Mapped[int] = mapped_column(init= False, primary_key= True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    criacao: Mapped[date] = mapped_column(init= False, server_default= func.now())

Test(nome='tony', email='tony@gmail.com')


# Session se conecta com a engine automaticamente
with Session(engine) as s:
    # s.scalar(insert(Test).values(nome="tony", email="tony@gmail.com"))
    # s.commit()
    result = s.scalar(select(Test).where(Test.id==1))
    print(result)
    # esta pegando a linha com o nome will e enviando como objeto para test
    test = s.scalar(select(Test).where(Test.nome=='will'))
    #   scalar = so 1 objeto
    #   scalars = muitos objetos

    # alterando diretamente pelo objeto recebido
    test.nome = 'WILL LINDO'
    result = s.scalar(select(Test).where(Test.id==1))
    print(result)
    s.commit()