from datetime import date

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, registry


engine = create_async_engine('postgresql+psycopg://app_user:senha123@localhost:5432/sqlalchemy')

reg = registry()



@reg.mapped_as_dataclass
class Test:
    __tablename__ = 'test'

    id: Mapped[int] = mapped_column(init= False, primary_key= True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    criacao: Mapped[date] = mapped_column(init= False, server_default= func.now())

Test(nome='tony', email='tony@gmail.com')

async def main():

    async with AsyncSession(engine) as s:

        result = await s.scalar(select(Test).where(Test.id==1))
        print(result)

from asyncio import run

run(main())